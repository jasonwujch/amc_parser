# 2006 AIME I Problem 7

## Problem

An angle is drawn on a set of equally spaced parallel lines as shown. The ratio of the area of shaded region $C$ to the area of shaded region $B$ is 11/5. Find the ratio of shaded region $D$ to the area of shaded region $A.$

[asy] defaultpen(linewidth(0.7)+fontsize(10)); for(int i=0; i<4; i=i+1) { fill((2*i,0)--(2*i+1,0)--(2*i+1,6)--(2*i,6)--cycle, mediumgray); } pair A=(1/3,4), B=A+7.5*dir(-17), C=A+7*dir(10); draw(B--A--C); fill((7.3,0)--(7.8,0)--(7.8,6)--(7.3,6)--cycle, white); clip(B--A--C--cycle); for(int i=0; i<9; i=i+1) { draw((i,1)--(i,6)); } label("$\mathcal{A}$", A+0.2*dir(-17), S); label("$\mathcal{B}$", A+2.3*dir(-17), S); label("$\mathcal{C}$", A+4.4*dir(-17), S); label("$\mathcal{D}$", A+6.5*dir(-17), S);[/asy]

## Solution 1
Note that the apex of the angle is not on the parallel lines. Set up a coordinate proof .
Let the set of parallel lines be perpendicular to the x-axis , such that they cross it at $0, 1, 2 \ldots$ . The base of region $\mathcal{A}$ is on the line $x = 1$ . The bigger base of region $\mathcal{D}$ is on the line $x = 7$ . Let the top side of the angle be $y = x - s$ and the bottom side be x-axis, as dividing the angle doesn't change the problem.
Since the area of the triangle is equal to $\frac{1}{2}bh$ ,
\[\frac{\textrm{Region\ }\mathcal{C}}{\textrm{Region\ }\mathcal{B}} = \frac{11}{5} = \frac{\frac 12(5-s)^2 - \frac 12(4-s)^2}{\frac 12(3-s)^2 - \frac12(2-s)^2}\]
Solve this to find that $s = \frac{5}{6}$ .
Using the same reasoning as above, we get $\frac{\textrm{Region\ }\mathcal{D}}{\textrm{Region\ }\mathcal{A}} = \frac{\frac 12(7-s)^2 - \frac 12(6-s)^2}{\frac 12(1-s)^2}$ , which is $\boxed{408}$ .

## Solution 2
Note that the sections between the two transversals can be divided into one small triangle and a number of trapezoids. Let one side length (not on a parallel line) of the small triangle be $x$ and the area of it be $x^2$ . Also, let all sections of the line on the same side as the side with length $x$ on a trapezoid be equal to $1$ .
Move on to the second-smallest triangle, formed by attaching this triangle with the next trapezoid. Parallel lines give us similar triangles, so we know the proportion of this triangle to the previous triangle is ${\left(\frac{x+1}{x}\right)}^2$ . Multiplying, we get $(x+1)^2$ as the area of the triangle, so the area of the trapezoid is $2x+1$ . Repeating this process, we get that the area of B is $2x+3$ , the area of C is $2x+7$ , and the area of D is $2x+11$ .
We can now use the given condition that the ratio of C and B is $\frac{11}{5}$ .
$\frac{11}{5} = \frac{2x+7}{2x+3}$ gives us $x = \frac{1}{6}$
So now we compute the ratio of D and A, which is $\frac{(2)(\frac{1}{6}) + 11}{(\frac{1}{6})^2} = \boxed{408.}$
Edit: fixed misplaced brackets

## Solution 3 (Bash)
Let the distances from the apex to the parallel lines be $x$ and $y$ and the distance between the intersections be $a,b.$ We know the area ratio means $\frac{(x+4a)(y+4b)-(x+3a)(y+3b)}{(x+2a)(y+2b)-(x+a)(y+b)} =\frac{5}{11}$ which simplifying yields $ab = 3ay+3bx.$ The ratio we seek is $\frac{(x+6a)(y+6b)-(x+5a)(y+5b)}{xy} =\frac{ay+yx+11ab}{xy}.$ We know that $ab = 3ay+3bx$ so the ratio we seed is $\frac{33(ay+yx)}{11xy}.$ Finally note that by similar triangles $\frac{x}{x+a} =\frac{y}{y+b} \implies bx = ya.$ Therefore the ratio we seek is $\frac{66(ay)}{11xy} =\frac{66a}{11x}.$ Finally note that $ab=3ay+3bx \implies ab = 6bx \implies a = 6x$ so the final ratio is $6 \cdot 68 = \boxed{408}.$
These problems are copyrighted © by the Mathematical Association of America.