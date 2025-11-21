# 2004 AIME I Problem 10

## Problem

A circle of radius 1 is randomly placed in a 15-by-36 rectangle $ABCD$ so that the circle lies completely within the rectangle. Given that the probability that the circle will not touch diagonal $AC$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

## Solution

## Solution 1
The location of the center of the circle must be in the $34 \times 13$ rectangle that is one unit away from the sides of rectangle $ABCD$ . We want to find the area of the right triangle with hypotenuse one unit away from $\overline{AC}$ . Let this triangle be $A'B'C'$ .
Notice that $ABC$ and $A'B'C'$ share the same incenter ; this follows because the corresponding sides are parallel, and so the perpendicular inradii are concurrent, except that the inradii of $\triangle ABC$ extend one unit farther than those of $\triangle A'B'C'$ . From $A = rs$ , we note that $r_{ABC} = \frac{[ABC]}{s_{ABC}} = \frac{15 \cdot 36 /2}{(15+36+39)/2} = 6$ . Thus $r_{A'B'C'} = r_{ABC} - 1 = 5$ , and since the ratio of the areas of two similar figures is equal to the square of the ratio of their corresponding lengths, $[A'B'C'] = [ABC] \cdot \left(\frac{r_{A'B'C'}}{r_{ABC}}\right)^2 = \frac{15 \times 36}{2} \cdot \frac{25}{36} = \frac{375}{2}$ .
The probability is $\frac{2[A'B'C']}{34 \times 13} = \frac{375}{442}$ , and $m + n = \boxed{817}$ .

## Solution 2
Let the bisector of $\angle CAD$ be $AE$ , with $E$ on $CD$ . By the angle bisector theorem, $DE = 36/5$ . Since $\triangle AOR \sim \triangle AED$ ( $O$ is the center of the circle), we find that $AR = 5$ since $OR = 1$ . Also $AT = 35$ so $RT = OQ = 30$ .
We can apply the same principle again to find that $PT = 27/2$ , and since $QT = 1$ , we find that $PQ = 27/2 - 1 = 25/2$ . The locus of all possible centers of the circle on this "half" of the rectangle is triangle $\triangle OPQ$ . There exists another congruent triangle that is symmetric over $AC$ that has the same area as triangle $\triangle OPQ$ . $\triangle APQ$ has area $\frac {1}{2}\cdot OP \cdot PQ = \frac {1}{2}\cdot 30\cdot \frac {25}{2}$ , since $\angle OQP$ is right. Thus the total area that works is $30\cdot \frac {25}{2} = 375$ , and the area of the locus of all centers of any circle with radius 1 is $34\cdot 13 = 442$ . Hence, the desired probability is $\frac {375}{442}$ , and our answer is $\boxed {817}$ .

## Solution 3
Again, the location of the center of the circle must be in the $34 \times 13$ rectangle that is one unit away from the sides of rectangle $ABCD$ . We want to find the area of the right triangle with hypotenuse one unit away from $\overline{AC}$ .
Let $A$ be at the origin, $B (36,0)$ , $C (36,15)$ , $D (0,15)$ . The slope of $\overline{AC}$ is $\frac{15}{36} = \frac{5}{12}$ . Let $\triangle A'B'C'$ be the right triangle with sides one unit inside $\triangle ABC$ . Since $\overline{AC} || \overline{A'C'}$ , they have the same slope, and the equation of $A'C'$ is $y = \frac{5}{12}x + c$ . Manipulating, $5x - 12y + 12c = 0$ . We need to find the value of $c$ , which can be determined since $\overline{AC}$ is one unit away from $\overline{A'C'}$ . Since the diagonal contains the origin, we can use the distance from a point to the line formula at the origin:
\[\left|\frac{Ax + By + C}{\sqrt{A^2+B^2}}\right| = 1 \Longrightarrow \left|\frac{(5)(0) + (-12)(0) + 12c}{\sqrt{5^2 + (-12)^2}}\right| = 1\] \[c = \pm \frac{13}{12}\]
The two values of $c$ correspond to the triangle on top and below the diagonal. We are considering $A'B'C'$ which is below, so $c = -\frac{13}{12}$ . Then the equation of $\overline{A'C'}$ is $y = \frac{5}{12}x - \frac{13}{12}$ . Solving for its intersections with the lines $y = 1, x = 35$ (boundaries of the internal rectangle), we find the coordinates of $A'B'C'$ are at $A'\ (5,1)\ B'\ (35,1)\ C'\ (35,\frac{27}{2})$ . The area is $\frac{1}{2}bh = \frac{1}{2}(35-5)\left(\frac{27}{2} - 1\right) = \frac{375}{2}$ .
Finally, the probability is $\frac{2\cdot \mathrm{area\ of\ triangle}}{34 \times 13} = \frac{375}{442}$ , and $m + n = \boxed{817}$ .
For this solution, if you didn't know the formula for the distance from a point to a line, you can use similar triangles to get the ratio:
$\frac{1}{36}=\frac{c}{39}$
This yields $c=\frac{13}{12}$ .
These problems are copyrighted © by the Mathematical Association of America.