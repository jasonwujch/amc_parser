# 2016 AMC 10B Problem 15

## Problem

All the numbers $1, 2, 3, 4, 5, 6, 7, 8, 9$ are written in a $3\times3$ array of squares, one number in each square, in such a way that if two numbers are consecutive then they occupy squares that share an edge. The numbers in the four corners add up to $18$ . What is the number in the center?

$\textbf{(A)}\ 5\qquad\textbf{(B)}\ 6\qquad\textbf{(C)}\ 7\qquad\textbf{(D)}\ 8\qquad\textbf{(E)}\ 9$

## Solution 1
Consecutive numbers share an edge. That means that it is possible to walk from $1$ to $9$ by single steps north, south, east, or west. Consequently, the squares in the diagram with different shades have different parity: [asy]size(4cm); for(int i=0;i<3;++i)for(int j=0;j<3;++j)filldraw(box((i,j),(i+1,j+1)),gray((i+j)%2*.2+.7));[/asy] But since there are only four even numbers in the set, the five darker squares must contain the odd numbers, which sum to $1+3+5+7+9=25.$ Therefore if the sum of the numbers in the corners is $18$ , the number in the center must be $\boxed {\textbf{(C) }7}$ .

## Solution 2 - Trial and Error
Quick testing shows that \[3~2~1\] \[4~7~8\] \[5~6~9\] is a valid solution. $3+1+5+9 = 18$ , and the numbers follow the given condition. The center number is found to be $\boxed {\textbf{(C) }7}$ .. — @adihaya ( talk ) 12:27, 21 February 2016 (EST) ~edited

## Solution 3 (not rigorous)
First let the numbers be \[1 ~8~ 7\] \[2 ~ 9 ~6\] \[3 ~ 4~ 5\] with the numbers $1-8$ around the outsides and $9$ in the middle. We see that the sum of the four corner numbers is $16$ . If we switch $7$ and $9$ , then the corner numbers will add up to $18$ and the consecutive numbers will still be touching each other. The answer is $\boxed {\textbf{(C) }7}$ . ~edited

## Solution 4 (answer choices)
Testing out the box with the center square taking on the value of 5 and 6, we find that they either do not satisfy the first or the second condition. Testing 7, we find that a valid configuration is \[1 ~8~ 9\] \[2 ~ 7 ~6\] \[3 ~ 4~ 5\]
$\boxed {\textbf{(C) }7}$
~JH. L
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .