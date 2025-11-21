# 2025 AIME I Problem 9

## Problem

The parabola with equation $y = x^2 - 4$ is rotated $60^\circ$ counterclockwise around the origin. The unique point in the fourth quadrant where the original parabola and its image intersect has $y$ -coordinate $\frac{a - \sqrt{b}}{c}$ , where $a$ , $b$ , and $c$ are positive integers, and $a$ and $c$ are relatively prime. Find $a + b + c$ .

### Graph

https://www.desmos.com/calculator/ci3vodl4vs

## Solution 1
We need to relate the rotation to something simpler because substituting the equation of the rotated parabola into the original will give us a quartic. [asy] size(300); import graph; // View window real L = 6; // Original parabola y = x^2 - 4 real f(real x){ return x^2 - 4; } // Rotation by +60 degrees about the origin pair rot60(pair P){ real ang = pi/3; return (P.x*cos(ang) - P.y*sin(ang), P.x*sin(ang) + P.y*cos(ang)); } // Axes draw((-L,0)--(L,0), gray(0.65), Arrows(4)); draw((0,-L)--(0,L), gray(0.65), Arrows(4)); // Plot original parabola real xmin=-3.5, xmax=3.5; path parab = graph(f, xmin, xmax); draw(parab, blue+1.2bp); // Build rotated parabola by sampling, then connecting smoothly int N=220; pair[] pts; for(int i=0; i<=N; ++i){ real x = xmin + (xmax - xmin)*i/N; pts.push(rot60((x, f(x)))); } path rpar = pts[0]; for(int i=1; i<=N; ++i) rpar = rpar..pts[i]; draw(rpar, red+1.2bp); // Line y = -sqrt(3) x draw((-L, sqrt(3)*L)--(L, -sqrt(3)*L), rgb(0,0.45,0)+1.2bp); // Vertices pair v1 = (0,-4); // original vertex pair v2 = rot60(v1); // rotated vertex dot(v1, blue+4bp); dot(v2, red+4bp); [/asy]
Notice that the vertices of the original parabola and its image are symmetrical about the angle bisector of the 60 degree rotation (shown in green).
The equation of this line is $y = -\tan60^\circ \cdot y = -\sqrt{3}x.$ This means that the point lying on this line and the original parabola must be the intersection of the new and original images since it won't change position with the rotation.
We substitute $y = x^2 - 4:$ \[x^2 - 4 = -\sqrt{3}x\] \[x = \frac{-\sqrt{3} + \sqrt{19}}{2}.\]
Then $y = (\frac{-\sqrt{3} + \sqrt{19}}{2})^2 - 4 = \frac{3 - \sqrt{57}}{2}.$ $57 + 3 + 2 = \boxed{62}.$
~ grogg007 , ~ mathkiddus , ~ athreyay

## Solution 2 (Similar to Solution 1)
Note that this question is equivalent to finding a point $B$ in the fourth quadrant, such that when a point $A$ on the graph of $y = x^2 - 4$ is rotated $60^\circ$ counterclockwise around the origin, it lands on $B$ , which is also on the graph.
The first thing to note is that point $A$ and $B$ must be equidistant to the origin. If we express the coordinates of $A$ as \((a, b)\), and the coordinates of $B$ as \((x, y)\), we have:
\(\|OA\|\) = \(\|OB\|\)
Which means that:
\(\sqrt{a^2 + b^2} = \sqrt{x^2 + y^2}\)
Since $b = a^2 - 4$ and $y = x^2 - 4$ , we have $a^2 = b + 4$ and $x^2 = y + 4$ , substituting this into the previous equation and squaring both sides yields:
\(2a^2 + 4 = 2x^2 + 4\)
Meaning that \(a^2 = x^2\), since $A$ and $B$ clearly cannot coincide, we must have \(a = -x\), since $y = x^2 - 4$ is an even function, this means that point $A$ and $B$ are just reflections of each other over the y axis. The angle between \(\overline{OA}\) and \(\overline{OB}\) is $60^\circ$ and $A$ and $B$ is symmetrical, the y axis should bisect the angle \angle AOB, i.e., the angle between \(\overline{OB}\) and the y axis is:
\[\frac{60^\circ}{2} = 30^\circ\]
Therefore the point $B$ must lie on the line \[y = -\sqrt{3}x\]
We have:
\[\begin{cases}y = x^2 - 4 \\ y = -\sqrt{3}x \end{cases}\]
\(x^2 - 4 = -\sqrt{3}x\)
Using the quadratic formula and keeping in mind that the x value is positive (since $B$ is in the fourth quadrant) yields \( x = \frac{\sqrt{19} - \sqrt{3}}{2} \).
Substituting into \[y = -\sqrt{3}x\] We get \[y=\frac{3-\sqrt{57}}{2}\implies \boxed{062}.\]
~ IDKHowtoaddsolution
The last part of this solution is essentially Solution 1.

## Video Solution
2025 AIME I #9
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .