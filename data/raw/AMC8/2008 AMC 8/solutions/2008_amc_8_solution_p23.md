# 2008 AMC 8 Problem 23

## Problem

In square $ABCE$ , $AF=2FE$ and $CD=2DE$ . What is the ratio of the area of $\triangle BFD$ to the area of square $ABCE$ ? [asy] size((100)); draw((0,0)--(9,0)--(9,9)--(0,9)--cycle); draw((3,0)--(9,9)--(0,3)--cycle); dot((3,0)); dot((0,3)); dot((9,9)); dot((0,0)); dot((9,0)); dot((0,9)); label("$A$", (0,9), NW); label("$B$", (9,9), NE); label("$C$", (9,0), SE); label("$D$", (3,0), S); label("$E$", (0,0), SW); label("$F$", (0,3), W); [/asy]

$\textbf{(A)}\ \frac{1}{6}\qquad\textbf{(B)}\ \frac{2}{9}\qquad\textbf{(C)}\ \frac{5}{18}\qquad\textbf{(D)}\ \frac{1}{3}\qquad\textbf{(E)}\ \frac{7}{20}$

## Solution 1
The area of $\triangle BFD$ is the area of square $ABCE$ subtracted by the the area of the three triangles around it. Arbitrarily assign the side length of the square to be $6$ .
[asy] size((100)); pair A=(0,9), B=(9,9), C=(9,0), D=(3,0), E=(0,0), F=(0,3); pair[] ps={A,B,C,D,E,F}; dot(ps); draw(A--B--C--E--cycle); draw(B--F--D--cycle); label("$A$",A, NW); label("$B$",B, NE); label("$C$",C, SE); label("$D$",D, S); label("$E$",E, SW); label("$F$",F, W); label("$6$",A--B,N); label("$6$",(10,4.5),E); label("$4$",D--C,S); label("$2$",E--D,S); label("$2$",E--F,W); label("$4$",F--A,W); [/asy]
The ratio of the area of $\triangle BFD$ to the area of $ABCE$ is
\[\frac{36-12-12-2}{36} = \frac{10}{36} = \boxed{\textbf{(C)}\ \frac{5}{18}}\]

## Solution 2
Say that $\overline{FE}$ has length $x$ , and that from there we can infer that $\overline{AF} = 2x$ . We also know that $\overline{ED} = x$ , and that $\overline{DC} = 2x$ . The area of triangle $BFD$ is the square's area subtracted from the area of the excess triangles, which is simply these equations: \[9x^2 - (3x^2 + \dfrac{x}{2}^2 + 3x^2)\] \[9x^2 - 6.5x^2\] \[2.5x^2\] Thus, the area of the triangle is $2.5x^2$ . We can now put the ratio of triangle $BFD$ 's area to the area of the square $ABCE$ as a fraction. We have: \[\dfrac{2.5x^2}{9x^2}\] \[\dfrac{2.5\cancel{x^2}}{9\cancel{x^2}}\] \[\dfrac{2.5}{9}\] \[\dfrac{5}{18}\] Thus, our answer is $\boxed{C}$ , $\boxed{\dfrac{5}{18}}$ .
~Mr.BigBrain_AoPS

## Video Solution by OmegaLearn
https://youtu.be/abSgjn4Qs34?t=528
~ pi_is_3.14
### See Also