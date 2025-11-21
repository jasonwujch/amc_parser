# 2002 AMC 10B Problem 17

## Problem

A regular octagon $ABCDEFGH$ has sides of length two. Find the area of $\triangle ADG$ .

$\textbf{(A) } 4 + 2\sqrt2 \qquad \textbf{(B) } 6 + \sqrt2\qquad \textbf{(C) } 4 + 3\sqrt2 \qquad \textbf{(D) } 3 + 4\sqrt2 \qquad \textbf{(E) } 8 + \sqrt2$

## Solution
[asy] unitsize(1cm); defaultpen(0.8); pair[] A = new pair[8]; A[0]=(0,0); for (int i=1; i<8; ++i) A[i] = A[i-1] + 2*dir(45*(i-1)); draw( A[0]--A[1]--A[2]--A[3]--A[4]--A[5]--A[6]--A[7]--cycle ); label("$A$",A[0],SW); label("$B$",A[1],SE); label("$C$",A[2],SE); label("$D$",A[3],NE); label("$E$",A[4],NE); label("$F$",A[5],NW); label("$G$",A[6],NW); label("$H$",A[7],SW); filldraw( A[0]--A[3]--A[6]--cycle, lightgray, black ); pair P = intersectionpoint( A[3]--A[6], A[0]--A[5] ); draw( A[0]--P ); draw( P -- A[5], dashed ); label("$P$",P,NE); draw( A[1]--A[4], dashed ); pair Q = intersectionpoint( A[3]--A[6], A[1]--A[4] ); label("$Q$",Q,NW); [/asy]
The area of the triangle $ADG$ can be computed as $\frac{DG \cdot AP}2$ . We will now find $DG$ and $AP$ .
Clearly, $PFG$ is a right isosceles triangle with hypotenuse of length $2$ , hence $PG=\sqrt 2$ . The same holds for triangle $QED$ and its leg $QD$ . The length of $PQ$ is equal to $FE=2$ . Hence $GD = 2 + 2\sqrt 2$ , and $AP = PD = 2 + \sqrt 2$ .
Then the area of $ADG$ equals $\frac{DG \cdot AP}2 = \frac{(2+2\sqrt 2)(2+\sqrt 2)}2 = \frac{8+6\sqrt 2}2 = \boxed{\textbf{(C)}=4+3\sqrt 2}$ .

## Solution 2 (a bit of trig)
(Refer to diagram above)
Notice how the area of triangle is equivalent to the area of the octagon minus $2A_{ABCD}$ and then minus $A_{\triangle AHG}$ .
THe trapezoid $ABCD$ is an isosceles trapezoid. It can be broken apart into a rectangle, and two right triangles. These triangles are isosceles, as $\angle GFP = \angle GFE - \angle PFE = 135^{\circ} - 90^{\circ} = 45^{\circ}$ .
$\sin(45^{\circ}) = \frac{\sqrt{2}}{2}$ , so the legs of the isosceles right triangles are $\sqrt{2}$ . The area of the trapezoid can be calculated as followed:
$A_{PQEF} + 2A_{GFP} = 2 \cdot \sqrt{2} + 2 \cdot \sqrt{2}^2 \div 2 = 2\sqrt{2}+2$ .
The area formula for a triangle is $\frac{1}{2}ab\sin(C)$ , where $C$ is the included angle between sides $a$ and $b$ . Using this for triangle $AHG$ , we get $\frac{1}{2} \cdot 4 \cdot \sin(135)$ . $\sin(135) = \sin(90+45) = \sin(90)\cos(45) + \cos(90)\sin(45) = 1 \cdot \frac{\sqrt{2}}{2} + 0 \cdot \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{2}$ . Therefore, the area of triangle $AHG$ is $\sqrt{2}$ .
The total area between two times the trapezoid $ABCD$ and triangle $AHG$ is $5\sqrt{2}+4$ . The area of the octagon is $2(1+\sqrt{2}) \cdot 2^2 = 8 + 8\sqrt{2}$ . Subtracting the areas, we get $4+3\sqrt{2}$ , or $\boxed{\text{C}}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .