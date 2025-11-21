# 2001 AMC 8 Problem 9

## Problem

To promote her school's annual Kite Olympics, Genevieve makes a small kite and a large kite for a bulletin board display. The kites look like the one in the diagram. For her small kite Genevieve draws the kite on a one-inch grid. For the large kite she triples both the height and width of the entire grid.

[asy] for (int a = 0; a < 7; ++a) { for (int b = 0; b < 8; ++b) { dot((a,b)); } } draw((3,0)--(0,5)--(3,7)--(6,5)--cycle); [/asy]

The large kite is covered with gold foil. The foil is cut from a rectangular piece that just covers the entire grid. How many square inches of waste material are cut off from the four corners?

$\textbf{(A)}\ 63 \qquad \textbf{(B)}\ 72 \qquad \textbf{(C)}\ 180 \qquad \textbf{(D)}\ 189 \qquad \textbf{(E)}\ 264$

## Solution
The large grid has dimensions three times that of the small grid, so its dimensions are $3(6)\times3(7)$ , or $18\times21$ , so the area is $(18)(21)=378$ . The area of the kite is half of the area of the rectangle as you can see, so the area of the waste material is also half the area of the rectangle. Thus, the area of the waste material is $378/2=\boxed{189\textbf{ (D)}}$ .
### See Also