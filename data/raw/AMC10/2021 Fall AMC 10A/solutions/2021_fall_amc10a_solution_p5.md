# 2021 Fall AMC 10A Problem 5

## Problem

The six-digit number $\underline{2}\,\underline{0}\,\underline{2}\,\underline{1}\,\underline{0}\,\underline{A}$ is prime for only one digit $A.$ What is $A?$

$\textbf{(A)}\ 1 \qquad\textbf{(B)}\ 3 \qquad\textbf{(C)}\ 5 \qquad\textbf{(D)}\ 7 \qquad\textbf{(E)}\ 9$

## Solution 1
First, modulo $2$ or $5$ , $\underline{20210A} \equiv A$ . Hence, $A \neq 0, 2, 4, 5, 6, 8$ .
Second modulo $3$ , $\underline{20210A} \equiv 2 + 0 + 2 + 1 + 0 + A \equiv 5 + A$ . Hence, $A \neq 1, 4, 7$ .
Third, modulo $11$ , $\underline{20210A} \equiv A + 1 + 0 - 0 - 2 - 2 \equiv A - 3$ . Hence, $A \neq 3$ .
Therefore, the answer is $\boxed{\textbf{(E)}\ 9}$ .
~NH14 ~Steven Chen (www.professorchenedu.com)

## Solution 2 (Elimination)
Any number ending in $5$ is divisible by $5$ . So we can eliminate option $\textbf{(C)}$ .
If the sum of the digits of a number is divisible by $3$ , the number is divisible by $3$ . The sum of the digits of this number is $2 + 0 + 2 + 1 + 0 + A = 5 + A$ . If $5 + A$ is divisible by $3$ , the number is divisible by $3$ . Thus we can eliminate options $\textbf{(A)}$ and $\textbf{(D)}$ .
So the correct option is either $\textbf{(B)}$ or $\textbf{(E)}$ . Let's try dividing the number with some integers.
$20210A/7 = 2887x$ , where $x$ is $1A/7$ . Since $13$ and $19$ are both indivisible by $7$ , this does not help us narrow the choices down.
$20210A/11 = 1837x$ , where $x$ is $3A/11$ . Since $33/11 = 3$ , option $\textbf{(B)}$ would make $20210A$ divisible by $11$ . Thus, by elimination, the correct choice must be option $\boxed{\textbf{(E)}\ 9}$ .
~ZoBro23

## Solution 3
$202100 \implies$ divisible by $2$ .
$202101 \implies$ divisible by $3$ .
$202102 \implies$ divisible by $2$ .
$202103 \implies$ divisible by $11$ .
$202104 \implies$ divisible by $2$ .
$202105 \implies$ divisible by $5$ .
$202106 \implies$ divisible by $2$ .
$202107 \implies$ divisible by $3$ .
$202108 \implies$ divisible by $2$ .
This leaves only $A=\boxed{\textbf{(E)}\ 9}$ .
~wamofan
### Sidenote
The divisibility test for $11$ is if the difference between the sum of the alternating digits is $0$ or $11$ , then that number is divisible by $11$ . For $202103$ , we have $2$ + $2$ - $1$ - $3$ = $0$ .
For $7$ , the divisibility test can be slow. Take the last digit, double it, and subtract it from the rest of the number. If it is divisible by $7$ , then the original number is divisible by $7$ . If the number is too large to determine whether or not it is a multiple of $7$ , then we repeat the process until we can determine whether or not the number is divisible by $7$ .
~Yvz2900

## Video Solution (Simple and Quick)
https://youtu.be/7_Dg9b2hQ5U
~Education, the Study of Everything

## Video Solution
https://youtu.be/jxnTkY3eb5Y
~savannahsolver

## Video Solution
https://youtu.be/AgzDyKlmNAo
~Charles3829

## Video Solution by TheBeautyofMath
for AMC 10: https://youtu.be/o98vGHAUYjM?t=623
for AMC 12: https://youtu.be/jY-17W6dA3c?t=392
~IceMatrix

## Video Solution
https://youtu.be/7TnFYSJ8i14
~Lucas

## Video Solution
https://youtu.be/7_Dg9b2hQ5U
~Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .