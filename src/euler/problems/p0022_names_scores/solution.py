'''
Problem 22: Names Scores
'''
import os
from pathlib import Path
from euler.utils.common import timeit

def get_name_score(name: str, position: int) -> int:
    """
    Calculates the score of a name based on its alphabetical value and position.
    COLIN = 3 + 15 + 12 + 9 + 14 = 53
    Score = 53 * position
    """
    # ord('A') is 65. So ord(char) - 64 gives A=1, B=2, etc.
    letter_sum = sum(ord(char) - 64 for char in name)
    return letter_sum * position

@timeit
def solve(file_path: str = "names.txt"):
    """
    Using names.txt, begin by sorting it into alphabetical order.
    Then working out the alphabetical value for each name, multiply this value 
    by its alphabetical position in the list to obtain a name score.
    """
    # Resolve file path relative to this script
    current_dir = Path(__file__).parent
    target_file = current_dir / file_path
    
    if not target_file.exists():
        # Fallback or error message if user hasn't provided the file yet
        return f"Error: File {target_file} not found. Please provide names.txt."
        
    with open(target_file, 'r') as f:
        content = f.read()
        
    # The file format is likely "MARY","PATRICIA","LINDA",...
    # We remove quotes and split by comma
    names = [name.strip('"') for name in content.split(',')]
    names.sort()
    
    total_score = 0
    for i, name in enumerate(names):
        # Position starts at 1
        total_score += get_name_score(name, i + 1)
        
    return total_score

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
