# 2013 AMC 10A Problem 23

## Problem

In $\triangle ABC$ , $AB = 86$ , and $AC=97$ . A circle with center $A$ and radius $AB$ intersects $\overline{BC}$ at points $B$ and $X$ . Moreover $\overline{BX}$ and $\overline{CX}$ have integer lengths. What is $BC$ ?

$\textbf{(A)}\ 11\qquad\textbf{(B)}\ 28\qquad\textbf{(C)}\ 33\qquad\textbf{(D)}\ 61\qquad\textbf{(E)}\ 72$

## Solution 1 (Number Theoretic Power of a Point)
Let $BX = q$ , $CX = p$ , and $AC$ meets the circle at $Y$ and $Z$ , with $Y$ on $AC$ . Then $AZ = AY = 86$ . Using the Power of a Point (Secant-Secant Power Theorem), we get that $p(p+q) = 11(183) = 11 * 3 * 61$ . We know that $p+q>p$ , so $p$ is either $3$ , $11$ , or $33$ . We also know that $p>11$ by the triangle inequality on $\triangle ACX$ . Thus, $p$ is $33$ so we get that $BC = p+q = \boxed{\textbf{(D) }61}$ .

## Solution 2
Let $CX=x, BX=y$ . Let the circle intersect $AC$ at $D$ and the diameter including $AD$ intersect the circle again at $E$ . Use power of a point on point C to the circle centered at A.
So $CX \cdot CB=CD \cdot CE \Rightarrow x(x+y)=(97-86)(97+86) \Rightarrow x(x+y)=3*11*61$ .
Obviously $x+y>x$ so we have three solution pairs for $(x,x+y)=(1,2013),(3,671),(11,183),(33,61)$ . By the Triangle Inequality, only $x+y=61$ yields a possible length of $BX+CX=BC$ .
Therefore, the answer is $\boxed{\textbf{(D) }61}$ .

## Solution 3
[asy] unitsize(2); import olympiad; import graph; pair A,B,C,D,E; A = (0,0); B = (70,51); C = (97,0); D = (82,29); E = (76,40); draw(Circle((0,0),86.609)); draw(A--B--C--A); draw(A--B--E--A); draw(A--D); dot(A); dot(B,blue); dot(C); dot(D,blue); dot(E); label("A",A,S); label("B",B,NE); label("C",C,S); label("D",D,NE); label("E",E,NE); label("86",(A+B)/2,NW); label("86",(A+D)/2,SE); label("97",(A+C)/2,S); label("h",(A+E)/2,N); label("k",(E+D)/2,NE); label("k",(B+E)/2,NE); label("m",(C+D)/2,NE); fill(anglemark(A,E,D,100),black); label("$90^\circ$",anglemark(A,E,D),3*S); [/asy]
We first draw the height of isosceles triangle $ABD$ and get two equations by the Pythagorean Theorem . First, $h^2 + k^2 = 86^2$ . Second, $h^2 + (k + m)^2 = 97^2$ . Subtracting these two equations, we get $2km + m^2 = 97^2 - 86^2 = (97 - 86)(97 + 86) = 2013$ . We then add $k^2$ to both sides to get $k^2 + 2km + m^2 = 2013 + k^2$ . We then complete the square to get $(k + m)^2 = 2013 + k^2$ . Because $k$ and $m$ are both integers, we get that $2013 + k^2$ is a square number. Simple guess and check reveals that $k = 14$ . Because $k$ equals $14$ , therefore $m = 33$ . We want $\overline{BC} = 2k + m$ , so we get that $\overline{BC} = \boxed{(D)~61}$ .
$\phantom{solution and diagram by bobjoe123}$

## Solution 4
Let $E$ be the foot of the altitude from $A$ to $BX.$ Since $\triangle ABX$ is isosceles $AX=AB=86,EB=EX,$ and the answer is $EC+EB=EC+EX.$ $(EC+EX)(EC-EX)=EC^2-EX^2=(97^2-AE^2)-(86^2-AE^2)=97^2-86^2=2013$ by the Pythagorean Theorem. Only $EC+EX=\boxed{(D)~61}$ is a factor of $2013$ such that $97>EC+EX>EC-EX=\frac{2013}{EC+EX}.$
~dolphin7

## Solution 5
We can apply Stewarts to $\triangle{ABC}$ with cevian $AX.$ If we let $BX = b$ and $CX = c,$ We can write the equation, \[bc(b+c) + 86^2(b+c) = 97^2(b) + 86^2(c).\] Now we do a clever set of changes to factor, \[bc(b+c) = 97^2(b) + 86^2(c) - 86^2(b+c) = 97^2(b)+86^2(c-(b+c)).\] \[bc(b+c)=97^2(b)+86^2(-b) = b(97^2-86^2).\] \[c(b+c) = 97^2 - 86^2 = 11\cdot 183 = 3 \cdot 11 \cdot 61.\] Now we can just use the factors of $3 \cdot 11 \cdot 61$ to find what $c$ is and an allowed value of $b+c.$ Using triangle inequality we have \[11 < BC = b+c < 183.\] Therefore applying these restrictions the only value of $b+c$ that works is $\boxed{61}$ with corresponding values of $c=33$ and $b = 28.$
~ mathkiddus

## Solution 6 (Law of Cosines)
Let $x = BC$ , $y = XC$ , and $\theta = \angle BCA = \angle XCA$ . Using law of cosines on $\triangle ABC$ and $\triangle AXC$ we get \[\cos(\theta) = \frac{97^2-86^2 + x^2}{2\cdot97x} = \frac{97^2-86^2 + y^2}{2\cdot97y}\] \[(2013 + x^2)y = (2013 + y^2)x\] \[2013(x-y) = xy(x-y)\] Because $x-y = \overline{BX}$ , we know $x-y$ is nonzero, so \[xy = 2013\] Now you can list factors of 2013 and use the triangle innequlity as above solutions to get $x = \boxed{(D)~61}$

## Video Solution by Richard Rusczyk
https://www.youtube.com/watch?v=f1nxu8MWWKc

## Video Solution by OmegaLearn
https://youtu.be/NsQbhYfGh1Q?t=2692
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .