# Almost Equilateral Triangles

## Problem 94

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed 1,000,000,000.

## Analysis

Let the sides be $(a, a, b)$ where $b = a \pm 1$.
The semi-perimeter $s = \frac{a + a + b}{2} = \frac{2a + b}{2}$.
Area $A = \sqrt{s(s-a)(s-a)(s-b)}$.

Case 1: $b = a + 1$.
$s = \frac{3a+1}{2}$.
$s-a = \frac{a+1}{2} = \frac{b}{2}$.
$s-b = \frac{3a+1-2a-2}{2} = \frac{a-1}{2}$.
$A = \sqrt{\frac{3a+1}{2} \cdot \frac{a+1}{2} \cdot \frac{a+1}{2} \cdot \frac{a-1}{2}} = \frac{a+1}{4} \sqrt{(3a+1)(a-1)}$.
For $A$ to be integer, $(3a+1)(a-1)$ must be a square, say $y^2$.
$3a^2 - 2a - 1 = y^2$.
Multiply by 3: $9a^2 - 6a - 3 = 3y^2$.
$(3a-1)^2 - 4 = 3y^2 \implies (3a-1)^2 - 3y^2 = 4$.
Let $x = 3a-1$. Then $x^2 - 3y^2 = 4$.

Case 2: $b = a - 1$.
$s = \frac{3a-1}{2}$.
$s-a = \frac{a-1}{2}$.
$s-b = \frac{a+1}{2}$.
$A = \frac{a-1}{4} \sqrt{(3a-1)(a+1)}$.
Square condition: $(3a-1)(a+1) = y^2$.
$3a^2 + 2a - 1 = y^2$.
$(3a+1)^2 - 4 = 3y^2 \implies (3a+1)^2 - 3y^2 = 4$.
Let $x = 3a+1$. Then $x^2 - 3y^2 = 4$.

Both cases reduce to $x^2 - 3y^2 = 4$ (wait, Pell usually = 1).
However, solutions to $x^2 - 3y^2 = 4$ are related to solutions of $X^2 - 3Y^2 = 1$ multiplied by 2, or generated similarly.
Specifically, if $(u, v)$ is a solution to $u^2 - 3v^2 = 1$, then $x=2u, y=2v$ solves $x^2 - 3y^2 = 4(u^2 - 3v^2) = 4(1) = 4$.
So we can just use the standard Pell equation $x^2 - 3y^2 = 1$ solutions and multiply by 2?
Let's check.
$x^2 - 3y^2 = 1$ solutions $(x_k, y_k)$:
(2, 1), (7, 4), (26, 15)...
Multiply by 2:
(4, 2), (14, 8), (52, 30)...
Test against $x = 3a \pm 1$.
- (14, 8): $x=14$. $3a \pm 1 = 14$.
  - $3a+1=14 \implies 3a=13$ (no).
  - $3a-1=14 \implies 3a=15 \implies a=5$. Matches $(5, 5, 6)$.
- (52, 30): $x=52$.
  - $3a+1=52 \implies 3a=51 \implies a=17$. Matches $(17, 17, 16)$.
  - $3a-1=52 \implies 3a=53$ (no).

So valid $x$ values come from $2 \times x_{pell}$.
Since $x_{pell}$ alternates parity? No, recurrence $x_{k+1} = 2x_k + 3y_k$.
Starting (2, 1): $2(2)+3(1) = 7$ (odd).
Next: $2(7)+3(4) = 26$ (even).
Next: $2(26)+3(15) = 97$ (odd).
So $x_k$ alternates even/odd.
Wait, if $x_{pell}$ is even, then $2 x_{pell}$ is divisible by 4.
$3a \pm 1$ is never divisible by 3.
The condition $3a \pm 1 = 2 x_{pell}$ implies we find $a$.
Actually, the pattern found in logic was: use $x_{pell}$ directly in the formula $a = (2x_{pell} \pm 1)/3$.
Let's re-verify that.
If $x_{pell} = 7$, $a = (14+1)/3 = 5$.
If $x_{pell} = 26$, $a = (52-1)/3 = 17$.
If $x_{pell} = 97$, $a = (194+1)/3 = 65$.
Yes, this works. The variable $x$ in my solution code refers to $x_{pell}$.
The derived $x$ in analysis ($3a \pm 1$) corresponds to $2 \times x_{pell}$.

### Algorithm
1. Initialize $x=2, y=1$.
2. Iterate using recurrence $x_{new} = 2x + 3y, y_{new} = x + 2y$.
3. For each $x$, check if it yields a valid integer side $a$ and perimeter $\le 10^9$.
4. Add to sum.
