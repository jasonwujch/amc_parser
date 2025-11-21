# 2000 AIME II Problem 11

## Problem

The coordinates of the vertices of isosceles trapezoid $ABCD$ are all integers, with $A=(20,100)$ and $D=(21,107)$ . The trapezoid has no horizontal or vertical sides, and $\overline{AB}$ and $\overline{CD}$ are the only parallel sides. The sum of the absolute values of all possible slopes for $\overline{AB}$ is $m/n$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
For simplicity, we translate the points so that $A$ is on the origin and $D = (1,7)$ . Suppose $B$ has integer coordinates; then $\overrightarrow{AB}$ is a vector with integer parameters (vector knowledge is not necessary for this solution). We construct the perpendicular from $A$ to $\overline{CD}$ , and let $D' = (a,b)$ be the reflection of $D$ across that perpendicular. Then $ABCD'$ is a parallelogram , and $\overrightarrow{AB} = \overrightarrow{D'C}$ . Thus, for $C$ to have integer coordinates, it suffices to let $D'$ have integer coordinates. [1]
Let the slope of the perpendicular be $m$ . Then the midpoint of $\overline{DD'}$ lies on the line $y=mx$ , so $\frac{b+7}{2} = m \cdot \frac{a+1}{2}$ . Also, $AD = AD'$ implies that $a^2 + b^2 = 1^2 + 7^2 = 50$ . Combining these two equations yields
\[a^2 + \left(7 - (a+1)m\right)^2 = 50\]
Since $a$ is an integer, then $7-(a+1)m$ must be an integer. There are $12$ pairs of integers whose squares sum up to $50,$ namely $( \pm 1, \pm 7), (\pm 7, \pm 1), (\pm 5, \pm 5)$ . We exclude the cases $(\pm 1, \pm 7)$ because they lead to degenerate parallelograms (rectangle, line segment, vertical and horizontal sides). Thus we have
\[7 - 8m = \pm 1, \quad 7 + 6m = \pm 1, \quad 7 - 6m = \pm 5, 7 + 4m = \pm 5\]
These yield $m = 1, \frac 34, -1, -\frac 43, 2, \frac 13, -3, - \frac 12$ . Therefore, the corresponding slopes of $\overline{AB}$ are $-1, -\frac 43, 1, \frac 34, -\frac 12, -3, \frac 13$ , and $2$ . The sum of their absolute values is $\frac{119}{12}$ . The answer is $m+n= \boxed{131}$
^ In other words, since is a parallelogram, the difference between the x-coordinates and the y-coordinates of and are, respectively, the difference between the x-coordinates and the y-coordinates of and . But since the latter are integers, then the former are integers also, so has integer coordinates iff has integer coordinates.
Note: It may not seem like we considered that the coordinates of $B$ have to be integers, but since the slopes of $\overline{AB}$ are all rational, we can just extend $\overline{AB}$ by some arbitrary amount so that $B$ becomes a lattice point, which won't affect the position of $D'$ . ~inaccessibles

## Solution 2
A very natural solution: Shift $A$ to the origin. Suppose point $B$ is $(x, kx)$ . Note $k$ is the slope we're looking for. Note that point $C$ must be of the form: $(x \pm 1, kx \pm 7)$ or $(x \pm 7, kx \pm 1)$ or $(x \pm 5, kx \pm 5)$ . Note that we want the slope of the line connecting $D$ and $C$ so also be $k$ , since $AB$ and $CD$ are parallel. Instead of dealing with the 12 cases, we consider point $C$ of the form $(x \pm Y, kx \pm Z)$ where we plug in the necessary values for $Y$ and $Z$ after simplifying. Since the slopes of $AB$ and $CD$ must both be $k$ , $\frac{7 - kx \pm Z}{1 - x \pm Y} = k \implies k = \frac{7 \pm Z}{1 \pm Y}$ . Plugging in the possible values of $\pm 7, \pm 1, \pm 5$ in their respective pairs and ruling out degenerate cases, we find the sum is $\frac{119}{12} \implies m + n = \boxed{131}$ - whatRthose
(Note: This Solution is a lot faster if you rule out $(Y, Z) = (1, 7)$ due to degeneracy.)
These problems are copyrighted © by the Mathematical Association of America.