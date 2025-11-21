# 2001 AMC 8 Problem 7

## Problem

To promote her school's annual Kite Olympics, Genevieve makes a small kite and a large kite for a bulletin board display. The kites look like the one in the diagram. For her small kite Genevieve draws the kite on a one-inch grid. For the large kite she triples both the height and width of the entire grid. [asy] for (int a = 0; a < 7; ++a) { for (int b = 0; b < 8; ++b) { dot((a,b)); } } draw((3,0)--(0,5)--(3,7)--(6,5)--cycle); [/asy]

What is the number of square inches in the area of the small kite?

$\text{(A)}\ 21 \qquad \text{(B)}\ 22 \qquad \text{(C)}\ 23 \qquad \text{(D)}\ 24 \qquad \text{(E)}\ 25$

## Solution 1
The area of a kite is half the product of its diagonals. The diagonals have lengths of $6$ and $7$ , so the area is $\frac{(6)(7)}{2}=21, \boxed{\text{A}}$ .

## Solution 2
Drawing in the diagonals of the kite will form four right triangles on the "inside" part of the grid. Drawing in the border of the 7 by 6 grid will form four right triangles on the "outside" part of the grid. Since each right triangle on the inside can be paired with a congruent right triangle that is on the outside, the area of the kite is half the total area of the grid, or $\frac{(6)(7)}{2}=21, \boxed{\text{A}}$ .

## Solution 3
Pick's Theorem states: \[\frac{\text{number of boundary points}}{2}+\text{number of interior points}-1\] as the area of a figure on a grid. Counting, we see there are $4$ boundary points and $20$ interior points. Therefore, we have \[\frac{4}{2}+20-1\implies 20+1\implies 21.\] Hence, the answer is $\boxed{\text{(A)}}$
### See Also