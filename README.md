# Covid 19 Relief Efforts Data Manager
Data Management system for Covid 19 relief efforts. This is an ongoing development.

## Requirements
- Docker

## Installation
1. Create the following; `.env.dev` and `.env-db.dev` refer to the sample `.env` and `.env-db` files.
2. Create a superuser `docker-compose exec web python manage.py createsuperuser` 

## Usage
1. Starting a service 
```
bash run_dev.sh
```
2. Stopping a service
```
bash stop_dev.sh
```
