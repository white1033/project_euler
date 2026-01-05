'''
Problem 27: Quadratic Primes
'''
from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes


@timeit
def solve() -> int:
    """
    Find the product of the coefficients, a and b, for the quadratic expression
    that produces the maximum number of primes for consecutive values of n, starting with n = 0.
    
    |a| < 1000, |b| <= 1000
    """
    # 1. Primes for primality testing.
    # Since n^2 + an + b can be larger than 1000, we need a larger sieve or a dedicated is_prime function.
    # Max n is likely < 100. Max val roughly 100^2 + 1000*100 + 1000 approx 111000.
    # But checking primality on the fly for numbers up to ~20000 might be fast enough without a huge sieve,
    # or just make a sieve up to 20000.
    # Let's use a reasonably large sieve for fast lookups.
    limit_sieve = 20000 # Heuristic limit
    primes_list = sieve_of_eratosthenes(limit_sieve)
    primes_set = set(primes_list)
    
    def is_prime_fast(n: int) -> bool:
        if n <= limit_sieve:
            return n in primes_set
        # Fallback for larger numbers (unlikely needed but safe)
        if n % 2 == 0: return False
        d = 3
        while d * d <= n:
            if n % d == 0: return False
            d += 2
        return True

    # 2. Candidate b's
    # When n=0, n^2+an+b = b. So b must be prime.
    # |b| <= 1000. Since we need positive primes for the sequence to start, b must be positive prime.
    candidate_bs = sieve_of_eratosthenes(1000)
    
    max_n = 0
    best_product = 0
    
    # 3. Iterate a and b
    for b in candidate_bs:
        for a in range(-999, 1000):
            n = 0
            while True:
                val = n*n + a*n + b
                if val > 1 and is_prime_fast(val):
                    n += 1
                else:
                    break
            
            if n > max_n:
                max_n = n
                best_product = a * b
                
    return best_product

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
