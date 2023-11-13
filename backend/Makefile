.PHONY: run-local
run-local:
	poetry run uvicorn app.uwsgi:app --port 8080

api/openapi.json:
	poetry run python3 app/openapi.py > api/openapi.json
