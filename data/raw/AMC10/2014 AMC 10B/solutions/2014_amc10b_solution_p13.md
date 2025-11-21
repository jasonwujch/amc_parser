# 2014 AMC 10B Problem 13

## Problem

Six regular hexagons surround a regular hexagon of side length $1$ as shown. What is the area of $\triangle{ABC}$ ?

[asy] draw((0,0)--(-5,8.66025404)--(0, 17.3205081)--(10, 17.3205081)--(15,8.66025404)--(10, 0)--(0, 0)); draw((30,0)--(25,8.66025404)--(30, 17.3205081)--(40, 17.3205081)--(45, 8.66025404)--(40, 0)--(30, 0)); draw((30,0)--(25,-8.66025404)--(30, -17.3205081)--(40, -17.3205081)--(45, -8.66025404)--(40, 0)--(30, 0)); draw((0,0)--(-5, -8.66025404)--(0, -17.3205081)--(10, -17.3205081)--(15, -8.66025404)--(10, 0)--(0, 0)); draw((15,8.66025404)--(10, 17.3205081)--(15, 25.9807621)--(25, 25.9807621)--(30, 17.3205081)--(25, 8.66025404)--(15, 8.66025404)); draw((15,-8.66025404)--(10, -17.3205081)--(15, -25.9807621)--(25, -25.9807621)--(30, -17.3205081)--(25, -8.66025404)--(15, -8.66025404)); label("A", (0,0), W); label("B", (30, 17.3205081), NE); label("C", (30, -17.3205081), SE); draw((0,0)--(30, 17.3205081)--(30, -17.3205081)--(0, 0)); //(Diagram Creds-DivideBy0) [/asy]

$\textbf {(A) } 2\sqrt{3} \qquad \textbf {(B) } 3\sqrt{3} \qquad \textbf {(C) } 1+3\sqrt{2} \qquad \textbf {(D) } 2+2\sqrt{3} \qquad \textbf {(E) } 3+2\sqrt{3}$

## Solution 1
We note that the $6$ triangular sections in $\triangle{ABC}$ can be put together to form a hexagon congruent to each of the seven other hexagons. By the formula for the area of the hexagon, we get the area for each hexagon as $\dfrac{3\sqrt{3}}{2}$ . The area of $\triangle{ABC}$ , which is equivalent to two of these hexagons together, is $\boxed{\textbf{(B)} 3\sqrt{3}}$ .

## Solution 2
The measure of an interior angle in a hexagon is 120 degrees. Each side of the 6 triangles that make up the remainder of triangle ABC are isosceles with 2 side lengths of 1 and an angle of 120 degrees. Therefore, by the Law of Cosines, we calculate that the longest side of this triangle is $\sqrt{3}$ , so the side length of triangle ABC is $2\sqrt{3}$ . Using the equilateral triangle area formula, we figure out that the answer is $\boxed{\textbf{(B)} 3\sqrt{3}}$ . (note that it may not be so nice to use trigonometry in AMC10 contest, however, it is a more efficient way of solving those geometry question. ~Kai Gao)

## Solution 3
We know the area of a triangle can be found through the formula $\text{Area = inradius} \cdot \text{semiperimeter}$ .
As the hexagon fully enveloped inside the triangle touches all $3$ sides, we can visualize that hexagon as $6$ congruent equilateral triangles, each with side lengths $1$ . Draw a circle that circumscribes the hexagon. Using the equilateral triangles, we can see that the circle has a radius of $1$ .
Since the circle touches all 3 sides of the triangle, we can say that $1$ is the inradius of $\triangle{ABC}$ . We can find the semiperimeter of $\triangle{ABC}$ by applying the $30-60-90$ rule of triangles on the $6$ congruent triangles inside $\triangle{ABC}$ to find that the perimeter is $6\sqrt{3}$ . Thus, the semiperimeter is $\dfrac{6\sqrt{3}}{2} = 3\sqrt{3}$ . Thus, the area of the triangle is $1 \cdot 3\sqrt{3} = \boxed{\textbf{(B)} 3\sqrt{3}}$ ~NSAoPS
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .