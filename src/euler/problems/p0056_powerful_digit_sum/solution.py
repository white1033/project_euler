from euler.utils.common import timeit


def sum_digits(n: int) -> int:
    """Calculates the sum of digits of n."""
    return sum(int(d) for d in str(n))

@timeit
def solve() -> int:
    """
    Finds the maximum digital sum of a^b for a, b < 100.
    """
    max_sum = 0
    
    # We iterate a and b from 1 to 99.
    # Heuristic optimization:
    # 1. We need large numbers to have large digit sums. 
    #    The number of digits is proportional to b * log(a).
    #    So we can likely skip small a and b.
    # 2. Multiples of 10 end in zeros, which don't contribute to the sum.
    #    However, skipping them is just a minor optimization. 
    #    Given the small search space (100x100), brute force is instant.
    
    for a in range(1, 100):
        # Optional: Skip multiples of 10 as they just append zeros compared to a/10
        # if a % 10 == 0: continue 
        
        for b in range(1, 100):
            # Calculate a^b using Python's arbitrary precision integers
            number = a ** b
            current_sum = sum_digits(number)
            
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum

if __name__ == "__main__":
    print(solve())