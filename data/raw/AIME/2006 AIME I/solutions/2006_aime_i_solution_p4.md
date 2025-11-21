# 2006 AIME I Problem 4

## Problem

Let $N$ be the number of consecutive $0$ 's at the right end of the decimal representation of the product $1!2!3!4!\cdots99!100!.$ Find the remainder when $N$ is divided by $1000$ .

## Solution
A number in decimal notation ends in a zero for each power of ten which divides it. Thus, we need to count both the number of 5s and the number of 2s dividing into our given expression. Since there are clearly more 2s than 5s, it is sufficient to count the number of 5s.
One way to do this is as follows: $96$ of the numbers $1!,\ 2!,\ 3!,\ 100!$ have a factor of $5$ . $91$ have a factor of $10$ . $86$ have a factor of $15$ . And so on. This gives us an initial count of $96 + 91 + 86 + \ldots + 1$ . Summing this arithmetic series of $20$ terms, we get $970$ . However, we have neglected some powers of $5$ - every $n!$ term for $n\geq25$ has an additional power of $5$ dividing it, for $76$ extra; every n! for $n\geq 50$ has one more in addition to that, for a total of $51$ extra; and similarly there are $26$ extra from those larger than $75$ and $1$ extra from $100$ . Thus, our final total is $970 + 76 + 51 + 26 + 1 = 1124$ , and the answer is $\boxed{124}$ .

## Solution 2 (Legendre's Formula )
This problem can be easily solved using Legendre's Formula :
First is to account for all of the factorials that are greater than $5n$ or $5, 10, 15, 20...100$ , then the factorials that are greater than $5^2n$ or $25, 50, 75, 100$ . Since $5^3=125>100$ we do not need to account for it.
This gives $96+91+86+...+1$ and $76+51+26+1$ respectively. Adding all of these terms up gives 1124 or $\boxed{124}$ .
~PeterDoesPhysics

## Video Solution by OmegaLearn
https://youtu.be/p5f1u44-pvQ?t=413
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.