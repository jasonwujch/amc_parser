# 2005 AMC 10A Problem 12

## Problem

The figure shown is called a trefoil and is constructed by drawing circular sectors about sides of the congruent equilateral triangles. What is the area of a trefoil whose horizontal base has length $2$ ?

[asy] unitsize(1.5cm); defaultpen(linewidth(.8pt)+fontsize(12pt)); pair O=(0,0), A=dir(0), B=dir(60), C=dir(120), D=dir(180); pair E=B+C; draw(D--E--B--O--C--B--A,linetype("4 4")); draw(Arc(O,1,0,60),linewidth(1.2pt)); draw(Arc(O,1,120,180),linewidth(1.2pt)); draw(Arc(C,1,0,60),linewidth(1.2pt)); draw(Arc(B,1,120,180),linewidth(1.2pt)); draw(A--D,linewidth(1.2pt)); draw(O--dir(40),EndArrow(HookHead,4)); draw(O--dir(140),EndArrow(HookHead,4)); draw(C--C+dir(40),EndArrow(HookHead,4)); draw(B--B+dir(140),EndArrow(HookHead,4)); label("2",O,S); draw((0.1,-0.12)--(1,-0.12),EndArrow(HookHead,4),EndBar); draw((-0.1,-0.12)--(-1,-0.12),EndArrow(HookHead,4),EndBar); [/asy]

$\textbf{(A) }\frac{1}{3}\pi+\frac{\sqrt{3}}{2}\qquad \textbf{(B) } \frac{2}{3}\pi\qquad \textbf{(C) } \frac{2}{3}\pi+\frac{\sqrt{3}}{4}\qquad \textbf{(D) } \frac{2}{3}\pi+\frac{\sqrt{3}}{3}\qquad \textbf{(E) } \frac{2}{3}\pi+\frac{\sqrt{3}}{2}$

## Solution
The area of the trefoil is equal to the area of an equilateral triangle with side length $2$ , plus the area of $4$ segments. Each segment has area equal to that of a $60^{\circ}$ sector with radius $\frac{2}{2} = 1$ , minus the area of an equilateral triangle with side length $1$ .
As there are $4$ segments, the area of the equilateral triangle with side length $1$ will be multiplied by $4$ , and this is equivalent to the area of an equilateral triangle with side length $1 \cdot \sqrt{4} = 2$ (since the area scale factor is the square of the length scale factor). Accordingly, the area of the equilateral triangle with side length $2$ will exactly cancel out, and we are left only with $4$ times the area of a $60^{\circ}$ sector with radius $1$ .
Thus the answer is $4\cdot\frac{60}{360}\cdot\pi\cdot 1^2 = \frac{4}{6}\cdot\pi = \boxed{\textbf{(B) } \frac{2}{3}\pi}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .