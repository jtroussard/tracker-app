.PHONY: test coverage clean reset-db cypresstests

test:
	pytest -s --cov-report=html --cov=app/ --cov-config=.coveragerc

test-no-cov:
	pytest --cov=app --no-cov

coverage:
	pytest --cov=app --cov-report=html --cov-report=term

clean:
	rm -rf .coverage htmlcov

create_db:
	python3 -c "from app.src import app; from app.src import db; app.app_context().push(); db.create_all();"

init_db:
	export FLASK_APP=run.py && flask db init

migrate_db:
	export FLASK_APP=run.py && flask db migrate

upgrade_db:
	export FLASK_APP=run.py && flask db upgrade

backup:
	pg_dump -U $(username) $(database) > instance/backup.sql


