# tahiti
Repository for backend execution of Lemonade project

### Install
```
git clone git@github.com:eubr-bigsea/tahiti.git
cd tahiti
pip install -r requirements.txt
```

### Config
Copy `tahiti.json.example` to `tahiti.json`
```
cp tahiti.json.example tahiti.json
```

Create a database named `tahiti`
```
#Example
mysql -uroot -pmysecret -e "CREATE DATABASE tahiti;"
```

Edit `tahiti.json` according to your database config
```
{
  "servers": {
    "database_url": "mysql://root:mysecret@localhost:3306/tahiti",
    "environment": "dev"
  }
}
```
### Run
```
python tahiti/app_api.py -c tahiti.json
```

#### Using docker
Build the container
```
docker build -t bigsea/tahiti .
```

Repeat [config](#config) stop and run using config file
```
docker run \
  -v $PWD/tahiti.json:/usr/src/app/tahiti.json \
  -p 5000:5000 \
  bigsea/tahiti
```
