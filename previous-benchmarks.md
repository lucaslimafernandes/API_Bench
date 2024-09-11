# Previous Benchmarks

## Results - 09/03/2024

Based on the data provided, we can draw the following conclusions regarding the performance of different frameworks and configurations:

1. **Overall Performance**
Go (net/http) and Go + Chi demonstrate high performance, with a high number of requests per second (RPS) and fast response times. Python + Flask shows the poorest performance, with an RPS 80% lower than Go and 93.22% request failures under heavy load. Python + Gunicorn + Flask significantly improves performance, approaching Go in high concurrency scenarios.

![](analysis/imgs/hello_world/time_taken.png)


2. **Throughput (Requests per Second)**
Go + Chi achieves the highest RPS with 100 concurrent requests. Gunicorn enhances RPS in Python, but Go still leads. At higher concurrency levels (1000), Go remains robust, while Python with Gunicorn gets closer.

![](analysis/imgs/hello_world/rps.png)


3. **Time per Request**
Go, with both net/http and Chi, maintains consistently low response times, indicating greater efficiency. Python without Gunicorn has high response times, while Python + Gunicorn significantly reduces these times, though still trailing behind Go in low concurrency and approaching in high concurrency.

![](analysis/imgs/hello_world/time_p_r.png)


4. **Request Failures**
Go shows few or no request failures, even under heavy load. Python + Flask has a high number of failures at high concurrency, indicating low scalability without Gunicorn.

![](analysis/imgs/hello_world/failed.png)


5. **Transfer Rate**
Go leads in transfer rate, showing higher efficiency in data transmission. Python + Flask again underperforms, with some improvement when using Gunicorn.

![](analysis/imgs/hello_world/transfer_rate.png)


6. **Response Time Percentiles**
Go and Go + Chi have low and consistent percentiles, indicating quick responses. Python + Flask without Gunicorn has high percentiles, indicating variability and significant slowdowns under load. Python + Gunicorn improves this but still shows outliers compared to Go.

**General Conclusions**
Go is superior in terms of performance, scalability, and reliability, handling high concurrency well. Python + Flask without Gunicorn is not suitable for high loads, but the introduction of Gunicorn improves performance. Go is ideal for critical applications that require high performance, while Python + Flask + Gunicorn is more suitable for less demanding scenarios. These tests were conducted in a local environment and serve as an initial demonstration, with further testing needed using different types of responses and monitoring CPU/memory load.