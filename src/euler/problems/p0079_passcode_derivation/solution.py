"""
Problem 79: Passcode Derivation
"""

from pathlib import Path

from euler.utils.common import timeit


def derive_passcode(logs: list[str]) -> str:
    """
    Derives the shortest passcode from a list of sequential observations.
    Uses Topological Sort (Kahn's Algorithm).
    """
    graph = {}
    in_degree = {}
    nodes = set()

    # Initialize graph structure
    for log in logs:
        # Ensure log has at least 2 chars to form an edge, but problem says 3.
        # "319" implies 3->1 and 1->9
        chars = list(log)
        for char in chars:
            nodes.add(char)
            if char not in graph:
                graph[char] = set()
            if char not in in_degree:
                in_degree[char] = 0

        # Create edges: c1->c2, c2->c3, ...
        for i in range(len(chars) - 1):
            u, v = chars[i], chars[i + 1]
            if v not in graph[u]:
                graph[u].add(v)
                # We calculate in-degree later or update dynamically

    # Calculate in-degrees based on unique edges
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    # Kahn's Algorithm
    # Start with nodes having 0 in-degree
    queue = [n for n in nodes if in_degree[n] == 0]
    # Sort to ensure deterministic output if multiple valid paths exist
    queue.sort()

    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)

        if u in graph:
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

            # Re-sort queue to maintain deterministic order (lexicographical)
            queue.sort()

    if len(result) != len(nodes):
        # This happens if there's a cycle (e.g. 1->2->1)
        raise ValueError("Cycle detected! Cannot determine a unique order.")

    return "".join(result)


@timeit
def solve() -> int:
    path = Path(__file__).parent / "keylog.txt"
    with open(path) as f:
        logs = [line.strip() for line in f if line.strip()]

    # Result is a string of digits, usually convert to int for PE
    return int(derive_passcode(logs))


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
