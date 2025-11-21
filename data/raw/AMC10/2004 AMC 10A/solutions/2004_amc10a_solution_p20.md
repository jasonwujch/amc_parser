# 2004 AMC 10A Problem 20

## Problem

Points $E$ and $F$ are located on square $ABCD$ so that $\triangle BEF$ is equilateral. What is the ratio of the area of $\triangle DEF$ to that of $\triangle ABE$ ?

[asy] unitsize(3 cm); pair A, B, C, D, E, F; A = (0,0); B = (1,0); C = (1,1); D = (0,1); E = (0,Tan(15)); F = (1 - Tan(15),1); draw(A--B--C--D--cycle); draw(B--E--F--cycle); label("$A$", A, SW); label("$B$", B, SE); label("$C$", C, NE); label("$D$", D, NW); label("$E$", E, W); label("$F$", F, N); [/asy]

$\mathrm{(A) \ } \frac{4}{3} \qquad \mathrm{(B) \ } \frac{3}{2} \qquad \mathrm{(C) \ } \sqrt{3} \qquad \mathrm{(D) \ } 2 \qquad \mathrm{(E) \ } 1+\sqrt{3}$

## Solution 1
Since triangle $BEF$ is equilateral, $EA=FC$ , and $EAB$ and $FCB$ are $HL$ congruent. Thus, triangle $DEF$ is an isosceles right triangle. So we let $DE=x$ . Thus $EF=EB=FB=x\sqrt{2}$ . If we go angle chasing, we find out that $\angle AEB=75^{\circ}$ , thus $\angle ABE=15^{\circ}$ . $\frac{AE}{EB}=\sin{15^{\circ}}=\frac{\sqrt{6}-\sqrt{2}}{4}$ . Thus $\frac{AE}{x\sqrt{2}}=\frac{\sqrt{6}-\sqrt{2}}{4}$ , or $AE=\frac{x(\sqrt{3}-1)}{2}$ . Thus $AB=\frac{x(\sqrt{3}+1)}{2}$ , and $[ABE]=\frac{x^2}{4}$ , and $[DEF]=\frac{x^2}{2}$ . Thus the ratio of the areas is $\boxed{\mathrm{(D)}\ 2}$
z

## Solution 2 (Non-trig)
WLOG, let the side length of $ABCD$ be 1. Let $DE = x$ . It suffices that $AE = 1 - x$ . Then triangles $ABE$ and $CBF$ are congruent by HL, so $CF = AE$ and $DE = DF$ . We find that $BE = EF = x \sqrt{2}$ , and so, by the Pythagorean Theorem, we have $(1 - x)^2 + 1 = 2x^2.$ This yields $x^2 + 2x = 2$ , so $x^2 = 2 - 2x$ . Thus, the desired ratio of areas is \[\dfrac{\dfrac{x^2}{2}}{\dfrac{1-x}{2}} = \dfrac{x^2}{1 - x} = \boxed{\text{(D) }2}.\]

## Solution 3 (System of Equations)
Assume $AB=1$ . Then, $FC$ is $x$ and $ED$ is $1-x$ . We see that using $HL$ , $FCB$ is congruent to EAB. Using Pythagoras of triangles $FCB$ and $FDE$ we get $2{(1-x)}^2=x^2+1$ . Expanding, we get $2x^2-4x+2=x^2+1$ . Simplifying gives $x^2-4x+1=0$ solving using completing the square (or other methods) gives 2 answers: $2-\sqrt{3}$ and $2+\sqrt{3}$ . Because $x < 1$ , $x=2-\sqrt{3}$ . Using the areas, the answer is $\boxed{\text{(D) }2}$

## Solution 4
First, since $\bigtriangleup BEF$ is equilateral and $ABCD$ is a square, by the Hypothenuse Leg Theorem, $\bigtriangleup ABE$ is congruent to $\bigtriangleup CBF$ . Then, assume length $AB = BC = x$ and length $DE = DF = y$ , then $AE = FC = x - y$ . $\bigtriangleup BEF$ is equilateral, so $EF = EB$ and $EB^2 = EF^2$ , it is given that $ABCD$ is a square and $\bigtriangleup DEF$ and $\bigtriangleup ABE$ are right triangles. Then we use the Pythagorean theorem to prove that $AB^2 + AE^2 = EB^2$ and since we know that $EB^2 = EF^2$ and $EF^2 = DE^2 + DF^2$ , which means $AB^2 + AE^2 = DE^2 + DF^2$ . Now we plug in the variables and the equation becomes $x^2 + (x-y)^2 = 2y^2$ , expand and simplify and you get $2x^2 - 2xy = y^2$ . We want the ratio of area of $\bigtriangleup DEF$ to $\bigtriangleup ABE$ . Expressed in our variables, the ratio of the area is $\frac{y^2}{x^2 - xy}$ and we know $2x^2 - 2xy = y^2$ , so the ratio must be $2$ . So, the answer is $\boxed{\text{(D) }2}$

## solution 5:
First, assume that $AB=1$ , and let $ED = DF = x$ . Then, we have $[DEF] = \frac{x^2}{2}$ and \[[ABE] = \frac{(AE)(AB)}{2} = \frac{(1-x)(1)}{2},\] so \[\frac{[DEF]}{[ABE]} = \frac{x^2}{1-x} .\] By the Pythagorean Theorem applied to $\triangle DEF$ , we have \[EF^2 = DE^2 + DF^2 = 2x^2.\] Applying the Pythagorean Theorem to $\triangle AEB$ , we have \[EB^2 = AB^2 + AE^2 = 1 + (1-x)^2 = 2 - 2x + x^2.\] Since $\triangle EFB$ is equilateral, we have $EF = EB$ , so \[2x^2 = 2-2x + x^2,\] or $x^2 = 2-2x= 2(1-x)$ . Hence the desired ratio of the areas is \[\frac{[DEF]}{[ABE]} = \frac{x^2}{1-x} = \boxed{2}.\]

## Video Solution
https://youtu.be/hwHIHRukYMk
Education, the Study of Everything

## Video Solution by TheBeautyofMath
https://youtu.be/BFKo9h8GhLY
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .