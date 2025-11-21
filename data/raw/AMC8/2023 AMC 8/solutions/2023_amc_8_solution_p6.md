# 2023 AMC 8 Problem 6

## Problem

The digits $2,0,2,$ and $3$ are placed in the expression below, one digit per box. What is the maximum possible value of the expression?

[asy] // Diagram by TheMathGuyd. I can compress this later size(5cm); real w=2.2; pair O,I,J; O=(0,0);I=(1,0);J=(0,1); path bsqb = O--I; path bsqr = I--I+J; path bsqt = I+J--J; path bsql = J--O; path lsqb = shift((1.2,0.75))*scale(0.5)*bsqb; path lsqr = shift((1.2,0.75))*scale(0.5)*bsqr; path lsqt = shift((1.2,0.75))*scale(0.5)*bsqt; path lsql = shift((1.2,0.75))*scale(0.5)*bsql; draw(bsqb,dashed); draw(bsqr,dashed); draw(bsqt,dashed); draw(bsql,dashed); draw(lsqb,dashed); draw(lsqr,dashed); draw(lsqt,dashed); draw(lsql,dashed); label(scale(3)*"$\times$",(w,1/3)); draw(shift(1.3w,0)*bsqb,dashed); draw(shift(1.3w,0)*bsqr,dashed); draw(shift(1.3w,0)*bsqt,dashed); draw(shift(1.3w,0)*bsql,dashed); draw(shift(1.3w,0)*lsqb,dashed); draw(shift(1.3w,0)*lsqr,dashed); draw(shift(1.3w,0)*lsqt,dashed); draw(shift(1.3w,0)*lsql,dashed); [/asy]

$\textbf{(A) }0 \qquad \textbf{(B) }8 \qquad \textbf{(C) }9 \qquad \textbf{(D) }16 \qquad \textbf{(E) }18$

## Solution 1
First, let us consider the case where $0$ is a base: This would result in the entire expression being $0.$ Contrastingly, if $0$ is an exponent, we will get a value greater than $0.$ $3^2\times2^0=9$ is greater than $2^3\times2^0=8$ and $2^2\times3^0=4.$ Therefore, the answer is $\boxed{\textbf{(C) }9}.$

## Solution 2
The maximum possible value of using the digits $2,0,2,$ and $3$ : We can maximize our value by keeping the $3$ and $2$ together in one power (the biggest with the biggest and the smallest with the smallest). This shows $3^{2}\times2^{0}=9\times1=9.$ (We don't want $0^{2}$ because that is $0$ .) It is going to be $\boxed{\textbf{(C)}\ 9}.$

## Solution 3
Trying all $12$ distinct orderings, we see that the only possible values are $0,4,8,$ and $9,$ the greatest of which is $\boxed{\textbf{(C)}\ 9}.$
~A_MatheMagician

## Solution 4
There are two 2’s and one 3. To make use of them all, use 2 and 3 as the bases and 2 and 0 as the exponents.
~spacepandamath13 .

## Solution 5
If 0 is a base, then the whole expression becomes 0. Therefore, 0 must be an exponent. But since $2^0$ = $3^0$ = $1$ , we do not want to waste our 3 on the 0. We will have a 3 and a 2 left, and since $3^2$ is greater than $2^3$ , we get $3^2\cdot2^0$ = $9$ .
~DrDominic

## Video Solution by CoolMathProblmes
https://youtu.be/Pf93RGtKo1I?feature=shared&t=381

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=299 ~hsnacademy

## Video Solution by Math-X (Smart and Simple)
https://youtu.be/Ku_c1YHnLt0?si=TGWfKGTgBNwzH3xf&t=763 ~Math-X

## Video Solution (HOW TO CREATIVELY THINK!!!)
https://youtu.be/HW6TUhQTj0o
~Education the Study of everything

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=5247

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=EcrktBc8zrM

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=439

## Video Solution by WhyMath
https://youtu.be/vKdWbtXYgz4
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=35BW7bsm_Cg&t=679s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/5Gw0hMUzp4s
### See Also