#!/bin/bash

# Golang
ab -n 100000 -c 100 http://localhost:8000/ >> Go_test.txt

# Golang + Chi
ab -n 100000 -c 100 http://localhost:8010/ >> Go_chi_test.txt

# Golang + Gin + Auth
ab -n 1000 -c 10 http://localhost:8020/auth/login >> Go_gin_test_auth.txt

# Python + Flask
ab -n 100000 -c 100 http://localhost:9000/ >> Python_test.txt

# Python + Flask + Gunicorn
ab -n 100000 -c 100 http://localhost:9010/ >> Python_gunicorn_test.txt

# Python + Flask + Gunicorn + Auth
ab -n 1000 -c 10 http://localhost:9020/ >> Flask_gunicorn_auth.txt

Concurrency: 1000

# Golang
ab -n 100000 -c 1000 http://localhost:8000/ >> Go_test.txt

# Golang + Chi
ab -n 100000 -c 1000 http://localhost:8010/ >> Go_chi_test.txt

# Golang + Gin + Auth
ab -n 1000 -c 100 http://localhost:8020/auth/login >> Go_gin_test_auth.txt

# Python + Flask
ab -n 100000 -c 1000 http://localhost:9000/ >> Python_test.txt

# Python + Flask + Gunicorn
ab -n 100000 -c 1000 http://localhost:9010/ >> Python_gunicorn_test.txt

# Python + Flask + Gunicorn + Auth
ab -n 1000 -c 100 http://localhost:9020/ >> Flask_gunicorn_auth.txt

