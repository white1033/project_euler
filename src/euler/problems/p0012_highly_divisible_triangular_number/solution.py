'''
Problem 12: Highly Divisible Triangular Number
'''
from euler.utils.common import timeit
from euler.utils.primes import count_divisors


@timeit
def solve(target_divisors: int = 500) -> int:
    """
    Finds the first triangle number with over `target_divisors` divisors.
    
    T_n = n * (n + 1) / 2
    
    Since n and n+1 are coprime:
    If n is even: T_n = (n/2) * (n+1) => d(T_n) = d(n/2) * d(n+1)
    If n is odd:  T_n = n * ((n+1)/2) => d(T_n) = d(n) * d((n+1)/2)
    
    We can iterate n and keep track of d(n) and d(n+1).
    """
    n = 1
    # We can cache the count of divisors to avoid recomputing.
    # When moving from n to n+1, the old "right" term becomes the new "left" term.
    # But wait, n+1 in one step is n in the next step.
    # Let's just compute efficiently. 
    # d_n = count_divisors(n)
    # d_next = count_divisors(n + 1)
    
    # Actually, the terms are (n) and (n+1). 
    # One is divided by 2.
    # Let's just keep it simple.
    
    while True:
        # Calculate d(T_n)
        if n % 2 == 0:
            term1 = n // 2
            term2 = n + 1
        else:
            term1 = n
            term2 = (n + 1) // 2
            
        divisors = count_divisors(term1) * count_divisors(term2)
        
        if divisors > target_divisors:
            return n * (n + 1) // 2
            
        n += 1

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
