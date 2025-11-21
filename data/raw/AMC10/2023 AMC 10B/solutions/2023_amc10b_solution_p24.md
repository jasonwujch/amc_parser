# 2023 AMC 10B Problem 24

## Problem

What is the perimeter of the boundary of the region consisting of all points which can be expressed as $(2u-3w, v+4w)$ with $0\le u\le1$ , $0\le v\le1,$ and $0\le w\le1$ ?

$\textbf{(A) } 10\sqrt{3} \qquad \textbf{(B) } 13 \qquad \textbf{(C) } 12 \qquad \textbf{(D) } 18 \qquad \textbf{(E) } 16$

## Solution 1
[asy] import geometry; pair A = (-3, 4); pair B = (-3, 5); pair C = (-1, 4); pair D = (-1, 5); pair AA = (0, 0); pair BB = (0, 1); pair CC = (2, 0); pair DD = (2, 1); //draw(A--B--D--C--cycle); draw(A--B); label("1",midpoint(A--B),W); label("2",midpoint(D--B),N); draw(A--C,dashed); draw(B--D); draw(C--D, dashed); draw(A--AA); label("5",midpoint(A--AA),W); draw(B--BB,dashed); draw(C--CC,dashed); draw(D--DD); label("5",midpoint(D--DD),E); label("1",midpoint(CC--DD),E); label("2",midpoint(AA--CC),S); // Dotted vertices dot(A); dot(B); dot(C); dot(D); dot(AA); dot(BB); dot(CC); dot(DD); draw(AA--BB,dashed); draw(AA--CC); draw(BB--DD,dashed); draw(CC--DD); label("(0,0)",AA,W); label("(-3,4)",A,SW); label("(-1,5)",D,E); label("(2,1)",DD,NE); [/asy] Notice that we are given a parametric form of the region, and $w$ is used in both $x$ and $y$ . We first fix $u$ and $v$ to $0$ , and graph $(-3w,4w)$ from $0\le w\le1$ . When $w$ is $0$ , we have the point $(0,0)$ , and when $w$ is $1$ , we have the point $(-3,4)$ . We see that since this is a directly proportional function, we can just connect the dots like this:
[asy] import graph; Label f; size(5cm); unitsize(0.7cm); xaxis(-5,5,Ticks(f, 5.0, 1.0)); yaxis(-5,5,Ticks(f, 5.0, 1.0)); draw((0,0)--(-3,4)); [/asy]
Now, when we vary $2u$ from $0$ to $2$ , this line is translated to the right $2$ units:
[asy] import graph; Label f; unitsize(0.7cm); size(5cm); xaxis(-5,5,Ticks(f, 5.0, 1.0)); yaxis(-5,5,Ticks(f, 5.0, 1.0)); draw((0,0)--(-3,4)); draw((2,0)--(-1,4)); [/asy]
We know that any points in the region between the line (or rather segment) and its translation satisfy $w$ and $u$ , so we shade in the region:
[asy] import graph; Label f; unitsize(0.7cm); size(5cm); xaxis(-5,5,Ticks(f, 5.0, 1.0)); yaxis(-5,5,Ticks(f, 5.0, 1.0)); draw((0,0)--(-3,4)); draw((2,0)--(-1,4)); filldraw((0,0)--(-3,4)--(-1,4)--(2,0)--cycle, gray); [/asy]
We can also shift this quadrilateral one unit up, because of $v$ . Thus, this is our figure:
[asy] import graph; Label f; unitsize(0.7cm); size(5cm); xaxis(-5,5,Ticks(f, 5.0, 1.0)); yaxis(-5,5,Ticks(f, 5.0, 1.0)); draw((0,0)--(-3,4)); draw((2,0)--(-1,4)); filldraw((0,0)--(-3,4)--(-1,4)--(2,0)--cycle, gray); filldraw((0,1)--(-3,5)--(-1,5)--(2,1)--cycle, gray); draw((0,0)--(0,1),black+dashed); draw((2,0)--(2,1),black+dashed); draw((-3,4)--(-3,5),black+dashed); [/asy]
[asy] import graph; Label f; unitsize(0.7cm); size(5cm); xaxis(-5,5,Ticks(f, 5.0, 1.0)); yaxis(-5,5,Ticks(f, 5.0, 1.0)); draw((0,0)--(-3,4)); draw((1,0)--(-2,4)); filldraw((0,0)--(2,0)--(2,1)--(-1,5)--(-3,5)--(-3,4)--cycle, gray); [/asy]
The length of the boundary is simply $1+2+5+1+2+5$ ( $5$ can be obtained by Pythagorean theorem since we have side lengths $3$ and $4$ .). This equals $\boxed{\textbf{(E) }16.}$
~Technodoggo ~ESAOPS

## Solution 2
We can find the "boundary points" and work with our intuition to solve the problem. We set each of $u, v, w$ equal to $0, 1$ for a total of $8$ combinations in $u, v, w$ . We now test each one.
Case 1: $u = 0, v = 0, w = 0 \implies (0, 0)$
Case 2: $u = 0, v = 0, w = 1 \implies (-3, 4)$
Case 3: $u = 0, v = 1, w = 0 \implies (0, 1)$
Case 4: $u = 0, v = 1, w = 1 \implies (-3, 5)$
Case 5: $u = 1, v = 0, w = 0 \implies (2, 0)$
Case 6: $u = 1, v = 0, w = 1 \implies (-1, 4)$
Case 7: $u = 1, v = 1, w = 0 \implies (2, 1)$
Case 8: $u = 1, v = 1, w = 1 \implies (-1, 5)$
When graphed on a coordinate plane, the points appear as follows.
[asy] import graph; import geometry; Label f; size(5cm); unitsize(0.7cm); xaxis(-5,5,Ticks(f, 5.0, 1.0)); yaxis(-5,5,Ticks(f, 5.0, 1.0)); pair A = (0, 0); dot (A); pair B = (-3, 4); dot (B); pair C = (0, 1); dot (C); pair D = (-3, 5); dot (D); pair E = (2, 0); dot (E); pair F = (-1, 4); dot (F); pair G = (2, 1); dot (G); pair H = (-1, 5); dot (H); [/asy]
Notice how there are two distinct rectangles visible in the figure. This leads us to believe that the region tracks the motion of this region as it travels in space. To understand why this is true, we can imagine a fixed $w$ (as it is present in both the $x$ and $y$ coordinates). Then if we hold one of $u$ or $v$ fixed and let the other vary, we get a straight line parallel to the $x$ or $y$ axis respectively. If we let the other vary, we get the other type of straight line. Together, they form a rectangular region. In addition, $w$ serves as a diagonal translation, so if we now let $w$ vary, it traces out the motion of the rectangle. Keeping this in mind, we connect the dots.
[asy] import graph; import geometry; Label f; size(5cm); unitsize(0.7cm); xaxis(-5,5,Ticks(f, 5.0, 1.0)); yaxis(-5,5,Ticks(f, 5.0, 1.0)); draw((0,0)--(-3,4)--(-3,5)--(-1,5)--(2,1)--(2,0)--cycle, gray); [/asy]
Each of the diagonal sides have length $5$ by the distance formula on $(0,0)$ and $(-3,4)$ (the other diagonal side is congruent), so our total perimeter is $2 + 1 + 5 + 2 + 1 + 5 = \boxed{\textbf{(E)}~ 16}$ .
~ cxsmi

## Solution 3 (Quick, Not rigorous)
Let's assume that $w = 0$ . If we plug $(0, 0), (0, 1), (1, 1), (1, 0)$ into $u$ and $v$ respectively, we will form a rectangle that has side lengths $1$ and $2$ . If we change $w$ to the maximum value (which is $1$ ), we will find out that w shifts the rectangle by $-3w$ on the x-axis and $4w$ on the y-axis. Since we need to find the perimeter of the shift and rectangle, we can calculate that the length that the corner has move during the shift using the Pythagorean Theorem . Thus, the distance is $5$ . Now, we can find the perimeter of the boundary which is $2(1 + 2 + 5) = 16$ . This means that the answer is $\boxed{\textbf{(E)}~ 16}$ .
~ROGER8432V3

## Video Solution 1 by OmegaLearn
https://youtu.be/KEV3ka5gWYU

## Video Solution
https://youtu.be/bqIlsWTOL3k
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .