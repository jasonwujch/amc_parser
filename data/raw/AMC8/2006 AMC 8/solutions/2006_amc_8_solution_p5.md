# 2006 AMC 8 Problem 5

## Problem

Points $A, B, C$ and $D$ are midpoints of the sides of the larger square. If the larger square has area 60, what is the area of the smaller square?

[asy]size(100); draw((0,0)--(2,0)--(2,2)--(0,2)--cycle,linewidth(1)); draw((0,1)--(1,2)--(2,1)--(1,0)--cycle); label("$A$", (1,2), N); label("$B$", (2,1), E); label("$C$", (1,0), S); label("$D$", (0,1), W);[/asy]

$\textbf{(A)}\ 15 \qquad \textbf{(B)}\ 20 \qquad \textbf{(C)}\ 24 \qquad \textbf{(D)}\ 30 \qquad \textbf{(E)}\ 40$

## Solution

## Solution 1
Drawing segments $AC$ and $BD$ , the number of triangles outside square $ABCD$ is the same as the number of triangles inside the square. Thus areas must be equal so the area of $ABCD$ is half the area of the larger square which is $\frac{60}{2}=\boxed{\textbf{(D)}\ 30 }$ .

## Solution 2
If the side length of the larger square is $x$ , the side length of the smaller square is $\frac{\sqrt{2} \cdot x}{2}$ . Therefore the area of the smaller square is $\frac{x^2}{2}$ , half of the larger square's area, $x^2$ .
Thus, the area of the smaller square in the picture is $\frac{60}{2}=\boxed{\textbf{(D)}\ 30 }$ .

## Solution 3
The smaller square forms four congruent isosceles right triangles whose legs measure half of the larger square's side length. Since the larger square has an area of $60$ , its sides measure $\sqrt{60}=2\sqrt{15}$ . Therefore, the legs of the right triangles measure $\sqrt{15}$ . Now we can use the Pythagorean Theorem to find the length of the hypotenuses, or the smaller square's sides. We have \[\sqrt{{\sqrt{15}}^2+{\sqrt{15}}^2}=\sqrt{15+15}=\sqrt{30}.\] Squaring this, the area of the smaller square is $\boxed{\textbf{(D)}\ 30 }$ .

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=822
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/pfqtAX6AHNg
### See Also