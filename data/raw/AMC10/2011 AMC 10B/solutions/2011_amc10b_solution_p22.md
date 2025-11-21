# 2011 AMC 10B Problem 22

## Problem

A pyramid has a square base with sides of length $1$ and has lateral faces that are equilateral triangles. A cube is placed within the pyramid so that one face is on the base of the pyramid and its opposite face has all its edges on the lateral faces of the pyramid. What is the volume of this cube?

$\textbf{(A)}\ 5\sqrt{2} - 7 \qquad\textbf{(B)}\ 7 - 4\sqrt{3} \qquad\textbf{(C)}\ \frac{2\sqrt{2}}{27} \qquad\textbf{(D)}\ \frac{\sqrt{2}}{9} \qquad\textbf{(E)}\ \frac{\sqrt{3}}{9}$

## Solution 1
It is often easier to first draw a diagram for such a problem.
Sometimes, it may also be easier to think of the problem in 2D. Take a cross section of the pyramid through the apex and two points from the base that are opposite to each other. Place it in two dimensions.
The dimensions of this triangle are $1, 1,$ and $\sqrt{2}$ because the sidelengths of the pyramid are $1$ and the base of the triangle is the diagonal of the pyramid's base. This is a $45-45-90$ triangle. Also, we can let the dimensions of the rectangle be $s$ and $s\sqrt{2}$ because the longer length was the diagonal of the cube's base and the shorter length was a side of the cube.
The two triangles on the right and left of the rectangle are also $45-45-90$ triangles because the rectangle is perpendicular to the base, and they share a $45^\circ$ angle with the larger triangle. Therefore, the legs of the right triangles can be expressed as $s.$
Now we can just use segment addition to find the value of $s.$ \[\sqrt{2}=s+s\sqrt{2}+s=2s+s\sqrt{2}=(2+\sqrt{2})s\] \[s=\frac{\sqrt{2}}{2+\sqrt{2}}=\frac{1}{\sqrt{2}+1}=\frac{\sqrt{2}-1}{2-1}=\sqrt{2}-1\]
The volume of the cube is $s^3 = (\sqrt{2}-1)^3 = (\sqrt{2}-1)(3-2\sqrt{2}) = 3\sqrt{2}-3-4+2\sqrt{2} = \boxed{\textbf{(A)} 5\sqrt{2}-7}$

## Solution 2
Let $s$ be the slant height and $d$ be the distance from one side of the base to the point right under the apex. Then using the Pythagorean Theorem, the altitude from the apex to the base is \[a=\sqrt{s^2-d^2}=\sqrt{\left(\dfrac{\sqrt{3}}{2}\right)^2-\left(\dfrac{1}{2}\right)^2}=\dfrac{\sqrt{2}}{2}\] Notice that the smaller pyramid on top of the cube is similar to the larger pyramid. Thus, letting $x$ be the edge length of the cube, then the altitude of the smaller pyramid is $\dfrac{\sqrt{2}}{2}\cdot{\dfrac{x}{1}}=\dfrac{\sqrt{2}}{2}x$ .
Since the altitude of the larger pyramid is the sum of the edge length of the cube and the altitude of the smaller pyramid, we have \[\dfrac{\sqrt{2}}{2}=x+\dfrac{\sqrt{2}}{2}x\] \[x=\sqrt{2}-1\]
Finally, $V_{cube}=x^3=(\sqrt{2}-1)^3=\boxed{\textbf{(A)} 5\sqrt{2}-7}$
~ Nafer (Minor edits by anonymous)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .