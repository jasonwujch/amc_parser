# 2007 AMC 10A Problem 21

## Problem

A sphere is inscribed in a cube that has a surface area of $24$ square meters. A second cube is then inscribed within the sphere. What is the surface area in square meters of the inner cube?

$\text{(A)}\ 3 \qquad \text{(B)}\ 6 \qquad \text{(C)}\ 8 \qquad \text{(D)}\ 9 \qquad \text{(E)}\ 12$

## Solution

## Solution 1
We rotate the smaller cube around the sphere such that two opposite vertices of the cube are on opposite faces of the larger cube. Thus the main diagonal of the smaller cube is the side length of the outer square.
Let $S$ be the surface area of the inner square. The ratio of the areas of two similar figures is equal to the square of the ratio of their sides. As the diagonal of a cube has length $s\sqrt{3}$ where $s$ is a side of the cube, the ratio of a side of the inner square to a side of the outer square is $\frac{1}{\sqrt{3}}$ (since the side of the outer square = the diagonal of the inner square). So we have $\frac{S}{24} = \left(\frac{1}{\sqrt{3}}\right)^2$ . Thus $S = 8\Rightarrow \mathrm{\boxed{(C)}}$ .

## Solution 2 (computation)
The area of each face of the outer cube is $\frac {24}{6} = 4$ , and the edge length of the outer cube is $2$ . This is also the diameter of the sphere, and thus the length of a long diagonal of the inner cube.
A long diagonal of a cube is the hypotenuse of a right triangle with a side of the cube and a face diagonal of the cube as legs. If a side of the cube is $x$ , we see that $2 = \sqrt {x^{2} + (\sqrt {2}x)^{2}}\Rightarrow x = \frac {2}{\sqrt {3}}$ .
Thus the surface area of the inner cube is $6x^{2} = 6\left(\frac {2}{\sqrt {3}}\right )^{2} = 8$ .

## Solution 3, from AoPS
Since the surface area of the original cube is 24 square meters, each face of the cube has a surface area of $24/6 = 4$ square meters, and the side length of this cube is 2 meters. The sphere inscribed within the cube has diameter 2 meters, which is also the length of the diagonal of the cube inscribed in the sphere. Let $l$ represent the side length of the inscribed cube. Applying the Pythagorean Theorem twice gives \[l^2 + l^2 + l^2 = 2^2 = 4.\] Hence each face has surface area \[l^2 = \frac{4}{3} \ \text{square meters}.\] So the surface area of the inscribed cube is $6\cdot \frac43 = \boxed{8}$ square meters.

## Solution 4
First of all, it is pretty easy to see the length of each edge of the bigger cube is $2$ so the radius of the sphere is $1$ . We know that when a cube is inscribed in a sphere, assuming the edge length of the square is $x$ the radius can be presented as $\frac {\sqrt3x}{2} = 1$ , we can solve that $x=\frac {2\sqrt3}{3}$ and now we only need to apply the basic formula to find the surface and we got our final answer as $\frac {2\sqrt3}{3}*\frac {2\sqrt3}{3}*6=8$ and the final answer is $\boxed{C}$

## Video Solution
https://www.youtube.com/watch?v=YCDbpU9EX4w ~David
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .