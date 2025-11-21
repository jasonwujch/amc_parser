# 1999 AMC 8 Problem 24

## Problem

When $1999^{2000}$ is divided by $5$ , the remainder is

$\text{(A)}\ 0 \qquad \text{(B)}\ 1 \qquad \text{(C)}\ 2 \qquad \text{(D)}\ 3 \qquad \text{(E)}\ 4$

## Solution 1
Note that the units digits of the powers of 9 have a pattern: $9^1 = {\bf 9}$ , $9^2 = 8{\bf 1}$ , $9^3 = 72{\bf 9}$ , $9^4 = 656{\bf 1}$ , and so on. Since all natural numbers with the same last digit have the same remainder when divided by 5, the entire number doesn't matter, just the last digit. For even powers of $9$ , the number ends in a $1$ . Since the exponent is even, the final digit is $1$ . Note that all natural numbers that end in $1$ have a remainder of $1$ when divided by $5$ . So, our answer is $\boxed{\text{(B)}\ 1}$ .

## Solution 2
Write $1999$ as $2000-1$ . We are taking $(2000-1)^{2000} \mod{10}$ . Using the binomial theorem, we see that ALL terms in this expansion are divisible by $2000$ , which is in turn divisible by $5$ , except for the very last term, which is just $(-1)^{2000}$ . This is clear because the binomial expansion is just choosing how many $2000$ s and how many $-1$ s there are for each term. Using this, we can take the entire polynomial $\mod{10}$ , which leaves just $(-1)^{2000}=\boxed{\text{(B)}\ 1}$ .

## Solution 3
As $1999 \equiv -1 \pmod{5}$ , we have $1999^{2000} \equiv (-1)^{2000} \equiv 1 \pmod{5}$ . Thus, the answer is $\boxed{\text{(B)}\ 1}$ .

## Solution 4
A sum/product of any two natural numbers has the same remainder, when divided by $5$ , as the sum/product of their remainders. Thus, we can use the basic definition of an exponent and view the problem as $1999 \cdot 1999 \cdot \cdot \cdot 1999$ .
Using the fact stated in the first sentence, we see that the remainder of $1999$ , when divided by $5$ , is $4$ . The problem can now be written viewed as finding the remainder of $4^{2000}$ when it is divided by $5$ , which is already much simpler.
Now, toying with the simplified problem a little, see notice that powers of $4$ alternate from ending in $4$ and $6$ . We notice that even powers of $4$ always end in $6$ , and also that $2000$ is even. Thus $4^{2000}$ must end in $6$ , which, when divided by $5$ gives a remainder of $\boxed{\text{(B)}\ 1}$ .

## Video Solution by Soo
https://youtu.be/jCHiQMK7k3w - Soo, DRMS, NM

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=U_WOZpd7eYQ
### See Also