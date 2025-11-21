# 2014 AIME I Problem 1

## Problem

The 8 eyelets for the lace of a sneaker all lie on a rectangle, four equally spaced on each of the longer sides. The rectangle has a width of 50 mm and a length of 80 mm. There is one eyelet at each vertex of the rectangle. The lace itself must pass between the vertex eyelets along a width side of the rectangle and then crisscross between successive eyelets until it reaches the two eyelets at the other width side of the rectangle as shown. After passing through these final eyelets, each of the ends of the lace must extend at least 200 mm farther to allow a knot to be tied. Find the minimum length of the lace in millimeters.

[asy] size(200); defaultpen(linewidth(0.7)); path laceL=(-20,-30)..tension 0.75 ..(-90,-135)..(-102,-147)..(-152,-150)..tension 2 ..(-155,-140)..(-135,-40)..(-50,-4)..tension 0.8 ..origin; path laceR=reflect((75,0),(75,-240))*laceL; draw(origin--(0,-240)--(150,-240)--(150,0)--cycle,gray); for(int i=0;i<=3;i=i+1) { path circ1=circle((0,-80*i),5),circ2=circle((150,-80*i),5); unfill(circ1); draw(circ1); unfill(circ2); draw(circ2); } draw(laceL--(150,-80)--(0,-160)--(150,-240)--(0,-240)--(150,-160)--(0,-80)--(150,0)^^laceR,linewidth(1));[/asy]

## Solution
The rectangle is divided into three smaller rectangles with a width of 50 mm and a length of $\dfrac{80}{3}$ mm. According to the Pythagorean Theorem (or by noticing the 8-15-17 Pythagorean triple), the diagonal of the rectangle is $\sqrt{50^2+\left(\frac{80}{3}\right)^2}=\frac{170}{3}$ mm. Since that on the lace, there are 6 of these diagonals, a width, and an extension of at least 200 mm on each side. Therefore, the minimum of the lace in millimeters is \[6\times \dfrac{170}{3}+50+200\times 2=\boxed{790}.\]
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .