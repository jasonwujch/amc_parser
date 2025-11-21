# 2014 AMC 10A Problem 19

## Problem

Four cubes with edge lengths $1$ , $2$ , $3$ , and $4$ are stacked as shown. What is the length of the portion of $\overline{XY}$ contained in the cube with edge length $3$ ?

[asy] dotfactor = 3; size(10cm); dot((0, 10)); label("$X$", (0,10),W,fontsize(8pt)); dot((6,2)); label("$Y$", (6,2),E,fontsize(8pt)); draw((0, 0)--(0, 10)--(1, 10)--(1, 9)--(2, 9)--(2, 7)--(3, 7)--(3,4)--(4, 4)--(4, 0)--cycle); draw((0,9)--(1, 9)--(1.5, 9.5)--(1.5, 10.5)--(0.5, 10.5)--(0, 10)); draw((1, 10)--(1.5,10.5)); draw((1.5, 10)--(3,10)--(3,8)--(2,7)--(0,7)); draw((2,9)--(3,10)); draw((3,8.5)--(4.5,8.5)--(4.5,5.5)--(3,4)--(0,4)); draw((3,7)--(4.5,8.5)); draw((4.5,6)--(6,6)--(6,2)--(4,0)); draw((4,4)--(6,6)); label("$1$", (1,9.5), W,fontsize(8pt)); label("$2$", (2,8), W,fontsize(8pt)); label("$3$", (3,5.5), W,fontsize(8pt)); label("$4$", (4,2), W,fontsize(8pt)); [/asy]

$\textbf{(A)}\ \dfrac{3\sqrt{33}}5\qquad\textbf{(B)}\ 2\sqrt3\qquad\textbf{(C)}\ \dfrac{2\sqrt{33}}3\qquad\textbf{(D)}\ 4\qquad\textbf{(E)}\ 3\sqrt2$

## Solution
By Pythagorean Theorem in three dimensions, the distance $XY$ is $\sqrt{4^2+4^2+10^2}=2\sqrt{33}$ .
Let the length of the segment $XY$ that is inside the cube with side length $3$ be $x$ . By similar triangles, $\dfrac{x}{3}=\dfrac{2\sqrt{33}}{10}$ , giving $x=\boxed{\textbf{(A) }\dfrac{3\sqrt{33}}{5}}$ .

## Solution 2 (3D Coordinate Geometry)
Let's redraw the diagram, however make a 3D coordinate plane, using D as the origin.
[asy] dotfactor = 3; size(10cm); dot((0, 10)); label("$X(0,10,0)$", (0,10),W,fontsize(8pt)); dot((6,2)); label("$Y(4,0,4)$", (6,2),E,fontsize(8pt)); draw((0, 0)--(0, 10)--(1, 10)--(1, 9)--(2, 9)--(2, 7)--(3, 7)--(3,4)--(4, 4)--(4, 0)--cycle); draw((0,9)--(1, 9)--(1.5, 9.5)--(1.5, 10.5)--(0.5, 10.5)--(0, 10)); draw((1, 10)--(1.5,10.5)); draw((1.5, 10)--(3,10)--(3,8)--(2,7)--(0,7)); draw((2,9)--(3,10)); draw((3,8.5)--(4.5,8.5)--(4.5,5.5)--(3,4)--(0,4)); draw((3,7)--(4.5,8.5)); draw((4.5,6)--(6,6)--(6,2)--(4,0)); draw((4,4)--(6,6)); label("$1$", (1,9.5), W,fontsize(8pt)); label("$2$", (2,8), W,fontsize(8pt)); label("$3$", (3,5.5), W,fontsize(8pt)); label("$4$", (4,2), W,fontsize(8pt)); label("$D(0,0,0)$", (0,0), W,fontsize(8pt)); [/asy]
Now we can use the distance formula in 3D, which is $\sqrt{(x_{1}-x_{2})^2+(y_{1}-y_{2})^2+(z_{1}-z_{2})^2}$ and plug it in for the distance of $XY$ .
$\sqrt{(0-4)^2+(10-0)^2+(0-4)^2}$
We get the answer as $\sqrt{132} = 2\sqrt{33}$ .
Continuing with solution 1, using similar triangles, we get the answer as $\textbf{(A)}\ \dfrac{3\sqrt{33}}5$
~ghfhgvghj10

## Solution 3
The diagonal of the base of the cube with side length $4$ is $4 \sqrt{2}$ . Hence by similarity:
$XY = \sqrt{3^2 + \left(\frac{3}{10} \cdot 4 \sqrt{2} \right)^2} = \sqrt{\frac{225}{25} + \frac{6^2 \cdot 2}{25}} = \frac{\sqrt{99 \cdot 3}}{5} = \boxed{ \frac{3 \sqrt{33}}{5}}$ .

## Solution 4 (cheap)
If you don't find any of the solutions above, you can solve the problem in 2D, by considering squares of side lengths $1$ , $2$ , $3$ , and $4$ . The total length of the line will be $\sqrt{4^2 + 10^2} = 2\sqrt{29}$ . Using similar triangles, we get that the length of the segment through the square with side $3$ is $\frac{3\sqrt{29}}{5}$ . Alternatively, note that this length is equal to $\frac{3}{1 + 2 + 3 + 4}\cdot 2\sqrt{29} = \frac{3\sqrt{29}}{5}$ . Thus $\boxed{\text{(A)}}$ , the only option with a denominator of $5$ , is likely to be the correct answer.

## Video Solution
https://youtu.be/4FInNJ9wM6s
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .