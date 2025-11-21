# 2014 AMC 8 Problem 9

## Problem

In $\bigtriangleup ABC$ , $D$ is a point on side $\overline{AC}$ such that $BD=DC$ and $\angle BCD$ measures $70^\circ$ . What is the degree measure of $\angle ADB$ ?

[asy] size(300); defaultpen(linewidth(0.8)); pair A=(-1,0),C=(1,0),B=dir(40),D=origin; draw(A--B--C--A); draw(D--B); dot("$A$", A, SW); dot("$B$", B, NE); dot("$C$", C, SE); dot("$D$", D, S); label("$70^\circ$",C,2*dir(180-35));[/asy]

$\textbf{(A) }100\qquad\textbf{(B) }120\qquad\textbf{(C) }135\qquad\textbf{(D) }140\qquad \textbf{(E) }150$

## Video Solution (CREATIVE THINKING)
https://youtu.be/jLnqUOe0HPE
~Education, the Study of Everything

## Video Solution
https://www.youtube.com/watch?v=HP-lBKohxhE ~David
https://youtu.be/j5KrHM81HZ8 ~savannahsolver

## Video Solution
https://youtu.be/abSgjn4Qs34?t=3140

## Solution
Using angle chasing is a good way to solve this problem. $BD = DC$ , so $\angle DBC = \angle DCB = 70$ , because it is an isosceles triangle. Then $\angle CDB = 180-(70+70) = 40$ . Since $\angle ADB$ and $\angle BDC$ are supplementary, $\angle ADB = 180 - 40 = \boxed{\textbf{(D)}~140}$ .
### See Also