# 2007 AMC 10A Problem 19

## Problem

A paint brush is swept along both diagonals of a square to produce the symmetric painted area, as shown. Half the area of the square is painted. What is the ratio of the side length of the square to the brush width?

[asy] unitsize(3 cm); real w = (sqrt(2) - 1)/2; filldraw((0,0)--(w*sqrt(2)/2,0)--(0.5,0.5 - w*sqrt(2)/2)--(1 - w*sqrt(2)/2,0)--(1,0)--(1,w*sqrt(2)/2)--(0.5 + w*sqrt(2)/2,0.5)--(1,1 - w*sqrt(2)/2)--(1,1)--(1 - w*sqrt(2)/2,1)--(0.5,0.5 + w*sqrt(2)/2)--(w*sqrt(2)/2,1)--(0,1)--(0,1 - w*sqrt(2)/2)--(0.5 - w*sqrt(2)/2,0.5)--(0,w*sqrt(2)/2)--cycle,gray(0.7)); draw((0,0)--(1,0)--(1,1)--(0,1)--cycle); [/asy]

$\text{(A)}\ 2\sqrt {2} + 1 \qquad \text{(B)}\ 3\sqrt {2}\qquad \text{(C)}\ 2\sqrt {2} + 2 \qquad \text{(D)}\ 3\sqrt {2} + 1 \qquad \text{(E)}\ 3\sqrt {2} + 2$

## Solution 1
Without loss of generality , let the side length of the square be $1$ unit. The area of the painted area is $\frac{1}2$ of the area of the larger square, so the total unpainted area is also $\frac{1}{2}$ . Each of the $4$ unpainted triangles has area $\frac{1}8$ . It can be observed that these triangles are isosceles right triangles, so let $a$ be the side length of one of the smaller triangles:
$\frac{a^2}2 = \frac{1}8 \rightarrow a= \frac{1}2$
The hypotenuse of the triangle is $\frac{\sqrt{2}}2$ . The corners of the painted area are also isosceles right triangles with side length $\frac{1-\frac{\sqrt{2}}2}2 = \frac{1}2-\frac{\sqrt2}4$ . Its hypotenuse is equal to the width of the paint, and is $\frac{\sqrt{2}}2-\frac{1}2$ . The answer we are looking for is thus $\frac{1}{\frac{\sqrt{2}}2-\frac{1}2}$ . Multiply the numerator and the denominator by $\frac{\sqrt{2}}2+\frac{1}2$ to simplify, and you get $\frac{\frac{\sqrt{2}}{2}+\frac{1}{2}}{\frac{2}{4}-\frac{1}{4}}$ or $4\left(\frac{\sqrt{2}}{2}+\frac{1}{2}\right)$ which is $\boxed{2\sqrt{2}+2} \rightarrow C$ .

## Solution 2
Again, have the length of the square equal to $1$ and let the width of each individual stripe be $n$ . Note that you can split each stripe into one rectangle and two isosceles right triangles at the corners. Then the area of each stripe is $n(\sqrt{2}-\frac{n}{2})=\sqrt{2}n-\frac{n^2}{2}$ . The area covered by the two total stripes is twice the area of one stripe, minus the area in the intersection of the stripes, which is a square with side length $n$ . This area is equal to $\frac{1}{2}$ . So:
$2\sqrt2n-2n^2=\frac{1}{2}\rightarrow-2n^2+2\sqrt2n-\frac{1}{2}=0$ .
By the quadratic formula ,
$n=\frac{-2\sqrt{2}\pm\sqrt{(2\sqrt{2})^2-4(-2)(-\frac{1}{2})}}{2(-2)}\rightarrow n=\frac{-2\sqrt{2}\pm 2}{-4}\rightarrow n=\frac{\sqrt{2}\pm 1}{2}$
$\frac{\sqrt{2}+1}{2}$ is greater than the length of the square, so it is impossible for that to be the brush width. Thus $n=\frac{\sqrt{2}-1}{2}$ . We want to find $\frac{1}{n}$ , and $\frac{1}{n}=\frac{2}{\sqrt{2}-1}$ . Multiply the numerator and the denominator by $\sqrt{2}+1$ ,
$\frac{1}{n}=\frac{2(\sqrt{2}+1)}{(\sqrt{2}-1)(\sqrt{2}+1)}=\boxed{2\sqrt{2}+2}\rightarrow C$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .