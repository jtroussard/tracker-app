.PHONY: test coverage clean

test:
	pytest

test-no-cov:
	pytest --cov=app --no-cov

coverage:
	pytest --cov=app --cov-report=html --cov-report=term

clean:
	rm -rf .coverage htmlcov
