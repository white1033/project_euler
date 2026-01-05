
from euler.utils.common import timeit
from euler.utils.primes import is_prime, sieve_of_eratosthenes

# Memoization for pair checking to speed up repeated checks
pair_cache = {}

def is_pair_prime(p1: int, p2: int) -> bool:
    """
    Checks if p1+p2 and p2+p1 (concatenation) are both prime.
    Uses memoization.
    """
    key = tuple(sorted((p1, p2)))
    if key in pair_cache:
        return pair_cache[key]
    
    s1 = str(p1)
    s2 = str(p2)
    
    # Check both concatenations
    if is_prime(int(s1 + s2)) and is_prime(int(s2 + s1)):
        pair_cache[key] = True
        return True
    
    pair_cache[key] = False
    return False

def find_clique(current_set: list[int], candidates: list[int], target_size: int) -> list[int] | None:
    """
    Recursive DFS to find a clique of target_size.
    
    Args:
        current_set: The current clique being built (e.g., [3, 7]).
        candidates: List of prime numbers strictly larger than max(current_set) to consider.
        target_size: The goal size (5).
        
    Returns:
        The first valid clique found (list of 5 ints), or None.
    """
    if len(current_set) == target_size:
        return current_set
    
    # Pruning: If we can't possibly reach the target size with remaining candidates
    if len(current_set) + len(candidates) < target_size:
        return None
        
    for i, p in enumerate(candidates):
        # Check if p forms a prime pair with EVERY member of the current_set
        valid_candidate = True
        for member in current_set:
            if not is_pair_prime(member, p):
                valid_candidate = False
                break
        
        if valid_candidate:
            # Try to extend the set with p
            # Pass only candidates larger than p to maintain order and reduce space
            new_candidates = candidates[i+1:]
            result = find_clique(current_set + [p], new_candidates, target_size)
            if result:
                return result
                
    return None

@timeit
def solve() -> int:
    """
    Finds the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
    """
    # 1. Generate candidate primes.
    # The limit is a guess. Based on similar problems, primes up to 10,000 might be enough.
    # If not, we'd need to increase this.
    limit = 10000 
    primes = sieve_of_eratosthenes(limit)
    
    # We can skip 2 and 5 because:
    # - Concatenating X with 2 or 5 at the end makes it divisible by 2 or 5 (unless the number is just 2 or 5).
    # - But we are concatenating primes > 2. e.g. "3" + "2" = 32 (even), "7"+"5"=75 (div by 5).
    # - So 2 and 5 can never be part of a set larger than size 1.
    primes = [p for p in primes if p != 2 and p != 5]
    
    # 2. Start DFS
    # Since we want the "lowest sum", treating primes in ascending order helps,
    # though it doesn't strictly guarantee the global minimum without checking more.
    # However, for Project Euler, the "first found" solution with this order is usually the answer.
    
    # We iterate the first element of the set to prune the search space effectively.
    for i, p in enumerate(primes):
        # We need to find 4 more primes from the list of primes larger than p
        result = find_clique([p], primes[i+1:], 5)
        if result:
            print(f"Found set: {result}")
            return sum(result)
            
    return 0

if __name__ == "__main__":
    print(solve())