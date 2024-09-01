# API_Bench
A Simple Benchmark using Go, Python, Nginx and Docker.

## Results

Based on the data provided, we can draw the following conclusions regarding the performance of different frameworks and configurations:




## Contributing

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

### Streamlit analysis (optional)

To install Streamlit for viewing the charts:

Navigate to the /analysis/ directory, then run:

```bash
apt install -y python3 python3-pip python3-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

The analysis/tests/comparison.csv file needs to be filled in manually.


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

Concurrency: 100

- Golang
```bash
ab -n 100000 -c 100 http://localhost:8080/ >> Go_test.txt
```

- Golang + Chi
```bash
ab -n 100000 -c 100 http://localhost:8090/ >> Go_chi_test.txt
```

- Python + Flask
```bash
ab -n 100000 -c 100 http://localhost:8100/ >> Python_test.txt
```

- Python + Flask + Gunicorn
```bash
ab -n 100000 -c 100 http://localhost:8110/ >> Python_gunicorn_test.txt
```

Concurrency: 1000

- Golang
```bash
ab -n 100000 -c 1000 http://localhost:8080/ >> Go_test.txt
```

- Golang + Chi
```bash
ab -n 100000 -c 1000 http://localhost:8090/ >> Go_chi_test.txt
```

- Python + Flask
```bash
ab -n 100000 -c 1000 http://localhost:8100/ >> Python_test.txt
```

- Python + Flask + Gunicorn
```bash
ab -n 100000 -c 1000 http://localhost:8110/ >> Python_gunicorn_test.txt
```