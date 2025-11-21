# 2006 AMC 10B Problem 6

## Problem

A region is bounded by semicircular arcs constructed on the side of a square whose sides measure $\frac{2}{\pi}$ , as shown. What is the perimeter of this region?

[asy] size(90); defaultpen(linewidth(0.7)); filldraw((0,0)--(2,0)--(2,2)--(0,2)--cycle,gray(0.5)); filldraw(arc((1,0),1,180,0, CCW)--cycle,gray(0.7)); filldraw(arc((0,1),1,90,270)--cycle,gray(0.7)); filldraw(arc((1,2),1,0,180)--cycle,gray(0.7)); filldraw(arc((2,1),1,270,90, CCW)--cycle,gray(0.7)); [/asy]

$\textbf{(A) } \frac{4}{\pi}\qquad \textbf{(B) } 2\qquad \textbf{(C) } \frac{8}{\pi}\qquad \textbf{(D) } 4\qquad \textbf{(E) } \frac{16}{\pi}$

## Solution
Since the side of the square is the diameter of the semicircle, the radius of the semicircle is $\frac{1}{2}\cdot\frac{2}{\pi}=\frac{1}{\pi}$ .
Since the length of one of the semicircular arcs is half the circumference of the corresponding circle, the length of one arc is $\frac{1}{2}\cdot2\cdot\pi\cdot\frac{1}{\pi}=1$ .
Since the desired perimeter is made up of four of these arcs, the perimeter is $4\cdot1=\boxed{\textbf{(D) }4}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .