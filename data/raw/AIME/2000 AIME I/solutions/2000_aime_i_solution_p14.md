# 2000 AIME I Problem 14

## Problem

In triangle $ABC,$ it is given that angles $B$ and $C$ are congruent . Points $P$ and $Q$ lie on $\overline{AC}$ and $\overline{AB},$ respectively, so that $AP = PQ = QB = BC.$ Angle $ACB$ is $r$ times as large as angle $APQ,$ where $r$ is a positive real number. Find $\lfloor 1000r \rfloor$ .

1 Problem

- 1 Problem

- 2 Official Solution (MAA)

- 3 Solution 1

- 4 Solution 2 (Law of sines)

- 5 Solution 3

- 6 Solution 4 (Trig identities)

- 7 Solution 5

- 8 See also

## Official Solution (MAA)
Let $\angle QPB=x^\circ$ . Because $\angle AQP$ is exterior to isosceles triangle $PQB$ its measure is $2x$ and $\angle PAQ$ has the same measure. Because $\angle BPC$ is exterior to $\triangle BPA$ its measure is $3x$ . Let $\angle PBC = y^\circ$ . It follows that $\angle ACB = x+y$ and that $4x+2y=180^\circ$ . Two of the angles of triangle $APQ$ have measure $2x$ , and thus the measure of $\angle APQ$ is $2y$ . It follows that $AQ=2\cdot AP\cdot \sin y$ . Because $AB=AC$ and $AP=QB$ , it also follows that $AQ=PC$ . Now apply the Law of Sines to triangle $PBC$ to find \[\frac{\sin 3x}{BC}=\frac{\sin y}{PC}=\frac{\sin y}{2\cdot AP\cdot \sin y}= \frac{1}{2\cdot BC}\] because $AP=BC$ . Hence $\sin 3x = \tfrac 12$ . Since $4x<180$ , this implies that $3x=30$ , i.e. $x=10$ . Thus $y=70$ and \[r=\frac{10+70}{2\cdot 70}=\frac 47,\] which implies that $1000r = 571 + \tfrac 37$ . So the answer is $\boxed{571}$ .

## Solution 1
Let point $R$ be in $\triangle ABC$ such that $QB = BR = RP$ . Then $PQBR$ is a rhombus , so $AB \parallel PR$ and $APRB$ is an isosceles trapezoid . Since $\overline{PB}$ bisects $\angle QBR$ , it follows by symmetry in trapezoid $APRB$ that $\overline{RA}$ bisects $\angle BAC$ . Thus $R$ lies on the perpendicular bisector of $\overline{BC}$ , and $BC = BR = RC$ . Hence $\triangle BCR$ is an equilateral triangle .
Now $\angle ABR = \angle BAC = \angle ACR$ , and the sum of the angles in $\triangle ABC$ is $\angle ABR + 60^{\circ} + \angle BAC + \angle ACR + 60^{\circ} = 3\angle BAC + 120^{\circ} = 180^{\circ} \Longrightarrow \angle BAC = 20^{\circ}$ . Then $\angle APQ = 140^{\circ}$ and $\angle ACB = 80^{\circ}$ , so the answer is $\left\lfloor 1000 \cdot \frac{80}{140} \right\rfloor = \left\lfloor \frac{4000}{7} \right\rfloor = \boxed{571}$ .

## Solution 2 (Law of sines)
Let $AP=PQ=QB=BC=x$ and $A$ be the measure of $\angle BAC$ . Since $\triangle APQ$ and $\triangle ABC$ are isoceles, $\angle APQ = 180-2A$ and $\angle ACB = 90-\frac{A}{2}$ . Because $\triangle APQ$ and $\triangle ABC$ both have a side length $x$ opposite $\angle BAC$ , by the law of sines:
$\frac{x}{\sin A}=\frac{AQ}{\sin(180-2A)}=\frac{AQ+x}{\sin(90-\frac{A}{2})}$
Simplifying, this becomes
$\frac{x}{\sin A}=\frac{AQ}{\sin 2A}=\frac{AQ+x}{\cos \frac{A}{2}}$
From the first two fractions,
$AQ\cdot \sin A = x \cdot \sin 2A = x \cdot (2\sin A \cos A) \Longrightarrow AQ=x\cdot 2\cos A$
Substituting, we have from the first and third fractions,
$\frac{x}{\sin A}=\frac{x\cdot 2\cos A + x}{\cos \frac{A}{2}} \Longrightarrow 2\cos A\sin A + \sin A=\sin 2A + \sin A = \cos \frac{A}{2}$
By sum-to-product,
$\sin 2A + \sin A = 2\sin \frac{3A}{2} \cos \frac{A}{2}$
Thus,
$2\sin \frac{3A}{2} \cos \frac{A}{2} = \cos \frac{A}{2} \Longrightarrow \sin \frac{3A}{2} = \frac{1}{2}$
Because $BC=QB<AB$ , $\angle A$ is acute, so $\frac{3A}{2}=30 \Longrightarrow A=20$
$\angle ACB = \frac{180-20}{2}=80$ , $\angle APQ = 180-2\cdot 20 = 140 \Longrightarrow r=\frac{4}{7}$
$1000r=\frac{4000}{7}=\boxed{571}.\overline{428571}$
~bad_at_mathcounts

## Solution 3
Again, construct $R$ as above.
Let $\angle BAC = \angle QBR = \angle QPR = 2x$ and $\angle ABC = \angle ACB = y$ , which means $x + y = 90$ . $\triangle QBC$ is isosceles with $QB = BC$ , so $\angle BCQ = 90 - \frac {y}{2}$ . Let $S$ be the intersection of $QC$ and $BP$ . Since $\angle BCQ = \angle BQC = \angle BRS$ , $BCRS$ is cyclic , which means $\angle RBS = \angle RCS = x$ . Since $APRB$ is an isosceles trapezoid, $BP = AR$ , but since $AR$ bisects $\angle BAC$ , $\angle ABR = \angle ACR = 2x$ .
Therefore we have that $\angle ACB = \angle ACR + \angle RCS + \angle QCB = 2x + x + 90 - \frac {y}{2} = y$ . We solve the simultaneous equations $x + y = 90$ and $2x + x + 90 - \frac {y}{2} = y$ to get $x = 10$ and $y = 80$ . $\angle APQ = 180 - 4x = 140$ , $\angle ACB = 80$ , so $r = \frac {80}{140} = \frac {4}{7}$ . $\left\lfloor 1000\left(\frac {4}{7}\right)\right\rfloor = \boxed{571}$ .

## Solution 4 (Trig identities)
Let $\angle BAC= 2\theta$ and $AP=PQ=QB=BC=x$ . $\triangle APQ$ is isosceles, so $AQ=2x\cos 2\theta =2x(1-2\sin^2\theta)$ and $AB= AQ+x=x\left(3-4\sin^2\theta\right)$ . $\triangle{ABC}$ is isosceles too, so $x=BC=2AB\sin\theta$ . Using the expression for $AB$ , we get \[1=2\left(3\sin\theta-4\sin^3\theta\right)=2\sin3\theta\] by the triple angle formula! Thus $\theta=10^\circ$ and $\angle A = 2\theta=20^\circ$ . It follows now that $\angle APQ=140^\circ$ , $\angle ACB=80^\circ$ , giving $r=\tfrac{4}{7}$ , which implies that $1000r = 571 + \tfrac 37$ . So the answer is $\boxed{571}$ .

## Solution 5
[asy]defaultpen(fontsize(8)); size(200); pair A=20*dir(80)+20*dir(60)+20*dir(100), B=(0,0), C=20*dir(0), P=20*dir(80)+20*dir(60), Q=20*dir(80), R=20*dir(0)+20*dir(80), D=20*dir(0)+20*dir(80)+20*dir(60)+20*dir(100); draw(Q--A--D--C--B--Q--P--R--Q); draw(A--C); label("A",A,NW); label("B",B,SW); label("C",C,SE); label("D",D,NE); label("P",P,W); label("Q",Q,W); label("R",R,E);[/asy] Reflect $\triangle ABC$ over $BC$ and translate it to attach side $AB$ onto $AC$ , mapping $\triangle ABC$ to $\triangle CAD$ . Point $P$ maps to $R$ , and $Q$ maps to $P$ . Then we have that $BC=BQ=QP=PA=AD=PR=RC$ . Notice how $BQ=RC$ and $BQ\parallel RC$ , so $BQRC$ is a parallelogram and $QR=BC$ . But $BC=QP=PR$ , so $\triangle QPR$ is actually equilateral. Set $\angle BAC=\angle ACD=x$ . Then notice that $\angle QPC=\angle PQA+\angle PAQ=2x$ , but $\angle RPC=\angle PQA=x$ . Thus $\angle QPR=3x=60$ , so $x=20$ . Thus $\angle QPA=140^{\circ}$ and $\angle BCA=80^{\circ}$ , so $r=\frac{80}{140}=\frac{4}{7}$ . The answer is $\left \lfloor \frac{4000}{7}\right \rfloor =\boxed{571}$ .
~ethanzhang1001
These problems are copyrighted © by the Mathematical Association of America.