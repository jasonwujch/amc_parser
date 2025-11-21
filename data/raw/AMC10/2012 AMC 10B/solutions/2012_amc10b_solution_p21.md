# 2012 AMC 10B Problem 21

## Problem

Four distinct points are arranged on a plane so that the segments connecting them have lengths $a$ , $a$ , $a$ , $a$ , $2a$ , and $b$ . What is the ratio of $b$ to $a$ ?

$\textbf{(A)}\ \sqrt{3}\qquad\textbf{(B)}\ 2\qquad\textbf{(C)}\ \sqrt{5}\qquad\textbf{(D)}\ 3\qquad\textbf{(E)}\ \pi$

## Solution
When you see that there are lengths a and 2a, one could think of 30-60-90 triangles. Since all of the other's lengths are a, you could think that $b=\sqrt{3}a$ . Drawing the points out, it is possible to have a diagram where $b=\sqrt{3}a$ . It turns out that $a,$ $2a,$ and $b$ could be the lengths of a 30-60-90 triangle, and the other 3 $a\text{'s}$ can be the lengths of an equilateral triangle formed from connecting the dots. So, $b=\sqrt{3}a$ , so $b:a= \boxed{\textbf{(A)} \: \sqrt{3}}$ [asy]draw((0, 0)--(1/2, sqrt(3)/2)--(1, 0)--cycle); draw((1/2, sqrt(3)/2)--(2, 0)--(1,0)); label("$a$", (0, 0)--(1, 0), S); label("$a$", (1, 0)--(2, 0), S); label("$a$", (0, 0)--(1/2, sqrt(3)/2), NW); label("$a$", (1, 0)--(1/2, sqrt(3)/2), NE); label("$b=\sqrt{3}a$", (1/2, sqrt(3)/2)--(2, 0), NE); [/asy]

## Solution 2
For any $4$ non-collinear points with the given requirement, notice that there must be a triangle with side lengths $a$ , $a$ , $2a$ , which is not possible as $a+a=2a$ . Thus at least $3$ of the $4$ points must be collinear.
If all $4$ points are collinear, then there would only be $3$ lines of length $a$ , which wouldn't work.
If exactly $3$ points are collinear, the only possibility that works is when a $30^{\circ}-90^{\circ}-60^{\circ}$ triangle is formed.
Thus $b=\sqrt{3}a$ , or $\frac{b}{a}=\boxed{\mathrm{(A)}\sqrt{3}}$
~ Nafer

## Solution 3 (using the answer choices)
We know that $a-b-2a$ form a triangle. From triangle inequality, we see that $b>a$ . Then, we also see that there is an isosceles triangle with lengths $a-a-b$ . From triangle inequality: $b<2a$ . The only answer choice that holds these two inequalities is: $\sqrt{3}$ .

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012amc10b/271
~dolphin7
(Direct Youtube Link) https://www.youtube.com/watch?v=6sL7bhkVivo
~lukiebear
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .