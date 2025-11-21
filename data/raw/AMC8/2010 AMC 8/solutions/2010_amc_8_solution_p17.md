# 2010 AMC 8 Problem 17

## Problem

The diagram shows an octagon consisting of $10$ unit squares. The portion below $\overline{PQ}$ is a unit square and a triangle with base $5$ . If $\overline{PQ}$ bisects the area of the octagon, what is the ratio $\dfrac{XQ}{QY}$ ?

[asy] import graph; size(300); real lsf = 0.5; pen dp = linewidth(0.7) + fontsize(10); defaultpen(dp); pen ds = black; pen xdxdff = rgb(0.49,0.49,1); draw((0,0)--(6,0),linewidth(1.2pt)); draw((0,0)--(0,1),linewidth(1.2pt)); draw((0,1)--(1,1),linewidth(1.2pt)); draw((1,1)--(1,2),linewidth(1.2pt)); draw((1,2)--(5,2),linewidth(1.2pt)); draw((5,2)--(5,1),linewidth(1.2pt)); draw((5,1)--(6,1),linewidth(1.2pt)); draw((6,1)--(6,0),linewidth(1.2pt)); draw((1,1)--(5,1),linewidth(1.2pt)); draw((1,1)--(1,0),linewidth(1.2pt)); draw((2,2)--(2,0),linewidth(1.2pt)); draw((3,2)--(3,0),linewidth(1.2pt)); draw((4,2)--(4,0),linewidth(1.2pt)); draw((5,1)--(5,0),linewidth(1.2pt)); draw((0,0)--(5,1.5),linewidth(1.2pt)); dot((0,0),ds); label("$P$", (-0.23,-0.26),NE*lsf); dot((0,1),ds); dot((1,1),ds); dot((1,2),ds); dot((5,2),ds); label("$X$", (5.14,2.02),NE*lsf); dot((5,1),ds); label("$Y$", (5.12,1.14),NE*lsf); dot((6,1),ds); dot((6,0),ds); dot((1,0),ds); dot((2,0),ds); dot((3,0),ds); dot((4,0),ds); dot((5,0),ds); dot((2,2),ds); dot((3,2),ds); dot((4,2),ds); dot((5,1.5),ds); label("$Q$", (5.14,1.51),NE*lsf); clip((-4.19,-5.52)--(-4.19,6.5)--(10.08,6.5)--(10.08,-5.52)--cycle); [/asy]

$\textbf{(A)}\ \frac{2}{5}\qquad\textbf{(B)}\ \frac{1}{2}\qquad\textbf{(C)}\ \frac{3}{5}\qquad\textbf{(D)}\ \frac{2}{3}\qquad\textbf{(E)}\ \frac{3}{4}$

## Solution 1
We see that half the area of the octagon is $5$ . We see that the triangle area is $5-1 = 4$ . That means that $\frac{5h}{2} = 4 \rightarrow h=\frac{8}{5}$ . \[\text{QY}=\frac{8}{5} - 1 = \frac{3}{5}\] Meaning, $\frac{\frac{2}{5}}{\frac{3}{5}} = \boxed{\textbf{(D) }\frac{2}{3}}$

## Solution 2
Like stated in solution 1, we know that half the area of the octagon is $5$ .
After moving the square from the bottom right to the top left, the area of the resulting trapezoid is $5+1=6$ .
$5(XQ+2)/2=6$ . Solving for $XQ$ , we get $XQ=2/5$ .
Subtracting $2/5$ from $1$ , we get $QY=3/5$ .
Therefore, the answer comes out to $\boxed{\textbf{(D) }\frac{2}{3}}$
~kempwood

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=937
### Video by MathTalks
https://www.youtube.com/watch?v=KSYVsSJDX-0&feature=youtu.be

## Video Solution by WhyMath
https://youtu.be/N7Yu9-bLqls
~savannahsolver
### See Also