# Web Project
## Summary
  - [Introduction](#introduction)
  - [Project idea](#project-idea)
  - [Requirements](#requirements)
  - [How to run the application](#How-to-run-the-application)
  - [How to deploy the application in heroku](#How-to-deploy-the-application-in-heroku)
  - [Teachers](#teachers)
  - [Authors](#authors)

## Introduction
**Web Project** is a subject of the [Degree Computer Engineering](http://www.grauinformatica.udl.cat/en) studied in [University of Lleida](http://www.udl.es/ca/).
This is the repository of the project of this subject.

## Project idea
The idea of our project is a web application that allows its registered users to access an online library that contains movies and series (similar to Netflix). The main difference that will exist between our idea and Netflix (or similar online apps that already exist) is that the platform which are we are going to be developing this project in will be completely free.

The main goal we are trying to achieve with this project will is to understand how a movie streaming service works through with a web application.

## Requirements
The document named **requirements.txt** should include the following dependencies:
```
  Django==3.1.7 
  gunicorn==20.1.0 
  django-heroku 
  whitenoise
```
## How to run the application
To run the application you have to execute the following commands:
```
docker-compose up
```
## How to deploy the application in heroku
To deploy the project in heroku you need to follow the following instructions:

1- Copy all the document files in a new folder.

2- We make sure that Procfile file exist.
```
  web: gunicorn fakefilms.wsgi
```
3- We make sure that requeriments.txt exist with all dependencies.
```
  Django==3.1.7 
  gunicorn==20.1.0 
  django-heroku 
  whitenoise
```
Review the section [Requeriments](#requirements).
4- Create a new repository:
```
  git init
  git add .
  git commit -m "heroku deployment"
```
5- Login in heroku:
```
  heroku login
```
6- Create new application in heroku:
```
  heroku create fakefilm
```
6.1- In case that the application is already created:
```
  heroku git:remote -a fakefilms
```
7- Push the new repository to the new heroku application:
```
  git push heroku master
```
8- Configure the django environment variables:
```
  heroku config:set DJANGO_SETTINGS_MODULE=fakefilms.settings_heroku
```
9- Migrate the DB:
```
  heroku run python manage.py migrate
```
10- Create superuser:
```
  heroku run python manage.py createsuperuser 
```

## Teachers
The teachers who have guided this project are:
- [Carles Mateu](https://github.com/carlesm)
- [Roberto Garcia](https://github.com/rogargon)

## Authors
This project have been developed by:
- [Alejandro Clavera Poza](https://github.com/alejandroclavera)
- [Pau Escolà Barragán](https://github.com/pauescola13)
- [Guillem Arbiol López de Zamora](https://github.com/ThaGuille)
- [Didac Colominas Abalde](https://github.com/ColoAlfa)
- [Miguel Ángel Barraza](https://github.com/Miguebaso)
- [Jordi Lazo](https://github.com/JordiLazo)
