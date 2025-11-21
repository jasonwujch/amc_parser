# 2022 AMC 10B Problem 20

## Problem

Let $ABCD$ be a rhombus with $\angle ADC = 46^\circ$ . Let $E$ be the midpoint of $\overline{CD}$ , and let $F$ be the point on $\overline{BE}$ such that $\overline{AF}$ is perpendicular to $\overline{BE}$ . What is the degree measure of $\angle BFC$ ?

$\textbf{(A)}\ 110 \qquad\textbf{(B)}\ 111 \qquad\textbf{(C)}\ 112 \qquad\textbf{(D)}\ 113 \qquad\textbf{(E)}\ 114$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(300); pair A, B, C, D, E, F; D = origin; A = 6*dir(46); C = (6,0); B = C + (A-D); E = midpoint(C--D); F = foot(A,B,E); dot("$A$",A,1.5*NW,linewidth(5)); dot("$B$",B,1.5*NE,linewidth(5)); dot("$C$",C,1.5*SE,linewidth(5)); dot("$D$",D,1.5*SW,linewidth(5)); dot("$E$",E,1.5*S,linewidth(5)); dot("$F$",F,1.5*dir(-20),linewidth(5)); markscalefactor=0.04; draw(rightanglemark(A,F,B),red); draw(A--B--C--D--cycle^^A--F--C^^B--E); label("$46^{\circ}$",D,3*dir(26),red); [/asy] ~MRENTHUSIASM

## Solution 1
Extend segments $\overline{AD}$ and $\overline{BE}$ until they meet at point $G$ .
Because $\overline{AB} \parallel \overline{ED}$ , we have $\angle ABG = \angle DEG$ and $\angle GDE = \angle GAB$ , so $\triangle ABG \sim \triangle DEG$ by AA.
Because $ABCD$ is a rhombus, $AB = CD = 2DE$ , so $AG = 2GD$ , meaning that $D$ is a midpoint of segment $\overline{AG}$ .
Now, $\overline{AF} \perp \overline{BE}$ , so $\triangle GFA$ is right and median $FD = AD$ .
So now, because $ABCD$ is a rhombus, $FD = AD = CD$ . This means that there exists a circle from $D$ with radius $AD$ that passes through $F$ , $A$ , and $C$ .
AG is a diameter of this circle because $\angle AFG=90^\circ$ . This means that $\angle GFC = \angle GAC = \frac{1}{2} \angle GDC$ , so $\angle GFC = \frac{1}{2}(180^\circ - 46^\circ)=67^\circ$ , which means that $\angle BFC = \boxed{\textbf{(D)} \ 113}$
~popop614

## Solution 3
Let $\overline{AC}$ meet $\overline{BD}$ at $O$ , then $AOFB$ is cyclic and $\angle FBO = \angle FAO$ . Also, $AC \cdot BO = [ABCD] = 2 \cdot [ABE] = AF \cdot BE$ , so $\frac{AF}{BO} = \frac{AC}{BE}$ , thus $\triangle AFC \sim \triangle BOE$ by SAS, and $\angle OEB = \angle ACF$ , then $\angle CFE = \angle EOC = \angle DAC = 67^\circ$ , and $\angle BFC = \boxed{\textbf{(D)} \ 113}$
~mathfan2020
A little bit faster: $AOFB$ is cyclic $\implies \angle OFE = \angle BAO$ .
$AB \parallel CD \implies \angle BAO = \angle OCE$ .
Therefore $\angle OFE=\angle OCE \implies OECF$ is cyclic.
Hence $\angle CFE=\angle COE=\angle CAD = 67^\circ$ .
~asops

## Solution 4
Observe that all answer choices are close to $112.5 = 90+\frac{45}{2}$ . A quick solve shows that having $\angle D = 90^\circ$ yields $\angle BFC = 135^\circ = 90 + \frac{90}{2}$ , meaning that $\angle BFC$ increases with $\angle D$ . Substituting, $\angle BFC = 90 + \frac{46}{2} = \boxed{\textbf{(D)} \ 113}$ .
~mathfan2020

## Solution 5 (Similarity and Circle Geometry)
This solution refers to the Diagram section.
We extend $AD$ and $BE$ to point $G$ , as shown below: [asy] /* Made by ghfhgvghj10 Edited by MRENTHUSIASM */ size(300); pair A, B, C, D, E, F, G; D = origin; A = 6*dir(46); C = (6,0); B = C + (A-D); E = midpoint(C--D); F = foot(A,B,E); G = 6*dir(226); dot("$A$",A,1.5*NW,linewidth(5)); dot("$B$",B,1.5*NE,linewidth(5)); dot("$C$",C,1.5*SE,linewidth(5)); dot("$D$",D,1.5*NW,linewidth(5)); dot("$E$",E,1.5*S,linewidth(5)); dot("$F$",F,1.5*dir(-20),linewidth(5)); dot("$G$",G,1.5*SW,linewidth(5)); markscalefactor=0.04; draw(rightanglemark(A,F,B),red); draw(A--B--C--D--cycle^^A--F--C^^B--E^^D--G^^E--G); label("$46^{\circ}$",D,3*dir(26),red+fontsize(10)); [/asy] We know that $AB=AD=2$ and $CE=DE=1$ .
By AA Similarity, $\triangle ABG \sim \triangle DEG$ with a ratio of $2:1$ . This implies that $2AD=AG$ and $AD \cong DG$ , so $AG=2AD=2\cdot2=4$ . That is, $D$ is the midpoint of $AG$ .
Note that as $\angle{AFG}$ has an angle of 90 deg and $AG=2DG$ , we can redraw our previous diagram, but construct a circle with radius $AD$ or $2$ centered at $D$ and by extending $CD$ to point $H$ , which is on the circle, as shown below: [asy] /* Made by ghfhgvghj10 Edited by MRENTHUSIASM */ size(300); pair A, B, C, D, E, F, G; D = origin; A = 6*dir(46); C = (6,0); B = C + (A-D); E = midpoint(C--D); F = foot(A,B,E); G = 6*dir(226); dot("$A$",A,1.5*NE,linewidth(5)); dot("$B$",B,1.5*NE,linewidth(5)); dot("$C$",C,1.5*SE,linewidth(5)); dot("$D$",D,1.5*NW,linewidth(5)); dot("$E$",E,1.5*S,linewidth(5)); dot("$F$",F,1.5*dir(-20),linewidth(5)); dot("$G$",G,1.5*SW,linewidth(5)); markscalefactor=0.04; draw(rightanglemark(A,F,B),red); draw(A--B--C--D--cycle^^A--F--C^^B--E^^D--G^^E--G); label("$46^{\circ}$",D,3*dir(26),red+fontsize(10)); draw(Circle(D,6),dashed); [/asy] Notice how $F$ and $C$ are on the circle and that $\angle CFE$ intercepts with $\overset{\Large\frown} {CG}$ .
Let's call $\angle CFE = \theta$ .
Note that $\angle CDG$ also intercepts $\overset{\Large\frown} {CG}$ , So $\angle CDG = 2\angle CFE$ .
Let $\angle CDG = 2\theta$ . Notice how $\angle CDG$ and $\angle ADC$ are supplementary to each other. We conclude that \begin{align*} 2\theta &= 180-\angle ADC \\ 2\theta &= 180-46 \\ 2\theta &= 134 \\ \theta &= 67. \end{align*} Since $\angle BFC=180-\theta$ , we have $\angle BFC=180-67=\boxed{\textbf{(D)} \ 113}$ .
~ghfhgvghj10 (If I make any minor mistakes, feel free to make minor fixes and edits). ~mathboy282
Note: You can also find that CFE is half of CDG via circle theorems. We know CDG = 180 - 46 = 134, therefore making CFE 67 and BFC 113.
~meikh_neiht

## Solution 6 (Simplification/Reduction)
If angle $ADC$ was a right angle, it would be much easier. Thus, first pretend that $ADC$ is a right angle. $ABCD$ is now a square. WLOG, let each of the side lengths be 1. We can use the Pythagorean Theorem to find the length of line $AE$ , which is $\sqrt{5}/2$ . We want the measure of angle $BFC$ , so to work closer to it, we should try finding the length of line $BF$ . Angle $FAB$ and angle $ABF$ are complementary. Angle $ABF$ and angle $FBC$ are also complementary. Thus, $\sin FAB=\cos ABF=\sin FBC$ . $\sin FAB=\sin FBC=(1/2)/(\sqrt{5}/2)=1/\sqrt{5}$ . Since $\sin FAB=1\sqrt{5}$ ,and $AB=1$ , $FB=\sin FAB$ . It follows now that $FE=3*\sqrt{5}/10$ .
Now, zoom in on triangle $BEC$ . To use the Law of Cosines on triangle $FBC$ , we need the length of $FC$ . Use the Law of Cosines on triangle $EFC$ . Cos $E=1/\sqrt{5}$ . Thus, after using the Law of Cosines, $FC=\sqrt{2/5}$ .
Since we now have SSS on $BEC$ , we can get use the Law of Cosines. $\cos BFC=1/-\sqrt{2}$ . $\arccos 1/-\sqrt{2}$ is 45, but if the cosine is negative that means that the angle is the supplement of the positive cosine value. $180-45=135$ . Angle $BFC$ is $135^\circ$ .
Realize that, around point F, there will always be 3 right angles, regardless of what angle $ADC$ is. There are only two angles that change when $ADC$ changes. Break up angle $BFC$ into angle $BFB'$ , which is always 90 degrees, and angle $B'FC$ , which we have discovered to to be half of $ADC$ . Thus, when angle $ADC$ is 46 degrees, then $B'FC$ will be 23. $23+90=113$ . Angle $BFC$ is $\boxed{\textbf{(D) }113}$ degrees.

## Solution 7
Draw an auxiliary line from D to the midpoint of AB. Label it G. Then quadrilateral BGDE is a parallelogram. Hence AF and BD are perpendicular. Now, G being the midpoint of the hypontenuse of triangle ABF, it is the circumcenter of it. Thus, GF = GA and so DG is the perpendicular bisector of AF. Therefore, triangle AFD is also a isosceles triangle. Since AD = FD = CD, triangle CFD is also an isosceles triangle. Their one distinct angles' sum being 46 degrees, angle BFC = 113.
Jeongha Cho

## Solution 8(lots and lots of tedious angle chasing)
It is a well known fact that connecting the midpoints of the sides of a rhombus gives us a rectangle. We let the midpoint of side $DC$ as $E$ , the midpoint of side $AD$ as $F$ , the midpoint of side $AB$ as $G$ , and the midpoint of side $BC$ as $H$ . We can connect $E, F, G, H$ to get rectangle $EFGH$ . Note that the obtuse angles of the rhombus are each $134$ degrees. We can perform a little bit of angle chasing following this diagram(I cannot draw diagrams in LaTex so the rest of this solution will be diagram-free). Let the intersection point between line segment $BE$ and line segment $GH$ as $I$ . Let angle $FEB$ to be $\theta$ . Performing more angle chasing leads us to finding that angle $GIB$ is angle $\theta$ and angle $IBG$ is $113 - \theta$ . Let point $J$ be on $BE$ such that $AJ$ is perpendicular to $BE$ . Then, by performing yet more angle chasing leads us to finding that angle $JEC$ is $90 - \theta + 23 = 113 - \theta$ . We can predict that triangle $JEC$ is similar to triangle $BIG$ . This is because since $GB$ and $EC$ both bisect the sides of the rhombus and one angle is common(the $113 - \theta$ angle). Therefore, we can safely say that all angles in these two triangles must be the same and thus angle $CJE = IGB = 67$ degrees. Thus, our desired angle, $CJB$ is simply just $180 - 67 = \boxed{113}$ .
~ilikemath247365

## Solution 9 (educated guess)
The answer choices must have something to do with 46. We can do some playing around, like trying $180 - 46 = 134$ . Since the answers are all around the $110$ s, we can start manipulating our $134$ . We could divide by $2$ , subtract $90$ , etc. Dividing by $2$ gives $67$ , and we can see $180 - 67 = 113$ . However, we can also see that $180-((180-(90-46))/2) = 112$ , but this seems much too complicated for a simple rhombus. Therefore, we can reasonably assume the answer is $\boxed{113}$ .
~PerseverePlayer

## Video Solution (⚡️Just 1 min!⚡️)
https://youtu.be/CriWEtfD5GE
~Education, the Study of Everything

## Video Solution
https://www.youtube.com/watch?v=HWJe96s_ugs&list=PLmpPPbOoDfgj5BlPtEAGcB7BR_UA5FgFj&index=6

## Video Solution
https://youtu.be/Ysb1EK_5B2g
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by OmegaLearn Using Clever Similar Triangles and Angle Chasing
https://youtu.be/lEmCprb20n4
~ pi_is_3.14

## Video Solution, best solution (not family friendly, no circles drawn)
https://www.youtube.com/watch?v=vwI3I7dxw0Q

## Video Solution, by Challenge 25
https://youtu.be/W1jbMaO8BIQ (cyclic quads)

## Video Solution by Interstigation
https://youtu.be/5Plt3mmZBC0
~Interstigation

## Video Solution (Cool Solution)
https://www.youtube.com/watch?v=cZcaeU9P25s&ab_channel=Chillin
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .