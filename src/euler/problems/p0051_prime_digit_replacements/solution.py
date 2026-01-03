from euler.utils.primes import sieve_of_eratosthenes, is_prime
from euler.utils.common import timeit

def get_family_size(pattern: str) -> list[int]:
    """
    Given a pattern like '56**3', returns the list of primes in this family.
    Replaces '*' with 0-9.
    """
    family = []
    for digit in '0123456789':
        # Skip leading zeros
        if pattern[0] == '*' and digit == '0':
            continue
            
        # Create the number string
        num_str = pattern.replace('*', digit)
        num = int(num_str)
        
        # We assume the input provided to the main loop comes from a prime list,
        # but the generated numbers need to be checked.
        # Note: We use is_prime here. Since we sieve up to 1M, 
        # and we assume the answer is within 1M, is_prime is fast enough.
        # If the number exceeds the sieve limit, is_prime handles it correctly.
        if is_prime(num):
            family.append(num)
            
    return family

@timeit
def solve() -> int:
    """
    Finds the smallest prime which, by replacing part of the number 
    (not necessarily adjacent digits) with the same digit, 
    is part of an eight prime value family.
    """
    # Generate primes up to 1,000,000 (likely 6 digits)
    # The example 56003 is ~50k. We need 8 primes, so likely slightly larger.
    primes = sieve_of_eratosthenes(1000000)
    
    # Pre-calculate string representations to avoid doing it repeatedly
    # Though doing it on the fly is memory efficient and CPU is likely fine.
    
    for p in primes:
        s = str(p)
        
        # We only care about numbers where a digit repeats 3 times.
        # Based on the "Modulo 3" arithmetic logic, the number of replacements
        # must be a multiple of 3 (so 3, 6, 9...). 
        # Since we want the smallest, we start with 3 replacements.
        
        # Also, we only need to check repeating digits 0, 1, and 2.
        # Why? Because we need a family of 8 primes. 
        # There are only 10 digits (0-9). We can afford at most 2 failures.
        # If the smallest prime in the family has a repeating digit of '3',
        # it implies that the versions with '0', '1', and '2' were ALL composite.
        # That's 3 failures. 10 - 3 = 7 max primes. Impossible to reach 8.
        # Therefore, the first prime found in an 8-prime family MUST have
        # the repeating digit as 0, 1, or 2.
        
        for duplicate in ['0', '1', '2']:
            if s.count(duplicate) == 3:
                # Create the pattern mask (e.g., 121313 with '1' -> *2*3*3)
                pattern = s.replace(duplicate, '*')
                
                # Check the family size
                family = get_family_size(pattern)
                
                if len(family) == 8:
                    # Return the smallest prime in the family
                    # (which should be the first one, family[0])
                    return family[0]
                    
    return -1

if __name__ == "__main__":
    print(solve())