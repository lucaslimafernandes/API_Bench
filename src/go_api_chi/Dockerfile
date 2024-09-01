# Golang image
FROM golang:1.22-alpine

WORKDIR /app

COPY . .

RUN go build main.go

EXPOSE 3000
CMD ["./main"]

