# 2016 AMC 8 Problem 5

## Problem

The number $N$ is a two-digit number.

• When $N$ is divided by $9$ , the remainder is $1$ .

• When $N$ is divided by $10$ , the remainder is $3$ .

What is the remainder when $N$ is divided by $11$ ?

$\textbf{(A) }0\qquad\textbf{(B) }2\qquad\textbf{(C) }4\qquad\textbf{(D) }5\qquad \textbf{(E) }7$

## Solution 1
From the second bullet point, we know that the second digit must be $3$ , for a number divisible by $10$ ends in zero. Since there is a remainder of $1$ when $N$ is divided by $9$ , the multiple of $9$ must end in a $2$ for it to have the desired remainder $\pmod {10}.$ We now look for this one:
$9(1)=9\\ 9(2)=18\\ 9(3)=27\\ 9(4)=36\\ 9(5)=45\\ 9(6)=54\\ 9(7)=63\\ 9(8)=72$
The number $72+1=73$ satisfies both conditions. We subtract the biggest multiple of $11$ less than $73$ to get the remainder. Thus, $73-11(6)=73-66=\boxed{\textbf{(E) }7}$ .
~CHECKMATE2021

## Solution 2
We know that the number has to be one more than a multiple of $9$ , because of the remainder of one, and the number has to be $3$ more than a multiple of $10$ , which means that it has to end in a $3$ . Now, if we just list the first few multiples of $9$ adding one to the number we get: $10, 19, 28, 37, 46, 55, 64, 73, 82, 91$ . As we can see from these numbers, the only one that has a three in the units place is $73$ , thus we divide $73$ by $11$ , getting $6$ $R7$ , hence, $\boxed{\textbf{(E) }7}$ . -fn106068
We could also remember that, for a two-digit number to be divisible by $9$ , the sum of its digits has to be equal to $9$ . Since the number is one more than a multiple of $9$ , the multiple we are looking for has a ones digit of $2$ , and therefore a tens digit of $9-2 = 7$ , and then we could proceed as above. -vaisri

## Video Solution
https://youtu.be/d-bCEDoZEjg?si=VFLhpgyJ_vHhE7h3
A solution so simple a 12-year-old made it!
~Elijahman~

## Video Solution by OmegaLearn
https://youtu.be/7an5wU9Q5hk?t=574

## Video Solution
https://youtu.be/aKWQl7kEMy0
~savannahsolver
### See Also