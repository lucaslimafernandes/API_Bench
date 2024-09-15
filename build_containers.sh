#!/bin/bash

echo $(pwd)

# Build Go Net containers
sudo docker build -t go_net ./src/go_net

# # Build Go Chi API containers
sudo docker build -t go_chi ./src/go_chi

# Build Go Gin containers
sudo docker build -t go_gin ./src/go_gin

# # Build and run Python API containers
sudo docker build -t python_api ./src/python_api

# # Build and run Python Gunicorn API containers
sudo docker build -t gunicorn_api ./src/gunicorn_api

# # Build and run Python API containers
sudo docker build -t flask ./src/flask

