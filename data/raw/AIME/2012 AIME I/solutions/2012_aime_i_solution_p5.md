# 2012 AIME I Problem 5

## Problem

Let $B$ be the set of all binary integers that can be written using exactly $5$ zeros and $8$ ones where leading zeros are allowed. If all possible subtractions are performed in which one element of $B$ is subtracted from another, find the number of times the answer $1$ is obtained.

## Solution
When $1$ is subtracted from a binary number, the number of digits will remain constant if and only if the original number ended in $10.$ Therefore, every subtraction involving two numbers from $B$ will necessarily involve exactly one number ending in $10.$ To solve the problem, then, we can simply count the instances of such numbers. With the $10$ in place, the seven remaining $1$ 's can be distributed in any of the remaining $11$ spaces, so the answer is ${11 \choose 7} = \boxed{330}$ .

## Video Solutions
https://www.youtube.com/watch?v=cQmmkfZvPgU&t=30s
https://www.youtube.com/watch?v=f5ZoAFfc-1E&list=PLyhPcpM8aMvIo_foUDwmXnQClMHngjGto&index=5 (Solution by Richard Rusczyk) - AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .