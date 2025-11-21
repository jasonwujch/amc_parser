# 2017 AMC 8 Problem 18

## Problem

In the non-convex quadrilateral $ABCD$ shown below, $\angle BCD$ is a right angle, $AB=12$ , $BC=4$ , $CD=3$ , and $AD=13$ . What is the area of quadrilateral $ABCD$ ?

[asy]draw((0,0)--(2.4,3.6)--(0,5)--(12,0)--(0,0)); label("$B$", (0, 0), SW); label("$A$", (12, 0), ESE); label("$C$", (2.4, 3.6), SE); label("$D$", (0, 5), N);[/asy]

$\textbf{(A) }12 \qquad \textbf{(B) }24 \qquad \textbf{(C) }26 \qquad \textbf{(D) }30 \qquad \textbf{(E) }36$

## Solution 1
We first connect point $B$ with point $D$ .
[asy]draw((0,0)--(2.4,3.6)--(0,5)--(12,0)--(0,0)); draw((0,0)--(0,5)); label("$B$", (0, 0), SW); label("$A$", (12, 0), ESE); label("$C$", (2.4, 3.6), SE); label("$D$", (0, 5), N);[/asy]
We can see that $\triangle BCD$ is a 3-4-5 right triangle. We can also see that $\triangle BDA$ is a right triangle, by the 5-12-13 Pythagorean triple. With these lengths, we can solve the problem. The area of $\triangle BDA$ is $\frac{5\cdot 12}{2}$ , and the area of $\triangle BCD$ is $\frac{3\cdot 4}{2}$ . Thus, the area of quadrilateral $ABCD$ is $30-6 = \boxed{\textbf{(B)}\ 24}.$
~CHECKMATE2021

## Solution 2
$\triangle BCD$ is a 3-4-5 right triangle. So the area of $\triangle BCD$ is 6. Then we can use Heron's formula to compute the area of $\triangle ABD$ whose sides have lengths 5,12,and 13. The area of $\triangle ABD$ = $\sqrt{s(s-5)(s-12)(s-13)}$ , where s is the semi-perimeter of the triangle, that is $s=(5+12+13)/2=15.$ Thus, the area of $\triangle ABD$ is 30, so the area of $ABCD$ is $30-6 = \boxed{\textbf{(B)}\ 24}.$ ---LarryFlora

## Video Solution by Pi Academy
https://youtu.be/aH4GrC5Nfwk?si=tFdEHOoFbkp4q7tD
~ savannahsolver
### See Also