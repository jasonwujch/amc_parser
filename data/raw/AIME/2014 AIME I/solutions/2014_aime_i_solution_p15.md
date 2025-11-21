# 2014 AIME I Problem 15

## Problem

In $\triangle ABC$ , $AB = 3$ , $BC = 4$ , and $CA = 5$ . Circle $\omega$ intersects $\overline{AB}$ at $E$ and $B$ , $\overline{BC}$ at $B$ and $D$ , and $\overline{AC}$ at $F$ and $G$ . Given that $EF=DF$ and $\frac{DG}{EG} = \frac{3}{4}$ , length $DE=\frac{a\sqrt{b}}{c}$ , where $a$ and $c$ are relatively prime positive integers, and $b$ is a positive integer not divisible by the square of any prime. Find $a+b+c$ .

## Fast Video Solution
https://www.youtube.com/watch?v=n2tDvCQYK-I

## Solution 1
Since $\angle DBE = 90^\circ$ , $DE$ is the diameter of $\omega$ . Then $\angle DFE=\angle DGE=90^\circ$ . But $DF=FE$ , so $\triangle DEF$ is a 45-45-90 triangle. Letting $DG=3x$ , we have that $EG=4x$ , $DE=5x$ , and $DF=EF=\frac{5x}{\sqrt{2}}$ .
Note that $\triangle DGE \sim \triangle ABC$ by SAS similarity, so $\angle BAC = \angle GDE$ and $\angle ACB = \angle DEG$ . Since $DEFG$ is a cyclic quadrilateral, $\angle BAC = \angle GDE=180^\circ-\angle EFG = \angle AFE$ and $\angle ACB = \angle DEG = \angle GFD$ , implying that $\triangle AFE$ and $\triangle CDF$ are isosceles. As a result, $AE=CD=\frac{5x}{\sqrt{2}}$ , so $BE=3-\frac{5x}{\sqrt{2}}$ and $BD =4-\frac{5x}{\sqrt{2}}$ .
Finally, using the Pythagorean Theorem on $\triangle BDE$ , \[\left(3-\frac{5x}{\sqrt{2}}\right)^2 + \left(4-\frac{5x}{\sqrt{2}}\right)^2 = (5x)^2\] Solving for $x$ , we get that $x=\frac{5\sqrt{2}}{14}$ , so $DE= 5x =\frac{25 \sqrt{2}}{14}$ . Thus, the answer is $25+2+14=\boxed{041}$ .

## Solution 2
[asy] pair A = (0,3); pair B = (0,0); pair C = (4,0); draw(A--B--C--cycle); dotfactor = 3; dot("$A$",A,dir(135)); dot("$B$",B,dir(215)); dot("$C$",C,dir(305)); pair D = (2.21, 0); pair E = (0, 1.21); pair F = (1.71, 1.71); pair G = (2, 1.5); dot("$D$",D,dir(270)); dot("$E$",E,dir(180)); dot("$F$",F,dir(90)); dot("$G$",G,dir(0)); draw(Circle((1.109, 0.609), 1.28)); draw(D--E); draw(E--F); draw(D--F); draw(E--G); draw(D--G); draw(B--F); draw(B--G); [/asy]
First we note that $\triangle DEF$ is an isosceles right triangle with hypotenuse $\overline{DE}$ the same as the diameter of $\omega$ . We also note that $\triangle DGE \sim \triangle ABC$ since $\angle EGD$ is a right angle and the ratios of the sides are $3:4:5$ .
From congruent arc intersections, we know that $\angle GED \cong \angle GBC$ , and that from similar triangles $\angle GED$ is also congruent to $\angle GCB$ . Thus, $\triangle BGC$ is an isosceles triangle with $BG = GC$ , so $G$ is the midpoint of $\overline{AC}$ and $AG = GC = 5/2$ . Similarly, we can find from angle chasing that $\angle ABF = \angle EDF = \frac{\pi}4$ . Therefore, $\overline{BF}$ is the angle bisector of $\angle B$ . From the angle bisector theorem, we have $\frac{AF}{AB} = \frac{CF}{CB}$ , so $AF = 15/7$ and $CF = 20/7$ .
Lastly, we apply power of a point from points $A$ and $C$ with respect to $\omega$ and have $AE \times AB=AF \times AG$ and $CD \times CB=CG \times CF$ , so we can compute that $EB = \frac{17}{14}$ and $DB = \frac{31}{14}$ . From the Pythagorean Theorem, we result in $DE = \frac{25 \sqrt{2}}{14}$ , so $a+b+c=25+2+14= \boxed{041}$
Also: $FG=\frac{20}{7}-\frac{5}{2}=\frac{5}{2}-\frac{15}{7}=\frac{5}{14}$ . We can also use Ptolemy's Theorem on quadrilateral $DEFG$ to figure what $FG$ is in terms of $d$ : \[DE\cdot FG+DG\cdot EF=DF\cdot EG\] \[d\cdot FG+\frac{3d}{5}\cdot \frac{d}{\sqrt{2}}=\frac{4d}{5}\cdot \frac{d}{\sqrt{2}}\] \[d\cdot FG+\frac{3d^2}{5\sqrt{2}}=\frac{4d^2}{5\sqrt{2}}\implies FG=\frac{d}{5\sqrt{2}}\] Thus $\frac{d}{5\sqrt{2}}=\frac{5}{14}\rightarrow d=5\sqrt{2}\cdot\frac{5}{14}=\frac{25\sqrt{2}}{14}$ . $a+b+c=25+2+14= \boxed{041}$

## Solution 3
Call $DE=x$ and as a result $DF=EF=\frac{x\sqrt{2}}{2}, EG=\frac{4x}{5}, GD=\frac{3x}{5}$ . Since $EFGD$ is cyclic we just need to get $DG$ and using LoS(for more detail see the $2$ nd paragraph of Solution $2$ ) we get $AG=\frac{5}{2}$ and using a similar argument(use LoS again) and subtracting you get $FG=\frac{5}{14}$ so you can use Ptolemy to get $x=\frac{25\sqrt{2}}{14} \implies \boxed{041}$ . ~First

## Solution 4
See inside the $\triangle DEF$ , we can find that $AG>AF$ since if $AG<AF$ , we can see that Ptolemy Theorem inside cyclic quadrilateral $EFGD$ doesn't work. Now let's see when $AG>AF$ , since $\frac{DG}{EG} = \frac{3}{4}$ , we can assume that $EG=4x;GD=3x;ED=5x$ , since we know $EF=FD$ so $\triangle EFD$ is isosceles right triangle. We can denote $DF=EF=\frac{5x\sqrt{2}}{2}$ .Applying Ptolemy Theorem inside the cyclic quadrilateral $EFGD$ we can get the length of $FG$ can be represented as $\frac{x\sqrt{2}}{2}$ . After observing, we can see $\angle AFE=\angle EDG$ , whereas $\angle A=\angle EDG$ so we can see $\triangle AEF$ is isosceles triangle. Since $\triangle ABC$ is a $3-4-5$ triangle so we can directly know that the length of AF can be written in the form of $3x\sqrt{2}$ . Denoting a point $J$ on side $AC$ with that $DJ$ is perpendicular to side $AC$ . Now with the same reason, we can see that $\triangle DJG$ is a isosceles right triangle, so we can get $GJ=\frac{3x\sqrt{2}}{2}$ while the segment $CJ$ is $2x\sqrt{2}$ since its 3-4-5 again. Now adding all those segments together we can find that $AC=5=7x\sqrt{2}$ and $x=\frac{5\sqrt{2}}{14}$ and the desired $ED=5x=\frac{25\sqrt{2}}{14}$ which our answer is $\boxed{041}$ ~bluesoul

## Solution 5
The main element of the solution is the proof that $BF$ is bisector of $\angle B.$
Let $O$ be the midpoint of $DE.$ $\angle EBF = 90^\circ \implies$
$O$ is the center of the circle $BDGFE.$ $\angle EOF = 90^\circ \implies \overset{\Large\frown} {EF} = 90^\circ \implies \angle EBF = 45^\circ \implies$ BF is bisector of $\angle ABC\implies BF = \frac {2AB \cdot BC}{AB+BC} \cos 45^\circ =\frac {12 \cdot \sqrt{2}}{7}.$ \[\angle EGD = 90^\circ, \frac {EG}{GD}=\frac{4}{3} \implies\] \[\angle GED = \angle GCD =\gamma \implies \overset{\Large\frown} {DG} = 2\gamma.\] \[2\angle ACB = \overset{\Large\frown} {BEF} - \overset{\Large\frown} {DG} \implies \overset{\Large\frown} {BEF} = 4 \gamma \implies\] \[\angle BOF = 4 \gamma \implies \angle OBF = \angle OFB = 90^\circ – 2 \gamma.\] Let $BO = EO = DO = r \implies BF = 2 r \cos(90^\circ – 2\gamma) =$ \[=2 r \sin 2\gamma = 4r \sin \gamma \cdot \cos \gamma = 4 r\cdot \frac {3}{5} \cdot \frac {4}{5} = \frac {48}{25} = \frac {12 \cdot \sqrt{2}}{7}\implies\] \[r = \frac {25 \cdot \sqrt{2}}{28}\implies ED = 2r = \frac {25 \cdot \sqrt{2}}{14}\implies \boxed{\textbf{041}}.\] vladimir.shelomovskii@gmail.com, vvsss

## Solution 6
The main element of the solution is the proof that $G$ is midpoint of $AC.$
As in Solution 5 we get $\angle GED = \angle DBG =\gamma \implies$
$\triangle BCG$ is isosceles triangle with $BG=CG.$
Similarly $BG = AG \implies AG = CG = BG = \frac {AC}{2} =\frac {5}{2}.$
\[\overset{\Large\frown} {FG} = 90^\circ – \overset{\Large\frown} {GD} = 90^\circ – 2\gamma \implies\] \[\overset{\Large\frown} {BFG} = 4\gamma + 90^\circ – 2\gamma = 90^\circ + 2\gamma \implies\] \[\angle BOG = 90^\circ + 2\gamma \implies \angle BGO = \angle GBO = 45^\circ - \gamma.\] Let $\hspace{10mm} BO = EO = DO = r \implies$ \[BG = 2 r \cos(45^\circ – \gamma) = 2 r (\sin \gamma + \cos \gamma)\frac {\sqrt {2}}{2} =\] \[r \biggl(\frac {3}{5} + \frac {4}{5}\biggr) \sqrt {2} = r \frac {7 \sqrt{2}}{5} = \frac {5}{2}\implies\] \[r = \frac {25 \cdot \sqrt{2}}{28}\implies ED = \frac {25 \cdot \sqrt{2}}{14}\implies \boxed{\textbf{041}}.\] vladimir.shelomovskii@gmail.com, vvsss

## Solution 7
Let $(BEFGD) = \omega$ . By Incenter-Excenter(Fact $5$ ), $F$ is the angle bisector of $\angle B$ . Then by Ratio Lemma we have \[\frac{AG}{CG} = \frac{\sin(ABG)}{\sin(CBG)} \cdot \frac{AB}{BC} = \frac{\sin(GDE)}{\sin(DEG)} \cdot \frac{3}{4} = 1\] Thus, $G$ is the midpoint of $AC$ .
We can calculate $AF$ and $CF$ to be $\frac{15}{7}$ and $\frac{20}{7}$ respectively. And then by Power of a Point, we have $\newline$ \[\operatorname{Pow}_{\omega}(A) = AE \cdot AB = AF \cdot AG \implies AE = \frac{25}{14}\] And then similarly, we have $CD = AE = \frac{25}{14}$ . $\newline$
Then $EB = \frac{17}{14}$ and $DB = \frac{31}{14}$ and by Pythagorean we have $DE = \frac{25\sqrt{2}}{14}$ , so our answer is $\boxed{\textbf{041}}.$
~dolphinday

## Solution 8 (funny angle chase & trig)
Since $\angle EBD$ is right, $DE$ is clearly the diameter. Let $EF=DF=x, ED=x\sqrt{2}, DG=\tfrac{3x\sqrt{2}}{5}, EG=\tfrac{4x\sqrt{2}}{5}$ . Then, let $\angle DEG=\alpha$ . Therefore, $\angle EFG=\angle EFD+\angle DFG=90^{\circ}+\alpha,$ and $\angle EFA=90^{\circ}-\alpha$ . However, $\triangle DGE \sim \triangle ABC$ so $\angle AFE$ also equals $90^{\circ}-\alpha$ . Thus, $\triangle AEF$ is isosceles with $\angle FAE \cong \angle EFA \implies AE=EF=x.$
Furthermore, $\angle FEG = \angle FDG = \angle EDG-\angle EDF=90^{\circ}-\alpha-45^{\circ}=45^{\circ}-\alpha$ . Also, $\angle AEF=2\alpha$ in triangle $\triangle AEF$ , thus $\angle BED=135^{\circ}-2\alpha$ since $\angle AEB=180^{\circ}$ . Using $\cos \alpha=\tfrac{4}{5}$ , it's relatively easy to derive that $\cos (135^{\circ}-2\alpha)=\tfrac{17\sqrt{2}}{50}$ . Since $\cos(135^{\circ}-2\alpha)=\tfrac{BE}{DE}$ , we get that $BE=\tfrac{17x}{25}$ . Finally, since $AE+BE=x+\tfrac{17x}{25}=3$ , we solve for \[x=\tfrac{25}{14} \implies DE=x\sqrt{2}=\tfrac{25\sqrt{2}}{14},\] so our desired answer is $\boxed{041}.$
~SirAppel

## Solution 9 (Vectors)
$\angle{B} = 90^\circ ==>$ $ED$ is the diameter of the circle $==> \angle{EGD} = 90^\circ$
Because $\frac{GD}{GE} = \frac{AB}{BC} = \frac{3}{4}, \Delta DGE \sim \Delta ABC$
$\angle{DFC} = \angle{DEG} = \angle{C} ==> CD = DF = EF$
We flip the triangle for easier calculation and let $C$ be the origin.
Let $x = CD$
$DF = x\cdot e^{i2\alpha}, EF = x\cdot e^{-(90^\circ-2\alpha)}$
$E$ is on $AB$ , which means that $Re(E)$ = 4.
\[Re(x+x\cdot e^{i2\alpha}+x\cdot e^{-(90^\circ-2\alpha)}) = 4\]
\[Re(x+x(\cos{2\alpha}+i\sin{2\alpha})+x(\cos{(2\alpha-90^\circ)}+i\sin{(2\alpha-90^\circ)})) = 4\]
\[x(1+\cos{2\alpha}+\sin{2\alpha})=4\]
$\cos{2\alpha} = \cos^2{\alpha} - \sin^2{\alpha} = \frac{7}{25}$
$\sin{2\alpha} = 2\sin{\alpha}\cos{\alpha} = \frac{24}{25}$
\[x\cdot \frac{56}{25} = 4\]
\[x = \frac{25}{14}\]
Therefore $DE=\sqrt{2}\cdot \frac{25}{14} = \frac{25\sqrt{2}}{14}$
$25+2+14=\boxed{041}$
~cassphe

## Solution 10(Very similar to Solution 1 but with an added LoS)
As noted in Solution 1, $DE$ is in fact the diameter of the circle. The proof is trivial. Note that $\triangle ABC$ is a right triangle which means $\angle ABC = \angle EBD = 90^{\circ}$ . Therefore $\triangle EBD$ is an inscribed right triangle of the circle which means its arc length is just double the inscribed angle(following the Inscribed Angle Theorem) meaning the circle is cut in half by $DE \implies DE$ is indeed the diameter of the circle.
Similarly, as $DE$ is the diameter, inscribed angles $\angle EFD = \angle EGD = 90^{\circ}$ . As $EF = DF$ , it follows $\angle FED = \angle FDE = 45^{\circ} \implies \triangle EGD$ is isosceles.
Let $EF = DF = y$ :
$ED = y\sqrt{2}$
Now as $\frac{DG}{EG} = \frac{3}{4} \implies DG = 3x, EG = 4x$
Hence $\triangle EGD$ is a right triangle with legs of length $3x, 4x$ and hypotenuse of length $y\sqrt{2}$ . Obviously, by $SAS$ similarity, $\triangle EGD \sim \triangle ABC \implies \frac{DG}{ED} = \frac{AB}{AC} \implies \frac{3x}{y\sqrt{2}} = \frac{3}{5} \implies y\sqrt{2} = 5x \implies y = \frac{5x}{\sqrt{2}}$ .
Now note that quadrilateral $EFGD$ is cyclic which yields opposite angles are supplementary. Hence
$\angle FED + \angle FGD = 180^{\circ}$ and $\angle FGD + \angle DGC = 180^{\circ}$ following Angle Addition Postulate. Hence by substitution, $\angle FED = \angle DGC = 45^{\circ}$ .
Let $\angle ACB = \theta$ . Hence $\sin(\theta) = \frac{3}{5}$ following the $3-4-5$ right triangle $ABC$ . Now $\angle ACB = \angle GCD = \theta$ so we can apply Law of Sines on $\triangle DGC$ .
We already know $\angle DGC = 45^{\circ}$ . Also $\angle GCD = \theta$ and $GD = 3x$ . Let $DC = a$ . Now we apply Law of Sines:
$\frac{DC}{\sin(\angle DGC)} = \frac{GD}{\sin(\angle GCD)} \implies \frac{a}{\sin(45^{\circ})} = \frac{3x}{\sin(\theta)} \implies \frac{a}{\frac{\sqrt{2}}{2}} = \frac{3x}{\frac{3}{5}} \implies a = \frac{5x}{\sqrt{2}}$ . This means $DC = \frac{5x}{\sqrt{2}}$ .
Now based on how we found $\angle FED = \angle DGC = 45^{\circ}$ using a combination of Supplementary Angle Theorem for cyclic quadrilaterals and Angle Addition Postulate, we can conclude based on a similar logic that $\angle EDG = \angle EFA$ . The proof is below:
$\angle EDG + \angle EFG = 180^{\circ}$ and $\angle EFG + \angle EFA = 180^{\circ}$ . By substitution, $\angle EDG = \angle EFA$ .
Now let $\angle EDG = \alpha$ . From the right triangle $\triangle EDG$ , $\sin(\angle EDG) = \frac{EG}{ED} = \frac{4x}{5x} = \frac{4}{5}$ . So $\sin(\alpha) = \frac{4}{5}$ .
Now let $\angle BAC = \angle EAF = \beta$ . From the right triangle $\triangle ABC$ , $\sin(\angle BAC) = \frac{4}{5} \implies \sin(\angle EAF) = \frac{4}{5} \implies \sin(\beta) = \frac{4}{5}$ .
Now we apply Law of Sines on $\triangle EAF$ :
$\frac{EF}{\sin(\angle EAF)} = \frac{AE}{\sin(\angle EFA)} \implies \frac{\frac{5x}{\sqrt{2}}}{\sin(\angle \beta)} = \frac{AE}{\sin(\alpha)} \implies \frac{\frac{5x}{\sqrt{2}}}{\frac{4}{5}} = \frac{AE}{\frac{4}{5}} \implies AE = \frac{5x}{\sqrt{2}}$ .
Hence $EB = AB - AE = 3 - \frac{5x}{\sqrt{2}}$ and $BD = CB - CD = 4 - \frac{5x}{\sqrt{2}}$ .
Now since $\triangle EBD$ is a right triangle with legs of $EB, BD$ and hypotenuse $ED = 5x$ we solve
$(3 - \frac{5x}{\sqrt{2}})^{2} + (4 - \frac{5x}{\sqrt{2}})^{2} = (5x)^{2}$
$9 - 6 \cdot \frac{5x}{\sqrt{2}} + \frac{25x^{2}}{2} + 16 - 8 \cdot \frac{5x}{\sqrt{2}} + \frac{25x^{2}}{2} = 25x^{2}$
$25 - \frac{30x}{\sqrt{2}} - \frac{40x}{\sqrt{2}} = 0$
$25 = \frac{70x}{\sqrt{2}} = 35x\sqrt{2}$ .
Now recall we're looking for $ED = 5x$ so we divide both sides by $7\sqrt{2}$
$\frac{25}{7\sqrt{2}} = 5x \implies 5x = \frac{25\sqrt{2}}{14}$ .
Thus the answer is $25 + 2 + 14 = \boxed{41}$ .
~ilikemath247365

## Video Solution by mop 2024
https://youtu.be/GxxZYZrQl2A
~r00tsOfUnity
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .