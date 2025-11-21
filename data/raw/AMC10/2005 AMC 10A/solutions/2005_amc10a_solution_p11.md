# 2005 AMC 10A Problem 11

## Problem

A wooden cube $n$ units on a side is painted red on all six faces and then cut into $n^3$ unit cubes. Exactly one-fourth of the total number of faces of the unit cubes are red. What is $n$ ?

$\textbf{(A) } 3\qquad \textbf{(B) } 4\qquad \textbf{(C) } 5\qquad \textbf{(D) } 6\qquad \textbf{(E) } 7$

## Solution 1
Since there are $n^2$ little faces on each face of the big wooden cube, there are a total of $6n^2$ little faces painted red. Moreover, as each unit cube has $6$ faces, there are $6n^3$ little faces in total.
Accordingly, as one-fourth of the little faces are painted red, we have \[\frac{6n^2}{6n^3} = \frac{1}{4} \iff \frac{1}{n} = \frac{1}{4} \iff n = \boxed{\textbf{(B) } 4}.\]

## Solution 2
We recall that when a cube of side length $n$ has its entire surface painted and is then split into $n^3$ unit cubes, there will be exactly $(n-2)^3$ unit cubes with $0$ faces painted, $6(n-2)^2$ unit cubes with $1$ face painted, $12(n-2)$ unit cubes with $2$ faces painted, and $8$ unit cubes with $3$ faces painted.
(Observe that these form the terms of the binomial expansion of $n^3 = \left(\left(n-2\right)+2\right)^3$ .)
Hence the total number of faces painted red is \begin{align*}(n-2)^3 \cdot 0 + 6(n-2)^2 \cdot 1 + 12(n-2) \cdot 2 + 8 \cdot 3 &= 6\left(n^2-4n+4\right)+24n-48+24 \\ &= 6n^2-24n+24+24n-24 \\ &= 6n^2,\end{align*} and now we may proceed as in Solution 1, again giving $n = \boxed{\textbf{(B) } 4}.$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .