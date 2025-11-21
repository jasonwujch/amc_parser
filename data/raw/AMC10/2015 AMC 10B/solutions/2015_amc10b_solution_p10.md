# 2015 AMC 10B Problem 10

## Problem

What are the sign and units digit of the product of all the odd negative integers strictly greater than $-2015$ ? $\textbf{(A) }$ It is a negative number ending with a 1. $\textbf{(B) }$ It is a positive number ending with a 1. $\textbf{(C) }$ It is a negative number ending with a 5. $\textbf{(D) }$ It is a positive number ending with a 5. $\textbf{(E) }$ It is a negative number ending with a 0.

## Solution 1
Since $-5>-2015$ , the product must end with a $5$ .
The multiplicands are the odd negative integers from $-1$ to $-2013$ . There are $\frac{|-2013+1|}2+1=1006+1$ of these numbers. Since $(-1)^{1007}=-1$ , the product is negative.
Therefore, the answer must be $\boxed{\text{(\textbf C) It is a negative number ending with a 5.}}$
Alternatively, we can calculate the units digit of each group of 5 odd numbers using modular arithmetic.

## Solution 2
To find the sign of the product, we need to count the number of integers in this set. We can do this by counting the positive odd integers from $1$ to $2013$ . This is equal to $\frac{2013-1}{2}+1=1007$ . Since there are $1007$ negative numbers being multiplied, and $1007$ is an odd number, the product will be negative. To find the units digit of the product, we only need to multiply the units digits of the numbers. This is equal to $1\times3\times5\times7\times9... 1\times3$ . Notice how it repeats in groups of $1\times3\times5\times7\times9...$ until the end where we just do an extra $1\times3$ . Let's go by cycles of $1\times3\times5\times7\times9$ . The first cycle we have $1\times3\times5\times7\times9=945$ , and our second cycle we have $1\times3\times5\times7\times9\times1\times3\times5\times7\times9=945\times945$ . Notice how the units digits is always 5, so whatever we multiply it by always has a units digits of 5, so our answer is $\boxed{\text{(\textbf C) It is a negative number ending with a 5.}}$
~Baihly2024

## Video Solution 1
https://youtu.be/r5QASm5hnII
~Education, the Study of Everything

## Video Solution
https://youtu.be/UoU-cvet1pg
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .