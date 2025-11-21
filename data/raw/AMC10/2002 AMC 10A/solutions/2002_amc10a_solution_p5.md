# 2002 AMC 10A Problem 5

## Problem

Each of the small circles in the figure has radius one. The innermost circle is tangent to the six circles that surround it, and each of those circles is tangent to the large circle and to its small-circle neighbors. Find the area of the shaded region.

[asy] unitsize(.3cm); path c=Circle((0,2),1); filldraw(Circle((0,0),3),grey,black); filldraw(Circle((0,0),1),white,black); filldraw(c,white,black); filldraw(rotate(60)*c,white,black); filldraw(rotate(120)*c,white,black); filldraw(rotate(180)*c,white,black); filldraw(rotate(240)*c,white,black); filldraw(rotate(300)*c,white,black); [/asy]

$\textbf{(A)}\ \pi \qquad \textbf{(B)}\ 1.5\pi \qquad \textbf{(C)}\ 2\pi \qquad \textbf{(D)}\ 3\pi \qquad \textbf{(E)}\ 3.5\pi$

## Solution
The outer circle has radius $1+1+1=3$ , and thus area $9\pi$ . The little circles have area $\pi$ each; since there are 7, their total area is $7\pi$ . Thus, our answer is $9\pi-7\pi=\boxed{2\pi\Rightarrow \textbf{(C)}}$ .

## Video Solution by Daily Dose of Math
https://youtu.be/VSPM5_pTK34?si=EIQDi3PF6I0P7wMR
~Thesmartgreekmathdude
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .