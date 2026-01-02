# Justfile

set shell := ["bash", "-c"]

# List available commands
default:
    @just --list

# Setup environment (install dependencies)
setup:
    uv sync
    uv add --dev ruff pytest pytest-cov

# Create a new problem
# Usage: just new 1 "Multiples of 3 and 5"
new id name="problem":
    uv run scripts/new_problem.py {{id}} "{{name}}"

# Run a specific problem solution
# Usage: just run 1
run id:
    @folder=$(find src/euler/problems -name "p{{shell("printf '%04d' " + id)}}_*" -type d | head -n 1); \
    if [ -z "$folder" ]; then \
        echo "Error: Problem {{id}} not found."; \
        exit 1; \
    fi; \
    echo "Running problem {{id}} from $folder..."; \
    uv run python "$folder/solution.py"

# Run all tests
test:
    uv run pytest

# Lint and format code
lint:
    uv run ruff check --fix .
    uv run ruff format .

# Clean cache files
clean:
    rm -rf .ruff_cache .pytest_cache .venv
    find . -type d -name "__pycache__" -exec rm -rf {} +
