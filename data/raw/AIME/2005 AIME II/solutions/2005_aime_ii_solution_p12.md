# 2005 AIME II Problem 12

## Problem

Square $ABCD$ has center $O,\ AB=900,\ E$ and $F$ are on $AB$ with $AE<BF$ and $E$ between $A$ and $F, m\angle EOF =45^\circ,$ and $EF=400.$ Given that $BF=p+q\sqrt{r},$ where $p,q,$ and $r$ are positive integers and $r$ is not divisible by the square of any prime , find $p+q+r.$

1 Problem

- 1 Problem

- 2 Solutions 2.1 Solution 1 (trigonometry) 2.2 Solution 2 (synthetic) 2.3 Solution 3 (similar triangles) 2.4 Solution 4 (Abusing Stewart) 2.5 Solution 5 (Complex Numbers) 2.6 Solution 6 2.7 Solution 7 (Using a Circle) 2.8 Solution 8 (More Similar Triangles) 2.9 Solution 9 2.10 Solution 10(Similar Triangles)

- 3 See also

- 2.1 Solution 1 (trigonometry)

- 2.2 Solution 2 (synthetic)

- 2.3 Solution 3 (similar triangles)

- 2.4 Solution 4 (Abusing Stewart)

- 2.5 Solution 5 (Complex Numbers)

- 2.6 Solution 6

- 2.7 Solution 7 (Using a Circle)

- 2.8 Solution 8 (More Similar Triangles)

- 2.9 Solution 9

- 2.10 Solution 10(Similar Triangles)

## Solutions

## Solution 1 (trigonometry)
Let $G$ be the foot of the perpendicular from $O$ to $AB$ . Denote $x = EG$ and $y = FG$ , and $x > y$ (since $AE < BF$ and $AG = BG$ ). Then $\tan \angle EOG = \frac{x}{450}$ , and $\tan \angle FOG = \frac{y}{450}$ .
By the tangent addition rule $\left( \tan (a + b) = \frac{\tan a + \tan b}{1 - \tan a \tan b} \right)$ , we see that \[\tan 45 = \tan (EOG + FOG) = \frac{\frac{x}{450} + \frac{y}{450}}{1 - \frac{x}{450} \cdot \frac{y}{450}}.\] Since $\tan 45 = 1$ , this simplifies to $1 - \frac{xy}{450^2} = \frac{x + y}{450}$ . We know that $x + y = 400$ , so we can substitute this to find that $1 - \frac{xy}{450^2} = \frac 89 \Longrightarrow xy = 150^2$ .
Substituting $x = 400 - y$ again, we know have $xy = (400 - y)y = 150^2$ . This is a quadratic with roots $200 \pm 50\sqrt{7}$ . Since $y < x$ , use the smaller root, $200 - 50\sqrt{7}$ .
Now, $BF = BG - FG = 450 - (200 - 50\sqrt{7}) = 250 + 50\sqrt{7}$ . The answer is $250 + 50 + 7 = \boxed{307}$ .

## Solution 2 (synthetic)
Label $BF=x$ , so $EA =$ $500 - x$ . Rotate $\triangle{OEF}$ about $O$ until $EF$ lies on $BC$ . Now we know that $\angle{EOF}=45^\circ$ therefore $\angle BOF+\angle AOE=45^\circ$ also since $O$ is the center of the square. Label the new triangle that we created $\triangle OGJ$ . Now we know that rotation preserves angles and side lengths, so $BG=500-x$ and $JC=x$ . Draw $GF$ and $OB$ . Notice that $\angle BOG =\angle OAE$ since rotations preserve the same angles so $\angle{FOG}=45^\circ$ too. By SAS we know that $\triangle FOE\cong \triangle FOG,$ so $FG=400$ . Now we have a right $\triangle BFG$ with legs $x$ and $500-x$ and hypotenuse $400$ . By the Pythagorean Theorem ,
\begin{align*} (500-x)^2+x^2&=400^2 \\ 250000-1000x+2x^2&=16000 \\ 90000-1000x+2x^2&=0 \end{align*}
and applying the quadratic formula we get that $x=250\pm 50\sqrt{7}$ . Since $BF > AE,$ we take the positive root, and our answer is $p+q+r = 250 + 50 + 7 = 307$ .

## Solution 3 (similar triangles)
[asy] size(3inch); pair A, B, C, D, M, O, X, Y; A = (0,900); B = (900,900); C = (900,0); D = (0,0); M = (450,900); O = (450,450); X = (250 - 50*sqrt(7),900); Y = (650 - 50*sqrt(7),900); draw(A--B--C--D--cycle); draw(X--O--Y); draw(M--O--A); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$E$",X,N); label("$F$",Y,NNE); label("$O$",O,S); label("$M$",M,N); [/asy] Let the midpoint of $\overline{AB}$ be $M$ and let $FB = x$ , so then $MF = 450 - x$ and $AF = 900 - x$ . Drawing $\overline{AO}$ , we have $\triangle OEF\sim\triangle AOF$ , so \[\frac{OF}{EF} = \frac{AF}{OF}\Rightarrow (OF)^2 = 400(900 - x).\] By the Pythagorean Theorem on $\triangle OMF$ , \[(OF)^2 = 450^2 + (450 - x)^2.\] Setting these two expressions for $(OF)^2$ equal and solving for $x$ (it is helpful to scale the problem down by a factor of 50 first), we get $x = 250\pm 50\sqrt{7}$ . Since $BF > AE$ , we want the value $x = 250 + 50\sqrt{7}$ , and the answer is $250 + 50 + 7 = \boxed{307}$ .

## Solution 4 (Abusing Stewart)
Let $x = BF$ , so $AE = 500-x$ . Let $a = OE$ , $b = OF$ . Applying Stewart's Theorem on triangles $AOB$ twice, first using $E$ as the base point and then $F$ , we arrive at the equations \[(450 \sqrt{2})^2 (900) = 900(500-x)(400+x) + a^2 (900)\] and \[(450 \sqrt{2})^2 (900) = 900x(900-x) + b^2 (900)\] Now applying law of sines and law of cosines on $\triangle EOF$ yields \[\frac{1}{2} ab \sin 45^{\circ} = \frac{4}{9} \times \frac{1}{4} \times 900^2 = 202500\] and \[a^2+b^2- 2 ab \cos 45^{\circ} = 160000\] Solving for $ab$ from the sines equation and plugging into the law of cosines equation yields $a^2+b^2 = 290000$ . We now finish by adding the two original stewart equations and obtaining: \[2(450\sqrt{2})^2 = (500-x)(400+x)+x(900-x)+520000\] This is a quadratic which only takes some patience to solve for $x = 250 + 50\sqrt{7}$

## Solution 5 (Complex Numbers)
Let lower case letters be the complex numbers correspond to their respective upper case points in the complex plane, with $o = 0, a = -450 + 450i, b = 450 + 450i$ , and $f = x + 450i$ . Since $EF$ = 400, $e = (x-400) + 450i$ . From $\angle{EOF} = 45^{\circ}$ , we can deduce that the rotation of point $F$ 45 degrees counterclockwise, $E$ , and the origin are collinear. In other words, \[\dfrac{e^{i \frac{\pi}{4}} \cdot (x + 450i)}{(x - 400) + 450i}\] is a real number. Simplyfying using the fact that $e^{i \frac{\pi}{4}} = \dfrac{\sqrt{2}}{2} + i \dfrac{\sqrt{2}}{2}$ , clearing the denominator, and setting the imaginary part equal to $0$ , we eventually get the quadratic \[x^2 - 400x + 22500 = 0\] which has solutions $x = 200 \pm 50\sqrt{7}$ . It is given that $AE < BF$ , so $x = 200 - 50\sqrt{7}$ and \[BF = 450 - (200 - 50\sqrt{7}) = 250 + 50\sqrt{7} \Rightarrow \boxed{307}.\]
-MP8148

## Solution 6
[asy] size(250); pair A,B,C,D,O,E,F,G,H,K; A = (0,0); B = (900,0); C = (900,900); D = (0,900); O = (450,450); E = (600,0); F = (150,0); G = (-600,0); H = (450,0); K = (0,270); draw(A--B--C--D--cycle); draw(O--E); draw(O--F); draw(O--G); draw(A--G); draw(O--H); label("O",O,N); label("A",A,S); label("B",B,SE); label("C",C,NE); label("D",D,NW); label("E",E,SE); label("F",F,S); label("H",H,SW); label("G",G,SW); label("x",H--E,S); label("K",K,NW); [/asy] Let G be a point such that it lies on AB, and GOE is 90 degrees. Let H be foot of the altitude from O to AB. Since $\triangle GOE \sim \triangle OHE$ , $\frac{GO}{OE} = \frac{450}{x}$ , and by Angle Bisector Theorem , $\frac{GF}{FE} = \frac{450}{x}$ . Thus, $GF = \frac{450 \cdot 400}{x}$ . $AF = AH-FH = 50+x$ , and $KA = EB$ (90 degree rotation), and now we can bash on 2 similar triangles $\triangle GAK \sim \triangle GHO$ .
\[\frac{GA}{AK} = \frac{GH}{OH}\] \[\frac{\frac{450 \cdot 400}{x}-50-x}{450-x} = \frac{\frac{450 \cdot 400}{x}+400-x}{450}\] I hope you like expanding \[x^2 - 850x + \frac{81000000}{x} = -450x - 22500 + \frac{81000000}{x}\] \[x^2 - 400x + 22500 = 0\] Quadratic formula gives us \[x = 200 \pm 50 \sqrt{7}\] Since AE < BF \[x = 200 - 50 \sqrt{7}\] Thus, \[BF = 250 + 50 \sqrt{7}\] So, our answer is $\boxed{307}$ .
-AlexLikeMath

## Solution 7 (Using a Circle)
We know that G is on the perpendicular bisector of $EF$ , which means that $EJ=JF=200$ , $EG=GF=200\sqrt{2}$ and $GH=250$ . Now, let $HO$ be equal to $x$ . We can set up an equation with the Pythagorean Theorem:
\begin{align*} \sqrt{x^2+250^2}&=(200\sqrt{2})^2 \\ x^2+62500&=80000 \\ x^2&=17500 \\ x&=50\sqrt{7} \end{align*}
Now, since $IO=450$ ,
\begin{align*} HI&=450-x \\ &=450-50\sqrt{7} \\ \end{align*} \\
Since $HI=AJ$ , we now have:
\begin{align*} BF&=AB-AJ-JF \\ &=900-(450-50\sqrt{7})-200 \\ &=250+50\sqrt{7} \\ \end{align*}
This means that our answer would be $250+50+7=\boxed{307}$
~Jerry_Guo

## Solution 8 (More Similar Triangles)
Construct $BO, AO.$ Let $\angle{FOB} = \alpha.$ Also let $FB = x$ then $AE = 500-x.$ We then have from simple angle-chasing: \begin{align*} \angle{BFO} = 135 - \alpha \\ \angle{OFE} = 45 + \alpha \\ \angle{EOA} = 45 - \alpha \\ \angle{AEO} = 90 + \alpha \\ \angle{OEF} = 90 - \alpha. \end{align*} From AA similarity we have \[\triangle{EOB} \sim \triangle{EFO}.\] This gives the ratios, \[\dfrac{400 + x}{EO} = \dfrac{450\sqrt{2}}{FO}.\] Similarly from AA similarity \[\triangle{FOA} \sim \triangle{FEO}.\] So we get the ratios \[\dfrac{EO}{450\sqrt{2}} = \dfrac{FO}{900-x}.\] We can multiply to get \[\dfrac{400 + x}{450\sqrt{2}} = \dfrac{450\sqrt{2}}{900 - x}.\] Cross-multiplying reveals \[360000 + 500x - x^2 = 405000.\] Bringing everything to one side we have \[x^2 - 500x + 45000 = 0.\] By the quadratic formula we get \[x = \dfrac{500 + \sqrt{500^2 - 4\cdot45000}}{2} = \dfrac{500 + \sqrt{70000}}{2} = \dfrac{500 + 100\sqrt{7}}{2} = 250 + 50\sqrt{7}.\] Therefore \[p+q+r = 250 + 50 + 7 = \boxed{307}.\] ~aa1024

## Solution 9
We use ratio lemma and Stewart's theorem: Connect $OA, OE, OF, OB$ and let $AE = x$ and $BF = 500 - x.$ Let angle $AOE = y,$ hence $BOF = 45 - y.$ Now, we apply Stewart's theorem in triangles $AOF$ and $BOE$ to get $OE$ and $OF$ in terms of $x$ finally, calculate $x/400$ and $500-x/400$ using ratio lemma to find $x$ and $y$

## Solution 10(Similar Triangles)
Draw AO, OB, and extend OB to D. Let $\angle{FOB} = \alpha.$ Then, after angle chasing, we find that \[\angle{AEB} = 90 + \alpha\] . Using this, we draw a line perpendicular to $AB$ at $E$ to meet $BD$ at $M$ . Since $\angle{MEO} = \alpha$ and $\angle{EMO} = 45$ , we have that \[\triangle{EMO} \sim \triangle{OBF}\] Let $FB = x$ . Then $EM = 400+x$ . Since $FB/BO = \frac{x}{450\sqrt{2}}$ , and $MO/EM = FB/OB$ , we have \[MO = \frac{(400+x)x}{450\sqrt{2}}\] Since $\triangle{EBM}$ is a $45-45-90$ triangle, \[(400+x)\sqrt{2} = 450 \sqrt{2} + \frac{(400+x)x}{450\sqrt{2}}\] Solving for $x$ , we get that $x=250 +- 50s\sqrt{7}$ , but since $FB>AE$ , $FB = 250+50\sqrt{7}$ , thus \[p+q+r=\boxed{307}\] -dchang0524
These problems are copyrighted © by the Mathematical Association of America.