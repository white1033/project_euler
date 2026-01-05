from collections import Counter
from pathlib import Path

from euler.utils.common import timeit

# Card Rank Mapping
RANK_MAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

def evaluate_hand(hand_str: list[str]) -> tuple:
    """
    Evaluates a poker hand and returns a tuple representing its strength.
    The tuple is designed such that Python's default comparison works correctly.
    
    Structure: (Rank, Tie_Breaker_1, Tie_Breaker_2, ...)
    """
    # Parse hand
    # Each card is like "8C", "TS", etc.
    # We separate ranks and suits
    ranks = sorted([RANK_MAP[c[0]] for c in hand_str], reverse=True)
    suits = [c[1] for c in hand_str]
    
    # Check for Flush and Straight
    is_flush = len(set(suits)) == 1
    
    # Check for Straight
    # Logic: Max - Min == 4 and unique count is 5 (no duplicates)
    # Special case: A, 2, 3, 4, 5 (Wheel) - Treated as 5-high straight if allowed?
    # Project Euler 54 usually assumes Ace is high only. But standard poker allows A-5.
    # Given the problem doesn't specify "Wheel", we assume standard A-high or 
    # simple consecutive check. We'll stick to simple consecutive for now.
    is_straight = (max(ranks) - min(ranks) == 4) and (len(set(ranks)) == 5)
    
    # Special Wheel Case: A, 5, 4, 3, 2 -> Ranks: [14, 5, 4, 3, 2]
    if ranks == [14, 5, 4, 3, 2]:
        is_straight = True
        ranks = [5, 4, 3, 2, 1] # Treat A as 1 for comparison purpose
    
    # Count frequencies for pairs, trips, quads
    counts = Counter(ranks)
    # Sort by count (desc), then by rank (desc)
    # Example: Full House 8s full of 5s -> [(8, 3), (5, 2)]
    sorted_counts = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    # Extract the rank structure for tie-breaking
    # e.g. for Full House, structure is (8, 5)
    rank_structure = tuple(r for r, c in sorted_counts)
    
    # Determine Hand Rank
    
    # 8. Straight Flush
    if is_straight and is_flush:
        return (8, ranks[0]) # Tie-break by highest card
        
    # 7. Four of a Kind
    if sorted_counts[0][1] == 4:
        # structure: (Quad_Rank, Kicker)
        return (7, ) + rank_structure
        
    # 6. Full House
    if sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
        # structure: (Trip_Rank, Pair_Rank)
        return (6, ) + rank_structure
        
    # 5. Flush
    if is_flush:
        # structure: (High1, High2, High3, High4, High5)
        return (5, ) + tuple(ranks)
        
    # 4. Straight
    if is_straight:
        # structure: (High_Rank)
        return (4, ranks[0])
        
    # 3. Three of a Kind
    if sorted_counts[0][1] == 3:
        # structure: (Trip_Rank, Kicker1, Kicker2)
        return (3, ) + rank_structure
        
    # 2. Two Pairs
    if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        # structure: (Pair1, Pair2, Kicker)
        return (2, ) + rank_structure
        
    # 1. One Pair
    if sorted_counts[0][1] == 2:
        # structure: (Pair, Kicker1, Kicker2, Kicker3)
        return (1, ) + rank_structure
        
    # 0. High Card
    # structure: (High1, High2, High3, High4, High5)
    return (0, ) + tuple(ranks)

@timeit
def solve() -> int:
    """
    Counts how many hands Player 1 wins in the poker.txt file.
    """
    # Locate the file relative to this script
    current_dir = Path(__file__).parent
    file_path = current_dir / "poker.txt"
    
    if not file_path.exists():
        print(f"Error: {file_path} not found.")
        return -1
        
    p1_wins = 0
    
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            cards = line.split()
            # First 5 cards: Player 1, Next 5: Player 2
            hand1 = cards[:5]
            hand2 = cards[5:]
            
            score1 = evaluate_hand(hand1)
            score2 = evaluate_hand(hand2)
            
            if score1 > score2:
                p1_wins += 1
                
    return p1_wins

if __name__ == "__main__":
    print(solve())