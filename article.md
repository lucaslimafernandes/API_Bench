# Tutorial-Análise de Performance de APIs com Docker Swarm no GCP: Comparando Go e Python com Integração de Postgres e Autenticação


## GCP - Criando conta e iniciando instâncias de computação

### Criar a conta

Primeiro, vamos criar uma conta no [Google Cloud](https://cloud.google.com/) para utilizar os recursos (Compute Engine)

Basta acessar o site, clicar em começe gratuitamente e seguir os passos

![](/docs/create_acc/1.png)

![](/docs/create_acc/2.png)

![](/docs/create_acc/3.png)

Pronto, tem um conta com $ 300 dólares iniciais, não se preocupe, caso você não ative a conta completa, ela não gerará cobrança, além do mais, recomendo o uso de um cartão virtual que possa ser bloqueado.

![](/docs/create_acc/msg.png)

### Criar instâncias 

1. Primeiro, acessar a coluna lateral e selecionar Compute Engine >> Instâncias de VM, caso seja primeiro acesso

![](/docs/create_vm/1.png)


2. Clicar no botão Criar Instância

![](/docs/create_vm/2.png)

2.1 Identificação

![](/docs/create_vm/3_1.png)

2.2 Rolando mais pra baixo a página, encontramos a configuração da máquina, selecionei uma E2 4vCPU, 2 núcleos, 4 GB Ram, peguei uma pré-definida, mas poderia ter personalizado

![](/docs/create_vm/3_2.png)

2.3 Selecionei o sistema operacional, deixei o padrão o tamanho de disco em 10 GB, e por, clicar em criar

![](/docs/create_vm/3_3.png)

2.4 Pronto, a primeira instância criada

![](/docs/create_vm/4.png)

2.5 Criei outras instâncias, uma para rodar postgres, outra para executar o rodar o ab - Apache HTTP server benchmarking tool e as intâncias rodando os containers dockers das aplicações

![](/docs/create_vm/5.png)

3. Configurando a instância

Verifique os status das instâncias, devem estar com setinha verde, e clique no botão SSH, para abrir o terminal e acessa-lás

3.1 Ao acessar o terminal, será exibido como um pop-up

![](/docs/configure_vm/terminal.png)

3.2. Primeiro passo, instalar o docker nas instâncias que rodarão aplicações e do postgres

```bash
sudo curl -fsSl http://get.docker.com | bash 
```

![](/docs/configure_vm/install_docker.png)

3.3 Executar o postgres, na instância destinada ao pg, rodar o comando docker

```bash
sudo docker run -d -p 5432:5432 --name pg_db --restart=always -v pg_vol:/var/lib/postgresql/data -e POSTGRES_PASSWORD=password postgres:14-alpine
```

![](/docs/configure_vm/pg.png)


4. Docker Swarm

na primeira instância, após instalar o docker, iniciar o swarm

```bash
sudo docker swarm init
```

![](/docs/configure_vm/swarm_init.png)

4.2 Clonar o repositório em todas as instâncias, para possui os arquivos de build

4.3. Em todas as instâncias, deve ser realizado o build das imagens das aplicações (exceto nas instâncias do pg e do ab)

```bash
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
```

como exemplo o arquivo `build_containers.sh` possui os comandos

4.4. Realizar o ingresso das instâncias

![](/docs/configure_vm/swarm_join.png)

As instâncias que juntei ao swarm foram i1, i2, i3 e i4
 
Quando todos os nós estiverem ok, pode-se verificar

```bash
sudo docker node ls
```

![](/docs/configure_vm/4.png)

4.5. Executar o stack

![](/docs/configure_vm/5.png)

```bash
sudo docker stack deploy -c src/docker-stack.yaml api_bench
```

Para verificar o ip local, pode usar o comando hostname

```bash
hostname - I
## Output
# 10.128.0.11 172.17.0.1 172.18.0.1

curl 10.128.0.11:8000/
curl 10.128.0.11:8010/
curl 10.128.0.11:8020/ping
curl 10.128.0.11:9000/
curl 10.128.0.11:9010/
curl 10.128.0.11:9020/ping
```

4.6. Para escalar o número de réplicas

```bash
sudo docker service scale nome=numero
```

![](/docs/configure_vm/12.png)



5. Na instância destinada a executar o apacha AB

instalar e executar a batida de testes:
```bash
apt install apache2-utils

ab -n 100000 -c 100 10.128.0.11:8000/ >> Salvar_em_arquivo.txt
```

Importante, o ip 10.128.0.11 é o endereço do ip interno de uma máquina rodando as aplicações

como exemplo o arquivo `run_ab.sh` possui os comandos


## Análise dos dados

