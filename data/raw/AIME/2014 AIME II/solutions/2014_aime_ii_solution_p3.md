# 2014 AIME II Problem 3

## Problem

A rectangle has sides of length $a$ and 36. A hinge is installed at each vertex of the rectangle, and at the midpoint of each side of length 36. The sides of length $a$ can be pressed toward each other keeping those two sides parallel so the rectangle becomes a convex hexagon as shown. When the figure is a hexagon with the sides of length $a$ parallel and separated by a distance of 24, the hexagon has the same area as the original rectangle. Find $a^2$ .

[asy] pair A,B,C,D,E,F,R,S,T,X,Y,Z; dotfactor = 2; unitsize(.1cm); A = (0,0); B = (0,18); C = (0,36); // don't look here D = (12*2.236, 36); E = (12*2.236, 18); F = (12*2.236, 0); draw(A--B--C--D--E--F--cycle); dot(" ",A,NW); dot(" ",B,NW); dot(" ",C,NW); dot(" ",D,NW); dot(" ",E,NW); dot(" ",F,NW); //don't look here R = (12*2.236 +22,0); S = (12*2.236 + 22 - 13.4164,12); T = (12*2.236 + 22,24); X = (12*4.472+ 22,24); Y = (12*4.472+ 22 + 13.4164,12); Z = (12*4.472+ 22,0); draw(R--S--T--X--Y--Z--cycle); dot(" ",R,NW); dot(" ",S,NW); dot(" ",T,NW); dot(" ",X,NW); dot(" ",Y,NW); dot(" ",Z,NW); // sqrt180 = 13.4164 // sqrt5 = 2.236[/asy]

## Solution 1
When we squish the rectangle, the hexagon is composed of a rectangle and two isosceles triangles with side lengths 18, 18, and 24 as shown below.
[asy] pair R,S,T,X,Y,Z; dotfactor = 2; unitsize(.1cm); R = (12*2.236 +22,0); S = (12*2.236 + 22 - 13.4164,12); T = (12*2.236 + 22,24); X = (12*4.472+ 22,24); Y = (12*4.472+ 22 + 13.4164,12); Z = (12*4.472+ 22,0); draw(R--S--T--X--Y--Z--cycle); draw(T--R,red); draw(X--Z,red); dot(" ",R,NW); dot(" ",S,NW); dot(" ",T,NW); dot(" ",X,NW); dot(" ",Y,NW); dot(" ",Z,NW); // sqrt180 = 13.4164 // sqrt5 = 2.236[/asy]
By Heron's Formula, the area of each isosceles triangle is $\sqrt{(30)(12)(12)(6)}=\sqrt{180\times 12^2}=72\sqrt{5}$ . So the area of both is $144\sqrt{5}$ . From the rectangle, our original area is $36a$ . The area of the rectangle in the hexagon is $24a$ . So we have \[24a+144\sqrt{5}=36a\implies 12a=144\sqrt{5}\implies a=12\sqrt{5}\implies a^2=\boxed{720}.\]

## Solution 2
Alternatively, use basic geometry. First, scale everything down by dividing everything by 6. Let $a/6=p$ . Then, the dimensions of the central rectangle in the hexagon is p x 4, and the original rectangle is 6 x p. By Pythagorean theorem and splitting the end triangles of the hexagon into two right triangles, the altitude of the end triangles is $\sqrt{3^2-2^2}=\sqrt{5}$ given 2 as the base of the constituent right triangles. The two end triangles form a large rectangle of area $\sqrt{5}$ x $4$ . Then, the area of the hexagon is $4p+4\sqrt{5}$ , and the area of the rectangle is $6p$ . Equating them, $p=2\sqrt{5}$ . Multiply by scale factor of 6 and square it to get $36(20)= 720 \implies a^2=\boxed{720}$ .
~BJHHar
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .