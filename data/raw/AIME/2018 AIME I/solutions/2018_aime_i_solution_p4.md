# 2018 AIME I Problem 4

## Problem

In $\triangle ABC, AB = AC = 10$ and $BC = 12$ . Point $D$ lies strictly between $A$ and $B$ on $\overline{AB}$ and point $E$ lies strictly between $A$ and $C$ on $\overline{AC}$ so that $AD = DE = EC$ . Then $AD$ can be expressed in the form $\dfrac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution (Easiest Law of Cosines)
We apply Law of Cosines on $\angle A$ twice (one from $\triangle ADE$ and one from $\triangle ABC$ ),
\begin{align*} 12^2 &= 10^2 + 10^2 - 2(10)(10) \cdot \cos{A} \\[5pt] x^2&=x^2+(10-x)^2-2(x)(10-x)\cdot \cos{A} \end{align*}
Solving for $\cos{A}$ in both equations, we get \begin{align*} \cos{A} &= \frac{7}{25} \\ \cos{A} &= \frac{(10-x)^2}{(2)(10-x)(x)} = \frac{10-x}{2x} \end{align*} Setting the two equal, \begin{align*} \frac{10-x}{2x} &= \frac{7}{25} \\[5pt] 250-25x &= 14x \\[5pt] x &= \frac{250}{39}. \end{align*} Therefore, our answer is $\boxed{289}$
Note that this strategy of applying LOC on congruent or supplementary angles is very common. It's also how Stewart's Theorem is derived.
-RootThreeOverTwo, edits by epiconan

## Solution 1 (No Trig)
[asy] import olympiad; import cse5; unitsize(10mm); pathpen=black; dotfactor=3; pair B = (0,0), A = (6,8), C = (12,0), D = intersectionpoints(circle(A,250/39),A--B)[0], E = intersectionpoints(circle(D,250/39),A--C)[0], F=intersectionpoints(circle(B,9.6),A--C)[0], G=A/2+E/2; pair[] dotted = {A,B,C,D,E,F,G}; D(A--B); D(C--B); D(A--C); D(D--E); pathpen=dashed; D(B--F); D(D--G); dot(dotted); label("$A$",A,N); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,NW); label("$E$",E,NE); label("$F$",F,NE); label("$G$",G,NE); label("$x$",A--D,NW); label("$x$",D--E,NW); label("$x$",E--C,NE); draw(rightanglemark(D,G,E)); draw(rightanglemark(B,F,E)); [/asy]
We draw the altitude from $B$ to $\overline{AC}$ to get point $F$ . We notice that the triangle's height from $A$ to $\overline{BC}$ is 8 because it is a $3-4-5$ Right Triangle. To find the length of $\overline{BF}$ , we let $h$ represent $\overline{BF}$ and set up an equation by finding two ways to express the area. The equation is $(8)(12)=(10)(h)$ , which leaves us with $h=9.6$ . We then solve for the length $\overline{AF}$ , which is done through pythagorean theorm and get $\overline{AF}$ = $2.8$ . We can now see that $\triangle AFB$ is a $7-24-25$ Right Triangle. Thus, we set $\overline{AG}$ as $5-$ $\tfrac{x}{2}$ , and yield that $\overline{AD}$ $=$ $($ $5-$ $\tfrac{x}{2}$ $)$ $($ $\tfrac{25}{7}$ $)$ . Now, we can see $x$ = $($ $5-$ $\tfrac{x}{2}$ $)$ $($ $\tfrac{25}{7}$ $)$ . Solving this equation, we yield $39x=250$ , or $x=$ $\tfrac{250}{39}$ . Thus, our final answer is $250+39=\boxed{289}$ .
~bluebacon008
Diagram edited by Afly

## Solution 2 (Easy Similar Triangles)
We start by adding a few points to the diagram. Call $F$ the midpoint of $AE$ , and $G$ the midpoint of $BC$ . (Note that $DF$ and $AG$ are altitudes of their respective triangles). We also call $\angle BAC = \theta$ . Since triangle $ADE$ is isosceles, $\angle AED = \theta$ , and $\angle ADF = \angle EDF = 90 - \theta$ . Since $\angle DEA = \theta$ , $\angle DEC = 180 - \theta$ and $\angle EDC = \angle ECD = \frac{\theta}{2}$ . Since $FDC$ is a right triangle, $\angle FDC = 180 - 90 - \frac{\theta}{2} = \frac{180-m}{2}$ .
Since $\angle BAG = \frac{\theta}{2}$ and $\angle ABG = \frac{180-m}{2}$ , triangles $ABG$ and $CDF$ are similar by Angle-Angle similarity. Using similar triangle ratios, we have $\frac{AG}{BG} = \frac{CF}{DF}$ . $AG = 8$ and $BG = 6$ because there are $2$ $6-8-10$ triangles in the problem. Call $AD = x$ . Then $CE = x$ , $AE = 10-x$ , and $EF = \frac{10-x}{2}$ . Thus $CF = x + \frac{10-x}{2}$ . Our ratio now becomes $\frac{8}{6} = \frac{x+ \frac{10-x}{2}}{DF}$ . Solving for $DF$ gives us $DF = \frac{30+3x}{8}$ . Since $DF$ is a height of the triangle $ADE$ , $FE^2 + DF^2 = x^2$ , or $DF = \sqrt{x^2 - (\frac{10-x}{2})^2}$ . Solving the equation $\frac{30+3x}{8} = \sqrt{x^2 - (\frac{10-x}{2})^2}$ gives us $x = \frac{250}{39}$ , so our answer is $250+39 = \boxed{289}$ .

## Solution 3 (Algebra w/ Law of Cosines)
As in the diagram, let $DE = x$ . Consider point $G$ on the diagram shown above. Our goal is to be able to perform Pythagorean Theorem on $DG, GC$ , and $DC$ . Let $GE = \frac{10-x}{2}$ . Therefore, it is trivial to see that $GC^2 = \Big(x + \frac{10-x}{2}\Big)^2$ (leave everything squared so that it cancels nicely at the end). By Pythagorean Theorem on Triangle $DGE$ , we know that $DG^2 = x^2 - \Big(\frac{10-x}{2}\Big)^2$ . Finally, we apply Law of Cosines on Triangle $DBC$ . We know that $\cos(\angle DBC) = \frac{3}{5}$ . Therefore, we get that $DC^2 = (10-x)^2 + 12^2 - 2(12)(10-x)\frac{3}{5}$ . We can now do our final calculation: \[DG^2 + GC^2 = DC^2 \implies x^2 - \Big(\frac{10-x}{2}\Big)^2 + \Big(x + \frac{10-x}{2}\Big)^2 = (10-x)^2 + 12^2 - 2(12)(10-x)\frac{3}{5}\] After some quick cleaning up, we get \[30x = \frac{72}{5} + 100 \implies x = \frac{250}{39}\] Therefore, our answer is $250+39=\boxed{289}$ .
~awesome1st

## Solution 4 (Coordinates)
Let $B = (0, 0)$ , $C = (12, 0)$ , and $A = (6, 8)$ . Then, let $x$ be in the interval $0<x<2$ and parametrically define $D$ and $E$ as $(6-3x, 8-4x)$ and $(12-3x, 4x)$ respectively. Note that $AD = 5x$ , so $DE = 5x$ . This means that \begin{align*} \sqrt{36+(8x-8)^2} &= 5x\\ 36+(8x-8)^2 &= 25x^2\\ 64x^2-128x+100 &= 25x^2\\ 39x^2-128x+100 &= 0\\ x &= \dfrac{128\pm\sqrt{16384-15600}}{78}\\ x &= \dfrac{100}{78}, 2\\ \end{align*} However, since $2$ is extraneous by definition, $x=\dfrac{50}{39}\implies AD = \dfrac{250}{39}\implies\boxed{289}$ ~ mathwiz0803

## Solution 5 (Law of Cosines)
As shown in the diagram, let $x$ denote $\overline{AD}$ . Let us denote the foot of the altitude of $A$ to $\overline{BC}$ as $F$ . Note that $\overline{AE}$ can be expressed as $10-x$ and $\triangle{ABF}$ is a $6-8-10$ triangle . Therefore, $\sin(\angle{BAF})=\frac{3}{5}$ and $\cos(\angle{BAF})=\frac{4}{5}$ . Before we can proceed with the Law of Cosines, we must determine $\cos(\angle{BAC})=\cos(2\cdot \angle{BAF})=\cos^2(\angle{BAF})-\sin^2(\angle{BAF})=\frac{7}{25}$ . Using LOC, we can write the following statement: \[(\overline{DE})^2=(\overline{AD})^2+\overline{AE}^2-2(\overline{AD})(\overline{AE})\cos(\angle{BAC})\implies\] \[x^2=x^2+(10-x)^2-2(x)(10-x)\left(\frac{7}{25}\right)\implies\] \[0=(10-x)^2-\frac{14x}{25}(10-x)\implies\] \[0=10-x-\frac{14x}{25}\implies\] \[10=\frac{39x}{25}\implies x=\frac{250}{39}\] Thus, the desired answer is $\boxed{289}$ ~ blitzkrieg21

## Solution 6
In isosceles triangle, draw the altitude from $D$ onto $\overline{AD}$ . Let the point of intersection be $X$ . Clearly, $AE=10-AD$ , and hence $AX=\frac{10-AD}{2}$ .
Now, we recognise that the perpendicular from $A$ onto $\overline{AD}$ gives us two $6$ - $8$ - $10$ triangles. So, we calculate $\sin \angle ABC=\frac{4}{5}$ and $\cos \angle ABC=\frac{3}{5}$
$\angle BAC = 180-2\cdot\angle ABC$ . And hence,
$\cos \angle BAC = \cos \angle (180-2\cdot\angle ABC) = -\cos (2\cdot\angle ABC) = \sin^2 \angle ABC - \cos^2 \angle ABC = 2\cos^2 \angle ABC - 1 = \frac{32}{25}-\frac{25}{25}=\frac{7}{25}$
Inspecting $\triangle ADX$ gives us $\cos \angle BAC = \frac{\frac{10-x}{2}}{x} = \frac{10-x}{2x}$ Solving the equation $\frac{10-x}{2x}=\frac{7}{25}$ gives $x= \frac{250}{39} \implies\boxed{289}$
~novus677

## Solution 7 (Area into Similar Triangles)
After calling $x=AD=DE=EC$ and $10-x=AE=BD$ , we see we have length ratios in terms of $x$ , which motivates area ratios. We look at the area of triangle $ADC$ in two ways in order to find $DG$ (perpendicular from $D$ to $AB$ ), and then use similar triangles to find $x$ .
Using area ratios, $[ADC] = \frac{x}{10}\cdot[ABC] = \frac{x}{10} \cdot 48 = \frac{24x}{5}$ . (To find the total area $[ABC] = 48$ , drop the altitudes from $A$ to $BC$ , and call the foot of the altitude $F$ . By the 6-8-10 triangle, the height $AF$ is $8$ and the area of $ABC$ is $48$ .)
The second way of finding the area of triangle $ACD$ is $\frac{1}{2}bh$ . The base is $AC=10$ , and $DG$ is the height. Therefore,
\begin{align*} [ACD] = \frac{24x}{5} &= \frac{1}{2} \cdot 10 \cdot DG \\[5pt] \frac{24x}{25} &= DG \end{align*}
Now we have $DG$ in terms of $x$ , we use the similar triangles $GCD$ and $FAC$ and set up the proportion \begin{align*} \frac{DG}{CF} &= \frac{GC}{FA} \\[5pt] \frac{\frac{24x}{25}}{6} &= \frac{5+\frac{x}{2}}{8} \\[5pt] x &= \frac{250}{39}. \end{align*} So, our answer is $\boxed{289}$ . -epiconan

## Solution 8 (Easiest way- Coordinates without bash)
Let $B=(0, 0)$ , and $C=(12, 0)$ . From there, we know that $A=(6, 8)$ , so line $AB$ is $y=\frac{4}{3}x$ . Hence, $D=(a, \frac{4}{3}a)$ for some $a$ , and $BD=\frac{5}{3}a$ so $AD=10-\frac{5}{3}a$ . Now, notice that by symmetry, $E=(6+a, 8-\frac{4}{3}a)$ , so $ED^2=6^2+(8-\frac{8}{3}a)^2$ . Because $AD=ED$ , we now have $(10-\frac{5}{3})^2=6^2+(8-\frac{8}{3}a)^2$ , which simplifies to $\frac{64}{9}a^2-\frac{128}{3}a+100=\frac{25}{9}a^2-\frac{100}{3}a+100$ , so $\frac{39}{9}a=\frac{13}{3}a=\frac{28}{3}$ , and $a=\frac{28}{13}$ . It follows that $AD=10-\frac{5}{3}\times\frac{28}{13}=10-\frac{140}{39}=\frac{390-140}{39}=\frac{250}{39}$ , and our answer is $250+39=\boxed{289}$ .
-Stormersyle

## Solution 9 one second accurate solve(1 variable equation)
Doing law of cosines we know that $\cos A$ is $\frac{7}{25}.$ * Dropping the perpendicular from $D$ to $AE$ we get that \[\frac{10-x}{2}=\frac{7x}{25}.\] Solving for $x$ we get $\frac{250}{39}$ so our answer is $289$ .
-harsha12345
- It is good to remember that doubling the smallest angle of a 3-4-5 triangle gives the larger (not right) angle in a 7-24-25 triangle.

## Solution 10 (Law of Sines)
Let's label $\angle A = \theta$ and $\angle ECD = \alpha$ . Using isosceles triangle properties and the triangle angle sum equation, we get \[180-(180-2\theta+\alpha) + \frac{180-\theta}{2} + \left(\frac{180-\theta}{2} - \alpha\right) = 180.\] Solving, we find $\theta = 2 \alpha$ .
Relabelling our triangle, we get $\angle ABC = 90 - \alpha$ . Dropping an altitude from $A$ to $BC$ and using the Pythagorean theorem, we find $[ABC] = 48$ . Using the sine area formula, we see $\frac12 \cdot 10 \cdot 12 \cdot \sin(90-\alpha) = 48$ . Plugging in our sine angle cofunction identity, $\sin(90-\alpha) = \cos(\alpha)$ , we get $\alpha = \cos{^{-1}}{\frac45}$ .
Now, using the Law of Sines on $\triangle ADE$ , we get \[\frac{\sin{2\alpha}}{\frac{p}{q}} = \frac{\sin{(180-4\alpha)}}{10-\frac{p}{q}}.\] After applying numerous trigonometric and algebraic tricks, identities, and simplifications, such as $\sin{(180-4\alpha)}=\sin{4\alpha}$ and $\sin{\left(\cos{^{-1}}{\frac45}\right)} = \frac35$ , we find $\frac{p}{q} = \frac{10\sin{2\alpha}}{\sin{4\alpha}+\sin{2\alpha}} = \frac{250}{39}$ .
Therefore, our answer is $250 + 39 = \boxed{289}$ .
~Tiblis

## Solution 11 (Trigonometry)
We start by labelling a few angles (all of them in degrees). Let $\angle{BAC}=2\alpha = \angle{AED}, \angle{EDC}=\angle{ECD}=\alpha, \angle{DEC}=180-2\alpha, \angle{BDC}=3\alpha, \angle{DCB}=90-2\alpha, \angle{DBC}=90-\alpha$ . Also let $AD=a$ . By sine rule in $\triangle{ADE},$ we get $\frac{a}{\sin{2\alpha}}=\frac{10-a}{\sin{4\alpha}} \implies \cos{2\alpha}=\frac{5}{a}-\frac{1}{2}$ Using sine rule in $\triangle{ABC}$ , we get $\sin{\alpha}=\frac{3}{5}$ . Hence we get $\cos{2\alpha}=1-2\sin^2{\alpha}=1-\frac{18}{25}=\frac{7}{25}$ . Hence $\frac{5}{a}=\frac{1}{2}+\frac{7}{25}=\frac{39}{50} \implies a=\frac{250}{39}$ . Therefore, our answer is $\boxed{289}$
Alternatively, use sine rule in $\triangle{BDC}$ . (It’s easier)
~Prabh1512

## Solution 12 (Double Angle Identity)
We let $AD=x$ . Then, angle $A$ is $2\sin^{-1}(\frac{3}{5})$ and so is angle $AED$ . We note that $AE=10-x$ . We drop an altitude from $D$ to $AE$ , and we call the foot $F$ . We note that $AF=\frac{10-x}{2}$ . Using the double angle identity, we have $\sin(2\sin^{-1}(\frac{3}{5}))=2(\frac{3}{5})(\frac{4}{5})=\frac{24}{25}.$ Therefore, $DG=\frac{24}{25}AD.$ We now use the Pythagorean Theorem, which gives $(\frac{10-x}{2})^2+(\frac{24}{25}x)^2=x^2$ . Rearranging and simplifying, this becomes $429x^2-12500x+62500=0$ . Using the quadratic formula, this is $\frac{12500\pm\sqrt{12500^2-250000\cdot429}}{858}$ . We take out a $10000$ from the square root and make it a $100$ outside of the square root to make it simpler. We end up with $\frac{12500\pm7000}{858}$ . We note that this must be less than 10 to ensure that $10-x$ is positive. Therefore, we take the minus, and we get $\frac{5500}{858}=\frac{250}{39} \implies \fbox{289}.$
~john0512

## Video Solution
https://www.youtube.com/watch?v=iE8paW_ICxw
https://youtu.be/dI6uZ67Ae2s ~yofro
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .