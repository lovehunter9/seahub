#!/bin/bash
#
#
#

seaf-server -c ~/dev/conf -d ~/dev/seafile-data -D all -f -l - &
cd frontend
npm run prod &
cd ..
python3 manage.py runserver 0.0.0.0:8000
