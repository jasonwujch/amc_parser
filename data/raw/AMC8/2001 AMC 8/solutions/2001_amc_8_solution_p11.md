# 2001 AMC 8 Problem 11

## Problem

Points $A$ , $B$ , $C$ and $D$ have these coordinates: $A(3,2)$ , $B(3,-2)$ , $C(-3,-2)$ and $D(-3, 0)$ . The area of quadrilateral $ABCD$ is

[asy] for (int i = -4; i <= 4; ++i) { for (int j = -4; j <= 4; ++j) { dot((i,j)); } } draw((0,-4)--(0,4),linewidth(1)); draw((-4,0)--(4,0),linewidth(1)); for (int i = -4; i <= 4; ++i) { draw((i,-1/3)--(i,1/3),linewidth(0.5)); draw((-1/3,i)--(1/3,i),linewidth(0.5)); } [/asy]

$\text{(A)}\ 12 \qquad \text{(B)}\ 15 \qquad \text{(C)}\ 18 \qquad \text{(D)}\ 21 \qquad \text{(E)}\ 24$

## Solution #1
[asy] for (int i = -4; i <= 4; ++i) { for (int j = -4; j <= 4; ++j) { dot((i,j)); } } draw((0,-4)--(0,4),linewidth(1)); draw((-4,0)--(4,0),linewidth(1)); for (int i = -4; i <= 4; ++i) { draw((i,-1/3)--(i,1/3),linewidth(0.5)); draw((-1/3,i)--(1/3,i),linewidth(0.5)); } { draw((3,2)--(3,-2)--(-3,-2)--(-3,0)--cycle,linewidth(1)); } label("$A$",(3,2),NE); label("$B$",(3,-2),SE); label("$C$",(-3,-2),SW); label("$D$",(-3,0),NW); [/asy]
This quadrilateral is a trapezoid, because $AB\parallel CD$ but $BC$ is not parallel to $AD$ . The area of a trapezoid is the product of its height and its median, where the median is the average of the side lengths of the bases. The two bases are $AB$ and $CD$ , which have lengths $2$ and $4$ , respectively, so the length of the median is $\frac{2+4}{2}=3$ . $CB$ is perpendicular to the bases, so it is the height, and has length $6$ . Therefore, the area of the trapezoid is $(3)(6)=18, \boxed{\text{C}}$

## Solution 2
Using the diagram above, the figure can be divided along the x-axis into two familiar regions that do not overlap: a right triangle and a rectangle. Since the areas do not overlap, the area of the entire trapezoid is the sum of the area of the triangle and the area of the rectangle.
$A_{trap} = A_{tri} + A_{rect}$
$A_{trap} = \frac{1}{2}bh + lw$
$A_{trap} = \frac{1}{2}\cdot 6 \cdot 2 + 6\cdot 2$
$A_{trap} = 6 + 12 = 18 \rightarrow \boxed{C}$

## Solution 3
Using the diagram in solution 1 we can use the Pick’s Theorem to solve this problem.There are twelve lattice points inside the quadrilateral and fourteen lattice points on the quadrilateral. Applying the Pick’s Theorem, 12 + $\frac{14}{2}$ - 1 = 18 $\rightarrow \boxed{C}$

## Video Solution
https://youtu.be/5gldUJaZZCg Soo, DRMS, NM
### See Also