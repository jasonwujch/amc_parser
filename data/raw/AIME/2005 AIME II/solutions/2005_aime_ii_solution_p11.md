# 2005 AIME II Problem 11

## Problem

Let $m$ be a positive integer, and let $a_0, a_1,\ldots,a_m$ be a sequence of reals such that $a_0 = 37, a_1 = 72, a_m = 0,$ and $a_{k+1} = a_{k-1} - \frac 3{a_k}$ for $k = 1,2,\ldots, m-1.$ Find $m.$

## Solution 1
For $0 < k < m$ , we have
$a_{k}a_{k+1} = a_{k-1}a_{k} - 3$ .
Thus the product $a_{k}a_{k+1}$ is a monovariant : it decreases by 3 each time $k$ increases by 1. For $k = 0$ we have $a_{k}a_{k+1} = 37\cdot 72$ , so when $k = \frac{37 \cdot 72}{3} = 888$ , $a_{k}a_{k+1}$ will be zero for the first time, which implies that $m = \boxed{889}$ , our answer.
Note: In order for $a_{m} = 0$ we need $a_{m-2}a_{m-1}=3$ simply by the recursion definition.

## Solution 2
Plugging in $k = m-1$ to the given relation, we get $0 = a_{m-2} - \frac {3}{a_{m-1}} \implies{a_{m-2}a_{m-1} = 3}$ . Inspecting the value of $a_{k}a_{k+1}$ for small values of $k$ , we see that $a_{k}a_{k+1} = 37\cdot 72 - 3k$ . Setting the RHS of this equation equal to $3$ , we find that $m$ must be $\boxed{889}$ .
~ anellipticcurveoverq
### Induction Proof
As above, we experiment with some values of $a_{k}a_{k+1}$ , conjecturing that $a_{m-p}a_{m-p-1}$ = $3p$ ,where $m$ is a positive integer and so is $p$ , and we prove this formally using induction. The base case is for $p = 1$ , $a_{m} = a_{m-2} - 3/a_{m-1}$ Since $a_{m} = 0$ , $a_{m-1}a_{m-2} = 3$ ; from the recursion given in the problem $a_{m-p+1} = a_{m-p-1} - 3/a_{m-p}$ , so $a_{m-p+1} = 3p/a_{m-p} - 3/a_{m-p} = 3(p-1)/a_{m-p}$ , so $a_{m-p}a_{m-p+1} = a_{m-(p-1)}a_{m-(p-1)-1} = 3(p-1)$ , hence proving our formula by induction. ~USAMO2023

## Solution 3 (Telescoping)
Note that $a_{k+1}\cdot a_{k} - a_{k}\cdot a_{k-1} = - 3$ . Then, we can generate a sum of series of equations such that $\sum_{k=1}^{m-1} a_{k+1}\cdot a_{k} - a_{k}\cdot a_{k-1} = - 3(m-1)$ . Then, note that all but the first and last terms on the LHS cancel out, leaving us with $a_m\cdot a_{m-1} - a_1\cdot a_0 = -3(m-1)$ . Plugging in $a_m=0$ , $a_0=37$ , $a_1=72$ , we have $-37\cdot 72 = -3(m-1)$ . Solving for $m$ gives $m=\boxed{889}$ . ~sigma

## Video solution
https://www.youtube.com/watch?v=JfxNr7lv7iQ
These problems are copyrighted © by the Mathematical Association of America.