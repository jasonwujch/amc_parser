# 2005 AMC 10A Problem 16

## Problem

The sum of the digits of a two-digit number is subtracted from the number. The units digit of the result is $6$ . How many two-digit numbers have this property?

$\textbf{(A) } 5\qquad \textbf{(B) } 7\qquad \textbf{(C) } 9\qquad \textbf{(D) } 10\qquad \textbf{(E) } 19$

## Solution 1
Let the number be $10a+b$ , where $a$ is its tens digit and $b$ is its units digit. Then $(10a+b)-(a+b) = 9a$ must have a units digit of $6$ , and as $a$ is the tens digit, we can only have $1 \leq a \leq 9$ , so $9 \leq 9a \leq 81$ .
Accordingly, $9a$ has units digit $6$ only if $9a = 36 \iff a=4$ . Thus the numbers that have the required property are all those with tens digit $4$ , from $40$ to $49$ , so the answer is $49-40+1 = \boxed{\textbf{(D) } 10}$ .

## Solution 2
As in Solution 1, suppose that $a$ and $b$ are the tens and units digits of the number respectively, so the result of the subtraction is $10a+b-(a+b)=9a$ . Thus $9a$ must have units digit $6$ .
We now observe that $10a$ is a multiple of 10, so has units digit $0$ , and hence $10a-9a = a$ will have units digit $10-6 = 4$ (where the $0$ will become $10$ in the subtraction by 'borrowing' $1$ from the tens digit). Since $a$ is a single digit, this simply means $a = 4$ , while $b$ can be any digit from $0$ to $9$ (since it cancelled out in the subtraction above).
Thus, as in Solution 1, there are $10$ possible choices for $b$ with $a = 4$ , so the answer is $\boxed{\textbf{(D) } 10}$ .
~BurpSuite
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .