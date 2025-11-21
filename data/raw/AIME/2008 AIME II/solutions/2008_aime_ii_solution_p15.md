# 2008 AIME II Problem 15

## Problem

Find the largest integer $n$ satisfying the following conditions:

## Solution

## Solution 1
Write $n^2 = (m + 1)^3 - m^3 = 3m^2 + 3m + 1$ , or equivalently, $(2n + 1)(2n - 1) = 4n^2 - 1 = 12m^2 + 12m + 3 = 3(2m + 1)^2$ .
Since $2n + 1$ and $2n - 1$ are both odd and their difference is $2$ , they are relatively prime . But since their product is three times a square, one of them must be a square and the other three times a square. We cannot have $2n - 1$ be three times a square, for then $2n + 1$ would be a square congruent to $2$ modulo $3$ , which is impossible.
Thus $2n - 1$ is a square, say $b^2$ . But $2n + 79$ is also a square, say $a^2$ . Then $(a + b)(a - b) = a^2 - b^2 = 80$ . Since $a + b$ and $a - b$ have the same parity and their product is even, they are both even. To maximize $n$ , it suffices to maximize $2b = (a + b) - (a - b)$ and check that this yields an integral value for $m$ . This occurs when $a + b = 40$ and $a - b = 2$ , that is, when $a = 21$ and $b = 19$ . This yields $n = 181$ and $m = 104$ , so the answer is $\boxed{181}$ .

## Solution 2
Suppose that the consecutive cubes are $m$ and $m + 1$ . We can use completing the square and the first condition to get: \[(2n)^2 - 3(2m + 1)^2 = 1\equiv a^2 - 3b^2\] where $a$ and $b$ are non-negative integers. Now this is a Pell equation , with solutions in the form $(2 + \sqrt {3})^k = a_k + \sqrt {3}b_k,$ $k = 0,1,2,3,...$ . However, $a$ is even and $b$ is odd. It is easy to see that the parity of $a$ and $b$ switch each time (by induction). Hence all solutions to the first condition are in the form: \[(2 + \sqrt {3})^{2k + 1} = a_k + \sqrt {3}b_k\] where $k = 0,1,2,..$ . So we can (with very little effort) obtain the following: $(k,a_k = 2n) = (0,2),(1,26),(2,362),(3,5042)$ . It is an AIME problem so it is implicit that $n < 1000$ , so $2n < 2000$ . It is easy to see that $a_n$ is strictly increasing by induction. Checking $2n = 362\implies n =\boxed{181}$ in the second condition works (we know $b_k$ is odd so we don't need to find $m$ ). So we're done.

## Solution 3 (Big Bash)
Let us generate numbers $1$ to $1000$ for the second condition, for squares. We know for $N$ to be integer, the squares must be odd. So we generate $N = 1, 21, 45, 73, 105, 141, 181, 381, 441, 721, 801$ . $N$ cannot exceed $1000$ since it is AIME problem. Now take the first criterion, let $a$ be the smaller consecutive cube. We then get:
$N^2 = (A + 1)^3 - A^3$
$N^2 - 1 = 3A^2 + 3A$
$(N + 1)(N - 1) = 3A(A + 1)$
Now we know either $N + 1$ or $N - 1$ must be factor of $3$ , hence $N = 1 \pmod 3$ or $N = 2 \pmod 3$ . Only $1, 73, 181, 721$ satisfy this criterion. Testing each of the numbers in the condition yields $181$ as the largest that fits both, thus answer $= \boxed{181}$ .

## Video Solution
2008 AIME II #15
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.