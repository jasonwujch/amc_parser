# 2004 AMC 8 Problem 24

## Problem

In the figure, $ABCD$ is a rectangle and $EFGH$ is a parallelogram. Using the measurements given in the figure, what is the length $d$ of the segment that is perpendicular to $\overline{HE}$ and $\overline{FG}$ ?

[asy] unitsize(3mm); defaultpen(linewidth(.8pt)+fontsize(10pt)); pair D=(0,0), C=(10,0), B=(10,8), A=(0,8); pair E=(4,8), F=(10,3), G=(6,0), H=(0,5); draw(A--B--C--D--cycle); draw(E--F--G--H--cycle); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$E$",E,N); label("$F$",(10.8,3)); label("$G$",G,S); label("$H$",H,W); label("$4$",A--E,N); label("$6$",B--E,N); label("$5$",(10.8,5.5)); label("$3$",(10.8,1.5)); label("$4$",G--C,S); label("$6$",G--D,S); label("$5$",D--H,W); label("$3$",A--H,W); draw((3,7.25)--(7.56,1.17)); label("$d$",(3,7.25)--(7.56,1.17), NE); [/asy]

$\textbf{(A)}\ 6.8\qquad \textbf{(B)}\ 7.1\qquad \textbf{(C)}\ 7.6\qquad \textbf{(D)}\ 7.8\qquad \textbf{(E)}\ 8.1$

## Solution
The area of the parallelogram can be found in two ways. The first is by taking rectangle $ABCD$ and subtracting the areas of the triangles cut out to create parallelogram $EFGH$ . This is \[(4+6)(5+3) - 2 \cdot \frac12 \cdot 6 \cdot 5 - 2 \cdot \frac12 \cdot 3 \cdot 4 = 80 - 30 - 12 = 38\] The second way is by multiplying the base of the parallelogram such as $\overline{FG}$ with its altitude $d$ , which is perpendicular to both bases. $\triangle FGC$ is a $3-4-5$ triangle so $\overline{FG} = 5$ . Set these two representations of the area together. \[5d = 38 \rightarrow d = \boxed{\textbf{(C)}\ 7.6}\] :)
~Ak ~Smiley face by Shreyansh Medatati

## Video Solution by Sohil Rathi (Omega Learn)
https://youtu.be/abSgjn4Qs34?t=4
~ pi is 3.14
### See Also