# 2013 AMC 10A Problem 13

## Problem

How many three-digit numbers are not divisible by $5$ , have digits that sum to less than $20$ , and have the first digit equal to the third digit?

$\textbf{(A)}\ 52 \qquad\textbf{(B)}\ 60 \qquad\textbf{(C)}\ 66 \qquad\textbf{(D)}\ 68 \qquad\textbf{(E)}\ 70$

## Solution
We use a casework approach to solve the problem. These three digit numbers are of the form $\overline{xyx}$ .( $\overline{abc}$ denotes the number $100a+10b+c$ ). We see that $x\neq 0$ and $x\neq 5$ , as $x=0$ does not yield a three-digit integer and $x=5$ yields a number divisible by 5.
The second condition is that the sum $2x+y<20$ . When $x$ is $1$ , $2$ , $3$ , or $4$ , $y$ can be any digit from $0$ to $9$ , as $2x<10$ . This yields $10(4) = 40$ numbers.
When $x=6$ , we see that $12+y<20$ so $y<8$ . This yields $8$ more numbers.
When $x=7$ , $14+y<20$ so $y<6$ . This yields $6$ more numbers.
When $x=8$ , $16+y<20$ so $y<4$ . This yields $4$ more numbers.
When $x=9$ , $18+y<20$ so $y<2$ . This yields $2$ more numbers.
Summing, we get $40 + 8 + 6 + 4 + 2 = \boxed{\textbf{(B) }60}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .