# tahiti
Repository for backend execution of Lemonade project

### Install Tahiti
```
git clone git@github.com:eubr-bigsea/tahiti.git
cd tahiti
```

### Install Requirements
```
pip install -r requirements.txt
```

If you prefer, use a virtualenv to install all requirements.


### Define Path
Execute the following command inside tahiti folder
```
export PYTHONPATH=.
```

### Config
Copy `tahiti.yaml.example` to `tahiti.yaml`
```
cp conf/tahiti.yaml.example tahiti.yaml
```

Create a database named `tahiti`
```
#Example
mysql -u root -p mysecret -e "CREATE DATABASE tahiti CHARACTER SET utf8;"

```
and then create a user and give him/her permissions to the database (
INSERT/UPDATE/DELETE/SELECT and DML).
```
#Example
mysql -u root -p mysecret
> CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
> GRANT INSERT, UPDATE, DELETE, SELECT on tahiti.* TO 'username'@'hostname';
> exit

```

Edit `tahiti.yaml` according to your database config


### Migration
In order to use Lemonade, you need to migrate the last version of the database to your 
recently created database and upgrade it as follows:

#### Run app
```
export TAHITI_CONFIG = tahiti.yaml
export FLASK_APP = tahiti/app.py
```

#### Migrate db
```
flask db stamp head
flask db migrate
```

#### Upgrade db
```
flask db upgrade
```

#### Check db migration version
```
flask db current
```

### Using Docker
Build the container
```
docker build -t bigsea/tahiti .
```

Repeat [config](#config) stop and run using config file
```
docker run \
  -v $PWD/conf/tahiti-config.yaml:/usr/local/tahiti/conf/tahiti-config.yaml \
  -p 3322:5000 \
  bigsea/tahiti
```

Again, you should import initial data as described above, even if you are using Docker.
