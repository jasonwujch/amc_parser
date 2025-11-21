# 2010 AIME I Problem 8

## Problem

For a real number $a$ , let $\lfloor a \rfloor$ denote the greatest integer less than or equal to $a$ . Let $\mathcal{R}$ denote the region in the coordinate plane consisting of points $(x,y)$ such that $\lfloor x \rfloor ^2 + \lfloor y \rfloor ^2 = 25$ . The region $\mathcal{R}$ is completely contained in a disk of radius $r$ (a disk is the union of a circle and its interior). The minimum value of $r$ can be written as $\frac {\sqrt {m}}{n}$ , where $m$ and $n$ are integers and $m$ is not divisible by the square of any prime. Find $m + n$ .

## Solution
The desired region consists of 12 boxes, whose lower-left corners are integers solutions of $x^2 + y^2 = 25$ , namely $(\pm5,0), (0,\pm5), (\pm3,\pm4), (\pm4,\pm3).$ Since the points themselves are symmetric about $(0,0)$ , the boxes are symmetric about $\left(\frac12,\frac12\right)$ . The distance from $\left(\frac12,\frac12\right)$ to the furthest point on a box that lays on an axis, for instance $(6,1)$ , is $\sqrt {\frac {11}2^2 + \frac12^2} = \sqrt {\frac {122}4}.$ The distance from $\left(\frac12,\frac12\right)$ to the furthest point on a box in the middle of a quadrant, for instance $(5,4)$ , is $\sqrt {\frac92^2 + \frac72^2} = \sqrt {\frac {130}4}.$ The latter is the larger, and is $\frac {\sqrt {130}}2$ , giving an answer of $130 + 2 = \boxed{132}$ .

## Solution 2
When observing the equation $\lfloor x \rfloor ^2 + \lfloor y \rfloor ^2 = 25$ , it is easy to see that it is a circle graph. So, we can draw a coordinate plane and find some points.
In quadrant $1$ , $x < 6$ and $y < 6$ . Note that $\lfloor 5.999...\rfloor = 5$ , but if we add more $9's$ after the $5$ , it will get infinitely close to $6$ , so we can use $6$ as a bounding line. Also, with the same logic, when $x = 6$ , $y = 1$ (the equal sign represents as $x$ approaches..., not equal to...) So, in quadrant one, we have points $(6,1)$ and $(1,6)$ .
Moving to quadrant $2$ , we must note that $\lfloor -4.999...\rfloor = -5$ , so the circle will not be centered at $(0,0)$ . In quadrant 2, $y$ is still positive, so we can have $y = 1$ . When $y = 1$ , $x = -5$ , so we have our next point $(-5,1)$ . With this method, other points can be found in quadrants $3$ and $4$ .
Additionally, $3 ^2 + 4 ^2 = 5 ^2$ , and with the same approaching limit, we know that quadrant $1$ also has lattice points $(4,5)$ and $(5,4)$ . We need a point that passes through the circle's center (we don't need to find the center). If we focus on $(5,4)$ , the "opposite" point is $(-4,-3)$ located in quadrant 3.
Using the distance formula, we find that the distance between the two points is $\sqrt {130}$ . Since the line connecting those two points passes through the circle's center, it is the diameter. So, the radius can be found by dividing $\sqrt {130}$ by $2$ to get $\frac {\sqrt {130}}2$ , and $m+n=130 + 2 = \boxed{132}$ .
~hwan ~edited by ALANARCHERMAN
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .