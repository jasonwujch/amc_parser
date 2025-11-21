# 2009 AIME II Problem 5

## Problem

Equilateral triangle $T$ is inscribed in circle $A$ , which has radius $10$ . Circle $B$ with radius $3$ is internally tangent to circle $A$ at one vertex of $T$ . Circles $C$ and $D$ , both with radius $2$ , are internally tangent to circle $A$ at the other two vertices of $T$ . Circles $B$ , $C$ , and $D$ are all externally tangent to circle $E$ , which has radius $\dfrac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

[asy] unitsize(3mm); defaultpen(linewidth(.8pt)); dotfactor=4; pair A=(0,0), D=8*dir(330), C=8*dir(210), B=7*dir(90); pair Ep=(0,4-27/5); pair[] dotted={A,B,C,D,Ep}; draw(Circle(A,10)); draw(Circle(B,3)); draw(Circle(C,2)); draw(Circle(D,2)); draw(Circle(Ep,27/5)); dot(dotted); label("$E$",Ep,E); label("$A$",A,W); label("$B$",B,W); label("$C$",C,W); label("$D$",D,E); [/asy]

## Solution 1
Let $X$ be the intersection of the circles with centers $B$ and $E$ , and $Y$ be the intersection of the circles with centers $C$ and $E$ . Since the radius of $B$ is $3$ , $AX =4$ . Assume $AE$ = $p$ . Then $EX$ and $EY$ are radii of circle $E$ and have length $4+p$ . $AC = 8$ , and angle $CAE = 60$ degrees because we are given that triangle $T$ is equilateral. Using the Law of Cosines on triangle $CAE$ , we obtain
$(6+p)^2 =p^2 + 64 - 2(8)(p) \cos 60$ .
The $2$ and the $\cos 60$ terms cancel out:
$p^2 + 12p +36 = p^2 + 64 - 8p$
$12p+ 36 = 64 - 8p$
$p =\frac {28}{20} = \frac {7}{5}$ . The radius of circle $E$ is $4 + \frac {7}{5} = \frac {27}{5}$ , so the answer is $27 + 5 = \boxed{032}$ .

## Solution 2 (NO TRIGONOMETRY!!!)
Draw $\overline{CD}$ from circle center $C$ to center $D$ . Let its midpoint be point $F$ .
Draw $\overline{BF}$ perpendicular to line segment $CD$ and intersecting $CD$ at point $F$ .
Let $G$ be the common external tangent point of circle $B$ and circle $E$ . $\overline{GA} = 4$
Circle centers $A$ and $E$ lie on $\overline{BF}$ .
Draw $\overline{AC}$ from circle center $A$ to center $C$ . $\overline{AC}$ has length $8$ .
Triangle $ACF$ is a right triangle with $\angle ACF = 30^{\circ}$ .
(If you take the original equilateral triangle with centroid A and draw the medians, dividing the triangle into 6 30 degree triangles, you find that triangle $ACF$ is similar to one of the triangles).
$\overline{AF} = 4$ and $\overline{CF} = 4\sqrt{3}$ .
Let the radius of circle $E$ have length $r$ . Draw $\overline{EC}$ from circle center $E$ to center $C$ .
$\overline{EC}$ has length $r + 2$ . $\overline{EF}$ has length $GA + AF - GE = 8 - r$ .
Since $CEF$ is a right triangle, by the Pythagorean theorem $EF^2 + CF^2 = EC^2$ .
$(8 - r)^2 + (4\sqrt{3})^2 = (r + 2)^2$ . Solving, $r = \frac {27}{5}$ and the answer is $27 + 5 = \boxed{032}$ .
-unhappyfarmer

## Video Solution
https://youtu.be/fZAChuJDlSw?si=wJUPmgVRlYwazauh
### See Also
These problems are copyrighted © by the Mathematical Association of America.