# 2023 AIME I Problem 12

## Problem

Let $\triangle ABC$ be an equilateral triangle with side length $55.$ Points $D,$ $E,$ and $F$ lie on $\overline{BC},$ $\overline{CA},$ and $\overline{AB},$ respectively, with $BD = 7,$ $CE=30,$ and $AF=40.$ Point $P$ inside $\triangle ABC$ has the property that \[\angle AEP = \angle BFP = \angle CDP.\] Find $\tan^2(\angle AEP).$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(300); pair A, B, C, D, E, F, P; A = 55*sqrt(3)/3 * dir(90); B = 55*sqrt(3)/3 * dir(210); C = 55*sqrt(3)/3 * dir(330); D = B + 7*dir(0); E = A + 25*dir(C-A); F = A + 40*dir(B-A); P = intersectionpoints(Circle(D,54*sqrt(19)/19),Circle(F,5*sqrt(19)/19))[0]; draw(anglemark(A,E,P,20),red); draw(anglemark(B,F,P,20),red); draw(anglemark(C,D,P,20),red); add(pathticks(anglemark(A,E,P,20), n = 1, r = 0.2, s = 12, red)); add(pathticks(anglemark(B,F,P,20), n = 1, r = 0.2, s = 12, red)); add(pathticks(anglemark(C,D,P,20), n = 1, r = 0.2, s = 12, red)); draw(A--B--C--cycle^^P--E^^P--F^^P--D); dot("$A$",A,1.5*dir(A),linewidth(4)); dot("$B$",B,1.5*dir(B),linewidth(4)); dot("$C$",C,1.5*dir(C),linewidth(4)); dot("$D$",D,1.5*S,linewidth(4)); dot("$E$",E,1.5*dir(30),linewidth(4)); dot("$F$",F,1.5*dir(150),linewidth(4)); dot("$P$",P,1.5*dir(-30),linewidth(4)); label("$7$",midpoint(B--D),1.5*S,red); label("$30$",midpoint(C--E),1.5*dir(30),red); label("$40$",midpoint(A--F),1.5*dir(150),red); [/asy] ~MRENTHUSIASM

## Solution 1 (Coordinates Bash)
By Miquel's theorem, $P=(AEF)\cap(BFD)\cap(CDE)$ (intersection of circles) $\text{*}$ . The law of cosines can be used to compute $DE=42$ , $EF=35$ , and $FD=13$ . Toss the points on the coordinate plane; let $B=(-7, 0)$ , $D=(0, 0)$ , and $C=(48, 0)$ , where we will find $\tan^{2}\left(\measuredangle CDP\right)$ with $P=(BFD)\cap(CDE)$ .
By the extended law of sines, the radius of circle $(BFD)$ is $\frac{13}{2\sin 60^{\circ}}=\frac{13}{3}\sqrt{3}$ . Its center lies on the line $x=-\frac{7}{2}$ , and the origin is a point on it, so $y=\frac{23}{6}\sqrt{3}$ .
The radius of circle $(CDE)$ is $\frac{42}{2\sin 60^{\circ}}=14\sqrt{3}$ . The origin is also a point on it, and its center is on the line $x=24$ , so $y=2\sqrt{3}$ .
The equations of the two circles are \begin{align*}(BFD)&:\left(x+\tfrac{7}{2}\right)^{2}+\left(y-\tfrac{23}{6}\sqrt{3}\right)^{2}=\tfrac{169}{3} \\ (CDE)&:\left(x-24\right)^{2}+\left(y-2\sqrt{3}\right)^{2}=588\end{align*} These equations simplify to \begin{align*}(BFD)&:x^{2}+7x+y^{2}-\tfrac{23}{3}\sqrt{3}y=0 \\ (CDE)&: x^{2}-48x+y^{2}-4\sqrt{3}y=0\end{align*} Subtracting these two equations gives that both their points of intersection, $D$ and $P$ , lie on the line $55x-\tfrac{11}{3}\sqrt{3}y=0$ . Hence, $\tan^{2}\left(\measuredangle AEP\right)=\tan^{2}\left(\measuredangle CDP\right)=\left(\frac{55}{\tfrac{11}{3}\sqrt{3}}\right)^{2}=3\left(\tfrac{55}{11}\right)^{2}=\boxed{075}$ . To scale, the configuration looks like the figure below: [asy] /* Made by MRENTHUSIASM */ size(400); pair A, B, C, D, E, F, P; A = 55*sqrt(3)/3 * dir(90); B = 55*sqrt(3)/3 * dir(210); C = 55*sqrt(3)/3 * dir(330); D = B + 7*dir(0); E = A + 25*dir(C-A); F = A + 40*dir(B-A); P = intersectionpoints(Circle(D,54*sqrt(19)/19),Circle(F,5*sqrt(19)/19))[0]; filldraw(D--E--F--cycle,yellow); draw(A--B--C--cycle); draw(circumcircle(A,E,F)^^circumcircle(B,D,F)^^circumcircle(C,D,E),blue); dot("$A$",A,1.5*dir(A),linewidth(4)); dot("$B$",B,1.5*dir(B),linewidth(4)); dot("$C$",C,1.5*dir(C),linewidth(4)); dot("$D$",D,1.5*S,linewidth(4)); dot("$E$",E,1.5*dir(30),linewidth(4)); dot("$F$",F,1.5*dir(150),linewidth(4)); dot("$P$",P,1.5*dir(-30),linewidth(4)); label("$7$",midpoint(B--D),1.5*S,red); label("$30$",midpoint(C--E),1.5*dir(30),red); label("$40$",midpoint(A--F),1.5*dir(150),red); [/asy]
$\text{*}$ Basic angle chasing gives $\angle BDP=180-\angle CDP.$ Because $\angle BFP+\angle BDP=180+\angle BFP-\angle CDP=180,$ which means that $BFPD$ is cyclic, and that $P$ passes through the circumcircle of triangle $BFD.$ Similar reasoning leads us to the fact that $P$ also passes through the circumcircles of triangles $AEF$ and $CDE,$ which means that $P=(AEF)\cap(BFD)\cap(CDE).$ Continue as above.
Note: Since $D$ and $P$ are the two intersections of $(BFD)$ and $(CDE),$ we know that $DP$ is perpendicular to the line between the centers of $(BFD)$ and $(CDE).$ Thus, after getting the coordinates of the centers of $(BFD)$ and $(CDE),$ we can then immediately find the slope of line $DP,$ and then get the answer from there.

## Solution 2 (Vectors/Complex)
Denote $\theta = \angle AEP$ .
In $AFPE$ , we have $\overrightarrow{AF} + \overrightarrow{FP} + \overrightarrow{PE} + \overrightarrow{EA} = 0$ . Thus, \[ AF + FP e^{i \theta} + PE e^{i \left( \theta + 60^\circ \right)} + EA e^{- i 120^\circ} = 0. \]
Taking the real and imaginary parts, we get \begin{align*} AF + FP \cos \theta + PE \cos \left( \theta + 60^\circ \right) + EA \cos \left( - 120^\circ \right) & = 0 \hspace{1cm} (1) \\ FP \sin \theta + PE \sin \left( \theta + 60^\circ \right) + EA \sin \left( - 120^\circ \right) & = 0 \hspace{1cm} (2) \end{align*}
In $BDPF$ , analogous to the analysis of $AFPE$ above, we get \begin{align*} BD + DP \cos \theta + PF \cos \left( \theta + 60^\circ \right) + FB \cos \left( - 120^\circ \right) & = 0 \hspace{1cm} (3) \\ DP \sin \theta + PF \sin \left( \theta + 60^\circ \right) + FB \sin \left( - 120^\circ \right) & = 0 \hspace{1cm} (4) \end{align*}
Taking $(1) \cdot \sin \left( \theta + 60^\circ \right) - (2) \cdot \cos \left( \theta + 60^\circ \right)$ , we get \[ AF \sin \left( \theta + 60^\circ \right) + \frac{\sqrt{3}}{2} FP - EA \sin \theta = 0 . \hspace{1cm} (5) \]
Taking $(3) \cdot \sin \theta - (4) \cdot \cos \theta$ , we get \[ BD \sin \theta - \frac{\sqrt{3}}{2} FP + FB \sin \left( \theta + 120^\circ \right) . \hspace{1cm} (6) \]
Taking $(5) + (6)$ , we get \[ AF \sin \left( \theta + 60^\circ \right) - EA \sin \theta + BD \sin \theta + FB \sin \left( \theta + 120^\circ \right) . \]
Therefore, \begin{align*} \tan \theta & = \frac{\frac{\sqrt{3}}{2} \left( AF + FB \right)} {\frac{FB}{2} + EA - \frac{AF}{2} - BD} \\ & = 5 \sqrt{3} . \end{align*}
Therefore, $\tan^2 \theta = \boxed{075}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3 (Synthetic)
Drop the perpendiculars from $P$ to $\overline{AB}$ , $\overline{AC}$ , $\overline{BC}$ , and call them $Q,R,$ and $S$ respectively. This gives us three similar right triangles $FQP$ , $ERP$ , and $DSP.$
The sum of the perpendiculars to a point $P$ within an equilateral triangle is always constant, so we have that $PQ+PR+PS=\dfrac{55 \sqrt{3}}{2}.$
The sum of the lengths of the alternating segments split by the perpendiculars from a point $P$ within an equilateral triangle is always equal to half the perimeter, so $QA+RC+SB = \dfrac{165}{2},$ which means that $FQ+ER+DS = QA+RC+SB - CE - AF - BD = \dfrac{165}{2} - 30 - 40 - 7 = \dfrac{11}{2}.$
Finally, $\tan AEP = \dfrac{PQ}{FQ} = \dfrac{PR}{ER} = \dfrac{PS}{DS} = \dfrac{PQ+PR+PS}{FQ+ER+DS} = 5 \sqrt{3}.$
Thus, $\tan^2 AEP = \boxed{075}.$
~anon
Claim
a) Carnot's theorem. Given triangle $\triangle ABC$ and point $P.$ Let $PS \perp BC,$ $PR \perp AC, PQ \perp AB.$ $P$ doesn't have to be inside $\triangle ABC.$
Prove that $AQ^2 + BS^2 + CR^2 = AR^2 + BQ^2 + CS^2.$
b) Let $\triangle ABC$ be the equilateral triangle. Prove that $AQ + BS + CR = \frac {3}{2} AB.$ (The sum of the lengths of the alternating segments split by the perpendiculars from a point $P$ within an equilateral triangle is equal to half the perimeter.)
Proof
a) $AP^2 = AQ^2 + PQ^2 = AR^2 + PR^2,$ \[BP^2 = BQ^2 + PQ^2 = BS^2 + PS^2,\] \[CP^2 = CR^2 + PR^2 = CS^2 + PS^2 \implies\] $AQ^2 + PQ^2 + BS^2 + PS^2 + CR^2 + PR^2 = AR^2 + PR^2 + BQ^2 + PQ^2 + CS^2 + PS^2,$ \[AQ^2 + BS^2 + CR^2 = AR^2 + BQ^2 + CS^2.\] b) $AQ + BQ = BS + CS = CR + AR = AB = AC = BC,$ \[AQ^2 + BQ^2 + 2 AQ \cdot BQ + BS^2 + CS^2 + 2 BS \cdot CS + AR^2 + CR^2+ 2 AR \cdot CR = 3 AB^2.\]
\[2AQ^2 + 2 AQ \cdot BQ + 2 BS^2 + 2 BS \cdot CS + 2 CR^2 + 2 AR \cdot CR = 3 AB^2.\] \[AQ (AQ + BQ) + BS (BS + CS) + CR (AR + CR) = \frac {3}{2} AB^2.\] \[AQ \cdot AB + BS \cdot BC + CR \cdot AC = \frac {3}{2} AB^2.\] \[AQ + BS + CR = \frac {3}{2} AB.\]
vladimir.shelomovskii@gmail.com, vvsss

## Solution 4 (Law of Cosines)
This solution is inspired by AIME 1999 Problem 14 Solution 2 (a similar question)
Draw line segments from $P$ to points $A$ , $B$ , and $C$ . And label the angle measure of $\angle{BFP}$ , $\angle{CDP}$ , and $\angle{AEP}$ to be $\alpha$
Using Law of Cosines (note that $\cos{\angle{AFP}}=\cos{\angle{BDP}}=\cos{\angle{CEP}}=\cos{180^\circ-\alpha}=-\cos{\alpha}$ )
\begin{align*} (1) \ BP^2 &= FP^2+15^2-2\cdot FP\cdot15\cdot\cos(\alpha)\\ (2) \ BP^2 &= DP^2+7^2+2\cdot DP\cdot7\cdot\cos(\alpha)\\ (3) \ CP^2 &= DP^2+48^2-2\cdot DP\cdot48\cdot\cos(\alpha)\\ (4) \ CP^2 &= EP^2+30^2+2\cdot EP\cdot30\cdot\cos(\alpha)\\ (5) \ AP^2 &= EP^2+25^2-2\cdot EP\cdot25\cdot\cos(\alpha)\\ (6) \ AP^2 &= FP^2+40^2+2\cdot FP\cdot40\cdot\cos(\alpha)\\ \end{align*}
We can perform this operation $(1) - (2) + (3) - (4) + (5) - (6)$ :
Leaving us with (after combining and simplifying) \[\cos{\alpha}=\frac{-11}{2\cdot(DP+EP+FP)}\]
Therefore, we want to solve for $DP+EP+FP$
Notice that $\angle{DPE}=\angle{EPF}=\angle{FPD}=120^\circ$
We can use Law of Cosines again to solve for the sides of $\triangle{DEF}$ , which have side lengths of $13$ , $42$ , and $35$ , and area $120\sqrt{3}$ .
Label the lengths of $PD$ , $PE$ , and $PF$ to be $x$ , $y$ , and $z$ .
Therefore, using the $\sin$ area formula,
\begin{align*} [\triangle{DEF}] &= \frac{1}{2}\cdot\sin{120°}\cdot(xy+yz+zx) = 120\sqrt{3} \\ xy+yz+zx &= 2^5\cdot3\cdot5 \end{align*}
In addition, we know that
\begin{align*} x^2+y^2+xy&=42^2\\ y^2+z^2+yz&=35^2\\ z^2+x^2+zx&=13^2\\ \end{align*}
By using Law of Cosines for $\triangle{DPE}$ , $\triangle{EPF}$ , and $\triangle{FPD}$ respectively
Because we want $DP+EP+FP$ , which is $x+y+z$ , we see that
\begin{align*} (x+y+z)^2 &= \frac{(x^2+y^2+xy)+(y^2+z^2+yz)+(z^2+x^2+zx)+3(zx+xy+yz+zx)}{2} \\ (x+y+z)^2 &= \frac{42^2+35^2+13^2+3\cdot2^5\cdot3\cdot5}{2} \\ (x+y+z)^2 &= 2299 \\ x+y+z &= 11\sqrt{19} \end{align*}
So plugging the results back into the equation before, we get
\begin{align*} \cos{\alpha} &= \frac{-1}{2\sqrt{19}}\\ \sin{\alpha} &= \frac{5\sqrt{3}}{2\sqrt{19}} \end{align*}
Giving us \[\tan^2{\alpha}=\boxed{075}\]
~ Danielzh

## Solution 5 (Combining Solutions 3 and 4)
We begin by using the fact stated in Solution 3 that, for any point in an equilateral triangle, the lengths of the three perpendicular lines dropped to the sides of the triangle add up to the altitude of that triangle. To make things simple, let's assign $\angle AEP = \angle BFP = \angle CDP = \alpha$ . We can label these three perpendiculars as: \[PD\cdot\sin{\alpha} + PE\cdot\sin{\alpha} + PF\cdot\sin{\alpha} = \dfrac{55 \sqrt{3}}{2}\] Simplifying, we get \[PD + PE + PF = \dfrac{55 \sqrt{3}}{2\cdot\sin{\alpha}}\] Now, as stated and quoting Solution 4, "Draw line segments from $P$ to points $A$ , $B$ , and $C$ . [We know that] the angle measure of $\angle{AEP}$ , $\angle{BFP}$ , and $\angle{CDP}$ is $\alpha$
Using Law of Cosines (note that $\cos{\angle{AFP}}=\cos{\angle{BDP}}=\cos{\angle{CEP}}=\cos{180^\circ-\alpha}=-\cos{\alpha}$ )
\begin{align*} (1) \ BP^2 &= FP^2+15^2-2\cdot FP\cdot15\cdot\cos(\alpha)\\ (2) \ BP^2 &= DP^2+7^2+2\cdot DP\cdot7\cdot\cos(\alpha)\\ (3) \ CP^2 &= DP^2+48^2-2\cdot DP\cdot48\cdot\cos(\alpha)\\ (4) \ CP^2 &= EP^2+30^2+2\cdot EP\cdot30\cdot\cos(\alpha)\\ (5) \ AP^2 &= EP^2+25^2-2\cdot EP\cdot25\cdot\cos(\alpha)\\ (6) \ AP^2 &= FP^2+40^2+2\cdot FP\cdot40\cdot\cos(\alpha)\\ \end{align*}
We can perform this operation $(1) - (2) + (3) - (4) + (5) - (6)$ :
Leaving us with (after combining and simplifying) \[PD + PE + PF=\frac{11}{2\cdot\cos{\alpha}}\] ".
Now, we can use our previous equation along with this one to get: \[\frac{11}{2\cdot\cos{\alpha}} = \dfrac{55 \sqrt{3}}{2\cdot\sin{\alpha}}\] .
This equation becomes: \[\tan{\alpha} = 5\sqrt{3}\] As so, our answer is \[\left(5\sqrt3\right)^2=\boxed{075}.\] ~Solution by armang32324 (Mathemagics Club)

## Solution 6
By the law of cosines, \[FE=\sqrt{AF^2+AE^2-2AF\cdot AE\cos\angle FAE}=35.\] Similarly we get $FD=13$ and $DE=42$ . $\angle AEP=\angle BFP=\angle CDP\overset\triangle=\theta$ implies that $AFPE$ , $BDPF$ , and $CDPE$ are three cyclic quadrilaterals, as shown below: [asy] /* Made by MRENTHUSIASM */ size(400); pair A, B, C, D, E, F, P; A = 55*sqrt(3)/3 * dir(90); B = 55*sqrt(3)/3 * dir(210); C = 55*sqrt(3)/3 * dir(330); D = B + 7*dir(0); E = A + 25*dir(C-A); F = A + 40*dir(B-A); P = intersectionpoints(Circle(D,54*sqrt(19)/19),Circle(F,5*sqrt(19)/19))[0]; draw(anglemark(A,E,P,20),red); draw(anglemark(B,F,P,20),red); draw(anglemark(C,D,P,20),red); add(pathticks(anglemark(A,E,P,20), n = 1, r = 0.2, s = 12, red)); add(pathticks(anglemark(B,F,P,20), n = 1, r = 0.2, s = 12, red)); add(pathticks(anglemark(C,D,P,20), n = 1, r = 0.2, s = 12, red)); draw(A--B--C--cycle^^P--E^^P--F^^P--D); draw(P--A^^P--B^^P--C,dashed); draw(circumcircle(A,E,F)^^circumcircle(B,D,F)^^circumcircle(C,D,E),blue); dot("$A$",A,1.5*dir(A),linewidth(4)); dot("$B$",B,1.5*dir(B),linewidth(4)); dot("$C$",C,1.5*dir(C),linewidth(4)); dot("$D$",D,1.5*S,linewidth(4)); dot("$E$",E,1.5*dir(30),linewidth(4)); dot("$F$",F,1.5*dir(150),linewidth(4)); dot("$P$",P,1.5*dir(-30),linewidth(4)); label("$7$",midpoint(B--D),1.5*S,red); label("$30$",midpoint(C--E),1.5*dir(30),red); label("$40$",midpoint(A--F),1.5*dir(150),red); [/asy] Using the law of sines in each, \[\frac{AP}{35}=\frac{AP}{FE}=\frac{CP}{42}=\frac{CP}{ED}=\frac{BP}{13}=\frac{BP}{DF}=\frac{\sin\theta}{\sin\frac\pi3}.\] So we can set $AP=35k$ , $BP=13k$ , and $CP=42k$ . Let $PD=d$ , $PE=e$ , and $PF=f$ . Applying Ptolemy theorem in the cyclic quadrilaterals, \[\begin{cases}AP\cdot FE=AF\cdot PE+AE\cdot PF,\\CP\cdot ED=CE\cdot PD+CD\cdot PE,\\BP\cdot DF=BD\cdot PF+BF\cdot PD.\end{cases} \implies \begin{cases} 1225k=40e+25f,\\1764k=30d+48e,\\169k=15d+7f, \end{cases}\] We can solve out $d=\frac{54k}5$ , $e=30k$ , $f=k$ . By the law of cosines in $\triangle PEF$ , $FE=\sqrt{900k^2+k^2-60k\cdot\left(\frac{-1}2\right)}=\sqrt{931}k$ . The law of sines yield $\frac{\sin\angle AEP}{\sin\angle FAE}=\frac{AP}{FE}=\frac{35k}{\sqrt{931}k}=\frac{35}{\sqrt{931}}$ . Lastly, $\sin\angle AEP=\frac{5\sqrt{57}}{38}$ , then $\tan\angle AEP=5\sqrt3$ . The answer is \[\left(5\sqrt3\right)^2=\boxed{075}.\]

## Solution 7
$P$ is well known to be the Miquel point of triangle $DEF$ . By Law of Cosines, $E F = 35$ , $F D = 13$ , $D E = 42$ . Call $P D$ , $P E$ , $P F$ : $x$ , $y$ , $z$ respectively. Then we obtain that $x^2+xy+y^2 = 42^2$ , $x^2+xz+z^2 = 13^2$ , $y^2+yz+z^2 = 35^2$ . Note that since the area of the triangle by sine area formula is $(xy + xz + yz)\left(\frac{\sqrt{3}}{4}\right)$ , but by Heron's formula, the area of the triangle is $\sqrt{(45)(3)(32)(10)} = (5)(3)(8)\sqrt{3} = 120\sqrt{3}$ . $xy+xz+yz = 480$ , and so we obtain $x+y+z = 11\sqrt{19}$ by adding all the equations together. Now, subtract any two equations from each other to obtain $(y-z)(11\sqrt{19}) = (55)(29)$ , $(x-z)(11\sqrt{19}) = (7)(77)$ , $x-z = \frac{49}{\sqrt{19}}$ , $y-z = \frac{145}{\sqrt{19}}$ , and $z = \frac{5}{\sqrt{19}}$ , $y = \frac{150}{\sqrt{19}}$ , and $x = \sqrt{54}{\sqrt{19}}$ . Now we find PC through Ptolemy's theorem, do Law of Cosines, and we are finished.

## Solution 8 (Coordinates Bash Again!)
Recall that if $\theta$ is the angle between two lines with slopes $m_1, m_2$ , we can write:
$\tan(\theta) = \mid \frac{m_1 - m_2}{1 + m_1 \cdot m_2} \mid$
We will use this fact to solve the problem. Let $B$ be at the origin, $C$ be at $(55, 0)$ and $A$ be at $(\frac{55}{2}, \frac{55\sqrt{3}}{2})$ . Next, we can easily find the equation of line $AB$ as $y = x\sqrt{3}$ and the equation of line $AC$ as $y = -x\sqrt{3} + 55\sqrt{3}$ . We also know that $D$ is at $(7, 0)$ given the problem's conditions. We can now find the coordinates of $E$ and $F$ . To find the coordinates of $F$ , recall that $F$ lies on line segment $AB$ which has equation $y = x\sqrt{3}$ . Hence, $F$ will be a point of the form $(x, x\sqrt{3})$ . We also know the distance between $F$ and $B$ (the origin), is just $55 - 40 = 15$ . So the distance between the point $(x, x\sqrt{3})$ and $(0, 0)$ is just $15$ . We can use the distance formula to get a solution of $x = \frac{15}{2}$ (there will be two solutions but one of them is unfeasible). So the coordinates of $F$ is just $(\frac{15}{2}, \frac{15\sqrt{3}}{2})$ . Similarly, we can find the coordinates of $E$ in a similar way to get $(40, 15\sqrt{3})$ . Note that $\angle BFP = \angle PEA = \angle PDC = \theta$ . Let's focus on $\angle BFP$ . This angle is between lines $BF$ and $FP$ so we just have to compute the slopes of these lines. Let $P$ be at point $(a, b)$ . Then, the slope of $BF$ is just $\sqrt{3}$ and the slope of $FP$ is just $\frac{2b - 15\sqrt{3}}{2a - 15}$ . Because the angle between these two lines is $\theta$ , we can use our above lemma to get the equation:
$\tan(\theta) = \mid \frac{\sqrt{3} - \frac{2b - 15\sqrt{3}}{2a - 15}}{1 + \sqrt{3} \cdot \frac{2b - 15\sqrt{3}}{2a - 15}} \mid$
We can similarly use the other angles and lines to come up with two more of these type of equations:
$\tan(\theta) = \mid \frac{-\sqrt{3} - \frac{15\sqrt{3} - b}{40 - a}}{1 - \sqrt{3} \cdot \frac{15\sqrt{3} - b}{40 - a}} \mid$
$\tan(\theta) = \mid \frac{b}{7 - a} \mid$
We have $3$ equations with $3$ variables and since we are trying to find $\tan(\theta)^{2}$ , we can treat $\tan(\theta)$ as a variable. We solve to get $\tan(\theta) = 5\sqrt{3}$ and therefore our answer is just $\boxed{075}$ .
$\textbf{Note: How to solve the system of equations}$
The first step is to realize that we need to make the inputs nicer. So we clear the fractions and set them equal. Doing so, we have:
$\frac{a\sqrt{3} - b}{a + b\sqrt{3} - 30} = \frac{a\sqrt{3} + b - 55\sqrt{3}}{-a + b\sqrt{3} - 5} = \frac{b}{7 - a}$ .
Now we can write:
$\frac{a\sqrt{3} - b}{a + b\sqrt{3} - 30} = \frac{b}{7 - a}$
$\frac{a\sqrt{3} + b - 55\sqrt{3}}{-a + b\sqrt{3} - 5} = \frac{b}{7 - a}$
Here, we're going to change $a$ to $x$ and $b$ to $y$ just to make the solving more traditional. We can cross multiply the first equation and simplify to get
$7x\sqrt{3} - x^{2} \sqrt{3} = y^{2} \sqrt{3} - 23y$
Next, we cross multiply the second equation to get:
$7x\sqrt{3} - x^{2} \sqrt{3} + 7y - xy - 385\sqrt{3} + 55x\sqrt{3} = -xy + y^{2} \sqrt{3} - 5y$
Notice we could make some substitutions from our first equation to the second equation:
$y^{2} \sqrt{3} - 23y + 7y - 385\sqrt{3} + 55x\sqrt{3} = y^{2} \sqrt{3} - 5y$
We simplify this to get:
$-16y - 385\sqrt{3} + 55x\sqrt{3} = -5y$
This means:
$55x\sqrt{3} - 385\sqrt{3} = 11y$
Which yields:
$y = 5\sqrt{3}(x - 7)$
Now, we plug this representation into the equation $7x\sqrt{3} - x^{2} \sqrt{3} = y^{2} \sqrt{3} - 23y$ we got earlier to get:
$7x\sqrt{3} - x^{2} \sqrt{3} = 75\sqrt{3} (x - 7)^{2} - 115x\sqrt{3} + 805\sqrt{3}$
We can expand and simplify to get:
$122x\sqrt{3} - x^{2} \sqrt{3} = 75x^{2} \sqrt{3} - 1050x\sqrt{3} + 4480\sqrt{3}$
Simplifying, we get:
$76x^{2} \sqrt{3} - 1172x\sqrt{3} + 4480\sqrt{3} = 0$
This yields:
$19x^{2} - 293x + 1120 = 0$
Now this is trivial to solve:
$x = \frac{293 \pm \sqrt{293^{2} - 76\cdot1120}}{38}$
To find $293^{2}$ really quickly under contest conditions, we can do:
$293^{2} = (200 + 93)^{2} = 200^{2} + 400\cdot93 + (90 + 3)^{2} = 40000 + 37200 + 8100 + 549 = 85849$
Now back to simplifying $x$ :
The discriminant nicely simplifies to $85849 - 85120 = 729 = 27^{2}$
So we have $x = \frac{293 + 27}{38} = \frac{320}{38} = \frac{160}{19}$ . (Note that if we take the negative version of the solution, we would have $x = \frac{266}{38} = 7$ but this would yield $y = 5\sqrt{3} \cdot 7 - 35\sqrt{3} = 0$ which is absurd)
And now we're basically done. Recall that $y = 5x\sqrt{3} - 35\sqrt{3} = \frac{5\sqrt{3}\cdot160}{19} - \frac{35\sqrt{3}\cdot19}{19} = \frac{135\sqrt{3}}{19}$ . Now recall that we let $a = x$ and $b = y$ so we now have $a = \frac{160}{19}$ and $b = \frac{135\sqrt{3}}{19}$ .
Now, recall that $\tan(\theta) = \mid \frac{b}{7 - a} \mid = \mid \frac{\frac{135\sqrt{3}}{19}}{7 - \frac{160}{19}} \mid = \mid \frac{\frac{135\sqrt{3}}{19}}{\frac{133 - 160}{19}} \mid = \mid \frac{135\sqrt{3}}{-27} \mid = \mid -5\sqrt{3} \mid = 5\sqrt{3}$ as desired.
~ilikemath247365

## Video Solution
https://www.youtube.com/watch?v=EdwM8GpY_yc
~MathProblemSolvingSkills.com

## Animated Video Solution
https://youtu.be/5d98iXeyu4E
~Star League ( https://starleague.us )

## Video Solution by MOP 2024
https://youtu.be/BYR3DollZeA
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .