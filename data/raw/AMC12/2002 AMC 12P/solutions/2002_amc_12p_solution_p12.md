# 2002 AMC 12P Problem 12

## Problem

For how many positive integers $n$ is $n^3 - 8n^2 + 20n - 13$ a prime number?

$\text{(A) 1} \qquad \text{(B) 2} \qquad \text{(C) 3} \qquad \text{(D) 4} \qquad \text{(E) more than 4}$

## Solution 1
Since this is a number theory question, it is clear that the main challenge here is factoring the given cubic. In general, the rational root theorem will be very useful for these situations.
The rational root theorem states that all rational roots of $n^3 - 8n^2 + 20n - 13$ will be among $1, 13, -1$ , and $-13$ . Evaluating the cubic at these values will give $n = 1$ as a root. Doing some synthetic division gives \[n^3 - 8n^2 + 20n - 13 = (n-1)(n^2 - 7n + 13)\]
Since $n > 0$ , $n-1$ must be positive. Since $(n-1)(n^2 - 7n + 13)$ evaluates to a prime, it is clear that exactly one of $n-1$ and $n^2 - 7n - 13$ is $1$ . We proceed by splitting the problem into 2 cases.
Case 1: $n-1 = 1$ It is clear that $n = 2$ . We have $2^2 - 7(2) + 13 = 3$ , so this case yields $n = 2$ as a solution.
Case 2: $n^2 - 7n + 13 = 1$ Solving for $n$ gives $n^2 - 7n + 12 = 0$ or $(n-3)(n-4) = 0$ . Therefore, $n = 3$ or $n = 4$ . Since both $3-1 = 2$ and $4-1 = 3$ are prime, both $n = 3$ and $n = 4$ work, yielding 2 solutions.
Putting everything together, the answer is $1 + 2 = \boxed{\textbf{(C) }3}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .