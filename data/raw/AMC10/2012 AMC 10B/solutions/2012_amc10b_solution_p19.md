# 2012 AMC 10B Problem 19

## Problem

In rectangle $ABCD$ , $AB=6$ , $AD=30$ , and $G$ is the midpoint of $\overline{AD}$ . Segment $AB$ is extended 2 units beyond $B$ to point $E$ , and $F$ is the intersection of $\overline{ED}$ and $\overline{BC}$ . What is the area of quadrilateral $BFDG$ ?

$\textbf{(A)}\ \frac{133}{2}\qquad\textbf{(B)}\ 67\qquad\textbf{(C)}\ \frac{135}{2}\qquad\textbf{(D)}\ 68\qquad\textbf{(E)}\ \frac{137}{2}$

## Solution
[asy] unitsize(10); pair B=(0,0); pair A=(0,6); pair C=(30,0); pair D=(30,6); pair G=(15,6); pair E=(0,-2); pair F=(15/2,0); dot(A); dot(B); dot(C); dot(D); dot(G); dot(E); dot(F); label("A",(0,6),NW); label("B",(0,0),W); label("C",(30,0),E); label("D",(30,6),NE); label("G",(15,6),N); label("E",(0,-2),SW); label("F",(15/2,0),N); label("15",(A--G),N); label("15",(G--D),N); label("6",(A--B),W); label("2",(B--E),W); label("6",(D--C),E); draw(A--B); draw(B--C); draw(C--D); draw(D--A); draw(E--D); draw(B--E); draw(B--G); [/asy]
Note that the area of $BFDG$ equals the area of $ABCD-\triangle AGB-\triangle DCF$ . Since $AG=\frac{AD}{2}=15,$ $\triangle AGB=\frac{15\times 6}{2}=45$ . Now, $\triangle AED\sim \triangle BEF$ , so $\frac{AE}{BE}=4=\frac{AD}{BF}=\frac{30}{BF}\implies BF=7.5$ and $FC=22.5,$ so $\triangle DCF=\frac{22.5\times6}{2}=\frac{135}{2}.$
Therefore, \begin{align*}BFDG&=ABCD-\triangle AGB-\triangle DCF \\ &=180-45-\frac{135}{2} \\ &=\boxed{\frac{135}{2}}\end{align*} hence our answer is $\fbox{C}$

## Solution 2
Notice that $BFDG$ is a trapezoid with height $6$ , so we need to find $BF$ . $\triangle BFE\sim \triangle ADE$ , so $4\cdot BF = AD$ . Since $AD = 30$ , $BF = \frac{15}{2}$ . The area of $BFDG$ is $6\cdot \frac{15+\frac{15}{2}}{2}=3\cdot \frac{45}{2}=\boxed{\textbf{(C) }\frac{135}{2}}$

## Solution 3 (Coordinate Bash)
Let $D=(0,0)$ . We know these points from the problem statement: $C=(6,0), B=(6,30), A=(0,30), G=(0,15), E=(8,30)$
We can use the Shoelace Formula to find the area of quadrilateral $BFDG$ . We know the coordinates of all of the points in $BFDG$ except $F$ . Since $F$ is the intersection of $\overline{ED}$ and $\overline{BC}$ , we can use a system of equations to solve for the coordinates of $F$ . The line for $\overline{BC}$ is simply $x = 6$ . The line for $\overline{ED}$ passes through the origin so it has a y-intercept of $0$ , and a slope of $\frac{30-0}{8-0}=\frac{30}{8}=\frac{15}{4}$ . Therefore, the line for $\overline{ED}$ is $y=\frac{15}{4} x$ . Substituting $6$ for $x$ , we find that $y = \frac{45}{2}$ . Therefore, $F=(6, \frac{45}{2})$ . Applying Shoelace on these points gives us that $[BFDG] = \boxed{\frac{135}{2}}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .