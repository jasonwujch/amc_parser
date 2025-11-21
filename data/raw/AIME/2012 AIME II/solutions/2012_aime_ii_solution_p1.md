# 2012 AIME II Problem 1

## Problem

Find the number of ordered pairs of positive integer solutions $(m, n)$ to the equation $20m + 12n = 2012$ .

## Solution

## Solution 1
Solving for $m$ gives us $m = \frac{503-3n}{5},$ so in order for $m$ to be an integer, we must have $3n \equiv 503 \mod 5 \longrightarrow n \equiv 1 \mod 5.$ The smallest possible value of $n$ is obviously $1,$ and the greatest is $\frac{503 - 5}{3} = 166,$ so the total number of solutions is $\frac{166-1}{5}+1 = \boxed{34}$

## Solution 2
Dividing by $4$ gives us $5m + 3n = 503$ .
Thus, we have $3n = 503 -5m \implies 503 - 5m \equiv 0 \ (\text{mod }3)$ , since $n$ is an integer.
Rearranging:
\[\begin{lgathered} 5m \equiv 503 \equiv 2 \ (\text{mod }3) \\ m \equiv 4 \ (\text{mod }3) \qquad \because 5^{-1} \equiv 2 \ (\text{mod }3)\\ m \equiv 1 \ (\text{mod }3) \\ \implies m = 3k + 1 \end{lgathered}\]
Since $503 - 5m > 0$ , we know that $m <\frac{503}{5}$ .
And because $m$ is an integer, $m \leq \left\lfloor \frac{503}{5} \right\rfloor \implies m \leq 100$
Therefore,
\[\begin{lgathered} 3k + 1 \leq 100 \\ 0 \leq k \leq 33 \end{lgathered}\]
Therefore, $m$ ranges from $3 \cdot 0+1$ to $3\cdot 33+1$ , giving total $\boxed{ 034 }$ values.
Alternatively, total integer values of $k$ is also $34$ , thus, $\boxed{ 034 }$ values.
~vaporwave
Elaborated and reworded by Moisentinel

## Solution 3
Because the x-intercept of the equation is $\frac{2012}{20}$ , and the y-intercept is $\frac{2012}{12}$ , the slope is $\frac{\frac{-2012}{12}}{\frac{2012}{20}} = \frac{-5}{3}$ . Now, notice the first obvious solution: (100,1). From it, we derive all the other solutions by applying the slope in reverse, i.e: $(100,1), (97,6), (94,11)...$ Because the solutions are only positive, we can generate only 33 more solutions, so in total we have $33+1=\boxed{34}$ solutions.

## Solution 4 (Quick)
Note that a positive integer is divisible by 20 if it ends in 0.
Notice that if a multiple of 12 end in 2, 12 must be multiplied by an integer that ends in 1 or 6.
So let's start checking because 2012 ends in 2, same as 12.
When $n=1$ , $m=100$ .
When $n=6$ , $m=97$ . What is happening? Why doesn't, say, as values of $n$ , do $1, 11, ...$ work, while $6, 16, 26$ work for $m$ to be an integer (as seen in 2022 CEMC Cayley #21 ( https://www.cemc.uwaterloo.ca/contests/past_contests/2022/2022CayleyContest.pdf , https://www.cemc.uwaterloo.ca/contests/past_contests/2022/2022CayleySolution.pdf )?)
Notice that we can break $1, 6, ...$ down into $0, 5, 10, ...$ . So $20m=2000-12k$ , where $k$ is a member of the set ${0, 5, 10, 15...}$ .
For a number to be divisible by 20, it must be divisible 10, and the quotient (that number divided by 10) must be divisible by 2. This means that the number must end in 0, and its tens digit must be even.
So notice that the tens digit cycle in: $0, 4, 8, 2, 6$ . Each of this is even (notice that when $k=25$ , $2000-12k=1700$ , it cycles again).
So we know that all values of $n$ , which end in 1 or 6, that make $2012-12n\geq20$ works.
So values of $n$ that belong to ${1, 6, ..., 166}$ work. Clearly, that is 34 integer values of $n$ . Therefore, the answer is $\boxed{034}$ .
~hastapasta
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .