"""
Problem 47: Distinct Primes Factors
"""

from euler.utils.common import timeit


@timeit
def solve():
    """
    Find the first four consecutive integers to have four distinct prime factors each.
    What is the first of these numbers?
    """
    # Estimate upper bound. 
    # Smallest number with 4 distinct prime factors is 2*3*5*7 = 210.
    # The answer is likely in the range of hundreds of thousands.
    # Let's try a sieve up to 200,000 first. If not found, we can increase.
    limit = 200_000
    
    while True:
        factors_count = [0] * limit
        
        # Sieve approach to count distinct prime factors
        for i in range(2, limit):
            # If factors_count[i] is 0, then i is prime
            if factors_count[i] == 0:
                # Iterate through all multiples of i
                for j in range(i, limit, i):
                    factors_count[j] += 1
        
        # Search for 4 consecutive numbers with 4 distinct prime factors
        # Optimization: We can skip by 1, but we need to track consecutive count.
        consecutive = 0
        target = 4
        
        for i in range(210, limit): # Start from 210 as it's the min possible
            if factors_count[i] == target:
                consecutive += 1
                if consecutive == target:
                    return i - target + 1
            else:
                consecutive = 0
        
        # If not found, increase limit and retry (though 200k should be enough based on typical PE problems)
        # For safety, let's just double it.
        print(f"Not found within {limit}, increasing limit...")
        limit *= 2


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")