# 2009 AIME II Problem 15

## Problem

Let $\overline{MN}$ be a diameter of a circle with diameter 1. Let $A$ and $B$ be points on one of the semicircular arcs determined by $\overline{MN}$ such that $A$ is the midpoint of the semicircle and $MB=\frac{3}5$ . Point $C$ lies on the other semicircular arc. Let $d$ be the length of the line segment whose endpoints are the intersections of diameter $\overline{MN}$ with chords $\overline{AC}$ and $\overline{BC}$ . The largest possible value of $d$ can be written in the form $r-s\sqrt{t}$ , where $r, s$ and $t$ are positive integers and $t$ is not divisible by the square of any prime. Find $r+s+t$ .

## Solutions

## Solution 1 (Quick Calculus)
Let $V = \overline{NM} \cap \overline{AC}$ and $W = \overline{NM} \cap \overline{BC}$ . Further more let $\angle NMC = \alpha$ and $\angle MNC = 90^\circ - \alpha$ . Angle chasing reveals $\angle NBC = \angle NAC = \alpha$ and $\angle MBC = \angle MAC = 90^\circ - \alpha$ . Additionally $NB = \frac{4}{5}$ and $AN = AM$ by the Pythagorean Theorem.
By the Angle Bisector Formula, \[\frac{NV}{MV} = \frac{\sin (\alpha)}{\sin (90^\circ - \alpha)} = \tan (\alpha)\] \[\frac{MW}{NW} = \frac{3\sin (90^\circ - \alpha)}{4\sin (\alpha)} = \frac{3}{4} \cot (\alpha)\]
As $NV + MV =MW + NW = 1$ we compute $NW = \frac{1}{1+\frac{3}{4}\cot(\alpha)}$ and $MV = \frac{1}{1+\tan (\alpha)}$ , and finally $VW = NW + MV - 1 = \frac{1}{1+\frac{3}{4}\cot(\alpha)} + \frac{1}{1+\tan (\alpha)} - 1$ . Taking the derivative of $VW$ with respect to $\alpha$ , we arrive at \[VW' = \frac{7\cos^2 (\alpha) - 4}{(\sin(\alpha) + \cos(\alpha))^2(4\sin(\alpha)+3\cos(\alpha))^2}\] Clearly the maximum occurs when $\alpha = \cos^{-1}\left(\frac{2}{\sqrt{7}}\right)$ . Plugging this back in, using the fact that $\tan(\cos^{-1}(x)) = \frac{\sqrt{1-x^2}}{x}$ and $\cot(\cos^{-1}(x)) = \frac{x}{\sqrt{1-x^2}}$ , we get
$VW = 7 - 4\sqrt{3}$ with $7 + 4 + 3 = \boxed{014}$
~always_correct

## Solution 2 (Projective)
Since $MA = \frac{\sqrt{2}}{2} \approx 0.707 > \frac{3}{5}$ , point $B$ lies between $M$ and $A$ on the semicircular arc. We will first compute the length of $\overline{AB}$ . By the law of cosines, $\cos \angle MOB = \frac{-(3/5)^2 + 2(1/2)^2}{2(1/2)^2} = \frac{7}{25}$ , so $\cos \angle AOB = \sin \angle MOB = \frac{24}{25}$ . Then $AB^2 = 2\left(\frac{1}{2}\right)^2 - 2\left(\frac{1}{2}\right)^2 \cdot \frac{24}{25} = \frac{1}{50}$ , so $AB = \frac{1}{5\sqrt{2}}$ .
Let $P = AC \cap MN$ and $Q = BC \cap MN$ , and let $MQ = x$ , $PQ = d$ , $PN = y$ . Note that \[(M, P; Q, N) \stackrel{C}{=} (M, A; B, N),\] that is, \[\frac{QP}{QM} \div \frac{NP}{NM} = \frac{BA}{BM} \div \frac{NA}{NM}\] or \[\frac{d}{xy} = \frac{1/(5\sqrt{2})}{(3/5) \cdot (\sqrt{2}/2)} = \frac{1}{3}.\] Hence $d = \frac{1}{3}xy$ , and we also know $d+x+y=1$ . Now AM-GM gives \[\frac{x+y}{2} \ge \sqrt{xy} \implies \frac{1-d}{2} \ge \sqrt{3d}.\] This gives the quadratic inequality $d^2 - 14d + 1 \ge 0$ , which solves as \[d \in \left(-\infty, 7-4\sqrt3\right] \cup \left[7+4\sqrt3, \infty\right).\] But $d \le 1$ , so the greatest possible value of $d$ is $7-4\sqrt3$ . The answer is $7+4+3=\boxed{014}$ .
~MSTang

## Solution 3 (Calculus)
Let $O$ be the center of the circle. Define $\angle{MOC}=t$ , $\angle{BOA}=2a$ , and let $BC$ and $AC$ intersect $MN$ at points $X$ and $Y$ , respectively. We will express the length of $XY$ as a function of $t$ and maximize that function in the interval $[0, \pi]$ .
Let $C'$ be the foot of the perpendicular from $C$ to $MN$ . We compute $XY$ as follows.
(a) By the Extended Law of Sines in triangle $ABC$ , we have
\[CA\]
\[= \sin\angle{ABC}\]
\[= \sin\left(\frac{\widehat{AN} + \widehat{NC}}{2}\right)\]
\[= \sin\left(\frac{\frac{\pi}{2} + (\pi-t)}{2}\right)\]
\[= \sin\left(\frac{3\pi}{4} - \frac{t}{2}\right)\]
\[= \sin\left(\frac{\pi}{4} + \frac{t}{2}\right)\]
(b) Note that $CC' = CO\sin(t) = \left(\frac{1}{2}\right)\sin(t)$ and $AO = \frac{1}{2}$ . Since $CC'Y$ and $AOY$ are similar right triangles, we have $CY/AY = CC'/AO = \sin(t)$ , and hence,
\[CY/CA\]
\[= \frac{CY}{CY + AY}\]
\[= \frac{\sin(t)}{1 + \sin(t)}\]
\[= \frac{\sin(t)}{\sin\left(\frac{\pi}{2}\right) + \sin(t)}\]
\[= \frac{\sin(t)}{2\sin\left(\frac{\pi}{4} + \frac{t}{2}\right)\cos\left(\frac{\pi}{4} - \frac{t}{2}\right)}\]
(c) We have $\angle{XCY} = \frac{\widehat{AB}}{2}=a$ and $\angle{CXY} = \frac{\widehat{MB}+\widehat{CN}}{2} = \frac{\left(\frac{\pi}{2} - 2a\right) + (\pi - t)}{2} = \frac{3\pi}{4} - a - \frac{t}{2}$ , and hence by the Law of Sines,
\[XY/CY\]
\[= \frac{\sin\angle{XCY}}{\sin\angle{CXY}}\]
\[= \frac{\sin(a)}{\sin\left(\frac{3\pi}{4} - a - \frac{t}{2}\right)}\]
\[= \frac{\sin(a)}{\sin\left(\frac{\pi}{4} + a + \frac{t}{2}\right)}\]
(d) Multiplying (a), (b), and (c), we have
\[XY\]
\[= CA * (CY/CA) * (XY/CY)\]
\[= \frac{\sin(t)\sin(a)}{2\cos\left(\frac{\pi}{4} - \frac{t}{2}\right)\sin\left(\frac{\pi}{4} + a + \frac{t}{2}\right)}\]
\[= \frac{\sin(t)\sin(a)}{\sin\left(\frac{\pi}{2} + a\right) + \sin(a + t)}\]
\[= \sin(a)\times\frac{\sin(t)}{\sin(t + a) + \cos(a)}\] ,
which is a function of $t$ (and the constant $a$ ). Differentiating this with respect to $t$ yields
\[\sin(a)\times\frac{\cos(t)(\sin(t + a) + \cos(a)) - \sin(t)\cos(t + a)}{(\sin(t + a) + \cos(a))^2}\] ,
and the numerator of this is
\[\sin(a) \times(\sin(t + a)\cos(t) - \cos(t + a)\sin(t) + \cos(a)\cos(t))\] \[= \sin(a) \times (\sin(a) + \cos(a)\cos(t))\] ,
which vanishes when $\sin(a) + \cos(a)\cos(t) = 0$ . Therefore, the length of $XY$ is maximized when $t=t'$ , where $t'$ is the value in $[0, \pi]$ that satisfies $\cos(t') = -\tan(a)$ .
Note that
\[\frac{1 - \tan(a)}{1 + \tan(a)} = \tan\left(\frac{\pi}{4} - a\right) = \tan((\widehat{MB})/2) = \tan\angle{MNB} = \frac{3}{4}\] ,
so $\tan(a) = \frac{1}{7}$ . We compute
\[\sin(a) = \frac{\sqrt{2}}{10}\]
\[\cos(a) = \frac{7\sqrt{2}}{10}\]
\[\cos(t') = -\tan(a) = -\frac{1}{7}\]
\[\sin(t') = \frac{4\sqrt{3}}{7}\]
\[\sin(t' + a)=\sin(t')\cos(a) + \cos(t')\sin(a) = \frac{28\sqrt{6} - \sqrt{2}}{70}\] ,
so the maximum length of $XY$ is $\sin(a)\times\frac{\sin(t')}{\sin(t' + a) + \cos(a)} = 7 - 4\sqrt{3}$ , and the answer is $7 + 4 + 3 = \boxed{014}$ .

## Solution 4
[asy] unitsize(144); pair A, B, C, M, n; A = (0,1); B = (-7/25, 24/25); C=(1/7,-4*sqrt(3)/7); M = (-1,0); n = (1,0); pair [] D = intersectionpoints(A--C,M--n); pair [] e = intersectionpoints(B--C,M--n); draw(circle((0,0),1)); draw(M--n--B--M--A--n--C--A--B--C--cycle); label("$A$",A,N); label("$B$",B,NNW); label("$M$",M,W); label("$C$",C,SSE); label("$N$",n,E); label("$D$",D[0],SE); label("$E$",e[0],SW); label("$x$",(M+C)/2,SW); label("$y$",(n+C)/2,SE); [/asy]
Suppose $\overline{AC}$ and $\overline{BC}$ intersect $\overline{MN}$ at $D$ and $E$ , respectively, and let $MC = x$ and $NC = y$ . Since $A$ is the midpoint of arc $MN$ , $\overline{CA}$ bisects $\angle MCN$ , and we get \[\frac{MC}{MD} = \frac{NC}{ND}\Rightarrow MD = \frac{x}{x + y}.\] To find $ME$ , we note that $\triangle BNE\sim\triangle MCE$ and $\triangle BME\sim\triangle NCE$ , so
\begin{align*} \frac{BN}{NE} &= \frac{MC}{CE} \\ \frac{ME}{BM} &= \frac{CE}{NC}. \end{align*}
Writing $NE = 1 - ME$ , we can substitute known values and multiply the equations to get
\[\frac{4(ME)}{3 - 3(ME)} = \frac{x}{y}\Rightarrow ME = \frac{3x}{3x + 4y}.\]
The value we wish to maximize is
\begin{align*} DE &= MD - ME \\ &= \frac{x}{x + y} - \frac{3x}{3x + 4y} \\ &= \frac{xy}{3x^2 + 7xy + 4y^2} \\ &= \frac{1}{3(x/y) + 4(y/x) + 7}. \end{align*}
By the AM-GM inequality, $3(x/y) + 4(y/x)\geq 2\sqrt{12} = 4\sqrt{3}$ , so \[DE\leq \frac{1}{4\sqrt{3} + 7} = 7 - 4\sqrt{3},\] giving the answer of $7 + 4 + 3 = \boxed{014}$ . Equality is achieved when $3(x/y) = 4(y/x)$ subject to the condition $x^2 + y^2 = 1$ , which occurs for $x = \frac{2\sqrt{7}}{7}$ and $y = \frac{\sqrt{21}}{7}$ .

## Solution 5 (Projective)
By Pythagoras in $\triangle BMN,$ we get $BN=\dfrac{4}{5}.$
Since cross ratios are preserved upon projecting, note that $(M,Y;X,N)\stackrel{C}{=}(M,B;A,N).$ By definition of a cross ratio, this becomes \[\dfrac{XM}{NY}:\dfrac{NM}{NY}=\dfrac{AM}{AB}:\dfrac{MN}{NB}.\] Let $MY=a,YX=b,XN=c$ such that $a+b+c=1.$ We know that $XM=a+b,XY=b,NM=1,NY=b+c,$ so the LHS becomes $\dfrac{(a+b)(b+c)}{b}.$
In the RHS, we are given every value except for $AB.$ However, Ptolemy's Theorem on $MBAN$ gives $AB\cdot MN+AN\cdot BM=AM\cdot BN\implies AB+\dfrac{3}{5\sqrt{2}}=\dfrac{4}{5\sqrt{2}}\implies AB=\dfrac{1}{5\sqrt{2}}.$ Substituting, we get $\dfrac{(a+b)(b+c)}{b}=4\implies b(a+b+c)+ac=4b, b=\dfrac{ac}{3}$ where we use $a+b+c=1.$
Again using $a+b+c=1,$ we have $a+b+c=1\implies a+\dfrac{ac}{3}+c=1\implies a=3\dfrac{1-c}{c+3}.$ Then $b=\dfrac{ac}{3}=\dfrac{c-c^2}{c+3}.$ Since this is a function in $c,$ we differentiate WRT $c$ to find its maximum. By quotient rule, it suffices to solve \[(-2c+1)(c+3)-(c-c^2)=0 \implies c^2+6c-3,c=-3+2\sqrt{3}.\] Substituting back yields $b=7-4\sqrt{3},$ so $7+4+3=\boxed{014}$ is the answer.
~Generic_Username

## Video Solution
https://youtu.be/4OZyKVD05Zg?si=yg1ndnP_GperfUx6
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.