# 2006 AMC 10A Problem 19

## Problem

How many non- similar triangles have angles whose degree measures are distinct positive integers in arithmetic progression ?

$\textbf{(A) } 0\qquad\textbf{(B) } 1\qquad\textbf{(C) } 59\qquad\textbf{(D) } 89\qquad\textbf{(E) } 178\qquad$

## Solution
The sum of the angles of a triangle is $180$ degrees. For an arithmetic progression with an odd number of terms, the middle term is equal to the average of the sum of all of the terms, making it $\frac{180}{3} = 60$ degrees. The minimum possible value for the smallest angle is $1$ and the highest possible is $59$ (since the numbers are distinct), so there are $\boxed{\textbf{(C) }59}$ possibilities.

## Solution 2 (Stars and Bars)
Let the first angle be $x$ , and the common difference be $d$ . The arithmetic progression can now be expressed as $x + (x + d) + (x + 2d) = 180$ . Simplifiying, $x + d = 60$ . Now, using stars and bars, we have $\binom{61}{1} = 61$ . However, we must subtract the two cases in which either $x$ or $d$ equal $0$ , so we have $61 - 2$ = $\boxed{\textbf{(C) }59}$ .

## Solution 3 (Quick Summation)
Consider that we have $(a+n)+(a+n+1)+(a+n+2)=180 \Longleftrightarrow 3a+3(n+1)=180 \Longleftrightarrow a=59-n$ , where $n \geq 0$ and $n$ is an integer. Since $a \neq 0$ , $n=0,1,2,3,\cdots, 58$ which is $\boxed{\textbf{(C) }59}$ solutions.
~~QuantumPsiInverted
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .