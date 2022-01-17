Customer Backend
================
A Django REST Backend Web App with Customer CRUD Operations

## Postman Collection
https://drive.google.com/file/d/12SNFocC5E5pfI_9NMtxlrn5QvsqbxOUX/view?usp=sharing

## Requirements

### 1.Programming Language ###

* python - 3.8.12

### 2.Framework ###

* django - 3.2.11

### 3.Other Requirements ###

* django-environ - 0.8.1
* django-rest-auth - 0.9.5
* django-rest-auth[with_social]
* djangorestframework - 3.13.1
* djangorestframework-simplejwt - 5.0.0
* psycopg2-binary - 2.9.3

## Usage

For initial project installation of the project for the sake of development,

1. clone the project via

```bash
git clone https://github.com/Avin-Techv/customer_backend_v2.git
```

2. Create a new file called .env and place it inside the folder with setttings.py file
```bash
touch .env
```

3. Add environment values like this
```bash
SECRET_KEY='django-insecure-y9uae8#otc#5&g_$@)!d-z9$^(c83jp_v)*e=(=bq(lr$79djy'
DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
DATABASE_NAME=customer_backend_db
DATABASE_USER=customer_backend_user
DATABASE_PASSWORD=customer_backend_pass
DATABASE_HOST=db
DATABASE_PORT=5432
```

4. run the project
The project can be run in two different ways

     4.1. tradional development run: in traditional development run we the project in a terminal via the following steps

          4.1.1. create a python virtual environment

          4.1.2. install all the requirements

          4.1.3. create the postgres database via pgadmin/postgres terminal

          4.1.4. perform migratations

          4.1.5. run django server

     4.2 running via docker

          4.2.1. go to the folder that contains file docker-compose.yml

          4.2.2. type and execute the command
          - sudo docker-compose -f docker-compose.yml build

          4.2.3. after successful build type and execute the command
          - sudo docker-compose -f docker-compose.yml up

4. download the postman collection and import it in the postman app

5. make necessary api calls