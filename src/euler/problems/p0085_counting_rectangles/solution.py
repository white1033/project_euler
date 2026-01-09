from euler.utils.common import timeit


@timeit
def solve(target: int = 2_000_000) -> int:
    """
    Find the area of the grid with the nearest solution to containing `target` rectangles.
    """
    min_diff = float("inf")
    best_area = 0

    # Estimate upper bound for W.
    # If H=1, Count = W(W+1)/2.
    # W(W+1)/2 ~ target => W^2 ~ 2*target.
    # W ~ sqrt(2*target).
    # For 2,000,000, W ~ 2000.
    limit_w = 2000

    for w in range(1, limit_w + 1):
        for h in range(1, w + 1):  # Assume h <= w to avoid duplicates and symmetric cases
            rect_count = (w * (w + 1) // 2) * (h * (h + 1) // 2)

            diff = abs(target - rect_count)

            if diff < min_diff:
                min_diff = diff
                best_area = w * h

            if rect_count > target:
                # Since rect_count increases with h, any further h will be even further from target
                break

    return best_area


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
