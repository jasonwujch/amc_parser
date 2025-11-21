# 2004 AIME I Problem 4

## Problem

Square $ABCD$ has sides of length 2. Set $S$ is the set of all line segments that have length 2 and whose endpoints are on adjacent sides of the square. The midpoints of the line segments in set $S$ enclose a region whose area to the nearest hundredth is $k$ . Find $100k$ .

## Solution
Without loss of generality, let $(0,0)$ , $(2,0)$ , $(0,2)$ , and $(2,2)$ be the vertices of the square. Suppose the endpoints of the segment lie on the two sides of the square determined by the vertex $(0,0)$ . Let the two endpoints of the segment have coordinates $(x,0)$ and $(0,y)$ . Because the segment has length 2, $x^2+y^2=4$ . Using the midpoint formula, we find that the midpoint of the segment has coordinates $\left(\frac{x}{2},\frac{y}{2}\right)$ . Let $d$ be the distance from $(0,0)$ to $\left(\frac{x}{2},\frac{y}{2}\right)$ . Using the distance formula we see that $d=\sqrt{\left(\frac{x}{2}\right)^2+\left(\frac{y}{2}\right)^2}= \sqrt{\frac{1}{4}\left(x^2+y^2\right)}=\sqrt{\frac{1}{4}(4)}=1$ . Thus the midpoints lying on the sides determined by vertex $(0,0)$ form a quarter- circle with radius 1.
The set of all midpoints forms a quarter circle at each corner of the square. The area enclosed by all of the midpoints is $4-4\cdot \left(\frac{\pi}{4}\right)=4-\pi \approx .86$ to the nearest hundredth. Thus $100\cdot k=\boxed{86}$

## Solution 2
If we imagine an arbitrary line with length $2$ connecting two sides of the square, we can draw the rectangle formed by drawing a perpendicular from where that line touches the square.
Drawing the other diagonal of the rectangle, it also has length two, and it bisects with the original line. Since their intersection is the midpoint of both lines, the distance from the corner to the midpoint is always $1$ , which forms a circle with radius $1$ centered at the corner of the square.
The area of the shape then follows from simple calculations.

## Solution 3
To imagine the area, think of a ladder with a length of $2$ sliding down a wall. It is known that as a ladder slides down a wall, its midpoint traces a quarter circle (if you don't believe me, try it with your pencil). There are $4$ quarter circles, so their area is one circle or $\pi$ . Thus, they enclose the area of the square minus the area of the quarter circles, which is $4-\pi \approx 0.86$ , so $100k = \boxed{086}$ . ~Extremelysupercooldude

## Solution 4
Consider the right triangle formed by the line segment and the vertex on the two sides it intersects. Since this right triangle has hypotenuse $2$ , its circumradius is $1$ . Since the circumcenter of a right triangle is the midpoint of the hypotenuse, the distance between the vertex of the square and the midpoint of the line segment is always $1$ . Thus, $S$ forms $4$ quarter-circles of radius $1$ around the vertices of the square. Combined, these quarter-circles have total area of $\pi$ , so the area enclosed by $S$ is $4-\pi \approx .86$ , and the answer is $\boxed{86}$ . ~A_MatheMagician
These problems are copyrighted © by the Mathematical Association of America.