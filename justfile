format:
	uv run ruff format

lint:
	uv run ruff check --fix

validate: format lint