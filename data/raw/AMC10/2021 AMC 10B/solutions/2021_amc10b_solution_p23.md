# 2021 AMC 10B Problem 23

## Problem

A square with side length $8$ is colored white except for $4$ black isosceles right triangular regions with legs of length $2$ in each corner of the square and a black diamond with side length $2\sqrt{2}$ in the center of the square, as shown in the diagram. A circular coin with diameter $1$ is dropped onto the square and lands in a random location where the coin is completely contained within the square. The probability that the coin will cover part of the black region of the square can be written as $\frac{1}{196}\left(a+b\sqrt{2}+\pi\right)$ , where $a$ and $b$ are positive integers. What is $a+b$ ? [asy] /* Made by samrocksnature */ draw((0,0)--(8,0)--(8,8)--(0,8)--(0,0)); fill((2,0)--(0,2)--(0,0)--cycle, black); fill((6,0)--(8,0)--(8,2)--cycle, black); fill((8,6)--(8,8)--(6,8)--cycle, black); fill((0,6)--(2,8)--(0,8)--cycle, black); fill((4,6)--(2,4)--(4,2)--(6,4)--cycle, black); filldraw(circle((2.6,3.31),0.5),gray); [/asy] $\textbf{(A)} ~64 \qquad\textbf{(B)} ~66 \qquad\textbf{(C)} ~68 \qquad\textbf{(D)} ~70 \qquad\textbf{(E)} ~72$

### Diagram

Note that the center of the coin can lie anywhere inside a green region, as shown below. [asy] /* Made by MRENTHUSIASM */ draw((0,0)--(8,0)--(8,8)--(0,8)--(0,0)); fill((2,0)--(0,2)--(0,0)--cycle, black); fill((6,0)--(8,0)--(8,2)--cycle, black); fill((8,6)--(8,8)--(6,8)--cycle, black); fill((0,6)--(2,8)--(0,8)--cycle, black); fill((4,6)--(2,4)--(4,2)--(6,4)--cycle, black); draw((0.5,7.5)--(0.5+1+sqrt(2)/2,7.5)--(0.5,7.5-1-sqrt(2)/2)--cycle, green); draw((0.5,0.5)--(0.5+1+sqrt(2)/2,0.5)--(0.5,0.5+1+sqrt(2)/2)--cycle, green); draw((7.5,7.5)--(7.5-1-sqrt(2)/2,7.5)--(7.5,7.5-1-sqrt(2)/2)--cycle, green); draw((7.5,0.5)--(7.5-1-sqrt(2)/2,0.5)--(7.5,0.5+1+sqrt(2)/2)--cycle, green); draw(Arc((4,6),0.5,135,45)--Arc((6,4),0.5,45,-45)--Arc((4,2),0.5,-45,-135)--Arc((2,4),0.5,225,135)--cycle, green); [/asy] ~MRENTHUSIASM

## Solution
To find the probability, we look at the $\frac{\text{success region}}{\text{total possible region}}$ . For the coin to be completely contained within the square, we must have the distance from the center of the coin to a side of the square to be at least $\frac{1}{2}$ , as it's the radius of the coin. This implies the $\text{total possible region}$ is a square with side length $8 - \frac{1}{2} - \frac{1}{2} = 7$ , with an area of $49$ . Now, we consider cases where needs to land to partially cover a black region.
Near The Center Square
We can have the center of the coin land within $\frac{1}{2}$ outside of the center square, or inside of the center square. So, we have a region with $\frac{1}{2}$ emanating from every point on the exterior of the square, forming four quarter circles and four rectangles. The four quarter circles combine to make a full circle of radius $\frac{1}{2}$ , so the area is $\frac{\pi}{4}$ . The area of a rectangle is $2 \sqrt 2 \cdot \frac{1}{2} = \sqrt 2$ , so $4$ of them combine to an area of $4 \sqrt 2$ . The area of the black square is simply $\left(2\sqrt 2\right)^2 = 8$ . So, for this case, we have a combined total of $8 + 4\sqrt 2 + \frac{\pi}{4}$ . Onto the second (and last) case.
Near A Triangle
We can also have the coin land within $\frac{1}{2}$ outside of one of the triangles. By symmetry, we can just find the successful region for one of them, then multiply by $4$ . Consider the above diagram. We can draw an altitude from the bottom corner of the square to hit the hypotenuse of the green triangle. The length of this when passing through the black region is $\sqrt 2$ , and when passing through the white region (while being contained in the green triangle) is $\frac{1}{2}$ . However, we have to subtract off when it doesn't pass through the red square. Then, it's the hypotenuse of a small isosceles right triangle with side lengths of $\dfrac{1}{2}$ which is $\dfrac{\sqrt{2}}{2}.$ So, the altitude of the green triangle is $\sqrt 2 + \frac{1}{2} - \frac{\sqrt 2}{2} = \frac{\sqrt 2 + 1}{2}$ . Then, recall, the area of an isosceles right triangle is $h^2$ , where $h$ is the altitude from the right angle. So, squaring this, we get $\frac{3 + 2\sqrt 2}{4}$ . Now, we have to multiply this by $4$ to account for all of the black triangles, to get $3 + 2\sqrt 2$ as the final area for this case.
Finishing
Then, to have the coin touching a black region, we add up the area of our successful regions, or $8 + 4\sqrt 2 + \frac{\pi}{4} + 3 + 2\sqrt 2 = 11 + 6\sqrt 2 + \frac{\pi}{4} = \frac{44 + 24\sqrt 2 + \pi}{4}$ . The total region is $49$ , so our probability is $\frac{\frac{44 + 24\sqrt 2 + \pi}{4}}{49} = \frac{44 + 24\sqrt 2 + \pi}{196}$ , which implies $a+b = 44+24 = 68$ . This corresponds to answer choice $\boxed{\textbf{(C)} ~68}$ .
~rocketsri ~ minor edit from jrepsa ~ minor edit from lpieleanu
### Image
~mathboy282

## Video Solution by OmegaLearn (Similar Triangles and Area Calculations)
https://youtu.be/-UvivZ0UA1U
~ pi_is_3.14

## Video Solution by Interstigation (Using Casework)
https://youtu.be/QYLg-xOtmPc
~ Interstigation

## Video Solution by The Power of Logic
https://www.youtube.com/watch?v=o3_kUpWUokw
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .