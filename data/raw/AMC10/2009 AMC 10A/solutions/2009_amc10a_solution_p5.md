# 2009 AMC 10A Problem 5

## Problem

What is the sum of the digits of the square of $\text 111111111$ ?

$\mathrm{(A)}\ 18\qquad\mathrm{(B)}\ 27\qquad\mathrm{(C)}\ 45\qquad\mathrm{(D)}\ 63\qquad\mathrm{(E)}\ 81$

## Solution 1
Using the standard multiplication algorithm, $111,111,111^2=12,345,678,987,654,321,$ whose digit sum is $\boxed{(E)\text{ }81.}$

## Solution 2
We note that
$1^2 = 1$ ,
$11^2 = 121$ ,
$111^2 = 12321$ ,
and $1,111^2 = 1234321$ .
We can clearly see the pattern: If $X$ is $111\cdots111$ , with $n$ ones (and for the sake of simplicity, assume that $n<10$ ), then the sum of the digits of $X^2$ is
$1+2+3+4+5\cdots n+(n-1)+(n-2)\cdots+1$
$=(1+2+3\cdots n)+(1+2+3+\cdots n-1)$
$=\dfrac{n(n+1)}{2}+\dfrac{(n-1)n}{2}$
$=\dfrac{n(n+1+n-1)}{2}=\dfrac{2n^2}{2}=n^2.$
Aha! We know that $111,111,111$ has $9$ digits, so its digit sum is $9^2=\boxed{81(E)}$ .

## Solution 3
We see that $111^2$ can be written as $111(100+10+1)=11100+1110+111=12321$ .
We can apply this strategy to find $111,111,111^2$ , as seen below.
$111111111^2=111111111(100000000+10000000\cdots+10+1)$
$=11111111100000000+1111111110000000+\cdots+111111111$
$=12,345,678,987,654,321$
The digit sum is thus $1+2+3+4+5+6+7+8+9+8+7+6+5+4+3+2+1=81 \boxed{(E)}$ .

## Solution 4 (Confusing But Fast)
We note that the only way for the sum of multiple numbers' digits to not equal the sum of the digits after they are all added is for a place (i.e., tens place, ones place, etc.) to be carried over. If that was a little confusing, note that $63+22=85,$ and $8+5=13.$ $6+3+2+2=13,$ too. The ones don't carry over to the tens and the tens don't carry over to the hundreds. However, $63+37=100,$ and $6+3+3+7=19 \neq 1.$ The ones carry over to the tens and the tens carry over to the hundreds, meaning it loses $2(9-1)=18$ of its digit sum.
If that made sense, note that $111111111$ has $9$ digits. Since the only operation in long multiplication will be $1 \cdot 1$ and the addition tower will be $9$ stacks long, there is no way a $1$ stack can be $10$ long and carry over its value. Thus, it is sufficient to conclude that we will multiply $1$ with $1$ $9 \cdot 9= \boxed{\textbf{(E) }81}$ times, with no $1$ being carried over.
~ Wesserwes7254
Note to author: This made sense $:)$

## Solution 5
We know that for the patterns, \begin{aligned} & 1^2=1 \\ & 11^2=121 \\ & 11^3=12321 \\ & So , (11111111)^2=12345678987654321 \end{aligned}
natural numbers from 1 to go up then down, and number of 1 's gives the middle number for this arrangement and obviously this tricks applicable for number of 1,s $< 10$ . Sum of digits, \( 1+2+3+\cdots+8+9+8+\cdots+3+2+1 \) \( =9^2=81 \) (Square of the middle number)
~KENJAKURA
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .