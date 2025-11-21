# 2016 AIME II Problem 7

## Problem

Squares $ABCD$ and $EFGH$ have a common center and $\overline{AB} || \overline{EF}$ . The area of $ABCD$ is 2016, and the area of $EFGH$ is a smaller positive integer. Square $IJKL$ is constructed so that each of its vertices lies on a side of $ABCD$ and each vertex of $EFGH$ lies on a side of $IJKL$ . Find the difference between the largest and smallest positive integer values for the area of $IJKL$ .

## Solution
Letting $AI=a$ and $IB=b$ , we have \[IJ^{2}=a^{2}+b^{2} \geq 1008\] by AM-GM inequality . Also, since $EFGH||ABCD$ , the angles that each square cuts another are equal, so all the triangles are formed by a vertex of a larger square and $2$ adjacent vertices of a smaller square are similar. Therefore, the areas form a geometric progression, so since \[2016=12^{2} \cdot 14\] we have the maximum area is \[2016 \cdot \dfrac{11}{12} = 1848\] (the areas of the squares from largest to smallest are $12^{2} \cdot 14, 11 \cdot 12 \cdot 14, 11^{2} \cdot 14$ forming a geometric progression).
The minimum area is $1008$ (every square is half the area of the square whose sides its vertices touch), so the desired answer is \[1848-1008=\boxed{840}\]
[asy] pair A,B,C,D,E,F,G,H,I,J,K,L; A=(0,0); B=(2016,0); C=(2016,2016); D=(0,2016); I=(1008,0); J=(2016,1008); K=(1008,2016); L=(0,1008); E=(504,504); F=(1512,504); G=(1512,1512); H=(504,1512); draw(A--B--C--D--A); draw(I--J--K--L--I); draw(E--F--G--H--E); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,NE); label("$D$",D,NW); label("$E$",E,SW); label("$F$",F,SE); label("$G$",G,NE); label("$H$",H,NW); label("$I$",I,S); label("$J$",J,NE); label("$K$",K,N); label("$L$",L,NW); [/asy]
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .