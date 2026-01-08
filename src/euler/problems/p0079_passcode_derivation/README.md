# Problem 79: Passcode Derivation

## Problem Description

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, [keylog.txt](keylog.txt), contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

[Link to Problem](https://projecteuler.net/problem=79)

## Analysis

This problem asks us to reconstruct a sequence (the passcode) given multiple constraints on the relative order of its elements. This is a classic **Topological Sort** problem on a Directed Acyclic Graph (DAG).

### Graph Construction
1.  **Nodes**: Each unique digit appearing in the keylog (0-9).
2.  **Edges**: For each login attempt `ABC`, we have directed edges $A \rightarrow B$ and $B \rightarrow C$.
    *   $A \rightarrow B$ means A comes before B in the passcode.
    *   $B \rightarrow C$ means B comes before C in the passcode.

### Algorithm
We can use **Kahn's Algorithm** for topological sorting:
1.  Calculate the **in-degree** of each node (number of edges pointing to it).
2.  Initialize a queue with nodes that have an in-degree of 0 (these are candidates for the first digit).
3.  While the queue is not empty:
    *   Remove a node `u` from the queue and add it to the result passcode.
    *   For each neighbor `v` of `u` (i.e., edge $u \rightarrow v$):
        *   Decrement the in-degree of `v`.
        *   If `v`'s in-degree becomes 0, add `v` to the queue.
        
### Assumptions
The problem asks for the *shortest* possible passcode. Topological sort naturally produces a valid sequence that uses each node exactly once (assuming no cycles). This corresponds to the shortest passcode where no digit is repeated. If the graph contained cycles (e.g., $1 \rightarrow 2$ and $2 \rightarrow 1$), or if a digit needed to appear multiple times to satisfy the constraints, simple topological sort would fail or need modification. However, for this specific problem instance, the digits are unique and the graph is acyclic.

## Implementation

We implement Kahn's Algorithm in Python. We also sort the queue to ensure a deterministic output (lexicographically smallest) if there are multiple valid topological sorts, although in this problem the order is likely unique.

```python
def derive_passcode(logs):
    # ... (Graph building) ...
    # ... (Kahn's Algorithm) ...
    return result
```
