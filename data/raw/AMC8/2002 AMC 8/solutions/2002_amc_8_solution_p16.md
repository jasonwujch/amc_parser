# 2002 AMC 8 Problem 16

## Problem

Right isosceles triangles are constructed on the sides of a 3-4-5 right triangle, as shown. A capital letter represents the area of each triangle. Which one of the following is true?

[asy] /* AMC8 2002 #16 Problem */ draw((0,0)--(4,0)--(4,3)--cycle); draw((4,3)--(-4,4)--(0,0)); draw((-0.15,0.1)--(0,0.25)--(.15,0.1)); draw((0,0)--(4,-4)--(4,0)); draw((4,0.2)--(3.8,0.2)--(3.8,-0.2)--(4,-0.2)); draw((4,0)--(7,3)--(4,3)); draw((4,2.8)--(4.2,2.8)--(4.2,3)); label(scale(0.8)*"$Z$", (0, 3), S); label(scale(0.8)*"$Y$", (3,-2)); label(scale(0.8)*"$X$", (5.5, 2.5)); label(scale(0.8)*"$W$", (2.6,1)); label(scale(0.65)*"5", (2,2)); label(scale(0.65)*"4", (2.3,-0.4)); label(scale(0.65)*"3", (4.3,1.5));[/asy]

$\textbf{(A)}\ X+Z=W+Y\qquad\textbf{(B)}\ W+X=Z\qquad\textbf{(C)}\ 3X+4Y=5Z\qquad$ $\textbf{(D)}\ X+W=\frac{1}{2}(Y+Z)\qquad\textbf{(E)}\ X+Y=Z$

## Solution 1
The area of a right triangle can be found by using the legs of triangle as the base and height. In the three isosceles triangles, the length of their second leg is the same as the side that is connected to the $3-4-5$ triangle.
\begin{align*} W&=(3)(4)/2 = 6\\ X&=(3)(3)/2=4.5\\ Y&=(4)(4)/2 = 8\\ Z&=(5)(5)/2 = 12.5 \end{align*}
Plugging into the answer choices, the only that works is $\boxed{\textbf{(E)}\ X+Y=Z}$ .

## Solution 2
Looking at the diagram, we notice that three right isosceles triangles on one right triangle reminds us of the Pythagorean theorem, since each right isosceles triangle is actually half of a square. Each square's area represents a side length squared, so the squares on the legs of the right triangle adds to the square on the hypotenuse. This gives $2X+2Y=2Z$ . Then, dividing by 2 we get $X+Y=Z$ , which is one of the answer choices. Since there can only be one correct answer, and there is already one, we see that the answer must be $\boxed{\textbf{(E)}\ X+Y=Z}$ .

## Video Solution
https://youtu.be/C505IVpZEMc Soo, DRMS, NM
https://www.youtube.com/watch?v=ClBrpurT0NQ ~David

## Video Solution by WhyMath
https://youtu.be/eJS_P89yKvU
### See Also