# 2002 AMC 8 Problem 19

## Problem

How many whole numbers between 99 and 999 contain exactly one 0?

$\text{(A)}\ 72\qquad\text{(B)}\ 90\qquad\text{(C)}\ 144\qquad\text{(D)}\ 162\qquad\text{(E)}\ 180$

## Solution 1
Numbers with exactly one zero have the form $\overline{a0b}$ or $\overline{ab0}$ , where the $a,b \neq 0$ . There are $(9\cdot1\cdot9)+(9\cdot9\cdot1) = 81+81 = \boxed{162}$ such numbers, hence our answer is $\fbox{D}$ .

## Solution 2 (Complementary Counting)
(Whole numbers between 99 and 999)-(Whole numbers which do not contain exactly one 0)= (How many whole numbers between 99 and 999 contain exactly one 0).
$1)$ How many whole numbers are between 99 and 999, $999-99=900$ , so there are 900 numbers between 99 and 999.
$2a)$ How many whole numbers in this range do not contain the digit $0$ , there are $10-1=9$ possible digits for each digit in this three digit number, $9^3=729$ . So there are $729$ numbers in this range which do not contain the digit $0$ .
$2b)$ How many whole numbers in this range contain the digit $0$ 2 times, there are $10-1=9$ possible digits for the first digit and the other two digits have to be the digit $0$ . So there are $9$ of these numbers.
So there are $900-(729+9)$ whole numbers between 99 and 999 that contain exactly one 0.
Simplifying the expression we get that there are $162$ whole numbers between 99 and 999 that contain exactly one 0. So the answer is $\fbox{D}$ .
~blankbox

## Video Solution
https://youtu.be/nctNL-xLImI Soo, DRMS, NM
https://www.youtube.com/watch?v=eAeVBrQ1PQI ~David

## Video Solution by WhyMath
https://youtu.be/3FikBB_Lx7c
### See Also