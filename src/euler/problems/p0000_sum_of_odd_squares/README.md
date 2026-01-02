# Problem 0: Sum of odd squares

## Description

A number is a perfect square if it is the square of a positive integer.
For example, $25 = 5^2$ is a square number, and it is also an odd square.

The first 5 square numbers are $1, 4, 9, 16, 25$.
The sum of the odd squares among them is $1 + 9 + 25 = 35$.

**Goal:** Among the first **491,000** square numbers, what is the sum of all the odd squares?

## Analysis

Let $N = 491,000$.
The sequence of the first $N$ square numbers is $1^2, 2^2, 3^2, \dots, N^2$.
We know that $k^2$ is odd if and only if $k$ is odd.
Therefore, the problem asks for the sum:
$$ \sum_{\substack{1 \le k \le N \\ k \text{ is odd}}} k^2 $$

### Method 1: Iteration (Brute Force)
We can simply iterate from 1 to $N$ with a step of 2 ($1, 3, 5, \dots$) and sum their squares.
Since $N \approx 5 \times 10^5$, this requires about 250,000 operations, which is trivial for a modern computer (microseconds).

### Method 2: Mathematical Closed Form ($O(1)$)
For larger $N$, a closed-form solution is preferred.

The sum of the first $n$ integers squared is given by the formula:
$$ S_n = \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} $$

We can express the sum of odd squares ($S_{odd}$) as the sum of all squares ($S_{total}$) minus the sum of even squares ($S_{even}$).

1.  **Total Sum ($S_{total}$)**:
    $$ S_{total} = \sum_{i=1}^N i^2 = S_N $$

2.  **Even Sum ($S_{even}$)**:
    The even numbers up to $N$ are $2, 4, 6, \dots, 2m$, where $m = \lfloor \frac{N}{2} \rfloor$.
    $$ S_{even} = \sum_{j=1}^m (2j)^2 = \sum_{j=1}^m 4j^2 = 4 \sum_{j=1}^m j^2 = 4 S_m $$

3.  **Result**:
    $$ S_{odd} = S_N - 4 S_m $$

In this problem, $N = 491,000$.
$$ m = \lfloor 491000 / 2 \rfloor = 245,500 $$

## Implementation Notes
We will implement the formula approach for efficiency and demonstration of mathematical properties.