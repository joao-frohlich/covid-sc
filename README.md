# COVID-SC APP

- [Dependências](#dependências)
- [Configurações](#configurações)
- [Desenvolvimento](#desenvolvimento)
- [Deploy](#deploy)

## Dependências

- Python 3.8.2
- Docker Compose

```sh
poetry install
```

## Configurações

```sh
cp local.env .env
```

Subir a base PostgreSQL com o Docker Compose:

```sh
docker-compose up -d
```

Rodar as migrações:

```sh
poetry run python manage.py migrate
```

E criar o usuário para o admin

```sh
poetry run python manage.py createsuperuser
```

## Desenvolvimento

Importar dados de desenvolvimento:

```sh
poetry run python manage.py loaddata apps/hospitals/fixtures.json
```

Executando a aplicação no ambiente local:

```sh
poetry run python manage.py runserver
```

Testes

```sh
poetry run pytest -vv
```

## Deploy

```sh
git push heroku master
```
