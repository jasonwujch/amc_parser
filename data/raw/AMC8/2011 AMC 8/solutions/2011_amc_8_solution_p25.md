# 2011 AMC 8 Problem 25

## Problem

A circle with radius $1$ is inscribed in a square and circumscribed about another square as shown. Which fraction is closest to the ratio of the circle's shaded area to the area between the two squares?

[asy] filldraw((-1,-1)--(-1,1)--(1,1)--(1,-1)--cycle,gray,black); filldraw(Circle((0,0),1), mediumgray,black); filldraw((-1,0)--(0,1)--(1,0)--(0,-1)--cycle,white,black);[/asy]

$\textbf{(A)}\ \frac{1}2\qquad\textbf{(B)}\ 1\qquad\textbf{(C)}\ \frac{3}2\qquad\textbf{(D)}\ 2\qquad\textbf{(E)}\ \frac{5}2$

## Solution 1
The area of the smaller square is one half of the product of its diagonals. Note that the distance from a corner of the smaller square to the center is equivalent to the circle's radius so the diagonal is equal to the diameter: $2 \cdot 2 \cdot \frac{1}{2}=2.$
The circle's shaded area is the area of the smaller square subtracted from the area of the circle: $\pi - 2.$
If you draw the diagonals of the smaller square, you will see that the larger square is split $4$ congruent half-shaded squares. The area between the squares is equal to the area of the smaller square: $2.$
Approximating $\pi$ to $3.14,$ the ratio of the circle's shaded area to the area between the two squares is about
\[\frac{\pi-2}{2} \approx \frac{3.14-2}{2} = \frac{1.14}{2} \approx \boxed{\textbf{(A)}\ \frac12}\]

## Solution 2
For the ratio of the circle's shaded area to the area between the squares to be $1,$ they would have to be approximately the same size. For any ratio larger than that, the circle's shaded area must be greater. However, we can clearly see that the circle's shaded area is part of the area between the squares, and is approximately $\boxed{\textbf{(A)}\ \frac12}$ .
Note that this solution is not rigorous, because we still should show that the ratio is less than $\frac{3}{4}$ .

## Solution 3
Set the side length of the bigger square to be $8$ . Then the area of the big square is $8^2 =64$ and the area of the small square $(4\sqrt{2})^2 = 32$ , making the difference $32$ . The area of the circle is $4^2$ times $\pi$ which is $16 \pi$ or about $48$ . Knowing the area of the small square is $32$ . $48-32$ is $16$ . The area of the big square is $64$ . So $32/64$ is $1/2$ , or $\boxed{\textbf{(A)}\ \frac12}$ .

## Solution 4 (Non-rigorous speed solution)
Note that that the shaded area of the circle is existent only between the gap between the two squares. This implies that the shaded area is less than the gap, and the only answer that shows that is $\boxed{\textbf{(A)}\ \frac{1}{2}}$ .
- by nickelslordm

## Video Solution
https://youtu.be/PR-45YsyBGM Soo, DRMS, NM

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=1759
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/Nsm9bggy30g
~savannahsolver
### See Also