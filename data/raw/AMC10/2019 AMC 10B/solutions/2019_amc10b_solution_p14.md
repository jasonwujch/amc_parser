# 2019 AMC 10B Problem 14

## Problem

The base-ten representation for $19!$ is $121,6T5,100,40M,832,H00$ , where $T$ , $M$ , and $H$ denote digits that are not given. What is $T+M+H$ ?

$\textbf{(A) }3 \qquad\textbf{(B) }8 \qquad\textbf{(C) }12 \qquad\textbf{(D) }14 \qquad\textbf{(E) } 17$

## Solution 1
We can figure out $H = 0$ by noticing that $19!$ will end with $3$ zeroes, as there are three factors of $5$ in its prime factorization, so there would be 3 powers of 10 meaning it will end in 3 zeros. Next, we use the fact that $19!$ is a multiple of both $11$ and $9$ . Their divisibility rules (see Solution 2) tell us that $T + M \equiv 3 \;(\bmod\; 9)$ and that $T - M \equiv 7 \;(\bmod\; 11)$ . By guess and checking, we see that $T = 4, M = 8$ is a valid solution. Therefore the answer is $4 + 8 + 0 = \boxed{\textbf{(C) }12}$ .

## Solution 2 (similar to Solution 1)
We know that $H = 0$ , because $19!$ ends in three zeroes (see Solution 1). Furthermore, we know that $9$ and $11$ are both factors of $19!$ . We can simply use the divisibility rules for $9$ and $11$ for this problem to find $T$ and $M$ . For $19!$ to be divisible by $9$ , the sum of digits must simply be divisible by $9$ . Summing the digits, we get that $T + M + 33$ must be divisible by $9$ . This leaves either $\text{A}$ or $\text{C}$ as our answer choice. Now we test for divisibility by $11$ . For a number to be divisible by $11$ , the alternating sum must be divisible by $11$ (for example, with the number $2728$ , $2-7+2-8 = -11$ , so $2728$ is divisible by $11$ ). Applying the alternating sum test to this problem, we see that $T - M - 7$ must be divisible by 11. By inspection, we can see that this holds if $T=4$ and $M=8$ . The sum is $8 + 4 + 0 = \boxed{\textbf{(C) }12}$ .

## Solution 3 (Brute Force)
Multiplying it out, we get $19! = 121,645,100,408,832,000$ . Evidently, $T = 4$ , $M = 8$ , and $H = 0$ . The sum is $8 + 4 + 0 = \boxed{\textbf{(C) }12}$ .
NEVER do this in a real contest unless you decide to devote most of your time to this problem.

## Solution 4 (1001?)
7, 11, 13 are < 19 and 1001 = 7 * 11 * 13. Check the alternating sum of block 3: H00 - 832 + 40M - 100 + 6T5 - 121 and it is divisible by 1001. HTM + 5 - 53 = 0 (mod 1001) => HTM = 48.
The answer is $4 + 8 + 0 = \boxed{\textbf{(C) }12}$ .
~ AliciaWu

## Video Solution by OmegaLearn
https://youtu.be/p5f1u44-pvQ?t=760
~ pi_is_3.14

## Video Solution
https://youtu.be/mXvetCMMzpU
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .