# 2009 AMC 10B Problem 9

## Problem

Segment $BD$ and $AE$ intersect at $C$ , as shown, $AB=BC=CD=CE$ , and $\angle A = \frac 52 \angle B$ . What is the degree measure of $\angle D$ ?

[asy] unitsize(2cm); defaultpen(linewidth(.8pt)+fontsize(8pt)); dotfactor=4; pair C=(0,0), Ep=dir(35), D=dir(-35), B=dir(145); pair A=intersectionpoints(Circle(B,1),C--(-1*Ep))[0]; pair[] ds={A,B,C,D,Ep}; dot(ds); draw(A--Ep--D--B--cycle); label("$A$",A,SW); label("$B$",B,NW); label("$C$",C,N); label("$E$",Ep,E); label("$D$",D,E); [/asy]

$\text{(A) } 52.5 \qquad \text{(B) } 55 \qquad \text{(C) } 57.7 \qquad \text{(D) } 60 \qquad \text{(E) } 62.5$

## Solution
$\triangle ABC$ is isosceles, hence $\angle ACB = \angle CAB$ .
The sum of internal angles of $\triangle ABC$ can now be expressed as $\angle B + \frac 52 \angle B + \frac 52 \angle B = 6\angle B$ , hence $\angle B = 30^\circ$ , and each of the other two angles is $75^\circ$ .
Now we know that $\angle DCE = \angle ACB = 75^\circ$ .
Finally, $\triangle CDE$ is isosceles, hence each of the two remaining angles ( $\angle D$ and $\angle E$ ) is equal to $\frac{180^\circ - 75^\circ}2 = \frac{105^\circ}2 = \boxed{52.5}$ .

## Video Solution
https://youtu.be/hsP804ZSocg
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .