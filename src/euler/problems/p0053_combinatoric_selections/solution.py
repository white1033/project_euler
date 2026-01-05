from euler.utils.common import timeit


@timeit
def solve() -> int:
    """
    How many, not necessarily distinct, values of (n choose r) 
    for 1 <= n <= 100, are greater than one-million?
    """
    limit = 1_000_000
    count = 0
    
    # We are told that n=23 is the first value to exceed 1M.
    for n in range(23, 101):
        # We take advantage of the symmetry and unimodality of Pascal's triangle.
        # The values increase from r=0 to n/2.
        # Once we find the first 'r' such that C(n, r) > 1M,
        # all values from 'r' to 'n-r' will also be > 1M.
        
        # We compute C(n, r) iteratively to avoid large factorials.
        # C(n, r) = C(n, r-1) * (n - r + 1) / r
        
        val = 1 # C(n, 0)
        for r in range(1, n // 2 + 1):
            # Iterative update: val = val * (n - (r - 1)) / r
            # Simplified: val = val * (n - r + 1) / r
            val = val * (n - r + 1) // r
            
            if val > limit:
                # We found the first r.
                # The valid range is [r, n-r].
                # The number of terms is (n - r) - r + 1 = n + 1 - 2*r
                count += (n + 1) - 2 * r
                
                # We don't need to check further for this n
                break
                
    return count

if __name__ == "__main__":
    print(solve())