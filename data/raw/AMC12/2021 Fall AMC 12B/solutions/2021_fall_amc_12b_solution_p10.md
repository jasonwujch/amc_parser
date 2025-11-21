# 2021 Fall AMC 12B Problem 10

## Problem

What is the sum of all possible values of $t$ between $0$ and $360$ such that the triangle in the coordinate plane whose vertices are \[(\cos 40^\circ,\sin 40^\circ), (\cos 60^\circ,\sin 60^\circ), \text{ and } (\cos t^\circ,\sin t^\circ)\] is isosceles?

$\textbf{(A)} \: 100 \qquad\textbf{(B)} \: 150 \qquad\textbf{(C)} \: 330 \qquad\textbf{(D)} \: 360 \qquad\textbf{(E)} \: 380$

## Solution
Let $A = (\cos 40^{\circ}, \sin 40^{\circ}), B = (\cos 60^{\circ}, \sin 60^{\circ}),$ and $C = (\cos t^{\circ}, \sin t^{\circ}).$ We apply casework to the legs of isosceles $\triangle ABC:$
1. $AB=AC$ Note that must be the midpoint of It follows that so
1. $BA=BC$ Note that must be the midpoint of It follows that so
1. $CA=CB$ Note that must be the midpoint of It follows that or so or
Note that $A$ must be the midpoint of $\widehat{BC}.$ It follows that $C = (\cos 20^{\circ}, \sin 20^{\circ}),$ so $t=20.$
Note that $B$ must be the midpoint of $\widehat{AC}.$ It follows that $C = (\cos 80^{\circ}, \sin 80^{\circ}),$ so $t=80.$
Note that $C$ must be the midpoint of $\widehat{AB}.$ It follows that $C = (\cos 50^{\circ}, \sin 50^{\circ})$ or $C = (\cos 230^{\circ}, \sin 230^{\circ}),$ so $t=50$ or $t=230.$
Together, the sum of all such possible values of $t$ is $20+80+50+230=\boxed{\textbf{(E)} \: 380}.$
Remark
The following diagram shows all possible locations of $C:$
[asy] /* Made by MRENTHUSIASM */ size(200); int xMin = -1; int xMax = 1; int yMin = -1; int yMax = 1; int numRays = 36; //Draws a polar grid that goes out to a number of circles //equal to big, with numRays specifying the number of rays: void polarGrid(int big, int numRays) { for (int i = 1; i < big+1; ++i) { draw(Circle((0,0),i), gray+linewidth(0.4)); } for (int i=0;i<numRays;++i) draw(rotate(i*360/numRays)*((-big,0)--(big,0)), gray+linewidth(0.4)); } polarGrid(xMax,numRays); draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$x$",(xMax,0),2*E); label("$y$",(0,yMax),2*N); pair A, B, C1, C2, C3, C4; A = dir(40); B = dir(60); C1 = dir(20); C2 = dir(80); C3 = dir(50); C4 = dir(230); dot("$A$",A,1.5*dir(A),linewidth(4)); dot("$B$",B,1.5*dir(B),linewidth(4)); dot("$C_1$",C1,1.5*dir(C1),red+linewidth(4)); dot("$C_2$",C2,1.5*dir(C2),red+linewidth(4)); dot("$C_3$",C3,1.5*dir(C3),red+linewidth(4)); dot("$C_3$",C4,1.5*dir(C4),red+linewidth(4)); [/asy]
~Steven Chen (www.professorchenedu.com) ~Wilhelm Z ~MRENTHUSIASM

## Video Solution (Just 1 min!)
https://youtu.be/F_Hy5OWBC54
~Education, the Study of Everything

## Video Solution by TheBeautyofMath
https://www.youtube.com/watch?v=4qgYrCYG-qw&t=1304
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .