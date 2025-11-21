# 2004 AMC 8 Problem 17

## Problem

Three friends have a total of $6$ identical pencils, and each one has at least one pencil. In how many ways can this happen?

$\textbf{(A)}\ 1\qquad \textbf{(B)}\ 3\qquad \textbf{(C)}\ 6\qquad \textbf{(D)}\ 10 \qquad \textbf{(E)}\ 12$

## Solution 1
For each person to have at least one pencil, assign one pencil to each of the three friends so that you have $3$ left. In partitioning the remaining $3$ pencils into $3$ distinct groups, use Ball-and-urn to find the number of possibilities is $\binom{3+3-1}{3-1} = \binom{5}{2} = \boxed{\textbf{(D)}\ 10}$ .
Solution by phoenixfire Minor Edit by Yuvag

## Solution 2
Like in solution 1, for each person to have at least one pencil, assign one of the pencils to each of the three friends so that you have $3$ left. In partitioning the remaining $3$ pencils into $3$ distinct groups, use number of non-negative integral solutions. Let the three friends be $a, b, c$ respectively.
$a+b+c = 3$ The total being 3 and 2 plus signs, which implies $\binom{3+2}{2} = \binom{5}{2} = \boxed{\textbf{(D)}\ 10}$ .
Solution by phoenixfire Minor Edit by Yuvag

## Solution 3
For each of the 3 People to have at least one pencil when distributing 6 pencil amongst them, we can use another formula from the Ball-and-urn counting technique, shown below:
for n = number of items, and s = slots:
Now we can plug in our values,
number of items = 6, and slots = 3:
$\binom{6-1}{3-1} = \binom{5}{2} = \boxed{\textbf{(D)}\ 10}$ .
Solution by Yuvag

## Solution 4
Like in solution 1 and solution 2, assign one pencil to each of the three friends so that you have $3$ left. In partitioning the remaining $3$ pencils into $3$ distinct groups use casework. Let the three friends be $a$ , $b$ , $c$ repectively.
$a+b +c = 3$ ,
Case $1:a=0$ ,
$b+c = 3$ ,
$b = 0,1,2,3$ ,
$c = 3,2,1,0$ ,
$\boxed{\textbf\ 4}$ solutions.
Case $2:a=1$ ,
$1 + b + c = 3$ ,
$b + c = 2$ ,
$b = 0,1,2$ ,
$c = 2,1,0$ ,
$\boxed{\textbf\ 3}$ solutions.
Case $3:a= 2$ ,
$2 + b + c = 3$ ,
$b + c = 1$ ,
$b = 0,1$ ,
$c = 1,0$ ,
$\boxed{\textbf\ 2}$ solutions.
Case $4:a = 3$ ,
$3+b+c = 3$ ,
$b+c = 0$ ,
$b = 0$ ,
$c = 0$ ,
$\boxed{\textbf\ 1}$ solution.
Therefore there will be a total of $4+3+2+1=\boxed{\textbf{(D)}\ 10}$ solutions. Solution by phoenixfire

## Video Solution
https://youtu.be/FUnwTLP7gr0 Soo, DRMS, NM
### See Also