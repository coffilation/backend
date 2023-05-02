.PHONY: environment, dev, migrations, migrate
environment:
	docker compose up -d

dev:
	docker compose up backend --build --force-recreate

migrations:
	docker compose run --rm backend python manage.py makemigrations

migrate:
	docker compose run --rm backend python manage.py migrate $(app) $(migration)
