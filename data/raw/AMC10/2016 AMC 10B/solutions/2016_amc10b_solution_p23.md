# 2016 AMC 10B Problem 23

## Problem

In regular hexagon $ABCDEF$ , points $W$ , $X$ , $Y$ , and $Z$ are chosen on sides $\overline{BC}$ , $\overline{CD}$ , $\overline{EF}$ , and $\overline{FA}$ respectively, so lines $AB$ , $ZW$ , $YX$ , and $ED$ are parallel and equally spaced. What is the ratio of the area of hexagon $WCXYFZ$ to the area of hexagon $ABCDEF$ ?

$\textbf{(A)}\ \frac{1}{3}\qquad\textbf{(B)}\ \frac{10}{27}\qquad\textbf{(C)}\ \frac{11}{27}\qquad\textbf{(D)}\ \frac{4}{9}\qquad\textbf{(E)}\ \frac{13}{27}$

## Solution 1
We draw a diagram to make our work easier: [asy] pair A,B,C,D,E,F,W,X,Y,Z; A=(0,0); B=(1,0); C=(3/2,sqrt(3)/2); D=(1,sqrt(3)); E=(0,sqrt(3)); F=(-1/2,sqrt(3)/2); X=(4/3,2sqrt(3)/3); W=(4/3,sqrt(3)/3); Z=(-1/3,sqrt(3)/3); Y=(-1/3,2sqrt(3)/3); draw(A--B--C--D--E--F--cycle); draw(W--Z); draw(X--Y); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,ESE); label("$D$",D,NE); label("$E$",E,NW); label("$F$",F,WSW); label("$W$",W,ENE); label("$X$",X,ESE); label("$Y$",Y,WSW); label("$Z$",Z,WNW); [/asy]
Assume that $AB$ is of length $1$ . Therefore, the area of $ABCDEF$ is $\frac{3\sqrt 3}2$ . To find the area of $WCXYFZ$ , we draw $\overline{CF}$ , and find the area of the trapezoids $WCFZ$ and $CXYF$ .
[asy] pair A,B,C,D,E,F,W,X,Y,Z; A=(0,0); B=(1,0); C=(3/2,sqrt(3)/2); D=(1,sqrt(3)); E=(0,sqrt(3)); F=(-1/2,sqrt(3)/2); W=(4/3,2sqrt(3)/3); X=(4/3,sqrt(3)/3); Y=(-1/3,sqrt(3)/3); Z=(-1/3,2sqrt(3)/3); draw(A--B--C--D--E--F--cycle); draw(W--Z); draw(X--Y); draw(F--C--B--E--D--A); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,ESE); label("$D$",D,NE); label("$E$",E,NW); label("$F$",F,WSW); label("$W$",W,ENE); label("$X$",X,ESE); label("$Y$",Y,WSW); label("$Z$",Z,WNW); [/asy]
From this, we know that $CF=2$ . We also know that the combined heights of the trapezoids is $\frac{\sqrt 3}3$ , since $\overline{ZW}$ and $\overline{YX}$ are equally spaced, and the height of each of the trapezoids is $\frac{\sqrt 3}6$ . From this, we know $\overline{ZW}$ and $\overline{YX}$ are each $\frac 13$ of the way from $\overline{CF}$ to $\overline{DE}$ and $\overline{AB}$ , respectively. We know that these are both equal to $\frac 53$ .
We find the area of each of the trapezoids, which both happen to be $\frac{11}6 \cdot \frac{\sqrt 3}6=\frac{11\sqrt 3}{36}$ , and the combined area is $\frac{11\sqrt 3}{18}$ .
We find that $\dfrac{\frac{11\sqrt 3}{18}}{\frac{3\sqrt 3}2}$ is equal to $\frac{22}{54}=\boxed{\textbf{(C)}\ \frac{11}{27}}$ .

## Solution 2
[asy] pair A,B,C,D,E,F,W,X,Y,Z; A=(0,0); B=(1,0); C=(3/2,sqrt(3)/2); D=(1,sqrt(3)); E=(0,sqrt(3)); F=(-1/2,sqrt(3)/2); W=(4/3,2sqrt(3)/3); X=(4/3,sqrt(3)/3); Y=(-1/3,sqrt(3)/3); Z=(-1/3,2sqrt(3)/3); draw(A--B--C--D--E--F--cycle); draw(W--Z); draw(X--Y); draw(F--C--B--E--D--A); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,ESE); label("$D$",D,NE); label("$E$",E,NW); label("$F$",F,WSW); label("$W$",W,ENE); label("$X$",X,ESE); label("$Y$",Y,WSW); label("$Z$",Z,WNW); [/asy]
First, like in the first solution, split the large hexagon into 6 equilateral triangles. Each equilateral triangle can be split into three rows of smaller equilateral triangles. The first row will have one triangle, the second three, the third five. Once you have drawn these lines, it's just a matter of counting triangles. There are $22$ small triangles in hexagon $ZWCXYF$ , and $9 \cdot 6 = 54$ small triangles in the whole hexagon.
Thus, the answer is $\frac{22}{54}=\boxed{\textbf{(C)}\ \frac{11}{27}}$ .

## Solution 3 (Similar Triangles)
[asy] pair A,B,C,D,E,F,W,X,Y,Z; A=(0,0); B=(1,0); C=(3/2,sqrt(3)/2); D=(1,sqrt(3)); E=(0,sqrt(3)); F=(-1/2,sqrt(3)/2); W=(4/3,2sqrt(3)/3); X=(4/3,sqrt(3)/3); Y=(-1/3,sqrt(3)/3); Z=(-1/3,2sqrt(3)/3); pair G = (0.5, sqrt(3)*3/2); draw(A--B--C--D--E--F--cycle); draw(W--Z); draw(X--Y); draw(E--G--D); draw(F--C); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,ESE); label("$D$",D,NE); label("$E$",E,NW); label("$F$",F,WSW); label("$W$",W,ENE); label("$X$",X,ESE); label("$Y$",Y,WSW); label("$Z$",Z,WNW); label("$G$",G,N); [/asy] Extend $\overline{EF}$ and $\overline{CD}$ to meet at point $G$ , as shown in the diagram. Then $\triangle GZW \sim \triangle GFC$ . Then $[GZW] = \left(\dfrac53\right)^2[GED]$ and $[GFC] = 2^2[GED]$ . Subtracting $[GED]$ , we find that $[EDWZ] = \dfrac{16}{9}[GED]$ and $[EDCF] = 3[GED]$ . Subtracting again, we find that \[[ZWCF] = [EDCF] - [EDWZ] = \dfrac{11}{9}[GED].\] Finally, \[\dfrac{[WCXYFZ]}{[ABCDEF]} = \dfrac{[ZWCF]}{[EDCF]} = \dfrac{\dfrac{11}{9}[GED]}{3[GED]} = \textbf{(C) } \dfrac{11}{27}.\]

## Solution 4 (Extending Lines)
Refer to the diagram from Solution 1.
Let us start by connecting points $F$ to $C$ to create a new line segment $FC$ . We drop a perpendicular line segment from $E$ to side $FC$ at point $P$ . Since $\angle FED = 120$ , and $\angle PED = 90$ , we know that $\angle FEP = 30.$
Therefore, $\triangle EFP$ is a 30-60-90 triangle. Assume that $EP = \sqrt{3}$ . Therefore, we know that $FP = 1$ , $EF = 2$ .
Let us draw $PQ$ such that $PQ$ is perpendicular to $ZW$ . Since the distance between the parallel lines are equal, we know that $PQ$ is half of the distance between the parallel lines. Hence, $PQ$ will be one-third the length of $EP$ .
From this, we also know that $EQ = EP - PQ = EP - \frac{1}{3} EP = \frac{2}{3} EP$ .
Hence, we know that $EQ = \frac{2}{3} EP = \frac{2\sqrt{3}}{3}.$ Since $\angle EQZ = 90, FEP = 30$ we know that $\triangle ZEQ$ is also a 30-60-90 triangle. From this, we know that $ZQ = \frac{2}{3}$ .
Let us drop another perpendicular line segment from $D$ to point $T$ such that $DT$ is perpendicular to $ZW$ .
Since $ED = QT$ and since $ED$ is the side length of the regular hexagon, we know that $ED = EF = QT = 2.$
By symmetry, we also know that $WT = \frac{2}{3}$ .
Therefore, we can find the length of $ZW = ZQ + QT + QW = \frac{2}{3} + 2 + \frac{2}{3}$ . Hence, we know that $ZW = \frac{10}{3}.$
Now, we can find the area of trapezoid $EDZW = \frac{ED + ZW}{2} \cdot EQ = \frac{2 + \frac{10}{3}}{2} \cdot \frac{2\sqrt{3}}{3} = \frac{16\sqrt{3}}{9}.$
By symmetry, we know that the area of trapezoid $YZAB = \frac{16\sqrt{3}}{9}.$
Using the area of a hexagon formula, we get that the area of regular hexagon $ABCDEF = \frac{3\sqrt{3}}{2} \cdot 2^2 = 6\sqrt{3}.$
Hence, the area of hexagon $WCXYFZ = 6\sqrt{3} - 2\left(\frac{16\sqrt{3}}{9}\right) = \frac{22\sqrt{3}}{9}.$
Hence, the ratio of the area of hexagon $WCXYFZ$ to the area of hexagon $ABCDEF$ is $\dfrac{\frac{22\sqrt{3}}{9}}{6\sqrt{3}} = \boxed{\frac{11}{27} \implies C}.$
~yk2007 :D

## Solution 5
We will do this by area subtraction. Drawing in the required lines, we drop an altitude from A to WZ and an altitude from E to XY. You get 2 30-60-90 triangles, and given that the side length is $x$ , AZ is $2x/3$ , which means that WZ is $5x/3$ , adding in AB. Using the 30-60-90 triangle again, you get that the area of trapezoid $ABWZ$ is $\frac{4x}{3} \cdot$ $\frac{x\sqrt3}{3}$ . Repeat on the other side to get that the area of both of these trapezoids combined are $\frac{8x^2\sqrt3}{9}$ . Finding the area of the hexagon, dividing, and subtracting, gets you C.
-dragoon (LATEX help)

## Video Solution by Pi Academy
https://youtu.be/N2eca474ljo?si=PLw0R0-KGp1zAnuQ
~ Pi Academy

## Video Solution by OmegaLearn
https://youtu.be/GrCtzL0S-Uo?t=638
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .