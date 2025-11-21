# 2005 AMC 8 Problem 23

## Problem

Isosceles right triangle $ABC$ encloses a semicircle of area $2\pi$ . The circle has its center $O$ on hypotenuse $\overline{AB}$ and is tangent to sides $\overline{AC}$ and $\overline{BC}$ . What is the area of triangle $ABC$ ?

[asy]pair a=(4,4), b=(0,0), c=(0,4), d=(4,0), o=(2,2); draw(circle(o, 2)); clip(a--b--c--cycle); draw(a--b--c--cycle); dot(o); label("$C$", c, NW); label("$A$", a, NE); label("$B$", b, SW);[/asy]

$\textbf{(A)}\ 6\qquad\textbf{(B)}\ 8\qquad\textbf{(C)}\ 3\pi\qquad\textbf{(D)}\ 10\qquad\textbf{(E)}\ 4\pi$

First, we notice half a square so first let's create a square. Once we have a square, we will have a full circle. This circle has a diameter of 4 which will be the side of the square. The area would be $4\cdot 4 = 16.$ Divide 16 by 2 to get the original shape and you get $\boxed{8}$

## Solution 2
We can figure out the radius of the semicircle from the question states that the area of the semicircle is $2\pi$ and we can multiply it by 2 to complete the circle to get $4\pi$ which we can find the radius of 2. Draw line segment OD such that it is the midsegment of triangle ABC, using the midsegment theorem we can see that line segment AC = $2*2=4$ . Since triangle ABC is an isosceles right triangle we can calculate the area to be $\frac{4^2}{2}$ = $\boxed{8}$

## Video Solution
https://www.youtube.com/watch?v=cNbXCQXUc6E ~David

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=1116
~ pi_is_3.14
### See Also