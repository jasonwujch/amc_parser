# 2005 AMC 8 Problem 13

## Problem

The area of polygon $ABCDEF$ is 52 with $AB=8$ , $BC=9$ and $FA=5$ . What is $DE+EF$ ?

[asy] pair a=(0,9), b=(8,9), c=(8,0), d=(4,0), e=(4,4), f=(0,4); draw(a--b--c--d--e--f--cycle); draw(shift(0,-.25)*a--shift(.25,-.25)*a--shift(.25,0)*a); draw(shift(-.25,0)*b--shift(-.25,-.25)*b--shift(0,-.25)*b); draw(shift(-.25,0)*c--shift(-.25,.25)*c--shift(0,.25)*c); draw(shift(.25,0)*d--shift(.25,.25)*d--shift(0,.25)*d); draw(shift(.25,0)*f--shift(.25,.25)*f--shift(0,.25)*f); label("$A$", a, NW); label("$B$", b, NE); label("$C$", c, SE); label("$D$", d, SW); label("$E$", e, SW); label("$F$", f, SW); label("5", (0,6.5), W); label("8", (4,9), N); label("9", (8, 4.5), E); [/asy]

$\textbf{(A)}\ 7\qquad\textbf{(B)}\ 8\qquad\textbf{(C)}\ 9\qquad\textbf{(D)}\ 10\qquad\textbf{(E)}\ 11$

## Solution
Notice that $AF + DE = BC$ , so $DE=4$ . Let $O$ be the intersection of the extensions of $AF$ and $DC$ , which makes rectangle $ABCO$ . The area of the polygon is the area of $FEDO$ subtracted from the area of $ABCO$ .
\[\text{Area} = 52 = 8 \cdot 9- EF \cdot 4\]
Solving for the unknown, $EF=5$ , therefore $DE+EF=4+5=\boxed{\textbf{(C)}\ 9}$ .

## Solution 2
Similar to solution 1, $AF + DE = BC$ , so $DE=4$ . Split the polygon into two rectangles by extending the $DE$ so it intersects $AB$ . Let's say the length of $FE$ is equal to $x$ . We can form the equation: \[5x + 9(8-x) = 52\] . We see that $x = 5$ , so we can add $5 + 4 = \boxed{\textbf{(C)}\ 9}$ .

## Video Solution by OmegaLearn
https://youtu.be/abSgjn4Qs34?t=1908
~ pi_is_3.14
### See Also