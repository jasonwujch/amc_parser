# 2002 AMC 10A Problem 23

## Problem

Points $A,B,C$ and $D$ lie on a line, in that order, with $AB = CD$ and $BC = 12$ . Point $E$ is not on the line, and $BE = CE = 10$ . The perimeter of $\triangle AED$ is twice the perimeter of $\triangle BEC$ . Find $AB$ .

$\text{(A)}\ 15/2 \qquad \text{(B)}\ 8 \qquad \text{(C)}\ 17/2 \qquad \text{(D)}\ 9 \qquad \text{(E)}\ 19/2$

## Solution
First, we draw an altitude to $BC$ from $E$ . Let it intersect at $M$ . As $\triangle BEC$ is isosceles, we immediately get $MB=MC=6$ , so the altitude is $8$ . Now, let $AB=CD=x$ . Using the Pythagorean Theorem on $\triangle EMA$ , we find $AE=\sqrt{x^2+12x+100}$ . From symmetry, $DE=\sqrt{x^2+12x+100}$ as well. Now, we use the fact that the perimeter of $\triangle AED$ is twice the perimeter of $\triangle BEC$ .
[asy] unitsize(0.25 cm); pair A, B, C, D, E, M; A = (0,0); B = (9,0); C = (21,0); D = (30,0); E = (15,-8); M = (15,0); draw(A--D--E--cycle); draw(B--E); draw(M--E); draw(C--E); label("$A$", A, N); label("$B$", B, N); label("$C$", C, N); label("$D$", D, N); label("$E$", E, S); label("$M$", M, N); [/asy]
We have $2\sqrt{x^2+12x+100}+2x+12=2(32)$ so $\sqrt{x^2+12x+100}=26-x$ . Squaring both sides, we have $x^2+12x+100=676-52x+x^2$ which nicely rearranges into $64x=576\rightarrow{x=9}$ . Hence, AB is 9 so our answer is $\boxed{\text{(D)}}$ .

## Solution 2 (Simpler)
Let $M$ be the foot of the altitude from $E$ to $BC.$ Then $MB=MC=6$ because $\triangle BEC$ is isosceles. By the Pythagorean triple $(6,8,10)$ the altitude is $8.$ Since $(8,15,17)$ is the only primitive Pythagorean triple with leg $8,$ we test $AE=DE=17,AM=DM=15.$ Since $2(10+10+12)=(17+17+2\cdot 15)$ this works, giving us $AB=15-6=\boxed{\text{(D)}\ 9}.$
~dolphin7

## Video Solution
https://www.youtube.com/watch?v=HJkfO6vuIwg ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .