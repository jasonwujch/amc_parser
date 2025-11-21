# 2000 AMC 8 Problem 22

## Problem

A cube has edge length $2$ . Suppose that we glue a cube of edge length $1$ on top of the big cube so that one of its faces rests entirely on the top face of the larger cube. The percent increase in the surface area (sides, top, and bottom) from the original cube to the new solid formed is closest to

[asy] draw((0,0)--(2,0)--(3,1)--(3,3)--(2,2)--(0,2)--cycle); draw((2,0)--(2,2)); draw((0,2)--(1,3)); draw((1,7/3)--(1,10/3)--(2,10/3)--(2,7/3)--cycle); draw((2,7/3)--(5/2,17/6)--(5/2,23/6)--(3/2,23/6)--(1,10/3)); draw((2,10/3)--(5/2,23/6)); draw((3,3)--(5/2,3));[/asy]

$\text{(A)}\ 10\qquad\text{(B)}\ 15\qquad\text{(C)}\ 17\qquad\text{(D)}\ 21\qquad\text{(E)}\ 25$

## Solution
The original cube has $6$ faces, each with an area of $2\cdot 2 = 4$ square units. Thus the original figure had a total surface area of $24$ square units.
The new figure has the original surface, with $6$ new faces that each have an area of $1$ square unit, for a total surface area of $6$ additional square units added to it. But $1$ square unit of the top of the bigger cube, and $1$ square unit on the bottom of smaller cube, is not on the surface, and does not count towards the surface area.
The total surface area is therefore $24 + 6 - 1 - 1 = 28$ square units.
The percent increase in surface area is $\frac{SA_{new} - SA_{old}}{SA_{old}}\cdot 100\% = \frac{28-24}{24}\cdot 100\% \approx 16.67\%$ , giving the closest answer as $\boxed{C}$ .

## Video Solution
https://www.youtube.com/watch?v=X5T02J3eNqM ~David
### See Also