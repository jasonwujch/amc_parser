# 2020 AIME II Problem 7

## Problem

Two congruent right circular cones each with base radius $3$ and height $8$ have the axes of symmetry that intersect at right angles at a point in the interior of the cones a distance $3$ from the base of each cone. A sphere with radius $r$ lies within both cones. The maximum possible value of $r^2$ is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution (Official MAA)
Consider the cross section of the cones and sphere by a plane that contains the two axes of symmetry of the cones as shown below. The sphere with maximum radius will be tangent to the sides of each of the cones. The center of that sphere must be on the axis of symmetry of each of the cones and thus must be at the intersection of their axes of symmetry. Let $A$ be the point in the cross section where the bases of the cones meet, and let $C$ be the center of the sphere. Let the axis of symmetry of one of the cones extend from its vertex, $B$ , to the center of its base, $D$ . Let the sphere be tangent to $\overline{AB}$ at $E$ . The right triangles $\triangle ABD$ and $\triangle CBE$ are similar, implying that the radius of the sphere is \[CE = AD \cdot\frac{BC}{AB} = AD \cdot\frac{BD-CD}{AB} =3\cdot\frac5{\sqrt{8^2+3^2}} = \frac{15}{\sqrt{73}}=\sqrt{\frac{225}{73}}.\] The requested sum is $225+73=298$ . [asy] unitsize(0.6cm); pair A = (0,0); pair TriangleOneLeft = (-6,0); pair TriangleOneDown = (-3,-8); pair TriangleOneMid = (-3,0); pair D = (0,-3); pair TriangleTwoDown = (0,-6); pair B = (-8,-3); pair C = IP(TriangleOneMid -- TriangleOneDown, B--D); pair EE = foot(C, A, B); real radius = arclength(C--EE); path circ = Circle(C, radius); draw(A--B--TriangleTwoDown--cycle); draw(B--D); draw(A--TriangleOneLeft--TriangleOneDown--cycle); draw(circ); draw(C--EE); draw(TriangleOneMid -- TriangleOneDown, gray); dot("$B$", B, W); dot("$E$", EE, NW); dot("$A$", A, NE); dot("$D$", D, E); dot("$C$", C, SE); [/asy]
Not part of MAA's solution, but this: https://www.geogebra.org/calculator/xv4nm97a is a good visual of the cones in GeoGebra.

## Solution (Incircles + Coordinate Bash)
[asy] unitsize(0.6cm); // Coordinates pair A = (0,0); pair B = (6,0); pair C = (0,6); // Calculate point C pair D = (3,8); pair E = (8,3); pair F = (144/73,384/73); // Draw triangles (cones) draw(A--B--D--cycle); draw(A--C--E--cycle); draw(incircle(A,E,F)); pair EE = foot(C, A, B); real radius = arclength(C--EE); path circ = Circle(C, radius); // Label points dot("$A$", A, NW); dot("$B$", B, SW); dot("$C$", C, NE); dot("$D$", D, SE); dot("$E$", E, SE); dot("$F$", F, NE); [/asy]
Let $A$ be the origin in the above diagram. Then $B$ is $(6,0)$ , $C$ is $(0,6)$ , $D$ is $(3,8)$ , and $E$ is $(8,3)$ . Also, it is easy to see that the inscribed sphere is simply the inscribed circle of $AEF$ . Then we want to find the intersection of $AD$ and $CE$ to determine the coordinates of point $F$ . Note that $AD$ is line $y=\frac{8}{3}x$ , and $CE$ is line $y=-\frac{3}{8}x+6$ . Then, you can see that these lines are perpendicular, indicating that $AEF$ is a right triangle with right angle at $F$ . Finding the intersection of the lines by solving the system, we get that $F$ is the point $(\frac{144}{73},\frac{384}{73})$ in this plane. Then, we can find the distances $EF$ and $AF$ by the distance formula, which are $\frac{55}{\sqrt{73}}$ and $\frac{48}{\sqrt{73}}$ respectively. Also, $AE=\sqrt{73}$ . Then, to find the radius of this triangle's incircle, we use the formula $a=rs$ from which we get that $r=\frac{15}{\sqrt{73}}$ and $r^2=\frac{225}{73} \implies \boxed{298}$ is the answer.
~SirAppel

## Solution (Clean analytic geometry)
Using the diagram above, we notice that the desired length is simply the distance between the point $C$ and $\overline{AB}$ . We can mark $C$ as $(3,3)$ since it is $3$ units away from each of the bases. Point $B$ is $(8,3)$ . Thus, line $\overline{AB}$ is $y = \frac{3}{8}x \Rightarrow 3x + 8y = 0$ . We can use the distance from point to line formula $\frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$ , where $x_0$ and $y_0$ are the coordinates of the point, and A, B, and C are the coefficients of the line in form $Ax + By + C = 0$ . Plugging everything in, we get \[\frac{|3(3) - 8(3)|}{\sqrt{8^2 + 3^2}} = \frac{15}{\sqrt{73}} \Rightarrow \frac{225}{73} \Rightarrow \boxed{298}\] .

## Solution 1: Graph paper coordbash
We graph this on graph paper, with the scale of $\sqrt{2}:1$ . So, we can find $OT$ then divide by $\sqrt{2}$ to convert to our desired units, then square the result. With 5 minutes' worth of coordbashing, we finally arrive at $298$ .
[asy] /* Geogebra to Asymptote conversion by samrocksnature, documentation at artofproblemsolving.com/Wiki go to User:Azjps/geogebra */ real labelscalefactor = 0.5; /* changes label-to-point distance */ pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */ pen dotstyle = black; /* point style */ real xmin = -8.325025958411356, xmax = 8, ymin = -0.6033105644019334, ymax = 12.237120576121757; /* image dimensions */ pen zzttqq = rgb(0.6,0.2,0); pen qqwuqq = rgb(0,0.39215686274509803,0); pen cqcqcq = rgb(0.7529411764705882,0.7529411764705882,0.7529411764705882); draw((5,11)--(0,0)--(-6,6)--cycle, linewidth(1) + zzttqq); draw((6,6)--(-5,11)--(0,0)--cycle, linewidth(1) + qqwuqq); draw((0.2328977836854361,5.767102216314564)--(0.4657955673708722,6)--(0.2328977836854361,6.232897783685436)--(0,6)--cycle, linewidth(1) + qqwuqq); /* draw grid of horizontal/vertical lines */ pen gridstyle = linewidth(0.7) + cqcqcq; real gridx = 1, gridy = 1; /* grid intervals */ for(real i = ceil(xmin/gridx)*gridx; i <= floor(xmax/gridx)*gridx; i += gridx) draw((i,ymin)--(i,ymax), gridstyle); for(real i = ceil(ymin/gridy)*gridy; i <= floor(ymax/gridy)*gridy; i += gridy) draw((xmin,i)--(xmax,i), gridstyle); /* end grid */ Label laxis; laxis.p = fontsize(10); xaxis(xmin, xmax, Ticks(laxis, Step = 1, Size = 2, NoZero),EndArrow(6), above = true); yaxis(ymin, ymax, Ticks(laxis, Step = 1, Size = 2, NoZero),EndArrow(6), above = true); /* draws axes; NoZero hides '0' label */ /* draw figures */ draw((5,11)--(0,0), linewidth(1) + zzttqq); draw((0,0)--(-6,6), linewidth(1) + zzttqq); draw((-6,6)--(5,11), linewidth(1) + zzttqq); draw((6,6)--(-5,11), linewidth(1) + qqwuqq); draw((-5,11)--(0,0), linewidth(1) + qqwuqq); draw((0,0)--(6,6), linewidth(1) + qqwuqq); draw((-3,3)--(5,11), linewidth(1)); draw((-5,11)--(3,3), linewidth(1)); draw(circle((0,6), 2.482817665807104), linewidth(1)); draw((0,6)--(2.2602739726027394,4.972602739726027), linewidth(1)); /* dots and labels */ dot((0,0),linewidth(1pt) + dotstyle); dot((3,3),dotstyle); dot((-3,3),dotstyle); dot((6,6),dotstyle); dot((-6,6),dotstyle); dot((5,11),dotstyle); dot((-5,11),dotstyle); dot((0,6),linewidth(1pt) + dotstyle); label("$O$", (0.059294254264342997,6.119672124650978), NE * labelscalefactor); dot((2.2602739726027394,4.972602739726027),linewidth(1pt) + dotstyle); label("$T$", (2.326166015469254,5.094921876435061), NE * labelscalefactor); clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle); /* end of picture */ [/asy]
~samrocksnature

## Solution 2
Using the graph drawn above in MAA solution, we see that $\sqrt{AC^2-r^2}$ + $\sqrt{BC^2-r^2}$ = $AB$ . $AB$ = $\sqrt{8^2+3^2}$ = $\sqrt{73}$ , $AC$ = 3 $\sqrt{2}$ , $AB$ = 5. Plugging in and solve for $r^2$ gives us $r^2$ = $\frac{225}{73}$ .
~S17209

## Video Solution
https://youtu.be/bz5N-jI2e0U?t=44

## Video Solution 2
https://www.youtube.com/watch?v=0XJddG43pIk ~ MathEx

## Video Solution 3
https://youtu.be/dHGXtB0FxXs
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .