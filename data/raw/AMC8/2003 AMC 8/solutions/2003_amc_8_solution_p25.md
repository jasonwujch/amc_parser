# 2003 AMC 8 Problem 25

## Problem

In the figure, the area of square $WXYZ$ is $25 \text{ cm}^2$ . The four smaller squares have sides 1 cm long, either parallel to or coinciding with the sides of the large square. In $\triangle ABC$ , $AB = AC$ , and when $\triangle ABC$ is folded over side $\overline{BC}$ , point $A$ coincides with $O$ , the center of square $WXYZ$ . What is the area of $\triangle ABC$ , in square centimeters?

[asy] defaultpen(fontsize(8)); size(225); pair Z=origin, W=(0,10), X=(10,10), Y=(10,0), O=(5,5), B=(-4,8), C=(-4,2), A=(-13,5); draw((-4,0)--Y--X--(-4,10)--cycle); draw((0,-2)--(0,12)--(-2,12)--(-2,8)--B--A--C--(-2,2)--(-2,-2)--cycle); dot(O); label("$A$", A, NW); label("$O$", O, NE); label("$B$", B, SW); label("$C$", C, NW); label("$W$",W , NE); label("$X$", X, N); label("$Y$", Y, S); label("$Z$", Z, SE); [/asy]

$\textbf{(A)}\ \frac{15}4\qquad\textbf{(B)}\ \frac{21}4\qquad\textbf{(C)}\ \frac{27}4\qquad\textbf{(D)}\ \frac{21}2\qquad\textbf{(E)}\ \frac{27}2$

## Solution
We see that $XY = 5$ , the vertical distance between $B$ and $X$ is $1$ , and the vertical distance between $C$ and $Y$ is $1$ . Therefore, $BC = 5 - 1 - 1 = 3$ . We are given that the length of the altitude of $\triangle ABC$ is equal to the distance between $\overline{BC}$ and $O$ , which is $1 + 1 + \frac{5}{2} = \frac{9}{2}$ . So the area of $\triangle ABC$ is $\frac{1}{2}\left(3\cdot \frac{9}{2}\right)$ , which is $\boxed{\textbf{(C)} \ \frac{27}{4}}$ .
~sidkris

## Video Solution
https://www.youtube.com/watch?v=4RBCH1rUcSw
~David
### See Also