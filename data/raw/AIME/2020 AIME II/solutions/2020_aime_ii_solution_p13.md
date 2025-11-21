# 2020 AIME II Problem 13

## Problem

Convex pentagon $ABCDE$ has side lengths $AB=5$ , $BC=CD=DE=6$ , and $EA=7$ . Moreover, the pentagon has an inscribed circle (a circle tangent to each side of the pentagon). Find the area of $ABCDE$ .

## Solution 1
Assume the incircle touches $AB$ , $BC$ , $CD$ , $DE$ , $EA$ at $P,Q,R,S,T$ respectively. Then let $PB=x=BQ=RD=SD$ , $ET=y=ES=CR=CQ$ , $AP=AT=z$ . So we have $x+y=6$ , $x+z=5$ and $y+z=7$ , solve it we have $x=2$ , $z=3$ , $y=4$ . Let the center of the incircle be $I$ , by SAS we can proof triangle $BIQ$ is congruent to triangle $DIS$ , and triangle $CIR$ is congruent to triangle $SIE$ . Then we have $\angle AED=\angle BCD$ , $\angle ABC=\angle CDE$ . Extend $CD$ , cross ray $AB$ at $M$ , ray $AE$ at $N$ , then by AAS we have triangle $END$ is congruent to triangle $BMC$ . Thus $\angle M=\angle N$ . Let $EN=MC=a$ , then $BM=DN=a+2$ . So by law of cosine in triangle $END$ and triangle $ANM$ we can obtain \[\frac{2a+8}{2(a+7)}=\cos N=\frac{a^2+(a+2)^2-36}{2a(a+2)}\] , solved it gives us $a=8$ , which yield triangle $ANM$ to be a triangle with side length 15, 15, 24, draw a height from $A$ to $NM$ divides it into two triangles with side lengths 9, 12, 15, so the area of triangle $ANM$ is 108. Triangle $END$ is a triangle with side lengths 6, 8, 10, so the area of two of them is 48, so the area of pentagon is $108-48=\boxed{60}$ .
-Fanyuchen20020715

## Solution 2 (Complex Bash)
Suppose that the circle intersects $\overline{AB}$ , $\overline{BC}$ , $\overline{CD}$ , $\overline{DE}$ , and $\overline{EA}$ at $P$ , $Q$ , $R$ , $S$ , and $T$ respectively. Then $AT = AP = a$ , $BP = BQ = b$ , $CQ = CR = c$ , $DR = DS = d$ , and $ES = ET = e$ . So $a + b = 5$ , $b + c = 6$ , $c + d = 6$ , $d + e = 6$ , and $e + a = 7$ . Then $2a + 2b + 2c + 2d + 2e = 30$ , so $a + b + c + d + e= 15$ . Then we can solve for each individually. $a = 3$ , $b = 2$ , $c = 4$ , $d = 2$ , and $e = 4$ . To find the radius, we notice that $4 \arctan(\frac{2}{r}) + 4 \arctan(\frac{4}{r}) + 2 \arctan (\frac{3}{r}) = 360 ^ \circ$ , or $2 \arctan(\frac{2}{r}) + 2 \arctan(\frac{4}{r}) + \arctan (\frac{3}{r}) = 180 ^ \circ$ . Each of these angles in this could be represented by complex numbers. When two complex numbers are multiplied, their angles add up to create the angle of the resulting complex number. Thus, $(r + 2i)^2 \cdot (r + 4i)^2 \cdot (r + 3i)$ is real. Expanding, we get:
\[(r^2 + 4ir - 4)(r^2 + 8ir -16)(r + 3i)\]
\[(r^4 + 12ir^3 - 52r^2 - 96ir + 64)(r + 3i)\]
On the last expanding, we only multiply the reals with the imaginaries and vice versa, because we only care that the imaginary component equals 0.
\[15ir^4 - 252ir^2 + 192i = 0\]
\[5r^4 - 84r^2 + 64 = 0\]
\[(5r^2 - 4)(r^2 - 16) = 0\]
$r$ must equal 4, as r cannot be negative or be approximately equal to 1. Thus, the area of $ABCDE$ is $4 \cdot (a + b + c + d + e) = 4 \cdot 15 = \boxed{60}$
-nihao4112

## Solution 3 (Guess 1)
This pentagon is very close to a regular pentagon with side lengths $6$ . The area of a regular pentagon with side lengths $s$ is $\frac{5s^2}{4\sqrt{5-2\sqrt{5}}}$ . $5-2\sqrt{5}$ is slightly greater than $\frac{1}{2}$ given that $2\sqrt{5}$ is slightly less than $\frac{9}{2}$ . $4\sqrt{5-2\sqrt{5}}$ is then slightly greater than $2\sqrt{2}$ . We will approximate that to be $2.9$ . The area is now roughly $\frac{180}{2.9}$ , but because the actual pentagon is not regular, but has the same perimeter of the regular one that we are comparing to we can say that this is an overestimate on the area and turn the $2.9$ into $3$ thus turning the area into $\frac{180}{3}$ which is $60$ and since $60$ is a multiple of the semiperimeter $15$ , we can safely say that the answer is most likely $\boxed{60}$ .
~Lopkiloinm

## Solution 4 (Guess 2)
Because the AIME answers have to be a whole number it would meant the radius of the circle have to be a whole number, thus by drawing the diagram and experimenting, we can safely say the radius is 4 and the answer is 60
(Edit: While the guess would be technically correct, the assumption that the radius would have to be a whole number for the ans to be a whole number is wrong)
By EtherealMidnight
(Edit: I think that will actually work because the area of $ABCDE$ is equal to the semi-perimeter times the radius. By a simple calculation, we know that the semi-perimeter is an integer so the radius should also be an integer)
By YBSuburbanTea
...the radius could be a fraction with denominator 3, 5, or 15, and the area of the pentagon would still be an integer. - GeometryJake

## Solution 5 (Official MAA 1)
Let $\omega$ be the inscribed circle, $I$ be its center, and $r$ be its radius. The area of $ABCDE$ is equal to its semiperimeter, $15,$ times $r$ , so the problem is reduced to finding $r$ . Let $a$ be the length of the tangent segment from $A$ to $\omega$ , and analogously define $b$ , $c$ , $d$ , and $e$ . Then $a+b=5$ , $b+c= c+d=d+e=6$ , and $e+a=7$ , with a total of $a+b+c+d+e=15$ . Hence $a=3$ , $b=d=2$ , and $c=e=4$ . It follows that $\angle B= \angle D$ and $\angle C= \angle E$ . Let $Q$ be the point where $\omega$ is tangent to $\overline{CD}$ . Then $\angle IAE = \angle IAB =\frac{1}{2}\angle A$ . Now we claim that points $A, I, Q$ are collinear, which can be proved if $\angle{AIQ}=\angle{QIA}=180^{\circ}$ . The sum of the internal angles in polygons $ABCQI$ and $AIQDE$ are equal, so $\angle IAE + \angle AIQ + \angle IQD + \angle D + \angle E = \angle IAB + \angle B + \angle C + \angle CQI + \angle QIA$ , which implies that $\angle AIQ$ must be $180^\circ$ . Therefore points $A$ , $I$ , and $Q$ are collinear. [asy] defaultpen(fontsize(8pt)); unitsize(0.025cm); pair[] vertices = {(0,0), (5,0), (8.6,4.8), (3.8,8.4), (-1.96, 6.72)}; string[] labels = {"$A$", "$B$", "$C$", "$D$", "$E$"}; pair[] dirs = {SW, SE,E, N, NW}; string[] smallLabels = {"$a$", "$b$", "$c$", "$d$", "$e$"}; pair I = (3,4); real rad = 4; pair Q = foot(I, vertices[2], vertices[3]); pair[] interpoints = {}; for(int i =0; i<vertices.length; ++i){ interpoints.push(foot(I, vertices[i], vertices[(i+1)%vertices.length])); } for(int i = 0; i< vertices.length; ++i){ draw(vertices[i]--vertices[(i+1)%vertices.length]); dot(labels[i],vertices[i],dirs[i]); draw(I--vertices[i]); } draw(Circle(I, rad)); dot("$I$", I, dir(200)); draw(I--Q); dot("$Q$", Q, NE); for(int i = 0; i < vertices.length; ++i){ label(smallLabels[i], vertices[i] --interpoints[i]); //dot(interpoints[i], blue); label(smallLabels[i], interpoints[(i-1)%vertices.length] -- vertices[i]); } [/asy] Because $\overline{AQ} \perp \overline{CD}$ , it follows that \[AC^2-AD^2=CQ^2-DQ^2=c^2-d^2=12.\] Another expression for $AC^2-AD^2$ can be found as follows. Note that $\tan \left(\frac{\angle B}{2}\right) = \frac{r}{2}$ and $\tan \left(\frac{\angle E}{2}\right) = \frac{r}{4}$ , so \[\cos (\angle B) =\frac{1-\tan^2 \left(\frac{\angle B}{2}\right)}{1+\tan^2 \left(\frac{\angle B}{2}\right)} = \frac{4-r^2}{4+r^2}\] and \[\cos (\angle E) = \frac{1-\tan^2 \left(\frac{\angle E}{2}\right)}{1+\tan^2 \left(\frac{\angle E}{2}\right)}= \frac{16-r^2}{16+r^2}.\] Applying the Law of Cosines to $\triangle ABC$ and $\triangle AED$ gives \[AC^2=AB^2+BC^2-2\cdot AB\cdot BC\cdot \cos (\angle B) = 5^2+6^2-2 \cdot 5 \cdot 6 \cdot \frac{4-r^2}{4+r^2}\] and \[AD^2=AE^2+DE^2-2 \cdot AE \cdot DE \cdot \cos(\angle E) = 7^2+6^2-2 \cdot 7 \cdot 6 \cdot \frac{16-r^2}{16+r^2}.\] Hence
\[12=AC^2- AD^2= 5^2-2\cdot 5 \cdot 6\cdot \frac{4-r^2}{4+r^2} -7^2+2\cdot 7 \cdot 6 \cdot \frac{16-r^2}{16+r^2},\] yielding \[2\cdot 7 \cdot 6 \cdot \frac{16-r^2}{16+r^2}- 2\cdot 5 \cdot 6\cdot \frac{4-r^2}{4+r^2}= 36;\] equivalently \[7(16-r^2)(4+r^2)-5(4-r^2)(16+r^2) = 3(16+r^2)(4+r^2).\] Substituting $x=r^2$ gives the quadratic equation $5x^2-84x+64=0$ , with solutions $\frac{42 - 38}{5}=\frac45$ , and $\frac{42 + 38}{5}= 16$ . The solution $r^2=\frac45$ corresponds to a five-pointed star, which is not convex. Indeed, if $r<3$ , then $\tan \left(\frac{\angle A}{2}\right)$ , $\tan \left(\frac{\angle C}{2}\right)$ , and $\tan \left(\frac{\angle E}{2}\right)$ are less than $1,$ implying that $\angle A$ , $\angle C$ , and $\angle E$ are acute, which cannot happen in a convex pentagon. Thus $r^2=16$ and $r=4$ . The requested area is $15\cdot4 = \boxed{60}$ .

## Solution 6 (Official MAA 2)
Define $a$ , $b$ , $c$ , $d$ , $e$ , and $r$ as in Solution 5. Then, as in Solution 5, $a=3$ , $b=d=2$ , $c=e=4$ , $\angle B= \angle D$ , and $\angle C= \angle E$ . Let $\alpha =\frac{\angle A}{2}$ , $\beta = \frac{\angle B}{2}$ , and $\gamma=\frac{\angle C}{2}$ . It follows that $540^{\circ} = 2\alpha + 4 \beta + 4 \gamma$ , so $270^{\circ} = \alpha + 2\beta + 2 \gamma$ . Thus \[\tan(2\beta + 2 \gamma) = \frac{1}{\tan \alpha},\] $\tan(\beta) = \frac{r}{2}$ , $\tan(\gamma) = \frac{r}{4}$ , and $\tan(\alpha) = \frac {r}{3}$ . By the Tangent Addition Formula, \[\tan(\beta +\gamma) = \frac{6r}{8-r^2}\] and \[\tan(2\beta + 2\gamma) = \frac{\frac{12r}{8-r^2}}{1-\frac{36r^2}{(8-r^2)^2}} = \frac{12r(8-r^2)}{(8-r^2)^2-36r^2}.\] Therefore \[\frac{12r(8-r^2)}{(8-r^2)^2-36r^2} = \frac{3}{r},\] which simplifies to $5r^4 - 84r^2 + 64 = 0$ . Then the solution proceeds as in Solution 5.

## Solution 7 (Official MAA 3)
Define $a$ , $b$ , $c$ , $d$ , $e$ , and $r$ as in Solution 5. Note that \[\arctan\left(\frac{a}{r}\right) + \arctan\left(\frac{b}{r}\right) + \arctan\left(\frac{c}{r}\right) + \arctan\left(\frac{d}{r}\right) + \arctan\left(\frac{e}{r}\right) = 180^{\circ}.\] Hence \[\operatorname{Arg}(r + 3i) + 2\cdot \operatorname{Arg}(r + 2i) + 2\cdot \operatorname{Arg}(r + 4i) = 180^{\circ}.\] Therefore \[\operatorname{Im} \big( (r + 3i)(r+2i)^2(r+4i)^2 \big) = 0.\] Simplifying this equation gives the same quadratic equation in $r^2$ as in Solution 5.

## Solution 8 (The same circle)
Notation shown on diagram. As in solution 5, we get $\overline{AQ} \perp \overline{CD}, AG = 3, GB = 2, CQ = 4$ and so on.
Let $\overline{AB}$ cross $\overline{CD}$ at $F, \overline{AE}$ cross $\overline{CD}$ at $F', CF = x.$ $FQ = FG \implies FB = x+2.$ $\angle BAQ = \angle EAQ \implies DF' = x + 2, EF' = x.$ Triangle $\triangle AFF'$ has semiperimeter $s = 2x + 11.$
The radius of incircle $\omega$ is $r =\sqrt{\frac{s-FF’}{s}}(s-AF) = \sqrt{\frac{3}{2x +11}}(x+4).$
Triangle $\triangle BCF$ has semiperimeter $s = x + 4.$
The radius of excircle $\omega$ is $r = \sqrt{\frac{s(s-BF)(s-CF)}{s-BC}} = \sqrt{ \frac{(x+4)\cdot 2 \cdot 4}{x - 2}}.$
It is the same radius, therefore \[\sqrt{\frac{3}{2x +11}}(x+4) = \sqrt{\frac{8(x+4)}{x – 2}} \implies \frac {3(x+4)}{2x+11} = \frac {8}{x-2} \implies (x-8)(3x + 14) = 0 \implies x = 8, r = 4.\]
Then the solution proceeds as in Solution 5.

## Solution 9 (EASIEST)
Let $O$ be the center of the incircle and $OP$ and $OQ$ are the perpendiculars dropped from point $O$ to sides $BC$ and $CD$ respectively, making $OP = OQ = r$ . After you got $CP$ and $CQ$ by the solutions which are given above (i.e Solution 1) then consider cyclic quadrilateral $OPCQ$ . Now by Pythagoras in TRIANGLE $OPC$ We get $OC^2 = r^2 + 16$ , and by Ptolemy you get $4r+4r = OC.PQ$ Making $64r^2 = (r^2 + 16)(32)$ leading to $2r^2 = (r^2 + 16)$ implying $r^2 = 16$ implying $r = 4$ . Now since in a tangential polygon Area = $sr$ where s = semiperimeter of that polygon and r = inradius Putting those values \implies AREA = $15r$ = $15(4)$ = $\boxed{60}$
vladimir.shelomovskii@gmail.com, vvsss

## Video Solution 1 by MOP 2024
https://youtube.com/watch?v=BXEXcCNXrlM
~r00tsOfUnity

## Video Solution 2
https://youtu.be/bz5N-jI2e0U?t=327

## Video Solution 3
https://youtu.be/_fwkGTdMd8U

## Video Solution 4
https://youtu.be/kn3c2LStiHA (solve in 5 minutes)
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .