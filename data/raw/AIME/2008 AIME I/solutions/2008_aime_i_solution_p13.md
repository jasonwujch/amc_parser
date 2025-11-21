# 2008 AIME I Problem 13

## Problem

Let

\[p(x,y) = a_0 + a_1x + a_2y + a_3x^2 + a_4xy + a_5y^2 + a_6x^3 + a_7x^2y + a_8xy^2 + a_9y^3.\]

Suppose that

\[p(0,0) = p(1,0) = p( - 1,0) = p(0,1) = p(0, - 1)\\ = p(1,1) = p(1, - 1) = p(2,2) = 0.\]

There is a point $\left(\frac {a}{c},\frac {b}{c}\right)$ for which $p\left(\frac {a}{c},\frac {b}{c}\right) = 0$ for all such polynomials, where $a$ , $b$ , and $c$ are positive integers, $a$ and $c$ are relatively prime, and $c > 1$ . Find $a + b + c$ .

## Solution

## Solution 1
\begin{align*} p(0,0) &= a_0 \\ &= 0 \\ p(1,0) &= a_0 + a_1 + a_3 + a_6 \\ &= a_1 + a_3 + a_6 \\ &= 0 \\ p(-1,0) &= -a_1 + a_3 - a_6 \\ &= 0 \end{align*}
Adding the above two equations gives $a_3 = 0$ , and so we can deduce that $a_6 = -a_1$ .
Similarly, plugging in $(0,1)$ and $(0,-1)$ gives $a_5 = 0$ and $a_9 = -a_2$ . Now, \begin{align*} p(1,1) &= a_0 + a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7 + a_8 + a_9 \\ &= 0 + a_1 + a_2 + 0 + a_4 + 0 - a_1 + a_7 + a_8 - a_2 \\ &= a_4 + a_7 + a_8 \\ &= 0 \\ p(1,-1) &= a_0 + a_1 - a_2 + 0 - a_4 + 0 - a_1 - a_7 + a_8 + a_2 \\ &= -a_4 - a_7 + a_8 \\ &= 0 \end{align*} Therefore $a_8 = 0$ and $a_7 = -a_4$ . Finally, \begin{align*} p(2,2) &= 0 + 2a_1 + 2a_2 + 0 + 4a_4 + 0 - 8a_1 - 8a_4 +0 - 8a_2 \\ &= -6 a_1 - 6 a_2 - 4 a_4 \\ &= 0 \end{align*} So, $3a_1 + 3a_2 + 2a_4 = 0$ , or equivalently $a_4 = -\frac{3(a_1 + a_2)}{2}$ .
Substituting these equations into the original polynomial $p$ , we find that at $\left(\frac{a}{c}, \frac{b}{c}\right)$ , \[a_1x + a_2y + a_4xy - a_1x^3 - a_4x^2y - a_2y^3 = 0 \iff\] \[a_1x + a_2y - \frac{3(a_1 + a_2)}{2}xy - a_1x^3 + \frac{3(a_1 + a_2)}{2}x^2y - a_2y^3 = 0 \iff\] \[a_1x(x - 1)\left(x + 1 - \frac{3}{2}y\right) + a_2y\left(y^2 - 1 - \frac{3}{2}x(x - 1)\right) = 0\] . The remaining coefficients $a_1$ and $a_2$ are now completely arbitrary because the original equations impose no more restrictions on them. Hence, for the final equation to hold for all possible $p$ , we must have $x(x - 1)\left(x + 1 - \frac{3}{2}y\right) = y\left(y^2 - 1 - \frac{3}{2}x(x - 1)\right) = 0$ .
As the answer format implies that the $x$ -coordinate of the root is non-integral, $x(x - 1)\left(x + 1 - \frac{3}{2}y\right) = 0 \iff x + 1 - \frac{3}{2}y = 0 \iff y = \frac{2}{3}(x + 1)\ (1)$ . The format also implies that $y$ is positive, so $y\left(y^2 - 1 - \frac{3}{2}x(x - 1)\right) = 0 \iff y^2 - 1 - \frac{3}{2}x(x - 1) = 0\ (2)$ . Substituting $(1)$ into $(2)$ and reducing to a quadratic yields $(19x - 5)(x - 2) = 0$ , in which the only non-integral root is $x = \frac{5}{19}$ , so $y = \frac{16}{19}$ .
The answer is $5 + 16 + 19 = \boxed{040}$ .
[asy] unitsize(1.2 cm); real upperhyper (real x) { return(sqrt((3*x^2 - 3*x + 2)/2)); } real lowerhyper (real x) { return(-sqrt((3*x^2 - 3*x + 2)/2)); } int i; for (i = -3; i <= 3; ++i) { draw((-3,i)--(3,i),gray(0.7)); draw((i,-3)--(i,3),gray(0.7)); } draw((0,-3)--(0,3),red); draw((1,-3)--(1,3),red); draw((-3,-4/3)--(3,8/3),red); draw((-3,0)--(3,0),blue); draw(graph(upperhyper,-1.863,2.863),blue); draw(graph(lowerhyper,-1.836,2.863),blue); dot("$(0,0)$", (0,0), NE, fontsize(8)); dot("$(1,0)$", (1,0), NE, fontsize(8)); dot("$(-1,0)$", (-1,0), NW, fontsize(8)); dot("$(0,1)$", (0,1), SW, fontsize(8)); dot("$(0,-1)$", (0,-1), NW, fontsize(8)); dot("$(1,1)$", (1,1), SE, fontsize(8)); dot("$(1,-1)$", (1,-1), NE, fontsize(8)); dot("$(2,2)$", (2,2), SE, fontsize(8)); dot((5/19,16/19), green); [/asy]

## Solution 2
Consider the cross section of $z = p(x, y)$ on the plane $z = 0$ . We realize that we could construct the lines/curves in the cross section such that their equations multiply to match the form of $p(x, y)$ (same degree of $x$ and $y$ in terms) and they include the eight given points. One simple way to do this would be to use the equations $x = 0$ , $x = 1$ , and $y = \frac{2}{3}x + \frac{2}{3}$ , giving us
$p_1(x, y) = x\left(x - 1\right)\left( \frac{2}{3}x - y + \frac{2}{3}\right) = \frac{2}{3}x + xy + \frac{2}{3}x^3-x^2y$ .
Another way to do this would to use the line $y = x$ and the ellipse, $x^2 + xy + y^2 = 1$ . This would give
$p_2(x, y) = \left(x - y\right)\left(x^2 + xy + y^2 - 1\right) = -x + y + x^3 - y^3$ . (But
(Another way would be to use the hyperbola from Solution 1. Interesting that different curves both work.)
At this point, we consider that $p_1$ and $p_2$ both must have $\left(\frac{a}{c}, \frac{b}{c}\right)$ as a zero. A quick graph of the 4 lines and the ellipse used to create $p_1$ and $p_2$ gives nine intersection points. Eight of them are the given ones, and the ninth is $\left(\frac{5}{19}, \frac{16}{19}\right)$ . The last intersection point can be found by finding the intersection points of $y = \frac{2}{3}x + \frac{2}{3}$ and $x^2 + xy + y^2 = 1$ . Finally, just add the values of $a$ , $b$ , and $c$ to get $5 + 16 + 19 = \boxed{040}$
[asy] unitsize(1.2 cm); real upperellipse(real x) { return((sqrt(4- 3*x^2 )-x)/2); } real lowerellipse(real x) { return((-sqrt(4- 3*x^2 )-x)/2); } int i; for (i = -3; i <= 3; ++i) { draw((-3,i)--(3,i),gray(0.7)); draw((i,-3)--(i,3),gray(0.7)); } draw((0,-3)--(0,3),red); draw((1,-3)--(1,3),red); draw((-3,-4/3)--(3,8/3),red); draw((-3, -3)--(3,3),blue); draw(graph(upperellipse,-1.1547,1.1547),blue); draw(graph(lowerellipse, -1.1547,1.1547),blue); dot("$(0,0)$", (0,0), NE, fontsize(8)); dot("$(1,0)$", (1,0), NE, fontsize(8)); dot("$(-1,0)$", (-1,0), NW, fontsize(8)); dot("$(0,1)$", (0,1), SW, fontsize(8)); dot("$(0,-1)$", (0,-1), NW, fontsize(8)); dot("$(1,1)$", (1,1), SE, fontsize(8)); dot("$(1,-1)$", (1,-1), NE, fontsize(8)); dot("$(2,2)$", (2,2), SE, fontsize(8)); dot((5/19,16/19), green); [/asy]

## Solution 3 (Ansatz)
We can plug in the values to obtain
\[p(0,0)=0\Longrightarrow a_0=0\]
\[p(1,0)=0\Longrightarrow a_1+a_3+a_6=0\]
\[p(0,1)=0\Longrightarrow a_2+a_5+a_9=0\]
\[p(-1,0)=0\Longrightarrow a_1-a_3+a_6=0\]
\[p(0,-1)=0\Longrightarrow a_2-a-5+a_9=0\]
\[p(1,1)=0\Longrightarrow a_4+a_7+a_8=0\]
\[p(1,-1)=0\Longrightarrow a_4+a_7-a_8=0\]
\[p(2,2)=0\Longrightarrow2a_4=3a_6+3a_9\Leftrightarrow2a_4+3a_1+3a_2=0.\]
Now, this means that
\[p(x,y)=a_1x+a_2y+a_4xy-a_1x^3+a_7x^2y+a_8xy^2-a_2y^3.\]
After some simplifying, we obtain
\[p(x,y)=a_1(x-x^3)+a_2(y-y^3)+a_4xy(1-x).\]
Since $p(x,y)=0$ , $3a_1+3a_2+2a_4=0,$ and we suspect that:
\[x-x^3=y-y^3\]
and
\[\frac{x-x^3}{xy(1-x)}=\frac{3}{2}\Leftrightarrow\frac{1+x}{y}=\frac{3}{2} \Leftrightarrow\frac{2}{3}+\frac{2x}{3}=y\] .
Plugging this into the first equation, and factoring, and cancelling $(x+1)$ , and simplifying, we get $19x^2 -43x+10=0$ , so we find that $(x,y)=\left(\frac{5}{19},\frac{16}{19}\right)\Longrightarrow a+b+c=5+16+19=\boxed{40}.$
~~pinkpig

## Video Solution
2008 AIME I #13
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.