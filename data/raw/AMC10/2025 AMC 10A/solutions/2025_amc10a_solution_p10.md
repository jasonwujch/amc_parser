# 2025 AMC 10A Problem 10

## Problem

A semicircle has diameter $\overline{AB}$ and chord $\overline{CD}$ of length $16$ parallel to $\overline{AB}$ . A smaller semicircle with diameter on $\overline{AB}$ and tangent to $\overline{CD}$ is cut from the larger semicircle, as shown below.

[asy] import graph; unitsize(14mm); defaultpen(linewidth(.8pt)+fontsize(10pt)); dotfactor=4; pair A = (-3,0); pair B = (3,0); fill(Arc((0,0),3,0,180)--cycle,palered); fill(Arc((-1.125,0),0.75,0,180)--cycle,white); draw(Arc((0,0),3,0,180),black); draw(Arc((-1.125,0),0.75,0,180),black); draw((-3,0) -- (-1.875,0),black); draw((-0.375,0) -- (3,0),black); draw((-2.895, 0.75) -- (2.895,0.75), black); dot((-3,0)); dot((3,0)); dot((-2.925, 0.75)); dot((2.925, 0.75)); label("$16$",midpoint((-2.925, 0.75)--(2.925, 0.75)),N); label("$A$",A,S); label("$B$",B,S); label("$C$",(-2.925, 0.75),W); label("$D$",(2.925, 0.75),E); [/asy]

What is the area of the resulting figure, shown shaded?

$\textbf{(A) } 16\pi \qquad\textbf{(B) } 24\pi \qquad\textbf{(C) } 32\pi \qquad\textbf{(D) } 48\pi \qquad\textbf{(E) } 64\pi$

## Video Solution
https://youtu.be/l1RY_C20Q2M
### Note
This question is similar to 2004 AMC 12B 10/AMC 10B 12 .
Lets call the radius of the big semi-circle $R$ and the radius of the small semi-circle $r$ . The $c$ in the 2004 AMC 12B 10/AMC 10B 12, corresponds to $r$ and the $b$ corresponds to $R$ . If we cut the chord by half, we get $8$ as a result, and the $8$ corresponds to $a$ . The only difference is this problem contains two semi-circles while the 2004 AMC 12B 10/AMC 10B 12 contains two circles. From that problem, we know that the area of the annulus is $\pi a^2$ , which means the area in this problem should be $\frac{\pi(8)^2}{2}$ which is $\boxed{\mathrm{(C)\ }32\pi}$ . Basically, the 2004 AMC 12B 10/AMC 10B 12 was just a generalized problem while this one was a more specific one
~Neo

## Rigorous Solution
This solution is a general solution if MAA stated the diagram is not to be altered in any way (i.e. the chord is not the diameter, the chord can't be moved, the semicircle can't be moved, shrunk, etc.)
Solution 2 is the only other solution (at the moment) that satisfies those prerequisites.
Call the center of the big semicircle \( \omega \). Also, call the radius of the big semicircle \( R \) and the smaller semicircle \( r \). We then see that the distance from \( \omega \) to the chord is simply \( r \). We also see that if we draw a line from the intersection of the bigger semicircle and the chord to \( \omega \), that is just \( R \). Finally, it is a given fact that drawing a line from \( \omega \) to the top of the semicircle perpendicularly bisects the chord into two lengths of 8. Thus, our first equation is \( r^2 + 64 = R^2 \).
For our second equation, we take our line we drew from \( \omega \) to the top of the semicircle, calling it \( l \). The distance from the intersection of the chord and \( l \), call it \( E \), to the top of the semicircle is \( R-r \). We take the midpoint of this line, call it \( M \), splitting The distance of \( E \) to the top of the semicircle into two equal parts of length \( \frac{R-r}{2} \). Quadrilateral \( C\omega DM \) is a rhombus* (Check below for proof). With that in mind it isnt hard to prove that triangles \( \omega EC \) and \( MEC \) are congruent through ASA, and then we see that \( \frac{R-r}{2} = r \), and \( R = 3r \).
Through substitution, we see \( r^2+64=R^2 \implies r^2 + 64 = 9r^2 \implies 64 = 8r^2 \implies 8 = r^2 \implies r = \sqrt{8} \), therefore the radius of the smaller semicircle is \( \sqrt{8} \).
We have \( R=3r \), and so the radius of the bigger semicircle is \( 3\sqrt{8} \).
We want the area of the bigger semicircle minus the area of the smaller semicircle, which is \( \frac{1}{2} \cdot (3\sqrt{8})^2 \pi - \frac{1}{2} \cdot (\sqrt{8})^2 \pi = 36 \pi - 4\pi = 32 \pi \)
Thus the answer is $\boxed{\text{(C) }32\pi}$
The other solutions are quite interesting. Go check em' out.
~Pinotation
### Proof that the quadrilateral is a rhombus
Reflect triangle \( C\omega D \) over line \( CD \). The figure formed is bound to be a rhombus (call the newly reflected point \( \omega \) to be \( \omega' \). We now just need to prove that \( \omega' \) lies on \( M \). We do so using angles.
Call the intersection other than \( \omega \) of line \( l \) and the bigger semicircle \( X \). It becomes quite easy to see quadrilateral \( C\omega DX \) is cyclic, with \( \angle X + \angle \omega = 180^\circ \). We can also see that \( \angle X \) is inscribed in \( \angle \omega' \), and say \( \omega = 2y^\circ \). Then because \( \angle \omega \cong \angle \omega' \), we see that \( \angle \omega' \) is \( 2y^\circ \), and therefore, through the inscribed angles theorem, \( \angle X = y^\circ \).
We don't really care about the degree measure of \( y \), but we only care about the fact that \( \angle \omega' \) is double that of \( \angle X \). Constructing a circle with diameter \( EX \), or \( R-r \), we see that point \( \omega' \) and point \( X \) are collinear, and because the angle \( X \) is inscribed within the angle \( \omega' \) in the ratio 1:2, \( \omega' \) is the center of this circle, or, in other terms, the midpoint of the line \( EX \).
We have claimed for \( M \) to be the midpoint of line \( EX \) though, so therefore point \( \omega' \) lies on point \( M \), and we continue as followed in the solution. \(\square\)
Note inside of Note: The cyclic quadrilateral isn't necessary for this proof. Just put it there if you want the angle measure of the rhombus.
~Pinotation

## Solution 1 (Somewhat Cheeky)
Notice that the size of the smaller semicircle is not specified, and there is no additional information that hints at any specific size for it. Hence, we can shrink the small semicircle until its area is arbitrarily small and negligible, leaving us with a semicircle with a diameter of $16$ . The area of the semicircle is given by $\frac{\pi r^2}{2}$ , so we have $r=\frac{16}{2}=8\Rightarrow$ $A=\frac{\pi(8)^2}{2}=\boxed{\text{(C) }32\pi}$
~Bocabulary142857

## Solution 2 (Generalized, no assumptions)
Let the radius of the larger semicircle be $R$ and that of the smaller one be $r.$ We are looking for $\dfrac{1}{2}\pi(R^2-r^2).$ If we connect the center of the large semicircle to one endpoint of the chord and to the center of the chord, we get a right triangle with legs $8$ and $r$ and hypotenuse $R.$ Hence, $R^2=r^2+8^2\implies R^2-r^2=64\implies\dfrac{1}{2}\pi(R^2-r^2)=\boxed{\text{(C) }32\pi}.!$
~Nioronean, $\LaTeX$ and writing by Tacos_are_yummy_1

## Solution 3
The problem doesn't restrict where the smaller semicircle is along the larger semicircle's diameter. Therefore, we can assume that the two semicircles are concentric. Let the center of both semicircles be $O$ , and let $CD$ be tangent to the smaller semicircle at $T$ . Let the radius of the smaller semicircle be $x$ , and let the radius of the larger semicircle be $r$ . If we mirror the diagram over $AB$ , we can see that we have two concentric circles. We are trying to find $\pi(\frac{r^2-x^2}{2})$ . By Power of a Point on $T$ , we can see that \[64 = (r + x)(r - x) = r^2 - x^2.\] Thus, $\pi(\frac{r^2 - x^2}{2}) = 32\pi \implies \boxed{\text{(C) }32\pi}.$ ~vinceS

## Solution 4
The problem doesn't define where the chord is within the circle. So, let's place the chord such that when lines are drawn from its ends to the center of the larger semicircle, an equilateral triangle with side length $16$ is formed.
[asy] import graph; unitsize(14mm); defaultpen(linewidth(.8pt)+fontsize(10pt)); dotfactor=4; fill(Arc((0,0),3,0,180)--cycle,palered); fill(Arc((0,0),2.598,0,180)--cycle,white); draw(Arc((0,0),3,0,180),black); draw(Arc((0,0),2.598,0,180),black); draw((-2.598,0) -- (2.598,0), white); draw((-1.5,2.598) -- (1.5,2.598),black); draw((0,0) -- (-1.5, 2.598), black); draw((0,0) -- (1.5, 2.598), black); draw((0,0) -- (0, 2.598), black); draw((-3,0) -- (-2.598, 0), black); draw((3,0) -- (2.598, 0), black); dot((0,0)); dot((0,2.598)); dot((-1.5,2.598)); dot((1.5,2.598)); dot((3,0)); dot((-3,0)); label("$16$",midpoint((0, 2.598)--(0, 2.598)),N); label("$8\sqrt{3}$",midpoint((0, 1.4)--(0, 1.4)),E); label("$16$",midpoint((-0.9, 1.3)--(-0.9, 1.3)),W); label("$16$",midpoint((0.9, 1.3)--(0.9, 1.3)),E); label("$A$",midpoint((-3, 0)--(-3, 0)),W); label("$B$",midpoint((3, 0)--(3, 0)),E); label("$C$",midpoint((-1.5,2.7)--(-1.5,2.7)),N); label("$D$",midpoint((1.5,2.7)--(1.5,2.7)),N); [/asy]
In this definition, the radius of the larger semicircle is $16,$ giving it an area of $\frac{\pi\cdot16^2}{2} = 128\pi.$
The height of the equilateral triangle is $8\sqrt{3},$ which is equal to the radius of the smaller semicircle. This gives the smaller semicircle an area of $\frac{\pi\cdot(8\sqrt{3})^2}{2} = 96\pi.$
The total shaded area is the difference of these semicircles, or $128\pi - 96\pi = \boxed{\text{(C) } 32\pi}.$
~chisps

## Solution 5
Let the radius of the larger semicircle be $R$ and the smaller one $r.$ We are asked to compute $\frac{R^2-r^2}{2} \cdot \pi$ . Since a diameter is always perpendicular and bisects a chord, by drawing a diameter and applying Power of a Point Theorem, this yields $(R+r)(R-r)=8^2$ $\implies$ $R^2-r^2=64$ . Therefore, the answer is $\frac{64}{2} \pi = \boxed{\text{(C) } 32\pi}.$ ~hxve

## Solution 6
Since the problem does not restrict where the chord is, WLOG we can simply let the chord be the base of the semicircle. Therefore, the area is simply $\frac{\pi\cdot8^2}{2} = 32\pi.$
~metrixgo

## Solution 7
We can move this small semicircle to the middle of the big semicircle. Let $r$ be the radius of the small semicircle. By Pythagorean Theorem, the line draw from the midpoint of the diameter of the big semicircle to the big semicircle at the height of the small semicircle (see the diagram) has length $\sqrt{r^2 + 64}$ . This is a radius of the big semicircle. So the shaded area would be \[\frac{\pi \cdot (\sqrt{r^2+64})^2 - \pi r^2}{2} = \frac{\pi(r^2 + 64 - r^2)}{2} = \frac{64\pi}{2} = \boxed{\text{(C) } 32\pi}.\] Diagram:
[asy] import graph; unitsize(14mm); defaultpen(linewidth(.8pt)+fontsize(10pt)); dotfactor=4; real R = 3; pair A = (-R,0), B = (R,0); fill(Arc((0,0),R,0,180)--cycle,palered); draw(Arc((0,0),R,0,180),black); real h = 0.75; pair C = (-sqrt(R^2 - h^2), h); pair D = ( sqrt(R^2 - h^2), h); draw(C--D,black); label("$C$",C,W); label("$D$",D,E); label("$16$", midpoint(C--D), N); real r = h; pair O = (0,0); pair Q = (0,r); fill(Arc(O,r,0,180)--cycle,white); draw(Arc(O,r,0,180),black); draw(A--B,black); draw(O--Q); draw(O--D); draw(Q--D, dashed); label("$A$",A,S); label("$B$",B,S); label("$r$", midpoint(O--Q), W); label("$\sqrt{r^{2}+64}$", midpoint(O--D), S); label("$8$", midpoint(Q--D), N); [/asy]
~JerryZYang

## Solution 8 (similar to some other stated solutions)
So basically, we see that the chord is very very similar in length to the diameter, so we solve for the area with 16 as the diameter. We find that the area is 64π, and because they want us to subtract the small semicircle and that 16 is actually less than the actual diameter, we can just use half of 64π as our answer. Thus, the answer is $\boxed{\mathrm{(C)\ }32\pi}$
~Sakura_kitty

## Chinese Video Solution
https://www.bilibili.com/video/BV1bj2uBxEkU/
~metrixgo

## Video Solution (In 1 Min)
https://youtu.be/8VWMNAx55g0?si=IqLseEtKLl2joUNU ~ Pi Academy

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution by Daily Dose of Math
https://youtu.be/gPh9w3X3QSw
~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .