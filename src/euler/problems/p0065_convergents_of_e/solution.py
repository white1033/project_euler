def solve(n: int = 100) -> int:
    """
    Find the sum of digits in the numerator of the n-th convergent of the continued fraction for e.
    """
    # 1. Generate the sequence of coefficients a_0, a_1, ..., a_{n-1}
    # a_0 = 2
    # For k >= 1:
    #   if k % 3 == 2: a_k = 2 * (k + 1) // 3
    #   else:          a_k = 1

    # We need the n-th convergent.
    # Convergents are h_k / k_k
    # h_0 = a_0
    # h_1 = a_1 * a_0 + 1
    # h_k = a_k * h_{k-1} + h_{k-2}

    # We only need to track the numerators h_{k}, h_{k-1}, h_{k-2}

    # Initialize recurrence state
    # h_{-2} = 0, h_{-1} = 1
    # h_k = a_k * h_{k-1} + h_{k-2}

    h_minus_2 = 0
    h_minus_1 = 1

    current_h = 0

    for k in range(n):
        a_k = 2 if k == 0 else (2 * (k + 1) // 3 if k % 3 == 2 else 1)

        current_h = a_k * h_minus_1 + h_minus_2

        # Shift for next iteration
        h_minus_2 = h_minus_1
        h_minus_1 = current_h

    # After n iterations (k from 0 to n-1), current_h is h_{n-1}, which is the n-th convergent.

    # Sum of digits
    return sum(int(d) for d in str(current_h))
