# 2015 AIME II Problem 9

## Problem

A cylindrical barrel with radius $4$ feet and height $10$ feet is full of water. A solid cube with side length $8$ feet is set into the barrel so that the diagonal of the cube is vertical. The volume of water thus displaced is $v$ cubic feet. Find $v^2$ .

[asy] import three; import solids; size(5cm); currentprojection=orthographic(1,-1/6,1/6); draw(surface(revolution((0,0,0),(-2,-2*sqrt(3),0)--(-2,-2*sqrt(3),-10),Z,0,360)),white,nolight); triple A =(8*sqrt(6)/3,0,8*sqrt(3)/3), B = (-4*sqrt(6)/3,4*sqrt(2),8*sqrt(3)/3), C = (-4*sqrt(6)/3,-4*sqrt(2),8*sqrt(3)/3), X = (0,0,-2*sqrt(2)); draw(X--X+A--X+A+B--X+A+B+C); draw(X--X+B--X+A+B); draw(X--X+C--X+A+C--X+A+B+C); draw(X+A--X+A+C); draw(X+C--X+C+B--X+A+B+C,linetype("2 4")); draw(X+B--X+C+B,linetype("2 4")); draw(surface(revolution((0,0,0),(-2,-2*sqrt(3),0)--(-2,-2*sqrt(3),-10),Z,0,240)),white,nolight); draw((-2,-2*sqrt(3),0)..(4,0,0)..(-2,2*sqrt(3),0)); draw((-4*cos(atan(5)),-4*sin(atan(5)),0)--(-4*cos(atan(5)),-4*sin(atan(5)),-10)..(4,0,-10)..(4*cos(atan(5)),4*sin(atan(5)),-10)--(4*cos(atan(5)),4*sin(atan(5)),0)); draw((-2,-2*sqrt(3),0)..(-4,0,0)..(-2,2*sqrt(3),0),linetype("2 4")); [/asy]

## Solution 1
Our aim is to find the volume of the part of the cube submerged in the cylinder. In the problem, since three edges emanate from each vertex, the boundary of the cylinder touches the cube at three points. Because the space diagonal of the cube is vertical, by the symmetry of the cube, the three points form an equilateral triangle. Because the radius of the circle is $4$ , by the Law of Cosines, the side length s of the equilateral triangle is
\[s^2 = 2\cdot(4^2) - 2\cdot(4^2)\cos(120^{\circ}) = 3(4^2)\]
so $s = 4\sqrt{3}$ .* Again by the symmetry of the cube, the volume we want to find is the volume of a tetrahedron with right angles on all faces at the submerged vertex, so since the lengths of the legs of the tetrahedron are $\frac{4\sqrt{3}}{\sqrt{2}} = 2\sqrt{6}$ (the three triangular faces touching the submerged vertex are all $45-45-90$ triangles) so
\[v = \frac{1}{3}(2\sqrt{6})\left(\frac{1}{2} \cdot (2\sqrt{6})^2\right) = \frac{1}{6} \cdot 48\sqrt{6} = 8\sqrt{6}\]
so
\[v^2 = 64 \cdot 6 = \boxed{384}.\]
In this case, our base was one of the isosceles triangles (not the larger equilateral one). To calculate volume using the latter, note that the height would be $2\sqrt{2}$ .
- Note that in a 30-30-120 triangle, side length ratios are $1:1:\sqrt{3}$ .
- Or, note that the altitude and the centroid of an equilateral triangle are the same point, so since the centroid is 4 units from the vertex (which is $\frac{2}{3}$ the length of the median), the altitude is 6, which gives a hypotenuse of $\frac{12}{\sqrt{3}}=4\sqrt{3}$ by $1:\frac{\sqrt{3}}{2}:\frac{1}{2}$ relationship for 30-60-90 triangles.

## Solution 2 (No trig)
Visualizing the corner which is submerged in the cylinder, we can see that it's like slicing off a corner, where they slice an equal part off every edge, to make a tetrahedron where there are 3 right isosceles triangles and one equilateral triangle. With this out of the way, we can now just find the area of that equilateral triangle, using the fact that the circle of radius $4$ is the circumcircle of the equilateral triangle. Using equilateral triangle properties, you can find that the height of the triangle is $6$ , and the side length is $\frac{6}{\sqrt{3}}=2\sqrt{3} \cdot 2=4\sqrt{3}$ . As the other faces are right isosceles triangles, they are $\frac{4\sqrt{3}}{\sqrt{2}}=2\sqrt{6}$ . Therefore the volume of this tetrahedron is
\[\left(\frac{2\sqrt{6}}{2}\right)^2=12 \ \cdot \ (2\sqrt{6})=24\sqrt{6} \implies \frac{24\sqrt{6}}{3}=8\sqrt{6} \implies (8\sqrt{6})^2=\boxed{384}\]
-dragoon
-lpieleanu (minor latex changes)
Note: The height of the cylinder and the side length of the cube had no effect on the result of the problem.
Note 2: If this doesn’t make sense, just imagine slicing a corner off a cube.

## Solution 3 (Also trig-less)
We can use the same method as in Solution 2 to find the side length of the equilateral triangle, which is $4\sqrt3$ . From here, its area is \[\dfrac{\bigl(4\sqrt3\bigr)^2\sqrt3}4=12\sqrt3.\] The leg of the isosceles right triangle is $\dfrac{4\sqrt3}{\sqrt2}=2\sqrt6$ , and the horizontal distance from the vertex to the base of the tetrahedron is $4$ (the radius of the cylinder), so we can find the height, as shown in the diagram. [asy] import olympiad; pair V, T, B; V = (-4, 0); B = origin; T = (0, 2*sqrt(2)); draw(V--B--T--cycle); draw(rightanglemark(V, B, T)); label("Vertex", V, W); label("Tip", T, N); label("Base", B, SE); label("$4$", V--B, S); label("$2\sqrt6$", V--T, NW); [/asy] The height from the tip to the base is $2\sqrt2$ , so the volume is $\dfrac{12\sqrt3\cdot2\sqrt2}3=8\sqrt6$ , and thus the answer is $\boxed{384}$ .
-integralarefun

## Solution 4 (De Gua's, no trig)
Since the diagonal is perpendicular to the base of the cylinder, all three edges and faces can be treated symmetrically.
The cross-section of the cube with the top face of the cylinder is an equilateral triangle inscribed in a circle with radius $4$ . This means the medians of the triangle have length $\frac{3}{2} \cdot 4=6$ , because the circumcenter is also the centroid, and the centroid divides the medians into lengths of ratio $2:1$ . Using $30-60-90$ triangles, the side length of the triangle is $4\sqrt{3}$ , and its area is $\frac{(4\sqrt{3})^2\sqrt{3}}{4}=12\sqrt{3}$ .
Next, consider the submerged triangular sections of the faces. Each is a $45-45-90$ triangle with leg length $x$ . The area of each is then $\frac{x^2}{2}$ . By De Gua's Theorem on the submerged pyramid (which we can apply because it has a right-angled corner), $3\left( \frac{x^2}{2} \right) ^2=(12\sqrt{3})^2$ . Solving yields $x=2\sqrt{6}$ .
The height of the pyramid is then $\sqrt{(2\sqrt{6})^2-4^2}=2\sqrt{2}$ , by the Pythagorean Theorem (using the slant height and circumradius). The volume is then $v=\frac{1}{3}\cdot 12\sqrt{3} \cdot 2\sqrt{2}=8\sqrt{6}$ , and the requested answer is $v^2=(8\sqrt{6})^2=\boxed{384}$ . ~bad_at_mathcounts

## Solution 5(Similarity)
First, note the diagonal is vertical so that the tetrahedron of cube in water is similar to the largest tetrahedron in the bottom of this cube. So we are trying to find their volume ratio by discovering their side length ration.
In the equilateral triangle at the cylinder's top, we can find its side is \[s_{1} = 2 * R * \sin(60^{\circ}) = 4\sqrt{3}\] as the base side of this tetrahedron.
For the largest tetrahedron in the cube, its side length is just \[s_{2} = 8\sqrt{2}\] a diagonal of one of the face. And its volume is \[v_{2} = 8 * 8 * \frac{1}{2} * 8 * \frac{1}{3} = \frac{8^3}{6}\] .
Therefore, \[v_{1} = v_{2} * (\frac{s_{1}}{s_{2}})^3 = 8\sqrt{6}\] \[v_{1}^2 = 384\]
~DRA777

## Video Solution by Punxsutawney Phil
https://youtube.com/watch?v=Zmilbjm382A
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .