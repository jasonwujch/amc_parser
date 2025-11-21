# 2019 AIME I Problem 15

## Problem

Let $\overline{AB}$ be a chord of a circle $\omega$ , and let $P$ be a point on the chord $\overline{AB}$ . Circle $\omega_1$ passes through $A$ and $P$ and is internally tangent to $\omega$ . Circle $\omega_2$ passes through $B$ and $P$ and is internally tangent to $\omega$ . Circles $\omega_1$ and $\omega_2$ intersect at points $P$ and $Q$ . Line $PQ$ intersects $\omega$ at $X$ and $Y$ . Assume that $AP=5$ , $PB=3$ , $XY=11$ , and $PQ^2 = \frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
[asy] size(8cm); pair O, A, B, P, O1, O2, Q, X, Y; O=(0, 0); A=dir(140); B=dir(40); P=(3A+5B)/8; O1=extension((A+P)/2, (A+P)/2+(0, 1), A, O); O2=extension((B+P)/2, (B+P)/2+(0, 1), B, O); Q=intersectionpoints(circle(O1, length(A-O1)), circle(O2, length(B-O2)))[1]; X=intersectionpoint(P -- (P+(P-Q)*100), circle(O, 1)); Y=intersectionpoint(Q -- (Q+(Q-P)*100), circle(O, 1)); draw(circle(O, 1)); draw(circle(O1, length(A-O1))); draw(circle(O2, length(B-O2))); draw(A -- B); draw(X -- Y); draw(A -- O -- B); draw(O1 -- P -- O2); dot("$O$", O, S); dot("$A$", A, A); dot("$B$", B, B); dot("$P$", P, dir(70)); dot("$Q$", Q, dir(200)); dot("$O_1$", O1, SW); dot("$O_2$", O2, SE); dot("$X$", X, X); dot("$Y$", Y, Y); [/asy] Let $O_1$ and $O_2$ be the centers of $\omega_1$ and $\omega_2$ , respectively. There is a homothety at $A$ sending $\omega$ to $\omega_1$ that sends $B$ to $P$ and $O$ to $O_1$ , so $\overline{OO_2}\parallel\overline{O_1P}$ . Similarly, $\overline{OO_1}\parallel\overline{O_2P}$ , so $OO_1PO_2$ is a parallelogram. Moreover, \[\angle O_1QO_2=\angle O_1PO_2=\angle O_1OO_2,\] hence $OO_1O_2Q$ is cyclic. However, \[OO_1=O_2P=O_2Q,\] so $OO_1O_2Q$ is an isosceles trapezoid. Since $\overline{O_1O_2}\perp\overline{XY}$ , $\overline{OQ}\perp\overline{XY}$ , so $Q$ is the midpoint of $\overline{XY}$ .
By Power of a Point, $PX\cdot PY=PA\cdot PB=15$ . Since $PX+PY=XY=11$ and $XQ=11/2$ , \[XP=\frac{11-\sqrt{61}}2\implies PQ=XQ-XP=\frac{\sqrt{61}}2\implies PQ^2=\frac{61}4,\] and the requested sum is $61+4=\boxed{065}$ .
(Solution by TheUltimate123)
### Note
One may solve for $PX$ first using PoAP, $PX = \frac{11}{2} - \frac{\sqrt{61}}{2}$ . Then, notice that $PQ^2$ is rational but $PX^2$ is not, also $PX = \frac{XY}{2} - \frac{\sqrt{61}}{2}$ . The most likely explanation for this is that $Q$ is the midpoint of $XY$ , so that $XQ = \frac{11}{2}$ and $PQ=\frac{\sqrt{61}}{2}$ . Then our answer is $m+n=61+4=\boxed{065}$ . One can rigorously prove this using the methods above

## Solution 2
Let the tangents to $\omega$ at $A$ and $B$ intersect at $R$ . Then, since $RA^2=RB^2$ , $R$ lies on the radical axis of $\omega_1$ and $\omega_2$ , which is $\overline{PQ}$ . It follows that \[-1=(A,B;X,Y)\stackrel{A}{=}(R,P;X,Y).\] Let $Q'$ denote the midpoint of $\overline{XY}$ . By the Midpoint of Harmonic Bundles Lemma(EGMO 9.17), \[RP\cdot RQ'=RX\cdot RY=RA^2=RP\cdot RQ,\] whence $Q=Q'$ . Like above, $XP=\tfrac{11-\sqrt{61}}2$ . Since $XQ=\tfrac{11}2$ , we establish that $PQ=\tfrac{\sqrt{61}}2$ , from which $PQ^2=\tfrac{61}4$ , and the requested sum is $61+4=\boxed{065}$ .
(Solution by TheUltimate123)

## Solution 3
Firstly we need to notice that $Q$ is the middle point of $XY$ . Assume the center of circle $w, w_1, w_2$ are $O, O_1, O_2$ , respectively. Then $A, O_1, O$ are collinear and $O, O_2, B$ are collinear. Link $O_1P, O_2P, O_1Q, O_2Q$ . Notice that, $\angle B=\angle A=\angle APO_1=\angle BPO_2$ . As a result, $PO_1\parallel O_2O$ and $OO_1\parallel O_2P$ . So we have parallelogram $PO_2OO_1$ . So $\angle O_2PO_1=\angle O$ Notice that, $O_1O_2\bot PQ$ and $O_1O_2$ divides $PQ$ into two equal length pieces, So we have $\angle O_2QO_1=\angle O_2PO_1=\angle O$ . As a result, $O_2, Q, O, O_1,$ lie on one circle. So $\angle OQO_1=\angle OO_2O_1=\angle O_2O_1P$ . Notice that since $\angle O_1PQ+\angle O_2O_1P=90^{\circ}$ , we have $\angle OQP=\angle OQO_1 + \angle O_1QP = \angle O_2O_1P + O_1PQ=90^{\circ}$ . As a result, $OQ\bot PQ$ . So $Q$ is the middle point of $XY$ .
Back to our problem. Assume $XP=x$ , $PY=y$ and $x<y$ . Then we have $AP\cdot PB=XP\cdot PY$ , that is, $xy=15$ . Also, $XP+PY=x+y=XY=11$ . Solve these above, we have $x=\frac{11-\sqrt{61}}{2}=XP$ . As a result, we have $PQ=XQ-XP=\frac{11}{2}-\frac{11-\sqrt{61}}{2}=\frac{\sqrt{61}}{2}$ . So, we have $PQ^2=\frac{61}{4}$ . As a result, our answer is $m+n=61+4=\boxed{065}$ .
Solution By BladeRunnerAUG (Fanyuchen20020715). Edited by bgn4493.

## Solution 4
Note that the tangents to the circles at $A$ and $B$ intersect at a point $Z$ on $XY$ by radical axis theorem. Since $\angle ZAB = \angle ZQA$ and $\angle ZBA = \angle ZQB$ , we have \[\angle AZB + \angle AQB = \angle AZB + \angle ZAB + \angle ZBA = 180^{\circ},\] so $ZAQB$ is cyclic.
But if $O$ is the center of $\omega$ , clearly $ZAOB$ is cyclic with diameter $ZO$ , so $\angle ZQO = 90^{\circ}$ implies that $Q$ is the midpoint of $XY$ . Then, by power of point $P$ , \[PY \cdot PX = PA \cdot PB = 15,\] whereas it is given that $PY+PX = 11$ . Thus \[PY, PX \in \left\{\tfrac 12 (11 \pm \sqrt{61})\right\}\] so $PQ = \frac{\sqrt{61}}{2}$ , i.e. $PQ^2 = \frac{61}{4}$ and the answer is $61+4 = \boxed{065}$ .

## Solution 5
Connect $AQ,QB$ , since $\angle{AO_1P}=\angle{AOB}=\angle{BO_2P}$ , so $\angle{AQP}=\frac{\angle{AO_1P}}{2}=\angle{BQP}=\frac{\angle{BO_2P}}{2}, \angle{AQB}=\angle{AOB}$ then, so $A,O,Q,B$ are concyclic
We let $\angle{AO_1P}=\angle{AOB}=\angle{BO_2P}=2\alpha$ , it is clear that $\angle{BQP}=\alpha, \angle{O_1AP}=90^{\circ}-\alpha$ , which leads to the conclusion $OQ\bot XY$ which tells $Q$ is the midpoint of $XY$
Then it is clear, $XP\cdot PY=15, XP=\frac{11-\sqrt{61}}{2}, PQ=\frac{11}{2}-\frac{11-\sqrt{61}}{2}=\frac{\sqrt{61}}{2}$ , the answer is $\boxed{065}$
~bluesoul

## Solution 6(lazy)
[asy] size(8cm); pair O, A, B, P, O1, O2, Q, X, Y; O=(0, 0); A=dir(140); B=dir(40); P=(3A+5B)/8; O1=extension((A+P)/2, (A+P)/2+(0, 1), A, O); O2=extension((B+P)/2, (B+P)/2+(0, 1), B, O); Q=intersectionpoints(circle(O1, length(A-O1)), circle(O2, length(B-O2)))[1]; X=intersectionpoint(P -- (P+(P-Q)*100), circle(O, 1)); Y=intersectionpoint(Q -- (Q+(Q-P)*100), circle(O, 1)); draw(circle(O, 1)); draw(circle(O1, length(A-O1))); draw(circle(O2, length(B-O2))); draw(A -- B,red); draw(X -- Y,green); dot("$A$", A, A); dot("$B$", B, B); dot("$P$", P, dir(70),blue); dot("$Q$", Q, dir(200)); dot("$X$", X, X); dot("$Y$", Y, Y); label("$3$", (A+P)/2, N, red); label("$5$", (B+P)/2, N, red); draw(brace(X,Y)); label("$11$",brace(X,Y),dir(20)); [/asy] $PX \cdot PY=AP \cdot PB=5 \cdot 3=15$ by power of a point. Also, $PX+PY=XY=11$ , so $PX$ and $PY$ are solutions to the quadratic $x^2-11x+15=0$ so $PX$ and $PY$ is $\frac{11\pm\sqrt{61}}{2}$ in some order. Now, because we want $PQ^2$ and it is known to be rational, we can guess that $PQ$ is irrational or the problem would simply ask for $PQ$ . We can also figure out that since $PQ^2$ is rational, $PQ$ is $\sqrt{\text{[something]}}$ . $PQ=QX-PX$ , and chances are low that $QX$ is some number with a square root plus or minus $\frac{\sqrt{61}}{2}$ to cancel out the $\frac{\sqrt{61}}{2}$ in $PX$ , so one can see that $PQ^2$ is most likely to be $\left(\frac{\sqrt{61}}{2}\right)^2=\frac{61}{4}$ , and our answer is $61+4=\boxed{065}$
Note : If our answer is correct, then $QX=\frac{11}{2}$ , which made $Q$ the midpoint of $XY$ , a feature that occurs often in AIME problems, so that again made our answer probable. Midpoints have many properties and there is a lot of ways to show if a point is the midpoint of a segment. Even if the answer is wrong, it's still the same as leaving it blank and 065 is a good guess. ~ Ddk001

## Solution 7
We will show that $Q$ is the midpoint of $XY.$ To do this, let $Q^{\prime}$ be the altitude from $O$ to $XY$ or, equivalently, to $PQ.$ Notice that $O_{1}00_{2}P$ is a parallelogram. Thus, the height from $O$ to $O_{1}O_{2}$ is equal to the height from $P$ to $O_{1}O_{2}.$ Say that the line through $P$ perpendicular to $O_{1}O_{2}$ intersects $O_{1}O_{2}$ at $H.$ Then, $PQ$ is perpendicular to $O_{1}O_{2},$ so $H$ is on $PQ.$ Now, we have that the altitude from $O$ to $O_{1}O_{2}$ is equal to the altitude from $Q^{\prime}$ to $O_{1}O_{2}$ (since $OQ^{\prime} \parallel O_{1}O_{2}$ ). However, the altitude from $Q^{\prime}$ to $O_{1}O_{2}$ is just $Q^{\prime}H.$ Also, the altitude from $P$ to $O_{1}O_{2}$ is $PH$ , so $PH = Q^{\prime}H.$ Thus, $O_{1}O_{2}$ bisects $PQ^{\prime}.$ However, this is true for $Q,$ too, so $Q = Q^{\prime},$ and we are done. Now, by PoP, we have \[AP \cdot BP = XP \cdot YP = 15.\] Also, we have $XY = XP+YP = 11,$ so $XP = \frac{11 \pm \sqrt{61}}{2}$ . Notice that $XQ = \frac{XY}{2} = \frac{11}{2},$ so $PQ = \frac{\sqrt{61}}{2},$ giving us our answer of $\boxed{065}.$

## Solution 8
Like Solution 7, let $Q'$ be the altitude from $O$ to $XY$ . And, let $M$ be the intersection of $O_1O_2$ and $PQ$ . Construct $P'$ on line $AO$ such that $PP' \parallel O_2O_1$ . First, because of isosceles triangles $OAB$ , $O_1AP$ , and $O_2BP$ , we have $\angle{OAP} = \angle{OBA} = \angle{APO_1} = \angle{BPO_2}$ , which means $OO_1PO_2$ is a parallelogram. So, $O_2P = OO_1$ . It is also clear that $PP'O_1O_2$ is a parallelogram by virtue of our definition. Thus, $O_2P = O_1P' = OO_1$ . Since $OQ' \parallel O_1O_2 \parallel P'P$ (because of the right angles), $\frac{Q'M}{MP} = \frac{OO_1}{O_1P'} = 1 \implies Q'M = MP$ . And, because $QM = MP$ , $Q = Q'$ . From Power of a Point on $P$ , we have $XP(11-XP) = 15$ , giving us $XP = \frac{11 - \sqrt{61}}{2}$ . Since $OQ$ is perpendicular to $XY$ , $Q$ is the midpoint of $XY$ , so $XQ = \frac{11}{2}$ . Thus, $PQ = \frac{11}{2} - \frac{11 - \sqrt{61}}{2} = \frac{\sqrt{61}}{2} \implies {PQ}^2 = \frac{61}{4}$ . Therefore, our answer is $\boxed{65}$ .
~ CrazyVideoGamez
$\newline$

## Video Solution 1 by StressedPineapple
https://youtube.com/watch?v=OXxtawwIw6Q

## Video Solution 2 by Mr. Math
https://www.youtube.com/watch?v=X_CSRwUh0Rc
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .