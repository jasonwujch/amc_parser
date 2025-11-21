# 2020 AIME I Problem 6

## Problem

A flat board has a circular hole with radius $1$ and a circular hole with radius $2$ such that the distance between the centers of the two holes is $7.$ Two spheres with equal radii sit in the two holes such that the spheres are tangent to each other. The square of the radius of the spheres is $\tfrac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(300); import graph3; import solids; currentprojection=orthographic((1,-5,1)); real r = sqrt(160/13); triple C1, C2, B1, B2; C1 = (0,0,sqrt(r^2-1^2)); C2 = (7,0,sqrt(r^2-2^2)); B1 = (0,0,0); B2 = (7,0,0); draw((-5,-10,0)--(-5,10,0)--(12,10,0)--(12,-10,0)--cycle); draw(shift(C1)*scale3(r)*unitsphere,yellow,light=White); draw(shift(C2)*scale3(r)*unitsphere,yellow,light=White); draw(Circle(B1,1,(0,0,1))); draw(Circle(B2,2,(0,0,1))); dot(C1^^C2^^B1^^B2,linewidth(4.5)); [/asy] ~MRENTHUSIASM

## Solution 1 (Pythagorean Theorem)
[asy] size(10cm); pair A, B, C, D, O, P, H, L, X, Y; A = (-1, 0); B = (1, 0); H = (0, 0); C = (5, 0); D = (9, 0); L = (7, 0); O = (0, sqrt(160/13 - 1)); P = (7, sqrt(160/13 - 4)); X = (0, sqrt(160/13 - 4)); Y = (O + P) / 2; draw(A -- O -- B -- cycle); draw(C -- P -- D -- cycle); draw(B -- C); draw(O -- P); draw(P -- X, dashed); draw(O -- H, dashed); draw(P -- L, dashed); draw(circle(O, sqrt(160/13))); draw(circle(P, sqrt(160/13))); path b = brace(L-(0,1), H-(0,1),0.5); draw(b); label("$r$", O -- Y, N); label("$r$", Y -- P, N); label("$r$", O -- A, NW); label("$r$", P -- D, NE); label("$1$", A -- H, N); label("$2$", L -- D, N); label("$7$", b, S); dot(A^^B^^C^^D^^O^^P^^H^^L^^X^^Y,linewidth(4)); [/asy] Set the common radius to $r$ . First, take the cross section of the sphere sitting in the hole of radius $1$ . If we draw the perpendicular bisector of the chord (the hole) through the circle, this line goes through the center. Connect the center also to where the chord hits the circle, for a right triangle with hypotenuse $r$ and base $1$ . Therefore, the height of this circle outside of the hole is $\sqrt{r^2-1}$ .
The other circle follows similarly for a height (outside the hole) of $\sqrt{r^2-4}$ . Now, if we take the cross section of the entire board, essentially making it two-dimensional, we can connect the centers of the two spheres, then form another right triangle with base $7$ , as given by the problem. The height of this triangle is the difference between the heights of the parts of the two spheres outside the holes, which is $\sqrt{r^2-1} - \sqrt{r^2-4}$ . Now we can set up an equation in terms of $r$ with the Pythagorean theorem: \[\left(\sqrt{r^2-1} - \sqrt{r^2-4}\right)^2 + 7^2 = (2r)^2.\] Simplifying a few times, \begin{align*} r^2 - 1 - 2\left(\sqrt{(r^2-1)(r^2-4)}\right) + r^2 - 4 + 49 &= 4r^2 \\ 2r^2-44 &= -2\left(\sqrt{(r^2-1)(r^2-4)}\right) \\ 22-r^2 &= \left(\sqrt{r^4 - 5r^2 + 4}\right) \\ r^4 -44r^2 + 484 &= r^4 - 5r^2 + 4 \\ 39r^2&=480 \\ r^2&=\frac{480}{39} = \frac{160}{13}. \end{align*} Therefore, our answer is $\boxed{173}$ .
~molocyxu

## Solution 2 (Tangential Distance)
Let $A$ and $B$ be the centers of the holes, let $C$ be the point of crossing $AB$ and radical axes of the circles. So $C$ has equal tangential distance to any point of both spheres. In particular to the circles ( https://en.wikipedia.org/wiki/Radical_axis .)
\[CA = \frac {AB} {2} – \frac {r_A^2 – r_B^2}{2 AB} = \frac{23}{7}, CB = AB - AC =\frac{26}{7},\] \[CA' = CB'= \sqrt{BC^2 – r_B^2} = \frac {4}{7} \sqrt{30}.\]
Let $D$ be the point of tangency of the spheres common radius $R$ centered at $O$ and $O'.$ Let $\alpha$ be the angle between $OO'$ and flat board. In the plane, perpendicular to board \[DC \perp OO', DC = \frac {4}{7} \sqrt{30}.\]
Distance between $C$ and midpoint $M$ of $AB$ is \[d = \frac {26}{7} - \frac {7}{2} = \frac{3}{14} \implies \sin \alpha = \frac {d}{DC} = \frac {3}{8\sqrt {30}}.\] \[\cos \alpha = \sqrt {1 – \frac {9}{64 \cdot 30}} = \sqrt{ \frac {637}{640}} = \frac {7}{2} \sqrt {\frac{13}{160}}.\] \[2R \cos \alpha = AB = 7 \implies R = \frac {\frac{7}{2} } {\frac{7}{2}\sqrt \frac{13}{160}} = \sqrt {\frac{160}{13}}.\] Hence the answer is \[160+13 = \boxed{173}.\] vladimir.shelomovskii@gmail.com, vvsss

## Video solution (With Animation)
https://youtu.be/cOf9uTJ9J40

## Video Solution
https://www.youtube.com/watch?v=qCTq8KhZfYQ
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .