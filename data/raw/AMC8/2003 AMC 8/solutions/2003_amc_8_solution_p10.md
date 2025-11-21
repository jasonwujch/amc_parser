# 2003 AMC 8 Problem 10

## Problem

Problems 8, 9 and 10 use the data found in the accompanying paragraph and figures

Four friends, Art, Roger, Paul and Trisha, bake cookies, and all cookies have the same thickness. The shapes of the cookies differ, as shown.

$\circ$ Art's cookies are trapezoids: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(5,0)--(5,3)--(2,3)--cycle); draw(rightanglemark((5,3), (5,0), origin)); label("5 in", (2.5,0), S); label("3 in", (5,1.5), E); label("3 in", (3.5,3), N);[/asy]

$\circ$ Roger's cookies are rectangles: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(4,0)--(4,2)--(0,2)--cycle); draw(rightanglemark((4,2), (4,0), origin)); draw(rightanglemark((0,2), origin, (4,0))); label("4 in", (2,0), S); label("2 in", (4,1), E);[/asy]

$\circ$ Paul's cookies are parallelograms: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(3,0)--(2.5,2)--(-0.5,2)--cycle); draw((2.5,2)--(2.5,0), dashed); draw(rightanglemark((2.5,2),(2.5,0), origin)); label("3 in", (1.5,0), S); label("2 in", (2.5,1), W);[/asy]

$\circ$ Trisha's cookies are triangles: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(3,0)--(3,4)--cycle); draw(rightanglemark((3,4),(3,0), origin)); label("3 in", (1.5,0), S); label("4 in", (3,2), E);[/asy]

How many cookies will be in one batch of Trisha's cookies?

$\textbf{(A)}\ 10\qquad\textbf{(B)}\ 12\qquad\textbf{(C)}\ 16\qquad\textbf{(D)}\ 18\qquad\textbf{(E)}\ 24$

## Solution
Art's cookies have areas of $3 \cdot 3 + \frac{2 \cdot 3}{2}=9+3=12$ . There are 12 cookies in one of Art's batches so everyone used $12 \cdot 12=144 \text{ in}^2$ of dough. Trisha's cookies have an area of $\frac{3 \cdot 4}{2}=6$ so she has $\frac{144}{6}=\boxed{\textbf{(E)}\ 24}$ cookies per batch.
### See Also