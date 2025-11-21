# 2005 AIME I Problem 12

## Problem

For positive integers $n,$ let $\tau (n)$ denote the number of positive integer divisors of $n,$ including 1 and $n.$ For example, $\tau (1)=1$ and $\tau(6) =4.$ Define $S(n)$ by $S(n)=\tau(1)+ \tau(2) + \cdots + \tau(n).$ Let $a$ denote the number of positive integers $n \leq 2005$ with $S(n)$ odd , and let $b$ denote the number of positive integers $n \leq 2005$ with $S(n)$ even . Find $|a-b|.$

1 Problem

- 1 Problem

- 2 Solution 1

- 3 Solution 2

- 4 Solution 3

- 5 Solution 4

- 6 See also

## Solution 1
It is well-known that $\tau(n)$ is odd if and only if $n$ is a perfect square . (Otherwise, we can group divisors into pairs whose product is $n$ .) Thus, $S(n)$ is odd if and only if there are an odd number of perfect squares less than $n$ . So $S(1), S(2)$ and $S(3)$ are odd, while $S(4), S(5), \ldots, S(8)$ are even, and $S(9), \ldots, S(15)$ are odd, and so on.
So, for a given $n$ , if we choose the positive integer $m$ such that $m^2 \leq n < (m + 1)^2$ we see that $S(n)$ has the same parity as $m$ .
It follows that the numbers between $1^2$ and $2^2$ , between $3^2$ and $4^2$ , and so on, all the way up to the numbers between $43^2$ and $44^2 = 1936$ have $S(n)$ odd. These are the only such numbers less than $2005$ (because $45^2 = 2025 > 2005$ ).

## Solution 2
Notice that the difference between consecutive squares are consecutively increasing odd numbers. Thus, there are $3$ numbers between $1$ (inclusive) and $4$ (exclusive), $5$ numbers between $4$ and $9$ , and so on. The number of numbers from $n^2$ to $(n + 1)^2$ is $(n + 1 - n)(n + 1 + n) = 2n + 1$ . Whenever the lowest square beneath a number is odd, the parity will be odd, and the same for even. Thus, $a = [2(1) + 1] + [2(3) + 1] \ldots [2(43) + 1] = 3 + 7 + 11 \ldots 87$ . $b = [2(2) + 1] + [2(4) + 1] \ldots [2(42) + 1] + 70 = 5 + 9 \ldots 85 + 70$ , the $70$ accounting for the difference between $2005$ and $44^2 = 1936$ , inclusive. Notice that if we align the two and subtract, we get that each difference is equal to $2$ . Thus, the solution is $|a - b| = |b - a| = |2 \cdot 21 + 70 - 87| = \boxed{025}$ .

## Solution 3
Similarly, $b = (3^2 - 2^2) + (5^2 - 4^2) + \ldots + (45^2 - 44^2) - 19$ , where the $-19$ accounts for those numbers between $2005$ and $2024$ .
Thus $a = (2^2 - 1^2) + (4^2 - 3^2) + \ldots + (44^2 - 43^2)$ .
Then, $|a - b| = |2(2^2 + 4^2 + \ldots + 44^2) - 2(1^2 + 3^2 + 5^2 + \ldots 43^2) + 1^2 - 45^2 + 19|$ . We can apply the formula $1^2 + 2^2 + \ldots + n^2 = \frac{n(n + 1)(2n + 1)}{6}$ . From this formula, it follows that $2^2 + 4^2 + \ldots + (2n)^2 = \frac{2n(n + 1)(2n + 1)}{3}$ and so that
$|a - b| = \left| 2\cdot \frac{44\cdot23\cdot45}{3} - 2\cdot \frac{22 \cdot 43 \cdot 45}{3} - 45^2 + 20\right| = |-25| =\boxed{025}$ .

## Solution 4
Let $\Delta n$ denote the sum $1+2+3+ \dots +n-1+n$ . We can easily see from the fact "It is well-known that $\tau(n)$ is odd if and only if $n$ is a perfect square.", that
$a = (2^2-1^2) + (4^2-3^2) \dots (44^2 - 43^2) = (2+1)(2-1)+(4+3)(4-3) \dots (44+43)(44-43) = 1+2+3...44 = \Delta 44$ .
$b = 3^2-2^2+5^2-4^2...2006-44^2 = (3+2)(3-2) \dots (43+42)(43-42) + 1 + (2005 - 44^2) = \Delta 43 + 69$ .
$a-b = \Delta 44-\Delta 43-69 = 44-69 = -25$ . They ask for $|a-b|$ , so our answer is $|-25| = \boxed{025}$
-Alexlikemath
These problems are copyrighted © by the Mathematical Association of America.