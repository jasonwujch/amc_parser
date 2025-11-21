# 2010 AIME II Problem 14

## Problem

Triangle $ABC$ with right angle at $C$ , $\angle BAC < 45^\circ$ and $AB = 4$ . Point $P$ on $\overline{AB}$ is chosen such that $\angle APC = 2\angle ACP$ and $CP = 1$ . The ratio $\frac{AP}{BP}$ can be represented in the form $p + q\sqrt{r}$ , where $p$ , $q$ , $r$ are positive integers and $r$ is not divisible by the square of any prime. Find $p+q+r$ .

## Solution 1
Let $O$ be the circumcenter of $ABC$ and let the intersection of $CP$ with the circumcircle be $D$ . It now follows that $\angle{DOA} = 2\angle ACP = \angle{APC} = \angle{DPB}$ . Hence $ODP$ is isosceles and $OD = DP = 2$ .
Denote $E$ the projection of $O$ onto $CD$ . Now $CD = CP + DP = 3$ . By the Pythagorean Theorem , $OE = \sqrt {2^2 - \frac {3^2}{2^2}} = \sqrt {\frac {7}{4}}$ . Now note that $EP = \frac {1}{2}$ . By the Pythagorean Theorem, $OP = \sqrt {\frac {7}{4} + \frac {1^2}{2^2}} = \sqrt {2}$ . Hence it now follows that,
\[\frac {AP}{BP} = \frac {AO + OP}{BO - OP} = \frac {2 + \sqrt {2}}{2 - \sqrt {2}} = 3 + 2\sqrt {2}\]
This gives that the answer is $\boxed{007}$ .
An alternate finish for this problem would be to use Power of a Point on $BA$ and $CD$ . By Power of a Point Theorem, $CP\cdot PD=1\cdot 2=BP\cdot PA$ . Since $BP+PA=4$ , we can solve for $BP$ and $PA$ , giving the same values and answers as above.

## Solution 2
Let $AC=b$ , $BC=a$ by convention. Also, Let $AP=x$ and $BP=y$ . Finally, let $\angle ACP=\theta$ and $\angle APC=2\theta$ .
We are then looking for $\frac{AP}{BP}=\frac{x}{y}$
Now, by arc interceptions and angle chasing we find that $\triangle BPD \sim \triangle CPA$ , and that therefore $BD=yb.$ Then, since $\angle ABD=\theta$ (it intercepts the same arc as $\angle ACD$ ) and $ADB$ is right,
$\cos\theta=\frac{DB}{AB}=\frac{by}{4}$ .
Using law of sines on $APC$ , we additionally find that $\frac{b}{\sin 2\theta}=\frac{x}{\sin\theta}.$ Simplification by the double angle formula $\sin 2\theta=2\sin \theta\cos\theta$ yields
$\cos \theta=\frac{b}{2x}$ .
We equate these expressions for $\cos\theta$ to find that $xy=2$ . Since $x+y=AB=4$ , we have enough information to solve for $x$ and $y$ . We obtain $x,y=2 \pm \sqrt{2}$
Since we know $x>y$ , we use $\frac{x}{y}=\frac{2+\sqrt{2}}{2-\sqrt{2}}=3+2\sqrt{2}$

## Solution 3
Let $\angle{ACP}$ be equal to $x$ . Then by Law of Sines, $PB = -\frac{\cos{x}}{\cos{3x}}$ and $AP = \frac{\sin{x}}{\sin{3x}}$ . We then obtain $\cos{3x} = 4\cos^3{x} - 3\cos{x}$ and $\sin{3x} = 3\sin{x} - 4\sin^3{x}$ . Solving, we determine that $\sin^2{x} = \frac{4 \pm \sqrt{2}}{8}$ . Plugging this in gives that $\frac{AP}{PB} = \frac{\sqrt{2}+1}{\sqrt{2}-1} = 3 + 2\sqrt{2}$ . The answer is $\boxed{007}$ .
(You can derive that $\cos{3x} = 4\cos^3{x} - 3\cos{x},$ and similarly for $\sin{3x},$ by considering the expansion of $(\text{cis}(x))^3,$ equating real parts to $\cos{x}$ and imaginary parts to $\sin{x},$ then substituting with $1-\sin^2{x}$ to finish. ~happypi31415)

## Solution 4 (The quickest and most elegant)
Let $\alpha=\angle{ACP}$ , $\beta=\angle{ABC}$ , and $x=BP$ . By Law of Sines,
$\frac{1}{\sin(\beta)}=\frac{x}{\sin(90-\alpha)}\implies \sin(\beta)=\frac{\cos(\alpha)}{x}$ (1), and
$\frac{4-x}{\sin(\alpha)}=\frac{4\sin(\beta)}{\sin(2\alpha)} \implies 4-x=\frac{2\sin(\beta)}{\cos(\alpha)}$ . (2)
Then, substituting (1) into (2), we get
$4-x=\frac{2}{x} \implies x^2-4x+2=0 \implies x=2-\sqrt{2} \implies \frac{4-x}{x}=\frac{2+\sqrt{2}}{2-\sqrt{2}}=3+2\sqrt{2}$
The answer is $\boxed{007}$ . ~Rowechen

## Solution 5
Let $\angle{ACP}=x$ . Then, $\angle{APC}=2x$ and $\angle{A}=180-3x$ . Let the foot of the angle bisector of $\angle{APC}$ on side $AC$ be $D$ . Then,
$CD=DP$ and $\triangle{DAP}\sim{\triangle{APC}}$ due to the angles of these triangles.
Let $CD=a$ . By the Angle Bisector Theorem, $\frac{1}{a}=\frac{AP}{AD}$ , so $AD=a\cdot{AP}$ . Moreover, since $CD=DP=a$ , by similar triangle ratios, $\frac{AP}{a+a\cdot{AP}}=a$ . Therefore, $AP = \frac{a^2}{1-a^2}$ .
Construct the perpendicular from $D$ to $AP$ and denote it as $F$ . Denote the midpoint of $CP$ as $M$ . Since $PD$ is an angle bisector, $PF$ is congruent to $PM$ , so $PF=\frac{1}{2}$ .
Also, $\triangle{DFA}\sim{\triangle{BCA}}$ . Thus, $\frac{FA}{AC}=\frac{AD}{AB}\Longrightarrow\frac{\frac{a^2}{1-a^2}-\frac{1}{2}}{a+\frac{a^3}{1-a^2}}=\frac{\frac{a^3}{1-a^3}}{4}$ . After some major cancellation, we have $7a^4-8a^2+2=0$ , which is a quadratic in $a^2$ . Thus, $a^2 = \frac{4\pm\sqrt{2}}{7}$ .
Taking the negative root implies $AP<BP$ , contradiction. Thus, we take the positive root to find that $AP=2+\sqrt{2}$ . Thus, $BP=2-\sqrt{2}$ , and our desired ratio is $\frac{2+\sqrt{2}}{2-\sqrt{2}}\implies{3+2\sqrt{2}}$ .
The answer is $\boxed{007}$ .

## Solution 6
Let $O$ be the circumcenter of $\triangle ABC$ . Since $\triangle ABC$ is a right triangle, $O$ will be on $\overline{AB}$ and $\overline{AO} \cong \overline{OB} \cong \overline{OC} = 2$ . Let $\overline{OP} = x$ .
Next, let's do some angle chasing. Label $\angle ACP = \theta^{\circ}$ , and $\angle APC = 2\theta^{\circ}$ . Thus, $\angle PAC = (180-3\theta)^{\circ}$ , and by isosceles triangles, $\angle ACO = (180-3\theta)^{\circ}$ . Then, by angle subtraction, $\angle OCP = (\theta - (180-3\theta))^{\circ} = (4\theta - 180)^{\circ}$ .
Using the Law of Sines: \[\frac{x}{\sin (4\theta-180)^{\circ}}=\frac{2}{\sin (2\theta)^{\circ}}\] Using trigonometric identies, $\sin (4\theta-180)^{\circ}=-\sin (4\theta)^{\circ}=-2\sin (2\theta)^{\circ}\cos (2\theta)^{\circ}$ . Plugging this back into the Law of Sines formula gives us: \[\frac{x}{-2\sin (2\theta)^{\circ}\cos (2\theta)^{\circ}}=\frac{2}{\sin (2\theta)^{\circ}}\]
\[-4\sin (2\theta)^{\circ}\cos (2\theta)^{\circ}=x\sin (2\theta)^{\circ}\] \[-4\cos (2\theta)^{\circ}=x\] \[\cos(2\theta)^{\circ}=\frac{-x}4\]
Next, using the Law of Cosines: \[2^2=1^2+x^2-2\cdot 1\cdot x\cdot \cos (2\theta)^{\circ}\] Substituting $\cos(2\theta)^{\circ}=\frac{-x}4$ gives us: \[2^2=1^2+x^2-2\cdot 1\cdot x\cdot \frac{-x}4\] \[4=1+x^2+\frac{x^2}{2}\]
Solving for x gives $x=\sqrt 2$
Finally: $\frac{\overline{AP}}{\overline{BP}}=\frac{\overline{AO}+\overline{OP}}{\overline{BO}-\overline{OP}}=\frac{2+\sqrt 2}{2-\sqrt 2}=3+2\sqrt2$ , which gives us an answer of $3+2+2=\boxed{007}$ . ~adyj
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .