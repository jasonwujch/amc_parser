# 2005 AMC 10A Problem 20

## Problem

An equiangular octagon has four sides of length $1$ and four sides of length $\sqrt{2}/2$ , arranged so that no two consecutive sides have the same length. What is the area of the octagon?

$\textbf{(A) } \frac{7}{2}\qquad \textbf{(B) } \frac{7\sqrt{2}}{2}\qquad \textbf{(C) } \frac{5+4\sqrt{2}}{2}\qquad \textbf{(D) } \frac{4+5\sqrt{2}}{2}\qquad \textbf{(E) } 7$

## Solution 1
The sum of the octagon's angles is $180\cdot(8-2)^{\circ} = 1080^{\circ}$ , so since it is equiangular, each angle is $\frac{1080^{\circ}}{8} = 135^{\circ}$ , i.e. the same as in a regular octagon. This means that this octagon, just like with a regular octagon, can be divided into squares (whose diagonals form $45^{\circ}$ angles) and right triangles.
In particular, as shown in the diagram below, the area of this octagon can be divided up into $5$ squares of side length $\frac{\sqrt{2}}{2}$ and $4$ right triangles, each of which has half the area of each of the squares (since each square has diagonal $\frac{\sqrt{2}}{2} \cdot \sqrt{2} = 1$ , so each right triangle is congruent by side-side-side to one of the triangles formed by slicing a square along one of its diagonals).
Therefore, the area of the octagon is equal to the area of $5 + 4 \cdot \frac{1}{2} = 7$ of the squares, and the area of each square is simply $\left(\frac{\sqrt{2}}{2}\right)^2 = \frac{1}{2}$ , so the answer is is $7 \cdot \frac{1}{2} = \boxed{\textbf{(A) } \frac{7}{2}}$ .
[asy] pair A=(0.5, 0), B=(0, 0.5), C=(0, 1.5), D=(0.5, 2), E=(1.5, 2), F=(2, 1.5), G=(2, 0.5), H=(1.5, 0); draw(A--B); draw(B--C); draw(C--D); draw(D--E);draw(E--F);draw(F--G); draw(G--H); draw(H--A);draw(A--F, blue);draw(E--B,blue);draw(C--H, blue); draw(D--G,blue);dot(A);dot(B);dot(C);dot(D);dot(E);dot(F);dot(G);dot(H); [/asy]

## Solution 2
Using the same diagram as in Solution 1, we can extend the sides of length $1$ to form a bounding square around the octagon, with the region inside the square but outside the octagon consisting of $4$ right triangles. (We could also extend the sides of length $\frac{\sqrt{2}}{2}$ to give a similar bounding square, but this would make the computations slightly harder.)
As in Solution 1, since all the interior angles of the octagon are $135^{\circ}$ , the right triangles are all $45^{\circ}-45^{\circ}-90^{\circ}$ triangles with hypotenuse $\frac{\sqrt{2}}{2}$ . Thus the length of their other legs is $\frac{\left(\frac{\sqrt{2}}{2}\right)}{\sqrt{2}} = \frac{1}{2}$ , so the bounding square has total side length $1 + 2 \cdot \frac{1}{2} = 2$ , and hence area $2^2 = 4$ . Each of the right triangles has area $\frac{1}{2} \cdot \left(\frac{1}{2}\right)^2 = \frac{1}{8}$ , so we deduce that the area of the octagon is $4 - 4 \cdot \frac{1}{8} = \boxed{\textbf{(A) } \frac{7}{2}}$ .
edited by mobius247

## Solution 3
As shown in the diagram below, we can also divide the octagon into squares and right triangles using horizontal and vertical lines, rather than the lines at a $45^{\circ}$ angle that were used in Solutions 1 and 2.
(Diagram made using Geogebra)
For the same reasons as in Solutions 1 and 2, the octagon's $135^{\circ}$ interior angles mean that the right triangles are $45^{\circ}-45^{\circ}-90^{\circ}$ triangles with hypotenuse $\frac{\sqrt{2}}{2}$ , so their other legs have length $\frac{\left(\frac{\sqrt{2}}{2}\right)}{\sqrt{2}} = \frac{1}{2}$ . Accordingly, their areas are each $\frac{1}{2} \cdot \left(\frac{1}{2}\right)^2 = \frac{1}{8}$ , while by symmetry, each of the squares also has side length $\frac{1}{2}$ , and thus area $\left(\frac{1}{2}\right)^2 = \frac{1}{4}$ .
Hence, as the octagon consists of $12$ squares and $4$ right triangles, its total area is $12\cdot\frac{1}{4}+4\cdot\frac{1}{8} = \boxed{\textbf{(A) } \frac{7}{2}}$ .
~JH. L

## Solution 4
We notice that we can draw four $45-45-90$ right triangles(each with side length $\frac{1}{2}$ ) and make the octagon a square with side length $2$ .
The area of the resulting square is $2^2 = 4$ . Additionally, the area of each extra triangle is $\frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$ , and so four of them would be $4 \cdot \frac{1}{8} = \frac{4}{8} = \frac{1}{2}$ . Therefore, the area of the octagon(which can be gotten by subtracting the area of the triangles from the area of the square) is $4 - \frac{1}{2} = \boxed{\textbf{(A) } \frac{7}{2}}$ .
~DearPrince

## Video Solution
https://youtu.be/rwPFZnYk9V8
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .