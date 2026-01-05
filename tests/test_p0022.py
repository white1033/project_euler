from euler.problems.p0022_names_scores.solution import get_name_score


def test_p0022_score_logic():
    # COLIN = 3 + 15 + 12 + 9 + 14 = 53
    # If COLIN is the 938th name
    assert get_name_score("COLIN", 938) == 49714

def test_p0022_solution():
    # We can't test the full solution without the file.
    # We can perhaps mock the file reading if we wanted to be strict,
    # but for now we will skip the integration test until the file is present.
    # Or we can create a dummy file for testing?
    from pathlib import Path

    from euler.problems.p0022_names_scores.solution import solve
    
    # Create a temporary test file
    test_content = '"COLIN","ALICE","BOB"'
    # Sorted: ALICE (1), BOB (2), COLIN (3)
    # ALICE: 1+12+9+3+5 = 30 * 1 = 30
    # BOB: 2+15+2 = 19 * 2 = 38
    # COLIN: 53 * 3 = 159
    # Total: 30 + 38 + 159 = 227
    
    # We need to put this file where the solution expects it relative to itself,
    # OR we modify solve to accept content?
    # The solution accepts `file_path`.
    
    test_file_path = Path("src/euler/problems/p0022_names_scores/test_names.txt")
    with open(test_file_path, "w") as f:
        f.write(test_content)
        
    try:
        assert solve("test_names.txt") == 227
    finally:
        if test_file_path.exists():
            test_file_path.unlink()
