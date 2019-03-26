# flaskr-tutorial
Tutorial da documentação oficial do Flask.  

## Gerenciando os serviços com Docker Compose  

```sh
# Iniciando normalmente os serviços.
docker-compose up

# Iniciando os serviços em segundo plano.
docker-compose up -d

# Recriando a imagem e iniciando os serviços.
docker-compose up --build

# Recriando a imagem e iniciando os serviços em segundo plano.
docker-compose up --build -d

# Removendo os serviços.
docker-compose down

# Verificando status dos serviços.
docker-compose ps
```
