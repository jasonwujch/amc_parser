# 2000 AMC 8 Problem 19

## Problem

Three circular arcs of radius $5$ units bound the region shown. Arcs $AB$ and $AD$ are quarter-circles, and arc $BCD$ is a semicircle. What is the area, in square units, of the region?

[asy] pair A,B,C,D; A = (0,0); B = (-5,5); C = (0,10); D = (5,5); draw(arc((-5,0),A,B,CCW)); draw(arc((0,5),B,D,CW)); draw(arc((5,0),D,A,CCW)); label("$A$",A,S); label("$B$",B,W); label("$C$",C,N); label("$D$",D,E);[/asy]

$\text{(A)}\ 25\qquad\text{(B)}\ 10+5\pi\qquad\text{(C)}\ 50\qquad\text{(D)}\ 50+5\pi\qquad\text{(E)}\ 25\pi$

## Solutions

## Solution 1
Draw two squares: one that has opposing corners at $A$ and $B$ , and one that has opposing corners at $A$ and $D$ . These squares share side $\overline{AO}$ , where $O$ is the center of the large semicircle.
These two squares have a total area of $2 \cdot 5^2$ , but have two quarter circle "bites" of radius $5$ that must be removed. Thus, the bottom part of the figure has area
$2\cdot 25 - 2 \cdot \frac{1}{4}\pi \cdot 5^2$
$50 - \frac{25\pi}{2}$
This is the area of the part of the figure underneath $\overline{BD}$ . The part of the figure over $\overline{BD}$ is just a semicircle with radius $5$ , which has area of $\frac{1}{2}\pi\cdot 5^2 = \frac{25\pi}{2}$
Adding the two areas gives a total area of $\boxed{(c)50}$

## Solution 2
Draw line $\overline{BD}$ . Then draw $\overline {CO}$ , where $O$ is the center of the semicircle. You have two quarter circles on top, and two quarter circle-sized "bites" on the bottom. Move the pieces from the top to fit in the bottom like a jigsaw puzzle. You now have a rectangle with length $\overline {BD}$ and height $\overline {AO}$ , which are equal to $10$ and $5$ , respectively. Thus, the total area is $50$ , and the answer is $\boxed{C}$ .

## Video Solution
https://youtu.be/kLH0ql186UE Soo, DRMS, NM
https://www.youtube.com/watch?v=-Sysux6_wXo ~David
### See Also