# 2020 AIME I Problem 4

## Problem

Let $S$ be the set of positive integers $N$ with the property that the last four digits of $N$ are $2020,$ and when the last four digits are removed, the result is a divisor of $N.$ For example, $42,020$ is in $S$ because $4$ is a divisor of $42,020.$ Find the sum of all the digits of all the numbers in $S.$ For example, the number $42,020$ contributes $4+2+0+2+0=8$ to this total.

## Solution 1
We note that any number in $S$ can be expressed as $a(10,000) + 2,020$ for some integer $a$ . The problem requires that $a$ divides this number, and since we know $a$ divides $a(10,000)$ , we need that $a$ divides 2020. Each number contributes the sum of the digits of $a$ , as well as $2 + 0 + 2 +0 = 4$ . Since $2020$ can be prime factorized as $2^2 \cdot 5 \cdot 101$ , it has $(2+1)(1+1)(1+1) = 12$ factors. So if we sum all the digits of all possible $a$ values, and add $4 \cdot 12 = 48$ , we obtain the answer.
Now we list out all factors of $2,020$ , or all possible values of $a$ . $1,2,4,5,10,20,101,202,404,505,1010,2020$ . If we add up these digits, we get $45$ , for a final answer of $45+48=\boxed{093}$ .
-molocyxu

## Solution 2 (Official MAA)
Suppose that $N$ has the required property. Then there are positive integers $k$ and $m$ such that $N = 10^4m + 2020 = k\cdot m$ . Thus $(k - 10^4)m = 2020$ , which holds exactly when $m$ is a positive divisor of $2020.$ The number $2020 = 2^2\cdot 5\cdot 101$ has $12$ divisors: $1, 2, 4, 5, 10, 20, 101, 202, 404, 505, 1010$ , and $2020.$ The requested sum is therefore the sum of the digits in these divisors plus $12$ times the sum of the digits in $2020,$ which is \[(1+2+4+5+1+2+2+4+8+10+2+4)+12\cdot4 = 93.\]

## Solution 3
Note that for all $N \in S$ , $N$ can be written as $N=10000x+2020=20(500x+101)$ for some positive integer $x$ . Because $N$ must be divisible by $x$ , $\frac{20(500x+101)}{x}$ is an integer. We now let $x=ab$ , where $a$ is a divisor of $20$ . Then $\frac{20(500x+101)}{x}=(\frac{20}{a})( \frac{500x}{b}+\frac{101}{b})$ . We know $\frac{20}{a}$ and $\frac{500x}{b}$ are integers, so for $N$ to be an integer, $\frac{101}{b}$ must be an integer. For this to happen, $b$ must be a divisor of $101$ . $101$ is prime, so $b\in \left \{ 1, 101 \right \}$ . Because $a$ is a divisor of $20$ , $a \in \left \{ 1,2,4,5,10,20\right\}$ . So $x \in \left\{1,2,4,5,10,20,101,202,404,505,1010,2020\right\}$ . Be know that all $N$ end in $2020$ , so the sum of the digits of each $N$ is the sum of the digits of each $x$ plus $2+0+2+0=4$ . Hence the sum of all of the digits of the numbers in $S$ is $12 \cdot 4 +45=\boxed{093}$ .

## Video Solutions
- https://youtu.be/5b9Nw4bQt_k
- https://youtu.be/djWzRC-jGYw
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .