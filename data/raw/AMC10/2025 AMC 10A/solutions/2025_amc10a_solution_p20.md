# 2025 AMC 10A Problem 20

## Problem

A silo (right circular cylinder) with diameter 20 meters stands in a field. MacDonald is located 20 meters west and 15 meters south of the center of the silo. McGregor is located 20 meters east and $g > 0$ meters south of the center of the silo. The line of sight between MacDonald and McGregor is tangent to the silo. The value of g can be written as $\frac{a\sqrt{b}-c}{d}$ , where $a,b,c,$ and $d$ are positive integers, $b$ is not divisible by the square of any prime, and $d$ is relatively prime to the greatest common divisor of $a$ and $c$ . What is $a+b+c+d$ ?

$\textbf{(A) } 119 \qquad\textbf{(B) } 120 \qquad\textbf{(C) } 121 \qquad\textbf{(D) } 122 \qquad\textbf{(E) } 123$

## Solution 1
[asy] import olympiad; size(340); // numeric setup for reliable AoPS rendering real R = 10; pair O = (0,0); pair B = (-20,0); pair A = (-20,-15); pair C = (20,0); real g = 5.55; // approximate numeric version of (20√21−75)/3 pair D = (20,-g); pair E = (2.30,-9.74); pair F = intersectionpoint(A--(A+4*(D-A)), B--(B+4*(C-B))); filldraw(circle(O,R), white, heavyblue); draw(A--F, heavygreen); draw(B--F); draw(A--B--O--cycle); draw(O--E); draw((C+2*(C-D))--(C + 3*(D-C)), dashed); dot(A); label("$A$", A, SW); dot(B); label("$B$", B, NW); dot(C); label("$C$", C, NE); dot(D); label("$D$", D, SE); dot(E); label("$E$", E, NE); dot(O); label("$O$", O, N); dot(F); label("$F$", F, S); draw(rightanglemark(A,B,O,50)); label("$20$", midpoint(B--O), dir(90)); label("$15$", midpoint(A--B), W); label("$25$", midpoint(A--O), SE); label("$g$", (C+D)/2, W); label(“?”, midpoint(A--F), SE); currentpicture.fit(); [/asy]
Let the silo center be $O$ , let the point MacDonald is situated at be $A$ , and let the point $20$ meters west of the silo center be $B$ . $ABO$ is then a right triangle with side lengths $15, 20,$ and $25$ .
Let the point $20$ meters east of the silo center be $C$ , and let the point McGregor is at be $D$ with $CD=g>0$ . Also let $AD$ be tangent to circle $O$ at $E$ .
Extend $BC$ and $AD$ to meet at point $F$ . This creates $3$ similar triangles, $\triangle ABF\sim \triangle DCF \sim \triangle OEF$ . Let the distance between point $C$ and $F$ be $x$ . The similarity ratio between triangles $ABF$ and $DCF$ is then $\frac{longer\;leg}{shorter\;leg} = \frac{40+x}{15} = \frac{x}{g}$
This is currently unsolvable so we bring in triangle $OEF$ . The hypotenuse of triangle $OEF$ is $OF=20+x$ and its shorter leg is the radius of the silo $=10$ . We can then establish a second similarity relationship between triangles $OEF$ and $ABF$ with $\frac{shorter\; leg}{hypotenuse}=\frac{10}{20+x}=\frac{15}{AF}$
Now we find the hypotenuse of $ABF$ in terms of $x$ using the Pythagorean theorem. $AF^2=15^2+(40+x)^2$ . Which simplifies to $AF^2=225+1600+80x+x^2=1825+80x+x^2$ So $AF=\sqrt{x^2+80x+1825}$
Plugging back in we get $\frac{10}{20+x}=\frac{15}{\sqrt{x^2+80x+1825}}$ . Now we can begin to break this down by multiplying both sides by both denominators. $10(\sqrt{x^2+80x+1825})=15(20+x)$ Dividing both sides by $5$ then squaring yields, $4x^2+320x+7300=9x^2+360x+3600$ This furthermore simplifies to $5x^2+40x-3700=0$ At which point we can divide off a $5$ and then apply the quadratic formula on $x^2+8x-740=0$ which we take the positive root of.
\[x = \frac{-8+\sqrt{64+2960}}{2} = \frac{-8+\sqrt{3024}}{2} =\frac{-8+\sqrt{144 \cdot 21}}{2}.\]
Simplifying yields that $x=6\sqrt{21}-4$
Then to solve for $g$ we simply plug $6\sqrt{21}-4$ back into the first similarity ratio to get $\frac{36+6\sqrt{21}}{15}=\frac{6\sqrt{21}-4}{g}$
Multiply both sides by $15g$ and dividing by $36+6\sqrt{21}$ will let us solve for $g=\frac{15(6\sqrt{21}-4)}{36+6\sqrt{21}}$ and after rationalizing the denominator we get $\frac{20\sqrt{21}-75}{3}$ . $20+21+75+3=\boxed{\textbf{(A)}~119}$
$\sim$ Nioronean ~ happyfish0922 (minor edit regarding what was previously point T changed to point E) ~ Avs2010 (diagram)
~JerryZYang (minor edit in latex and style)

## Solution 2 (Coordinates)
Let MacDonald's position be at $(0,0)$ . Then, the center of the silo will be at $(20,15)$ and McGregor will be at $(40, 15-g)$ .
Let the line of sight between MacDonald and McGregor be represented by the line $y=mx$ , where $m=\frac{15-g}{40}$ . As the radius of the silo is $10$ , we can construct the equation of a circle and get the system of equations: \[y=mx\] \[(x-20)^2+(y-15)^2=100\]
Substituting, we get: \[(x-20)^2+(mx-15)^2=100\] \[x^2-40x+400+m^2x^2-30mx+225=100\] \[(m^2+1)x^2-(30m+40)x+525=0\]
We want a value of $m$ such that this equation has $1$ solution, so we set the discriminant to be equal to $0$ . \[(30m+40)^2-4(m^2+1)(525)=0\] \[900m^2+2400m+1600-2100m^2-2100=0\] \[12m^2-24m+5=0\] \[m=\frac{24 \pm \sqrt{576-240}}{24}\] \[m=\frac{6 \pm \sqrt{21}}{6}\]
The slope obviously has to be less than $1$ , so we take the negative root $\frac{6-\sqrt{21}}{6}$ .
Substituting back for $m$ and solving for $g$ , \[\frac{15-g}{40}=\frac{6-\sqrt{21}}{6}\] \[15-g=\frac{20}{3}(6-\sqrt{21})\] \[g=\frac{20\sqrt{21}-75}{3}\]
Finally, $a=20$ , $b=21$ , $c=75$ , and $d=3$ , summing up to a total of $20+21+75+3=\boxed{\textbf{(A)}~119}$
~megaboy6679 (I actually did this in the comp)

## Solution 3 (Trig)
(I don't know how to make a diagram or latex very well oops)
Let the silo center be $O$ , let the point MacDonald is situated at be $A$ , and let the point $15$ meters south of the silo center be $B$ . $ABO$ is then a right triangle with side lengths $15, 20, 25$ .
Also let the tangency point be $E$ . Then, because a tangent line is defined as having a right angle to the radius $OE$ , triangle $AEO$ is also a right triangle with side lengths $5\sqrt{21},10,25$ since we know $AO$ is 25 from pythag on $ABO$ and that $OE$ is 10 because it's a radius, so $AE$ follows from pythag on $AEO$ .
Let the position McGregor is in be $G$ and let the point that is both directly south of McGregor and directly east of MacDonald be $F$ . (For reference, $F$ is $20$ meters east and $15$ meters south of O, which is also $40$ meters east of D and $15-g$ meters south of $G$ .)
Now, we can see that the triangle $AFG$ is also a right triangle. Since $G$ is on the line $AE$ by definition and $F$ is on line $AB$ because they are all on the same horizontal line $15$ meters south of O, $\angle GAF=\angle EAB$ . This leads us to conclude that $\tan{\angle GAF}=\frac{15-g}{40}=\tan{\angle EAB}$ .
From here, we can use tangent subtraction formula to find $\tan(\angle EAB)$ .
We know that $\tan(\angle OAB)=\frac{15}{20}=\frac34$ and that $\tan(\angle OAE)=\frac{10}{5\sqrt{21}}\frac2{\sqrt{21}}$ . Since $\angle EAB = \angle OAB - \angle OAE$ , we have that
$\tan(\angle EAB)=\tan(\angle OAB - \angle OAE)=\frac{\tan(\angle OAB)-\tan(\angle OAE)}{1+\tan(\angle OAB)\tan(\angle OAE)}=\frac{\frac34-\frac2{\sqrt{21}}}{1+\frac6{4\sqrt{21}}}$
Multiplying the top and bottom by $4\sqrt{21}$ , this equals
$\frac{3\sqrt{21}-8}{4\sqrt{21}+6}=\frac12\cdot\frac{3\sqrt{21}-8}{2\sqrt{21}+3}$ (factoring out $\frac12$ is personal preference)
Now, rationalizing the denominator by multiplying the top and bottom by $2\sqrt{21}-3$ , we get this equals
$\frac12\cdot\frac{(3\sqrt{21}-8)\cdot(2\sqrt{21}-3)}{(2\sqrt{21}+3)\cdot(2\sqrt{21}-3)}=\frac12\cdot\frac{150-25\sqrt{21}}{75}=\frac{6-\sqrt{21}}6$
Recalling that this implies $\frac{15-g}{40}=\frac{6-\sqrt{21}}6$ , we get that $g=\frac{20\sqrt{21}-75}{3}$ . $20+21+75+3=\boxed{\textbf{(A)}~119}$
~Ant_Eater

## Solution 4
[asy] import olympiad; size(340); // numeric setup for reliable AoPS rendering real R = 10; pair O = (0,0); pair B = (-20,0); pair A = (-20,-15); pair C = (20,0); real g = 5.55; // approximate numeric version of (20√21−75)/3 pair D = (20,-g); pair E = (2.30,-9.74); pair F = intersectionpoint(A--(A+4*(D-A)), B--(B+4*(C-B))); filldraw(circle(O,R), white, heavyblue); draw(A--F, heavygreen); draw(B--F); draw(A--B--O--cycle); draw(O--E); draw((C+2*(C-D))--(C + 3*(D-C)), dashed); dot(A); label("$A$", A, SW); dot(B); label("$B$", B, NW); dot(C); label("$C$", C, NE); dot(D); label("$D$", D, SE); dot(E); label("$E$", E, NE); dot(O); label("$O$", O, N); dot(F); label("$F$", F, S); draw(rightanglemark(A,B,O,50)); label("$20$", midpoint(B--O), dir(90)); label("$15$", midpoint(A--B), W); label("$25$", midpoint(A--O), SE); label("$g$", (C+D)/2, W); currentpicture.fit(); [/asy]
We use the point names given in Solution 1.
By Pythagorean Theorem (twice), we have \[AE=\sqrt{AO^2-OE^2}=\sqrt{AB^2+BO^2-10^2}=\sqrt{525}=5\sqrt{21}.\] Similarly, we find that \[DE=\sqrt{DO^2-OE^2}=\sqrt{CD^2+CO^2-10^2}=\sqrt{300+g^2}.\] Note that the altitude from $D$ to $AB$ (call the foot $H$ ) has length $40$ . Also, $AD=AE+DE=5\sqrt{21}+\sqrt{300+g^2}$ and $DH=15-g$ . By Pythagoras on $\triangle ADH$ , we have \[\left(5\sqrt{21}+\sqrt{300+g^2}\right)^2=40^2+(15-g)^2.\] Expanding, \[525+10\sqrt{21}\cdot\sqrt{300+g^2}+300+g^2=1600+225-30g+g^2\] and simplifying gives \[10\sqrt{6300+21g^2}=1000-30g.\] Dividing by $10$ and squaring, \[6300+21g^2=10000-600g+9g^2\] and putting it in standard form, \[0=12g^2+600g-3700.\] Dividing by $4$ and applying the quadratic formula, \[g=\frac{-150\pm\sqrt{22500-4(3)(-925)}}{6}=\frac{-75\pm20\sqrt{21}}3.\] From the answer form, we take the positive root, so \[g=\frac{20\sqrt{21}-75}3.\] Finally, we have $20+21+75+3=\boxed{\text{(A) }119}.$
~Waddles2010 (Minor calculation error fixed by hellokikki)

## Solution 5 (trig & similarity)
[asy] import olympiad; size(340); // numeric setup for reliable AoPS rendering real R = 10; pair O = (0,0); pair B = (-20,0); pair A = (-20,-15); pair C = (20,0); real g = 5.55; // approximate numeric version of (20√21−75)/3 pair D = (20,-g); pair E = (2.30,-9.74); pair F = intersectionpoint(A--(A+4*(D-A)), B--(B+4*(C-B))); filldraw(circle(O,R), white, heavyblue); draw(A--F, heavygreen); draw(B--F); draw(A--B--O--cycle); draw(O--E); draw((C+2*(C-D))--(C + 3*(D-C)), dashed); dot(A); label("$A$", A, SW); dot(B); label("$B$", B, NW); dot(C); label("$C$", C, NE); dot(D); label("$D$", D, SE); dot(E); label("$E$", E, NE); dot(O); label("$O$", O, N); dot(F); label("$F$", F, S); draw(rightanglemark(A,B,O,50)); label("$20$", midpoint(B--O), dir(90)); label("$15$", midpoint(A--B), W); label("$25$", midpoint(A--O), SE); label("$g$", (C+D)/2, W); currentpicture.fit(); [/asy]
First, taking the Pythagorean Theorem on $\Delta BOD$ and $\Delta AOE$ gives $AO = 25, AE = 5\sqrt{21}$ . By cosine angular addition, $\cos{(\angle BOD + \angle AOE)} = \cos{\angle BOE} = \frac{8-3\sqrt21}{25}$ , so $\cos{\angle EOC} = \frac{3\sqrt21-8}{25}$ .
Dropping the altitude from $E$ to $BC$ and labelling the foot $P$ , we have that $OP = 10 \cdot \frac{3\sqrt21-8}{25} = \frac{6\sqrt21-16}{5}$ , so the ratio of $BP$ to $BC$ is $\frac{3\sqrt{21}+42}{100}$ . This is the same as the ratio of $AE$ to $AD$ , so $AD = 5\sqrt{21} \cdot \frac{100}{3\sqrt{21}+42} = \frac{20}{3} \cdot (2\sqrt{21}-3)$ .
Dropping the altitude from $D$ to $AB$ and labelling the foot $Q$ , $AQ$ can be (tediously) computed to be $\frac{20}{3} \cdot \sqrt{(2\sqrt{21}-3)^2-6^2} = \frac{20}{3} \cdot \sqrt{57-12\sqrt{21}} = \frac{20}{3} \cdot (6-\sqrt{21}) =\frac{120-20\sqrt{21}}{3}$ , and subtracting this from $AB$ gives the length of $BQ$ equivalent to $CD$ , which is our desired length, so our answer is $\frac{20\sqrt{21}-75}{3} \implies \boxed{\text{(A) }119}.$
~ tiguhbabehwo
~Sakura_kitty (copy and pasted diagram, plz add point p, idk how to use latex.)

## Solution 6
[asy] import geometry; unitsize(7); pair _O = (0,0); pair _B = (-20,0); pair _A = (-20,-15); pair _C = (20,0); pair _D = (20, -(20sqrt(21)-75)/3); pair _E = extension(_A, _D, _O, _O + rotate(90)*(_A - _D)); pair _F = (_A + _D)/2; pair _G = (-20, _D.y); draw(arc(_O, 10, 0, -180)); draw(_A -- _D -- _C -- _B -- _A ^^ _E -- _O -- (_A + _D)/2); draw(_D -- _G, dashed); dot(_A ^^ _B ^^ _C ^^ _D ^^ _E ^^ _F ^^ _G ^^ _O); markrightangle(_A, _B, _O, 0.5*markangleradius()); label("$A$", _A, SW); label("$B$", _B, NW); label("$C$", _C, NE); label("$D$", _D, SE); label("$E$", _E, S); label("$F$", _F, S); label("$G$", _G, SE); label("$O$", _O, N); label("$20$", midpoint(_B -- _O), N); label("$20$", midpoint(_C -- _O), N); label("$15$", midpoint(_A -- _B), W); label("$10$", (_E + 2_O)/3, SE); label("$g$", midpoint(_C -- _D), E); [/asy]
$F$ is the midpoint of $AD$ , $DG \perp AB$ . Notice that $\triangle OEF \sim \triangle DGA$ , we have \[\frac{OE}{OF} = \frac{DG}{DA}\] Given the length of $CD$ is $g$ , $OF$ is the midline, $CD = BG$ , therefore $GA = 15 - g$ , $DA = \sqrt{40^2 + (15 - g)^2}$ , $OF = \dfrac{15 + g}{2}$ \[\frac{OE}{OF} = \frac{DG}{GA}\] \[\cfrac{10}{\cfrac{15 + g}{2}} = \frac{40}{\sqrt{40^2 + (15 - g)^2}}\] \[2(15 + g) = \sqrt{40^2 + (15 - g)^2}\] \[3g^2 + 150g - 925 = 0\] \[g = \frac{-150 + \sqrt{22500 + 11100}}{6}\] \[g = \frac{20\sqrt{21}-75}{3}\] The answer is $20+21+75+3=\boxed{\textbf{(A)}~119}$
~ reda_mandymath

## Video Solution 1 by OmegaLearn.org
https://youtu.be/JlGQWan5fRE

## Video Solution by grogg007
https://youtu.be/wTk9fhyXpNU

## Video Solution (In 5 Mins)
https://youtu.be/1Xc1blWnWSo?si=pBd85mIZwYjbOEdG ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .