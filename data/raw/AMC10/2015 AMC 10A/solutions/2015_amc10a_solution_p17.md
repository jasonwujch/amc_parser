# 2015 AMC 10A Problem 17

## Problem

A line that passes through the origin intersects both the line $x = 1$ and the line $y=1+ \frac{\sqrt{3}}{3} x$ . The three lines create an equilateral triangle. What is the perimeter of the triangle?

$\textbf{(A)}\ 2\sqrt{6} \qquad\textbf{(B)} \ 2+2\sqrt{3} \qquad\textbf{(C)} \ 6 \qquad\textbf{(D)} \ 3 + 2\sqrt{3} \qquad\textbf{(E)} \ 6 + \frac{\sqrt{3}}{3}$

## Solution 1
Since the triangle is equilateral and one of the sides is a vertical line, the triangle must have a horizontal line of symmetry, and therefore the other two sides will have opposite slopes. The slope of the other given line is $\frac{\sqrt{3}}{3}$ (which is must be, given 60 degree angle of the triangle, relative to vertical) so the third must be $-\frac{\sqrt{3}}{3}$ . Since this third line passes through the origin, its equation is simply $y = -\frac{\sqrt{3}}{3}x$ . To find two vertices of the triangle, plug in $x=1$ to both the other equations.
$y = -\frac{\sqrt{3}}{3}$
$y = 1 + \frac{\sqrt{3}}{3}$
We now have the coordinates of two vertices, $\left(1, -\frac{\sqrt{3}}{3}\right)$ and $\left(1, 1 + \frac{\sqrt{3}}{3}\right)$ . The length of one side is the distance between the y-coordinates, or $1 + \frac{2\sqrt{3}}{3}$ .
The perimeter of the triangle is thus $3\left(1 + \frac{2\sqrt{3}}{3}\right)$ , so the answer is $\boxed{\textbf{(D) }3 + 2\sqrt{3}}$
Note: We know that the slope for the third line must be $-\frac{\sqrt{3}}{3}$ , as the slope for the second given line is $\frac{\sqrt{3}}{3}$ . The slope is determined from two points on a line, and we pick one of the points to be the point where they intersect. Now, drawing the symmetric line, it splits the first line; x=1 into two equal parts. Now, the second point for the third and second lines have the same x coordinate, but opposite y coordinates.

## Solution 1 Different Approach
It is important to note that because \( \tan(x) \) represents the slope of a function, then \( \frac{\sqrt{3}}{3} \) is just \( \tan(30^\circ) \). Then, if we reflect \( \frac{\sqrt{3}}{3} x+1 \) over the line \( y=\frac{1}{2} \), we get \( y=-\frac{\sqrt{3}}{3}x \) as our new function.
Given that, we may resume with solution 1.
~Pinotation (I did not write solution 1)

## Solution 2
Draw a line from the y-intercept of the equation $y=1+ \frac{\sqrt{3}}{3} x$ perpendicular to the line $x=1$ . There is a square of side length 1 inscribed in the equilateral triangle. The problem becomes reduced to finding the perimeter of an equilateral triangle with a square of side length 1 inscribed in it. The side length is $2\left(\frac{1}{\sqrt{3}}\right) + 1$ . After multiplying the side length by 3 and rationalizing, you get $\boxed{\textbf{(D) }3 + 2\sqrt{3}}$ .

## Solution 3
Let the intersection point between the line $y = 1 + \frac{\sqrt{3}}{3}x$ and the line that crosses the origin be $P$ .
We drop an altitude from $P$ onto the line $x = 1$ . Since the overall triangle is an equilateral triangle, we are splitting the base (on $x=1$ ) in half. As the y-axis is parallel to the line $x=1$ , the altitude from P will also split the y-axis from $y=0$ to $y=1$ in half. From this, we can get that the y-value of P is $\frac{1}{2}$ .
Plugging this into the equation $y = 1 + \frac{\sqrt{3}}{3}x$ , we get that $x = -\frac{\sqrt{3}}{2}$ , and thus our height for the equilateral triangle is $1 + \frac{\sqrt{3}}{2}$ . Using that, we can calculate the perimeter to be $\boxed{\textbf{(D) }3 + 2\sqrt{3}}$ .

## Solution 4 (quick)
$1+\frac{\sqrt{3}}{3}x$ clearly must form a 60 degree angle with $x=1$ . The other line is the one that forms a $-60$ degree angle with $x=1$ . Thus, it must have slope $-\frac{\sqrt{3}}{3}$ , and equation $y-0=-\frac{\sqrt{3}}{3}(x-0)$ .
This equation, $x=1$ , and the x-axis form a 30-60-90 triangle. The length of the short leg is $0-(-\frac{\sqrt{3}}{3}(1))$ or $\frac{\sqrt{3}}{3}$ . Multiplying by 2 gives the hypotenuse and then by 3 gives the perimeter, $\boxed{\textbf{(D) }3 + 2\sqrt{3}}$
~Stress-couture

## Video Solution
https://youtu.be/-l1Kawq_hds
~savannahsolver
### See Also
Video Solution:
https://www.youtube.com/watch?v=2kvSRL8KMac
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .