# 2009 AMC 10B Problem 13

## Problem

As shown below, convex pentagon $ABCDE$ has sides $AB=3$ , $BC=4$ , $CD=6$ , $DE=3$ , and $EA=7$ . The pentagon is originally positioned in the plane with vertex $A$ at the origin and vertex $B$ on the positive $x$ -axis. The pentagon is then rolled clockwise to the right along the $x$ -axis. Which side will touch the point $x=2009$ on the $x$ -axis?

[asy] unitsize(3mm); defaultpen(linewidth(.8pt)+fontsize(8pt)); dotfactor=4; pair A=(0,0), Ep=7*dir(105), B=3*dir(0); pair D=Ep+B; pair C=intersectionpoints(Circle(D,6),Circle(B,4))[1]; pair[] ds={A,B,C,D,Ep}; dot(ds); draw(B--C--D--Ep--A); draw((6,6)..(8,4)..(8,3),EndArrow(3)); xaxis("$x$",-8,14,EndArrow(3)); label("$E$",Ep,NW); label("$D$",D,NE); label("$C$",C,E); label("$B$",B,SE); label("$(0,0)=A$",A,SW); label("$3$",midpoint(A--B),N); label("$4$",midpoint(B--C),NW); label("$6$",midpoint(C--D),NE); label("$3$",midpoint(D--Ep),S); label("$7$",midpoint(Ep--A),W); [/asy]

$\text{(A) } \overline{AB} \qquad \text{(B) } \overline{BC} \qquad \text{(C) } \overline{CD} \qquad \text{(D) } \overline{DE} \qquad \text{(E) } \overline{EA}$

## Solution
The perimeter of the polygon is $3+4+6+3+7 = 23$ . Hence as we roll the polygon to the right, every $23$ units the side $\overline{AB}$ will be the bottom side.
We have $2009 = 23 \times 87 + 8$ . Thus at some point in time we will get the situation when $A=(2001,0)$ and $\overline{AB}$ is the bottom side. Obviously, at this moment $B=(2004,0)$ .
After that, the polygon rotates around $B$ until point $C$ hits the $x$ axis at $(2008,0)$ .
And finally, the polygon rotates around $C$ until point $D$ hits the $x$ axis at $(2014,0)$ . At this point the side $\boxed{\overline{CD}}$ touches the point $(2009,0)$ . So the answer is $\boxed{C}$

## Solution 2: Mod Arithmetic
The perimeter is $23$ and $2009\equiv8($ mod $23)$ , so it will end up on side $AB$ + a total of 8 more units. $4<8$ , but $4+6=10>8$ , so it ends on side $CD$ for an answer of $\boxed{C}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .