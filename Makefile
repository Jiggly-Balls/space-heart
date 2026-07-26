.PHONY: ruff check start
all: ruff

ruff:
	uv run --dev ruff format .
	uv run --dev ruff check . --fix

check:
	uv run --dev ty check .

start:
	uv run python -m durkbot