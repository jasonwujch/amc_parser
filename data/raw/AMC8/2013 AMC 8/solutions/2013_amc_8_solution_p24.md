# 2013 AMC 8 Problem 24

## Problem

Squares $ABCD$ , $EFGH$ , and $GHIJ$ are equal in area. Points $C$ and $D$ are the midpoints of sides $IH$ and $HE$ , respectively. What is the ratio of the area of the shaded pentagon $AJICB$ to the sum of the areas of the three squares?

$\textbf{(A)}\hspace{.05in}\frac{1}{4}\qquad\textbf{(B)}\hspace{.05in}\frac{7}{24}\qquad\textbf{(C)}\hspace{.05in}\frac{1}{3}\qquad\textbf{(D)}\hspace{.05in}\frac{3}{8}\qquad\textbf{(E)}\hspace{.05in}\frac{5}{12}$

[asy] pair A,B,C,D,E,F,G,H,I,J; A = (0.5,2); B = (1.5,2); C = (1.5,1); D = (0.5,1); E = (0,1); F = (0,0); G = (1,0); H = (1,1); I = (2,1); J = (2,0); draw(A--B); draw(C--B); draw(D--A); draw(F--E); draw(I--J); draw(J--F); draw(G--H); draw(A--J); filldraw(A--B--C--I--J--cycle,grey); draw(E--I); dot("$A$", A, NW); dot("$B$", B, NE); dot("$C$", C, NE); dot("$D$", D, NW); dot("$E$", E, NW); dot("$F$", F, SW); dot("$G$", G, S); dot("$H$", H, N); dot("$I$", I, NE); dot("$J$", J, SE); [/asy]

## Solution 1
We notice that ABCX is a trapezoid with the bases AB and CX. Assuming AB is 1, we find that CX is 0.25 since it is half of CH which is 0.5. Using the area of the trapezoid formula, we calculate the area of ABCX to be 0.625 and XCIJ to be 0.375. The combined areas equal 1. Therefore, the ratio of the area of the hexagon to the three squares is 1:3 because the area of the three squares is 3. The answer is $\boxed{\textbf{(C)}\ \frac {1}{3}}$ -~TheNerdwhoIsNerdy. (I don't know if this is correct, pls check).

## Solution 2 (extremely simple)
Extend line AD such that it intersects line FG. Call the intersection K. If we assign an arbitrary value to the side lengths of the squares, such as 2, the base of the now formed triangle AJK would have a length of 3, while the height would be 4. The area of triangle AJK would then be 6, and the rectangle EDKF would have an area of 2. 6 + 2 = 8, and since all of the squares' areas add up to a total of 12 (if each has side length 2), we obtain (12 - 8)/12 for the shaded part of the diagram which yields 4/12 = $\boxed{\textbf{(C)}\ \frac {1}{3}}$
~ martianrunner
### See Also