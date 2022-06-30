migrate:
	docker-compose run web python manage.py migrate

migration:
	docker-compose run web python manage.py makemigrations

logs:
	docker-compose logs

up:
	docker-compose up

bg_up:
	docker-compose up -d

down:
	docker-compose down

superuser:
	docker-compose run web python manage.py createsuperuser

build:
	docker-compose build

test:
	docker-compose run web pytest