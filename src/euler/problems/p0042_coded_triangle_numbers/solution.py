"""
Problem 42: Coded Triangle Numbers
"""
import os
import math
from euler.utils.common import timeit


def get_word_value(word: str) -> int:
    """
    Calculate the word value by summing the alphabetical positions of its characters.
    A=1, B=2, ..., Z=26
    """
    value = 0
    for char in word:
        # 'A' is 65 in ASCII. So char code - 64 gives 1 for A.
        value += ord(char) - 64
    return value


def is_triangle_number(x: int) -> bool:
    """
    Check if x is a triangle number.
    t_n = 0.5 * n * (n + 1) = x
    => n^2 + n - 2x = 0
    => n = (-1 + sqrt(1 + 8x)) / 2
    
    For n to be an integer:
    1. 1 + 8x must be a perfect square.
    2. sqrt(1 + 8x) must be odd (since -1 + odd = even, even/2 is int).
    """
    if x <= 0:
        return False
        
    discriminant = 1 + 8 * x
    root = int(math.isqrt(discriminant))
    
    return (root * root == discriminant) and (root % 2 != 0)


@timeit
def solve():
    """
    Using words.txt, a 16K text file containing nearly two-thousand common English words, 
    how many are triangle words?
    """
    file_path = os.path.join(os.path.dirname(__file__), "words.txt")
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return 0

    with open(file_path, 'r') as f:
        content = f.read()
        
    # The file format is "WORD","WORD","WORD"...
    # We remove quotes and split by comma.
    words = content.replace('"', '').split(',')
    
    triangle_word_count = 0
    for word in words:
        if is_triangle_number(get_word_value(word)):
            triangle_word_count += 1
            
    return triangle_word_count


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")