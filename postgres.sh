#!/bin/bash

sudo docker run -d -p 5432:5432 --name pg_db --restart=always -v pg_vol:/var/lib/postgresql/data -e POSTGRES_PASSWORD=password postgres:14-alpine
