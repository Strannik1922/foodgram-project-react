# [Foodgram](http://foodmanager.sytes.net/recipes) is a website with many functions, the main one of which is to share your recipes.

![Build Status](https://github.com/Strannik1922/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Tech.
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Djoser](https://img.shields.io/badge/-Djoser-464646?style=flat&logo=Djoser&logoColor=56C0C0&color=008080)](https://github.com/sunscrapers/djoser)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://hub.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)

##### The full list of modules used in the project is available in [backend/requirements.txt](https://github.com/Strannik1922/foodgram-project-react/blob/master/backend/requirements.txt)


### The service is available to users:
```
http://158.160.35.246/
```

## Description.
Online Foodgram service and API for it. There is an implementation of the CI/CD project. In this service, users can publish recipes, subscribe to other users' publications, add their favorite recipes to Favorites, download a list of products needed to prepare one or more selected dishes.

## Service features.
##### User access levels:
* Guest (unauthorized user)
* Authorized user
* Administrator

##### What unauthorized users can do:
* Create an account.
* View recipes on the main page.
* View individual recipe pages.
* View user pages.
* Filter recipes by tags. 

##### What authorized users can do:
* Log in with your username and password.
* Log out (log out).
* Change your password.
* Create/edit/delete your own recipes
* View recipes on the main page.
* View user pages.
* View individual recipe pages.
* Filter recipes by tags.
* Work with a personal favorites list: add recipes to it or delete them, view your favorites recipes page.
* Work with a personal shopping list: add/remove any recipes, upload a file with the number of necessary ingredients for recipes from the shopping list.
* Subscribe to recipe authors' publications and cancel your subscription, view your subscriptions page.

##### Any actions are available to the administrator.

##### More information is available in the API documentation at <http://localhost/api/docs/> after run the project.

#### Workflow of the project.
Starts when executing the 'git push' command.
**Jobs:**
- **tests:** Checking the code for compliance with the PEP8 standard (using the flake8 package)
- **build_image_and_push_to_docker_hub:** Build and push the project image on DockerHub.
- **deploy:** Automatic deployment of the project to the server.
- **send_message:** Sending a notification to the user in Telegram.

## Installing and running the project on a local machine.
You must have installed and run Docker. More information in [Instructions](https://docs.docker.com/).
#### 1. Clone a repository.
* Option 1. Use SSH:
```bash
git clone git@github.com:Strannik1922/foodgram-project-react.git
```
#### 2. Create and activate a virtual environment.
Command for Windows:
```bash
python -m venv venv
. venv/Scripts/activate
```
#### 3. Go to the infra directory.
```bash
cd infra
```
#### 4. Сreate ".env" file and fill in the sample.

DB_ENGINE=django.db.backends.postgresql # database
DB_NAME=postgres # name database
POSTGRES_USER=postgres # login for connect to database
POSTGRES_PASSWORD=12345 # password for connect to database
DB_HOST=db # name container with database
DB_PORT=5432 # login for connect to database
SECRET_KEY=12345 # secret key for Django project

#### 5. Run docker-compose.
```bash
docker-compose up -d
```
#### 6. Open bash terminal in container backend.
```bash
docker-compose exec backend bash
```
#### 7. Сreate and apply migrations.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
#### 8. Сreate superuser.
If you need create new admin:
```bash
python manage.py createsuperuser
```
#### 10. Enjoy.
open [URL](http://127.0.0.1/recipes) and enjoy.


### Author: Ivan Shamaiski


## Installing and running the project on a remote server.
#### For workflow to work correctly, you need to add environment variables to the Secrets of this repository on GitHub:

* PostgreSQL = get from .env file
* SECRET_KEY = get from .env file

* DOCKER_USERNAME = username from DockerHub
* DOCKER_PASSWORD = password from DockerHub

* USER = username for log in to a remote server
* HOST = ip adress of remote server
* SSH_KEY = your private SSH key (to get use the command: cat ~/.ssh/id_rsa)
* PASSPHRASE = if you specified the code to connect to the server via ssh

* TELEGRAM_TO = your Telegram account id
* TELEGRAM_TOKEN = your Telegram bot token

#### 1. Log in to a remote server:
```bash
ssh <username>@<ip_address>
```
#### 2. Install Docker and Docker-compose.
```bash
sudo apt install docker.io
sudo apt-get update
sudo apt-get install docker-compose-plugin
sudo apt install docker-compose
```
#### 3. Being locally in the infra/ directory, copy the docker-compose files.yml and nginx.conf to a remote server.
```bash
scp docker-compose.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
scp .env <username>@<host>:/home/<username>/
```

#### 4. Collect the container and create migrations.
```bash
sudo docker-compose up -d --build
sudo docker-compose exec backend python manage.py migrate
```

#### 5. Create superuser and collect static.
```bash
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
