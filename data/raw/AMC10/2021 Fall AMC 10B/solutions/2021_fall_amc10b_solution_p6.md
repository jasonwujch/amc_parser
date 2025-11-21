# 2021 Fall AMC 10B Problem 6

## Problem

The least positive integer with exactly $2021$ distinct positive divisors can be written in the form $m \cdot 6^k$ , where $m$ and $k$ are integers and $6$ is not a divisor of $m$ . What is $m+k?$

$(\textbf{A})\: 47\qquad(\textbf{B}) \: 58\qquad(\textbf{C}) \: 59\qquad(\textbf{D}) \: 88\qquad(\textbf{E}) \: 90$

## Solution 1
Let this positive integer be written as $p_1^{e_1}\cdot p_2^{e_2}$ . The number of factors of this number is therefore $(e_1+1) \cdot (e_2+1)$ , and this must equal 2021. The prime factorization of 2021 is $43 \cdot 47$ , so $e_1+1 = 43 \implies e_1=42$ and $e_2+1=47\implies e_2=46$ . To minimize this integer, we set $p_1 = 3$ and $p_2 = 2$ . Then this integer is $3^{42} \cdot 2^{46} = 2^4 \cdot 2^{42} \cdot 3^{42} = 16 \cdot 6^{42}$ . Now $m=16$ and $k=42$ so $m+k = 16 + 42 = \boxed{\textbf{(B) }58}$
~KingRavi

## Solution 2
Recall that $6^k$ can be written as $2^k \cdot 3^k$ . Since we want the integer to have $2021$ divisors, we must have it in the form $p_1^{42} \cdot p_2^{46}$ , where $p_1$ and $p_2$ are prime numbers. Therefore, we want $p_1$ to be $3$ and $p_2$ to be $2$ . To make up the remaining $2^4$ , we multiply $2^{42} \cdot 3^{42}$ by $m$ , which is $2^4$ which is $16$ . Therefore, we have $42 + 16 = \boxed{\textbf{(B) }58}$
~Arcticturn

## Solution 3
If a number has prime factorization $p_1^{k_1} p_2^{k_2} \cdots p_m^{k_m}$ , then the number of distinct positive divisors of this number is $\left( k_1 + 1 \right) \left( k_2 + 1 \right) \cdots \left( k_m + 1 \right)$ .
We have $2021 = 43 \cdot 47$ . Hence, if a number $N$ has 2021 distinct positive divisors, then $N$ takes one of the following forms: $p_1^{2020}$ , $p_1^{42} p_2^{46}$ .
Therefore, the smallest $N$ is $3^{42} 2^{46} = 2^4 \cdot 6^{42} = 16 \cdot 6^{42}$ .
Therefore, the answer is $\boxed{\textbf{(B) }58}$ .
~Steven Chen (www.professorchenedu.com)

## Video Solution by Interstigation
https://youtu.be/p9_RH4s-kBA?t=530

## Video Solution
https://youtu.be/bRohyPen8ik
~Education, the Study of Everything

## Video Solution by WhyMath
https://youtu.be/bErxcXXwWkw
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/RyN-fKNtd3A
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .