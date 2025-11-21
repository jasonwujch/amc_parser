# 2006 AMC 10B Problem 8

## Problem

A square of area 40 is inscribed in a semicircle as shown. What is the area of the semicircle?

[asy] defaultpen(linewidth(0.8)); size(100); real r=sqrt(50), s=sqrt(10); draw(Arc(origin, r, 0, 180)); draw((r,0)--(-r,0), dashed); draw((-s,0)--(s,0)--(s,2*s)--(-s,2*s)--cycle); [/asy]

$\textbf{(A) } 20\pi\qquad \textbf{(B) } 25\pi\qquad \textbf{(C) } 30\pi\qquad \textbf{(D) } 40\pi\qquad \textbf{(E) } 50\pi$

## Solution
Since the area of the square is $40$ , the length of a side is $\sqrt{40}=2\sqrt{10}$ . The distance between the center of the semicircle and one of the bottom vertices of the square is half the length of the side, which is $\sqrt{10}$ .
Using the Pythagorean Theorem to find the radius $r$ of the semicircle, $r^2 = (2\sqrt{10})^2 + (\sqrt{10})^2 = 50$ . So, the area of the semicircle is $\frac{1}{2}\cdot \pi \cdot 50 = \boxed{\textbf{(B) }25\pi}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .