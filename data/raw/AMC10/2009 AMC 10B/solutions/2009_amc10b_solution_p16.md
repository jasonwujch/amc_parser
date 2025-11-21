# 2009 AMC 10B Problem 16

## Problem

Points $A$ and $C$ lie on a circle centered at $O$ , each of $\overline{BA}$ and $\overline{BC}$ are tangent to the circle, and $\triangle ABC$ is equilateral. The circle intersects $\overline{BO}$ at $D$ . What is $\frac{BD}{BO}$ ?

$\text{(A) } \frac {\sqrt2}{3} \qquad \text{(B) } \frac {1}{2} \qquad \text{(C) } \frac {\sqrt3}{3} \qquad \text{(D) } \frac {\sqrt2}{2} \qquad \text{(E) } \frac {\sqrt3}{2}$

## Solution

## Solution 1
[asy] unitsize(1.5cm); defaultpen(0.8); pair B=(0,0), A=(3,0), C=3*dir(60), O=intersectionpoint( C -- (C+3*dir(-30)), A -- (A+3*dir(90)) ); pair D=intersectionpoint(B--O, circle(O,length(A-O))); draw(circle(O,length(A-O))); draw(A--B--C--O--A); draw(B--O); draw(rightanglemark(B,A,O)); draw(rightanglemark(B,C,O)); draw(A--C, dashed ); label("$B$",B,SW); label("$A$",A,S); label("$C$",C,NW); label("$O$",O,NE); label("$D$",D,(S+SSW)); [/asy]
As $\triangle ABC$ is equilateral, we have $\angle BAC = \angle BCA = 60^\circ$ , hence $\angle OAC = \angle OCA = 30^\circ$ . Then $\angle AOC = 120^\circ$ , and from symmetry we have $\angle AOB = \angle COB = 60^\circ$ . Thus, this gives us $\angle ABO = \angle CBO = 30^\circ$ .
We know that $DO = AO$ , as $D$ lies on the circle. From $\triangle ABO$ we also have $AO = BO \sin 30^\circ = \frac{BO}2$ , Hence $DO = \frac{BO}2$ , therefore $BD = BO - DO = \frac{BO}2$ , and $\frac{BD}{BO} = \boxed{\frac 12 \Longrightarrow B}$ .

## Solution 2
[asy] unitsize(1.5cm); defaultpen(0.8); pair B=(0,0), A=(3,0), C=3*dir(60), O=intersectionpoint( C -- (C+3*dir(-30)), A -- (A+3*dir(90)) ); pair D=intersectionpoint(B--O, circle(O,length(A-O))); draw(circle(O,length(A-O))); draw(A--B--C--O--A); draw(B--O); draw(rightanglemark(B,A,O)); draw(rightanglemark(B,C,O)); draw(A--C--D--A, dashed ); pair Sp = intersectionpoint(D--O,A--C); label("$B$",B,SW); label("$A$",A,S); label("$C$",C,NW); label("$O$",O,NE); label("$D$",D,(S+SSW)); label("$S$",Sp,(S+SSW)); [/asy]
As in the previous solution, we find out that $\angle AOB = \angle COB = 60^\circ$ . Hence $\triangle AOD$ and $\triangle COD$ are both equilateral.
We then have $\angle SCD = \angle SAD = 30^\circ$ , hence $D$ is the incenter of $\triangle ABC$ , and as $\triangle ABC$ is equilateral, $D$ is also its centroid. Hence $2 \cdot SD = BD$ , and as $SD = SO$ , we have $2\cdot SD = SD + SO = OD$ , therefore $BD=OD$ , and as before we conclude that $\frac{BD}{BO} = \boxed{\frac 12}$ .

## Solution 3
$\triangle BAO\cong\triangle BCO$ by SSS congruence, so $\angle ABO = \angle CBO = \frac{60}{2} = 30 ^\circ$ . Since $BA$ is tangent to the circle, it is perpendicular to $AO$ . This means that $\triangle BAO$ is a 30-60-90 triangle. The ratio of the side-lengths of a 30-60-90 triangle is $1:\sqrt3:2$ , so $BO=2$ . $BD = BO-DO$ . Since $DO$ is the radius of the circle, $DO=1$ and $BD = 2-1=1$ . Hence, $\frac{BD}{BO} = \frac{1}{2}$ , and the answer is $\boxed{\textbf{(B) } \frac{1}{2}}$ ~azc1027
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .