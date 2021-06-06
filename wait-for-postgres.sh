#!/bin/bash
set -e

cnt=0

until timeout 5 psql $DATABASE_URL -c "\q"
do

  echo "Connecting to db server " + $cnt
  sleep 2
  cnt=$(( ++cnt ))

  if [ $cnt -eq 5 ] ; then
    echo "No response from db server"
    exit 1
  fi

done

echo "Completed normally"

python3 server/app.py & python3 -m pytest

/bin/bash
