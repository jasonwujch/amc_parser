# 2003 AMC 8 Problem 9

## Problem

Problems 8, 9 and 10 use the data found in the accompanying paragraph and figures

Four friends, Art, Roger, Paul and Trisha, bake cookies, and all cookies have the same thickness. The shapes of the cookies differ, as shown.

$\circ$ Art's cookies are trapezoids: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(5,0)--(5,3)--(2,3)--cycle); draw(rightanglemark((5,3), (5,0), origin)); label("5 in", (2.5,0), S); label("3 in", (5,1.5), E); label("3 in", (3.5,3), N);[/asy]

$\circ$ Roger's cookies are rectangles: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(4,0)--(4,2)--(0,2)--cycle); draw(rightanglemark((4,2), (4,0), origin)); draw(rightanglemark((0,2), origin, (4,0))); label("4 in", (2,0), S); label("2 in", (4,1), E);[/asy]

$\circ$ Paul's cookies are parallelograms: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(3,0)--(2.5,2)--(-0.5,2)--cycle); draw((2.5,2)--(2.5,0), dashed); draw(rightanglemark((2.5,2),(2.5,0), origin)); label("3 in", (1.5,0), S); label("2 in", (2.5,1), W);[/asy]

$\circ$ Trisha's cookies are triangles: [asy]size(80);defaultpen(linewidth(0.8));defaultpen(fontsize(8)); draw(origin--(3,0)--(3,4)--cycle); draw(rightanglemark((3,4),(3,0), origin)); label("3 in", (1.5,0), S); label("4 in", (3,2), E);[/asy]

Each friend uses the same amount of dough, and Art makes exactly $12$ cookies. Art's cookies sell for $60$ cents each. To earn the same amount from a single batch, how much should one of Roger's cookies cost in cents?

$\textbf{(A)}\ 18\qquad\textbf{(B)}\ 25\qquad\textbf{(C)}\ 40\qquad\textbf{(D)}\ 75\qquad\textbf{(E)}\ 90$

## Solution
The area of one of Art's cookies is $3 \cdot 3 + \frac{2 \cdot 3}{2}=9+3=12$ . As he has $12$ cookies in a batch, the amount of dough each person used is $12 \cdot 12=144$ . Roger's cookies have an area of $\frac{144}{2 \cdot 4}=\frac{144}{8}= 18$ cookies in a batch. In total, the amount of money Art will earn is $12 \cdot 60=720$ . Thus, the amount Roger would need to charge per cookie is $\frac{720}{18}=\boxed{\textbf{(C)}\ 40}$ .
### See Also