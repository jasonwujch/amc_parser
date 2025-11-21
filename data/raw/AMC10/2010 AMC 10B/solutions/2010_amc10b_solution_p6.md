# 2010 AMC 10B Problem 6

## Problem

A circle is centered at $O$ , $\overline{AB}$ is a diameter and $C$ is a point on the circle with $\angle COB = 50^\circ$ . What is the degree measure of $\angle CAB$ ?

$\textbf{(A)}\ 20 \qquad \textbf{(B)}\ 25 \qquad \textbf{(C)}\ 45 \qquad \textbf{(D)}\ 50 \qquad \textbf{(E)}\ 65$

## Solution 1
Assuming we do not already know an inscribed angle is always half of its central angle, we will try a different approach. Since $O$ is the center, $OC$ and $OA$ are radii and they are congruent. Thus, $\triangle COA$ is an isosceles triangle. Also, note that $\angle COB$ and $\angle COA$ are supplementary, then $\angle COA = 180 - 50 = 130^{\circ}$ . Since $\triangle COA$ is isosceles, then $\angle OCA \cong \angle OAC$ . They also sum to $50^{\circ}$ , so each angle is $\boxed{\textbf{(B)}\ 25}$ .

## Solution 2 (Alcumus)
Note that $\angle AOC = 180^\circ - 50^\circ = 130^\circ$ . Because triangle $AOC$ is isosceles, $\angle CAB = (180^\circ - 130^\circ)/2 = \boxed{25^\circ}$ .
[asy] import graph; unitsize(2 cm); pair O, A, B, C; O = (0,0); A = (-1,0); B = (1,0); C = dir(50); draw(Circle(O,1)); draw(B--A--C--O); label("$A$", A, W); label("$B$", B, E); label("$C$", C, NE); label("$O$", O, S); [/asy]

## Video Solution
https://youtu.be/wqRMJBoSm_A
~Education, the Study of Everything

## Video Solution
https://youtu.be/I3yihAO87CE
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .