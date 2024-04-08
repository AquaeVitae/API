#!/bin/sh

docker compose up --build -d
docker-compose exec web python aquaevitae_api/manage.py migrate --noinput
docker-compose exec web python aquaevitae_api/manage.py collectstatic --noinput
