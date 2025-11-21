# 2014 AIME II Problem 15

## Problem

For any integer $k\geq 1$ , let $p(k)$ be the smallest prime which does not divide $k.$ Define the integer function $X(k)$ to be the product of all primes less than $p(k)$ if $p(k)>2$ , and $X(k)=1$ if $p(k)=2.$ Let $\{x_n\}$ be the sequence defined by $x_0=1$ , and $x_{n+1}X(x_n)=x_np(x_n)$ for $n\geq 0.$ Find the smallest positive integer $t$ such that $x_t=2090.$

## Solution
Note that for any $x_i$ , for any prime $p$ , $p^2 \nmid x_i$ . This provides motivation to translate $x_i$ into a binary sequence $y_i$ .
Let the prime factorization of $x_i$ be written as $p_{a_1} \cdot p_{a_2} \cdot p_{a_3} \cdots$ , where $p_i$ is the $i$ th prime number. Then, for every $p_{a_k}$ in the prime factorization of $x_i$ , place a $1$ in the $a_k$ th digit of $y_i$ . This will result in the conversion $x_1 = 2, x_{2} = 3, x_{3} = 2 * 3 = 6, \cdots$ .
Multiplication for the sequence $x_i$ will translate to addition for the sequence $y_i$ . Thus, we see that $x_{n+1}X(x_n) = x_np(x_n)$ translates into $y_{n+1} = y_n+1$ . Since $x_0=1$ , and $y_0=0$ , $x_i$ corresponds to $y_i$ , which is $i$ in binary. Since $x_{10010101_2} = 2 \cdot 5 \cdot 11 \cdot 19 = 2090$ , $t = 10010101_2$ = $\boxed{149}$ .

## Solution 2 DO NOT DO (Painful Bash)
We go through the terms and look for a pattern. We find that
$x_0 = 1$ $x_8 = 7$
$x_1 = 2$ $x_9 = 14$
$x_2 = 3$ $x_{10} = 21$
$x_3 = 6$ $x_{11} = 42$
$x_4 = 5$ $x_{12} = 35$
$x_5 = 10$ $x_{13} = 70$
$x_6 = 15$ $x_{14} = 105$
$x_7 = 30$ $x_{15} = 210$
Commit to the bash. Eventually, you will receive that $x_{149} = 2090$ , so $\boxed{149}$ is the answer. Trust me, this is worth the 10 index points.
$\textbf{-RootThreeOverTwo}$

## Solution 3 (induction)
Let $P_k$ denote the $k$ th prime. Lemma: $x_{n+2^{k-1}} = P_k \cdot x_{n}$ for all $0 \leq n \leq 2^{k-1} - 1.$
$\mathbf{\mathrm{Proof:}}$
We can prove this using induction. Assume that $x_{2^{k-1}-1} = \prod_{j=1}^{k-1} P_j.$ Then, using the given recursion $x_{k+1} = \frac{x_np(x_n)}{X(x_n)}$ , we would “start fresh” for $x_{2^{k-1}} = P_k.$ It is then easy to see that then $\frac{x_n}{P_k}$ just cycles through the previous $x_{2^{k-1}}$ terms of $\{ x_n \},$ since the recursion process is the same and $P_k$ being a factor of $x_n$ is not affected until $n = 2 \cdot {2^{k-1}} = 2^k,$ when given our assumption $x_{2^k - 1} = \prod_{j=1}^{k} P_j$ and $n = 2^k$ is now the least $n$ such that \[P_{k+1} = p(x_{2^{n-1}}),\] in which $P_a = p(x_n)$ where $a > k$ is the only way that the aforementioned cycle would be affected. Specifically, by cancellation according to our recursion, $x_{2^k} = P_{k+1},$ and the values of $x_n$ just starts cycling through the previous $x_{2^k}$ terms again until $x_{2^{k+1}}$ when a new prime shows up in the prime factorization of $x_n,$ when it starts cycling again, and so on. Using our base cases of $x_0$ and $x_1,$ our induction is complete. Now, it is easy to see that $2090 = 2 \cdot 5 \cdot 11 \cdot 19 = P_1 \cdot P_3 \cdot P_5 \cdot P_8,$ and by Lemma #1, the least positive integer $n$ such that $19 | x_n$ is $2^7.$ By repeatedly applying our obtained recursion from Lemma #1, it is easy to see that our answer is just $2^7 + 2^4 + 2^2 + 2^0,$ or $10010101_2 = \boxed{149}.$
-fidgetboss_4000

## Video Solution
https://youtu.be/SXZ01azDCGE?si=_lIcna68SgCcG3av
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .