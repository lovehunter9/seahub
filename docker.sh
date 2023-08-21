#!/bin/bash
#
#
#

cd frontend
#npm install @babel/plugin-proposal-private-property-in-object caniuse-lite chart.js@^3.9.1 react-chartjs-2@^4.3.1 --legacy-peer-deps --save-dev
#npm run build
export DANGEROUSLY_DISABLE_HOST_CHECK=true
export NODE_OPTIONS=--max_old_space_size=512
npm run dev --allowed-hosts all --allowed-host .snowinning.com &
cd ..

seaf-server -c ~/dev/conf -d ~/dev/seafile-data -D all -f -l - &
#cd frontend
#npm run dev &
#cd ..
python3 manage.py runserver 0.0.0.0:8000
