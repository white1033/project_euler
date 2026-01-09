import heapq
from pathlib import Path

from euler.utils.common import timeit


@timeit
def solve():
    current_dir = Path(__file__).parent

    possible_files = ["0083_matrix.txt", "matrix.txt"]
    matrix_path = None

    for fname in possible_files:
        p = current_dir / fname
        if p.exists():
            matrix_path = p
            break

    if not matrix_path:
        raise FileNotFoundError(f"Could not find matrix file in {current_dir}")

    with open(matrix_path) as f:
        matrix = [[int(num) for num in line.strip().split(",")] for line in f if line.strip()]

    rows = len(matrix)
    cols = len(matrix[0])
    target = (rows - 1, cols - 1)

    # Dijkstra's Algorithm
    # Priority Queue stores: (cost, r, c)
    pq = [(matrix[0][0], 0, 0)]

    # Distance matrix to keep track of minimum cost to reach each cell
    # Initialize with infinity
    min_dist = [[float("inf")] * cols for _ in range(rows)]
    min_dist[0][0] = matrix[0][0]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while pq:
        cost, r, c = heapq.heappop(pq)

        # If we reached the bottom-right corner, return the cost
        if (r, c) == target:
            return cost

        # Optimization: If current path is worse than already found, skip
        if cost > min_dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = cost + matrix[nr][nc]

                if new_cost < min_dist[nr][nc]:
                    min_dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

    return -1  # Should not be reached


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
