#!/bin/bash

# Create network
sudo docker network create backend_api_ab

# Build and run Go API containers
sudo docker build -t go-api ./go_api
sudo docker run -d --name api1 --network backend_api_ab go-api
sudo docker run -d --name api2 --network backend_api_ab go-api

# Build and run Go Chi API containers
sudo docker build -t go-api-chi ./go_api_chi
sudo docker run -d --name api_chi1 --network backend_api_ab go-api-chi
sudo docker run -d --name api_chi2 --network backend_api_ab go-api-chi

# Build and run Python API containers
sudo docker build -t python-api ./python_api
sudo docker run -d --name python_api1 --network backend_api_ab python-api
sudo docker run -d --name python_api2 --network backend_api_ab python-api

# Build and run Python Gunicorn API containers
sudo docker build -t python-gunicorn-api ./python_gunicorn_api
sudo docker run -d --name python_gunicorn_api1 --network backend_api_ab python-gunicorn-api
sudo docker run -d --name python_gunicorn_api2 --network backend_api_ab python-gunicorn-api

# Run NGINX container
sudo docker run -d --name nginx --network backend_api_ab \
  -p 8080:8080 \
  -p 8110:8110 \
  -p 8090:8090 \
  -p 8100:8100 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
  nginx:alpine
