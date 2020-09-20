SHELL := /bin/bash # Use bash syntax

install:
	pip install --upgrade pip && \
	pip install poetry && \
	poetry install


test:
	pytest --cov=alphakill-tweebot tests/

build:
	docker-compose -f docker-compose.yml build

serve:
	docker-compose -f docker-compose.yml up --build -d

migrate:
	docker-compose run alphakill-tweebot alembic upgrade head

bash:
	docker-compose run alphakill-tweebot bash

logs:
	docker-compose logs -f alphakill-tweebot

reset:
	docker-compose rm -fsv
