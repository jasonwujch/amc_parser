# 2003 AMC 8 Problem 22

## Problem

The following figures are composed of squares and circles. Which figure has a shaded region with largest area?

[asy]/* AMC8 2003 #22 Problem */ size(3inch, 2inch); unitsize(1cm); pen outline = black+linewidth(1); filldraw((0,0)--(2,0)--(2,2)--(0,2)--cycle, mediumgrey, outline); filldraw(shift(3,0)*((0,0)--(2,0)--(2,2)--(0,2)--cycle), mediumgrey, outline); filldraw(Circle((7,1), 1), mediumgrey, black+linewidth(1)); filldraw(Circle((1,1), 1), white, outline); filldraw(Circle((3.5,.5), .5), white, outline); filldraw(Circle((4.5,.5), .5), white, outline); filldraw(Circle((3.5,1.5), .5), white, outline); filldraw(Circle((4.5,1.5), .5), white, outline); filldraw((6.3,.3)--(7.7,.3)--(7.7,1.7)--(6.3,1.7)--cycle, white, outline); label("A", (1, 2), N); label("B", (4, 2), N); label("C", (7, 2), N); draw((0,-.5)--(.5,-.5), BeginArrow); draw((1.5, -.5)--(2, -.5), EndArrow); label("2 cm", (1, -.5)); draw((3,-.5)--(3.5,-.5), BeginArrow); draw((4.5, -.5)--(5, -.5), EndArrow); label("2 cm", (4, -.5)); draw((6,-.5)--(6.5,-.5), BeginArrow); draw((7.5, -.5)--(8, -.5), EndArrow); label("2 cm", (7, -.5)); draw((6,1)--(6,-.5), linetype("4 4")); draw((8,1)--(8,-.5), linetype("4 4"));[/asy]

$\textbf{(A)}\ \text{A only}\qquad\textbf{(B)}\ \text{B only}\qquad\textbf{(C)}\ \text{C only}\qquad\textbf{(D)}\ \text{both A and B}\qquad\textbf{(E)}\ \text{all are equal}$

## Solution
First we have to find the area of the shaded region in each of the figures. In figure $\textbf{A}$ the area of the shaded region is the area of the circle subtracted from the area of the square. That is $2^2-1^2 \pi=4-\pi$ . In figure $\textbf{B}$ the area of the shaded region is the sum of the areas of the 4 circles subtracted from the area of the square. That is $2^2-4 \left( \left( \frac{1}{2} \right)^2 \pi \right)=4-4 \left(\frac{\pi}{4} \right)=4-\pi$ . In figure $\textbf{C}$ the area of the shaded region is the area of the square subtracted from the area of the circle. The diameter of the circle and the diagonal of the square are equal to 2. We can easily find the area of the square using the area formula $\frac{d_1 d_2}{2}$ . So the area of the shaded region is $1^2 \pi-\frac{2\cdot{2}}{2}=\pi-2$ . Clearly the largest area that we found among the three shaded regions is $\pi-2$ . Thus the answer is $\boxed{C}$ .

## Video Solution
https://www.youtube.com/watch?v=ei9blxnl9Gw ~David
### See Also