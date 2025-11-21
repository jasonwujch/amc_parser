# 2010 AIME II Problem 3

## Problem

Let $K$ be the product of all factors $(b-a)$ (not necessarily distinct) where $a$ and $b$ are integers satisfying $1\le a < b \le 20$ . Find the greatest positive integer $n$ such that $2^n$ divides $K$ .

## Solution
In general, there are $20-n$ pairs of integers $(a, b)$ that differ by $n$ because we can let $b$ be any integer from $n+1$ to $20$ and set $a$ equal to $b-n$ . Thus, the product is $(1^{19})(2^{18})\cdots(19^1)$ (or alternatively, $19! \cdot 18! \cdots 1!$ .)
When we count the number of factors of $2$ , we have 4 groups, factors that are divisible by $2$ at least once, twice, three times and four times.
- Numbers that are divisible by $2$ at least once: $2, 4, \cdots, 18$
- Numbers that are divisible by $2$ at least twice: $4, 8, \cdots, 16$
- Numbers that are divisible by $2$ at least three times: $8,16$
- Number that are divisible by $2$ at least four times: $16$
Summing these give an answer of $\boxed{150}$ .

## Video Solution
For those of you who want a video solution: https://www.youtube.com/watch?v=NL-9fJBE3HI&list=PLpoKXj-PWCba2d6OG3-ExCZKTLRVYoAkq&index=6
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .