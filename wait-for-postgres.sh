#!/bin/bash
set -e

until psql $DATABASE_URL
do
  echo "No response from db server"
  sleep 3
done
