# 2005 AMC 10A Problem 14

## Problem

How many three-digit numbers satisfy the property that the middle digit is the average of the first and the last digits?

$\textbf{(A) } 41\qquad \textbf{(B) } 42\qquad \textbf{(C) } 43\qquad \textbf{(D) } 44\qquad \textbf{(E) } 45$

## Solution 1
If the middle digit is the average of the first and last digits, twice the middle digit must be equal to the sum of the first and last digits.
Doing some casework :
If the middle digit is $1$ , possible numbers range from $111$ to $210$ . So there are $2$ numbers in this case.
If the middle digit is $2$ , possible numbers range from $123$ to $420$ . So there are $4$ numbers in this case.
If the middle digit is $3$ , possible numbers range from $135$ to $630$ . So there are $6$ numbers in this case.
If the middle digit is $4$ , possible numbers range from $147$ to $840$ . So there are $8$ numbers in this case.
If the middle digit is $5$ , possible numbers range from $159$ to $951$ . So there are $9$ numbers in this case.
If the middle digit is $6$ , possible numbers range from $369$ to $963$ . So there are $7$ numbers in this case.
If the middle digit is $7$ , possible numbers range from $579$ to $975$ . So there are $5$ numbers in this case.
If the middle digit is $8$ , possible numbers range from $789$ to $987$ . So there are $3$ numbers in this case.
If the middle digit is $9$ , the only possible number is $999$ . So there is $1$ number in this case.
So the total number of three-digit numbers that satisfy the property is $2+4+6+8+9+7+5+3+1=\boxed{\textbf{(E) } 45}$ .

## Solution 2
Alternatively, we could note that the middle digit is uniquely defined by the first and third digits since it is half of their sum. This also means that the sum of the first and third digits must be even. Since even numbers are formed either by adding two odd numbers or two even numbers, we can split our problem into $2$ cases:
If both the first digit and the last digit are odd, then we have $1, 3, 5, 7,$ or $9$ as choices for each of these digits, and there are $5\cdot5=25$ numbers in this case.
If both the first and last digits are even, then we have $2, 4, 6, 8$ as our choices for the first digit and $0, 2, 4, 6, 8$ for the third digit. There are $4\cdot5=20$ numbers here.
The total number, then, is $20+25=\boxed{\textbf{(E) } 45}$ .

## Solution 3
As we noted in Solution 2, we note that the sum of the first and third digits has to be even. The first digit can have $9$ possibilities $(1-9)$ , and the third digit can have $10$ possibilities $(0-9)$ . This means there can be $9\cdot10=90$ possible two-digit numbers in which the first digit and the third digit are digits. Exactly half of these would have their sum be divisible by $2$ (since $90$ is even), so our answer is $\frac{90}{2}=\boxed{\textbf{(E) }45}$ .
- SweetMango77

## Solution 4
If our first digit is odd, the last digit also has to be odd for there to be a whole number middle digit that is the average of the first and the last digits.
If our first digit is even, the last digit has to be even, or $0$ for there to be a whole number middle digit that is the average of the first and the last digits.
As there are $5$ different possible values for each starting digit of our number, we can multiply that by the number of possible first digits $(1-9)$ to achieve our desired solution. $5 \cdot 9 = \boxed{\textbf{(E) }45}$ .
-JinhoK

## Video Solution
https://youtu.be/eItd9O8cCnQ
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .