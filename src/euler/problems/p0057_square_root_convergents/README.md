# Square Root Convergents

## Problem Statement

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

$$ \sqrt{2} = 1 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \dots}}} $$

By expanding this for the first four iterations, we get:

$$ 1 + \frac{1}{2} = \frac{3}{2} = 1.5 $$
$$ 1 + \frac{1}{2 + \frac{1}{2}} = 1 + \frac{1}{\frac{5}{2}} = 1 + \frac{2}{5} = \frac{7}{5} = 1.4 $$
$$ 1 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}} = 1 + \frac{1}{2 + \frac{2}{5}} = 1 + \frac{1}{\frac{12}{5}} = 1 + \frac{5}{12} = \frac{17}{12} = 1.41666 \dots $$
$$ 1 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}}} = 1 + \frac{1}{2 + \frac{5}{12}} = 1 + \frac{1}{\frac{29}{12}} = 1 + \frac{12}{29} = \frac{41}{29} = 1.41379 \dots $$

The next three expansions are $\frac{99}{70}$, $\frac{239}{169}$, and $\frac{577}{408}$, but the eighth expansion, $\frac{1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

## Solution Analysis

### Recursive Relation

Let the $k$-th convergent be denoted as $\frac{N_k}{D_k}$.
We are given:
$$ \sqrt{2} = 1 + \frac{1}{2 + (\sqrt{2} - 1)} $$
Actually, let's look at the structure more simply.
The fraction part (excluding the initial $1$) is:
$$ f_k = \frac{1}{2 + f_{k-1}} $$
where $f_0 = 0$ is not quite right because the sequence starts at $1 + 1/2$.

Let's try the full expression.
Let the expansion be $a_k$.
$$ a_1 = 1 + \frac{1}{2} = \frac{3}{2} $$
$$ a_2 = 1 + \frac{1}{2 + \frac{1}{2}} = 1 + \frac{1}{1 + a_1} $$
Wait, this recursive definition is tricky because the "infinite" part is at the bottom.

Let's use the property derived from the observation:
If $a_k = \frac{N_k}{D_k}$, then the next term is obtained by replacing the last $\frac{1}{2}$ with $\frac{1}{2 + \frac{1}{2}}$.
Actually, a simpler recurrence relation exists for convergents of continued fractions, but let's derive the one shown in the thinking process.

Observe:
$$ \sqrt{2} \approx \frac{N}{D} $$
The next approximation uses the identity $\sqrt{2} = 1 + \frac{1}{1 + \sqrt{2}}$.
So if $\frac{N}{D} \approx \sqrt{2}$, then the next approximation is:
$$ \frac{N'}{D'} = 1 + \frac{1}{1 + \frac{N}{D}} = 1 + \frac{1}{\frac{D+N}{D}} = 1 + \frac{D}{N+D} = \frac{N+D+D}{N+D} = \frac{N+2D}{N+D} $$

Let's verify:
1. Start: $3/2$ ($N=3, D=2$)
2. Next: $\frac{3+2(2)}{3+2} = \frac{7}{5}$. Correct.
3. Next: $\frac{7+2(5)}{7+5} = \frac{17}{12}$. Correct.
4. Next: $\frac{17+2(12)}{17+12} = \frac{41}{29}$. Correct.

### Algorithm
1. Initialize $n=3, d=2$.
2. Initialize `count = 0`.
3. Loop 1000 times (since the problem asks for the first one-thousand expansions, and we start with the first one, we need to handle the loop count carefully. The example says the 8th expansion is the first match. We should check if the loop needs to run 1000 times starting from the first).
   - Actually, strictly speaking, the recurrence transforms the $k$-th to the $(k+1)$-th.
   - We check the condition: `len(str(n)) > len(str(d))`.
   - Update $n, d \leftarrow n+2d, n+d$.
   - Note: The problem asks for the first 1000 expansions.
     - Iteration 1: $3/2$
     - Iteration 2: $7/5$
     - ...
     - Iteration 1000: ...
   - So we loop $i$ from 1 to 1000. In each iteration, we check the *current* $n, d$, then update for the *next* iteration (or update first, depending on start state).
   - Since we start initialized at the 1st expansion ($3/2$), we check, then update 999 times? No, we need to check 1000 expansions.
   - So:
     - Init $n=3, d=2$.
     - Loop $i$ from 1 to 1000:
       - Check digit counts.
       - Update $n, d$ for next round.

### Complexity
- **Time Complexity**: $O(K)$, where $K=1000$. The number of digits grows linearly (adding roughly a digit every few steps), and Python's big integer arithmetic handles this efficiently. $1000$ iterations is trivial.
- **Space Complexity**: $O(\text{digits})$, which is small.