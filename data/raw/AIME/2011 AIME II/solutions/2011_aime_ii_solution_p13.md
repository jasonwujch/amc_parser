# 2011 AIME II Problem 13

## Problem

Point $P$ lies on the diagonal $AC$ of square $ABCD$ with $AP > CP$ . Let $O_{1}$ and $O_{2}$ be the circumcenters of triangles $ABP$ and $CDP$ respectively. Given that $AB = 12$ and $\angle O_{1}PO_{2} = 120^{\circ}$ , then $AP = \sqrt{a} + \sqrt{b}$ , where $a$ and $b$ are positive integers. Find $a + b$ .

### Quickest Method of Solving

This is a combination of Solutions 1 and 2.

First, draw $O_1P,O_2P,BP,DP$ . Then, observe that $\angle BAP=45$ implies that $\angle BO_1P=90$ . So, $\triangle BO_1P$ is a $45-90-45$ triangle. Similarly, observe that $DO_2P$ is too. So, a rotation of $\angle O_1PO_2$ to $\angle BPO_2$ adds $45$ degrees. Then, moving to $BPD$ subtracts $45$ degrees. Hence, $\angle BPD=120$ . Let the intersection of $BD$ and $AC$ be $Q$ . Then $BQP$ is a $30-90-60$ triangle, hence $QP=\frac{6\sqrt{2}}{\sqrt{3}}$ (We know that $BQ$ is $6\sqrt{2}$ ), or $QP=2\sqrt{6}$ Finally, $AP=QP+AQ=2\sqrt{6}+6\sqrt{2}=\sqrt{24}+\sqrt{72} \Rightarrow \boxed{096}$

## Solution 1
Denote the midpoint of $\overline{DC}$ be $E$ and the midpoint of $\overline{AB}$ be $F$ . Because they are the circumcenters, both Os lie on the perpendicular bisectors of $AB$ and $CD$ and these bisectors go through $E$ and $F$ .
It is given that $\angle O_{1}PO_{2}=120^{\circ}$ . Because $O_{1}P$ and $O_{1}B$ are radii of the same circle, the have the same length. This is also true of $O_{2}P$ and $O_{2}D$ . Because $m\angle CAB=m\angle ACD=45^{\circ}$ , $m\stackrel{\frown}{PD}=m\stackrel{\frown}{PB}=2(45^{\circ})=90^{\circ}$ . Thus, $O_{1}PB$ and $O_{2}PD$ are isosceles right triangles. Using the given information above and symmetry, $m\angle DPB = 120^{\circ}$ . Because ABP and ADP share one side, have one side with the same length, and one equal angle, they are congruent by SAS. This is also true for triangle CPB and CPD. Because angles APB and APD are equal and they sum to 120 degrees, they are each 60 degrees. Likewise, both angles CPB and CPD have measures of 120 degrees.
Because the interior angles of a triangle add to 180 degrees, angle ABP has measure 75 degrees and angle PDC has measure 15 degrees. Subtracting, it is found that both angles $O_{1}BF$ and $O_{2}DE$ have measures of 30 degrees. Thus, both triangles $O_{1}BF$ and $O_{2}DE$ are 30-60-90 right triangles. Because F and E are the midpoints of AB and CD respectively, both FB and DE have lengths of 6. Thus, $DO_{2}=BO_{1}=4\sqrt{3}$ . Because of 45-45-90 right triangles, $PB=PD=4\sqrt{6}$ .
Now, letting $x = AP$ and using Law of Cosines on $\triangle ABP$ , we have
\[96=144+x^{2}-24x\frac{\sqrt{2}}{2}\] \[0=x^{2}-12x\sqrt{2}+48\]
Using the quadratic formula, we arrive at
\[x = \sqrt{72} \pm \sqrt{24}\]
Taking the positive root, $AP=\sqrt{72}+ \sqrt{24}$ and the answer is thus $\framebox[1.5\width]{096.}$

## Solution 2
This takes a slightly different route than Solution 1.
Solution 1 proves that $\angle{DPB}=120^{\circ}$ and that $\overline{BP} = \overline{DP}$ . Construct diagonal $\overline{BD}$ and using the two statements above it quickly becomes clear that $\angle{BDP} = \angle{DBP} = 30^{\circ}$ by isosceles triangle base angles. Let the midpoint of diagonal $\overline{AC}$ be $M$ , and since the diagonals are perpendicular, both triangle $DMP$ and triangle $BMP$ are 30-60-90 right triangles. Since $\overline{AB} = 12$ , $\overline{AC} = \overline{BD} = 12\sqrt{2}$ and $\overline{BM} = \overline{DM} = 6\sqrt{2}$ . 30-60-90 triangles' sides are in the ratio $1 : \sqrt{3} : 2$ , so $\overline{MP} = \frac{6\sqrt{2}}{\sqrt{3}} = 2\sqrt {6}$ . $\overline{AP} = \overline{MP} + \overline{BM} = 6\sqrt{2} + 2\sqrt{6} = \sqrt{72} + \sqrt{24}$ . Hence, $72 + 24 = \framebox[1.5\width]{096}$ .

## Solution 3
Use vectors. In an $xy$ plane, let $(-s,0)$ be $A$ , $(0,s)$ be $B$ , $(s,0)$ be $C$ , $(0,-s)$ be $D$ , and $(p,0)$ be P, where $s=|AB|/\sqrt{2}=6\sqrt{2}$ . It remains to find $p$ .
The line $y=-x$ is the perpendicular bisector of $AB$ and $CD$ , so $O_1$ and $O_2$ lies on the line. Now compute the perpendicular bisector of $AP$ . The center has coordinate $(\frac{p-s}{2},0)$ , and the segment is part of the $x$ -axis, so the perpendicular bisector has equation $x=\frac{p-s}{2}$ . Since $O_1$ is the circumcenter of triangle $ABP$ , it lies on the perpendicular bisector of both $AB$ and $AP$ , so \[O_1=(\frac{p-s}{2},-\frac{p-s}{2})\] Similarly, \[O_2=(\frac{p+s}{2},-\frac{p+s}{2})\] The relation $\angle O_1PO_2=120^\circ$ can now be written using dot product as \[\vec{PO_1}\cdot\vec{PO_2}=|\vec{PO_1}|\cdot|\vec{PO_2}|\cos 120^\circ=-\frac{1}{2}|\vec{PO_1}|\cdot|\vec{PO_2}|\] Computation of both sides yields \[\frac{p^2-s^2}{p^2+s^2}=-\frac{1}{2}\] Solve for $p$ gives $p=s/\sqrt{3}=2\sqrt{6}$ , so $AP=s+p=6\sqrt{2}+2\sqrt{6}=\sqrt{72}+\sqrt{24}$ . The answer is 72+24 $\Rightarrow\boxed{096}$

## Solution 4
Translate $\triangle{ABP}$ so that the image of $AB$ coincides $DC$ . Let the image of $P$ be $P’$ .
$\angle{DPC}=\angle{CPB}$ by symmetry, and $\angle{APB}=\angle{DP’C}$ because translation preserves angles. Thus $\angle{DP’C}+\angle{CPD}=\angle{CPB}+\angle{APB}=180^\circ$ . Therefore, quadrilateral $CPDP’$ is cyclic. Thus the image of $O_1$ coincides with $O_2$ .
$O_1P$ is parallel to $O_2P’$ so $\angle{P’O_2P}=\angle{O_1PO_2}=120^\circ$ , so $\angle{PDP’}=60^\circ$ and $\angle{PDC}=15^\circ$ , thus $\angle{ADP}=75^{\circ}$ .
Let $M$ be the foot of the perpendicular from $D$ to $AC$ . Then $\triangle{AMD}$ is a 45-45-90 triangle and $\triangle{DMP}$ is a 30-60-90 triangle. Thus
$AM=6\sqrt{2}$ and $MP=\frac{6\sqrt{2}}{\sqrt{3}}$ .
This gives us $AP=AM+MP=\sqrt{72}+\sqrt{24}$ , and the answer is $72+24=\boxed{096}.$

## Solution 5
Reflect $O_1$ across $AP$ to $O_1'$ . By symmetry $O_1’$ is the circumcenter of $\triangle{ADP}$
$\angle{DO_1’P}$ = $2*\angle{DAP} = 90^\circ$ , so $\angle{O_1’PD}=45^\circ$
similarly $\angle{DO_2P}$ = $2*\angle{DCP} = 90^\circ$ , so $\angle{O_2PD}=45^\circ$
Therefore $\angle{O_1’PO_2}=90^\circ$ , so that $\angle{O_1’PO_1} =120^\circ - 90^\circ = 30^\circ$
By symmetry, $\angle{O_1'PA} = \angle{APO_1} = 0.5*\angle{O_1’PO_1} = 15^\circ$
Therefore, since $O_1’$ is the circumcenter of $\triangle{ADP}$ , $\angle{ADP}$ = $0.5*(180^\circ - 2*\angle{O_1'PA}) = 75^\circ$
Therefore $\angle{APD} = 180^\circ - 45^\circ - 75^\circ = 60^\circ$
Using sine rule in $\triangle{ADP}$ , $AP = (12 * \sin 75^\circ) / \sin 60^\circ =\sqrt{72}+\sqrt{24}$ , and the answer is $72+24=\boxed{096}.$
By Kris17

## Video Solution
2011 AIME II #13
MathProblemSolvingSkills.com

## Solution 6 (Coordinates)
Why not use coordinates? After all, 45 degrees is rather friendly in terms of ordered-pair representation! We can set $A=(0, 12)$ , $B=(12,12)$ , $C=(12, 0)$ , $D=(0, 0)$ . Let this $P=(a, 12-a)$ for some $a$ .
We also know that the circumcenter is the intersection of all perpendicular bisectors of sides, but two will suffice also due to this property. Therefore, we see that $O_{1}$ is the intersection of $x=6$ and, knowing the midpoint of $AP$ to be $(\frac{a}{2}, \frac{12-a}{2})$ and thus the equation to be $y=x+(12-a)$ , we get $(6, 18-a)$ . Likewise for $O_{2}$ it's $(6, 6-a)$ . Now what do we see? $O_{1}P=O_{2}P$ (just look at the coordinates)! So both of those distances are $4\sqrt{3}$ . Solving for $a$ we get it to be $6+2\sqrt{3}$ , since $AP>CP$ . Multiply by $\sqrt{2}$ because we are looking for $AP$ to get the answer of $\boxed{096}$ .

## Solution 7 (Pure Angle Chasing)
Let $\angle APD = \theta$ . Then $\angle ADP = 180^{\circ}-45^{\circ}-\theta=135^{\circ}-\theta \implies \angle PDC=\theta-45^{\circ}$ . Realize that because $O_1$ is a circumcenter, $\angle DO_1P=\angle DCP=45^{\circ} \implies \angle DPO_1=\frac{180^{\circ}-\angle DO_1P}{2}=45^{\circ}$ . Then $\angle O_2PA=75^{\circ}-\theta \implies \angle AOP = 180^{\circ}-2\angle O_2PA = 2\theta+30^{\circ} \implies \angle ABP=\theta + 15^{\circ} \implies \angle PBC=75-\theta$ . Now, because $P$ lies on diagonal $AC$ , $\triangle PDC \cong \triangle PBC \implies \angle PDC = \angle PBC \implies \theta-45^{\circ}=75^{\circ}-\theta \implies \theta = 60^{\circ}$ . To finish, we look at $\triangle ADP$ . Drop a perpendicular from $D$ to $AP$ at $E$ . Then $\triangle ADE$ is a $45-45-90$ and $\triangle PDE$ is a $30-60-90$ . Therefore, $DE=EA=6\sqrt{2}, EP=2\sqrt{6}$ , so $AP=AE+EP=6\sqrt{2}+2\sqrt{6}=\sqrt{72}+\sqrt{24} \implies \boxed{096}$ . $\blacksquare$ ~msc

## Solution 8 (similar to solution 4)
Both $O_1$ and $O_2$ lie on the perpendicular bisector of $AB$ .
Claim: $O_1O_2=12$ and $O_1P=O_2P$ .
Proof. Translate $O_1$ and $P$ $12$ units down, and let their images be $O_1'$ and $P'$ , respectively. Note that $\triangle ABP\cong\triangle DCP'$ . Additionally, \[\angle CP'D = \angle BPA = 180^{\circ} - \angle BPC = 180^{\circ} - \angle CPD,\] so $CPDP'$ is cyclic. This means $O_1'$ and $O_2$ coincide, so $O_1O_2=12$ . This also means the circumradii of both triangles are equal, so $O_1P=O_2P$ . $\blacksquare$ .
Let the perpendicular from $P$ intersect $O_1O_2$ at $X$ and $AD$ at $Y$ . Since $\triangle O_1XP$ is 30-60-90, $XP=\frac{6}{\sqrt{3}} = 2\sqrt3$ . Since $YX=6$ , $PY=6+2\sqrt3$ , so $AP=6\sqrt2+2\sqrt6 = \sqrt{72}+\sqrt{24} \implies\boxed{96}$ .
~rayfish

## Solution 9 Visual
\[BP = DP, \angle PAB =\angle PCD = 45^\circ \implies O_{1}P =O_{2}P\] by the Law of Sines.
\[AB= CD, O_{1}A = O_{2}D = O_{1}B = O_{2}C \implies \triangle AO_{1}B = \triangle DO_{2}C.\] They have translational symmetry. The translation vector is \[\vec {AD} \implies O_{1}O_{2} = AD.\]
\[\triangle PO_{1}O_{2} = \triangle O_{1}AB \implies \angle AO_{1}B = 120^\circ \implies\] \[\angle APB = 60^\circ \implies \angle ABP = 180^\circ – 60^\circ – 45^\circ = 75^\circ.\] By the Law of Sines \[AP = \frac {AB \cdot \sin 75^\circ}{\sin 60^\circ} = \frac {AB \cdot \sin (30^\circ + 45^\circ)} {\sin 60^\circ}\] \[AP = AB \cdot (\sin 45^\circ + \cos 45^\circ \cdot \tan 30^\circ),\] \[AP = \frac {AB}{\sqrt{2}} (1 + \frac {1}{\sqrt{3}}) = 6 \sqrt {2} + 2 \sqrt {6} \implies \boxed{\textbf{096}.}\] vladimir.shelomovskii@gmail.com, vvsss
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .