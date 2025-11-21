# 2001 AIME I Problem 8

## Problem

Call a positive integer $N$ a 7-10 double if the digits of the base- $7$ representation of $N$ form a base- $10$ number that is twice $N$ . For example, $51$ is a 7-10 double because its base- $7$ representation is $102$ . What is the largest 7-10 double?

## Solution
We let $N_7 = \overline{a_na_{n-1}\cdots a_0}_7$ ; we are given that
\[2(a_na_{n-1}\cdots a_0)_7 = (a_na_{n-1}\cdots a_0)_{10}\] (This is because the digits in $N$ ' s base 7 representation make a number with the same digits in base 10 when multiplied by 2)
Expanding, we find that
\[2 \cdot 7^n a_n + 2 \cdot 7^{n-1} a_{n-1} + \cdots + 2a_0 = 10^na_n + 10^{n-1}a_{n-1} + \cdots + a_0\]
or re-arranging,
\[a_0 + 4a_1 = 2a_2 + 314a_3 + \cdots + (10^n - 2 \cdot 7^n)a_n\]
Since the $a_i$ s are base- $7$ digits, it follows that $a_i < 7$ , and the LHS is less than or equal to $30$ . Hence our number can have at most $3$ digits in base- $7$ . Letting $a_2 = 6$ , we find that $630_7 = \boxed{315}_{10}$ is our largest 7-10 double.

## Solution 2 (Guess and Check)
Let $A$ be the base $10$ representation of our number, and let $B$ be its base $7$ representation.
Given this is an AIME problem, $A<1000$ . If we look at $B$ in base $10$ , it must be equal to $2A$ , so $B<2000$ when $B$ is looked at in base $10.$
If $B$ in base $10$ is less than $2000$ , then $B$ as a number in base $7$ must be less than $2*7^3=686$ .
$686$ is non-existent in base $7$ , so we're gonna have to bump that down to $666_7$ .
This suggests that $A$ is less than $\frac{666}{2}=333$ .
Guess and check shows that $A<320$ , and checking values in that range produces $\boxed{315}$ .

## Solution 3
Since this is an AIME problem, the maximum number of digits the 7-10 double can have is 3. Let the number be \[abc\] in base 7. Then the number in expanded form is \[49a+7b+c\] in base 7 and \[100a+10b+c\] in base 10. Since the number in base 7 is half the number in base 10, we get the following equation. \[98a+14b+2c=100a+10b+c\] which simplifies to \[2a=4b+c.\] The largest possible value of a is 6 because the number is in base 7. Then to maximize the number, $b$ is $3$ and $c$ is $0$ . Therefore, the largest 7-10 double is 630 in base 7, or $\boxed{315}$ in base 10.
These problems are copyrighted © by the Mathematical Association of America.