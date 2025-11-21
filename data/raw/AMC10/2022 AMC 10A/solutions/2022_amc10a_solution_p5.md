# 2022 AMC 10A Problem 5

## Problem

Square $ABCD$ has side length $1$ . Points $P$ , $Q$ , $R$ , and $S$ each lie on a side of $ABCD$ such that $APQCRS$ is an equilateral convex hexagon with side length $s$ . What is $s$ ?

$\textbf{(A) } \frac{\sqrt{2}}{3} \qquad \textbf{(B) } \frac{1}{2} \qquad \textbf{(C) } 2 - \sqrt{2} \qquad \textbf{(D) } 1 - \frac{\sqrt{2}}{4} \qquad \textbf{(E) } \frac{2}{3}$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(200); real s = 2-sqrt(2); pair A, B, C, D, P, Q, R, S; A = (0,1); B = (1,1); C = (1,0); D = (0,0); P = A + (s,0); Q = B - (0,1-s); R = C - (s,0); S = D + (0,1-s); fill(A--P--Q--C--R--S--cycle,yellow); draw(A--B--C--D--cycle^^P--Q^^R--S); dot("$A$",A,NW,linewidth(4)); dot("$B$",B,NE,linewidth(4)); dot("$C$",C,SE,linewidth(4)); dot("$D$",D,SW,linewidth(4)); dot("$P$",P,N,linewidth(4)); dot("$Q$",Q,E,linewidth(4)); dot("$R$",R,(0,-1),linewidth(4)); dot("$S$",S,W,linewidth(4)); label("$s$",midpoint(A--P),N,red); label("$s$",midpoint(P--Q),NE,red); label("$s$",midpoint(Q--C),E,red); label("$s$",midpoint(C--R),(0,-1),red); label("$s$",midpoint(R--S),SW,red); label("$s$",midpoint(S--A),W,red); [/asy] ~MRENTHUSIASM

## Solution 1
Note that $BP=BQ=DR=DS=1-s.$ It follows that $\triangle BPQ$ and $\triangle DRS$ are congruent isosceles right triangles.
In $\triangle BPQ,$ we have $PQ=BP\sqrt2,$ or \begin{align*} s &= (1-s)\sqrt2 \\ s &= \sqrt2 - s\sqrt2 \\ \left(\sqrt2+1\right)s &= \sqrt2 \\ s &= \frac{\sqrt2}{\sqrt2 + 1}. \end{align*} Therefore, the answer is \[s = \frac{\sqrt2}{\sqrt2 + 1}\cdot\frac{\sqrt2 - 1}{\sqrt2 - 1} = \boxed{\textbf{(C) } 2 - \sqrt{2}}.\] ~MRENTHUSIASM

## Solution 2
Since it is an equilateral convex hexagon, all sides are the same, so we will call the side length $x$ . Notice that $(1-x)^2+(1-x)^2 = x^2$ . We can solve this equation which gives us our answer. \begin{align*} 1+x^2-2x+1+x^2-2x &= x^2 \\ 2x^2-4x+2 &= x^2 \\ x^2-4x+2 &= 0 \\ \end{align*}
We then use the quadratic formula which gives us:
\begin{align*} x &= \frac{4\:\pm\sqrt{4^2-4\cdot 1\cdot 2}}{2\cdot 1} \\ &= \frac{4\:\pm\sqrt{8}}{2} \\ &= \frac{4\:\pm2\sqrt{2}}{2} \\ \end{align*}
Then we simplify it by dividing and crossing out 2 which gives us $2\pm{\sqrt2}$ and that gives us $\boxed{\textbf{(C) }2-{\sqrt2}}$ .
~ orenbad

## Solution 3 (Area)
We can find areas in terms of $s.$ From the diagram, draw in segments $SP$ and $RQ.$ We then have two non-shaded triangles, two shaded triangles, and a rectangle.
The non-shaded triangles have leg lengths of $1-s,$ so they each have area $\frac{(1-s)^2}{2}.$ Therefore, the total area of the two triangles is $(1-s)^2.$
The shaded triangles have side lengths $s,$ so they each have area $\frac{s^2}{2}.$ Then, we get that their combined area is $s^2.$
Looking at the rectangle, we find that $SP=RQ=s\sqrt2,$ from 45-45-90 triangles $APS$ and $CRQ.$ Multiplying this with the other side length $s,$ we see that the rectangle has area $s^2\sqrt2.$
These three expressions of area sum up to the big square, which has area 1. So, we add them up and solve:
\begin{align*} (1-s)^2+s^2+s^2\sqrt2=&~1 \\ s^2-2s+1+s^2+s^2\sqrt2=&~1 \\ 2s^2+s^2\sqrt2-2s=&~0 \\ s((2+\sqrt2)s-2)=&~0 \\ \end{align*}
$s$ cannot be 0, since it represents a positive side length. This means that $s$ satisfies $(2+\sqrt2)s-2=0.$ Solving, we see that
\[s=\frac{2}{2+\sqrt2}=\frac{2}{2+\sqrt2}\cdot\frac{2-\sqrt2}{2-\sqrt2}=\frac{4-2\sqrt2}{2}=\boxed{\textbf{(C) }2-{\sqrt2}}.\]
~UltimateDL

## Solution 4 (Pythagorean Theorem)
A corner of the square gives a right triangle (e.g. $\triangle DRS$ ) with legs $1-s$ and hypotenuse $s$ . It follows that
\begin{align*} 2(1-s)^2&=s^2 \\ s^2-4s+2&=0 \\ \end{align*}
Completing the square gives
\begin{align*} s^2-4s+4&=2 \\ (s-2)^2&=2 \\ s&=\pm \sqrt{2}+2 \\ \end{align*}
The only answer choice that appears in our solution is $-\sqrt{2}+2$ , or $\boxed{\textbf{(C) }2-{\sqrt2}}$ .
~MrThinker

## Video Solution 1 (Quick and Easy)
https://youtu.be/uXG8xTGwx-8
~Education, the Study of Everything

## Video Solution 2
https://youtu.be/P4Oiyf_JjHo
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .