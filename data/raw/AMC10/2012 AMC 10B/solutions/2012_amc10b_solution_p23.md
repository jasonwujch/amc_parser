# 2012 AMC 10B Problem 23

## Problem

A solid tetrahedron is sliced off a solid wooden unit cube by a plane passing through two nonadjacent vertices on one face and one vertex on the opposite face not adjacent to either of the first two vertices. The tetrahedron is discarded and the remaining portion of the cube is placed on a table with the cut surface face down. What is the height of this object?

$\textbf{(A)}\ \frac{\sqrt{3}}{3} \qquad\textbf{(B)}\ \frac{2 \sqrt{2}}{3}\qquad\textbf{(C)}\ 1\qquad\textbf{(D)}\ \frac{2 \sqrt{3}}{3}\qquad\textbf{(E)}\ \sqrt{2}$

## Solution 1
This tetrahedron has the 4 vertices in these positions: on a corner (let's call this $A$ ) of the cube, and the other three corners ( $B$ , $C$ , and $D$ ) adjacent to this corner. We can find the height of the remaining portion of the cube by finding the height of the tetrahedron. We can find the height of this tetrahedron in perspective to the equilateral triangle base (we call this height $x$ ) by finding the volume of the tetrahedron in two ways. $\frac{1 \times 1}{2}$ is the area of the isosceles base of the tetrahedron. Multiply by the height, $1$ , and divide by $3$ , we have the volume of the tetrahedron as $\frac{1}{6}$ . We set this area equal to one-third the product of our desired height and the area of the equilateral triangle base. First, find the area of the equilateral triangle: $[BCD]=\frac{\sqrt{2}^2 \times \sqrt{3}}{4}=\frac{\sqrt{3}}{2}$ . So we have: $\frac{1}{3} \cdot \frac{\sqrt{3}}{2} \cdot x=\frac{1}{6}$ , and so $x=\frac{\sqrt{3}}{3}$ .
Since we know what the height is, we can find the height of the remaining structure. The height of the structure if the tetrahedron was still on would simply be the space diagonal of the cube, $\sqrt{3}$ , so we just subtract $\frac{\sqrt{3}}{3}$ from $\sqrt{3}$ to get $\frac{2\sqrt{3}}{3}$ , or $\boxed{\textbf{(D)}}.$

## Solution 2
We can write the volume of a tetrahedron as $\frac{Bh}{3}$ and revise the formula for the volume of a cube to be $Bh$ . Also note that the height of the tetrahedron goes through the space diagonal of the cube. So, the remaining part of the cube's space diagonal should be $\frac{2}{3}$ of the original space diagonal. Hence, the length is $\boxed{\textbf{(D)} \: \frac{2\sqrt{3}}{3}}$

## Solution 3
Plot the cube $ABCDEFGH$ (let's call it this)on a $3-D$ cartesian coordinate system so that the two bottom vertices(C and D) of the face at the very front(and on the y-z plane) are on the y-axis. Cut out the tetrahedron from the cube. Its $4$ vertices are $A$ , $B$ , $D$ and $E.$ Therefore, corner A has now vanished. The coordinate of corner C is $(0,0,0)$ , $E(1,0,1)$ , $B(0,1,1)$ , and $H(1,1,0)$ . Since we are trying to figure out the height of the object, we have to determine which corner is the farthest away from the cut surface. It is corner $H$ , and the height of the object is the distance between the center of mass of the cut surface and corner $H$ . The center of mass of the cut surface is $G(1/3, 1/3, 2/3)$ . Using the distance between two points formula, the height of the object $\sqrt{(1-\frac{1}{3})^{2}+(1-\frac{1}{3})^{2}+(0-\frac{2}{3})^{2}}=\sqrt{\frac{12}{9}}=\frac{2\sqrt{3}}{3}$ . Therefore the answer is $\boxed{\textbf{(D)}}.$

## Solution 4
[asy]import three; draw((1,1,1)--(1,0,1)--(1,0,0)--(0,0,0)--(0,0,1)--(0,1,1)--(1,1,1)--(1,1,0)--(0,1,0)--(0,1,1)); draw((0,0,1)--(1,0,1)); draw((1,0,0)--(1,1,0)); draw((0,0,0)--(0,1,0)); label("A",(0,0,0),S); label("B",(1,0,0),W); label("C",(0,0,1),N); label("D",(1,0,1),NW); label("E",(1,1,0),S); label("F",(0,1,0),E); label("G",(1,1,1),SE); label("H",(0,1,1),NE); [/asy]
We can approach this problem similar to the solution above, by attacking it on the Cartesian plane. As mentioned before, it has been proved that the space diagonal intersects the centroid of triangle $BGF$ (I have defined the tetrahedron as cutting through points $B$ , $G$ , $F$ , and $E$ ). We can label $E$ as $(0, 0, 0)$ , $F$ as $(1, 0, 0)$ , $B$ as $(0, 1, 0)$ , and $G$ as $(0, 0, 1)$ . Therefore, the centroid of triangle $BGF$ would be the average of these three points, or ( $\frac{1}{3}$ , $\frac{1}{3}$ , $\frac{1}{3}$ ). Since $C$ is defined as $(1, 1, 1)$ , and the intersection point passes through ( $\frac{1}{3}$ , $\frac{1}{3}$ , $\frac{1}{3}$ ) (or one-third of the space diagonal), we can conclude that the altitude is $\boxed{\textbf{(D)}}$ , or $\frac{2}{3}$ of $\sqrt3$ .

## Video Solution 1 by Pi Academy
https://youtu.be/Kx0e33xjgk0?si=P9WffaUBIM_DwNUm ~ Pi Academy

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012amc10b/268
(Direct Youtube Link) https://www.youtube.com/watch?v=3mItG-TtR74
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .