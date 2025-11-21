# 2012 AMC 10B Problem 12

## Problem

Point $B$ is due east of point $A$ . Point $C$ is due north of point $B$ . The distance between points $A$ and $C$ is $10\sqrt 2$ , and $\angle BAC = 45^\circ$ . Point $D$ is $20$ meters due north of point $C$ . The distance $AD$ is between which two integers?

$\textbf{(A)}\ 30\ \text{and}\ 31 \qquad\textbf{(B)}\ 31\ \text{and}\ 32 \qquad\textbf{(C)}\ 32\ \text{and}\ 33 \qquad\textbf{(D)}\ 33\ \text{and}\ 34 \qquad\textbf{(E)}\ 34\ \text{and}\ 35$

## Solution
[asy] unitsize(4); pair A=(0,0); label ("A",(0,0),W); pair B=(10,0); label ("B",(10,0),E); pair C=(10,10); label ("C",(10,10),E); pair D=(10,30); label ("D",(10,30),E); dot(A); dot(B); dot(C); dot(D); draw(A--B); draw(A--C); draw(A--D); draw(C--D); draw(B--C); [/asy] If point B is due east of point A and point C is due north of point B, $\angle CBA$ is a right angle. And if $\angle BAC = 45^\circ$ , $\triangle CBA$ is a 45-45-90 triangle. Thus, the lengths of sides $CB$ , $BA$ , and $AC$ are in the ratio $1:1:\sqrt 2$ , and $CB$ is $10 \sqrt 2 \div \sqrt 2 = 10$ .
$\triangle DBA$ is clearly a right triangle with $C$ on the side $DB$ . $DC$ is 20, so $DB = DC + CB = 20 + 10 = 30$ .
By the Pythagorean Theorem, $DA = \sqrt {DB^2 + BA^2} = \sqrt {30^2 + 10 ^2} = \sqrt {1000}$ .
$31^2 = 961$ , and $32^2 = 1024$ . Thus, $\sqrt {1000}$ must be between $31$ and $32$ . The answer is $\boxed {B}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .