# 2005 AMC 8 Problem 21

## Problem

How many distinct triangles can be drawn using three of the dots below as vertices?

[asy]dot(origin^^(1,0)^^(2,0)^^(0,1)^^(1,1)^^(2,1));[/asy]

$\textbf{(A)}\ 9\qquad\textbf{(B)}\ 12\qquad\textbf{(C)}\ 18\qquad\textbf{(D)}\ 20\qquad\textbf{(E)}\ 24$

## Solution 1
The number of ways to choose three points to make a triangle is $\binom 63 = 20$ . However, two* of these are a straight line so we subtract $2$ to get $\boxed{\textbf{(C)}\ 18}$ .

## Solution 2
Case 1: One vertex is on the top 3 points
Here, there is $\binom 31 =3$ ways to choose the vertex on the top and $\binom 32 =3$ ways the choose the $2$ on the bottom, so there is $3 \cdot 3=9$ triangles.
Case 2: One vertex is on the bottom 3 points
By symmetry, there is $9$ triangles.
Otherwise, the triangle is degenerate.
Our final answer is $9+9=\boxed{\text{(C) 18}}$ ~ Ddk001

## Video solution
https://www.youtube.com/watch?v=XQS-KVW1O6M ~David
### See Also