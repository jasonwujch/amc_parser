# 2017 AIME II Problem 3

## Problem

A triangle has vertices $A(0,0)$ , $B(12,0)$ , and $C(8,10)$ . The probability that a randomly chosen point inside the triangle is closer to vertex $B$ than to either vertex $A$ or vertex $C$ can be written as $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution 1
[asy] pair A,B,C,D,X,Z,P; A=(0,0); B=(12,0); C=(8,10); X=(10,5); Z=(6,0); P=(6,3.4); fill(B--X--P--Z--cycle,lightgray); draw(A--B--C--cycle); dot(A); label("$A$",A,SW); dot(B); label("$B$",B,SE); dot(C); label("$C$",C,N); draw(X--P,dashed); draw(Z--P,dashed); dot(X); label("$X$",X,NE); dot(Z); label("$Z$",Z,S); dot(P); label("$P$",P,NW); [/asy]
The set of all points closer to point $B$ than to point $A$ lie to the right of the perpendicular bisector of $AB$ (line $PZ$ in the diagram), and the set of all points closer to point $B$ than to point $C$ lie below the perpendicular bisector of $BC$ (line $PX$ in the diagram). Therefore, the set of points inside the triangle that are closer to $B$ than to either vertex $A$ or vertex $C$ is bounded by quadrilateral $BXPZ$ . Because $X$ is the midpoint of $BC$ and $Z$ is the midpoint of $AB$ , $X=(10,5)$ and $Z=(6,0)$ . The coordinates of point $P$ is the solution to the system of equations defined by lines $PX$ and $PZ$ . Using the point-slope form of a linear equation and the fact that the slope of the line perpendicular to a line with slope $m$ is $-\frac{1}{m}$ , the equation for line $PX$ is $y=\frac{2}{5}x+1$ and the equation for line $PZ$ is $x=6$ . The solution of this system is $P=\left(6,\frac{17}{5}\right)$ . Using the shoelace formula on quadrilateral $BXPZ$ and triangle $ABC$ , the area of quadrilateral $BXPZ$ is $\frac{109}{5}$ and the area of triangle $ABC$ is $60$ . Finally, the probability that a randomly chosen point inside the triangle is closer to vertex $B$ than to vertex $A$ or vertex $C$ is the ratio of the area of quadrilateral $BXPZ$ to the area of $ABC$ , which is $\frac{\frac{109}{5}}{60}=\frac{109}{300}$ . The answer is $109+300=\boxed{409}$ .

## Solution 2
Since we know the coordinates of all three vertices of the triangle, we can find the side lengths: $AB=12$ , $AC=2\sqrt{41}$ , and $BC=2\sqrt{29}$ . We notice that the point where the three distances are the same is the circumcenter - so we use one of the triangle area formulas to find the circumradius, since we know what the area is. \[\frac{12 \cdot 2\sqrt{41} \cdot 2\sqrt{29}}{4 \cdot R}=\frac{12 \cdot 10}{2}.\] We rearrange to get \[R=\frac{\sqrt{41} \cdot \sqrt{29}}{5}.\] [asy] draw((0,0)--(12,0)--(8,10)--(0,0)); draw((6,0)--(6,3.4)--(10,5)); draw((6,3.4)--(4,5)); label("$A$", (0,0), SW); label("$B$", (12,0), SE); label("$C$", (8, 10), N); label("$P$", (6, 3.4), NNE); label("$R$", (10, 5), NE); label("$S$", (6, 0), S); label("$T$", (4, 5), NW); [/asy] We know that $AP=\frac{\sqrt{41} \cdot \sqrt{29}}{5}$ , and $AS=6$ , so using the Pythagorean Theorem gives $SP=\frac{17}{5}$ . This means $[ASP]=[BSP]=\frac{17}{5} \cdot 6 \cdot \frac{1}{2} = \frac{51}{5}$ . Similarly, we know that $BP=\frac{\sqrt{41} \cdot \sqrt{29}}{5}$ , and $BR=\sqrt{29}$ , so we get that $PR=\frac{4\sqrt{29}}{5}$ , and so $[BRP]=[CRP]=\frac{4\sqrt{29}}{5} \cdot \sqrt{29} \cdot \frac{1}{2} = \frac{58}{5}$ . Lastly, we know that $CP=\frac{\sqrt{41} \cdot \sqrt{29}}{5}$ , and $CT=\sqrt{41}$ , so we get that $PT=\frac{2\sqrt{41}}{5}$ , and $[ATP]=[CTP]=\frac{2\sqrt{41}}{5} \cdot \sqrt{41} \cdot \frac{1}{2} = \frac{41}{5}$ . Therefore, our answer is $\frac{51+58}{2(51+58+41)}=\frac{109}{300} \rightarrow \boxed{409}$ .

## Solution 3
To start the problem, identify the two midpoints that connect $AB$ and $BC$ . This is because the midpoints of such lines is the mark at which the point will sway closer to vertex $A$ / $C$ or vertex $B$ . The midpoint of $AB$ is $(6,0)$ , and the midpoint of $BC$ is $(10,5)$ . Then, determine the line at which the distance between vertex $B$ and vertex $C$ are the same. Assuming that $x$ is the real value of $x$ and $y$ is the real value of $y$ , we can create a simple equation:
$\sqrt{|x-8|^2 + (10-y)^2}$ = $\sqrt{(12-x)^2 + y^2}$
where the left side of the equation is for the distance to vertex $C$ and the right side of the equation is the distance to vertex $B$ .
Squaring both sides and then distributing, we get
$x^2 - 16x + 64 + y^2 - 20y + 100 = x^2 - 24x + 144 + y^2$ .
Notice that $(x-8)^2 = (-x+8)^2$ , and thus there is no need to create another equation.
Simplifying, we get $8x + 20 = 20y$ .
Divide both sides by 20, then simplify, and the line that represents equivalent distance between vertex $B$ and vertex $C$ is $y = \frac{2x}{5} + 1$ .
This line starts at the midpoint of $BC$ , which is $(10,5)$ , and ends at the line $x=6$ , as $x=6$ represents equivalent distance between vertex $A$ and vertex $B$ . Plug in $x=6$ to the equation $y = \frac{2x}{5} + 1$ , and we get $y = \frac{17}{5}$ . Now that we have our four points that are $(6,0), (6,\frac{17}{5}), (10,5)$ , and $(12,0)$ , we can calculate the area of the quadrilateral in which a point is closer to vertex $B$ as opposed to either vertex $A$ or vertex $C$ . Simply draw a rectangle that has the points $(6,0), (6,5), (12,5)$ and $(12,0)$ , and then subtract the two triangles that appear in between.
Thus, the area of the quadrilateral is $6\cdot5 - (\frac{\frac{8}{5}\cdot4}{2} + \frac{5\cdot2}{2}) \rightarrow 30 - \frac{41}{5} = \frac{109}{5}$ . Since the problem asks us for the probability that a point chosen inside the triangle is inside the quadrilateral, and because the area of $\triangle ABC$ is $\frac{12\cdot10}{2} = 60$ , the probability is $\frac{\frac{109}{5}}{60}=\frac{109}{300}$ , which means the final answer is $109+300=\boxed{409}$ .
Solution by IronicNinja~

## Solution 4 (Shoelace Theorem/Formula)
Calculate the area of the triangle using the Shoelace Theorem on $(0,0), (12,0), (8,10)$ \[\frac{1}{2}|(0+120+0)-(0+0+0)|=60\]
Get the four points $(6,0), (6,\frac{17}{5}), (10,5)$ , and $(12,0)$ by any method from the above solutions. Then use the Shoelace Theorem to find the area of the region we want: \[\frac{1}{2}|(0+60+34+0)-(0+0+30+\frac{102}{5})|=\frac{109}{5}\]
Therefore the probability is $\frac{\frac{109}{5}}{60}=\frac{109}{300}$ . Thus giving the final answer of $109+300=\boxed{409}$ .
Solution by phoenixfire

## Solution 5
Draw the circumradii from the circumcenter to the three vertices. Drop perpendicular from the circumcenter to the sides. Note that since the triangle is isosceles, the perpendicular are in fact perpendicular bisectors. Therefore the region containing the points closer to B are in $\triangle{OBP_{1}} , \triangle{OBP_{2}}$ where $O$ is the circumcenter and $P_{1}, P_{2}$ points of contact of the perpendiculars and the sides. Therefore our fraction is $\frac{109}{300}$ . Our answer is then $\boxed{409}$ .
~ Prabh1512 (Edit by GeoWhiz4536)

## Solution 6
Using the same graph and methods as Solution 1, find the coordinates of $P$ , $X$ , $B$ , and $Z$ . Also, note that angles $PXB$ and $PZB$ are right angles, so $PXBZ$ is a cyclic quadrilateral. Then, use Brahmagupta's formula to determine the area of the quadrilateral, which is $\frac{109}{5}$ . Then find the area of triangle $ABC$ , which is $60$ . The probability is $\frac{109}{300}$ . Finally, we get our answer of $\boxed{409}$
~BLOATED_BAGEL ~minor edit by Mathkiddie
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .