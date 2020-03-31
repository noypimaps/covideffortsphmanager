docker exec <service-name> python manage.py makemigrations
docker exec <service-name> python manage.py migrate
docker exec <service-name> python manage.py createsuperuser

docker exec -it <service-name> python manage.py createsuperuser
