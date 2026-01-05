from euler.utils.common import timeit


def is_palindrome(n: int) -> bool:
    """Checks if a number is a palindrome."""
    s = str(n)
    return s == s[::-1]

def is_lychrel(n: int) -> bool:
    """
    Checks if n is a Lychrel number.
    Based on the problem statement, we assume a number is Lychrel if it does not 
    produce a palindrome within 50 iterations.
    """
    current = n
    for _ in range(50):
        # Reverse and add
        rev = int(str(current)[::-1])
        current += rev
        
        if is_palindrome(current):
            return False
            
    return True

@timeit
def solve() -> int:
    """
    How many Lychrel numbers are there below ten-thousand?
    """
    count = 0
    for n in range(1, 10000):
        if is_lychrel(n):
            count += 1
    return count

if __name__ == "__main__":
    print(solve())