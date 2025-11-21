# 2001 AIME I Problem 13

## Problem

In a certain circle , the chord of a $d$ -degree arc is $22$ centimeters long, and the chord of a $2d$ -degree arc is $20$ centimeters longer than the chord of a $3d$ -degree arc, where $d < 120.$ The length of the chord of a $3d$ -degree arc is $- m + \sqrt {n}$ centimeters, where $m$ and $n$ are positive integers. Find $m + n.$

## Solution

## Solution 1
Note that a cyclic quadrilateral in the form of an isosceles trapezoid can be formed from three chords of three $d$ -degree arcs and one chord of one $3d$ -degree arc. The diagonals of this trapezoid turn out to be two chords of two $2d$ -degree arcs. Let $AB$ , $AC$ , and $BD$ be the chords of the $d$ -degree arcs, and let $CD$ be the chord of the $3d$ -degree arc. Also let $x$ be equal to the chord length of the $3d$ -degree arc. Hence, the length of the chords, $AD$ and $BC$ , of the $2d$ -degree arcs can be represented as $x + 20$ , as given in the problem.
Using Ptolemy's theorem ,
\[AB \cdot CD + AC \cdot BD = AD \cdot BC\] \[\iff 22x + 22 \cdot 22 = (x + 20)^2\] \[\iff 22x + 484 = x^2 + 40x + 400\] \[\iff x^2 + 18x - 84 = 0.\]
We can then apply the quadratic formula to find the positive root of this equation (since polygons obviously cannot have sides of negative length): \[x = \frac{-18 + \sqrt{18^2 + 4 \cdot 84}}{2} = \frac{-18 + \sqrt{660}}{2}.\]
This simplifies to $x = \frac{-18 + 2\sqrt{165}}{2} = -9 + \sqrt{165}$ . Thus the answer is $9 + 165 = \boxed{174}$ .

## Solution 2
Let $z=\frac{d}{2},$ and $R$ be the circumradius. From the given information, \[2R\sin z=22, \quad\text{and}\] \[2R(\sin 2z-\sin 3z)=20.\] Dividing the latter equation by the former gives \[\frac{2\sin z\cos z-\left(3\cos^2z\sin z-\sin^3 z\right)}{\sin z}=2\cos z-\left(3\cos^2z-\sin^2z\right)=1+2\cos z-4\cos^2z=\frac{10}{11}\] \[\iff 4\cos^2z-2\cos z-\frac{1}{11}=0. \qquad (*)\] We want to find \[\frac{22\sin (3z)}{\sin z}=22(3-4\sin^2z)=22(4\cos^2z-1).\] From $(*),$ this is equivalent to $44\cos z-20$ . Using the quadratic formula, we deduce that this expression equals $-9+\sqrt{165}$ , so our answer is $\boxed{174}$ .

## Solution 3
Let $z=\frac{d}{2}$ , $R$ be the circumradius, and $a$ be the length of a $3d$ -degree chord. Using the extended sine law, we obtain: \[22=2R\sin(z),\] \[20+a=2R\sin(2z), \quad\text{and}\] \[a=2R\sin(3z).\] Dividing the second equation by the first, and using the double angle formula, we obtain $\cos(z)=\frac{20+a}{44}$ . Now, using the triple angle formula, we can rewrite the third equation as follows: \[a=2R \sin(3z)=\frac{22}{\sin(z)}\left(3\sin(z)-4\sin^3(z)\right) = 22\left(3-4\sin^2(z)\right) = 22\left(4\cos^2(z)-1\right) = \frac{(20+a)^2}{22}-22,\] and solving this quadratic equation gives the answer as $\boxed{174}$ .
These problems are copyrighted © by the Mathematical Association of America.