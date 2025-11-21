# 2017 AIME I Problem 3

## Problem

For a positive integer $n$ , let $d_n$ be the units digit of $1 + 2 + \dots + n$ . Find the remainder when \[\sum_{n=1}^{2017} d_n\] is divided by $1000$ .

## Solution
We see that $d_n$ appears in cycles of $20$ and the cycles are \[1,3,6,0,5,1,8,6,5,5,6,8,1,5,0,6,3,1,0,0,\] adding a total of $70$ each cycle. Since $\left\lfloor\frac{2017}{20}\right\rfloor=100$ , we know that by $2017$ , there have been $100$ cycles and $7000$ has been added. This can be discarded as we're just looking for the last three digits. Adding up the first $17$ of the cycle of $20$ , we can see that the answer is $\boxed{069}$ .

## Video Solution
https://youtu.be/BiiKzctXDJg ~ Shrea S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .