# 2013 AIME II Problem 8

## Problem

A hexagon that is inscribed in a circle has side lengths $22$ , $22$ , $20$ , $22$ , $22$ , and $20$ in that order. The radius of the circle can be written as $p+\sqrt{q}$ , where $p$ and $q$ are positive integers. Find $p+q$ .

## Solution
[asy] import olympiad; import math; real a; a=2*asin(11/(5+sqrt(267))); pair A,B,C,D,E,F; A=expi(pi); B=expi(pi-a); C=expi(a); D=expi(0); E=expi(-a); F=expi(pi+a); draw(A--B--C--D--E--F--A--D); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); draw(unitcircle); label("$A$",A,W);label("$B$",B,NW);label("$C$",C,NE);label("$D$",D,dir(0));label("$E$",E,SE);label("$F$",F,SW); [/asy]

## Solution 1
Let us call the hexagon $ABCDEF$ , where $AB=CD=DE=AF=22$ , and $BC=EF=20$ . We can just consider one half of the hexagon, $ABCD$ , to make matters simpler. Draw a line from the center of the circle, $O$ , to the midpoint of $BC$ , $X$ . Now, draw a line from $O$ to the midpoint of $AB$ , $Y$ . Clearly, $\angle BXO=90^{\circ}$ , because $BO=CO$ , and $\angle BYO=90^{\circ}$ , for similar reasons. Also notice that $\angle AOX=90^{\circ}$ . Let us call $\angle BOY=\theta$ . Therefore, $\angle AOB=2\theta$ , and so $\angle BOX=90-2\theta$ . Let us label the radius of the circle $r$ . This means \[\sin{\theta}=\frac{BY}{r}=\frac{11}{r}\] \[\sin{(90-2\theta)}=\frac{BX}{r}=\frac{10}{r}\] Now we can use simple trigonometry to solve for $r$ . Recall that $\sin{(90-\alpha)}=\cos(\alpha)$ : That means $\sin{(90-2\theta)}=\cos{2\theta}=\frac{10}{r}$ . Recall that $\cos{2\alpha}=1-2\sin^2{\alpha}$ : That means $\cos{2\theta}=1-2\sin^2{\theta}=\frac{10}{r}$ . Let $\sin{\theta}=x$ . Substitute to get $x=\frac{11}{r}$ and $1-2x^2=\frac{10}{r}$ Now substitute the first equation into the second equation: $1-2\left(\frac{11}{r}\right)^2=\frac{10}{r}$ Multiplying both sides by $r^2$ and reordering gives us the quadratic \[r^2-10r-242=0\] Using the quadratic equation to solve, we get that $r=5+\sqrt{267}$ (because $5-\sqrt{267}$ gives a negative value), so the answer is $5+267=\boxed{272}$ .

## Solution 2
Using the trapezoid $ABCD$ mentioned above, draw an altitude of the trapezoid passing through point $B$ onto $AD$ at point $J$ . Now, we can use the pythagorean theorem: $(22^2-(r-10)^2)+10^2=r^2$ . Expanding and combining like terms gives us the quadratic \[r^2-10r-242=0\] and solving for $r$ gives $r=5+\sqrt{267}$ . So the solution is $5+267=\boxed{272}$ .

## Solution 3
Join the diameter of the circle $AD$ and let the length be $d$ . By Ptolemy's Theorem on trapezoid $ADEF$ , $(AD)(EF) + (AF)(DE) = (AE)(DF)$ . Since it is an isosceles trapezoid, both diagonals are equal. Let them be equal to $x$ each. Then
\[20d + 22^2 = x^2\]
Since $\angle AED$ is subtended by the diameter, it is right. Hence by the Pythagorean Theorem with right $\triangle AED$ :
\[(AE)^2 + (ED)^2 = (AD)^2\] \[x^2 + 22^2 = d^2\]
From the above equations, we have: \[x^2 = d^2 - 22^2 = 20d + 22^2\] \[d^2 - 20d = 2\times22^2\] \[d^2 - 20d + 100 = 968+100 = 1068\] \[(d-10) = \sqrt{1068}\] \[d = \sqrt{1068} + 10 = 2\times(\sqrt{267}+5)\]
Since the radius is half the diameter, it is $\sqrt{267}+5$ , so the answer is $5+267 \Rightarrow \boxed{272}$ .

## Solution 4
As we can see this image, it is symmetrical hence the diameter divides the hexagon into two congruent quadrilateral. Now we can apply the Ptolemy's theorem. Denote the radius is r, we can get \[22*2x+440=\sqrt{4x^2-400}\sqrt{4x^2-484}\] , after simple factorization, we can get \[x^4-342x^2-2420x=0\] , it is easy to see that $x=-10, x=0$ are two solutions for the equation, so we can factorize that into \[x(x+10)(x^2-10x-242)\] so we only need to find the solution for \[x^2-10x-242=0\] and we can get $x=(\sqrt{267}+5)$ is the desired answer for the problem, and our answer is $5+267 \Rightarrow \boxed{272}$ .～bluesoul

## Solution 6 (Trig Bash)
Let $\angle{AOB} = \theta$ . So, we have $\sin \dfrac{\theta}{2} = \dfrac{11}{r}$ and $\cos \dfrac{\theta}{2} = \dfrac{\sqrt{r^{2} - 121}}{r}$ . So, $\sin \theta = 2 \sin \dfrac{\theta}{2} \cos \dfrac{\theta}{2} = \dfrac{22 \sqrt{r^{2} - 121}}{r^{2}}$ . Let $H$ be the foot of the perpendicular from $B$ to $\overline{AD}$ . We have $BF = 2 BH = 2 r \sin \theta = \dfrac{44 \sqrt{r^{2} - 121}}{r}$ . Using Pythagorean theorem on $\triangle BCF$ , to get $(\dfrac{44 \sqrt{r^{2} - 121}}{r})^{2} + 20^{2} = (2r)^{2}$ , or $\dfrac{44^{2}r^{2} - 44^{2} \cdot 121}{r^{2}} + 20^{2} = 4r^{4}$ . Multiplying by $r^{2}$ , we get $44^{2} r^{2} - 44^{2} \cdot 121 + 20^{2} r^{2} = 4r^{4}$ . Rearranging and simplifying, we get a quadratic in $r^{2}$ : \[r^{4} - 584r^{2} + 242^{2} = 0 \text{,}\] which gives us $r^{2} = 292 \pm 10\sqrt{267}$ . Because $r$ is in the form $p + \sqrt{q}$ , we know to choose the larger option, meaning $r^2 = 292 + 10\sqrt{267}$ , so $p\sqrt{q} = 5\sqrt{267}$ and $p^2 + q = 292$ . By inspection, we get $(p, q) = (5, 267)$ , so our answer is $5 + 267 = \boxed{272}$ .
~Puck_0

## Solution 7
[asy] import olympiad; import math; real a; a=2*asin(11/(5+sqrt(267))); pair A,B,C,D,E,F; A=expi(pi); B=expi(pi-a); C=expi(a); D=expi(0); E=expi(-a); F=expi(pi+a); draw(A--B--C--D--E--F--A--D); draw(B--D); draw(A--C); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); draw(unitcircle); label("$A$",A,W);label("$B$",B,NW);label("$C$",C,NE);label("$D$",D,dir(0));label("$E$",E,SE);label("$F$",F,SW); [/asy]
We know that $AD=x$ is a diameter, hence $ABD$ and $ACD$ are right triangles. Let $AB=BC=22$ , and $CD=20.$ Hence, $ABD$ is a right triangle with legs $22,\sqrt{x^2-484},$ and hypotenuse, $x,$ and $ACD$ is a right triangle with legs $20, \sqrt{x^2-400},$ with hypotenuse $x$ . By Ptolemy's we have \[22(x+20)=\sqrt{x^2-400}\sqrt{x^2-484}\] . We square both sides to get \[484(x+20)^2=(x^2-400)(x^2-484) \implies 484(x+20)=(x-20)(x^2-484) \implies 484x=x^3-20x^2-484x \implies x(x^2-20x-968)=0\]
We solve for $x$ via the Quadratic Formula and receive $x=10+2\sqrt{267}$ , but we must divide by $2$ since we want the radius, and hence $267+5=\boxed{272}.$ ~SirAppel
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .