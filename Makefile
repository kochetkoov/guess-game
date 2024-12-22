install:
	poetry install

play-game:
	poetry run play-game

build:
	poetry build

lint:
	poetry run flake8 guess_game