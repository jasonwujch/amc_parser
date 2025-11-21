# 2015 AMC 10A Problem 18

## Problem

Hexadecimal (base-16) numbers are written using numeric digits $0$ through $9$ as well as the letters $A$ through $F$ to represent $10$ through $15$ . Among the first $1000$ positive integers, there are $n$ whose hexadecimal representation contains only numeric digits. What is the sum of the digits of $n$ ?

$\textbf{(A) }17\qquad\textbf{(B) }18\qquad\textbf{(C) }19\qquad\textbf{(D) }20\qquad\textbf{(E) }21$

## Solution 1
Notice that $1000$ is $3E8$ when converted to hexadecimal ( $3 \cdot 16^2 + 14 \cdot 16^1 + 8 \cdot 16^0$ ). We will proceed by constructing numbers that consist of only numeric digits in hexadecimal.
The first digit could be $0,$ $1,$ $2,$ or $3,$ and the second two could be any digit $0 - 9$ , giving $4 \cdot 10 \cdot 10 = 400$ combinations. However, this includes $000,$ so this number must be diminished by $1.$ Therefore, there are $399$ valid $n$ corresponding to those $399$ positive integers less than $1000$ that consist of only numeric digits. (Notice that $399$ is the least hexadecimal number using only decimal digits before $3E8$ .) Therefore, our answer is $3 + 9 + 9 = \boxed{\textbf{(E) } 21}$

## Solution 2 (Casework)
First, we set a bound by writing $1000$ in base- $16$ . $1000_{10}=3E8_{16}$ . Therefore, we are considering numbers with a maximum of $3$ digits, and a maximum of $3$ in the $256$ ths-place (the first place in a $3$ -digit number).
Case $1$ : $1$ -digit numbers: There are evidently $9$ numbers that fit this category.
Case $2$ : $2$ -digit numbers: There are $9\cdot10=90$ numbers that fit this category.
Case $3$ : $3$ -digit numbers: There are $3\cdot10\cdot10=300$ numbers that fit this category
Adding these up, we get $9+90+300=399$ numbers. $3 + 9 + 9 = \boxed{\textbf{(E) } 21}$ ~sosiaops

## Solution 3
We can quickly see that $400$ in hexadecimal = $0+0+16^2*4$ = 1024. If we go down to 399 in hexadecimal, we have $9+9*16+3*256$ which is $921$ , which is obviously less than 1000. Therefore, the answer is $3+9+9$ = $\boxed{\textbf{(E) } 21}$
~Arcticturn

## Video Solutions
https://youtu.be/ZhAZ1oPe5Ds?t=4596
https://www.youtube.com/watch?v=2DVSkWu_H1g
https://youtu.be/jkxWTsfbAjQ
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .