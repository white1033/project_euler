'''
Problem 31: Coin Sums
'''
from euler.utils.common import timeit


@timeit
def solve(target: int = 200) -> int:
    """
    How many different ways can target (default £2 = 200p) be made using any number of coins?
    Coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    # dp[i] will store the number of ways to make amount i
    dp = [0] * (target + 1)
    dp[0] = 1 # There is one way to make 0: use no coins
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
            
    return dp[target]

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
