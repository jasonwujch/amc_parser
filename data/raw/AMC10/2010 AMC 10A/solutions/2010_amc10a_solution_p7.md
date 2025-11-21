# 2010 AMC 10A Problem 7

## Problem

Crystal has a running course marked out for her daily run. She starts this run by heading due north for one mile. She then runs northeast for one mile, then southeast for one mile. The last portion of her run takes her on a straight line back to where she started. How far, in miles is this last portion of her run?

$\mathrm{(A)}\ 1 \qquad \mathrm{(B)}\ \sqrt{2} \qquad \mathrm{(C)}\ \sqrt{3} \qquad \mathrm{(D)}\ 2 \qquad \mathrm{(E)}\ 2\sqrt{2}$

## Solution 1
Crystal first runs north for one mile. Changing directions, she runs northeast for another mile. The angle difference between north and northeast is 45 degrees. She then switches directions to southeast, meaning a 90 degree angle change. The distance now from traveling north for one mile, and her current destination is $\sqrt{2}$ miles, because it is the hypotenuse of a 45-45-90 triangle with side length one (mile). Therefore, Crystal's distance from her starting position, x, is equal to $\sqrt{((\sqrt{2})^2+1^2)}$ , which is equal to $\sqrt{3}$ . The answer is $\boxed{C}$
[asy] import olympiad; draw((0,0)--(0,1)); draw((0,1)--(0,1.7071067811865476), dotted); draw((0,1)--(0.7071067811865476, 1.7071067811865476)); draw((0.7071067811865476, 1.7071067811865476)--(1.4142135623730951,1)); draw(anglemark((0.7071067811865476, 1.7071067811865476),(0,1),(0,1.7071067811865476))); label("$45^{\circ}$", (0,1.25), NE); draw((0, 1)--(1.4142135623730951,1), dotted); draw((1.4142135623730951,1)--(0,0), green); [/asy]

## Solution 2
Crystal runs north one mile, then her next two moves can be broken up into four individual moves: for her northeast section, it forms a $45-45-90$ triangle whose legs are each $\frac{\sqrt{2}}{2}$ . For her southeast section, it is also a $45-45-90$ triangle whose legs are each $\frac{\sqrt{2}}{2}$ . Notice that the two of the legs cancel each other out; she moves north $\frac{\sqrt{2}}{2}$ units and also south $\frac{\sqrt{2}}{2}$ units. So her net movement these two moves is $\sqrt{2}$ to the right. Finally, after the third move, she is at the corner of a right triangle with legs $1$ and $\sqrt{2}$ . Using the Pythagorean theorem, $d^{2}=1^{2}+\left(\sqrt{2}\right)^{2}=1+2=3$ and $d=\sqrt{3} \Longrightarrow \boxed{\textbf{(C) } \sqrt{3}}$ .
~JH. L

## Video Solution
https://youtu.be/P7rGLXp_6es?t=132
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .