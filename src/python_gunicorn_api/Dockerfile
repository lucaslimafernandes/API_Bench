# Python3 image
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install Flask gunicorn

EXPOSE 5050

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "main:app"]
