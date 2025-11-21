# 2022 AIME I Problem 11

## Problem

Let $ABCD$ be a parallelogram with $\angle BAD < 90^\circ.$ A circle tangent to sides $\overline{DA},$ $\overline{AB},$ and $\overline{BC}$ intersects diagonal $\overline{AC}$ at points $P$ and $Q$ with $AP < AQ,$ as shown. Suppose that $AP=3,$ $PQ=9,$ and $QC=16.$ Then the area of $ABCD$ can be expressed in the form $m\sqrt{n},$ where $m$ and $n$ are positive integers, and $n$ is not divisible by the square of any prime. Find $m+n.$

[asy] defaultpen(linewidth(0.6)+fontsize(11)); size(8cm); pair A,B,C,D,P,Q; A=(0,0); label("$A$", A, SW); B=(6,15); label("$B$", B, NW); C=(30,15); label("$C$", C, NE); D=(24,0); label("$D$", D, SE); P=(5.2,2.6); label("$P$", (5.8,2.6), N); Q=(18.3,9.1); label("$Q$", (18.1,9.7), W); draw(A--B--C--D--cycle); draw(C--A); draw(Circle((10.95,7.45), 7.45)); dot(A^^B^^C^^D^^P^^Q); [/asy]

## Solution 1 (No trig)
Let's redraw the diagram, but extend some helpful lines.
[asy] size(10cm); pair A,B,C,D,EE,F,P,Q,O; A=(0,0); EE = (24,15); F = (30,0); O = (10.5,7.5); label("$A$", A, SW); B=(6,15); label("$B$", B, NW); C=(30,15); label("$C$", C, NE); D=(24,0); label("$D$", D, SE); P=(5.2,2.6); label("$P$", (5.8,2.6), N); Q=(18.3,9.1); label("$Q$", (18.1,9.7), W); draw(A--B--C--D--cycle); draw(C--A); draw(Circle((10.95,7.45), 7.45)); dot(A^^B^^C^^D^^P^^Q); dot(O); label("$O$",O,W); draw((10.5,15)--(10.5,0)); draw(D--(24,15),dashed); draw(C--(30,0),dashed); draw(D--(30,0)); dot(EE); dot(F); label("$3$", midpoint(A--P), S); label("$9$", midpoint(P--Q), S); label("$16$", midpoint(Q--C), S); label("$x$", (5.5,13.75), W); label("$20$", (20.25,15), N); label("$6$", (5.25,0), S); label("$6$", (1.5,3.75), W); label("$x$", (8.25,15),N); label("$14+x$", (17.25,0), S); label("$6-x$", (27,15), N); label("$6+x$", (27,7.5), S); label("$6\sqrt{3}$", (30,7.5), E); label("$T_1$", (10.5,15), N); label("$T_2$", (10.5,0), S); label("$T_3$", (4.5,11.25), W); label("$E$", EE, N); label("$F$", F, S); [/asy]
We obviously see that we must use power of a point since they've given us lengths in a circle and there are intersection points. Let $T_1, T_2, T_3$ be our tangents from the circle to the parallelogram. By the secant power of a point, the power of $A = 3 \cdot (3+9) = 36$ . Then $AT_2 = AT_3 = \sqrt{36} = 6$ . Similarly, the power of $C = 16 \cdot (16+9) = 400$ and $CT_1 = \sqrt{400} = 20$ . We let $BT_3 = BT_1 = x$ and label the diagram accordingly.
Notice that because $BC = AD, 20+x = 6+DT_2 \implies DT_2 = 14+x$ . Let $O$ be the center of the circle. Since $OT_1$ and $OT_2$ intersect $BC$ and $AD$ , respectively, at right angles, we have $T_2T_1CD$ is a right-angled trapezoid and more importantly, the diameter of the circle is the height of the triangle. Therefore, we can drop an altitude from $D$ to $BC$ and $C$ to $AD$ , and both are equal to $2r$ . Since $T_1E = T_2D$ , $20 - CE = 14+x \implies CE = 6-x$ . Since $CE = DF, DF = 6-x$ and $AF = 6+14+x+6-x = 26$ . We can now use Pythagorean theorem on $\triangle ACF$ ; we have $26^2 + (2r)^2 = (3+9+16)^2 \implies 4r^2 = 784-676 \implies 4r^2 = 108 \implies 2r = 6\sqrt{3}$ and $r^2 = 27$ .
We know that $CD = 6+x$ because $ABCD$ is a parallelogram. Using Pythagorean theorem on $\triangle CDF$ , $(6+x)^2 = (6-x)^2 + 108 \implies (6+x)^2-(6-x)^2 = 108 \implies 12 \cdot 2x = 108 \implies 2x = 9 \implies x = \frac{9}{2}$ . Therefore, base $BC = 20 + \frac{9}{2} = \frac{49}{2}$ . Thus the area of the parallelogram is the base times the height, which is $\frac{49}{2} \cdot 6\sqrt{3} = 147\sqrt{3}$ and the answer is $\boxed{150}$
~KingRavi

## Solution 2
Let the circle tangent to $BC,AD,AB$ at $P,Q,M$ separately, denote that $\angle{ABC}=\angle{D}=\alpha$
Using POP, it is very clear that $PC=20,AQ=AM=6$ , let $BM=BP=x,QD=14+x$ , using LOC in $\triangle{ABP}$ , $x^2+(x+6)^2-2x(x+6)\cos\alpha=36+PQ^2$ , similarly, use LOC in $\triangle{DQC}$ , getting that $(14+x)^2+(6+x)^2-2(6+x)(14+x)\cos\alpha=400+PQ^2$ . We use the second equation to minus the first equation, getting that $28x+196-(2x+12)\times14\times\cos\alpha=364$ , we can get $\cos\alpha=\frac{2x-12}{2x+12}$ .
Now applying LOC in $\triangle{ADC}$ , getting $(6+x)^2+(20+x)^2-2(6+x)\times(20+x)\times\frac{2x-12}{2x+12}=(3+9+16)^2$ , solving this equation to get $x=\frac{9}{2}$ , then $\cos\alpha=-\frac{1}{7}$ , $\sin\alpha=\frac{4\sqrt{3}}{7}$ , the area is $\frac{21}{2}\cdot\frac{49}{2}\cdot\frac{4\sqrt{3}}{7}=147\sqrt{3}$ leads to $\boxed{150}$
~bluesoul,HarveyZhang

## Solution 3
Denote by $O$ the center of the circle. Denote by $r$ the radius of the circle. Denote by $E$ , $F$ , $G$ the points that the circle meets $AB$ , $CD$ , $AD$ at, respectively.
Because the circle is tangent to $AD$ , $CB$ , $AB$ , $OE = OF = OG = r$ , $OE \perp AD$ , $OF \perp CB$ , $OG \perp AB$ .
Because $AD \parallel CB$ , $E$ , $O$ , $F$ are collinear.
Following from the power of a point, $AG^2 = AE^2 = AP \cdot AQ$ . Hence, $AG = AE = 6$ .
Following from the power of a point, $CF^2 = CQ \cdot CP$ . Hence, $CF = 20$ .
Denote $BG = x$ . Because $DG$ and $DF$ are tangents to the circle, $BF = x$ .
Because $AEFB$ is a right trapezoid, $AB^2 = EF^2 + \left( AE - BF \right)^2$ . Hence, $\left( 6 + x \right)^2 = 4 r^2 + \left( 6 - x \right)^2$ . This can be simplified as \[ 6 x = r^2 . \hspace{1cm} (1) \]
In $\triangle ACB$ , by applying the law of cosines, we have \begin{align*} AC^2 & = AB^2 + CB^2 - 2 AB \cdot CB \cos B \\ & = AB^2 + CB^2 + 2 AB \cdot CB \cos A \\ & = AB^2 + CB^2 + 2 AB \cdot CB \cdot \frac{AE - BF}{AB} \\ & = AB^2 + CB^2 + 2 CB \left( AE - BF \right) \\ & = \left( 6 + x \right)^2 + \left( 20 + x \right)^2 + 2 \left( 20 + x \right) \left( 6 - x \right) \\ & = 24 x + 676 . \end{align*}
Because $AC = AP + PQ + QC = 28$ , we get $x = \frac{9}{2}$ . Plugging this into Equation (1), we get $r = 3 \sqrt{3}$ .
Therefore, \begin{align*} {\rm Area} \ ABCD & = CB \cdot EF \\ & = \left( 20 + x \right) \cdot 2r \\ & = 147 \sqrt{3} . \end{align*}
Therefore, the answer is $147 + 3 = \boxed{\textbf{(150) }}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 4
Let $\omega$ be the circle, let $r$ be the radius of $\omega$ , and let the points at which $\omega$ is tangent to $AB$ , $BC$ , and $AD$ be $X$ , $Y$ , and $Z$ , respectively. Note that PoP on $A$ and $C$ with respect to $\omega$ yields $AX=6$ and $CY=20$ . We can compute the area of $ABC$ in two ways:
1. By the half-base-height formula, $[ABC]=r(20+BX)$ .
2. We can drop altitudes from the center $O$ of $\omega$ to $AB$ , $BC$ , and $AC$ , which have lengths $r$ , $r$ , and $\sqrt{r^2-\frac{81}{4}}$ . Thus, $[ABC]=[OAB]+[OBC]+[OAC]=r(BX+13)+14\sqrt{r^2-\frac{81}{4}}$ .
Equating the two expressions for $[ABC]$ and solving for $r$ yields $r=3\sqrt{3}$ .
Let $BX=BY=a$ . By the Parallelogram Law, $(a+6)^2+(a+20)^2=38^2$ . Solving for $a$ yields $a=9/2$ . Thus, $[ABCD]=2[ABC]=2r(20+a)=147\sqrt{3}$ , for a final answer of $\boxed{150}$ .
~ Leo.Euler

## Solution 5
Let $\omega$ be the circle, let $r$ be the radius of $\omega$ , and let the points at which $\omega$ is tangent to $AB$ , $BC$ , and $AD$ be $H$ , $K$ , and $T$ , respectively. PoP on $A$ and $C$ with respect to $\omega$ yields \[AT=6, CK=20.\]
Let $TG = AC, CG||AT.$
In $\triangle KGT$ $KT \perp BC,$ $KT = \sqrt{GT^2 – (KC + AT)^2} = 6 \sqrt{3}=2r.$
$\angle AOB = 90^{\circ}, OH \perp AB, OH = r = \frac{KT}{2},$ \[OH^2 = AH \cdot BH \implies BH = \frac {9}{2}.\]
Area is \[(BK + KC) \cdot KT = (BH + KC) \cdot 2r = \frac{49}{2} \cdot 6\sqrt{3} = 147 \sqrt{3} \implies 147+3 = \boxed{\textbf{150}}.\]
vladimir.shelomovskii@gmail.com, vvsss

## Solution 6 (Short and Sweet)
Let $O$ be the center of the circle. Let points $M, N$ and $L$ be the tangent points of lines $BC, AD$ and $AB$ respectively to the circle. By Power of a Point, $({MC})^2=16\cdot{25} \Longrightarrow MC=20$ . Similarly, $({AL})^2=3\cdot{12} \Longrightarrow AL=6$ . Notice that $AL=AN=6$ since quadrilateral $LONA$ is symmetrical. Let $AC$ intersect $MN$ at $I$ . Then, $\bigtriangleup{IMC}$ is similar to $\bigtriangleup{AIN}$ . Therefore, $\frac{CI}{MC}=\frac{AI}{AN}$ . Let the length of $PI=l$ , then $\frac{25-l}{20}=\frac{3+l}{6}$ . Solving we get $l=\frac{45}{13}$ . Doing the Pythagorean theorem on triangles $IMC$ and $AIN$ for sides $MI$ and $IN$ respectively, we obtain the equation $\sqrt{(\frac{280}{13})^2-400} +\sqrt{(\frac{84}{13})^2-36}=MN=2r_1$ where $r_1$ denotes the radius of the circle. Solving, we get $MN=6\sqrt{3}$ . Additionally, quadrilateral $OLBM$ is symmetrical so $OL=OM$ . Let $OL=OM=x$ and extend a perpendicular foot from $B$ to $AD$ and call it $R$ . Then, $\bigtriangleup{ABR}$ is right with $AR=6-x$ , $AB=6+x$ , and $RB=2r_1=MN=6\sqrt{3}$ . Taking the difference of squares, we get $108=24x \Longrightarrow x=\frac{9}{2}$ . The area of $ABCD$ is $MN\cdot{BC}=(20+x)\cdot{MN} \Longrightarrow \frac{49}{2}\cdot{6\sqrt{3}}=147\sqrt{3}$ . Therefore, the answer is $147+3=\boxed{150}$
~ Magnetoninja

## Solution 7 (Intuitive, no trig, no weird auxiliary lines)
Say that $BC$ is tangent to the circle at $X$ and $AD$ tangent at $Y$ . Also, $H$ is the intersection of $XY$ (diameter) and $AC$ (diagonal). Then by power of a point with given info on $A$ and $C$ we get that $AY=6$ and $CX=20$ . Note that $HAY \sim HCX$ , and since $\frac{AY}{CX}=\frac{3}{10}$ we note that \[\frac{AH}{CH} = \frac{AP+PH}{CQ+QH} = \frac{3+PH}{16+QH} =\frac{AY}{CX}=\frac{3}{10}\] . Since $PH+HQ=9$ , we get that $PH=\frac{45}{13}$ and $QH=\frac{72}{13}$ . This is the length information within the circle. The same triangle similarity also means that $\frac{YH}{XH}=\frac{3}{10}$ , so if the radius of the circle is $r$ then we have $XH=\frac{20}{13}r$ and $YH = \frac{6}{13}r$ . By power of a point on H, we can figure out $r$ : \[XH\cdot YH = PH \cdot QG\] \[\frac{20}{13}r \cdot \frac{6}{13}r = \frac{45}{13} \cdot \frac{72}{13}\] and we get that $r = 3 \sqrt 3$ . Thus, we have that the height of the parallelogram is $2r=6 \sqrt 3$ and we want to find $BC$ . If $AB$ is tangent to the circle at $E$ , then set $a = BX = BE$ . Using pythagorean theorem, $AO^2+BO^2=AB^2$ and we can plug in diagram values: \[(AY^2+OY^2)+(BX^2+OX)^2=AB^2\] \[(6^2+(3 \sqrt 3)^2) + (a^2+(3 \sqrt 3)^2)=(a+6)^2.\] Solving, we get $a=\frac{9}{2}$ Finally, we have $[ABCD]=XY \cdot BC = 6 \sqrt 3 \cdot (20+\frac{9}{2}) \rightarrow \boxed{150}$
~ Brocolimanx

## Solution 8 (Ptolemy's Theorem + Power of Point + Pythagorean Theorem)
Let $E$ , $F$ , $G$ be the circle's point of tangency with sides $AD$ , $AB$ , and $BC$ , respectively. Let $O$ be the center of the inscribed circle.
By Power of a Point, $AE^2 = AP \cdot AQ = 3(3+9) = 36$ , so $AE = 6$ . Similarly, $GC^2 = CQ \cdot CP = 16(16+9) = 400$ , so $GC = 20$ .
Construct $GE$ , and let $I$ be the point of intersection of $GE$ and $AC$ . $GE \perp BC$ and $GE \perp AD$ . By AA, $\triangle IGC \sim \triangle IEA$ , and we have $\frac{AI}{IC} = \frac{AE}{GC} = \frac{3}{10}$ . We also know $AI + IC = AC = 28$ , so $AI = \frac{84}{13}$ and $IC = \frac{280}{13}$ .
Using Pythagorean Theorem on $\triangle IEA$ and $\triangle CIG$ , we find that $EI = \frac{18\sqrt{3}}{13}$ and $IG = \frac{60\sqrt{3}}{13}$ . Thus, $GE = EI + IG = 6\sqrt{3}$ , and the radius of the circle is $3\sqrt{3}$ .
Construct $EF$ , $FG$ . $\angle AFO = \angle AEO = 90^{\circ}$ , so $AEOF$ is cyclic. Similarly, $BFOG$ is cyclic.
Now, we attempt to set up Ptolemy. Using Pythagorean Theorem on $\triangle AEO$ , we find that $AO = 3\sqrt{7}$ . By Ptolemy's Theorem, $(AE)(FO) + (AF)(EO) = (AO)(FE)$ , from which we have $(6)(3\sqrt{3}) + (6)(3\sqrt{3}) = (3\sqrt{7})(FE)$ and $FE = 12\frac{\sqrt{3}}{\sqrt{7}}$ . From Thales' Circle, $\triangle FGE$ is a right triangle, and $EF^2 + FG^2 = GE^2$ , so $FG = \frac{18}{\sqrt{7}}$ .
Set $BF = BG = s$ . $BO = \sqrt{s^2 + (3\sqrt{3})^2} = \sqrt{s^2+27}$ , so by Ptolemy's Theorem on $BFOG$ , we have
\[(BF)(GO) + (BG)(FO) = (FG)(BO)\] \[(3\sqrt{3})(s) + (3\sqrt{3})(s) = (\frac{18}{\sqrt{7}})(\sqrt{s^2+27})\] Solving yields $s = \frac{9}{2}$ .
We know that $BC = BG + GC = 20 + \frac{9}{2} = \frac{49}{2}$ , so the area of $ABCD = (\frac{49}{2})(6\sqrt{3}) = 147\sqrt{3}$ . The requested answer is $147 + 3 = \boxed{150}$ .
~ adam_zheng

## Solution 9
Let points $E$ , $F$ , $G$ be the points where lines $BC$ , $AB$ , and $AD$ are tangent to the circle respectively. Then extend line $BC$ to point $H$ such that $AH$ is perpendicular to $BC$ .
According to Power of a Point, $CQ\cdot CP=CE^2\rightarrow 16\cdot 25=CE^2\rightarrow CE=20$ .
Similarly, $AP\cdot AQ=AF^2\rightarrow 3\cdot 12=AF^2\rightarrow AF=6$ .
(Note that $AG=AF=6$ because they are intersecting tangents from the same circle. Furthermore, $HE=AG=6$ due to a simple upwards translation.)
Therefore, $HC=HE+EC=6+20=26$ , and we already know that $AC=28$ , meaning that we can use the Pythagorean Theorem on $\Delta AHC$ to obtain: $AH=6\sqrt{3}$ .
Let $HB=k$ . Then $BE=6-HB=6-k$ . Since they are intersecting tangents from the same circle, $BF=BE=6-k$ .
Therefore, $AB=AF+BF=6+6-k=12-k$ . We have all the side lengths of $\Delta ABH$ , so applying the Pythagorean Theorem: $(6\sqrt{3})^2+k^2=(12-k)^2\rightarrow k=\frac{3}{2}$ .
Thus, $BC=BE+EC=6-k+20=26-k=\frac{49}{2}$ .
$[ABCD]=AH\cdot BC=6\sqrt{3}\cdot \frac{49}{2}=147\sqrt{3}$ , so the answer is $\boxed{150}$ .
~ sid2012

## Video Solution
https://www.youtube.com/watch?v=FeM_xXiJj0c&t=1s
~Steven Chen (www.professorchenedu.com)

## Video Solution 2 (Mathematical Dexterity)
https://www.youtube.com/watch?v=1nDKQkr9NaU

## Video Solution 3 by OmegaLearn
https://youtu.be/LpOegT0fKy8?t=740
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .