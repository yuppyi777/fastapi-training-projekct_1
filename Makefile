.PHONY: help build up down restart logs shell test lint format clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build Docker containers
	docker-compose build

up: ## Start Docker containers
	docker-compose up -d

down: ## Stop Docker containers
	docker-compose down

restart: down up ## Restart Docker containers

logs: ## Show container logs
	docker-compose logs -f app

shell: ## Access application shell
	docker-compose exec app /bin/bash

db-shell: ## Access database shell
	docker-compose exec db psql -U admin -d app_db

test: ## Run tests
	docker-compose exec app pytest

test-cov: ## Run tests with coverage
	docker-compose exec app pytest --cov=app --cov-report=html --cov-report=term

lint: ## Run linters
	docker-compose exec app flake8 app tests
	docker-compose exec app mypy app

format: ## Format code
	docker-compose exec app black app tests
	docker-compose exec app isort app tests

format-check: ## Check code formatting
	docker-compose exec app black --check app tests
	docker-compose exec app isort --check-only app tests

clean: ## Clean up containers and volumes
	docker-compose down -v
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf htmlcov .pytest_cache .mypy_cache .coverage

migrate: ## Run database migrations (when Alembic is set up)
	docker-compose exec app alembic upgrade head

migration: ## Create new migration (usage: make migration message="your message")
	docker-compose exec app alembic revision --autogenerate -m "$(message)"

install: build up ## Initial setup: build and start containers
	@echo "Waiting for database to be ready..."
	@sleep 5
	@echo "Application is ready at http://localhost:8000"
	@echo "API docs available at http://localhost:8000/docs"
