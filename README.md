# Python Inspiration Clean Architecture Project Pattern

## 🔍 What Is It?
This template serves as your trustworthy compass in the realm of Python development. It's built upon the principles of Clean Architecture, which empower you to create code that's readable, maintainable, and scalable.

## 🚀 Why Is It Important?
Clean Architecture makes your projects resilient to change and ready to scale. It divides your code into logical layers, making it a breeze to add new features and maintain the existing ones.

## 💼 Who Is It For?
This template is suitable for both beginners and seasoned developers. Regardless of your skill level, you'll find everything you need to level up your skills.

## 🛠️ What's Included?
A project structure ready for Clean Architecture principles.
Easy configuration using '.env' files.
A powerful Python toolkit for development and testing.
Examples and tips for a quick start.

## 🌟 Get Experience!
Use this template to craft Python applications that are easy to maintain, extend, and customize. Elevate your code to a new level and acquaint yourself with the world of Clean Architecture. Code that leaves an impression. 💻🚀


## Quick Start

**NOTE**: The project uses Python 3.12, so need it installed first. It is recommended to use [`pyenv`](https://github.com/pyenv/pyenv) for installation.

**NOTE**: Root of the django project is at the `src` folder

Here is a short instruction on how to quickly set up the project for development:

1. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone
```bash
$ git clone https://github.com/azizjon-aliev/python_clean_architecture.git
```

3. Install requirements:
```bash
$ uv sync
```

4. Install pre-commit hooks: `$ pre-commit install`
6. Add and setup .env file: `$ cp .env.example .env` -> edit `.env`
5. Initiate the database: `$ python manage.py migrate`
8. Run the server: `$ python manage.py runserver`

### Run the API backend

Create docker images and execute the containers for development. From the project directory:
```
$ docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml --env-file ./.env up -d --build
```

## Execute tests suite

1. Execute the docker containers with environment variables setup for testing:
```
$ docker-compose -f docker/docker-compose.yml -f docker/docker-compose.test.yml --env-file ./.env up -d --build
```

2. Access running api backend _api_container_ docker container shell:
```
docker exec -it api_container bash
```
3. Execute pytest command from project directory:
```
pytest
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

[django]: <https://www.djangoproject.com>
[djangorestframework]: <https://www.django-rest-framework.org>
[postgres]: <https://www.postgresql.org>
[cleanarchitecture]: <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[swagger]: <https://github.com/sdediego/django-clean-architecture/blob/main/docs/forex.yaml>
