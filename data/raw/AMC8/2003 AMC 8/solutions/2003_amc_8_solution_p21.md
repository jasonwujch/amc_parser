# 2003 AMC 8 Problem 21

## Problem

The area of trapezoid $ABCD$ is $164\text{ cm}^2$ . The altitude is 8 cm, $AB$ is 10 cm, and $CD$ is 17 cm. What is $BC$ , in centimeters?

[asy]/* AMC8 2003 #21 Problem */ size(4inch,2inch); draw((0,0)--(31,0)--(16,8)--(6,8)--cycle); draw((11,8)--(11,0), linetype("8 4")); draw((11,1)--(12,1)--(12,0)); label("$A$", (0,0), SW); label("$D$", (31,0), SE); label("$B$", (6,8), NW); label("$C$", (16,8), NE); label("10", (3,5), W); label("8", (11,4), E); label("17", (22.5,5), E);[/asy]

$\textbf{(A)}\ 9\qquad\textbf{(B)}\ 10\qquad\textbf{(C)}\ 12\qquad\textbf{(D)}\ 15\qquad\textbf{(E)}\ 20$

## Solution
Using the formula for the area of a trapezoid, we have $164=8(\frac{BC+AD}{2})$ . Thus $BC+AD=41$ . Drop perpendiculars from $B$ to $AD$ and from $C$ to $AD$ and let them hit $AD$ at $E$ and $F$ respectively. Note that each of these perpendiculars has length $8$ . From the Pythagorean Theorem, $AE=6$ and $DF=15$ thus $AD=BC+21$ . Substituting back into our original equation we have $BC+BC+21=41$ thus $BC=\boxed{\text{(B)}\ 10}$
### See Also