# 2013 AMC 10A Problem 22

## Problem

Six spheres of radius $1$ are positioned so that their centers are at the vertices of a regular hexagon of side length $2$ . The six spheres are internally tangent to a larger sphere whose center is the center of the hexagon. An eighth sphere is externally tangent to the six smaller spheres and internally tangent to the larger sphere. What is the radius of this eighth sphere?

$\textbf{(A)}\ \sqrt2\qquad\textbf{(B)}\ \frac{3}{2}\qquad\textbf{(C)}\ \frac{5}{3}\qquad\textbf{(D)}\ \sqrt3\qquad\textbf{(E)}\ 2$

## Solution 1
Set up an isosceles triangle between the center of the $8$ th sphere and two opposite ends of the hexagon. Then set up another triangle between the point of tangency of the $7$ th and $8$ th spheres, and the points of tangency between the $7$ th sphere and $2$ of the original spheres on opposite sides of the hexagon. Express each side length of the triangles in terms of $r$ (the radius of sphere $8$ ) and $h$ (the height of the first triangle). You can then use Pythagorean Theorem to set up two equations for the two triangles, and find the values of $h$ and $r$ .
$(1+r)^2=2^2+h^2$
$(3\sqrt{2})^2=3^2+(h+r)^2$
$r = \boxed{\textbf{(B) }\frac{3}{2}}$
Note: We can easily tell that h = 3-r because the line connecting the centers of the two opposite spheres is a diameter of the largest sphere and so intersects the center of the largest sphere, so the middle of this line is the center of the largest sphere. From this we know that the center of the line connected to the top of the 8th sphere is 3 and the height therefore is 3-r ~Srag

## Solution 2
We have a regular hexagon with side length $2$ and six spheres on each vertex with radius $1$ that are internally tangent, therefore, drawing radii to the tangent points would create this regular hexagon.
Imagine a 2D overhead view. There is a larger sphere which the $6$ spheres are internally tangent to, with the center in the center of the hexagon. To find the radius of the larger sphere we must first, either by prior knowledge or by deducing from the angle sum that the hexagon can be split into $6$ equilateral triangles from its vertices, that the radius is two more than the small radius, or $3$ .
[asy] draw(circle((0.5,0.866025404),0.5)); draw(circle((-0.5,0.866025404),0.5)); draw(circle((1,0),0.5)); draw(circle((-1,0),0.5)); draw(circle((0.5,-0.866025404),0.5)); draw(circle((-0.5,-0.866025404),0.5)); draw(circle((0,0),1.5)); draw((-0.5,0.866025404)--(0.5,0.866025404)); draw((-1,0)--(1,0)); draw((-0.5,-0.866025404)--(0.5,-0.866025404)); draw((-1,0)--(-0.5,0.866025404)); draw((-0.5,-0.866025404)--(0.5,0.866025404)); draw((0.5,-0.866025404)--(1,0)); draw((0.5,0.866025404)--(1,0)); draw((-0.5,0.866025404)--(0.5,-0.866025404)); draw((-1,0)--(-0.5,-0.866025404)); [/asy]
diagram made by erics118
Now imagine the figure in $3$ dimensions. The 8th sphere must be sitting atop of the $6$ spheres, which is the only possibility for it to be tangent to all the $6$ small spheres externally and the larger sphere internally. The ring of $6$ small spheres is symmetrical and the 8th sphere will be resting atop it with its center aligned with the diameter of the large sphere.
We can now create a right triangle with the legs being the line from a vertex of the hexagon to the center of the hexagon and the line from the center of the 7th sphere to the center of the 8th sphere. Let the radius of our 8th sphere be $r$ . As previously mentioned, the distance from the center of the hexagon to one of its vertices is $2$ . The distance between the centers will be $3-r$ . The hypotenuse will be $r+1$ .
We now have a right triangle. Applying the Pythagorean Theorem, $2^2+(3-r)^2=(1+r)^2$ . Expanding and solving for $r$ , we find $r=\frac{12}{8}=\boxed{\textbf{(B)}\frac{3}{2}}$ .

## Video Solution by Richard Rusczyk
https://www.youtube.com/watch?v=83JgSTi_0VE
hint: turn a 3D geometry problem into a 2D problem by taking cross-sections! Much easier to visualize.
What type of cross-section...? Well, that's in the video :D
~ dolphin7
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .