# tahiti
Repository for backend execution of Lemonade project

### Install
```
git clone git@github.com:eubr-bigsea/tahiti.git
cd tahiti
pip install -r requirements.txt
```

### Config
Copy `tahiti.yaml.example` to `tahiti.yaml`
```
cp tahiti.yaml.example tahiti.yaml
```

Create a database named `tahiti`
```
#Example
mysql -uroot -pmysecret -e "CREATE DATABASE tahiti;"

```
and then create a user and give him/her permissions to the database (
SELECT/INSERT/DELETE/UPDATE and DML).

Edit `tahiti.yaml` according to your database config
```
# Tahiti configuration file
tahiti:
    debug: true
    servers:
        database_url: mysql://user:secret@server:3306/tahiti
    services:
    config:
        SQLALCHEMY_POOL_SIZE: 10
        SQLALCHEMY_POOL_RECYCLE: 240
```
In order to use Lemonade, you need to import the SQL script tahiti.sql, located
under the folder `migrations/versions`'. This script will load initial list of
operations and platforms supported by Lemonade.
To import the script, use the following command (requires installation of mysql-clients package):

`mysql -h "server" -P 3306 -u user -p "secret" "tahiti" < "migrations/versions/tahiti.sql"`

### Run
```
TAHITI_CONFIG=tahiti.yaml python tahiti/app.py
```

#### Using docker
Build the container
```
docker build -t bigsea/tahiti .
```

Repeat [config](#config) stop and run using config file
```
docker run \
  -v $PWD/tahiti.yaml:/usr/src/app/tahiti.yaml \
  -p 3322:3322\
  bigsea/tahiti
```

Again, you should import initial data as described above, even if you are using Docker.
