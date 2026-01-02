# Names Scores

## Problem Statement

Using `names.txt` (a 46K text file containing over five-thousand first names), begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the 938th name in the list. So, COLIN would obtain a score of $938 \times 53 = 49714$.

What is the total of all the name scores in the file?

## Analysis

This is a straightforward data processing task.

1.  **Input Parsing**: The file contains names enclosed in quotes and separated by commas (e.g., `"MARY","PATRICIA",...`). We need to strip the quotes and split by comma.
2.  **Sorting**: Sort the list of names alphabetically.
3.  **Scoring**:
    *   **Alphabetical Value**: Sum of character codes where 'A'=1, 'B'=2, ..., 'Z'=26. In Python, `ord(char) - 64` achieves this efficiently for uppercase letters.
    *   **Position**: The index in the sorted list + 1 (1-based index).
    *   **Name Score**: `Alphabetical Value * Position`.
4.  **Result**: Sum of all individual name scores.

### Complexity
*   **Time Complexity**: $O(N \log N)$ due to sorting, where $N$ is the number of names.
*   **Space Complexity**: $O(N)$ to store the names.