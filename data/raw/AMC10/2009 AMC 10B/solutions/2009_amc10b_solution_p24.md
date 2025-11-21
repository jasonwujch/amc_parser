# 2009 AMC 10B Problem 24

## Problem

The keystone arch is an ancient architectural feature. It is composed of congruent isosceles trapezoids fitted together along the non-parallel sides, as shown. The bottom sides of the two end trapezoids are horizontal. In an arch made with $9$ trapezoids, let $x$ be the angle measure in degrees of the larger interior angle of the trapezoid. What is $x$ ?

[asy] unitsize(4mm); defaultpen(linewidth(.8pt)); int i; real r=5, R=6; path t=r*dir(0)--r*dir(20)--R*dir(20)--R*dir(0); for(i=0; i<9; ++i) { draw(rotate(20*i)*t); } draw((-r,0)--(R+1,0)); draw((-R,0)--(-R-1,0)); [/asy]

$\text{(A) } 100 \qquad \text{(B) } 102 \qquad \text{(C) } 104 \qquad \text{(D) } 106 \qquad \text{(E) } 108$

## Solution 1
Extend all the legs of the trapezoids. They will all intersect in the middle of the bottom side of the picture, forming the situation shown below.
[asy] unitsize(6mm); defaultpen(linewidth(.8pt)); int i; real r=5, R=6; path t=r*dir(0)--r*dir(20)--R*dir(20)--R*dir(0); for(i=0; i<9; ++i) { draw(rotate(20*i)*t); } draw((-r,0)--(R+1,0)); draw((-R,0)--(-R-1,0)); for (int i=1; i<9; ++i) draw( (0,0) -- (rotate(20*i)*(r,0)), dotted ); label("$X$",(0,0),S); label("$Y$",(R,0),SE); label("$Z$",rotate(20)*(R,0),ENE); draw( arc( (0,0), (1.5,0), rotate(20)*(1.5,0) ) ); label("$20^\circ$", rotate(10)*(1.75,0), E ); [/asy]
Each of the angles at $X$ is $\frac{180^\circ}9 = 20^\circ$ . From $\triangle XYZ$ , the degree measure of the smaller interior angle of the trapezoid is $\frac{180^\circ - 20^\circ}2 = 80^\circ$ , hence the degree measure of the larger interior angle is $180^\circ - 80^\circ = \boxed{100^\circ \Longrightarrow A}$ .
Proof that all the extended trapezoid legs intersect at the same point: It is sufficient to prove this for any pair of neighboring trapezoids. For two neighboring trapezoids, the situation is symmetric according to their common leg, therefore the extensions of both outside legs intersect the extension of the common leg at the same point, Q.E.D.
Knowing this, we can now easily see that the intersection point must be on the bottom side of our picture, as it lies on the bottom leg of the rightmost trapezoid. And by symmetry the point must be in the center of this side.

## Solution 2
A decagon can be formed from the trapezoids and the base. The sum of the decagon's angles is $180(10-2)=1440^\circ$ . Letting the larger angle in each trapezoid be $x$ , the two angles formed by the line each measures $(180-x)^\circ$ . There are $8$ congruent angles left. Each of those angles measures $(360-2x)^\circ$ . Putting it all together: $8(360-2x)+2(180-x)=1440\implies x=\boxed{\mathrm{(A)\ }100^\circ}$ .

## Solution 3
If we reflect the arch across the line, we form an 18-gon. $\frac{180*(18-2)}{18} = 160^\circ$ so each interior angle of the 18-gon is $160^\circ$ . Let $x$ be the degree measure of the larger interior angle of a trapezoid. From the diagram, we see that $2x + 160 = 360$ , so $2x = 200$ and $x = 100$ , or $\boxed{A}$ .

## Video Solution by OmegaLearn
https://youtu.be/FDgcLW4frg8?t=1914
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .