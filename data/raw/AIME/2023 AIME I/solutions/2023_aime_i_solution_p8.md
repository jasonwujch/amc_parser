# 2023 AIME I Problem 8

## Problem

Rhombus $ABCD$ has $\angle BAD < 90^\circ.$ There is a point $P$ on the incircle of the rhombus such that the distances from $P$ to the lines $DA,AB,$ and $BC$ are $9,$ $5,$ and $16,$ respectively. Find the perimeter of $ABCD.$

### Diagram

[asy] /* Made by MRENTHUSIASM; inspired by Math Jams. */ size(300); pair A, B, C, D, O, P, R, S, T; A = origin; B = (125/4,0); C = B + 125/4 * dir((3,4)); D = A + 125/4 * dir((3,4)); O = (25,25/2); P = (15,5); R = foot(P,A,D); S = foot(P,A,B); T = foot(P,B,C); markscalefactor=0.15; draw(rightanglemark(P,R,D)^^rightanglemark(P,S,B)^^rightanglemark(P,T,C),red); draw(Circle(O,25/2)^^A--B--C--D--cycle^^B--T); draw(P--R^^P--S^^P--T,red+dashed); dot("$A$",A,1.5*dir(225),linewidth(4.5)); dot("$B$",B,1.5*dir(-45),linewidth(4.5)); dot("$C$",C,1.5*dir(45),linewidth(4.5)); dot("$D$",D,1.5*dir(135),linewidth(4.5)); dot("$P$",P,1.5*dir(60),linewidth(4.5)); dot(R^^S^^T,linewidth(4.5)); dot(O,linewidth(4.5)); label("$9$",midpoint(P--R),dir(A-D),red); label("$5$",midpoint(P--S),dir(180),red); label("$16$",midpoint(P--T),dir(A-D),red); [/asy] ~MRENTHUSIASM

## Solution 1
This solution refers to the Diagram section.
Let $O$ be the incenter of $ABCD$ for which $\odot O$ is tangent to $\overline{DA},\overline{AB},$ and $\overline{BC}$ at $X,Y,$ and $Z,$ respectively. Moreover, suppose that $R,S,$ and $T$ are the feet of the perpendiculars from $P$ to $\overleftrightarrow{DA},\overleftrightarrow{AB},$ and $\overleftrightarrow{BC},$ respectively, such that $\overline{RT}$ intersects $\odot O$ at $P$ and $Q.$
We obtain the following diagram: [asy] /* Made by MRENTHUSIASM; inspired by Math Jams. */ size(300); pair A, B, C, D, O, P, R, S, T, X, Y, Z, Q; A = origin; B = (125/4,0); C = B + 125/4 * dir((3,4)); D = A + 125/4 * dir((3,4)); O = (25,25/2); P = (15,5); R = foot(P,A,D); S = foot(P,A,B); T = foot(P,B,C); X = (15,20); Y = (25,0); Z = (35,5); Q = intersectionpoints(Circle(O,25/2),R--T)[1]; fill(R--T--Z--X--cycle,cyan); markscalefactor=0.15; draw(rightanglemark(P,R,D)^^rightanglemark(P,S,B)^^rightanglemark(P,T,C),red); draw(Circle(O,25/2)^^A--B--C--D--cycle^^B--T); draw(P--R^^P--S^^P--T,red+dashed); draw(O--X^^O--Y^^O--Z); dot("$A$",A,1.5*dir(225),linewidth(4.5)); dot("$B$",B,1.5*dir(-45),linewidth(4.5)); dot("$C$",C,1.5*dir(45),linewidth(4.5)); dot("$D$",D,1.5*dir(135),linewidth(4.5)); dot("$P$",P,1.5*dir(60),linewidth(4.5)); dot("$R$",R,1.5*dir(135),linewidth(4.5)); dot("$S$",S,1.5*dir(-90),linewidth(4.5)); dot("$T$",T,1.5*dir(-45),linewidth(4.5)); dot("$O$",O,1.5*dir(45),linewidth(4.5)); dot("$X$",X,1.5*dir(135),linewidth(4.5)); dot("$Y$",Y,1.5*dir(-90),linewidth(4.5)); dot("$Z$",Z,1.5*dir(-45),linewidth(4.5)); dot("$Q$",Q,1.5*dir(60),linewidth(4.5)); label("$9$",midpoint(P--R),dir(A-D),red); label("$5$",midpoint(P--S),dir(180),red); label("$16$",midpoint(P--T),dir(A-D),red); [/asy] Note that $\angle RXZ = \angle TZX = 90^\circ$ by the properties of tangents, so $RTZX$ is a rectangle. It follows that the diameter of $\odot O$ is $XZ = RT = 25.$
Let $x=PQ$ and $y=RX=TZ.$ We apply the Power of a Point Theorem to $R$ and $T:$ \begin{align*} y^2 &= 9(9+x), \\ y^2 &= 16(16-x). \end{align*} We solve this system of equations to get $x=7$ and $y=12.$ Alternatively, we can find these results by the symmetry on rectangle $RTZX$ and semicircle $\widehat{XPZ}.$
We extend $\overline{SP}$ beyond $P$ to intersect $\odot O$ and $\overleftrightarrow{CD}$ at $E$ and $F,$ respectively, where $E\neq P.$ So, we have $EF=SP=5$ and $PE=25-SP-EF=15.$ On the other hand, we have $PX=15$ by the Pythagorean Theorem on right $\triangle PRX.$ Together, we conclude that $E=X.$ Therefore, points $S,P,$ and $X$ must be collinear.
Let $G$ be the foot of the perpendicular from $D$ to $\overline{AB}.$ Note that $\overline{DG}\parallel\overline{XP},$ as shown below: [asy] /* Made by MRENTHUSIASM; inspired by Math Jams. */ size(300); pair A, B, C, D, O, P, R, S, T, X, Y, Z, Q, G; A = origin; B = (125/4,0); C = B + 125/4 * dir((3,4)); D = A + 125/4 * dir((3,4)); O = (25,25/2); P = (15,5); R = foot(P,A,D); S = foot(P,A,B); T = foot(P,B,C); X = (15,20); Y = (25,0); Z = (35,5); Q = intersectionpoints(Circle(O,25/2),R--T)[1]; G = foot(D,A,B); fill(D--A--G--cycle,green); fill(P--R--X--cycle,yellow); markscalefactor=0.15; draw(rightanglemark(P,R,D)^^rightanglemark(D,G,A),red); draw(Circle(O,25/2)^^A--B--C--D--cycle^^X--P^^D--G); draw(P--R,red+dashed); dot("$A$",A,1.5*dir(225),linewidth(4.5)); dot("$B$",B,1.5*dir(-45),linewidth(4.5)); dot("$C$",C,1.5*dir(45),linewidth(4.5)); dot("$D$",D,1.5*dir(135),linewidth(4.5)); dot("$P$",P,1.5*dir(60),linewidth(4.5)); dot("$R$",R,1.5*dir(135),linewidth(4.5)); dot("$O$",O,1.5*dir(45),linewidth(4.5)); dot("$X$",X,1.5*dir(135),linewidth(4.5)); dot("$G$",G,1.5*dir(-90),linewidth(4.5)); draw(P--X,MidArrow(0.3cm,Fill(red))); draw(G--D,MidArrow(0.3cm,Fill(red))); label("$9$",midpoint(P--R),dir(A-D),red); label("$12$",midpoint(R--X),dir(135),red); label("$15$",midpoint(X--P),dir(0),red); label("$25$",midpoint(G--D),dir(0),red); [/asy] As $\angle PRX = \angle AGD = 90^\circ$ and $\angle PXR = \angle ADG,$ we conclude that $\triangle PRX \sim \triangle AGD$ by the AA Similarity. The ratio of similitude is \[\frac{PX}{AD} = \frac{RX}{GD}.\] We get $\frac{15}{AD} = \frac{12}{25},$ from which $AD = \frac{125}{4}.$
Finally, the perimeter of $ABCD$ is $4AD = \boxed{125}.$
~MRENTHUSIASM (inspired by awesomeming327. and WestSuburb)

## Solution 2
Let $G$ be the extension of line $CD$ such that $CG \perp FG,$ $E$ be the point where $AB$ is tangent to the circle, $H$ be where the perpendicular from $F$ to line $GC$ meets the circle after point $P$ , and $I$ be the point where $PH$ meets $AD$ (point $I$ is added to make it clear that $H$ is not on $AD$ ).
Connect $H$ to the point where the circle is tangent to $CD$ , call this point $K.$ Since $EK$ is a diameter, $PH$ is a chord, and $EK \parallel PH$ (they are parallel because $EFGK$ is a rectangle), the perpendicular bisector of $PH$ will also perpendicularly bisect $EK.$ So trapezoid $PHKE$ is symmetrical about this perpendicular bisector and is therefore isosceles. Then $PE = HK.$ So by Hypotenuse-Leg congruence $\triangle EFP \cong \triangle KGH.$ Then $HG = FP = 9$ and since the length of $FG$ is $25,$ $PH = 7.$ Now, consider the right triangle formed by the radius, height, and half of the top base of the isosceles trapezoid. Let $h$ be the height. We have $h^2 + (7/2)^2 = (25/2)^2 \implies h = FE = 12.$ Then by the Pythagorean Theorem on $\triangle EFP$ , $EP = 15.$
We observe that $\angle FPE \cong \angle EAJ$ since right triangles $EFP$ and $EJA$ share common angle $E.$
Therefore, $\sin(\angle FPE) = \frac{12}{15} = \frac{4}{5} = \sin(\angle EAJ)$ .
The height of the rhombus is $25$ since the diameter of the circle is $25$ . If $s$ is the side length of the rhombus, $h$ is the height, and $\theta$ is an interior angle, then $\sin(\theta) = \frac{h}{s}$ (you can see this by dropping an altitude from $B$ to $AD$ ).
Given $\sin(\theta) = \frac{4}{5}$ , we have $\frac{25}{s} = \frac{4}{5}$ .
Solving, we find $s = \frac{125}{4}$ .
So the perimeter of the rhombus is $4s = 4 \cdot \frac{125}{4} = \boxed{125}$ .
~ grogg007

## Solution 3
This solution refers to the Diagram section.
Define points $O,R,S,$ and $T$ as Solution 1 does. Moreover, let $H$ be the foot of the perpendicular from $P$ to $\overleftrightarrow{CD},$ $M$ be the foot of the perpendicular from $O$ to $\overleftrightarrow{HS},$ and $N$ be the foot of the perpendicular from $O$ to $\overleftrightarrow{RT}.$
We obtain the following diagram: [asy] /* Made by MRENTHUSIASM; inspired by Math Jams. */ size(300); pair A, B, C, D, O, P, R, S, T, H, M, N; A = origin; B = (125/4,0); C = B + 125/4 * dir((3,4)); D = A + 125/4 * dir((3,4)); O = (25,25/2); P = (15,5); R = foot(P,A,D); S = foot(P,A,B); T = foot(P,B,C); H = foot(S,C,D); M = foot(O,S,H); N = foot(O,R,T); fill(O--M--P--cycle,yellow); fill(O--N--P--cycle,green); markscalefactor=0.15; draw(rightanglemark(P,R,D)^^rightanglemark(P,S,B)^^rightanglemark(P,T,C)^^rightanglemark(O,M,P)^^rightanglemark(O,N,P)^^rightanglemark(S,H,D),red); draw(Circle(O,25/2)^^A--B--C--D--cycle^^B--T^^D--H^^O--M^^O--N^^O--P); draw(P--R^^P--S^^P--T^^P--H,red+dashed); dot("$A$",A,1.5*dir(225),linewidth(4.5)); dot("$B$",B,1.5*dir(-45),linewidth(4.5)); dot("$C$",C,1.5*dir(45),linewidth(4.5)); dot("$D$",D,1.5*dir(90),linewidth(4.5)); dot("$P$",P,1.5*dir(60),linewidth(4.5)); dot("$R$",R,1.5*dir(135),linewidth(4.5)); dot("$S$",S,1.5*dir(-90),linewidth(4.5)); dot("$T$",T,1.5*dir(-45),linewidth(4.5)); dot("$O$",O,1.5*dir(45),linewidth(4.5)); dot("$H$",H,1.5*dir(90),linewidth(4.5)); dot("$M$",M,1.5*dir(180),linewidth(4.5)); dot("$N$",N,1.5*dir(15),linewidth(4.5)); label("$9$",midpoint(P--R),dir(A-D),red); label("$5$",midpoint(P--S),dir(180),red); label("$16$",midpoint(P--T),dir(A-D),red); [/asy] Note that the diameter of $\odot O$ is $HS=RT=25,$ so $OP=\frac{25}{2}.$ It follows that:
1. In right $\triangle OMP,$ we have $MP=\frac{HS}{2}-PS=\frac{15}{2}$ by symmetry, from which $OM=10$ by the Pythagorean Theorem.
1. In right $\triangle ONP,$ we have $NP=\frac{RT}{2}-RP=\frac{7}{2}$ by symmetry, from which $ON=12$ by the Pythagorean Theorem.
Since $\overline{MO}\parallel\overline{AB}$ and $\overline{ON}\parallel\overline{DA},$ we conclude that $\angle A = \angle MON.$ We apply the Sine of a Sum Formula: \begin{align*} \sin\angle A &= \sin\angle MON \\ &= \sin(\angle MOP + \angle PON) \\ &= \sin\angle MOP \cos\angle PON + \cos\angle MOP \sin\angle PON \\ &= \frac{3}{5}\cdot\frac{24}{25} + \frac{4}{5}\cdot\frac{7}{25} \\ &= \frac{4}{5}. \end{align*} Note that \[\sin\angle A = \frac{HS}{DA},\] from which $\frac{4}{5} = \frac{25}{DA}.$ We solve this equation to get $DA=\frac{125}{4}.$
Finally, the perimeter of $ABCD$ is $4DA = \boxed{125}.$
~MRENTHUSIASM (credit given to TheAMCHub)

## Solution 4
Label the points of the rhombus to be $X$ , $Y$ , $Z$ , and $W$ and the center of the incircle to be $O$ so that $9$ , $5$ , and $16$ are the distances from point $P$ to side $ZW$ , side $WX$ , and $XY$ respectively. Through this, we know that the distance from the two pairs of opposite lines of rhombus $XYZW$ is $25$ and circle $O$ has radius $\frac{25}{2}$ .
Call the feet of the altitudes from $P$ to side $ZW$ , side $WX$ , and side $XY$ to be $A$ , $B$ , and $C$ respectively. Additionally, call the feet of the altitudes from $O$ to side $ZW$ , side $WX$ , and side $XY$ to be $D$ , $E$ , and $F$ respectively.
Draw a line segment from $P$ to $\overline{OD}$ so that it is perpendicular to $\overline{OD}$ . Notice that this segment length is equal to $AD$ and is $\sqrt{\left(\frac{25}{2}\right)^2-\left(\frac{7}{2}\right)^2}=12$ by Pythagorean Theorem.
Similarly, perform the same operations with perpendicular from $P$ to $\overline{OE}$ to get $BE=10$ .
By equal tangents, $WD=WE$ . Now, label the length of segment $WA=n$ and $WB=n+2$ .
Using Pythagorean Theorem again, we get
\begin{align*} WA^2+PA^2&=WB^2+PB^2 \\ n^2+9^2&=(n+2)^2+5^2 \\ n&=13. \end{align*}
Which also gives us $\tan{\angle{OWX}}=\frac{1}{2}$ and $OW=\frac{25\sqrt{5}}{2}$ .
Since the diagonals of the rhombus intersect at $O$ and are angle bisectors and are also perpendicular to each other, we can get that
\begin{align*} \frac{OX}{OW}&=\tan{\angle{OWX}} \\ OX&=\frac{25\sqrt{5}}{4} \\ WX^2&=OW^2+OX^2 \\ WX&=\frac{125}{4} \\ 4WX&=\boxed{125}. \end{align*}
~ Danielzh

## Solution 5
Denote by $O$ the center of $ABCD$ . We drop an altitude from $O$ to $AB$ that meets $AB$ at point $H$ . We drop altitudes from $P$ to $AB$ and $AD$ that meet $AB$ and $AD$ at $E$ and $F$ , respectively. We denote $\theta = \angle BAC$ . We denote the side length of $ABCD$ as $d$ .
Because the distances from $P$ to $BC$ and $AD$ are $16$ and $9$ , respectively, and $BC \parallel AD$ , the distance between each pair of two parallel sides of $ABCD$ is $16 + 9 = 25$ . Thus, $OH = \frac{25}{2}$ and $d \sin \theta = 25$ .
We have \begin{align*} \angle BOH & = 90^\circ - \angle HBO \\ & = 90^\circ - \angle HBD \\ & = 90^\circ - \frac{180^\circ - \angle C}{2} \\ & = 90^\circ - \frac{180^\circ - \theta}{2} \\ & = \frac{\theta}{2} . \end{align*}
Thus, $BH = OH \tan \angle BOH = \frac{25}{2} \tan \frac{\theta}{2}$ .
In $FAEP$ , we have $\overrightarrow{FA} + \overrightarrow{AE} + \overrightarrow{EP} + \overrightarrow{PF} = 0$ . Thus, \[ AF + AE e^{i \left( \pi - \theta \right)} + EP e^{i \left( \frac{3 \pi}{2} - \theta \right)} - PF i . \]
Taking the imaginary part of this equation and plugging $EP = 5$ and $PF = 9$ into this equation, we get \[ AE = \frac{9 + 5 \cos \theta}{\sin \theta} . \]
We have \begin{align*} OP^2 & = \left( OH - EP \right)^2 + \left( AH - AE \right)^2 \\ & = \left( \frac{25}{2} - 5 \right)^2 + \left( d - \frac{25}{2} \tan \frac{\theta}{2} - \frac{9 + 5 \cos \theta}{\sin \theta} \right) \\ & = \left( \frac{15}{2} \right)^2 + \left( \frac{25}{\sin \theta} - \frac{25}{2} \tan \frac{\theta}{2} - \frac{9 + 5 \cos \theta}{\sin \theta} \right) . \hspace{1cm} (\bigstar) \end{align*}
Because $P$ is on the incircle of $ABCD$ , $OP = \frac{25}{2}$ . Plugging this into $(\bigstar)$ , we get the following equation \[ 20 \sin \theta - 15 \cos \theta = 7 . \]
By solving this equation, we get $\sin \theta = \frac{4}{5}$ and $\cos \theta = \frac{3}{5}$ . Therefore, $d = \frac{25}{\sin \theta} = \frac{125}{4}$ .
Therefore, the perimeter of $ABCD$ is $4d = \boxed{125}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 6
The center of the incircle is $O.$ Denote the points in which the incircle meets $\overline{AB},$ $\overline{BC},$ $\overline{CD},$ and $\overline{DA}$ as $W,$ $X,$ $Y,$ and $Z,$ respectively. Next, also denote the base of the perpendicular from $P$ to $\overline{AB},$ $\overline{AD},$ $\overline{OW},$ and $\overline{OZ}$ as $M,$ $N,$ $S,$ and $T,$ respectively.
We can easily see that the radius of the circle is $\frac{25}{2}.$ Using this and Pythagorus on right $\triangle OSP$ and $\triangle OTP,$ we find that $MW = PS = 10$ and $NZ = PT = 12.$
Since $AW = AZ$ by properties of circle tangents, we can deduce by the above information that $AM = AN+2.$ Doing Pythagorus on right $\triangle AMP$ and $\triangle ANP$ we find that $a^2 = b^2 + 56$ (because $a^2+25=b^2+81.$ ) From solving the $2$ just derived equations, we find that $AM=15$ and $AN=13.$
Next, we use Pythagorus on right $\triangle AOB$ (we can see it's right because of properties of rhombuses.) We get \[AB^2 = AO^2 + BO^2.\] We know $AB = AW + WB = 25 + WB.$ By Pythagorus on $\triangle AWO$ and $\triangle BWO,$ we also know $AO^2 = 25^2+\left(\frac{25}{2}\right)^2$ and $BO^2=WB^2+\left(\frac{25}{2}\right)^2.$ Substituting these in, we have \[25^2 + 50WB + WB^2 = 25^2+\left(\frac{25}{2}\right)^2+\left(\frac{25}{2}\right)^2+WB^2.\] Solving for $WB,$ we get $WB = \frac{25}{4}.$ Now we find that each side of the rhombus $=AB=25+\frac{25}{4}=\frac{125}{4}.$ The perimeter of the rhombus would be that times $4.$ Our final answer is \[\frac{125}{4}\cdot4=\boxed{125}.\]
~s214425

## Solution 7
Notation is shown on diagram, $RT \perp AD, FG \perp AB, E = AD \cap \omega, E' = FG \cap AD.$ $RT = 9 + 16 = 25 = FG$ as hights of rhombus. \[RP = QT = 9, PQ = 16 - 9 = 7, GE' = PF = 5,\] \[PE' = 25 - 5 - 5 = 15, RE = \sqrt{RP \cdot RQ} = \sqrt{9 \cdot 16} = 12.\] \[PE = \sqrt{RP^2 + RE^2} = 15 \implies E = E'.\] \[\sin \alpha = \frac {RE}{PE} = \frac {GF}{AD} \implies AD = \frac {15 \cdot 25}{12} = \frac {125}{4}.\] The perimeter of $ABCD$ is $\frac{125}{4}\cdot4=\boxed{125}.$
vladimir.shelomovskii@gmail.com, vvsss

## Video Solution
https://youtu.be/AYH6zdJqZLM
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .