# 2012 AMC 10B Problem 16

## Problem

Three circles with radius 2 are mutually tangent. What is the total area of the circles and the region bounded by them, as shown in the figure?

[asy] filldraw((0,0)--(2,0)--(1,sqrt(3))--cycle,gray,gray); filldraw(circle((1,sqrt(3)),1),gray); filldraw(circle((0,0),1),gray); filldraw(circle((2,0),1),grey);[/asy]

$\textbf{(A)}\ 10\pi+4\sqrt{3}\qquad\textbf{(B)}\ 13\pi-\sqrt{3}\qquad\textbf{(C)}\ 12\pi+\sqrt{3}\qquad\textbf{(D)}\ 10\pi+9\qquad\textbf{(E)}\ 13\pi$

## Solution 1
To determine the area of the figure, you can connect the centers of the circles to form an equilateral triangle with a side of length $4$ . We must find the area of this triangle to include the figure formed in between the circles. Since the equilateral triangle has two 30-60-90 triangles inside, we can find the height and the base of each 30-60-90 triangle from the ratios: $1: \sqrt{3}: 2.$ The height is $2\sqrt{3}$ and the base is $2$ . Multiplying the height and base together with $\dfrac{1}{2}$ , we get $2\sqrt{3}$ . Since there are two 30-60-90 triangles in the equilateral triangle, we multiply the area of the $30-60-90$ triangle by $2$ : \[2\cdot 2\sqrt{3} = 4\sqrt{3}.\]
To find the area of the remaining sectors, which are $\dfrac{5}{6}$ of the original circles once we remove the triangle, we know that the sectors have a central angle of $300^\circ$ since the equilateral triangle already covered that area. Since there are $3$ $\dfrac{1}{6}$ pieces gone from the equilateral triangle, we have, in total, $\dfrac{1}{2}$ of a circle (with radius $2$ ) gone. Each circle has an area of $\pi r^2 = 4\pi$ , so three circles gives a total area of $12\pi$ . Subtracting the half circle, we have: \[12\pi - \dfrac{4\pi}{2} = 12\pi - 2\pi = 10\pi.\]
Summing the areas from the equilateral triangle and the remaining circle sections gives us: $\boxed{\textbf{(A)} 10\pi + 4\sqrt3}$ .

## Solution 2
First, the area of the 3 circles is simply $3*\pi*2^2 = 12 \pi$ . Notice that the middle area is a little more than a rectangle formed by completely filling the rectangle formed by connecting two 90 degrees partial circles and then subtracting the two 90 degrees partial circles. The area of the rectangle is $4*2=8$ and the area of the 90 degrees partial circles are $2*(1/4)*\pi*2^2 = 2\pi$ . Therefore, the area of the shape in between the three circles is a little less than $8 - 2\pi$ . Summing up the 3 circles we got and the approximate area of the middle shape, we get $10\pi+8$ , which is a little more than what we want. We see that all answer choices except $\boxed{\textbf{(A)} 10\pi + 4\sqrt3}$ is greater than $10\pi+8$ , therefore it's the only answer. -dchang0524

## Solution 3 (answer choices, not recommended)
Notice as in solution 1 that the figure is simply an equilateral triangle and $3$ sectors of $\frac{5}{6}$ of a circle which makes a total of $\frac{5}{2}$ circles. Calculating this area with $\pi r^2$ , we get $10\pi$ . We also know that the equilateral triangle will give us some constant multiplied by $\sqrt3$ . The only answer choice with $10\pi$ and $\sqrt3$ is $\boxed{\textbf{(A)}}$ . ~chrisdiamond10

## Solution 4
Notice that we can connect the centers of the 3 circles to make an equilateral triangle with length $4$ . The equilateral triangle with length $4$ has area $4$ $\sqrt{3}$ . Because the triangle took $1/6$ th of all the 3 circles away, we have the area of the circles as $(5/6)*(4\pi)*3 = 10\pi$ . We add the area of the triangle to get $10 \pi$ + $4$ $\sqrt{3}$ = $\boxed {A}$

## Solution 5 (Arcs)
Notice that we can connect the centers of the circles to form an equilateral triangle. Then we notice the triangle is made of $3$ arcs and the wonky area in the middle. Area of an equilateral triangle is $\frac{\sqrt{3}}{4}a^2$ . We can get that a side of the triangle is $2$ times the radius of the circle, which is $4$ . Therefore the area is $16\frac{\sqrt{3}}{4}=\frac{16\sqrt{3}}{4}=4\sqrt{3}$ . Arc formula is $\frac{\theta}{360}\pi r^2$ , where $\theta$ is the degree of the arc. All angles of an equilateral triangle is $90$ , so the area of the $3$ arcs is $3\frac{60}{360}4\pi=3(\frac{1}{6}4\pi)=\frac{1}{2}(4\pi)=2\pi$ . Therefore the area of the wonky "triangle" is the triangle minus the 3 arcs, which is $4\sqrt{3}-2\pi$ . The area of the $3$ circles is $3(4\pi)$ which is $12\pi$ . Therefore the area of the whole shape is $12\pi-2\pi+4\sqrt{3}=\boxed{\textbf{(A)} 10\pi + 4\sqrt3}$ . ~ shunyipanda

## Video Solution
https://youtu.be/G44CDSfgt7Y
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/NsQbhYfGh1Q?t=1569
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .