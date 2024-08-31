# API_Bench
A Simple Benchmark using Go, Python, Nginx and Docker.

## Installation

### Docker

To install Docker

```bash
curl -fsSl https://get.docker.com | bash
```

### ab - Apache HTTP server benchmarking tool

Apache ab [docs](https://httpd.apache.org/docs/current/programs/ab.html)

```bash
apt install apache2-utils
```


## Running 

### Starting the servers

Navigate to the src/ directory.

For the first time:
```bash
sudo docker compose up --build
```

if you already have the Go and Python containers built:
```bash
sudo docker compose up
```

### Run the Benchmark test

Basic Apache ab commands:

- -n: Number of requests to perform

- -c: Number of multiple requests to make at a time

- Golang
```bash
ab -n 100000 -c 100 http://localhost:8080/ >> Go_test.txt
```

- Python
```bash
ab -n 100000 -c 100 http://localhost:8090/ >> Python_test.txt
```

