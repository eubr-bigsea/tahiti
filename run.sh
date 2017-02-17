#!/bin/bash

python ./tahiti/manage.py db upgrade
python ./tahiti/app.py
