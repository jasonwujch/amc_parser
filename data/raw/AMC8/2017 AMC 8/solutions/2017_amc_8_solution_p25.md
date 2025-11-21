# 2017 AMC 8 Problem 25

## Problem

In the figure shown, $\overline{US}$ and $\overline{UT}$ are line segments each of length 2, and $m\angle TUS = 60^\circ$ . Arcs $\overarc{TR}$ and $\overarc{SR}$ are each one-sixth of a circle with radius 2. What is the area of the region shown?

[asy]draw((1,1.732)--(2,3.464)--(3,1.732)); draw(arc((0,0),(2,0),(1,1.732))); draw(arc((4,0),(3,1.732),(2,0))); label("$U$", (2,3.464), N); label("$S$", (1,1.732), W); label("$T$", (3,1.732), E); label("$R$", (2,0), S);[/asy]

$\textbf{(A) }3\sqrt{3}-\pi\qquad\textbf{(B) }4\sqrt{3}-\frac{4\pi}{3}\qquad\textbf{(C) }2\sqrt{3}\qquad\textbf{(D) }4\sqrt{3}-\frac{2\pi}{3}\qquad\textbf{(E) }4+\frac{4\pi}{3}$

## Solution 1
[asy]draw((1,1.732)--(2,3.464)--(3,1.732)); draw(arc((0,0),(2,0),(1,1.732))); draw(arc((4,0),(3,1.732),(2,0))); label("$U$", (2,3.464), N); label("$S$", (1,1.732), W); label("$T$", (3,1.732), E); label("$R$", (2,0), S);[/asy]
In addition to the given diagram, we can draw lines $\overline{SR}$ and $\overline{RT}.$ The area of rhombus $SRTU$ is half the product of its diagonals, which is $\frac{2\sqrt3 \cdot 2}{2}=2\sqrt3$ . However, we have to subtract off the circular segments. The area of those can be found by computing the area of the circle with radius 2, multiplying it by $\frac{1}{6}$ , then finally subtracting the area of an equilateral triangle with a side length 2 from the sector. The sum of the areas of the circular segments is $2(\frac{4 \pi}{6}-\sqrt3).$ The area of rhombus $SRTU$ minus the circular segments is $2\sqrt3-\frac{4 \pi}{3}+2\sqrt3= \boxed{\textbf{(B)}\ 4\sqrt{3}-\frac{4\pi}{3}}.$
~PEKKA

## Solution 2 (tiny bit intuitional)
We can extend $\overline{US}$ , $\overline{UT}$ to $X$ and $Y$ , respectively, such that $X$ and $Y$ are collinear to point $R$ . Connect $\overline{XY}$ . We can see points $X$ , $Y$ are probably circle centers of arc $SR$ , $TR$ , respectively. So, $\overline{XS} = 2 = \overline{TY}$ . Thus, $\triangle{UXY}$ is equilateral. The area of $\triangle{UXY}$ is $\frac{\sqrt{3}}{4} \cdot 4^2$ , or $4\sqrt{3}$ , and both one sixth circles total up to $\frac{4\pi}{3}$ . Finally, the answer is $\boxed{\textbf{(B)} 4\sqrt{3}-\frac{4\pi}{3}}$ .
~ lovelearning999

## Video Solutions
https://youtu.be/sVclz6EmpEU
~savannahsolver
### See Also