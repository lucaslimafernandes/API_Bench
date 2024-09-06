#!/bin/bash

# Golang
ab -n 100000 -c 100 http://localhost:8080/ >> Go_test.txt

# Golang + Chi
ab -n 100000 -c 100 http://localhost:8090/ >> Go_chi_test.txt

# Golang + Gin + Auth
ab -n 100000 -c 100 http://localhost:8080/ >> Go_test.txt

# Python + Flask
ab -n 100000 -c 100 http://localhost:8100/ >> Python_test.txt

# Python + Flask + Gunicorn
ab -n 100000 -c 100 http://localhost:8110/ >> Python_gunicorn_test.txt

# Python + Flask + Gunicorn + Auth
ab -n 100000 -c 100 http://localhost:8110/ >> Python_gunicorn_test.txt

Concurrency: 1000

# Golang
ab -n 100000 -c 1000 http://localhost:8080/ >> Go_test.txt

# Golang + Chi
ab -n 100000 -c 1000 http://localhost:8090/ >> Go_chi_test.txt

# Golang + Gin + Auth
ab -n 100000 -c 1000 http://localhost:8080/ >> Go_test.txt

# Python + Flask
ab -n 100000 -c 1000 http://localhost:8100/ >> Python_test.txt

# Python + Flask + Gunicorn
ab -n 100000 -c 1000 http://localhost:8110/ >> Python_gunicorn_test.txt

# Python + Flask + Gunicorn + Auth
ab -n 100000 -c 1000 http://localhost:8110/ >> Python_gunicorn_test.txt

