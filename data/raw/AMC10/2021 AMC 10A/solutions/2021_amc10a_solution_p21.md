# 2021 AMC 10A Problem 21

## Problem

Let $ABCDEF$ be an equiangular hexagon. The lines $AB, CD,$ and $EF$ determine a triangle with area $192\sqrt{3}$ , and the lines $BC, DE,$ and $FA$ determine a triangle with area $324\sqrt{3}$ . The perimeter of hexagon $ABCDEF$ can be expressed as $m +n\sqrt{p}$ , where $m, n,$ and $p$ are positive integers and $p$ is not divisible by the square of any prime. What is $m + n + p$ ?

$\textbf{(A)} ~47\qquad\textbf{(B)} ~52\qquad\textbf{(C)} ~55\qquad\textbf{(D)} ~58\qquad\textbf{(E)} ~63$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(250); path P1, P2; P1 = scale(16sqrt(3))*polygon(3); P2 = shift(3,3)*scale(36)*rotate(180)*polygon(3); draw(P1, dashed+black); draw(P2, dashed+black); pair A, B, C, D, E, F; E = intersectionpoints(P1,P2)[0]; F = intersectionpoints(P1,P2)[1]; A = intersectionpoints(P1,P2)[2]; B = intersectionpoints(P1,P2)[3]; C = intersectionpoints(P1,P2)[4]; D = intersectionpoints(P1,P2)[5]; filldraw(A--B--C--D--E--F--cycle,yellow); dot("$E$",E,1.5*dir(0),linewidth(4)); dot("$F$",F,1.5*dir(60),linewidth(4)); dot("$A$",A,1.5*dir(120),linewidth(4)); dot("$B$",B,1.5*dir(180),linewidth(4)); dot("$C$",C,1.5*dir(-120),linewidth(4)); dot("$D$",D,1.5*dir(-60),linewidth(4)); dot(16sqrt(3)*dir(90)^^16sqrt(3)*dir(210)^^16sqrt(3)*dir(330),linewidth(4)); dot((3,3)+36*dir(30)^^(3,3)+36*dir(150)^^(3,3)+36*dir(270),linewidth(4)); [/asy] ~MRENTHUSIASM

## Solution 1
Let $P,Q,R,X,Y,$ and $Z$ be the intersections $\overleftrightarrow{AB}\cap\overleftrightarrow{CD},\overleftrightarrow{CD}\cap\overleftrightarrow{EF},\overleftrightarrow{EF}\cap\overleftrightarrow{AB},\overleftrightarrow{BC}\cap\overleftrightarrow{DE},\overleftrightarrow{DE}\cap\overleftrightarrow{FA},$ and $\overleftrightarrow{FA}\cap\overleftrightarrow{BC},$ respectively.
The sum of the interior angles of any hexagon is $720^\circ.$ Since hexagon $ABCDEF$ is equiangular, each of its interior angles is $720^\circ\div6=120^\circ.$ By angle chasing, we conclude that the interior angles of $\triangle PBC,\triangle QDE,\triangle RFA,\triangle XCD,\triangle YEF,$ and $\triangle ZAB$ are all $60^\circ.$ Therefore, these triangles are all equilateral triangles, from which $\triangle PQR$ and $\triangle XYZ$ are both equilateral triangles.
We are given that \begin{alignat*}{8} [PQR]&=\frac{\sqrt{3}}{4}\cdot PQ^2&&=192\sqrt3, \\ [XYZ]&=\frac{\sqrt{3}}{4}\cdot YZ^2&&=324\sqrt3, \end{alignat*} so we get $PQ=16\sqrt3$ and $YZ=36,$ respectively.
By equilateral triangles and segment addition, we find the perimeter of hexagon $ABCDEF:$ \begin{align*} AB+BC+CD+DE+EF+FA&=AZ+PC+CD+DQ+YF+FA \\ &=(YF+FA+AZ)+(PC+CD+DQ) \\ &=YZ+PQ \\ &=36+16\sqrt{3}. \end{align*} Finally, the answer is $36+16+3=\boxed{\textbf{(C)} ~55}.$
~sugar_rush ~MRENTHUSIASM

## Solution 2
Let the length $AB=x, BC=y.$ Then, we have \begin{align*} (y+2x)^2\cdot\frac{\sqrt 3}{4}&=324\sqrt3, \\ (x+2y)^2\cdot\frac{\sqrt 3}{4}&=192\sqrt3. \end{align*} We get \begin{align*} y+2x&=36, \\ x+2y&=16\sqrt3. \end{align*} We want $3x+3y,$ and it follows that \[3x+3y=(y+2x)+(x+2y)=36+16\sqrt3.\] Finally, the answer is $36+16+3=\boxed{\textbf{(C)} ~55}.$
~mathboy282
Note: This solution is kind of a fakesolve because it assumes the hexagon is rotationally symmetric, which we can see it is not by the diagram in Solution 1.
~Almora

## Solution 3
Since it is an equiangular hexagon, each interior angle measures 120 degrees, and by angle chasing you can conclude that all the triangles are equilateral. Since the area formula for an equiangular triangle is s^2 sqrt(3)/4, the side lengths of the triangles are 36 and 16 sqrt(3). In the above diagram the sum of the lengths of AF, AB, and FE is 36 and the sum of the lengths of BC, CD, and DE is 16sqrt(3). Since these are also the side lengths of the hexagon, the answer is 36+16+3=55 (C).
~NamyaB.

## Video Solution by OmegaLearn (Angle Chasing and Equilateral Triangles)
https://youtu.be/ptBwDcmDaLA
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/8qcbZ8c7fHg
~IceMatrix

## Video Solution by MRENTHUSIASM (English & Chinese)
https://www.youtube.com/watch?v=0n8EAu2VAiM
~MRENTHUSIASM
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .