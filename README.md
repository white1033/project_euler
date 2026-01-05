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
| 13 | Large Sum | [Code](src/euler/problems/p0013_large_sum/solution.py) | [Note](src/euler/problems/p0013_large_sum/README.md) |
| 14 | Longest Collatz Sequence | [Code](src/euler/problems/p0014_longest_collatz_sequence/solution.py) | [Note](src/euler/problems/p0014_longest_collatz_sequence/README.md) |
| 15 | Lattice Paths | [Code](src/euler/problems/p0015_lattice_paths/solution.py) | [Note](src/euler/problems/p0015_lattice_paths/README.md) |
| 16 | Power Digit Sum | [Code](src/euler/problems/p0016_power_digit_sum/solution.py) | [Note](src/euler/problems/p0016_power_digit_sum/README.md) |
| 17 | Number Letter Counts | [Code](src/euler/problems/p0017_number_letter_counts/solution.py) | [Note](src/euler/problems/p0017_number_letter_counts/README.md) |
| 18 | Maximum Path Sum I | [Code](src/euler/problems/p0018_maximum_path_sum_i/solution.py) | [Note](src/euler/problems/p0018_maximum_path_sum_i/README.md) |
| 19 | Counting Sundays | [Code](src/euler/problems/p0019_counting_sundays/solution.py) | [Note](src/euler/problems/p0019_counting_sundays/README.md) |
| 20 | Factorial Digit Sum | [Code](src/euler/problems/p0020_factorial_digit_sum/solution.py) | [Note](src/euler/problems/p0020_factorial_digit_sum/README.md) |
| 21 | Amicable Numbers | [Code](src/euler/problems/p0021_amicable_numbers/solution.py) | [Note](src/euler/problems/p0021_amicable_numbers/README.md) |
| 22 | Names Scores | [Code](src/euler/problems/p0022_names_scores/solution.py) | [Note](src/euler/problems/p0022_names_scores/README.md) |
| 23 | Non-Abundant Sums | [Code](src/euler/problems/p0023_non_abundant_sums/solution.py) | [Note](src/euler/problems/p0023_non_abundant_sums/README.md) |
| 24 | Lexicographic Permutations | [Code](src/euler/problems/p0024_lexicographic_permutations/solution.py) | [Note](src/euler/problems/p0024_lexicographic_permutations/README.md) |
| 25 | 1000-digit Fibonacci Number | [Code](src/euler/problems/p0025_1000_digit_fibonacci_number/solution.py) | [Note](src/euler/problems/p0025_1000_digit_fibonacci_number/README.md) |
| 26 | Reciprocal Cycles | [Code](src/euler/problems/p0026_reciprocal_cycles/solution.py) | [Note](src/euler/problems/p0026_reciprocal_cycles/README.md) |
| 27 | Quadratic Primes | [Code](src/euler/problems/p0027_quadratic_primes/solution.py) | [Note](src/euler/problems/p0027_quadratic_primes/README.md) |
| 28 | Number Spiral Diagonals | [Code](src/euler/problems/p0028_number_spiral_diagonals/solution.py) | [Note](src/euler/problems/p0028_number_spiral_diagonals/README.md) |
| 29 | Distinct Powers | [Code](src/euler/problems/p0029_distinct_powers/solution.py) | [Note](src/euler/problems/p0029_distinct_powers/README.md) |
| 30 | Digit Fifth Powers | [Code](src/euler/problems/p0030_digit_fifth_powers/solution.py) | [Note](src/euler/problems/p0030_digit_fifth_powers/README.md) |
| 31 | Coin Sums | [Code](src/euler/problems/p0031_coin_sums/solution.py) | [Note](src/euler/problems/p0031_coin_sums/README.md) |
| 32 | Pandigital Products | [Code](src/euler/problems/p0032_pandigital_products/solution.py) | [Note](src/euler/problems/p0032_pandigital_products/README.md) |
| 33 | Digit Cancelling Fractions | [Code](src/euler/problems/p0033_digit_cancelling_fractions/solution.py) | [Note](src/euler/problems/p0033_digit_cancelling_fractions/README.md) |
| 34 | Digit Factorials | [Code](src/euler/problems/p0034_digit_factorials/solution.py) | [Note](src/euler/problems/p0034_digit_factorials/README.md) |
| 35 | Circular Primes | [Code](src/euler/problems/p0035_circular_primes/solution.py) | [Note](src/euler/problems/p0035_circular_primes/README.md) |
| 36 | Double-base Palindromes | [Code](src/euler/problems/p0036_double_base_palindromes/solution.py) | [Note](src/euler/problems/p0036_double_base_palindromes/README.md) |
| 37 | Truncatable Primes | [Code](src/euler/problems/p0037_truncatable_primes/solution.py) | [Note](src/euler/problems/p0037_truncatable_primes/README.md) |
| 38 | Pandigital Multiples | [Code](src/euler/problems/p0038_pandigital_multiples/solution.py) | [Note](src/euler/problems/p0038_pandigital_multiples/README.md) |
| 39 | Integer Right Triangles | [Code](src/euler/problems/p0039_integer_right_triangles/solution.py) | [Note](src/euler/problems/p0039_integer_right_triangles/README.md) |
| 40 | Champernowne's Constant | [Code](src/euler/problems/p0040_champernowne's_constant/solution.py) | [Note](src/euler/problems/p0040_champernowne's_constant/README.md) |
| 41 | Pandigital Prime | [Code](src/euler/problems/p0041_pandigital_prime/solution.py) | [Note](src/euler/problems/p0041_pandigital_prime/README.md) |
| 42 | Coded Triangle Numbers | [Code](src/euler/problems/p0042_coded_triangle_numbers/solution.py) | [Note](src/euler/problems/p0042_coded_triangle_numbers/README.md) |
| 43 | Sub-string Divisibility | [Code](src/euler/problems/p0043_sub_string_divisibility/solution.py) | [Note](src/euler/problems/p0043_sub_string_divisibility/README.md) |
| 44 | Pentagon Numbers | [Code](src/euler/problems/p0044_pentagon_numbers/solution.py) | [Note](src/euler/problems/p0044_pentagon_numbers/README.md) |
| 45 | Triangular, Pentagonal, and Hexagonal | [Code](src/euler/problems/p0045_triangular,_pentagonal,_and_hexagonal/solution.py) | [Note](src/euler/problems/p0045_triangular,_pentagonal,_and_hexagonal/README.md) |
| 46 | Goldbach's Other Conjecture | [Code](src/euler/problems/p0046_goldbach's_other_conjecture/solution.py) | [Note](src/euler/problems/p0046_goldbach's_other_conjecture/README.md) |
| 47 | Distinct Primes Factors | [Code](src/euler/problems/p0047_distinct_primes_factors/solution.py) | [Note](src/euler/problems/p0047_distinct_primes_factors/README.md) |
| 48 | Self Powers | [Code](src/euler/problems/p0048_self_powers/solution.py) | [Note](src/euler/problems/p0048_self_powers/README.md) |
| 49 | Prime Permutations | [Code](src/euler/problems/p0049_prime_permutations/solution.py) | [Note](src/euler/problems/p0049_prime_permutations/README.md) |
| 50 | Consecutive Prime Sum | [Code](src/euler/problems/p0050_consecutive_prime_sum/solution.py) | [Note](src/euler/problems/p0050_consecutive_prime_sum/README.md) |
| 51 | Prime Digit Replacements | [Code](src/euler/problems/p0051_prime_digit_replacements/solution.py) | [Note](src/euler/problems/p0051_prime_digit_replacements/README.md) |
| 52 | Permuted Multiples | [Code](src/euler/problems/p0052_permuted_multiples/solution.py) | [Note](src/euler/problems/p0052_permuted_multiples/README.md) |
| 53 | Combinatoric Selections | [Code](src/euler/problems/p0053_combinatoric_selections/solution.py) | [Note](src/euler/problems/p0053_combinatoric_selections/README.md) |
| 54 | Poker Hands | [Code](src/euler/problems/p0054_poker_hands/solution.py) | [Note](src/euler/problems/p0054_poker_hands/README.md) |
| 55 | Lychrel Numbers | [Code](src/euler/problems/p0055_lychrel_numbers/solution.py) | [Note](src/euler/problems/p0055_lychrel_numbers/README.md) |
| 56 | Powerful Digit Sum | [Code](src/euler/problems/p0056_powerful_digit_sum/solution.py) | [Note](src/euler/problems/p0056_powerful_digit_sum/README.md) |
| 57 | Square Root Convergents | [Code](src/euler/problems/p0057_square_root_convergents/solution.py) | [Note](src/euler/problems/p0057_square_root_convergents/README.md) |
| 58 | Spiral Primes | [Code](src/euler/problems/p0058_spiral_primes/solution.py) | [Note](src/euler/problems/p0058_spiral_primes/README.md) |
| 59 | XOR Decryption | [Code](src/euler/problems/p0059_xor_decryption/solution.py) | [Note](src/euler/problems/p0059_xor_decryption/README.md) |
| 60 | Prime Pair Sets | [Code](src/euler/problems/p0060_prime_pair_sets/solution.py) | [Note](src/euler/problems/p0060_prime_pair_sets/README.md) |
| 61 | Cyclical Figurate Numbers | [Code](src/euler/problems/p0061_cyclical_figurate_numbers/solution.py) | [Note](src/euler/problems/p0061_cyclical_figurate_numbers/README.md) |
