# 2015 AMC 10B Problem 17

## Problem

The centers of the faces of the right rectangular prism shown below are joined to create an octahedron. What is the volume of this octahedron?

[asy] import three; size(2inch); currentprojection=orthographic(4,2,2); draw((0,0,0)--(0,0,3),dashed); draw((0,0,0)--(0,4,0),dashed); draw((0,0,0)--(5,0,0),dashed); draw((5,4,3)--(5,0,3)--(5,0,0)--(5,4,0)--(0,4,0)--(0,4,3)--(0,0,3)--(5,0,3)); draw((0,4,3)--(5,4,3)--(5,4,0)); label("3",(5,0,3)--(5,0,0),W); label("4",(5,0,0)--(5,4,0),S); label("5",(5,4,0)--(0,4,0),SE); [/asy]

$\textbf{(A) } \dfrac{75}{12} \qquad\textbf{(B) } 10 \qquad\textbf{(C) } 12 \qquad\textbf{(D) } 10\sqrt2 \qquad\textbf{(E) } 15$

## Solution 1
The octahedron is just two congruent pyramids glued together by their base. The base of one pyramid is a rhombus with diagonals $4$ and $5$ , for an area $A=10$ . The height $h$ , of one pyramid, is $\frac{3}{2}$ , so the volume of one pyramid is $\frac{Ah}{3}=5$ . Thus, the octahedron has volume $2\cdot5=\boxed{\textbf{(B) }10}$

## Solution 2 (Scaling)
The "base" of the octahedron is half the base of the rectangular prism because it is connected by the midpoints. Additionally, the volume of an octahedron is $\dfrac{1}{3}$ of its respective prism. Thus, the octahedron's volume is $\dfrac{1}{2} \cdot \dfrac{1}{3} = \dfrac{1}{6}$ of the rectangular prism's volume, meaning that the answer is $3 \cdot 4 \cdot 5 \cdot \dfrac{1}{6} = \boxed{\\10}$

## Video Solution
https://www.youtube.com/watch?v=NEQNfr_T8OA
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .