# Cuboid Route

## Problem 86

A spider, S, sits in one corner of a cuboid room, measuring $6 \times 5 \times 3$, and a fly, F, sits in the opposite corner. By traveling on the surfaces of the room, the shortest "straight line" distance from S to F is $10$ and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid, corresponding to the three ways to unfold the net of the cuboid. If the dimensions are $a, b, c$, the squared distances are:
1. $a^2 + (b+c)^2$
2. $b^2 + (a+c)^2$
3. $c^2 + (a+b)^2$

Assuming $a \ge b \ge c$, the shortest distance is always $\sqrt{a^2 + (b+c)^2}$.

The shortest route has an integer length if $a^2 + (b+c)^2$ is a perfect square.

By considering all cuboid rooms with integer dimensions $M \times b \times c$, where $1 \le c \le b \le M$, it can be shown that there are exactly $2060$ distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of $M=100$, for which the shortest route has integer length.

Find the least value of $M$ such that the number of solutions first exceeds one million.

## Analysis

Let the dimensions of the cuboid be $a, b, c$ such that $1 \le c \le b \le a = M$.
The shortest path on the surface is given by $d = \sqrt{a^2 + (b+c)^2}$.
For $d$ to be an integer, $a^2 + (b+c)^2$ must be a perfect square.

Let $s = b + c$. Then $d = \sqrt{M^2 + s^2}$.
The constraints on $b$ and $c$ are $1 \le c \le b \le M$.
This implies the range of $s$:
- Minimum $s = 1 + 1 = 2$.
- Maximum $s = M + M = 2M$.

For a fixed $M$ and a fixed sum $s$, we need to count how many pairs $(b, c)$ satisfy $b+c=s$ and $1 \le c \le b \le M$.

**Case 1: $s \le M$**
Possible pairs are $(b, c) = (s-1, 1), (s-2, 2), \dots$.
We need $c \le b$.
Since $c = s - b$, this means $s - b \le b \implies s \le 2b \implies b \ge s/2$.
Also $b < s$ (since $c \ge 1$).
So $b$ ranges from $\lceil s/2 \rceil$ to $s-1$.
Wait, actually it's easier to count $c$.
$c$ ranges from $1$ up to $\lfloor s/2 \rfloor$.
Wait, $b \le M$ is automatically satisfied because $b = s - c < s \le M$.
So for a fixed $s \le M$, the number of pairs is $\lfloor s/2 \rfloor$.

**Case 2: $s > M$**
We still need $b \ge s/2$ (since $b \ge c$).
We also need $b \le M$.
So $b$ ranges from $\lceil s/2 \rceil$ to $M$.
The number of values is $M - \lceil s/2 \rceil + 1$.
Note that $\lceil s/2 \rceil = (s+1)//2$ using integer division.
So count is $M - (s+1)//2 + 1$.

### Algorithm
We iterate $M$ starting from 1 (or 100, since we know $M=100 \implies 2060$).
We maintain a running total of integer solutions.
For each new $M$, we only consider cuboids where the largest dimension is exactly $M$.
This means we set $a = M$ and iterate $s$ from $2$ to $2M$.
Check if $M^2 + s^2$ is a perfect square.
If yes, add the number of valid $(b, c)$ pairs for this $s$ to the total count.
Stop when total count $> 1,000,000$.
