# 2008 AMC 10A Problem 21

## Problem

A cube with side length $1$ is sliced by a plane that passes through two diagonally opposite vertices $A$ and $C$ and the midpoints $B$ and $D$ of two opposite edges not containing $A$ or $C$ , as shown. What is the area of quadrilateral $ABCD$ ?

[asy] import three; unitsize(3cm); defaultpen(fontsize(8)+linewidth(0.7)); currentprojection=obliqueX; draw((0.5,0,0)--(0,0,0)--(0,0,1)--(0,0,0)--(0,1,0),linetype("4 4")); draw((0.5,0,1)--(0,0,1)--(0,1,1)--(0.5,1,1)--(0.5,0,1)--(0.5,0,0)--(0.5,1,0)--(0.5,1,1)); draw((0.5,1,0)--(0,1,0)--(0,1,1)); dot((0.5,0,0)); label("$A$",(0.5,0,0),WSW); dot((0,1,1)); label("$C$",(0,1,1),NE); dot((0.5,1,0.5)); label("$D$",(0.5,1,0.5),ESE); dot((0,0,0.5)); label("$B$",(0,0,0.5),NW);[/asy]

$\mathrm{(A)}\ \frac{\sqrt{6}}{2}\qquad\mathrm{(B)}\ \frac{5}{4}\qquad\mathrm{(C)}\ \sqrt{2}\qquad\mathrm{(D)}\ \frac{5}{8}\qquad\mathrm{(E)}\ \frac{3}{4}$

## Solution
Since $AB = AD = CB = CD = \sqrt{\left(\frac{1}{2}\right)^2+1^2}$ , it follows that $ABCD$ is a rhombus . The area of the rhombus can be computed by the formula $A = \frac 12 d_1d_2$ , where $d_1,\,d_2$ are the diagonals of the rhombus (or of a kite in general). $BD$ has the same length as a face diagonal, or $\sqrt{1^2 + 1^2} = \sqrt{2}$ . $AC$ is a space diagonal, with length $\sqrt{1^2+1^2+1^2} = \sqrt{3}$ . Thus $A = \frac 12 \times \sqrt{2} \times \sqrt{3} = \frac{\sqrt{6}}{2}\ \mathrm{(A)}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .