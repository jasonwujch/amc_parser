# 2020 AIME II Problem 15

## Problem

Let $\triangle ABC$ be an acute scalene triangle with circumcircle $\omega$ . The tangents to $\omega$ at $B$ and $C$ intersect at $T$ . Let $X$ and $Y$ be the projections of $T$ onto lines $AB$ and $AC$ , respectively. Suppose $BT = CT = 16$ , $BC = 22$ , and $TX^2 + TY^2 + XY^2 = 1143$ . Find $XY^2$ .

## Solution 1
Let $O$ be the circumcenter of $\triangle ABC$ ; say $OT$ intersects $BC$ at $M$ ; draw segments $XM$ , and $YM$ . We have $MT=3\sqrt{15}$ .
Since $\angle A=\angle CBT=\angle BCT$ , we have $\cos A=\tfrac{11}{16}$ . Notice that $AXTY$ is cyclic, so $\angle XTY=180^{\circ}-A$ , so $\cos XTY=-\cos A$ , and the cosine law in $\triangle TXY$ gives \[1143-2XY^2=-\frac{11}{8}\cdot XT\cdot YT.\]
Since $\triangle BMT \cong \triangle CMT$ , we have $TM\perp BC$ , and therefore quadrilaterals $BXTM$ and $CYTM$ are cyclic. Let $P$ (resp. $Q$ ) be the midpoint of $BT$ (resp. $CT$ ). So $P$ (resp. $Q$ ) is the center of $(BXTM)$ (resp. $CYTM$ ). Then $\theta=\angle ABC=\angle MTX$ and $\phi=\angle ACB=\angle YTM$ . So $\angle XPM=2\theta$ , so \[\frac{\frac{XM}{2}}{XP}=\sin \theta,\] which yields $XM=2XP\sin \theta=BT(=CT)\sin \theta=TY$ . Similarly we have $YM=XT$ .
Ptolemy's theorem in $BXTM$ gives \[16TY=11TX+3\sqrt{15}BX,\] while Pythagoras' theorem gives $BX^2+XT^2=16^2$ . Similarly, Ptolemy's theorem in $YTMC$ gives \[16TX=11TY+3\sqrt{15}CY\] while Pythagoras' theorem in $\triangle CYT$ gives $CY^2+YT^2=16^2$ . Solve this for $XT$ and $TY$ and substitute into the equation about $\cos XTY$ to obtain the result $XY^2=\boxed{717}$ .
(Notice that $MXTY$ is a parallelogram, which is an important theorem in Olympiad, and there are some other ways of computation under this observation.)
-Fanyuchen20020715

## Solution 2 (Official MAA)
Let $M$ denote the midpoint of $\overline{BC}$ . The critical claim is that $M$ is the orthocenter of $\triangle AXY$ , which has the circle with diameter $\overline{AT}$ as its circumcircle. To see this, note that because $\angle BXT = \angle BMT = 90^\circ$ , the quadrilateral $MBXT$ is cyclic, it follows that \[\angle MXA = \angle MXB = \angle MTB = 90^\circ - \angle TBM = 90^\circ - \angle A,\] implying that $\overline{MX} \perp \overline{AC}$ . Similarly, $\overline{MY} \perp \overline{AB}$ . In particular, $MXTY$ is a parallelogram. [asy] defaultpen(fontsize(8pt)); unitsize(0.8cm); pair A = (0,0); pair B = (-1.26,-4.43); pair C = (-1.26+3.89, -4.43); pair M = (B+C)/2; pair O = circumcenter(A,B,C); pair T = (0.68, -6.49); pair X = foot(T,A,B); pair Y = foot(T,A,C); path omega = circumcircle(A,B,C); real rad = circumradius(A,B,C); filldraw(A--B--C--cycle, 0.2*royalblue+white); label("$\omega$", O + rad*dir(45), SW); //filldraw(T--Y--M--X--cycle, rgb(150, 247, 254)); filldraw(T--Y--M--X--cycle, 0.2*heavygreen+white); draw(M--T); draw(X--Y); draw(B--T--C); draw(A--X--Y--cycle); draw(omega); dot("$X$", X, W); dot("$Y$", Y, E); dot("$O$", O, W); dot("$T$", T, S); dot("$A$", A, N); dot("$B$", B, W); dot("$C$", C, E); dot("$M$", M, N); [/asy] Hence, by the Parallelogram Law, \[TM^2 + XY^2 = 2(TX^2 + TY^2) = 2(1143-XY^2).\] But $TM^2 = TB^2 - BM^2 = 16^2 - 11^2 = 135$ . Therefore \[XY^2 = \frac13(2 \cdot 1143-135) = \boxed{717}.\]

## Solution 3 (Law of Cosines)
Let $H$ be the orthocenter of $\triangle AXY$ .
Lemma 1: $H$ is the midpoint of $BC$ .
Proof: Let $H'$ be the midpoint of $BC$ , and observe that $XBH'T$ and $TH'CY$ are cyclical. Define $H'Y \cap BA=E$ and $H'X \cap AC=F$ , then note that: \[\angle H'BT=\angle H'CT=\angle H'XT=\angle H'YT=\angle A.\] That implies that $\angle H'XB=\angle H'YC=90^\circ-\angle A$ , $\angle CH'Y=\angle EH'B=90^\circ-\angle B$ , and $\angle BH'Y=\angle FH'C=90^\circ-\angle C$ . Thus $YH'\perp AX$ and $XH' \perp AY$ ; $H'$ is indeed the same as $H$ , and we have proved lemma 1.
Since $AXTY$ is cyclical, $\angle XTY=\angle XHY$ and this implies that $XHYT$ is a paralelogram. By the Law of Cosines: \[XY^2=XT^2+TY^2+2(XT)(TY)\cdot \cos(\angle A)\] \[XY^2=XH^2+HY^2+2(XH)(HY) \cdot \cos(\angle A)\] \[HT^2=HX^2+XT^2-2(HX)(XT) \cdot \cos(\angle A)\] \[HT^2=HY^2+YT^2-2(HY)(YT) \cdot \cos(\angle A).\] We add all these equations to get: \[HT^2+XY^2=2(XT^2+TY^2) \qquad (1).\] We have that $BH=HC=11$ and $BT=TC=16$ using our midpoints. Note that $HT \perp BC$ , so by the Pythagorean Theorem, it follows that $HT^2=135$ . We were also given that $XT^2+TY^2=1143-XY^2$ , which we multiply by $2$ to use equation $(1)$ . \[2(XT^2+TY^2)=2286-2 \cdot XY^2\] Since $2(XT^2+TY^2)=2(HT^2+TY^2)=HT^2+XY^2$ , we have \[135+XY^2=2286-2 \cdot XY^2\] \[3 \cdot XY^2=2151.\] Therefore, $XY^2=\boxed{717}$ . ~ MathLuis

## Solution 4 (Similarity and median)
Using the Claim (below) we get $\triangle ABC \sim \triangle XTM \sim \triangle YMT.$
Corresponding sides of similar $\triangle XTM \sim \triangle YMT$ is $MT,$ so
$\triangle XTM = \triangle YMT \implies MY = XT, MX = TY \implies XMYT$ – parallelogram.
\[4 TD^2 = MT^2 = \sqrt{BT^2 - BM^2} =\sqrt{153}.\] The formula for median $DT$ of triangle $XYT$ is \[2 DT^2 = XT^2 + TY^2 – \frac{XY^2}{2},\] \[3 \cdot XY^2 = 2XT^2 + 2TY^2 + 2XY^2 – 4 DT^2,\] \[3 \cdot XY^2 = 2 \cdot 1143-153 = 2151 \implies XY^2 = \boxed{717}.\]
Claim
Let $\triangle ABC$ be an acute scalene triangle with circumcircle $\omega$ . The tangents to $\omega$ at $B$ and $C$ intersect at $T$ . Let $X$ be the projections of $T$ onto line $AB$ . Let M be midpoint BC. Then triangle ABC is similar to triangle XTM.
Proof
$\angle BXT = \angle BMT = 90^o \implies$ the quadrilateral $MBXT$ is cyclic.
$BM \perp MT, TX \perp AB \implies \angle MTX = \angle MBA.$
$\angle CBT = \angle BAC = \frac {\overset{\Large\frown} {BC}}{ 2} \implies \triangle ABC \sim \triangle XTM.$
vladimir.shelomovskii@gmail.com, vvsss

## Solution 5 (Symmedian and Stewarts)
Let $M$ be the midpoint of $BC$ . Note that $\angle XYT = \angle XAT = \angle MAC$ because $AT$ is a symmedian. Similarly, $\angle TXY = \angle MAB$ . $XT = 16\sin{C}$ and $YT = 16\sin{C}$ . By law of sines on $XYT$ , $\frac{16\sin{C}}{\sin{XYT}} = \frac{XY}{\sin{A}}$ . However by law of sines on $MAC$ , $\frac{\sin{C}}{\sin{MAC}} = \frac{AM}{11}$ . Combining these two yields, $\frac{16}{11} AM = \frac{XY}{\sin{A}}$ . Since $\sin{A} = \frac{\sqrt{135}}{16}$ , we have $XY^2 = \frac{135}{121} AM^2$ .
Letting $AB = x$ , $AC = y$ , and $AM = d$ , we have $x^2 + y^2 = 2d^2 + 242$ by Stewarts. Since $x = 2R\sin{C}$ , and $y = 2R\sin{B}$ by extended law of sines, we can write $\sin^2{B} + \sin^2{C} = \frac{2d^2 + 242}{4R^2}$ . By law of cosines on $ABC$ , $x^2 + y^2 - 2xy(\frac{11}{16}) = 484$ , $\frac{11}{8} xy + 484 = 2d^2 + 242$ , $xy = \frac{8}{11} (2d^2 - 242)$ . Then similarly as before we can write $\sin{B}\sin{C} = \frac{\frac{8}{11} (2d^2 - 242)}{4R^2}$ .
By law of cosines on $XYT$ and using $XT^2 + XY^2 + YT^2 = 1143$ , we have $512(\sin^2{B} + \sin^2{C}) - 1143 = -512\sin{B}\sin{C}(\frac{11}{16})$ . Substituting our previous values here and using $R = \frac{176}{\sqrt{135}}$ yields a value for $d^2$ , and multiplying by $\frac{135}{121}$ gives $\boxed{717}$ .
~sdfgfjh
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .