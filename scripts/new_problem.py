import sys
from pathlib import Path


def create_problem(problem_id: int, name: str = "problem"):
    # Format folder name, e.g., p0001_multiples_of_3_and_5
    folder_name = f"p{problem_id:04d}_{name.lower().replace(' ', '_').replace('-', '_')}"
    base_path = Path("src/euler/problems") / folder_name
    
    if base_path.exists():
        print(f"Error: Directory {base_path} already exists!")
        return

    base_path.mkdir(parents=True)
    (base_path / "__init__.py").touch()

    # Create solution.py template
    solution_code = f"""'''
Problem {problem_id}: {name}
'''
from euler.utils.common import timeit

@timeit
def solve():
    # Write your solution here
    return None

if __name__ == "__main__":
    result = solve()
    print(f"Result: {{result}}")
"""
    with open(base_path / "solution.py", "w") as f:
        f.write(solution_code)

    # Create README.md template
    readme_content = f"""# Problem {problem_id}: {name}

## Description
<!-- Paste problem description here -->
[Link to Problem](https://projecteuler.net/problem={problem_id})

## Analysis
<!-- Mathematical derivation or logic -->

## Implementation
<!-- Notes on code implementation -->
"""
    with open(base_path / "README.md", "w") as f:
        f.write(readme_content)

    print(f"✅ Created problem structure at: {base_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: uv run scripts/new_problem.py <id> [name]")
        sys.exit(1)
    
    try:
        p_id = int(sys.argv[1])
    except ValueError:
        print("Error: Problem ID must be an integer.")
        sys.exit(1)

    p_name = sys.argv[2] if len(sys.argv) > 2 else "New Problem"
    create_problem(p_id, p_name)
