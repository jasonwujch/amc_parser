# 2021 Fall AMC 10A Problem 19

## Problem

A disk of radius $1$ rolls all the way around the inside of a square of side length $s>4$ and sweeps out a region of area $A$ . A second disk of radius $1$ rolls all the way around the outside of the same square and sweeps out a region of area $2A$ . The value of $s$ can be written as $a+\frac{b\pi}{c}$ , where $a,b$ , and $c$ are positive integers and $b$ and $c$ are relatively prime. What is $a+b+c$ ?

$\textbf{(A)} ~10\qquad\textbf{(B)} ~11\qquad\textbf{(C)} ~12\qquad\textbf{(D)} ~13\qquad\textbf{(E)} ~14$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(200); real s = 5 + pi/4; path p1, p2; p1 = Arc((1,1),(0,1),(1,0))--(s-1,0)--Arc((s-1,1),(s-1,0),(s,1))--(s,s-1)--Arc((s-1,s-1),(s,s-1),(s-1,s))--(1,s)--Arc((1,s-1),(1,s),(0,s-1))--cycle; p2 = Arc((0,0),(-2,0),(0,-2))--(s,-2)--Arc((s,0),(s,-2),(s+2,0))--(s+2,s)--Arc((s,s),(s+2,s),(s,s+2))--(0,s+2)--Arc((0,s),(0,s+2),(-2,s))--cycle; fill(p2,green); fill((0,0)--(s,0)--(s,s)--(0,s)--cycle,white); fill(p1,red); fill((2,2)--(s-2,2)--(s-2,s-2)--(2,s-2)--cycle,white); draw(Circle((2.5,s-1),1)^^Circle((-1,2.5),1),dashed); draw((0,0)--(s,0)--(s,s)--(0,s)--cycle,linewidth(1.5)); Label L1 = Label("$s$", align=(0,0), position=MidPoint, filltype=Fill(3,0,green)); draw((0,-0.75)--(s,-0.75), L=L1, arrow=Arrows(),bar=Bars(15)); [/asy]

~MRENTHUSIASM

## Solution 1
The side length of the inner square traced out by the disk with radius $1$ is $s-4.$ However, there is a piece at each corner (bounded by two line segments and one $90^\circ$ arc) where the disk never sweeps out. The combined area of these four pieces is $(1+1)^2-\pi\cdot1^2=4-\pi.$ As a result, we have \[A=s^2-(s-4)^2-(4-\pi)=8s-20+\pi.\] Now, we consider the second disk. The part it sweeps is comprised of four quarter circles with radius $2$ and four rectangles with side lengths of $2$ and $s.$ When we add it all together, we have $2A=8s+4\pi,$ or \[A=4s+2\pi.\] We equate the expressions for $A,$ and then solve for $s:$ \[8s-20+\pi=4s+2\pi.\] We get $s=5+\frac{\pi}{4},$ so the answer is $5+1+4=\boxed{\textbf{(A)} ~10}.$
~MathFun1000 (Inspired by Way Tan)

## Solution 2 (Fakesolve here, fakesolve there...)
(P) Assume that the area of the outside region \( 2A \) is just \( 4s \times \pi \). Then, the inner region \( A \) is just \( 2s \times \pi \). We can also fakesolve that the regions not hit by the sphere each make up a sphere with radius 1/2, and the area of that region itself is just \( \frac{1}{4} \pi \).
(I) Then, as Pinotation said, the area of the square is \( s^2 = 2s \times \pi + \frac{1}{4} \pi \). We then make the assumption that we can multiply \( s \) by \( 2\pi + \frac{1}{4} \pi - \frac{9}{4} \pi \), giving us \( s^2 = s\left(\frac{9}{4} \pi\right) \).
(P) Then, as IllusionalIntegral said, we subtract by \( s\left(\frac{9}{4} \pi\right) \) on both sides to get \( s^2 - s\left(\frac{9}{4} \pi\right) = 0 \), and factoring our \( s \), gives \( s\left(s-\frac{9}{4} \pi\right) \). \( s > 4 \), so \( s \neq 0 \), and \( s = \frac{9}{4} \pi \).
(P & I) Finally, \( s = \frac{9}{4} \pi \) can be written as \( \frac{9 \times \pi}{4} \), which we assume for the final time is \( \frac{4}{4} + \frac{5\pi}{4} \), giving us \( 1 + \frac{5\pi}{4} \), and \( 1 + 5 + 4 = \) $\boxed{\textbf{(A)} ~10}.$
$\textbf{Fakesolve Everywhere!}$
~Fakesolve by Pinotation and IllusionalIntegral
Note from IllusionalIntegral: Assumptions can be proved.
~Posted by Pinotation

## Video Solution (Under 4 min!)
https://youtu.be/AvgCmcEl5RE (This solution is pretty straightforward. Just basic geometry.)
~Education, the Study of Everything

## Video Solution by TheBeautyofMath
https://youtu.be/w4w99JBGnYM
~IceMatrix

## Animated Video Solutions
https://youtu.be/G57mijA4424 (vertical YouTube #Shorts for phone)
https://youtu.be/d5-AluTfxuU (landscape version for desktop)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .