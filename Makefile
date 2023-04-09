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
    if [[ $$confirm == [yY] ]]; then \
        python -c "from weight_tracker.src import app, db; from weight_tracker.src.models import User, Entry; app.app_context().push(); db.drop_all(); db.create_all();" \
    else \
        echo "Reset canceled" \
    fi

