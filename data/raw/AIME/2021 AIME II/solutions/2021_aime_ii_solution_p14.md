# 2021 AIME II Problem 14

## Problem

Let $\Delta ABC$ be an acute triangle with circumcenter $O$ and centroid $G$ . Let $X$ be the intersection of the line tangent to the circumcircle of $\Delta ABC$ at $A$ and the line perpendicular to $GO$ at $G$ . Let $Y$ be the intersection of lines $XG$ and $BC$ . Given that the measures of $\angle ABC, \angle BCA,$ and $\angle XOY$ are in the ratio $13 : 2 : 17,$ the degree measure of $\angle BAC$ can be written as $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(375); pair A, B, C, O, G, X, Y; A = origin; B = (1,0); C = extension(A,A+10*dir(585/7),B,B+10*dir(180-585/7)); O = circumcenter(A,B,C); G = centroid(A,B,C); Y = intersectionpoint(G--G+(100,0),B--C); X = intersectionpoint(G--G-(100,0),A--scale(100)*rotate(90)*dir(O-A)); markscalefactor=3/160; draw(rightanglemark(O,G,X),red); dot("$A$",A,1.5*dir(180+585/7),linewidth(4)); dot("$B$",B,1.5*dir(-585/7),linewidth(4)); dot("$C$",C,1.5N,linewidth(4)); dot("$O$",O,1.5N,linewidth(4)); dot("$G$",G,1.5S,linewidth(4)); dot("$Y$",Y,1.5E,linewidth(4)); dot("$X$",X,1.5W,linewidth(4)); draw(A--B--C--cycle^^X--O--Y--cycle^^A--X^^O--G^^circumcircle(A,B,C)); [/asy] ~MRENTHUSIASM

## Solution 1
In this solution, all angle measures are in degrees.
Let $M$ be the midpoint of $\overline{BC}$ so that $\overline{OM}\perp\overline{BC}$ and $A,G,M$ are collinear. Let $\angle ABC=13k,\angle BCA=2k$ and $\angle XOY=17k.$
Note that:
1. Since $\angle OGX = \angle OAX = 90,$ quadrilateral $OGAX$ is cyclic by the Converse of the Inscribed Angle Theorem. It follows that as they share the same intercepted arc
1. Since $\angle OGY = \angle OMY = 90,$ quadrilateral $OGYM$ is cyclic by the supplementary opposite angles. It follows that as they share the same intercepted arc
It follows that $\angle OAG = \angle OXG,$ as they share the same intercepted arc $\widehat{OG}.$
It follows that $\angle OMG = \angle OYG,$ as they share the same intercepted arc $\widehat{OG}.$
Together, we conclude that $\triangle OAM \sim \triangle OXY$ by AA, so $\angle AOM = \angle XOY = 17k.$
Next, we express $\angle BAC$ in terms of $k.$ By angle addition, we have \begin{align*} \angle AOM &= \angle AOB + \angle BOM \\ &= 2\angle BCA + \frac12\angle BOC \hspace{10mm} &&\text{by Inscribed Angle Theorem and Perpendicular Bisector Property} \\ &= 2\angle BCA + \angle BAC. &&\text{by Inscribed Angle Theorem} \end{align*} Substituting back gives $17k=2(2k)+\angle BAC,$ from which $\angle BAC=13k.$
For the sum of the interior angles of $\triangle ABC,$ we get \begin{align*} \angle ABC + \angle BCA + \angle BAC &= 180 \\ 13k+2k+13k&=180 \\ 28k&=180 \\ k&=\frac{45}{7}. \end{align*} Finally, we obtain $\angle BAC=13k=\frac{585}{7},$ from which the answer is $585+7=\boxed{592}.$
~Constance-variance ~MRENTHUSIASM

## Solution 2
Let $M$ be the midpoint of $BC$ . Because $\angle{OAX}=\angle{OGX}=\angle{OGY}=\angle{OMY}=90^o$ , $AXOG$ and $OMYG$ are cyclic, so $O$ is the center of the spiral similarity sending $AM$ to $XY$ , and $\angle{XOY}=\angle{AOM}$ . Because $\angle{AOM}=2\angle{BCA}+\angle{BAC}$ , it's easy to get $\frac{585}{7} \implies \boxed{592}$ from here.
~Lcz

## Solution 3 (Easy and Simple)
Firstly, let $M$ be the midpoint of $BC$ . Then, $\angle OMB = 90^o$ . Now, note that since $\angle OGX = \angle XAO = 90^o$ , quadrilateral $AGOX$ is cyclic. Also, because $\angle OMY + \angle OGY = 180^o$ , $OMYG$ is also cyclic. Now, we define some variables: let $\alpha$ be the constant such that $\angle ABC = 13\alpha, \angle ACB = 2\alpha,$ and $\angle XOY = 17\alpha$ . Also, let $\beta = \angle OMG = \angle OYG$ and $\theta = \angle OXG = \angle OAG$ (due to the fact that $AGOX$ and $OMYG$ are cyclic). Then, \[\angle XOY = 180 - \beta - \theta = 17\alpha \implies \beta + \theta = 180 - 17\alpha.\] Now, because $AX$ is tangent to the circumcircle at $A$ , $\angle XAC = \angle CBA = 13\alpha$ , and $\angle CAO = \angle OAX - \angle CAX = 90 - 13\alpha$ . Finally, notice that $\angle AMB = \angle OMB - \angle OMG = 90 - \beta$ . Then, \[\angle BAM = 180 - \angle ABC - \angle AMB = 180 - 13\alpha - (90 - \beta) = 90 + \beta - 13\alpha.\] Thus, \[\angle BAC = \angle BAM + \angle MAO + \angle OAC = 90 + \beta - 13\alpha + \theta + 90 - 13\alpha = 180 - 26\alpha + (\beta + \theta),\] and \[180 = \angle BAC + 13\alpha + 2\alpha = 180 - 11\alpha + \beta + \theta \implies \beta + \theta = 11\alpha.\] However, from before, $\beta+\theta = 180 - 17 \alpha$ , so $11 \alpha = 180 - 17 \alpha \implies 180 = 28 \alpha \implies \alpha = \frac{180}{28}$ . To finish the problem, we simply compute \[\angle BAC = 180 - 15 \alpha = 180 \cdot \left(1 - \frac{15}{28}\right) = 180 \cdot \frac{13}{28} = \frac{585}{7},\] so our final answer is $585+7=\boxed{592}$ .
~advanture

## Solution 4 (Why Isosceles)
[asy] /* Made by MRENTHUSIASM */ size(375); pair A, B, C, O, G, X, Y; A = origin; B = (1,0); C = extension(A,A+10*dir(585/7),B,B+10*dir(180-585/7)); O = circumcenter(A,B,C); G = centroid(A,B,C); Y = intersectionpoint(G--G+(100,0),B--C); X = intersectionpoint(G--G-(100,0),A--scale(100)*rotate(90)*dir(O-A)); pair O1=circumcenter(O,G,A); real r1=length(O1-O); markscalefactor=3/160; filldraw(O--X--Y--cycle, rgb(255,255,0)); draw(rightanglemark(O,G,X),red); draw(A--O--B,fuchsia+0.4); draw(Arc(O1,r1,-40,50),royalblue+0.5); draw(circumcircle(O,G,Y), heavygreen+0.5); dot("$A$",A,1.5*dir(180+585/7),linewidth(4)); dot("$B$",B,1.5*dir(-585/7),linewidth(4)); dot("$C$",C,1.5N,linewidth(4)); dot("$O$",O,1.5N,linewidth(4)); dot("$G$",G,1.5S,linewidth(4)); dot("$Y$",Y,1.5E,linewidth(4)); dot("$X$",X,1.5W,linewidth(4)); draw(A--B--C--cycle^^X--O--Y--cycle^^A--X^^O--G^^circumcircle(A,B,C)); [/asy] $\angle OAX = \angle OGX = 90^\circ \implies$ quadrilateral $XAGO$ is cyclic $\implies$
$\angle GXO = \angle GAO,$ as they share the same intersept $\overset{\Large\frown} {GO}.$
$\angle OGY = \angle OMY = 90^\circ \implies$ quadrilateral $OGYM$ is cyclic $\implies$
$\angle GYO = \angle OMG,$ as they share the same intercept $\overset{\Large\frown} {GO}.$
In triangles $\triangle XOY$ and $\triangle AOM,$ two pairs of angles are equal, which means that the third angles $\angle XOY = \angle AOM$ are also equal.
$\angle ABC : \angle BCA : \angle AOM = 13 : 2 : 17,$ so $\angle AOM = \angle ABC + 2 \angle BCA.$
According to the Claim , $\triangle ABC$ is isosceles, \[\angle ABC : \angle BCA : \angle BAC = 13 : 2 : 13.\] \[\angle BAC = \frac{13} {13 + 2 + 13} \cdot 180^\circ = \frac {585^\circ}{7} \implies 585 + 7 = \boxed{592}.\]
Claim
Let $\triangle ABC$ be an acute triangle with circumcenter $O.$
Let $M$ be the midpoint of $BC$ so $MO\perp BC.$
If $\angle AOM = 2\angle ACB + \angle ABC,$ then $AC = BC.$
We define $\angle AOM$ as the sum of $\angle AOB + \angle BOM,$ this angle can be greater than $180^\circ.$
Proof
$\angle BAC = \angle BOM$ as they share the same intercept $\overset{\Large\frown} {BC}$ (an inscribed angle and half of central angle).
$\angle AOB = 2\angle ACB$ as they share the same intercept $\overset{\Large\frown} {AB}.$
\[\angle AOM = \angle AOB + \angle BOM = 2 \angle ACB + \angle CAB.\]
If $\angle AOM = 2 \angle ACB + \angle ABC,$ then $\angle ABC = \angle CAB, AC = BC.$
vladimir.shelomovskii@gmail.com, vvsss

## Solution 5
Extend $XA$ and meet line $CB$ at $P$ . Extend $AG$ to meet $BC$ at $F$ . Since $AF$ is the median from $A$ to $BC$ , $A,G,F$ are collinear. Furthermore, $OF$ is perpendicular to $BC$
Draw the circumcircle of $\triangle{XPY}$ , as $OA\bot XP, OG\bot XY, OF\bot PY$ , $A,G,F$ are collinear, $O$ lies on $(XYP)$ as $AGF$ is the Simson line of $O$ with respect to $\triangle{XPY}$ . Thus, $\angle{P}=180-17x, \angle{PAB}=\angle{C}=2x, 180-15x=13x, x=\frac{45}{7}$ , the answer is $180-15\cdot \frac{45}{7}=\frac{585}{7}$ which is $\boxed{592}$ .
~bluesoul

## Video Solution 1
https://www.youtube.com/watch?v=zFH1Z7Ydq1s
~Mathematical Dexterity

## Video Solution 2
https://www.youtube.com/watch?v=7Bxr2h4btWo
~Osman Nal

## Video Solution by Interstigation
https://www.youtube.com/watch?v=yIWe7ME6fpA
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .