# 2021 Fall AMC 10A Problem 22

## Problem

Inside a right circular cone with base radius $5$ and height $12$ are three congruent spheres with radius $r$ . Each sphere is tangent to the other two spheres and also tangent to the base and side of the cone. What is $r$ ?

$\textbf{(A)}\ \frac{3}{2} \qquad\textbf{(B)}\ \frac{90-40\sqrt{3}}{11} \qquad\textbf{(C)}\ 2 \qquad\textbf{(D)}\ \frac{144-25\sqrt{3}}{44} \qquad\textbf{(E)}\ \frac{5}{2}$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(250); import graph3; import solids; currentprojection=orthographic((0,-6,4)); real r = (90-40sqrt(3))/11; triple A, B, C; A = (2/3*sqrt(3)*r*Cos(90),2/3*sqrt(3)*r*Sin(90),r); B = (2/3*sqrt(3)*r*Cos(210),2/3*sqrt(3)*r*Sin(210),r); C = (2/3*sqrt(3)*r*Cos(330),2/3*sqrt(3)*r*Sin(330),r); draw(scale(5,5,12)*unitcone,yellow,light=White); draw(Circle((0,0,0),5,(0,0,1))); draw(shift(A)*scale3(r)*unitsphere,lightgray,light=White); draw(shift(B)*scale3(r)*unitsphere,lightgray,light=White); draw(shift(C)*scale3(r)*unitsphere,lightgray,light=White); dot(A^^B^^C^^(0,0,0),linewidth(4.5)); [/asy]

~MRENTHUSIASM

## Solution 1 (Cross Sections and Angle Bisectors)
We can take half of a cross section of the sphere, as such: [asy] unitsize(0.5cm); real r = (90-40*sqrt(3))/11; pair C = (0,0); pair A = (-5,0); pair B = (0,12); pair O = (-((2*sqrt(3))/3) * r, r); draw(A--B--C--cycle); draw(circle(O,r)); pair D = (-(2*sqrt(3))/3 * r - (12/13)*r, (18/13)*r); pair E = (-2.2, 0); draw(O--E); draw(D--O); label("$A$", A, SW); label("$B$", B, N); label("$C$", C, SE); label("$O$", O, (1,0)); label("$D$", D, NW); label("$E$", E, S); dot(D); dot(E); dot(O); [/asy] Notice that we chose a cross section where one of the spheres was tangent to the lateral surface of the cone at $D$ .
To evaluate $r$ , we will find $AE$ and $EC$ in terms of $r$ ; we also know that $AE+EC = 5$ , so with this, we can solve $r$ . Firstly, to find $EC$ , we can take a bird's eye view of the cone: [asy] unitsize(0.8cm); pair C = (0,0); draw(circle(C,5)); label("$C$", C, N); dot(C); real r = (90-40*sqrt(3))/11; real raise = r*(2/3*sqrt(3)); pair E = (-r,raise/-2); pair X = (0,raise); pair Y = (r,raise/-2); label("$E$", E, SW); dot(E); label("$X$", X, N); dot(X); label("$Y$", Y, SE); dot(Y); draw(circle(X,r),dashed); draw(circle(E,r),dashed); draw(circle(Y,r),dashed); draw(E--X,dashed); draw(X--Y,dashed); draw(E--Y,dashed); [/asy] Note that $C$ is the centroid of equilateral triangle $EXY$ . Also, since all of the medians of an equilateral triangle are also altitudes, we want to find two-thirds of the altitude from $E$ to $XY$ ; this is because medians cut each other into a $2$ to $1$ ratio. This equilateral triangle has a side length of $2r$ , therefore it has an altitude of length $r \sqrt{3}$ ; two thirds of this is $\frac{2r \sqrt{3}}{3}$ , so $EC = \frac{2r \sqrt{3}}{3}.$ [asy] unitsize(0.5cm); real r = (90-40*sqrt(3))/11; pair C = (0,0); pair A = (-5,0); pair B = (0,12); pair O = (-((2*sqrt(3))/3) * r, r); draw(A--B--C--cycle); draw(circle(O,r)); pair D = (-(2*sqrt(3))/3 * r - (12/13)*r, (18/13)*r); pair E = (-2.2, 0); pair F = (-2.2, 6.72); draw(E--F); draw(D--O); draw(A--O, dashed); label("$A$", A, SW); label("$B$", B, N); label("$C$", C, SE); label("$O$", O, (1,0)); label("$D$", D, NW); label("$E$", E, S); label("$F$", F, NW); dot(D); dot(E); dot(O); [/asy] To evaluate $AE$ in terms of $r$ , we will extend $\overline{OE}$ past point $O$ to $\overline{AB}$ at point $F$ . $\triangle AEF$ is similar to $\triangle ACB$ . Also, $AO$ is the angle bisector of $\angle EAB$ . Therefore, by the angle bisector theorem, $\frac{OE}{OF} = \frac{AE}{AF} = \frac{5}{13}$ . Also, $OE = r$ , so $\frac{r}{OF} = \frac{5}{13}$ , so $OF = \frac{13r}{5}$ . This means that \[AE = \frac{5 \cdot EF}{12} = \frac{5 \cdot (OE + OF)}{12} = \frac{5 \cdot (r + \frac{13r}{5})}{12} = \frac{18r}{12} = \frac{3r}{2}.\] We have that $EC = \frac{2r \sqrt{3}}{3}$ and that $AE = \frac{3r}{2}$ , so $AC = EC + AE = \frac{2r \sqrt{3}}{3} + \frac{3r}{2} = \frac{4r \sqrt{3} + 9r}{6}$ . We also were given that $AC = 5$ . Therefore, we have \[\frac{4r \sqrt{3} + 9r}{6} = 5.\] This is a simple linear equation in terms of $r$ . We can solve for $r$ to get $r = \boxed{\textbf{(B)}\ \frac{90-40\sqrt{3}}{11}}.$
~ihatemath123

## Solution 2 (Cross Sections and Areas)
Denote by $O_1$ , $O_2$ , $O_3$ the centers of three spheres.
Because three congruent spheres are tangent to the base of the cone, the plane formed by $O_1$ , $O_2$ , $O_3$ (denoted as $\alpha$ ) is parallel to the base, with the distance $r$ .
Let $D$ be the point that the sphere with center $O_1$ meets the base of the cone at. Hence, $O_1 D = r$ .
Because three congruent spheres are mutually externally tangent to each other, $\triangle O_1 O_2 O_3$ is equilateral, with side length $2 r$ .
Let $O$ be the center of the base, $V$ be the vertex of the cone. Let line $OV$ and plane $\alpha$ intersect at point $E$ . By symmetry, $E$ is the center $\triangle O_1 O_2 O_3$ . Hence, $O_1 E = \frac{\sqrt{3}}{3} O_1 O_2 = \frac{2 \sqrt{3}}{3} r$ .
Let $F$ be the point that the sphere with center $O_1$ meets the side of the cone at. Hence, $O_1 F = r$ .
Let line $VF$ and the base intersect at point $A$ .
Hence, we only need to analyze the following 2-d geometry problem: In $\triangle VOA$ with $\angle O = 90^\circ$ , $VO = 12$ , $OA = 5$ , there is an interior point $O_1$ whose distances to $OA$ , $OV$ , $VA$ , are $r$ , $\frac{2 \sqrt{3}}{3} r$ , and $r$ , respectively. What is $r$ ?
Now, we solve this problem.
We compute the area of $\triangle VOA$ in two ways.
First, we have \begin{align*} {\rm Area} \ \triangle VOA & = \frac{1}{2} OA \cdot OV = 30 . \end{align*}
Second, we have \begin{align*} {\rm Area} \ \triangle VOA & = {\rm Area} \ \triangle O_1 OA + {\rm Area} \ \triangle O_1 OV + {\rm Area} \ \triangle O_1 VA \\ & = \frac{1}{2} \cdot OA \cdot O_1 D + \frac{1}{2} \cdot OV \cdot O_1 E + \frac{1}{2} \cdot VA \cdot O_1 F \\ & = \frac{1}{2} \cdot 5 \cdot r + \frac{1}{2}\cdot 12 \cdot\frac{2 \sqrt{3}}{3}\cdot r + \frac{1}{2} \cdot 13 \cdot r \\ & = \left( 9 + 4 \sqrt{3} \right) r . \end{align*}
These two approaches to compute ${\rm Area} \ \triangle VOA$ should give me the same number. Hence, \[r = \frac{30}{9 + 4 \sqrt{3}} = \boxed{\textbf{(B)}\ \frac{90-40\sqrt{3}}{11}}.\]
~Steven Chen (www.professorchenedu.com)

## Solution 3 (Coordinate Geometry)
We will use coordinates. WLOG, let the coordinates of the center of the base of the cone be the origin. Then, let the center of one of the spheres be $\left(0, \frac{2r}{\sqrt{3}}, r\right)$ . Note that the distance between this point and the plane given by $12y+5z=60$ is $r$ . Thus, by the point-to-plane distance formula, we have \[\frac{\left|12 \cdot \frac{2r}{\sqrt{3}} + 5r - 60\right|}{\sqrt{0^2+5^2+12^2}}=r.\] Solving for $r$ yields $r = \boxed{\textbf{(B)}\ \frac{90-40\sqrt{3}}{11}}$ .
~ Leo.Euler

## Solution 4 (Very Cheesy and Risky)
Clearly the answer must have square roots, leaving $\textbf{(B)}$ and $\textbf{(D)}.$ D has a lot of perfect squares, so we suspect it is a trap. This leads us to choose $\textbf{(B)}$ .
~ YOUSmomentumSAG

## Video Solution by TheBeautyofMath
https://youtu.be/g48WbqgilZs
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .