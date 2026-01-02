'''
Problem 26: Reciprocal Cycles
'''
from euler.utils.common import timeit

def get_cycle_length(d: int) -> int:
    """
    Calculates the length of the recurring cycle in 1/d.
    Uses long division simulation.
    """
    remainders = {}
    value = 1
    position = 0
    
    while value != 0:
        if value in remainders:
            return position - remainders[value]
        
        remainders[value] = position
        value = (value * 10) % d
        position += 1
        
    return 0 # Terminating decimal

@timeit
def solve(limit: int = 1000) -> int:
    """
    Find the value of d < limit for which 1/d contains the longest recurring cycle.
    """
    max_length = 0
    max_d = 0
    
    # Iterate from limit-1 down to 2
    # Optimization: The max cycle length for d is d-1.
    # If we find a cycle length of K, we don't need to check any d <= K.
    for d in range(limit - 1, 1, -1):
        if max_length >= d:
            break
            
        length = get_cycle_length(d)
        if length > max_length:
            max_length = length
            max_d = d
            
    return max_d

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
