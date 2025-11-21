# 2021 Fall AMC 10B Problem 21

## Problem

Regular polygons with $5,6,7,$ and $8$ sides are inscribed in the same circle. No two of the polygons share a vertex, and no three of their sides intersect at a common point. At how many points inside the circle do two of their sides intersect?

$(\textbf{A})\: 52\qquad(\textbf{B}) \: 56\qquad(\textbf{C}) \: 60\qquad(\textbf{D}) \: 64\qquad(\textbf{E}) \: 68$

## Solution
Imagine we have $2$ regular polygons with $m$ and $n$ sides and $m>n$ inscribed in a circle without sharing a vertex. We see that each side of the polygon with $n$ sides (the polygon with fewer sides) will be intersected twice. (We can see this because to have a vertex of the $m$ -gon on an arc subtended by a side of the $n$ -gon, there will be one intersection to “enter” the arc and one to “exit” the arc. ~KingRavi)
This means that we will end up with $2$ times the number of sides in the polygon with fewer sides.
If we have polygons with $5,$ $6,$ $7,$ and $8$ sides, we need to consider each possible pair of polygons and count their intersections.
Throughout $6$ of these pairs, the $5$ -sided polygon has the least number of sides $3$ times, the $6$ -sided polygon has the least number of sides $2$ times, and the $7$ -sided polygon has the least number of sides $1$ time.
Therefore the number of intersections is $2\cdot(3\cdot5+2\cdot6+1\cdot7)=\boxed{(\textbf{E}) \:68}$ .
~kingofpineapplz
### Remark
For regular polygons with $5,6,7,$ and $8$ sides, the $68$ points of intersection inside the circle are shown below: [asy] /* Made by MRENTHUSIASM */ size(350); path p5 = polygon(5); path p6 = polygon(6); path p7 = rotate(180)*polygon(7); path p8 = polygon(8); draw(p5,red); draw(p6,green); draw(p7,blue); draw(p8,olive); draw(Circle(origin,1)); dot(intersectionpoints(p5,p6),linewidth(2.5)); dot(intersectionpoints(p5,p7),linewidth(2.5)); dot(intersectionpoints(p5,p8),linewidth(2.5)); dot(intersectionpoints(p6,p7),linewidth(2.5)); dot(intersectionpoints(p6,p8),linewidth(2.5)); dot(intersectionpoints(p7,p8),linewidth(2.5)); [/asy] ~MRENTHUSIASM

## Video Solution by Interstigation
https://youtu.be/7cfZwwYSttQ
~Interstigation

## Video Solution 2 by WhyMath
https://youtu.be/5nHMBfDyvps
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/yTQSKinIo8g
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .