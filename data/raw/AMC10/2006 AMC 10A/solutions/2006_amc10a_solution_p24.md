# 2006 AMC 10A Problem 24

## Problem

Centers of adjacent faces of a unit cube are joined to form a regular octahedron . What is the volume of this octahedron?

$\textbf{(A) } \frac{1}{8}\qquad\textbf{(B) } \frac{1}{6}\qquad\textbf{(C) } \frac{1}{4}\qquad\textbf{(D) } \frac{1}{3}\qquad\textbf{(E) } \frac{1}{2}\qquad$

## Solution
We can break the octahedron into two square pyramids by cutting it along a plane perpendicular to one of its internal diagonals. [asy] import three; real r = 1/2; triple A = (-0.5,1.5,0); size(400); currentprojection=orthographic(1,1/4,1/2); draw((0,0,0)--(1,0,0)--(1,1,0)--(0,1,0)--(0,0,0)^^(0,0,1)--(1,0,1)--(1,1,1)--(0,1,1)--(0,0,1)^^(0,0,0)--(0,0,1)^^(1,0,0)--(1,0,1)^^(0,1,0)--(0,1,1)^^(1,1,0)--(1,1,1),gray(0.8)); draw((0,r,r)--(r,1,r)--(1,r,r)--(r,0,r)--cycle^^(r,r,0)--(0,r,r)--(r,r,1)--(r,1,r)--(r,r,0)--(1,r,r)--(r,r,1)--(r,0,r)--(r,r,0)); draw((0,r,r)+A--(r,1,r)+A--(1,r,r)+A--(r,0,r)+A--cycle^^(0,r,r)+A--(r,r,1)+A--(1,r,r)+A^^(r,1,r)+A--(r,r,1)+A--(r,0,r)+A); [/asy] The cube has edges of length 1 so all edges of the regular octahedron have length $\frac{\sqrt{2}}{2}$ . Then the square base of the pyramid has area $\left(\frac{1}{2}\sqrt{2}\right)^2 = \frac{1}{2}$ . We also know that the height of the pyramid is half the height of the cube, so it is $\frac{1}{2}$ . The volume of a pyramid with base area $B$ and height $h$ is $A=\frac{1}{3}Bh$ so each of the pyramids has volume $\frac{1}{3}\left(\frac{1}{2}\right)\left(\frac{1}{2}\right) = \frac{1}{12}$ . The whole octahedron is twice this volume, so $\frac{1}{12} \cdot 2 = \boxed{\textbf{(B) }\frac{1}{6}}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .