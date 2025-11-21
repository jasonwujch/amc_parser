# 2009 AIME II Problem 10

## Problem

Four lighthouses are located at points $A$ , $B$ , $C$ , and $D$ . The lighthouse at $A$ is $5$ kilometers from the lighthouse at $B$ , the lighthouse at $B$ is $12$ kilometers from the lighthouse at $C$ , and the lighthouse at $A$ is $13$ kilometers from the lighthouse at $C$ . To an observer at $A$ , the angle determined by the lights at $B$ and $D$ and the angle determined by the lights at $C$ and $D$ are equal. To an observer at $C$ , the angle determined by the lights at $A$ and $B$ and the angle determined by the lights at $D$ and $B$ are equal. The number of kilometers from $A$ to $D$ is given by $\frac {p\sqrt{q}}{r}$ , where $p$ , $q$ , and $r$ are relatively prime positive integers, and $r$ is not divisible by the square of any prime. Find $p$ + $q$ + $r$ .

### Diagram

[asy] size(120); pathpen = linewidth(0.7); pointpen = black; pen f = fontsize(10); pair B=(0,0), A=(5,0), C=(0,13), E=(-5,0), O = incenter(E,C,A), D=IP(A -- A+3*(O-A),E--C); D(A--B--C--cycle); D(A--D--C); D(D--E--B, linetype("4 4")); MP("5", (A+B)/2, f); MP("13", (A+C)/2, NE,f); MP("A",D(A),f); MP("B",D(B),f); MP("C",D(C),N,f); MP("A'",D(E),f); MP("D",D(D),NW,f); D(rightanglemark(C,B,A,20)); D(anglemark(D,A,E,35));D(anglemark(C,A,D,30)); [/asy] -asjpz

## Video Solution by Punxsutawney Phil
https://www.youtube.com/watch?v=f3zEesJh4Ws

## Solution 1
Let $O$ be the intersection of $BC$ and $AD$ . By the Angle Bisector Theorem , $\frac {5}{BO}$ = $\frac {13}{CO}$ , so $BO$ = $5x$ and $CO$ = $13x$ , and $BO$ + $OC$ = $BC$ = $12$ , so $x$ = $\frac {2}{3}$ , and $OC$ = $\frac {26}{3}$ . Let $P$ be the foot of the altitude from $D$ to $OC$ . It can be seen that triangle $DOP$ is similar to triangle $AOB$ , and triangle $DPC$ is similar to triangle $ABC$ . If $DP$ = $15y$ , then $CP$ = $36y$ , $OP$ = $10y$ , and $OD$ = $5y\sqrt {13}$ . Since $OP$ + $CP$ = $46y$ = $\frac {26}{3}$ , $y$ = $\frac {13}{69}$ , and $AD$ = $\frac {60\sqrt{13}}{23}$ (by the pythagorean theorem on triangle $ABO$ we sum $AO$ and $OD$ ). The answer is $60$ + $13$ + $23$ = $\boxed{096}$ .

## Solution 2
Extend $AB$ and $CD$ to intersect at $P$ . Note that since $\angle ACB=\angle PCB$ and $\angle ABC=\angle PBC=90^{\circ}$ by ASA congruency we have $\triangle ABC\cong \triangle PBC$ . Therefore $AC=PC=13$ .
By the angle bisector theorem, $PD=\dfrac{130}{23}$ and $CD=\dfrac{169}{23}$ . Now we apply Stewart's theorem to find $AD$ :
\begin{align*}13\cdot \dfrac{130}{23}\cdot \dfrac{169}{23}+13\cdot AD^2&=13\cdot 13\cdot \dfrac{130}{23}+10\cdot 10\cdot \dfrac{169}{23}\\ 13\cdot \dfrac{130}{23}\cdot \dfrac{169}{23}+13\cdot AD^2&=\dfrac{169\cdot 130+169\cdot 100}{23}\\ 13\cdot \dfrac{130}{23}\cdot \dfrac{169}{23}+13\cdot AD^2&=1690\\ AD^2&=130-\dfrac{130\cdot 169}{23^2}\\ AD^2&=\dfrac{130\cdot 23^2-130\cdot 169}{23^2}\\ AD^2&=\dfrac{130(23^2-169)}{23^2}\\ AD^2&=\dfrac{130(360)}{23^2}\\ AD&=\dfrac{60\sqrt{13}}{23}\\ \end{align*}
and our final answer is $60+13+23=\boxed{096}$ .

## Solution 3
Notice that by extending $AB$ and $CD$ to meet at a point $E$ , $\triangle ACE$ is isosceles. Now we can do a straightforward coordinate bash. Let $C=(0,0)$ , $B=(12,0)$ , $E=(12,-5)$ and $A=(12,5)$ , and the equation of line $CD$ is $y=-\dfrac{5}{12}x$ . Let F be the intersection point of $AD$ and $BC$ , and by using the Angle Bisector Theorem: $\dfrac{BF}{AB}=\dfrac{FC}{AC}$ we have $FC=\dfrac{26}{3}$ . Then the equation of the line $AF$ through the points $(12,5)$ and $\left(\frac{26}{3},0\right)$ is $y=\frac32 x-13$ . Hence the intersection point of $AF$ and $CD$ is the point $D$ at the coordinates $\left(\dfrac{156}{23},-\dfrac{65}{23}\right)$ . Using the distance formula, $AD=\sqrt{\left(12-\dfrac{156}{23}\right)^2+\left(5+\dfrac{65}{23}\right)^2}=\dfrac{60\sqrt{13}}{23}$ for an answer of $60+13+23=\fbox{096}$ .

## Solution 4
After drawing a good diagram, we reflect $ABC$ over the line $BC$ , forming a new point that we'll call $A'$ . Also, let the intersection of $AD$ and $BC$ be point $E$ . Point $D$ lies on line $A'C$ . Since line $AD$ bisects $\angle{CAB}$ , we can use the Angle Bisector Theorem. $AA'=10$ and $AC=13$ , so $\frac{CD}{A'D}=\frac{13}{10}$ . Letting the segments be $13x$ and $10x$ respectively, we now have $13x+10x=13$ . Therefore, $x=\frac{13}{23}$ . By the Pythagorean Theorem, $AE=\frac{5\sqrt{13}}{3}$ . Using the Angle Bisector Theorem on $\angle{ACD}$ , we have that $ED=\frac{5x\sqrt{13}}{3}$ . Substituting in $x=\frac{13}{23}$ , we have that $AD=\left(\frac{5\sqrt{13}}{3}\right)(1+x)=\frac{60\sqrt{13}}{23}$ , so the answer is $60+13+23=\boxed{096}$ .
-RootThreeOverTwo

## Solution 5 (Angle Bisector Theorem + Law of Cosines)
Let $CD$ and $AB$ meet at $A'$ ; then $\overline{AD}$ is an angle bisector of isosceles $\triangle AA'C$ . Then by the Angle Bisector Theorem, $A'D=\frac {10}{10+13} \cdot 13=\frac {130}{23}$ , and $\cos \angle DA'A=\frac {5}{13}$ . By the Law of Cosines on $\triangle AA'D$ , we have \[AD^2=10^2+\left(\frac {130}{23}\right)^2-2 \cdot 10 \cdot \frac {130}{23} \cdot \frac {5}{13}=\frac {2^4 \cdot 3^2 \cdot 5^2 \cdot 13}{23^2} \Longrightarrow AD=\frac {60\sqrt {13}}{23}\] and the answer is $60+13+23=\boxed{096}$ .
[asy] size(120); pathpen = linewidth(0.7); pointpen = black; pen f = fontsize(10); pair B=(0,0), A=(5,0), C=(0,13), E=(-5,0), O = incenter(E,C,A), D=IP(A -- A+3*(O-A),E--C); D(A--B--C--cycle); D(A--D--C); D(D--E--B, linetype("4 4")); MP("5", (A+B)/2, f); MP("13", (A+C)/2, NE,f); MP("A",D(A),f); MP("B",D(B),f); MP("C",D(C),N,f); MP("A'",D(E),f); MP("D",D(D),NW,f); D(rightanglemark(C,B,A,20)); D(anglemark(D,A,E,35));D(anglemark(C,A,D,30)); [/asy]
-azjps

## Solution 6 (Law of Sines)
[asy]pathpen = linewidth(0.7); pen f = fontsize(10); size(144); pair B=(0,0); pair A=(5,0); pair C=(0,12); pair E=(-5,0); pair abA = A+unit(C-A)+unit(B-A); pair D = extension(A,abA,C,E); D(A--C); D(C--B); D(A--B); D(C--D); D(A--D); D(D--E,dashed); D(B--E,dashed); D(rightanglemark(C,B,A,20),red); MP("A",D(A),plain.SE,f); MP("B",D(B),plain.S,f); MP("C",D(C),plain.N,f); MP("D",D(D),plain.NW,f); MP("E",D(E),plain.SW,f); MP("5",(A+B)/2,plain.S,f); MP("12",(B+C)/2,plain.E,f); MP("13",(A+C)/2,plain.NE,f); MP("\alpha",A,4*(unit(D-A)+unit(C-A))/2,f); MP("\alpha",A,4*(unit(B-A)+unit(D-A))/2,f); MP("2\alpha",E,4*(unit(C-E)+unit(B-E))/2,f); MP("\beta",C,6*(unit(A-C)+unit(B-C))/2,f); MP("\beta",C,6*(unit(E-C)+unit(B-C))/2,f);[/asy]
Using the law of sines on $\bigtriangleup ADE$ ,
\begin{align*} AD &= AE \cdot \dfrac{\sin(2\alpha)}{\sin(180^\circ-3\alpha)}\\ &= AE \cdot \dfrac{\sin(2\alpha)}{\sin(\alpha+2\alpha)}\\ &= 10 \cdot \dfrac{\sin(2\alpha)}{\sin(\alpha)\cos(2\alpha)+\cos(\alpha)\sin(2\alpha)}\\ &= 10 \cdot \dfrac{\sin(2\alpha)}{\sqrt{\dfrac{1-\cos(2\alpha)}{2}}\cdot\cos(2\alpha)+\sqrt{\dfrac{1+\cos(2\alpha)}{2}}\cdot\sin(2\alpha)}\\ &= 10 \cdot \dfrac{\dfrac{12}{13}}{\sqrt{\dfrac{8}{26}}\cdot\dfrac{5}{13}+\sqrt{\dfrac{18}{26}}\cdot\dfrac{12}{13}}\\ &= 10 \cdot \dfrac{12\sqrt{13}}{10+36} = \dfrac{60\sqrt{13}}{23} \end{align*}
$\therefore$ the answer is $60+13+23=\boxed{096}$ .
-m1sterzer0
### See Also
These problems are copyrighted © by the Mathematical Association of America.