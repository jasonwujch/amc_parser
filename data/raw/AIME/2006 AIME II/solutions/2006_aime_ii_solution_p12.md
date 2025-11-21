# 2006 AIME II Problem 12

## Problem

Equilateral $\triangle ABC$ is inscribed in a circle of radius $2$ . Extend $\overline{AB}$ through $B$ to point $D$ so that $AD=13,$ and extend $\overline{AC}$ through $C$ to point $E$ so that $AE = 11.$ Through $D,$ draw a line $l_1$ parallel to $\overline{AE},$ and through $E,$ draw a line $l_2$ parallel to $\overline{AD}.$ Let $F$ be the intersection of $l_1$ and $l_2.$ Let $G$ be the point on the circle that is collinear with $A$ and $F$ and distinct from $A.$ Given that the area of $\triangle CBG$ can be expressed in the form $\frac{p\sqrt{q}}{r},$ where $p, q,$ and $r$ are positive integers, $p$ and $r$ are relatively prime , and $q$ is not divisible by the square of any prime, find $p+q+r.$

## Solution 1
Notice that $\angle{E} = \angle{BGC} = 120^\circ$ because $\angle{A} = 60^\circ$ . Also, $\angle{GBC} = \angle{GAC} = \angle{FAE}$ because they both correspond to arc ${GC}$ . So $\Delta{GBC} \sim \Delta{EAF}$ .
\[[EAF] = \frac12 (AE)(EF)\sin \angle AEF = \frac12\cdot11\cdot13\cdot\sin{120^\circ} = \frac {143\sqrt3}4.\]
Because the ratio of the area of two similar figures is the square of the ratio of the corresponding sides, $[GBC] = \frac {BC^2}{AF^2}\cdot[EAF] = \frac {12}{11^2 + 13^2 - 2\cdot11\cdot13\cdot\cos120^\circ}\cdot\frac {143\sqrt3}4 = \frac {429\sqrt3}{433}$ . Therefore, the answer is $429+433+3=\boxed{865}$ .

## Solution 2: Analytic Geometry/Coord Bash
Solution by e_power_pi_times_i/edited by srisainandan6
Let the center of the circle be $O$ and the origin. Then, $A (0,2)$ , $B (-\sqrt{3}, -1)$ , $C (\sqrt{3}, -1)$ . $D$ and $E$ can be calculated easily knowing $AD$ and $AE$ , $D (-\dfrac{13}{2}, \dfrac{-13\sqrt{3}+4}{2})$ , $E (\dfrac{11}{2}, \dfrac{-11\sqrt{3}+4}{2})$ . As $DF$ and $EF$ are parallel to $AE$ and $AD$ , $F (-1, -12\sqrt{3}+2)$ . $G$ and $A$ is the intersection between $AF$ and circle $O$ . Therefore $G (-\dfrac{48\sqrt{3}}{433}, -\dfrac{862}{433})$ . Using the Shoelace Theorem, $[CBG] = \dfrac{429\sqrt{3}}{433}$ , so the answer is $\boxed{865}$ . Note that although the solution may appear short, actually getting all the coordinates take a while as there is plenty of computation.
Note by chrisdiamond10: We can save time calculating the area of the triangle once we have the coordinates of $B,C,G$ by using $\frac{b\cdot h}{2}$ . Use $BC$ as the base, then the base is $2\sqrt{3}$ . The height is easily calculated as $-1-\left(-\frac{862}{433}\right)=-1+\frac{862}{433}=\frac{429}{433}$ , so multiplying base by height and dividing by two we find that the total area is $\frac{429\sqrt{3}}{433}$ , and our answer is $\boxed{865}$ .

## Solution 3: Trig
Lines $l_1$ and $l_2$ are constructed such that $AEFD$ is a parallelogram, hence $DF = 13$ . Since $BAC$ is equilateral with angle of $60^{\circ}$ , angle $D$ is $120^{\circ}$ . Use law of cosines to find $AF = \sqrt{433}$ . Then use law of sines to find angle $BAG$ and $GAC$ . Next we use Ptolemy's Theorem on $ABGC$ to find that $CG + BG = AG$ . Next we use law of cosine on triangles $BAG$ and $GAC$ , solving for BG and CG respectively. Subtract the two equations and divide out a $BG + CG$ to find the value of $CG - BG$ . Next, $AG = 2\cdot R \cos{\theta}$ , where R is radius of circle $= 2$ and $\theta =$ angle $BAG$ . We already know sine of the angle so find cosine, hence we have found $AG$ . At this point it is system of equation yielding $CG = \frac{26\sqrt{3}}{\sqrt{433}}$ and $BG = \frac{22\sqrt{3}}{\sqrt{433}}$ . Given $[CBG] = \frac{BC \cdot CG \cdot BG}{4R}$ , and $BC = 2\sqrt{3}$ by $30-60-90$ triangle, we can evaluate to find $[CBG] = \frac{429\sqrt{3}}{433}$ , to give answer = $\boxed{865}$ .

## Solution 4
Note that $AB=2\sqrt3$ , $DF=11$ , and $EF=13$ . If we take a homothety of the parallelogram with respect to $A$ , such that $F$ maps to $G$ , we see that $\frac{[ABG]}{[ACG]}=\frac{11}{13}$ . Since $\angle AGB=\angle AGC=60^{\circ}$ , from the sine area formula we have $\frac{BG}{CG}=\frac{11}{13}$ . Let $BG=11k$ and $CG=13k$ .
By Law of Cosines on $\triangle BGC$ , we have \[12=k^2(11^2+11\cdot13+13^2)=433k^2\implies k^2=\frac{12}{433}\] Thus, $[CBG]=\frac12 (11k)(13k)\sin 120^{\circ} = \frac{\sqrt3}{4}\cdot 143\cdot \frac{12}{433}=\frac{429\sqrt3}{433}\implies\boxed{865}$ .
~rayfish

## Solution 5: Easy Similar triangles
First, by properties of cyclic quadrilterals, $<BGC = 180-<BAC=120$ . Next, we notice quadrilateral AEFD is a parallelogram, and opposites angles are supplementary, and therefore $<ADF = 180-<BAC = 120$ . Finally, by inscribed angles, $<BAG = <BCG$ . Thus we can conclude $\triangle CBG \sim \triangle AFD$ by AA similarity.
Because $\triangle FAE \cong \triangle AFD$ , $\triangle FAE \sim \triangle CBG$ aswell. So, we can write $\frac{BC}{AF} = \frac{BG}{DF} \to \frac{2\sqrt{3}}{\sqrt{433}} = \frac{BG}{11}$ since $AF = \sqrt{433}$ by the Law of Cosines. This gives $BG = \frac{22\sqrt{3}}{\sqrt{433}}$ and doing an identical process yields $CG = \frac{26\sqrt{3}}{\sqrt{433}}$ . Thus, $[CBG] = \frac{26\sqrt{3}}{\sqrt{433}} \cdot \frac{22\sqrt{3}}{\sqrt{433}} \cdot \sin 120 = \frac{429\sqrt{3}}{433} \to p+q+r = \boxed{865}$ .
~BossLu99
These problems are copyrighted © by the Mathematical Association of America.