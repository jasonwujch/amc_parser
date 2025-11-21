# 2007 AMC 8 Problem 8

## Problem

In trapezoid $ABCD$ , $\overline{AD}$ is perpendicular to $\overline{DC}$ , $AD = AB = 3$ , and $DC = 6$ . In addition, $E$ is on $\overline{DC}$ , and $\overline{BE}$ is parallel to $\overline{AD}$ . Find the area of $\triangle BEC$ . [asy] defaultpen(linewidth(0.7)); pair A=(0,3), B=(3,3), C=(6,0), D=origin, E=(3,0); draw(E--B--C--D--A--B); draw(rightanglemark(A, D, C)); label("$A$", A, NW); label("$B$", B, NW); label("$C$", C, SE); label("$D$", D, SW); label("$E$", E, NW); label("$3$", A--D, W); label("$3$", A--B, N); label("$6$", E, S); [/asy]

$\textbf{(A)}\ 3 \qquad \textbf{(B)}\ 4.5 \qquad \textbf{(C)}\ 6 \qquad \textbf{(D)}\ 9 \qquad \textbf{(E)}\ 18$

## Solution 1 (Area Formula for Triangles)
Clearly, $ABED$ is a square with side-length $3.$ By segment subtraction, we have $EC = DC - DE = 6 - 3 = 3.$
The area of $\triangle BEC$ is \[\frac12\cdot EC\cdot BE = \frac12\cdot3\cdot3 = \boxed{\textbf{(B)}\ 4.5}.\] ~Aplus95 (Solution)
~MRENTHUSIASM (Revision)

## Solution 2 (Area Subtraction)
Clearly, $ABED$ is a square with side-length $3.$
Let the brackets denote areas. We apply area subtraction to find the area of $\triangle BEC:$ \begin{align*} [BEC]&=[ABCD]-[ABED] \\ &=\frac{AB+CD}{2}\cdot AD - AB^2 \\ &=\frac{3+6}{2}\cdot 3 - 3^2 \\ &=\boxed{\textbf{(B)}\ 4.5}. \end{align*} ~MRENTHUSIASM

## Solution 3 (Cheese, Don't use in competition unless stuck)
$4.5$ is the only one that isn't an integer, and is the odd one out. \begin{align*} &\boxed{\textbf{(B)}\ 4.5}. \end{align*}
~SHREYANSH

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=omFpSGMWhFc

## Video Solution by WhyMath
https://youtu.be/Qdbpdc-Khg4
### See Also