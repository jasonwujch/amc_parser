# 2017 AMC 10B Problem 15

## Problem

Rectangle $ABCD$ has $AB=3$ and $BC=4$ . Point $E$ is the foot of the perpendicular from $B$ to diagonal $\overline{AC}$ . What is the area of $\triangle AED$ ?

$\textbf{(A)}\ 1\qquad\textbf{(B)}\ \frac{42}{25}\qquad\textbf{(C)}\ \frac{28}{15}\qquad\textbf{(D)}\ 2\qquad\textbf{(E)}\ \frac{54}{25}$

## Solution 1
[asy] pair A,B,C,D,E; A=(0,4); B=(3,4); C=(3,0); D=(0,0); draw(A--B--C--D--cycle); label("$A$",A,N); label("$B$",B,N); label("$C$",C,S); label("$D$",D,S); E=foot(B,A,C); draw(E--B); draw(A--C); draw(rightanglemark(B,E,C)); label("$E$",E,N); draw(D--E); label("$3$",A--B,N); label("$4$",B--C,E); [/asy]
First, note that $AC=5$ because $ABC$ is a right triangle. In addition, we have $AB\cdot BC=2[ABC]=AC\cdot BE$ , so $BE=\frac{12}{5}$ . Using similar triangles within $ABC$ , we get that $AE=\frac{9}{5}$ and $CE=\frac{16}{5}$ .
Let $F$ be the foot of the perpendicular from $E$ to $AB$ . Since $EF$ and $BC$ are parallel, $\Delta AFE$ is similar to $\Delta ABC$ . Therefore, we have $\frac{AF}{AB}=\frac{AE}{AC}=\frac{9}{25}$ . Since $AB=3$ , $AF=\frac{27}{25}$ . Note that $AF$ is an altitude of $\Delta AED$ from $AD$ , which has length $4$ . Therefore, the area of $\Delta AED$ is $\frac{1}{2}\cdot\frac{27}{25}\cdot4=\boxed{\textbf{(E)}\frac{54}{25}}.$

## Solution 2
From similar triangles, we know that $AE=\frac{9}{5}$ (see Solution 1). Furthermore, we also know that $AD=4$ from the rectangle. Using the sine formula for area, we have \[\frac{1}{2}(AE)(AD)(\sin(m\angle EAD)).\] But, note that $\sin(m\angle EAD)=\sin(m\angle CAD)=\frac{O}{H}=\frac{3}{5}$ . Thus, we see that \[[AED]=\frac{1}{2}\cdot \frac{9}{5}\cdot 4\cdot\frac{3}{5}=\boxed{\textbf{(E)}\frac{54}{25}}.\] ~coolwiz

## Solution 3
Alternatively, we can use coordinates. Denote $D$ as the origin. We find the equation for $AC$ as $y=-\frac{4}{3}x+4$ , and $BE$ as $y=\frac{3}{4}x+\frac{7}{4}$ . Solving for $x$ yields $\frac{27}{25}$ . Our final answer then becomes $\frac{1}{2}\cdot\frac{27}{25}\cdot4=\boxed{\textbf{(E)}\frac{54}{25}}.$

## Solution 4
We note that the area of $ABE$ must equal the area of $AED$ because they share the base $AE$ and the height of both is the altitude of congruent triangles. Therefore, we find the area of $ABE$ to be $\frac{1}{2}*\frac{9}{5}*\frac{12}{5}=\boxed{\textbf{(E)}\frac{54}{25}}.$

## Solution 5
We know all right triangles are 5-4-3, so the areas are proportional to the square of corresponding sides. Area of $ABE$ is $(\dfrac{3}{5})^2$ of $ABC = \frac{54}{25}$ . Using similar logic in Solution 4, Area of $AED$ is the same as $ABE$ .

## Solution 6
Drop an altitude from $E$ to $BC$ and call its foot $X$ . We have that $EX \cdot BC=BE \cdot EC$ since both are equal to two times the area of $BEC$ . Since $BC=4$ , $BE=\frac{12}{5}$ , and $EC=\frac{16}{5}$ , we can calculate that $EX=\frac{48}{25}$ . If $EX$ is extended to meet $AD$ at point $Y$ , $EY=3-\frac{48}{25}=\frac{27}{25}$ . Therefore, $[AED]=\frac{EY \cdot AD}{2}=\frac{\frac{27}{25} \cdot 4}{2}=\boxed{\textbf{(E)}\frac{54}{25}}$ .
- Fasolinka

## Video Solution by OmegaLearn
https://youtu.be/GrCtzL0S-Uo?t=369
~ pi_is_3.14

## Video Solution by Math4All999
https://www.youtube.com/watch?v=hSrgGKxduho
~Math4All999
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .