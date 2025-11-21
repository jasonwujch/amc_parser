# 2003 AMC 8 Problem 8

## Problem

Problems 8, 9 and 10 use the data found in the accompanying paragraph and figures

Four friends, Art, Roger, Paul and Trisha, bake cookies, and all cookies have the same thickness. The shapes of the cookies differ, as shown.

$\circ$ Art's cookies are trapezoids. [asy] size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(5,0)--(5,3)--(2,3)--cycle); draw(rightanglemark((5,3), (5,0), origin)); label("5 in", (2.5,0), S); label("3 in", (5,1.5), E); label("3 in", (3.5,3), N); [/asy]

$\circ$ Roger's cookies are rectangles. [asy] size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(4,0)--(4,2)--(0,2)--cycle); draw(rightanglemark((4,2), (4,0), origin)); draw(rightanglemark((0,2), origin, (4,0))); label("4 in", (2,0), S); label("2 in", (4,1), E); [/asy]

$\circ$ Paul's cookies are parallelograms. [asy] size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(3,0)--(2.5,2)--(-0.5,2)--cycle); draw((2.5,2)--(2.5,0), dashed); draw(rightanglemark((2.5,2),(2.5,0), origin)); label("3 in", (1.5,0), S); label("2 in", (2.5,1), W); [/asy]

$\circ$ Trisha's cookies are triangles. [asy] size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(3,0)--(3,4)--cycle); draw(rightanglemark((3,4),(3,0), origin)); label("3 in", (1.5,0), S); label("4 in", (3,2), E); [/asy]

Each friend uses the same amount of dough, and Art makes exactly 12 cookies. Who gets the fewest cookies from one batch of cookie dough?

$\textbf{(A)}\ \text{Art}\qquad\textbf{(B)}\ \text{Roger}\qquad\textbf{(C)}\ \text{Paul}\qquad\textbf{(D)}\ \text{Trisha}\qquad\textbf{(E)}\ \text{There is a tie for fewest.}$

## Solution
Out of all the cookies, Art's has an area of $12 \text{ in}^2$ , which was the greatest area out of all the cookies' areas. Roger's cookie had an area of $8 \text{ in} ^2$ , and both Paul and Trisha's cookies had an area of $6 \text{ in}^2$ . This means $\boxed{\textbf{(A)}\ \text{Art}}$ makes the fewest cookies, since his cookie area is the greatest. The answer is not that there is a tie between Paul and Trisha because they can make the most cookies with a given amount of cookie dough, not the least.
### See Also