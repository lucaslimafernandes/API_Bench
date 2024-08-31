# Usando a imagem oficial do Golang
FROM golang:1.22-alpine

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o código da aplicação para dentro do contêiner
COPY . .

# Compilando a aplicação
# RUN go build -o main .
RUN go build main.go

# Definindo a porta e o comando de inicialização
EXPOSE 8080
CMD ["./main"]

