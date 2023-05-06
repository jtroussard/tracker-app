.PHONY: test coverage clean reset-db

test:
	pytest

test-no-cov:
	pytest --cov=app --no-cov

coverage:
	pytest --cov=app --cov-report=html --cov-report=term

clean:
	rm -rf .coverage htmlcov

reset-db:
	@read -p "Are you sure you want to reset the database? [y/N] " confirm && \
	if [[ $confirm == [yY] ]]; then
		python -c "from app.src import app, db; from app.src.models import User, Entry; app.app_context().push(); db.drop_all(); db.create_all();"
	else \
		echo "Reset canceled"
	fi

create_db:
	python3 -c "from app.src import app; from app.src import db; app.app_context().push(); db.create_all();"

migrate_db:
	export FLASK_APP=run.py && flask db migrate -m "migration via make command"

upgrade_db:
	export FLASK_APP=run.py && flask db upgrade

