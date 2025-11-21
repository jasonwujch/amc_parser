# 2017 AIME I Problem 15

## Problem

The area of the smallest equilateral triangle with one vertex on each of the sides of the right triangle with side lengths $2\sqrt{3},~5,$ and $\sqrt{37},$ as shown, is $\frac{m\sqrt{p}}{n},$ where $m,~n,$ and $p$ are positive integers, $m$ and $n$ are relatively prime, and $p$ is not divisible by the square of any prime. Find $m+n+p.$

[asy] size(5cm); pair C=(0,0),B=(0,2*sqrt(3)),A=(5,0); real t = .385, s = 3.5*t-1; pair R = A*t+B*(1-t), P=B*s; pair Q = dir(-60) * (R-P) + P; fill(P--Q--R--cycle,gray); draw(A--B--C--A^^P--Q--R--P); dot(A--B--C--P--Q--R); [/asy]

## Solution 1
Lemma: If $x,y$ satisfy $px+qy=1$ , then the minimal value of $\sqrt{x^2+y^2}$ is $\frac{1}{\sqrt{p^2+q^2}}$ .
Proof: Recall that the distance between the point $(x_0,y_0)$ and the line $px+qy+r = 0$ is given by $\frac{|px_0+qy_0+r|}{\sqrt{p^2+q^2}}$ . In particular, the distance between the origin and any point $(x,y)$ on the line $px+qy=1$ is at least $\frac{1}{\sqrt{p^2+q^2}}$ .
---
Let the vertices of the right triangle be $(0,0),(5,0),(0,2\sqrt{3}),$ and let $(a,0),(0,b)$ be the two vertices of the equilateral triangle on the legs of the right triangle. Then, the third vertex of the equilateral triangle is $\left(\frac{a+b\sqrt{3}}{2},\frac{a\sqrt{3}+b}{2}\right)$ . This point must lie on the hypotenuse $\frac{x}{5} + \frac{y}{2\sqrt{3}} = 1$ , i.e. $a,b$ must satisfy \[\frac{a+b\sqrt{3}}{10}+\frac{a\sqrt{3}+b}{4\sqrt{3}} = 1,\] which can be simplified to \[\frac{7}{20}a + \frac{11\sqrt{3}}{60}b = 1.\]
By the lemma, the minimal value of $\sqrt{a^2+b^2}$ is \[\frac{1}{\sqrt{\left(\frac{7}{20}\right)^2 + \left(\frac{11\sqrt{3}}{60}\right)^2}} = \frac{10\sqrt{3}}{\sqrt{67}},\] so the minimal area of the equilateral triangle is \[\frac{\sqrt{3}}{4} \cdot \left(\frac{10\sqrt{3}}{\sqrt{67}}\right)^2 = \frac{\sqrt{3}}{4} \cdot \frac{300}{67} = \frac{75\sqrt{3}}{67},\] and hence the answer is $75+3+67=\boxed{145}$ .

## Solution 2
Let $AB=2\sqrt{3}, BC=5$ , $D$ lies on $BC$ , $F$ lies on $AB$ and $E$ lies on $AC$
Set $D$ as the origin, $BD=a,BF=b$ , $F$ can be expressed as $-a+bi$ in argand plane, the distance of $CD$ is $5-a$
We know that $(-a+bi)\cdot[\cos(-\frac{\pi}{3})+ i\sin(-\frac{\pi}{3})]=(-\frac{a+\sqrt{3}b}{2}+\frac{\sqrt{3}a+b}{2}i)$ . We know that the slope of $AC$ is $-\frac{2\sqrt{3}}{5}$ , we have that $\frac{5-a-(-\frac{a+\sqrt{3}b}{2})}{(\sqrt{3}a+b)/2}=\frac{5}{2\sqrt{3}}$ , after computation, we have $11b+7\sqrt{3}a=20\sqrt{3}$
Now the rest is easy with C-S inequality, $(a^2+b^2)(147+121)\geq (7\sqrt{3}a+11b)^2, a^2+b^2\geq \frac{300}{67}$ so the smallest area is $\frac{\sqrt{3}}{4}\cdot \frac{300}{67}=\frac{75\sqrt{3}}{67}$ , and the answer is $\boxed{145}$
~bluesoul

## Solution 3
Let $\triangle ABC$ be the right triangle with sides $AB = x$ , $AC = y$ , and $BC = z$ and right angle at $A$ .
Let an equilateral triangle touch $AB$ , $AC$ , and $BC$ at $D$ , $E$ , and $F$ respectively, having side lengths of $c$ .
Now, call $AD$ as $a$ and $AE$ as $b$ . Thus, $DB = x-a$ and $EC = y-b$ .
By Law of Sines on triangles $\triangle DBF$ and $ECF$ ,
$BF = \frac{z(a\sqrt{3}+b)} {2y}$ and $CF = \frac{z(a+b\sqrt{3})} {2x}$ .
Summing,
$BF+CF = \frac{z(a\sqrt{3}+b)} {2y} + \frac{z(a+b\sqrt{3})} {2x} = BC = z$ .
Now substituting $AB = x = 2\sqrt{3}$ , $AC = y = 5$ , and $BC = \sqrt{37}$ and solving, $\frac{7a}{20} + \frac{11b\sqrt{3}}{60} = 1$ .
We seek to minimize $[DEF] = c^2 \frac{\sqrt{3}}{4} = (a^2 + b^2) \frac{\sqrt{3}}{4}$ .
This is equivalent to minimizing $a^2+b^2$ .
Using the lemma from solution 1, we conclude that $\sqrt{a^2+b^2} = \frac{10\sqrt{3}}{\sqrt{67}}$
Thus, $[DEF] = \frac{75\sqrt{3}}{67}$ and our final answer is $\boxed{145}$
- Awsomness2000

## Solution 4 (Trigonometry)
Let $ED = DF = x, AC = 5, \angle BAC = \alpha, \angle CDE = \beta.$
Then $\cot \alpha = \frac {5}{2\sqrt{3}},\angle CDF = \beta - 60^\circ,$ \[\angle AED = \beta - \alpha, CD = x \cos(\beta - 60^\circ).\]
By Law of Sines on triangle $\triangle ADE$ we get \[AD = x \frac {\sin (\beta – \alpha)}{\sin{\alpha}}.\] \[AD + CD = AC \implies\] \[x(\frac {\sin \beta}{\tan{\alpha}} - \cos \beta) +x (\frac {\cos\beta}{2} +\frac{\sin\beta \sqrt{3}}{2}) = AC\] \[\implies \frac{AC}{x} = \sin \beta (\cot \alpha + \frac{\sqrt{3}}{2})- \frac{\cos\beta}{2}\] \[a \sin \beta + b \cos \beta \le \sqrt {a^2+b^2} \implies\] \[\frac{AC}{x} \le \sqrt {\left(\cot \alpha + \frac {\sqrt3}{2}\right)^2 + \left(\frac {1}{2}\right)^2} = \sqrt {\cot^2 \alpha + \sqrt {3} \cot \alpha + 1}\] The smallest area $[DEF]$ is \[\frac {\sqrt {3}}{4} \cdot x_{min}^2 = \frac {\sqrt {3} AC^2}{4 (\cot ^2 \alpha + \sqrt {3} \cot \alpha + 1)} = \frac{75 \sqrt{3}}{67}.\] vladimir.shelomovskii@gmail.com, vvsss
### Note
$a \sin \beta + b \cos \beta \le \sqrt {a^2+b^2}$ follows from Cauchy-Schwarz. \[a \sin \beta + b \cos \beta \le \sqrt{a^2+b^2}\sqrt{\sin^2+\cos^2}=\sqrt{a^2+b^2}\] ~mathboy282

## Solution 5 (Complex numbers)
We will use complex numbers. Set the vertex at the right angle to be the origin, and set the axes so the other two vertices are $5$ and $2\sqrt{3}i$ , respectively. Now let the vertex of the equilateral triangle on the real axis be $a$ and let the vertex of the equilateral triangle on the imaginary axis be $bi$ . Then, the third vertex of the equilateral triangle is given by: \[(bi-a)e^{-\frac{\pi}{3}i}+a=(bi-a)(\frac{1}{2}-\frac{\sqrt{3}}{2}i)+a=(\frac{a}{2}+\frac{b\sqrt{3}}{2})+(\frac{a\sqrt{3}}{2}+\frac{b}{2})i\] .
For this to be on the hypotenuse of the right triangle, we also have the following: \[\frac{\frac{a\sqrt{3}}{2}+\frac{1}{2}}{\frac{a}{2}+\frac{b\sqrt{3}}{2}-5}=-\frac{2\sqrt{3}}{5}\iff 7\sqrt{3}a+11b=20\sqrt{3}\]
Note that the area of the equilateral triangle is given by $\frac{\sqrt{3}(a^2+b^2)}{4}$ , so we seek to minimize $a^2+b^2$ . This can be done by using the Cauchy Schwarz Inequality on the relation we derived above: \[1200=(7\sqrt{3}a+11b)^2\leq ((7\sqrt{3})^2+11^2)(a^2+b^2)\implies a^2+b^2\geq \frac{1200}{268}\]
Thus, the minimum we seek is simply $\frac{\sqrt{3}}{4}\cdot\frac{1200}{268}=\frac{75\sqrt{3}}{67}$ , so the desired answer is $\boxed{145}$ .

## Solution 6
In the complex plane, let the vertices of the triangle be $a = 5,$ $b = 2i \sqrt{3},$ and $c = 0.$ Let $e$ be one of the vertices, where $e$ is real. A point on the line passing through $a = 5$ and $b = 2i \sqrt{3}$ can be expressed in the form \[f = (1 - t) a + tb = 5(1 - t) + 2ti \sqrt{3}.\] We want the third vertex $d$ to lie on the line through $b$ and $c,$ which is the imaginary axis, so its real part is 0. Since the small triangle is equilateral, $d - e = \cos 60^\circ \cdot (f - e),$ or \[d - e = \frac{1 + i \sqrt{3}}{2} \cdot (5(1 - t) - e + 2ti \sqrt{3}).\] Then the real part of $d$ is \[\frac{5(1 - t) - e}{2} - 3t + e = 0.\] Solving for $t$ in terms of $e,$ we find \[t = \frac{e + 5}{11}.\] Then \[f = \frac{5(6 - e)}{11} + \frac{2(e + 5) \sqrt{3}}{11} i,\] so \[f - e = \frac{30 - 16e}{11} + \frac{2(e + 5) \sqrt{3}}{11} i,\] so \begin{align*} |f - e|^2 &= \left( \frac{30 - 16e}{11} \right)^2 + \left( \frac{2(e + 5) \sqrt{3}}{11} \right)^2 \\ &= \frac{268e^2 - 840e + 1200}{121}. \end{align*} This quadratic is minimized when $e = \frac{840}{2 \cdot 268} = \frac{105}{67},$ and the minimum is $\frac{300}{67},$ so the smallest area of the equilateral triangle is \[\frac{\sqrt{3}}{4} \cdot \frac{300}{67} = \boxed{\frac{75 \sqrt{3}}{67}}.\]

## Solution 7
We can use complex numbers. Set the origin at the right angle. Let the point on the real axis be $a$ and the point on the imaginary axis be $bi$ . Then, we see that $(a-bi)\left(\text{cis}\frac{\pi}{3}\right)+bi=(a-bi)\left(\frac{1}{2}+i\frac{\sqrt{3}}{2}\right)+bi=\left(\frac{1}{2}a+\frac{\sqrt{3}}{2}b\right)+i\left(\frac{\sqrt{3}}{2}a+\frac{1}{2}b\right).$ Now we switch back to Cartesian coordinates. The equation of the hypotenuse is $y=-\frac{2\sqrt{3}}{5}x+2\sqrt{3}.$ This means that the point $\left(\frac{1}{2}a+\frac{\sqrt{3}}{2}b,\frac{\sqrt{3}}{2}a+\frac{1}{2}b\right)$ is on the line. Plugging the numbers in, we have $\frac{\sqrt{3}}{2}a+\frac{1}{2}b=-\frac{\sqrt{3}}{5}a-\frac{3}{5}b+2\sqrt{3} \implies 7\sqrt{3}a+11b=20\sqrt{3}.$ Now, we note that the side length of the equilateral triangle is $a^2+b^2$ so it suffices to minimize that. By Cauchy-Schwarz, we have $(a^2+b^2)(147+121)\geq(7\sqrt{3}a+11b)^2 \implies (a^2+b^2)\geq\frac{300}{67}.$ Thus, the area of the smallest triangle is $\frac{300}{67}\cdot\frac{\sqrt{3}}{4}=\frac{75\sqrt{3}}{67}$ so our desired answer is $\boxed{145}$ .
(Solution by Pleaseletmetwin, but not added to the Wiki by Pleaseletmetwin)

## Solution 8
Employ the same complex bash as in Solution 5, but instead note that minimizing $x^2+y^2$ is the same as minimizing the distance from 0,0 to x,y, since they are the same quantity. We use point to plane instead, which gives you the required distance.

## Solution 9 (Non Analytic)
Let $S$ be the triangle with side lengths $2\sqrt{3},~5,$ and $\sqrt{37}$ .
We will think about this problem backwards, by constructing a triangle as large as possible (We will call it $T$ , for convenience) which is similar to $S$ with vertices outside of a unit equilateral triangle $\triangle ABC$ , such that each vertex of the equilateral triangle lies on a side of $T$ . After we find the side lengths of $T$ , we will use ratios to trace back towards the original problem.
First of all, let $\theta = 90^{\circ}$ , $\alpha = \arctan\left(\frac{2\sqrt{3}}{5}\right)$ , and $\beta = \arctan\left(\frac{5}{2\sqrt{3}}\right)$ (These three angles are simply the angles of triangle $S$ ; out of these three angles, $\alpha$ is the smallest angle, and $\theta$ is the largest angle). Then let us consider a point $P$ inside $\triangle ABC$ such that $\angle APB = 180^{\circ} - \theta$ , $\angle BPC = 180^{\circ} - \alpha$ , and $\angle APC = 180^{\circ} - \beta$ . Construct the circumcircles $\omega_{AB}, ~\omega_{BC},$ and $\omega_{AC}$ of triangles $APB, ~BPC,$ and $APC$ respectively.
From here, we will prove the lemma that if we choose points $X$ , $Y$ , and $Z$ on circumcircles $\omega_{AB}, ~\omega_{BC},$ and $\omega_{AC}$ respectively such that $X$ , $B$ , and $Y$ are collinear and $Y$ , $C$ , and $Z$ are collinear, then $Z$ , $A$ , and $X$ must be collinear. First of all, if we let $\angle PAX = m$ , then $\angle PBX = 180^{\circ} - m$ (by the properties of cyclic quadrilaterals), $\angle PBY = m$ (by adjacent angles), $\angle PCY = 180^{\circ} - m$ (by cyclic quadrilaterals), $\angle PCZ = m$ (adjacent angles), and $\angle PAZ = 180^{\circ} - m$ (cyclic quadrilaterals). Since $\angle PAX$ and $\angle PAZ$ are supplementary, $Z$ , $A$ , and $X$ are collinear as desired. Hence, $\triangle XYZ$ has an inscribed equilateral triangle $ABC$ .
In addition, now we know that all triangles $XYZ$ (as described above) must be similar to triangle $S$ , as $\angle AXB = \theta$ and $\angle BYC = \alpha$ , so we have developed $AA$ similarity between the two triangles. Thus, $\triangle XYZ$ is the triangle similar to $S$ which we were desiring. Our goal now is to maximize the length of $XY$ , in order to maximize the area of $XYZ$ , to achieve our original goal.
Note that, all triangles $PYX$ are similar to each other if $Y$ , $B$ , and $X$ are collinear. This is because $\angle PYB$ is constant, and $\angle PXB$ is also a constant value. Then we have $AA$ similarity between this set of triangles. To maximize $XY$ , we can instead maximize $PY$ , which is simply the diameter of $\omega_{BC}$ . From there, we can determine that $\angle PBY = 90^{\circ}$ , and with similar logic, $PA$ , $PB$ , and $PC$ are perpendicular to $ZX$ , $XY$ , and $YZ$ respectively We have found our desired largest possible triangle $T$ .
All we have to do now is to calculate $YZ$ , and use ratios from similar triangles to determine the side length of the equilateral triangle inscribed within $S$ . First of all, we will prove that $\angle ZPY = \angle ACB + \angle AXB$ . By the properties of cyclic quadrilaterals, $\angle AXB = \angle PAB + \angle PBA$ , which means that $\angle ACB + \angle AXB = 180^{\circ} - \angle PAC - \angle PBC$ . Now we will show that $\angle ZPY = 180^{\circ} - \angle PAC - \angle PBC$ . Note that, by cyclic quadrilaterals, $\angle YZP = \angle PAC$ and $\angle ZYP = \angle PBC$ . Hence, $\angle ZPY = 180^{\circ} - \angle PAC - \angle PBC$ (since $\angle ZPY + \angle YZP + \angle ZYP = 180^{\circ}$ ), proving the aforementioned claim. Then, since $\angle ACB = 60^{\circ}$ and $\angle AXB = \theta = 90^{\circ}$ , $\angle ZPY = 150^{\circ}$ .
Now we calculate $PY$ and $PZ$ , which are simply the diameters of circumcircles $\omega_{BC}$ and $\omega_{AC}$ , respectively. By the extended law of sines, $PY = \frac{BC}{\sin{BPC}} = \frac{\sqrt{37}}{2\sqrt{3}}$ and $PZ = \frac{CA}{\sin{CPA}} = \frac{\sqrt{37}}{5}$ .
We can now solve for $ZY$ with the law of cosines:
\[(ZY)^2 = \frac{37}{25} + \frac{37}{12} - \left(\frac{37}{5\sqrt{3}}\right)\left(-\frac{\sqrt{3}}{2}\right)\]
\[(ZY)^2 = \frac{37}{25} + \frac{37}{12} + \frac{37}{10}\]
\[(ZY)^2 = \frac{37 \cdot 67}{300}\]
\[ZY = \sqrt{37} \cdot \frac{\sqrt{67}}{10\sqrt{3}}\]
Now we will apply this discovery towards our original triangle $S$ . Since the ratio between $ZY$ and the hypotenuse of $S$ is $\frac{\sqrt{67}}{10\sqrt{3}}$ , the side length of the equilateral triangle inscribed within $S$ must be $\frac{10\sqrt{3}}{\sqrt{67}}$ (as $S$ is simply as scaled version of $XYZ$ , and thus their corresponding inscribed equilateral triangles must be scaled by the same factor). Then the area of the equilateral triangle inscribed within $S$ is $\frac{75\sqrt{3}}{67}$ , implying that the answer is $\boxed{145}$ .
-Solution by TheBoomBox77

## Solution 10
Let the right triangle's lower-left point be at $O(0,0)$ . Notice the 2 other points will determine a unique equilateral triangle. Let 2 points be on the $x$ -axis ( $B$ ) and the $y$ -axis ( $A$ ) and label them $(b, 0)$ and $(0, a)$ respectively. The third point ( $C$ ) will then be located on the hypotenuse. We proceed to find the third point's coordinates in terms of $a$ and $b$ .
1. Find the slope of $AB$ and take the negative reciprocal of it to find the slope of the line containing $C$ . Notice the line contains the midpoint of $AB$ so we can then have an equation of the line.
2. Let $AB=x.$ For $ABC$ to be an equilateral triangle, the altitude from $C$ to $AB$ must be $\frac{x\sqrt{3}}{2}.$
We then have two equations and two variables, so we can solve for $C$ 's coordinates.
We can find $C(\frac{a+b\sqrt{3}}{2}), (\frac{b+a\sqrt{3}}{2}).$ Also, note that $C$ must be on the hypotenuse of the triangle $\frac{x}{5}+\frac{y}{2\sqrt{3}}=1.$ We can plug in $x$ and $y$ as the coordinates of $C$ , which simplifies to
\[11b+7\sqrt{3}a=20\sqrt{3}.\]
We aim to minimize the side length of the triangle, which is $\sqrt{a^2+b^2}.$ Applying the Cauchy inequality gives us
\[(a^2+b^2)(7\sqrt{3}^2+11^2)\geq (11b+7\sqrt3a)^2 = 1200\]
From which we obtain $\sqrt{a^2+b^2} \geq \sqrt{\frac{300}{67}}.$ Thus, the area of the triangle = $\frac{75\sqrt{3}}{67}$ which leads to the answer $75+3+67=\boxed{145}.$
-hi_im_bob

## Solution 11
The general solution to the minimal area is as following:
\[A_{min}={{\sqrt{3}m^2n^2}\over{4(m^2+n^2+\sqrt{3}mn)}},\]
where $m$ and $n$ are the two legs of the right triangle. In this particular case $m=5$ and $n=2\sqrt{3}$ . When we plug in these two values, we recover the correct answer of $\frac{75\sqrt3}{67}$ .
The contour of the minimal area $A_{min}$ is plotted as a function of leg lengths $m$ and $n$ , as shown on the right hand side.
### Note
The proof of the formula can be done in a similar fashion as Solution 4, where instead of using specific values, we define variables, $m$ and $n$ in this case, as per the formula.

## Solution 12 (Geometry)
Let $ED = DF = x, AC = 5, \angle BAC = \alpha.$ Then $\cot \alpha = \frac {5}{2\sqrt{3}}.$
$P -$ midpoint $DE, M -$ midpoint $FE, Q -$ circumcenter $\triangle AE.$ \[\angle EQM = \alpha, \angle MQE = 90^\circ - \alpha,\] \[\angle PEQ = \angle MQE + 60^\circ = 150^\circ - \alpha.\] \[PE = \frac {x}{2}, QE = \frac {x}{2 \sin \alpha} \implies\] \[PQ^2 = PE^2 + QE^2 - 2 PE \cdot QE \cdot \cos(150^\circ - \alpha),\] \[PQ^2 = \frac{x^2}{4} (\cot ^2 \alpha + \sqrt {3} \cot \alpha + 1) .\] Points $P$ and $Q$ lies on bisectors of $CE$ and $AE,$ so $PQ \ge \frac {AC}{2}.$
The smallest area $[DEF]$ is \[\frac {\sqrt {3}}{4} \cdot x_{min}^2 = \frac {\sqrt {3} AC^2}{4 (\cot ^2 \alpha + \sqrt {3} \cot \alpha + 1)} = \frac{75 \sqrt{3}}{67}.\] vladimir.shelomovskii@gmail.com, vvsss

## Solution 13 (Kinematics+Geometry)
Let $ED = DF = x, AC = 5, \angle BAC = \alpha.$ Then $\cot \alpha = \frac {5}{2\sqrt{3}}.$
Let the required triangle with minimal sides $DEF$ be constructed.
Let us vary its position in an acceptable way, that is, we will perform a movement in which the vertices of the $\triangle DEF$ remain on the sides of the $\triangle ABC.$ Any motion of a solid plane figure can be considered as rotation around some point, the center of rotation. The speed of movement of any point is perpendicular to the segment from the center of rotation to this point. With an acceptable variation, the velocities of the vertices of the $\triangle DEF$ are directed along the sides $\triangle ABC.$ Consequently, there is a point $X$ located at the intersection of perpendiculars to the sides of $\triangle ABC,$ around which $\triangle DEF$ rotates. The bases of the perpendiculars dropped from $X$ to the sides of $\triangle ABC$ form a regular $\triangle DEF.$
Therefore $X$ is the first isodynamic point of $\triangle ABC.$
It is known that $\angle AXB = \angle ACB + 60^\circ = 150^\circ.$
The points $A, F, X,$ and $E$ are concyclic, $AX$ is the diameter, so $AX = \frac {x}{\sin \alpha}.$ Similarly, $BX = \frac {x}{\cos \alpha}.$ \[AX^2 + BX^2 - 2 AX BX \cos 150^\circ = AB^2, AC = AB \cos \alpha \implies\] \[AC^2 = x^2 \cdot (\cot ^2 \alpha + \sqrt {3} \cot \alpha + 1).\] The smallest area $[DEF]$ is \[\frac {\sqrt {3}}{4} \cdot x_{min}^2 = \frac {\sqrt {3} AC^2}{4 (\cot ^2 \alpha + \sqrt {3} \cot \alpha + 1)} = \frac{75 \sqrt{3}}{67}.\] vladimir.shelomovskii@gmail.com, vvsss

## Solution 14 (Fastest Trig)
Let the right triangle be $\triangle ABC$ with $BC=2\sqrt{3}$ , $AC=5$ , and $AB=\sqrt{37}$ , and let the equilateral be $\triangle DEF$ with $D, E, F$ on $AC, AB, BC$ respectively. Call its side length $x$ . Let the foot from $E$ to $BC$ be $H$ , and let $\angle EFH=\theta$ . Since $\angle EFD=60^{\circ}$ , $\angle DFC=120^{\circ}-\theta$ . We get $FC=x\cos(120^{\circ}-\theta)$ and $HF=x\cos\theta$ . Meanwhile, since $EH =x\sin\theta$ and $\triangle EBC \sim \triangle ABC$ , $BH=\frac{2\sqrt{3}}{5} x\sin\theta$ . We have
\[2\sqrt{3}=BC=BH+HF+FC=\frac{2\sqrt{3}}{5}x\sin\theta + x\cos\theta +x\cos\left(120^{\circ}-\theta\right)\]
\[\implies 2\sqrt{3}=x\left(\frac{2\sqrt{3}}{5}\sin\theta+\cos\theta-\frac{1}{2}\cos\theta+\frac{\sqrt{3}}{2}\sin\theta\right)\]
\[\implies x=\frac{2\sqrt{3}}{\frac{9\sqrt{3}}{10}\sin\theta+\frac{1}{2}\cos\theta}.\]
\[\implies [\triangle DEF]=\frac{\sqrt{3}}{4}x^2=\frac{\sqrt{3}}{4}\cdot \frac{12}{\left(\frac{9\sqrt{3}}{10}\sin\theta+\frac{1}{2}\cos\theta\right)^2}=\frac{3\sqrt{3}}{\left(\frac{9\sqrt{3}}{10}\sin\theta+\frac{1}{2}\cos\theta \right)^2}\]
By Cauchy-Schwarz, \[\left(\frac{9\sqrt{3}}{10}\sin\theta+\frac{1}{2}\cos\theta \right)^2 \le \left(\cos^2\theta+\sin^2\theta\right)\left(\left(\frac{9\sqrt{3}}{10}\right)^2+\left(\frac{1}{2}\right)^2\right)=\frac{67}{25}\]
\[\implies [\triangle DEF] \ge \frac{3\sqrt{3}}{\frac{67}{25}}=\frac{75\sqrt{3}}{67}.\]
The requested sum is $75+3+67=\boxed{145}$ .
~bomberdoodles
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .