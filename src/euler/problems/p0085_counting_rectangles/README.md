# Problem 85: Counting Rectangles

## Description
By counting carefully it can be seen that a rectangular grid measuring $3$ by $2$ contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

[Link to Problem](https://projecteuler.net/problem=85)

## Analysis

### Formula for Number of Rectangles
In a grid of size $W \times H$, a rectangle is defined by choosing 2 distinct vertical lines from the $W+1$ vertical grid lines, and 2 distinct horizontal lines from the $H+1$ horizontal grid lines.

Number of ways to choose 2 vertical lines:
$$ \binom{W+1}{2} = \frac{(W+1)W}{2} $$

Number of ways to choose 2 horizontal lines:
$$ \binom{H+1}{2} = \frac{(H+1)H}{2} $$

The total number of rectangles $C(W, H)$ is the product:
$$ C(W, H) = \frac{W(W+1)}{2} \times \frac{H(H+1)}{2} $$

This can also be seen as: Sum of integers $1..W$ multiplied by Sum of integers $1..H$.

### Algorithm
We want to find $W, H$ such that $C(W, H) \approx 2,000,000$.
Let the target be $T = 2,000,000$.

1.  **Bounds**:
    Assume $H=1$. Then $C(W, 1) = \frac{W(W+1)}{2}$.
    $$ \frac{W^2}{2} \approx T \implies W \approx \sqrt{2T} \approx \sqrt{4,000,000} = 2000 $$
    So we only need to search $W$ up to approx 2000.
    Since we can swap $W$ and $H$, we can assume $H \le W$ and iterate $W$ from 1 to 2000, and $H$ from 1 to $W$.

2.  **Search**:
    Iterate $W$ and $H$. Calculate $C(W, H)$.
    Track the pair $(W, H)$ that minimizes $|C(W, H) - T|$.
    The answer is the area $W \times H$.

## Complexity
*   **Time Complexity**: $O(\sqrt{T} \times \sqrt{T}) = O(T)$.
    Actually, since inner loop stops when $C > T$, the complexity is much lower.
    Roughly we check $W$ up to 2000.
    Inner loop runs $H$ up to $W$ but breaks early.
    Total operations roughly $2000 \times \text{small factor}$. Very fast.
*   **Space Complexity**: $O(1)$.
