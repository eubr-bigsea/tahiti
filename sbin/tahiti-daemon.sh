#!/usr/bin/env bash

# This script controls the tahiti server daemon initialization, status reporting
# and termination
# TODO: rotate logs

usage="Usage: tahiti-daemon.sh (start|startf|stop|status)"

# this sript requires the command parameter
if [ $# -le 0 ]; then
  echo $usage
  exit 1
fi

# parameter option
cmd_option=$1

# set tahiti_home if unset
if [ -z "${TAHITI_HOME}" ]; then
  export TAHITI_HOME="$(cd "`dirname "$0"`"/..; pwd)"
fi
echo $TAHITI_HOME

# get log directory
if [ "$TAHITI_LOG_DIR" = "" ]; then
  export TAHITI_LOG_DIR="${TAHITI_HOME}/logs"
fi
mkdir -p "$TAHITI_LOG_DIR"

# get pid directory
if [ "$TAHITI_PID_DIR" = "" ]; then
  export TAHITI_PID_DIR=/tmp
fi
mkdir -p "$TAHITI_PID_DIR"

# log and pid files
log="$TAHITI_LOG_DIR/tahiti-server-$USER-$HOSTNAME.out"
pid="$TAHITI_PID_DIR/tahiti-server-$USER.pid"

case $cmd_option in

   (start)
      # set python path
      PYTHONPATH=$TAHITI_HOME:$PYTHONPATH nohup -- python $TAHITI_HOME/tahiti/runner/tahiti_server.py \
         -c $TAHITI_HOME/conf/tahiti-config.yaml >> $log 2>&1 < /dev/null &
      tahiti_server_pid=$!

      # persist the pid
      echo $tahiti_server_pid > $pid

      echo "Tahiti server started, logging to $log (pid=$tahiti_server_pid)"
      ;;

   (startf)
      trap "$0 stop" SIGINT SIGTERM
      # set python path
      PYTHONPATH=$TAHITI_HOME:$PYTHONPATH python $TAHITI_HOME/tahiti/runner/tahiti_server.py \
         -c $TAHITI_HOME/conf/tahiti-config.yaml &
      tahiti_server_pid=$!

      # persist the pid
      echo $tahiti_server_pid > $pid

      echo "Tahiti server started, logging to $log (pid=$tahiti_server_pid)"
      wait
      ;;

   (stop)

      if [ -f $pid ]; then
         TARGET_ID="$(cat "$pid")"
         if [[ $(ps -p "$TARGET_ID" -o comm=) =~ "python" ]]; then
            echo "stopping tahiti server, user=$USER, hostname=$HOSTNAME"
            (pkill -SIGTERM -P "$TARGET_ID" && \
               kill -SIGTERM "$TARGET_ID" && \
               rm -f "$pid")
         else
            echo "no tahiti server to stop"
         fi
      else
         echo "no tahiti server to stop"
      fi
      ;;

   (status)

      if [ -f $pid ]; then
         TARGET_ID="$(cat "$pid")"
         if [[ $(ps -p "$TARGET_ID" -o comm=) =~ "python" ]]; then
            echo "tahiti server is running (pid=$TARGET_ID)"
            exit 0
         else
            echo "$pid file is present (pid=$TARGET_ID) but tahiti server not running"
            exit 1
         fi
      else
         echo tahiti server not running.
         exit 2
      fi
      ;;

   (*)
      echo $usage
      exit 1
      ;;
esac
