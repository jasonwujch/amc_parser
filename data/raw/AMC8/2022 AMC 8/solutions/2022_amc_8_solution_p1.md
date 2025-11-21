# 2022 AMC 8 Problem 1

## Problem

The Math Team designed a logo shaped like a multiplication symbol, shown below on a grid of 1-inch squares. What is the area of the logo in square inches?

[asy] defaultpen(linewidth(0.5)); size(5cm); defaultpen(fontsize(14pt)); label("$\textbf{Math}$", (2.1,3.7)--(3.9,3.7)); label("$\textbf{Team}$", (2.1,3)--(3.9,3)); filldraw((1,2)--(2,1)--(3,2)--(4,1)--(5,2)--(4,3)--(5,4)--(4,5)--(3,4)--(2,5)--(1,4)--(2,3)--(1,2)--cycle, mediumgray*0.5 + lightgray*0.5); draw((0,0)--(6,0), gray); draw((0,1)--(6,1), gray); draw((0,2)--(6,2), gray); draw((0,3)--(6,3), gray); draw((0,4)--(6,4), gray); draw((0,5)--(6,5), gray); draw((0,6)--(6,6), gray); draw((0,0)--(0,6), gray); draw((1,0)--(1,6), gray); draw((2,0)--(2,6), gray); draw((3,0)--(3,6), gray); draw((4,0)--(4,6), gray); draw((5,0)--(5,6), gray); draw((6,0)--(6,6), gray); [/asy]

$\textbf{(A) } 10 \qquad \textbf{(B) } 12 \qquad \textbf{(C) } 13 \qquad \textbf{(D) } 14 \qquad \textbf{(E) } 15$

## Solution 1 (A quick solution.)
We can see that there are 4 whole squares, since the area of each square will be 1, 4 * 1 = 4. Next, there are 12 half squares, and 2 half squares are 1 whole square, so 12/2 = 6 whole squares. The area of this will be 6 * 1 = 6. Finally, we can add the 2 numbers. 4 + 6 = $\boxed{\textbf{(A)} ~10}$ .
~~Brainiacs77~~

## Solution 2
Draw the following four lines as shown: [asy] usepackage("mathptmx"); defaultpen(linewidth(0.5)); size(5cm); defaultpen(fontsize(14pt)); label("$\textbf{Math}$", (2.1,3.7)--(3.9,3.7)); label("$\textbf{Team}$", (2.1,3)--(3.9,3)); filldraw((1,2)--(2,1)--(3,2)--(4,1)--(5,2)--(4,3)--(5,4)--(4,5)--(3,4)--(2,5)--(1,4)--(2,3)--(1,2)--cycle, mediumgray*0.5 + lightgray*0.5); draw((0,0)--(6,0), gray); draw((0,1)--(6,1), gray); draw((0,2)--(6,2), gray); draw((0,3)--(6,3), gray); draw((0,4)--(6,4), gray); draw((0,5)--(6,5), gray); draw((0,6)--(6,6), gray); draw((0,0)--(0,6), gray); draw((1,0)--(1,6), gray); draw((2,0)--(2,6), gray); draw((3,0)--(3,6), gray); draw((4,0)--(4,6), gray); draw((5,0)--(5,6), gray); draw((6,0)--(6,6), gray); draw((3,4)--(4,3), red); draw((4,3)--(3,2), red); draw((3,2)--(2,3), red); draw((2,3)--(3,4), red); [/asy]
We see these lines split the figure into five squares with side length $\sqrt2$ . Thus, the area is $5\cdot\left(\sqrt2\right)^2=5\cdot 2 = \boxed{\textbf{(A) } 10}$ .
~pog ~wamofan

## Solution 3
There are $5$ lattice points in the interior of the logo and $12$ lattice points on the boundary of the logo. Because of Pick's Theorem, the area of the logo is $5+\frac{12}{2}-1=\boxed{\textbf{(A) } 10}$ .
~MathFun1000

## Solution 4
Notice that the area of the figure is equal to the area of the $4 \times 4$ square subtracted by the $12$ triangles that are half the area of each square, which is $1$ . The total area of the triangles not in the figure is $12 \cdot \frac{1}{2} = 6$ , so the answer is $16-6 = \boxed{\textbf{(A) } 10}$ .
~hh99754539

## Solution 5
Draw the following four lines as shown:
[asy] usepackage("mathptmx"); defaultpen(linewidth(0.5)); size(5cm); defaultpen(fontsize(14pt)); label("$\textbf{Math}$", (2.1,3.7)--(3.9,3.7)); label("$\textbf{Team}$", (2.1,3)--(3.9,3)); filldraw((1,2)--(2,1)--(3,2)--(4,1)--(5,2)--(4,3)--(5,4)--(4,5)--(3,4)--(2,5)--(1,4)--(2,3)--(1,2)--cycle, mediumgray*0.5 + lightgray*0.5); draw((0,0)--(6,0), gray); draw((0,1)--(6,1), gray); draw((0,2)--(6,2), gray); draw((0,3)--(6,3), gray); draw((0,4)--(6,4), gray); draw((0,5)--(6,5), gray); draw((0,6)--(6,6), gray); draw((0,0)--(0,6), gray); draw((1,0)--(1,6), gray); draw((2,0)--(2,6), gray); draw((3,0)--(3,6), gray); draw((4,0)--(4,6), gray); draw((5,0)--(5,6), gray); draw((6,0)--(6,6), gray); draw((2,4)--(4,4), red); draw((4,4)--(4,2), red); draw((4,2)--(2,2), red); draw((2,2)--(2,4), red); [/asy]
The area of the big square is $4$ , and the area of each triangle is $0.5$ . There are $12$ of these triangles, so the total area of all the triangles is $0.5\cdot12=6$ . Therefore, the area of the entire figure is $4+6=\boxed{\textbf{(A) } 10}$ .
~RocketScientist

## Solution 6 (Shoelace Theorem)
The coordinates are $(1,2), (2,1), (3,2), (4,1), (5,2), (4,3), (5,4), (4,5), (3,4), (2,5), (1,4), (2,3)$ Use the Shoelace Theorem to get $\boxed{\textbf{(A)} ~10}$ .

## Solution 7 (Quick)
If the triangles are rearranged such that the gaps are filled, there would be a $4$ by $2$ rectangle, and two $1$ by $1$ squares are present. Thus, the answer is $\boxed{\textbf{(A)} ~10}$ .
~peelybonehead

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/tYWp6fcUAik?si=V8hv_zOn_zYOi9E5&t=28 ~hsnacademy

## Video Solution 1 by Math-X (First understand the problem!!!)
https://youtu.be/oUEa7AjMF2A?si=7nqtNywjcJi2uIf7&t=62
~Math-X

## Video Solution 2 (HOW TO CREATIVELY THINK!!!)
https://youtu.be/8TyfWyTOxLI
~Education, the Study of Everything

## Video Solution 3
https://www.youtube.com/watch?v=Ij9pAy6tQSg ~Interstigation

## Video Solution 4
https://youtu.be/mKAqJxZMKTM
~savannahsolver

## Video Solution 5
https://youtu.be/Q0R6dnIO95Y
~STEMbreezy

## Video Solution 6
https://www.youtube.com/watch?v=pGpDR0hm6qs
~harungurcan

## Video Solution 7 by Dr. David
https://youtu.be/v02hhkayXYI
### See Also