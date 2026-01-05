'''
Problem 32: Pandigital Products
'''
from euler.utils.common import timeit


def is_pandigital(n_str: str) -> bool:
    """
    Checks if the string contains digits 1-9 exactly once.
    """
    if len(n_str) != 9:
        return False
    return sorted(n_str) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

@timeit
def solve() -> int:
    """
    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    """
    products = set()
    
    # We deduced that the product must be 4 digits.
    # Case 1: 1-digit * 4-digit = 4-digit
    # Iterate a from 1 to 9
    for a in range(1, 10):
        # b can range from 1234 to 9876/a
        # But actually b must be such that product is 4 digits.
        # Min product 1234, Max product 9876.
        # So b >= 1234/a, b <= 9876/a
        start_b = 1234 // a
        if start_b < 1234: start_b = 1234 # b must be 4 digits
        end_b = 9876 // a
        
        for b in range(start_b, end_b + 1):
            product = a * b
            identity_str = str(a) + str(b) + str(product)
            if is_pandigital(identity_str):
                products.add(product)
                
    # Case 2: 2-digit * 3-digit = 4-digit
    # Iterate a from 12 to 98
    for a in range(12, 99):
        # b must be 3 digits
        start_b = 123
        end_b = 9876 // a
        if end_b > 987: end_b = 987
        
        for b in range(start_b, end_b + 1):
            product = a * b
            identity_str = str(a) + str(b) + str(product)
            if is_pandigital(identity_str):
                products.add(product)
                
    return sum(products)

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
