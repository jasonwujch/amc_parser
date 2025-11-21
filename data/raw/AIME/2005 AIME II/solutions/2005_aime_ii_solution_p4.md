# 2005 AIME II Problem 4

## Problem

Find the number of positive integers that are divisors of at least one of $10^{10},15^7,18^{11}.$

## Solution 1
$10^{10} = 2^{10}\cdot 5^{10}$ so $10^{10}$ has $11\cdot11 = 121$ divisors .
$15^7 = 3^7\cdot5^7$ so $15^7$ has $8\cdot8 = 64$ divisors.
$18^{11} = 2^{11}\cdot3^{22}$ so $18^{11}$ has $12\cdot23 = 276$ divisors.
Now, we use the Principle of Inclusion-Exclusion . We have $121 + 64 + 276$ total potential divisors so far, but we've overcounted those factors which divide two or more of our three numbers. Thus, we must subtract off the divisors of their pair-wise greatest common divisors .
$\gcd(10^{10},15^7) = 5^7$ which has 8 divisors.
$\gcd(15^7, 18^{11}) = 3^7$ which has 8 divisors.
$\gcd(18^{11}, 10^{10}) = 2^{10}$ which has 11 divisors.
So now we have $121 + 64 + 276 - 8 -8 -11$ potential divisors. However, we've now undercounted those factors which divide all three of our numbers. Luckily, we see that the only such factor is 1, so we must add 1 to our previous sum to get an answer of $121 + 64 + 276 - 8 - 8 - 11 + 1 = \boxed{435}$ .

## Solution 2
We can rewrite the three numbers as $10^{10} = 2^{10}\cdot 5^{10}$ , $15^7 = 3^7\cdot5^7$ , and $18^{11} = 2^{11}\cdot3^{22}$ . Assume that $n$ (a positive integer) is a divisor of one of the numbers. Therefore, $n$ can be expressed as ${p_1}^{e_1}$ or as ${p_2}^{e_2}{p_3}^{e_3}$ where $p_1$ , $p_2$ are in $\{2,3,5\}$ and $e_1$ , $e_2$ are positive integers.
If $n$ is the power of a single prime, then there are 11 possibilities ( $2^1$ to $2^{11}$ ) for $p_1=2$ , 22 possibilities ( $3^1$ to $3^{22}$ ) for $p_1=3$ , 10 possibilities ( $5^1$ to $5^{10}$ ) for $p_1=5$ , and 1 possibility if $n=1$ . From this case, there are $11+22+10+1=44$ possibilities.
If $n$ is the product of the powers of two primes, then we can just multiply the exponents of each rewritten product to get the number of possibilities, since each exponent of the product must be greater than 0. From this case, there are $10*10+11*22+7*7=100+242+49=391$ possibilities.
Adding up the two cases, there are $44+391=\boxed{435}$ positive integers.
-alpha_2
These problems are copyrighted © by the Mathematical Association of America.