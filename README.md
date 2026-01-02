# Project Euler Solutions

Welcome to my personal collection of [Project Euler](https://projecteuler.net/) solutions, implemented in Python.

This project focuses on writing **clean, efficient, and well-documented** code. Each problem typically includes:
1.  **Iterative Solution**: A brute-force approach for verification.
2.  **Optimized Solution**: A mathematical approach (often $O(1)$ or significantly faster) to solve the problem efficiently.
3.  **Markdown Analysis**: Detailed mathematical derivations and explanations.

## 🏗 Project Structure

The project uses a **folder-per-problem** structure to keep things organized.

```text
project_euler/
├── justfile                # Command runner (entry point)
├── pyproject.toml          # Python config (uv, ruff, pytest)
├── scripts/
│   └── new_problem.py      # Scaffolding script
├── src/
│   └── euler/
│       ├── utils/          # Shared mathematical libraries
│       │   ├── common.py   # Decorators (e.g., @timeit)
│       │   └── primes.py   # Prime number generation/factorization
│       └── problems/       # Solutions
│           ├── p0001_multiples_of_3_or_5/
│           │   ├── solution.py  # Python code
│           │   └── README.md    # Math explanation
│           └── ...
└── tests/                  # Automated tests
```

## 🛠 Tech Stack

*   **[uv](https://github.com/astral-sh/uv)**: Extremely fast Python package and project manager.
*   **[Ruff](https://docs.astral.sh/ruff/)**: Blazing fast Python linter and formatter.
*   **[Just](https://github.com/casey/just)**: A handy command runner to simplify workflows.
*   **[Pytest](https://docs.pytest.org/)**: Testing framework.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
*   [uv](https://github.com/astral-sh/uv)
*   [just](https://github.com/casey/just)
*   Python 3.12+

### Setup

Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd project_euler

# Install dependencies and setup virtual environment
just setup
```

## 💻 Usage

I use `just` to manage common tasks.

### 1. Create a New Problem
To generate the folder structure (`solution.py` and `README.md`) for a new problem:

```bash
# Usage: just new <id> "<problem_name>"
just new 4 "Largest Palindrome Product"
```

### 2. Run a Solution
To run the solution for a specific problem ID:

```bash
# Usage: just run <id>
just run 1
```

### 3. Run Tests
To run the test suite:

```bash
just test
```

### 4. Lint & Format
To check code style and automatically fix formatting issues:

```bash
just lint
```

## 📚 Progress

| ID | Problem | Solution | Analysis |
|----|---------|:--------:|:--------:|
| 00 | Problem Zero (Example) | [Code](src/euler/problems/p0000_sum_of_odd_squares/solution.py) | [Note](src/euler/problems/p0000_sum_of_odd_squares/README.md) |
| 01 | Multiples of 3 or 5 | [Code](src/euler/problems/p0001_multiples_of_3_or_5/solution.py) | [Note](src/euler/problems/p0001_multiples_of_3_or_5/README.md) |
| 02 | Even Fibonacci Numbers | [Code](src/euler/problems/p0002_even_fibonacci_numbers/solution.py) | [Note](src/euler/problems/p0002_even_fibonacci_numbers/README.md) |
| 03 | Largest Prime Factor | [Code](src/euler/problems/p0003_largest_prime_factor/solution.py) | [Note](src/euler/problems/p0003_largest_prime_factor/README.md) |
| 04 | Largest Palindrome Product | [Code](src/euler/problems/p0004_largest_palindrome_product/solution.py) | [Note](src/euler/problems/p0004_largest_palindrome_product/README.md) |
| 05 | Smallest Multiple | [Code](src/euler/problems/p0005_smallest_multiple/solution.py) | [Note](src/euler/problems/p0005_smallest_multiple/README.md) |
| 06 | Sum Square Difference | [Code](src/euler/problems/p0006_sum_square_difference/solution.py) | [Note](src/euler/problems/p0006_sum_square_difference/README.md) |
| 07 | 10 001st Prime | [Code](src/euler/problems/p0007_10001st_prime/solution.py) | [Note](src/euler/problems/p0007_10001st_prime/README.md) |
| 08 | Largest Product in a Series | [Code](src/euler/problems/p0008_largest_product_in_a_series/solution.py) | [Note](src/euler/problems/p0008_largest_product_in_a_series/README.md) |
| 09 | Special Pythagorean Triplet | [Code](src/euler/problems/p0009_special_pythagorean_triplet/solution.py) | [Note](src/euler/problems/p0009_special_pythagorean_triplet/README.md) |
| 10 | Summation of Primes | [Code](src/euler/problems/p0010_summation_of_primes/solution.py) | [Note](src/euler/problems/p0010_summation_of_primes/README.md) |
| 11 | Largest Product in a Grid | [Code](src/euler/problems/p0011_largest_product_in_a_grid/solution.py) | [Note](src/euler/problems/p0011_largest_product_in_a_grid/README.md) |
| 12 | Highly Divisible Triangular Number | [Code](src/euler/problems/p0012_highly_divisible_triangular_number/solution.py) | [Note](src/euler/problems/p0012_highly_divisible_triangular_number/README.md) |
