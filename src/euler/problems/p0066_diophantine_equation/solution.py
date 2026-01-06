import math


def solve(limit: int = 1000) -> int:
    """
    Find the value of D <= limit in minimal solutions of x for which the largest value of x
    is obtained.
    Equation: x^2 - D * y^2 = 1
    """
    max_x = 0
    result_D = 0
    
    for D in range(2, limit + 1):
        limit_root = math.isqrt(D)
        if limit_root * limit_root == D:
            continue
            
        # Continued Fraction Algorithm to find fundamental solution (x, y)
        # We generate coefficients a_k and convergents h_k/k_k simultaneously.
        
        # Initial state for Continued Fraction (Problem 64 logic)
        m = 0
        d = 1
        a0 = limit_root
        a = a0
        
        # Initial state for Convergents (Problem 65 logic)
        # h_{-2} = 0, h_{-1} = 1
        # k_{-2} = 1, k_{-1} = 0
        h_prev2, h_prev1 = 0, 1
        k_prev2, k_prev1 = 1, 0
        
        # The first convergent is based on a0
        # h_0 = a0 * h_{-1} + h_{-2} = a0 * 1 + 0 = a0
        # k_0 = a0 * k_{-1} + k_{-2} = a0 * 0 + 1 = 1
        
        # We can treat the loop as generating a_k for k=0, 1, 2...
        # But actually, the check condition x^2 - Dy^2 = 1 needs to be checked 
        # for each convergent.
        
        # Let's handle the first term (k=0) separately or integrate it.
        # k=0: x = a0, y = 1. check: a0^2 - D*1^2 = 1 ? (Impossible unless D is trivial, but D>=2)
        
        # We start loop from finding a1, a2...
        # But we need current x, y variables.
        
        x = a0
        y = 1
        
        # State update for next iteration
        h_prev2, h_prev1 = 1, a0
        k_prev2, k_prev1 = 0, 1
        
        while True:
            # Check if current (x, y) is a solution
            # Note: We use the definition x^2 - Dy^2 = 1
            if x * x - D * y * y == 1:
                if x > max_x:
                    max_x = x
                    result_D = D
                break
            
            # Generate next continued fraction coefficient (a_{k+1})
            # Standard algorithm:
            m = d * a - m
            d = (D - m * m) // d
            a = (a0 + m) // d
            
            # Update convergents to get new x, y
            # x_new = a * x_old + x_older
            # y_new = a * y_old + y_older
            
            x_next = a * h_prev1 + h_prev2
            y_next = a * k_prev1 + k_prev2
            
            # Shift states
            h_prev2, h_prev1 = h_prev1, x_next
            k_prev2, k_prev1 = k_prev1, y_next
            
            x = x_next
            y = y_next
            
    return result_D