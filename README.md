# Bespoke Wear - Loja de Rupas

## Como rodar?
 Vamos precisar criar o projeto e fazer o build de tudo, utilize os comandos abaixo:

```bash
#Para criar os containers
docker-compose build
#Para iniciar os containers
docker-compose up -d backend frontend
```
Depois de fazer o build e iniciar todos containers, fazendo um docker ps é possível ver que temos os seguintes serviços rodando:
```bash
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                 NAMES
a72fb2ab3ba2   back-todoten           "wait-for-it localho…"  mytodolist_backend_1
6ef83aab15e5   front-todoten          "docker-entrypoint.s…"  mytodolist_frontend_1
6def45b54094   nginx                  "/docker-entrypoint.…"  mytodolist_nginx_1
93e76c660729   postgres:13.3-alpine   "docker-entrypoint.s…"  mytodolist_postgres_1
```

Para conseguir logar, vamos precisar criar um usuário no Django. Podemos fazer isto entrando no container backend e rodar o comando do Django ./manage.py createsuperuser:
```bash
$ docker-compose exec backend ./manage.py createsuperuser

Usuário (leave blank to use 'root'): admin
Endereço de email: admin@example.com
Password:
Password (again):
Superuser created successfully.
```
## Alimentar o Banco com produtos para teste
```
docker-compose exec backend python manage.py loaddata products.json
```

## Previa 
![image](https://user-images.githubusercontent.com/104439599/218184021-ca7648a1-7cae-4f85-9995-47e0c5b0fce6.png)
![image](https://user-images.githubusercontent.com/104439599/218184301-c7c03c84-36c4-489d-a8bf-0259f22d684f.png)

![image](https://user-images.githubusercontent.com/104439599/218184644-5892f430-8c50-4497-92ae-13d1331d9b2b.png)
![image](https://user-images.githubusercontent.com/104439599/218184872-8349e9d7-b63d-4db6-9370-077c74ee509d.png)
![image](https://user-images.githubusercontent.com/104439599/218185379-22b05dfa-146a-4906-a785-3f53f08c9e47.png)


https://user-images.githubusercontent.com/104439599/218233863-10869c73-8eb0-4c74-a796-fd7d5da4a541.mp4





