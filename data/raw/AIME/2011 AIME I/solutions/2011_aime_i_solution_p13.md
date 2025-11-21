# 2011 AIME I Problem 13

## Problem

A cube with side length 10 is suspended above a plane. The vertex closest to the plane is labeled $A$ . The three vertices adjacent to vertex $A$ are at heights 10, 11, and 12 above the plane. The distance from vertex $A$ to the plane can be expressed as $\frac{r-\sqrt{s}}{t}$ , where $r$ , $s$ , and $t$ are positive integers. Find $r+s+t$ .

## Solution 1
Set the cube at the origin with the three vertices along the axes and the plane equal to $ax+by+cz+d=0$ , where $a^2+b^2+c^2=1$ . The distance from a point $(X,Y,Z)$ to a plane with equation $Ax+By+Cz+D=0$ is \[\frac{AX+BY+CZ+D}{\sqrt{A^2+B^2+C^2}},\] so the (directed) distance from any point $(x,y,z)$ to the plane is $ax+by+cz+d$ . So, by looking at the three vertices, we have $10a+d=10, 10b+d=11, 10c+d=12$ , and by rearranging and summing, \[(10-d)^2+(11-d)^2+(12-d)^2= 100\cdot(a^2+b^2+c^2)=100.\]
Solving the equation is easier if we substitute $11-d=y$ , to get $3y^2+2=100$ , or $y=\sqrt {98/3}$ . The distance from the origin to the plane is simply $d$ , which is equal to $11-\sqrt{98/3} =(33-\sqrt{294})/3$ , so $33+294+3=\boxed{330}$ .

## Solution 2
Let the vertices with distance $10,11,12$ be $B,C,D$ , respectively. An equilateral triangle $\triangle BCD$ is formed with side length $10\sqrt{2}$ . We care only about the $z$ coordinate: $B=10,C=11,D=12$ . It is well known that the centroid of a triangle is the average of the coordinates of its three vertices, so $\text{centroid}=(10+11+12)/3=11$ . Designate the midpoint of $BD$ as $M$ . Notice that median $CM$ is parallel to the plane because the $\text{centroid}$ and vertex $C$ have the same $z$ coordinate, $11$ , and the median contains $C$ and the $\text{centroid}$ . We seek the angle $\theta$ of the line: $(1)$ through the centroid $(2)$ perpendicular to the plane formed by $\triangle BCD$ , $(3)$ with the plane under the cube. Since the median is parallel to the plane, this orthogonal line is also perpendicular $\textit{in slope}$ to $BD$ . Since $BD$ makes a $2-14-10\sqrt{2}$ right triangle, the orthogonal line makes the same right triangle rotated $90^\circ$ . Therefore, $\sin\theta=\frac{14}{10\sqrt{2}}=\frac{7\sqrt{2}}{10}$ .
It is also known that the centroid of $\triangle BCD$ is a third of the way between vertex $A$ and $H$ , the vertex farthest from the plane. Since $AH$ is a diagonal of the cube, $AH=10\sqrt{3}$ . So the distance from the $\text{centroid}$ to $A$ is $10/\sqrt{3}$ . So, the $\Delta z$ from $A$ to the centroid is $\frac{10}{\sqrt{3}}\sin\theta=\frac{10}{\sqrt{3}}\left(\frac{7\sqrt{2}}{10}\right)=\frac{7\sqrt{6}}{3}$ .
Thus the distance from $A$ to the plane is $11-\frac{7\sqrt{6}}{3}=\frac{33-7\sqrt{6}}{3}=\frac{33-\sqrt{294}}{3}$ , and $33+294+3=\boxed{330}$ .

## Solution 3

## Video Solution
2011 AIME I #13
MathProblemSolvingSkills.com

## Video Solution
https://youtube.com/watch?v=Wi-aqv8Ron0
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .