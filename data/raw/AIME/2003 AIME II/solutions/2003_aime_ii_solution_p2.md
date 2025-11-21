# 2003 AIME II Problem 2

## Problem

Let $N$ be the greatest integer multiple of 8, no two of whose digits are the same. What is the remainder when $N$ is divided by 1000?

## Solution
We want a number with no digits repeating, so we can only use the digits $0-9$ once in constructing our number. To make the greatest number, we want the greatest digit to occupy the leftmost side and the least digit to occupy the rightmost side. Therefore, the last three digits of the greatest number should be an arrangement of the digits $0,1,2$ . Since the number has to be divisible by 8, the integer formed by the arrangement of $0,1,2$ is also divisible by 8. The only arrangement that works is $120$ .
Therefore, the remainder when the number is divided by $1000$ is $\boxed{120}$ .
Note: The number is $9876543120$

## Solution 2
We notice that the number doesn't matter after the thousands place because any place higher will be divisible by 8. Therefore, the number will look like this(with the maximizing constraint):
$9876543abc$
The abc is there because we don't have the guarantee of divisibility by 8. abc will be a rearrangement of $0, 1, 2$
Now all we have to do is look for the smallest rearrangement of 0, 1, 2. We can write a congruence statement as shown:
$100a+10b+10c \cong 0 \mod 8$
which simplifies to:
$4a+2b+c \cong 0 \mod 8$
Now, since we want to minimize the number, we can first try the case when a = 0.
This doesn't work, as 2+0 isn't congruent to 0 mod 8.
Now lets try a = 1.
We have $4 + 2b + c \cong 0 \mod 8$
From which we get 120 as the smallest.
Now, taking adding that to the number, we get 9876543120. Getting the remainder mod 1000 gives $\boxed{120}$
These problems are copyrighted © by the Mathematical Association of America.