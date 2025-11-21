# 2010 AMC 10A Problem 25

## Problem

Jim starts with a positive integer $n$ and creates a sequence of numbers. Each successive number is obtained by subtracting the largest possible integer square less than or equal to the current number until zero is reached. For example, if Jim starts with $n = 55$ , then his sequence contains $5$ numbers:

\[\begin{array}{ccccc} {}&{}&{}&{}&55\\ 55&-&7^2&=&6\\ 6&-&2^2&=&2\\ 2&-&1^2&=&1\\ 1&-&1^2&=&0\\ \end{array}\]

Let $N$ be the smallest number for which Jim’s sequence has $8$ numbers. What is the units digit of $N$ ?

$\mathrm{(A)}\ 1 \qquad \mathrm{(B)}\ 3 \qquad \mathrm{(C)}\ 5 \qquad \mathrm{(D)}\ 7 \qquad \mathrm{(E)}\ 9$

## Solution 1
We can find the answer by working backwards. We begin with $1-1^2=0$ on the bottom row, then the $1$ goes to the right of the equal's sign in the row above. We find the smallest value $x$ for which $x-1^2=1$ and $x>1^2$ , which is $x=2$ .
We repeat the same procedure except with $x-1^2=1$ for the next row and $x-1^2=2$ for the row after that. However, at the fourth row, we see that solving $x-1^2=3$ yields $x=4$ , in which case it would be incorrect since $1^2=1$ is not the greatest perfect square less than or equal to $x$ . So we make it a $2^2$ and solve $x-2^2=3$ . We continue on using this same method where we increase the perfect square until $x$ can be made bigger than it. When we repeat this until we have $8$ rows, we get:
\[\begin{array}{ccccc}{}&{}&{}&{}&7223\\ 7223&-&84^{2}&=&167\\ 167&-&12^{2}&=&23\\ 23&-&4^{2}&=&7\\ 7&-&2^{2}&=&3\\ 3&-&1^{2}&=&2\\ 2&-&1^{2}&=&1\\ 1&-&1^{2}&=&0\\ \end{array}\]
Hence the solution is the last digit of $7223$ , which is $\boxed{\textbf{(B)}\ 3}$ .
Note: We can go up to $167$ , and then notice the pattern of units digits alternating between $3$ and $7$ , so we do not need to calculate $7223$ .

## Solution 2
Notice that to get the previous term, we must add the smallest square number, (let's call it $n^2$ ) such that the sum is less than $(n+1)^2$ . Otherwise, instead of subtracting $n^2$ from the previous term, we're subtracting a greater square number.
Remember that $(x+1)^2 = x^2 + 2x + 1$ . Recall that to find the previous term, we must add a square number such that it is less than the next square number. $a + n^2 < (n+1)^2$ . For this to be true, $a < 2n + 1$ . What that means is that given a term $a$ , we can find the previous term by adding $n^2$ where $n > \frac {a-1}{2}$ .
For example, to find the term that precedes $167$ , we know that $n>166/2 = 83$ . Therefore, $n=84$ and the previous term is $167 + 84^2 = 7223$ . The last digit of $7223$ is $3 \Rightarrow \boxed{\textbf{(B)}\ 3}$

## Video Solution by the Beauty of Math
https://youtu.be/wKPoslWOlKY