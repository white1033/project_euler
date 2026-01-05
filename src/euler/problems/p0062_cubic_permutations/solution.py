from collections import defaultdict

from euler.utils.common import timeit


@timeit
def solve(target_permutations: int = 5) -> int:
    """
    Find the smallest cube for which exactly `target_permutations` permutations of its digits are cube.
    """
    # Mapping from "sorted digit signature" to list of cubes
    # Key: str (e.g., "01234566")
    # Value: list[int] (e.g., [345^3, 384^3, ...])
    groups: dict[str, list[int]] = defaultdict(list)
    
    n = 1
    current_digit_length = 0
    
    while True:
        cube = n * n * n
        s_cube = str(cube)
        length = len(s_cube)
        
        # When digit length increases, we process the groups from the previous length
        if length > current_digit_length:
            # Check if any group found so far meets the condition
            candidates = []
            for members in groups.values():
                if len(members) == target_permutations:
                    candidates.append(members[0]) # The first member is the smallest
            
            if candidates:
                return min(candidates)
            
            # Reset for the new length
            groups.clear()
            current_digit_length = length
            
        # Add current cube to its group
        signature = "".join(sorted(s_cube))
        groups[signature].append(cube)
        
        n += 1
