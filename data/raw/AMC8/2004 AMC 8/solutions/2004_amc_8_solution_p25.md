# 2004 AMC 8 Problem 25

## Problem

Two $4 \times 4$ squares intersect at right angles, bisecting their intersecting sides, as shown. The circle's diameter is the segment between the two points of intersection. What is the area of the shaded region created by removing the circle from the squares?

[asy] unitsize(6mm); draw(unitcircle); filldraw((0,1)--(1,2)--(3,0)--(1,-2)--(0,-1)--(-1,-2)--(-3,0)--(-1,2)--cycle,lightgray,black); filldraw(unitcircle,white,black); [/asy]

$\text{(A)}\ 16-4\pi\qquad \text{(B)}\ 16-2\pi \qquad \text{(C)}\ 28-4\pi \qquad \text{(D)}\ 28-2\pi \qquad \text{(E)}\ 32-2\pi$

## Solution 1
If the circle was shaded in, the intersection of the two squares would be a smaller square with half the sidelength, $2$ . The area of this region would be the two larger squares minus the area of the intersection, the smaller square. This is $4^2 + 4^2 - 2^2 = 28$ .
The diagonal of this smaller square created by connecting the two points of intersection of the squares is the diameter of the circle. This value can be found with Pythagorean or a $45^\circ - 45^\circ - 90^\circ$ circle to be $2\sqrt{2}$ . The radius is half the diameter, $\sqrt{2}$ . The area of the circle is $\pi r^2 = \pi (\sqrt{2})^2 = 2\pi$ .
The area of the shaded region is the area of the two squares minus the area of the circle which is $\boxed{\textbf{(D)}\ 28-2\pi}$ .

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=2824
~ pi_is_3.14
### See Also: