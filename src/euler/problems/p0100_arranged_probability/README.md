# Arranged Probability

## Problem 100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, $P(BB) = (15/21) \times (14/20) = 1/2$.

The next such arrangement, for which there is exactly $50\%$ chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over $10^{12} = 1,000,000,000,000$ discs in total, determine the number of blue discs that the box would contain.

## Analysis

Let $b$ be the number of blue discs and $n$ be the total number of discs.
The probability of picking two blue discs is:
$$ P(BB) = \frac{b}{n} \times \frac{b-1}{n-1} = \frac{1}{2} $$
$$ 2b(b-1) = n(n-1) $$
$$ 2b^2 - 2b = n^2 - n $$
Multiply by 4 to complete the square easier:
$$ 8b^2 - 8b = 4n^2 - 4n $$
$$ 2(4b^2 - 4b + 1) - 2 = (2n - 1)^2 - 1 $$
$$ 2(2b - 1)^2 - 2 = (2n - 1)^2 - 1 $$
$$ 2(2b - 1)^2 - 1 = (2n - 1)^2 $$
$$ (2n - 1)^2 - 2(2b - 1)^2 = -1 $$

Let $X = 2n - 1$ and $Y = 2b - 1$.
The equation becomes the Pell-like equation:
$$ X^2 - 2Y^2 = -1 $$

### Solving the Diophantine Equation
The fundamental solution to $X^2 - 2Y^2 = -1$ is $(X_1, Y_1) = (1, 1)$ (trivial, $n=1, b=1$, prob 1? No, formula $1(0)/1(0)$ undefined/0).
The recurrence relation for solutions $(X_k, Y_k)$ can be derived from the fundamental solution of $u^2 - 2v^2 = 1$, which is $(3, 2)$.
$$ X_{k+1} + Y_{k+1}\sqrt{2} = (X_k + Y_k\sqrt{2})(3 + 2\sqrt{2}) $$
$$ X_{k+1} = 3X_k + 4Y_k $$
$$ Y_{k+1} = 2X_k + 3Y_k $$

We iterate until $n = (X+1)/2 > 10^{12}$. Then we calculate $b = (Y+1)/2$.
