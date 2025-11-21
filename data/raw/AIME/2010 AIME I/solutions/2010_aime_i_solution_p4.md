# 2010 AIME I Problem 4

## Problem

Jackie and Phil have two fair coins and a third coin that comes up heads with probability $\frac47$ . Jackie flips the three coins, and then Phil flips the three coins. Let $\frac {m}{n}$ be the probability that Jackie gets the same number of heads as Phil, where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
This can be solved quickly and easily with generating functions .
Let $x^n$ represent flipping $n$ heads.
The generating functions for these coins are $(1+x)$ , $(1+x)$ ,and $(3+4x)$ in order.
The product is $3+10x+11x^2+4x^3$ . ( $ax^n$ means there are $a$ ways to get $n$ heads, eg there are $10$ ways to get $1$ head, and therefore $2$ tails, here.)
The sum of the coefficients squared (total number of possible outcomes, squared because the event is occurring twice) is $(4 + 11 + 10 + 3)^2 = 28^2 = 784$ and the sum of the squares of each coefficient (the sum of the number of ways that each coefficient can be chosen by the two people) is $4^2 + 11^2 + 10^2 + 3^2=246$ . The probability is then $\frac{4^2 + 11^2 + 10^2 + 3^2}{28^2} = \frac{246}{784} = \frac{123}{392}$ . (Notice the relationship between the addends of the numerator here and the cases in the following solution.)
$123 + 392 = \boxed{515}$

## Solution 2
We perform casework based upon the number of heads that are flipped.
- Case 1 : No heads.
- Case 2 : One head.
- Case 3 : Two heads.
\[\frac {1(3 \cdot 3) + 4(3 \cdot 4) + 4(4 \cdot 4)}{28^{2}} = \frac {121}{784}.\]
- Case 4 : Three heads.
Finally, we take the sum: $\frac {9 + 100 + 121 + 16}{784} = \frac {246}{784} = \frac {123}{392}$ , so our answer is $123 + 392 = \fbox{515}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .