# MySchoolFront

## Sumário

- [Resumo](#resumo)
- [Fluxo desenvolvimento](#fluxo-desenvolvimento)
  - [Rodando ambiente com Docker](#rodando-ambiente-com-docker)
  - [django-cli](#django-cli)
  
## Resumo

 Está a é uma aplicação cujo objetivo
 é gerir a api  de um CRUD (Create, Read, Update, Delete) para o cadastro de estudantes. 

## Fluxo desenvolvimento
    Foram utlizadas as seguintes dependencias 
        Django~=5.1
        djangorestframework~=3.15.2
        django-filter~=24.3
        markdown~=3.6
        mysqlclient~=2.2.4
        python-dotenv~=1.0.1
        django-cors-headers~=4.4.0
        django-oauth-toolkit~=2.4.0
        gunicorn==21.2.0
    
    O banco de dados utilizado no projeto foi MySQL     

## Rodando ambiente com Docker

  Acesse o diretório em que o repositório foi clonado através do terminal e
  execute os comandos:

    - `docker-compose up` para inicializar o servidor


## django-cli
    Comandos para sincronizar migrations do banco de dados
        ./manage.py migrate
    Comando para criar um super admin
        ./manage.py createsuperuser
    Comando para iniciar o projeto
        ./manage.py runserver

## Variaveis de ambiente
  Necessario criar um arquivo .env para iniciar o sitema
  segue um exemplo.

    HOST: "db"
    PORT: 3306
    NAME: "myschoolDB"
    PASSWORD: "root"
    USER: "root"
    DJANGO_SUPERUSER_NAME: "admin"
    DJANGO_SUPERUSER_EMAIL: "admin@email.com"
    DJANGO_SUPERUSER_PASSWORD: "admin"


<!-- START links -->

[1]: #resumo
[3]: #setup  
[3]: #docker
[4]: #angular-cli



<!-- END links -->