# 2020 AIME I Problem 8

## Problem

A bug walks all day and sleeps all night. On the first day, it starts at point $O$ , faces east, and walks a distance of $5$ units due east. Each night the bug rotates $60^\circ$ counterclockwise. Each day it walks in this new direction half as far as it walked the previous day. The bug gets arbitrarily close to the point $P$ . Then $OP^2=\tfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1 (Coordinates)
[asy] size(8cm); pair O, A, B, C, D, F, G, H, I, P, X; O = (0, 0); A = (5, 0); X = (8, 0); P = (5, 5 / sqrt(3)); B = rotate(-120, A) * ((O + A) / 2); C = rotate(-120, B) * ((A + B) / 2); D = rotate(-120, C) * ((B + C) / 2); F = rotate(-120, D) * ((C + D) / 2); G = rotate(-120, F) * ((D + F) / 2); H = rotate(-120, G) * ((F + G) / 2); I = rotate(-120, H) * ((G + H) / 2); draw(O -- A -- B -- C -- D -- F -- G -- H -- I); draw(A -- X, dashed); markscalefactor = 0.05; path angle = anglemark(X, A, B); draw(angle); dot(P); dot(O); dot(A); dot(B); dot(C); dot(D); label("$O$", O, W); label("$P$", P, E); label("$A$", A, S); label("$B$", B, E); label("$C$", C, E); label("$D$", D, W); label("$60^\circ$", angle, ENE*3); [/asy]
We notice that the moves cycle every 6 moves, so we plot out the first 6 moves on the coordinate grid with point $O$ as the origin. We will keep a tally of the x-coordinate and y-coordinate separately. Then, we will combine them and account for the cycling using the formula for an infinite geometric series.
First move: The ant moves right $5$ . Second move: We use properties of a $30-60-90$ triangle to get $\frac{5}{4}$ right, $\frac{5\sqrt{3}}{4}$ up. Third move: $\frac{5}{8}$ left, $\frac{5\sqrt{3}}{8}$ up. Fourth move: $\frac{5}{8}$ left. Fifth move: $\frac{5}{32}$ left, $\frac{5\sqrt{3}}{32}$ down. Sixth move: $\frac{5}{64}$ right, $\frac{5\sqrt{3}}{64}$ down.
Total of x-coordinate: $5 + \frac{5}{4} - \frac{5}{8} - \frac{5}{8} - \frac{5}{32} + \frac{5}{64} = \frac{315}{64}$ . Total of y-coordinate: $0 + \frac{5\sqrt{3}}{4} + \frac{5\sqrt{3}}{8} + 0 - \frac{5\sqrt{3}}{32} - \frac{5\sqrt{3}}{64} = \frac{105\sqrt{3}}{64}$ .
After this cycle of six moves, all moves repeat with a factor of $(\frac{1}{2})^6 = \frac{1}{64}$ . Using the formula for a geometric series, multiplying each sequence by $\frac{1}{1-\frac{1}{64}} = \frac{64}{63}$ will give us the point $P$ .
Now, knowing the initial $x$ and $y,$ we plug this into the geometric series formula ( $\frac{a}{1-r}$ ), and we get $\frac{315}{64} \cdot \frac{64}{63} = 5$ , $\frac{105\sqrt{3}}{64} \cdot \frac{64}{63} = \frac{5\sqrt{3}}{3}$ . Therefore, the coordinates of point $P$ are $(5,\frac{5\sqrt{3}}{3})$ , so using the Pythagorean Theorem, $OP^2 = \frac{100}{3}$ , for an answer of $\boxed{103}$ .
-molocyxu

## Solution 2 (Complex)
We place the ant at the origin of the complex plane with its first move being in the positive real direction. Then the ant's journey can be represented as the infinite series \[5\left(1 + \frac{e^{\frac{i\pi}{3}}}{2} + \left(\frac{e^{\frac{i\pi}{3}}}{2}\right)^2 + \cdots\right)\] Using the formula for an infinite geometric series, this is equal to \[\frac{5}{1 - \frac12e^{\frac{i\pi}{3}}} = \frac{5}{1 - \frac{1 + i\sqrt{3}}{4}} = \frac{20}{3 - i\sqrt{3}} = 5 + \frac{5i\sqrt{3}}{3}\] We are looking for the square of the modulus of this value: \[\left|\frac{5 + 5i\sqrt{3}}{3}\right|^2 = 25 + \frac{25}{3} = \frac{100}{3}\] so the answer is $100 + 3 = \boxed{103}$ .

## Solution 3 (Solution 1 Faster)
The ant goes in the opposite direction every $3$ moves, going $(1/2)^3=1/8$ the distance backwards. Using geometric series, he travels $1-1/8+1/64-1/512...=(7/8)(1+1/64+1/4096...)=(7/8)(64/63)=8/9$ the distance of the first three moves over infinity moves. Now, we use coordinates meaning $(5+5/4-5/8, 0+5\sqrt3/4+5\sqrt3/8)$ or $(45/8, 15\sqrt3/8)$ . Multiplying these by $8/9$ , we get $(5, 5\sqrt3/3)$ $\implies$ $\boxed{103}$ .
~Lcz

## Solution 4 (Official MAA 1)
Suppose that the bug starts at the origin $(0,0)$ and travels a distance of $a$ units due east on the first day, and that there is a real number $r$ with $0<r < 1$ such that each day after the first, the bug walks $r$ times as far as the previous day. On day $n$ , the bug travels along the vector $\pmb v_{n}$ that has magnitude $ar^{n-1}$ and direction $\langle\cos(n\cdot 60^\circ),\sin(n\cdot 60^\circ)\rangle$ . Then $P$ is the terminal point of the infinite sum of the vectors $\pmb v_{1}+\pmb v_{2}+\pmb v_3+\cdots$ . The $x$ -coordinate of this sum is \[a\big(\!\cos0^\circ+r\cos60^\circ + r^{2}\cos120^\circ+r^{3}\cos180^\circ+r^{4}\cos240^\circ\] \[+r^{5}\cos300^\circ+r^{6}\cos360^\circ+\cdots\big).\] Because the angles repeat after 6 terms, this sum is equal to \[aS(1+r^{6}+r^{12}+r^{18}+\cdots)=\frac{aS}{1-r^{6}},\] where \[S=\cos0^\circ+r\cos60^\circ + r^{2}\cos120^\circ+r^{3}\cos180^\circ+r^{4}\cos240^\circ+ r^{5}\cos300^\circ.\] Similarly, the $y$ -coordinate of $P$ will be ${\frac{aT}{1-r^{6}}}$ , where \[T=\sin0^\circ+r\sin60^\circ + r^{2}\sin120^\circ+r^{3}\sin180^\circ+r^{4}\sin240^\circ+ r^{5}\sin300^\circ.\] In this case $r=\frac12$ and $a = 5$ , so \[S=1+\frac14-\frac18-\frac18-\frac1{32}+\frac1{64}=\frac{63}{64},\] \[T=0+\frac{\sqrt3}4+\frac{\sqrt3}8+0-\frac{\sqrt3}{32}-\frac{\sqrt3}{64}=\frac{21\sqrt3}{64},\] and the coordinates of $P$ are \[\left(\frac{5S}{1-\frac1{64}}, \frac{5T}{1-\frac1{64}}\right)=\left(5,\frac{5\sqrt3}{3}\right).\] Thus the square of the distance from the origin to $P$ is $25+\frac{25}3=\frac{100}3$ . The requested sum is $100+3=\boxed{103}$ .

## Solution 5 (Official MAA 2)
Let point $O$ be the origin in the complex plane. Point $P$ is the complex sum $5(1+z+z^2+\cdots) = \frac{5}{1-z}$ , where $z=\frac{1+i\sqrt3}4$ . The distance squared is \[{OP}^2=\left|\frac5{1-\frac{1+i\sqrt3}4}\right|^{2}= \frac{(4\cdot5)^2}{\left|4-(1+i\sqrt3)\right|^2}=\frac{400}{9+3}=\frac{100}3.\] Hence the answer is $100 + 3 = \boxed{103}$ .

## Solution 6 (No coordinates, but basically using the same idea as Solution 1)
The bug goes forward and backward in three directions: straight east, northeast, and northwest. It travels $5-\frac{5}{8}+\frac{5}{64}-\cdots=\frac{40}{9}$ units east. Thus, it goes northeast $\frac{\frac{40}{9}}{2}=\frac{20}{9}$ units northeast and $\frac{10}{9}$ units northwest. Now, the bug travels a total of $\frac{40}{9}+\frac{10}{9}-\frac{5}{9}=\frac{45}{9}=5$ units east and a total of $\frac{10\sqrt{3}}{9}+\frac{5\sqrt{3}}{9}=\frac{15\sqrt{3}}{9}=\frac{5\sqrt{3}}{3}$ units north because of the 30-60-90 right triangles formed. Now, $OP^2=5^2+\frac{5^2}{3}=\frac{100}{3}$ by the Pythagorean Theorem, and the answer is $\boxed{103}$ .
-integralarefun

## Solution 7
The bug's bearings on each traversal are $0^\circ, 60^\circ, 120^\circ,$ and so on; in general, the $n-$ th traversal has length $5\cdot (1/2)^{n-1}$ and bearing $60(n-1).$ This means that the $x$ and $y$ displacements for the $n-$ th traversal are
\[(\Delta x_n, \Delta y_n)=(5\cdot (1/2)^{n-1}\cos (60(n-1))^\circ,5\cdot (1/2)^{n-1}\sin (60(n-1))^\circ).\]
Summing this over all the displacements, we get
\[x_P=\sum_{n=1}^{\infty} 5\cdot (1/2)^{n-1}\cos (60(n-1))^\circ, y_P=\sum_{n=1}^{\infty} 5\cdot (1/2)^{n-1}\sin (60(n-1))^\circ.\]
We then have
\begin{align} OP^2 &= x_P^2+y_P^2 \\ &=\sum_{n=1}^{\infty} (5\cdot (1/2)^{n-1}\cos ^2(60(n-1))^\circ) + (5\cdot (1/2)^{n-1}\sin ^2(60(n-1))^\circ) \\ &= \sum_{n=1}^{\infty} (5\cdot (1/2)^{n-1})^2(\cos ^2 (60(n-1))^\circ+\sin ^2 (60(n-1))^\circ) \\ &= \sum_{n=1}^{\infty} (25\cdot (1/4)^{n-1}) \\ &= \dfrac{25}{1-1/4} \\ &= 100/3. \end{align}
Thus, the answer is $100+3=\boxed{103}.$ --MenuThreeOne

## Video Solution with Motion in Python
https://youtu.be/RrMsMw_ZrBU
Moving Bug in AIME solution with python turtle scripts

## Video Solution
https://www.youtube.com/watch?v=BtMBSoZ3cMQ
-avn
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .