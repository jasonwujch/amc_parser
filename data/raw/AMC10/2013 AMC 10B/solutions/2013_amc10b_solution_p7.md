# 2013 AMC 10B Problem 7

## Problem

Six points are equally spaced around a circle of radius 1. Three of these points are the vertices of a triangle that is neither equilateral nor isosceles. What is the area of this triangle?

$\textbf{(A)}\ \frac{\sqrt{3}}{3}\qquad\textbf{(B)}\ \frac{\sqrt{3}}{2}\qquad\textbf{(C)}\ \textbf{1}\qquad\textbf{(D)}\ \sqrt{2}\qquad\textbf{(E)}\ \text{2}$

## Solution

## Solution 1
[asy] unitsize(72); draw((0,0)--(1/2,sqrt(3)/2)); draw((1/2,sqrt(3)/2)--(3/2,sqrt(3)/2)); draw((3/2,sqrt(3)/2)--(2,0)); draw((2,0)--(3/2,-sqrt(3)/2)); draw((3/2,-sqrt(3)/2)--(1/2,-sqrt(3)/2)); draw((1/2,-sqrt(3)/2)--(0,0)); draw((3/2,sqrt(3)/2)--(1/2,-sqrt(3)/2)); draw((3/2,sqrt(3)/2)--(3/2,-sqrt(3)/2)); label("2",(3/2,sqrt(3)/2)--(1/2,-sqrt(3)/2),NW); label("$\sqrt{3}$",(3/2,sqrt(3)/2)--(3/2,-sqrt(3)/2),E); label("1",(3/2,-sqrt(3)/2)--(1/2,-sqrt(3)/2),S); import olympiad; markscalefactor=0.01; draw(rightanglemark((3/2,sqrt(3)/2),(3/2,-sqrt(3)/2),(1/2,-sqrt(3)/2))); [/asy]
If there are no two points on the circle that are adjacent, then the triangle would be equilateral. If the three points are all adjacent, it would be isosceles. Thus, the only possibility is two adjacent points and one point two away. Because one of the sides of this triangle is the diameter, the opposite angle is a right angle. Also, because the two adjacent angles are one sixth of the circle apart, the angle opposite them is thirty degrees. This is a $30-60-90$ triangle. If the original six points are connected, a regular hexagon is created. This hexagon consists of six equilateral triangles, so the radius is equal to one of its side lengths. The radius is $1$ , so the side opposite the thirty degree angle in the triangle is also $1$ . From the properties of $30-60-90$ triangles, the area is $\frac{1 \cdot \sqrt{3}}{2}=\boxed{\textbf{(B) } \frac{\sqrt3}{2}}$

## Solution 2
As every point on the circle is evenly spaced, the length of each arc is $\frac{\pi}{3}$ , because the circumference is $2\pi$ . Once we draw the triangle (as is explained in solution 1), we see that one angle in the triangle subtends one such arc. Thus, the measure of that angle is thirty degrees. Similarly, another angle in the triangle subtends an arc of twice the length, and thus equals 60 degrees. The last angle is equal to 90 degrees and the triangle is a $30-60-90$ triangle. We know that as the diameter, the length of the hypotenuse is 2, and thus, the other sides are 1 and $\sqrt{3}$ . We then find the area to be $\boxed{\textbf{(B) } \frac{\sqrt{3}}{2} }$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .