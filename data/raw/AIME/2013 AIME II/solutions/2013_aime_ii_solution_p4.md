# 2013 AIME II Problem 4

## Problem

In the Cartesian plane let $A = (1,0)$ and $B = \left( 2, 2\sqrt{3} \right)$ . Equilateral triangle $ABC$ is constructed so that $C$ lies in the first quadrant. Let $P=(x,y)$ be the center of $\triangle ABC$ . Then $x \cdot y$ can be written as $\tfrac{p\sqrt{q}}{r}$ , where $p$ and $r$ are relatively prime positive integers and $q$ is an integer that is not divisible by the square of any prime. Find $p+q+r$ .

## Solution 1
The distance from point $A$ to point $B$ is $\sqrt{13}$ . The vector that starts at point A and ends at point B is given by $B - A = (1, 2\sqrt{3})$ . Since the center of an equilateral triangle, $P$ , is also the intersection of the perpendicular bisectors of the sides of the triangle, we need first find the equation for the perpendicular bisector to $\overline{AB}$ . The line perpendicular to $\overline{AB}$ through the midpoint, $M = \left(\dfrac{3}{2},\sqrt{3}\right)$ , $\overline{AB}$ can be parameterized by $\left(\dfrac{2\sqrt{3}}{\sqrt{13}}, \dfrac{-1}{\sqrt{13}}\right) t + \left(\dfrac{3}{2},\sqrt{3}\right)$ . At this point, it is useful to note that $\Delta BMP$ is a 30-60-90 triangle with $\overline{MB}$ measuring $\dfrac{\sqrt{13}}{2}$ . This yields the length of $\overline{MP}$ to be $\dfrac{\sqrt{13}}{2\sqrt{3}}$ . Therefore, $P =\left(\dfrac{2\sqrt{3}}{\sqrt{13}},\dfrac{-1}{\sqrt{13}}\right)\left(\dfrac{\sqrt{13}}{2\sqrt{3}}\right) + \left(\dfrac{3}{2},\sqrt{3}\right) = \left(\dfrac{5}{2}, \dfrac{5}{2\sqrt{3}}\right)$ . Therefore $xy = \dfrac{25\sqrt{3}}{12}$ yielding an answer of $p + q + r = 25 + 3 + 12 = \boxed{040}$ .

## Solution 2
Rather than considering the Cartesian plane, we use complex numbers. Thus A is 1 and B is $2 + 2\sqrt{3}i$ .
Recall that a rotation of $\theta$ radians counterclockwise is equivalent to multiplying a complex number by $e^{i\theta}$ , but here we require a clockwise rotation, so we multiply by $e^{-\frac{i\pi}{3}}$ to obtain C. Upon averaging the coordinates of A, B, and C, we obtain the coordinates of P, viz. $\left(\frac{5}{2}, \frac{5\sqrt{3}}{6}\right)$ .
Therefore $xy$ is $\frac{25\sqrt{3}}{12}$ and the answer is $25 + 12 + 3 = \boxed{040}$ .

## Solution 3
We can also consider the slopes of the lines. Midpoint $M$ of $AB$ has coordinates $\left(\frac{3}{2},\ \sqrt{3}\right)$ . Because line $AB$ has slope $2\sqrt{3}$ , the slope of line $MP$ is $-\frac{1}{2\sqrt{3}}$ (Because of perpendicular slopes).
Since $\Delta ABC$ is equilateral, and since point $P$ is the centroid, we can quickly calculate that $MP = \frac{\sqrt{39}}{6}$ . Then, define $\Delta x$ and $\Delta y$ to be the differences between points $M$ and $P$ . Because of the slope, it is clear that $\Delta x = 2\sqrt{3} \Delta y$ .
We can then use the Pythagorean Theorem on line segment $MP$ : $MP^2 = \Delta x^2 + \Delta y^2$ yields $\Delta y = -\frac{1}{2\sqrt{3}}$ and $\Delta x = 1$ , after substituting $\Delta x$ . The coordinates of P are thus $\left(\frac{5}{2},\ \frac{5\sqrt{3}}{6}\right)$ . Multiplying these together gives us $\frac{25\sqrt{3}}{12}$ , giving us $\boxed{040}$ as our answer.

## Solution 4
Since $AC$ will be segment $AB$ rotated clockwise $60^{\circ}$ , we can use a rotation matrix to find $C$ . We first translate the triangle $1$ unit to the left, so $A'$ lies on the origin, and $B' = (1, 2\sqrt{3})$ . Rotating clockwise $60^{\circ}$ is the same as rotating $300^{\circ}$ counter-clockwise, so our rotation matrix is $\begin{bmatrix} \cos{300^{\circ}} & -\sin{300^{\circ}}\\ \sin{300^{\circ}} & \cos{300^{\circ}}\\ \end{bmatrix} = \begin{bmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2}\\ -\frac{\sqrt{3}}{2} & \frac{1}{2}\\ \end{bmatrix}$ . Then $C' = \begin{bmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2}\\ -\frac{\sqrt{3}}{2} & \frac{1}{2}\\ \end{bmatrix} \cdot \begin{bmatrix} 1\\ 2\sqrt{3}\\ \end{bmatrix} = \begin{bmatrix} \frac{7}{2}\\ \frac{\sqrt{3}}{2}\\ \end{bmatrix}$ . Thus, $C = (\frac{9}{2}, \frac{\sqrt{3}}{2})$ . Since the triangle is equilateral, the center of the triangle is the average of the coordinates of the vertices. Then $P = (\frac{1 + 2 + \frac{9}{2}}{3}, \frac{2\sqrt{3} + \frac{\sqrt{3}}{2}}{3}) = (\frac{5}{2}, \frac{5\sqrt{3}}{6})$ . Our answer is $\frac{5}{2} \cdot \frac{5\sqrt{3}}{6} = \frac{25\sqrt{3}}{12}$ . $25 + 3 + 12 = \boxed{40}$

## Solution 5
We construct point $C$ by drawing two circles with radius $r = AB = \sqrt{13}$ . One circle will be centered at $A$ , while the other is centered at $B$ . The equations of the circles are:
$(x - 1)^2 + y^2 = 13$
$(x - 2)^2 + (y - 2\sqrt{3})^2 = 13$
Setting the LHS of each of these equations equal to each other and solving for $x$ yields after simplification:
$x = \frac{15}{2} - 2\sqrt{3}y$
Plugging that into the first equation gives the following quadratic in $y$ after simplification:
$y^2 - 2\sqrt{3}y + \frac{9}{4} = 0$
The quadratic formula gives $y = \frac{\sqrt{3}}{2}, \frac{3\sqrt{3}}{2}$ .
Since $x > 0$ and $x = \frac{15}{2} - 2\sqrt{3}y$ , we pick $y = \frac{\sqrt{3}}{2}$ in the hopes that it will give $x > 0$ . Plugging $y$ into the equation for $x$ yields $x = \frac{9}{2}$ .
Thus, $C(\frac{9}{2}, \frac{\sqrt{3}}{2})$ . Averaging the coordinates of the vertices of equilateral triangle $ABC$ will give the center of mass of the triangle.
Thus, $P(\frac{5}{2}, \frac{5\sqrt{3}}{6})$ , and the product of the coordinates is $\frac{25\sqrt{3}}{12}$ , so the desired quantity is $\boxed{040}$ .

## Solution 6
Labeling our points and sketching a graph we get that $C$ is to the right of $AB$ . Of course, we need to find $C$ . Note that the transformation from $A$ to $B$ is $[1,2\sqrt{3}]$ , and if we imagine a height dropped to $AB$ we see that a transformation from the midpoint $(\frac{3}{2},\sqrt {3})$ to $C$ is basically the first transformation, with $\frac{\sqrt{3}}{2}$ the magnitude and the x and y switched– then multiply the new y by -1. Then, applying this transformation of $[3,\frac{-\sqrt{3}}{2}]$ we get that $C=(\frac{9}{2},\frac{\sqrt{3}}{2})$ which means that $P=(\frac{5}{2},\frac{5\sqrt{3}}{6})$ . Then our answer is $\boxed{40}$ .

## Solution 7
Transform this into the complex plane and let $a=1, b=2+2\sqrt3 i$ . We know that 3 complex numbers $a,b,c$ form an equilateral triangle if $a^2+b^2+c^2=ab+bc+ac$ , so plugging in our values of $a,b$ , we get $8\sqrt3 i - 7 +c^2 = 2+2\sqrt3 i + (3+2\sqrt 3i)c.$ Solving for $c$ using Wolfram Alpha, we find that the solutions are $c=\frac 92 + \frac{i\sqrt3}{2}, -\frac 32 + \frac{3i\sqrt3}{2}$ . The first one is in the first quadrant, so $C\left( \frac 92, \frac{\sqrt3}{2} \right)$ . The center is the average of the coordinates and we find that it is $\left(\frac{5}2, \frac{5\sqrt3}{6} \right)$ . Then $xy = \frac{25\sqrt3}{12} \implies 40$ .
-bobthegod78, krwang, and Simplest14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .