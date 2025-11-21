# 2016 AMC 10B Problem 9

## Problem

All three vertices of $\bigtriangleup ABC$ lie on the parabola defined by $y=x^2$ , with $A$ at the origin and $\overline{BC}$ parallel to the $x$ -axis. The area of the triangle is $64$ . What is the length of $BC$ ?

$\textbf{(A)}\ 4\qquad\textbf{(B)}\ 6\qquad\textbf{(C)}\ 8\qquad\textbf{(D)}\ 10\qquad\textbf{(E)}\ 16$

## Solution
[asy]import graph;size(7cm,IgnoreAspect); real f(real x) {return x*x;} draw((0,0)--(4,16)--(-4,16)--cycle,blue); draw(graph(f,-5,5,operator ..),gray); xaxis("$x$");yaxis("$y$",-1); label("$y=x^2$",(4.5,20.25),E); draw((4.2,0)--(4.2,16),Arrows); label("$r^2$",(4.2,0)--(4.2,16),E); draw((0,17)--(4,17),Arrows); label("$r$",(0,17)--(4,17),N); [/asy] The area of the triangle is $\frac{(2r)(r^2)}{2} = r^3$ , so $r^3=64\implies r=4$ , giving a total distance across the top of $8$ , which is answer $\textbf{(C)}$ .

## Solution 2 (Guess and Check)
Let the point where the height of the triangle intersects with the base be $D$ . Now we can guess what $x$ is and find $y$ . If $x$ is $3$ , then $y$ is $9$ . The cords of $B$ and $C$ would be $(-3,9)$ and $(3,9)$ , respectively. The distance between $B$ and $C$ is $6$ , meaning the area would be $\frac{6 \cdot 9}{2}=27$ , not $64$ . Now we let $x=4$ . $y$ would be $16$ . The cords of $B$ and $C$ would be $(-4,16)$ and $(4,16)$ , respectively. $BC$ would be $8$ , and the height would be $16$ . The area would then be $\frac{8 \cdot 16}{2}$ which is $64$ , so $BC$ is $\boxed{\textbf{(C)}\ 8}$ .

## Video Solution (CREATIVE THINKING)
https://youtu.be/pSJkO6kQGOs
~Education, the Study of Everything

## Video Solution
https://youtu.be/1pi0eiD3jHc
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .