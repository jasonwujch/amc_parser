# 2002 AMC 10B Problem 19

## Problem

Suppose that $\{a_n\}$ is an arithmetic sequence with \[a_1+a_2+\cdots+a_{100}=100 \text{ and } a_{101}+a_{102}+\cdots+a_{200}=200.\] What is the value of $a_2 - a_1 ?$

$\mathrm{(A) \ } 0.0001\qquad \mathrm{(B) \ } 0.001\qquad \mathrm{(C) \ } 0.01\qquad \mathrm{(D) \ } 0.1\qquad \mathrm{(E) \ } 1$

## Solution 1
We should realize that the two equations are 100 terms apart, so by subtracting the two equations in a form like...
\[(a_{101} - a_1) + (a_{102} - a_2) +... + (a_{200} - a_{100}) = 200-100 = 100\]
...we get the value of the common difference of every hundred terms one hundred times. So we have to divide the answer by one hundred to get ...
$\frac{100}{100} = 1$
...the common difference of every hundred terms. Then we have to simply divide the answer by hundred again to find the common difference between one term, therefore...
$\frac{1}{100} =\boxed{(\textbf{C})\ 0.01}$

## Solution 2
Adding the two given equations together gives
$a_1+a_2+...+a_{200}=300$ .
Now, let the common difference be $d$ . Notice that $a_2-a_1=d$ , so we merely need to find $d$ to get the answer. The formula for an arithmetic sum is
$\frac{n}{2}\left(2a_1+d(n-1)\right)$ ,
where $a_1$ is the first term, $n$ is the number of terms, and $d$ is the common difference. Now we use this formula to find a closed form for the first given equation and the sum of the given equations. For the first equation, we have $n=100$ . Therefore, we have
$50(2a_1+99d)=100$ ,
or
$2a_1+99d=2$ . * (1)
For the sum of the equations (shown at the beginning of the solution) we have $n=200$ , so
$100(2a_1+199d)=300$
or
$2a_1+199d=3$ * (2)
Now we have a system of equations in terms of $a_1$ and $d$ . Subtracting (1) from (2) eliminates $a_1$ , yielding $100d=1$ , and $d=a_2-a_1=\frac{1}{100}=\boxed{(\textbf{C})\ 0.01}$ .

## Solution 3
Subtracting the 2 given equations yields
$(a_{101}-a_1)+(a_{102}-a_2)+(a_{103}-a_3)+...+(a_{200}-a_{100})=100$
Now express each $a_n$ in terms of first term $a_1$ and common difference $x$ between consecutive terms
$((a_1+100x)-(a_1))+((a_1+101x)-(a_1+x))+((a_1+102x)-(a_1+2x))+...+((a_1+199x)-(a_1+99x))=100$
Simplifying and canceling $a_1$ and $x$ terms gives
$100x+100x+100x+...+100x=100$
$100x\times100=100$
$100x=1$
$x=0.01=\boxed{(\textbf{C})\ 0.01}$

## Video Solution by OmegaLearn
https://youtu.be/tKsYSBdeVuw?t=4410
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=38p1OD_ATFE ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .