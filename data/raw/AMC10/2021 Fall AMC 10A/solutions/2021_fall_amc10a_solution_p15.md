# 2021 Fall AMC 10A Problem 15

## Problem

Isosceles triangle $ABC$ has $AB = AC = 3\sqrt6$ , and a circle with radius $5\sqrt2$ is tangent to line $AB$ at $B$ and to line $AC$ at $C$ . What is the area of the circle that passes through vertices $A$ , $B$ , and $C?$

$\textbf{(A) }24\pi\qquad\textbf{(B) }25\pi\qquad\textbf{(C) }26\pi\qquad\textbf{(D) }27\pi\qquad\textbf{(E) }28\pi$

## Solution 1 (Cyclic Quadrilateral)
Let $\odot O_1$ be the circle with radius $5\sqrt2$ that is tangent to $\overleftrightarrow{AB}$ at $B$ and to $\overleftrightarrow{AC}$ at $C.$ Note that $\angle ABO_1 = \angle ACO_1 = 90^\circ.$ Since the opposite angles of quadrilateral $ABO_1C$ are supplementary, quadrilateral $ABO_1C$ is cyclic.
Let $\odot O_2$ be the circumcircle of quadrilateral $ABO_1C.$ It follows that $\odot O_2$ is also the circumcircle of $\triangle ABC,$ as shown below: [asy] /* Made by MRENTHUSIASM */ size(200); pair A, B, C, D, O1, O2; A = (0,2sqrt(26)); O1 = (0,0); B = intersectionpoints(Circle(A,3sqrt(6)),Circle(O1,5sqrt(2)))[0]; C = intersectionpoints(Circle(A,3sqrt(6)),Circle(O1,5sqrt(2)))[1]; O2 = midpoint(A--O1); fill(A--B--C--cycle, yellow); dot("$A$",A,1.5*N,linewidth(4)); dot("$B$",B,1.5*W,linewidth(4)); dot("$C$",C,1.5*E,linewidth(4)); dot("$O_1$",O1,1.5*S,linewidth(4)); dot("$O_2$",O2,1.5*N,linewidth(4)); label("$3\sqrt6$",midpoint(A--B),scale(0.5)*rotate(90)*dir(midpoint(A--B)--A),red+fontsize(10)); label("$3\sqrt6$",midpoint(A--C),scale(0.5)*rotate(90)*dir(midpoint(A--C)--C),red+fontsize(10)); label("$5\sqrt2$",midpoint(O1--B),0.5*SW,red+fontsize(10)); label("$5\sqrt2$",midpoint(O1--C),0.5*SE,red+fontsize(10)); markscalefactor=0.05; draw(rightanglemark(A,B,O1)^^rightanglemark(A,C,O1),red); draw(A--B--O1--C--cycle^^B--C^^circumcircle(A,B,C)); [/asy] By the Inscribed Angle Theorem, we conclude that $\overline{AO_1}$ is the diameter of $\odot O_2.$ By the Pythagorean Theorem on right $\triangle ABO_1,$ we have \[AO_1 = \sqrt{AB^2 + BO_1^2} = 2\sqrt{26}.\] Therefore, the area of $\odot O_2$ is $\pi\cdot\left(\frac{AO_1}{2}\right)^2=\boxed{\textbf{(C) }26\pi}.$
~MRENTHUSIASM ~kante314

## Solution 2 (Similar Triangles)
[asy] import olympiad; unitsize(50); pair A,B,C,D,E,I,F,G,O; A=origin; B=(2,3); C=(-2,3); D=(4.3,6.3); E=(-4.3,6.3); F=(1,1.5); G=(-1,1.5); O=circumcenter(A,B,C); // olympiad - circumcenter I=incenter(A,D,E); draw(A--B--C--cycle); dot(O); dot(I); dot(F); dot(G); draw(circumcircle(A,B,C)); // olympiad - circumcircle draw(incircle(A,D,E)); draw(I--B); draw(I--C); draw(I--A); draw(rightanglemark(A,C,I)); draw(rightanglemark(A,B,I)); draw(O--F); draw(O--G); draw(rightanglemark(A,F,O)); draw(rightanglemark(A,G,O)); label("$O$",O,W); label("$A$",A,S); label("$B$",B,N); label("$C$",C,W); label("$D$",F,S); label("$E$",G,W); label("$3\sqrt{6}$",(1.5,1.5),S); label("$3\sqrt{6}$",(-1.5,1.5),S); label("$5\sqrt{2}$",(1,3.625),N); label("$5\sqrt{2}$",(-1,3.625),N); label("$I$",I,N); label("$r$",(-0.25,1.5),E); label("$r$",(0.5,2.125),S); add(pathticks(A--F,1,0.5,0,2)); add(pathticks(F--B,1,0.5,0,2)); add(pathticks(A--G,1,0.5,0,2)); add(pathticks(G--C,1,0.5,0,2)); [/asy] Because circle $I$ is tangent to $\overline{AB}$ at $B, \angle{ABI} \cong 90^{\circ}$ . Because $O$ is the circumcenter of $\bigtriangleup ABC, \overline{OD}$ is the perpendicular bisector of $\overline{AB}$ , and $\angle{BAI} \cong \angle{DAO}$ , so therefore $\bigtriangleup ADO \sim \bigtriangleup ABI$ by AA similarity. Then we have $\frac{AD}{AB} = \frac{DO}{BI} \implies \frac{1}{2} = \frac{r}{5\sqrt{2}} \implies r = \frac{5\sqrt{2}}{2}$ . We also know that $\overline{AD} = \frac{3\sqrt{6}}{2}$ because of the perpendicular bisector, so the hypotenuse of $\bigtriangleup ADO$ is \[\sqrt{\left(\frac{5\sqrt{2}}{2}\right)^2+\left(\frac{3\sqrt{6}}{2}\right)^2} = \sqrt{\frac{25}{2}+\frac{27}{2}} = \sqrt{26}.\] This is the radius of the circumcircle of $\bigtriangleup ABC$ , so the area of this circle is $\boxed{\textbf{(C) }26\pi}$ .
~KingRavi

## Solution 3 (Trigonometry)
Denote by $O$ the center of the circle that is tangent to line $AB$ at $B$ and to line $AC$ at $C$ .
Because this circle is tangent to line $AB$ at $B$ , we have $OB \perp AB$ and $OB = 5 \sqrt{2}$ .
Because this circle is tangent to line $AC$ at $C$ , we have $OC \perp AC$ and $OC = 5 \sqrt{2}$ .
Because $AB = AC$ , $OB = OC$ , $AO = AO$ , we get $\triangle ABO \cong \triangle ACO$ . Hence, $\angle BAO = \angle CAO$ .
Let $AO$ and $BC$ meet at point $D$ . Because $AB = AC$ , $\angle BAO = \angle CAO$ , $AD = AD$ , we get $\triangle ABD \cong \triangle ACD$ . Hence, $BD = CD$ and $\angle ADB = \angle ADC = 90^\circ$ .
Denote $\theta = \angle BAO$ . Hence, $\angle BAC = 2 \theta$ .
Denote by $R$ the circumradius of $\triangle ABC$ . In $\triangle ABC$ , following from the law of sines, $2 R = \frac{BC}{\sin \angle BAC}$ .
Therefore, the area of the circumcircle of $\triangle ABC$ is \begin{align*} \pi R^2 & = \pi \left( \frac{BC}{2 \sin \angle BAC} \right)^2 \\ & = \pi \left( \frac{2 BD}{2 \sin \angle BAC} \right)^2 \\ & = \pi \left( \frac{BD}{\sin 2 \theta} \right)^2 \\ & = \pi \left( \frac{AB \sin \theta }{\sin 2 \theta} \right)^2 \\ & = \pi \left( \frac{AB \sin \theta }{2 \sin \theta \cos \theta} \right)^2 \\ & = \pi \left( \frac{AB }{2 \cos \theta} \right)^2 \\ & = \pi \left( \frac{AO}{2} \right)^2 \\ & = \frac{\pi}{4} \left( AB^2 + OB^2 \right) \\ & = \boxed{\textbf{(C) }26\pi}. \end{align*} ~Steven Chen (www.professorchenedu.com)

## Solution 4 (Circumradius of a Right Triangle)
Label the center of the circle with radius $5\sqrt{2}$ as $O_2$ . Observe that both $\triangle ABO_2$ and $\triangle ABO_2$ are right triangles, as radii connecting the center of a circle to the point of tangency of a line are perpendicular to the line. Furthermore, these two triangles are congruent by SSS. Consider the midpoint of $\overline{AO_2}$ , letting it be $O_1$ . We prove that $O_2$ is the circumcenter of $\triangle ABC$ .
The radii of the circumcenters of $\triangle ABO_2$ and $\triangle ABO_2$ must be equal, as the two triangles are congruent. We recall that the midpoint of the hypotenuse of a right triangle is it's circumcenter, so $\overline{BO_1}$ and $\overline{CO_2}$ - as the radii of the circumcircles of their respective triangles - must be congruent. Furthermore, we have $\overline{BO_1} \cong \overline{AO_1}$ and $\overline{CO_1} \cong \overline{AO_1}$ , from the same fact, so $\overline{BO_1} \cong \overline{AO_1} \cong \overline{CO_1}$ . Thus, $O_1$ is the circumcenter of $\triangle ABC$ .
By the Pythagorean Theorem, $\overline{AO_2} = \sqrt{ (3\sqrt{6})^2 + (5\sqrt{2})^2 } = 2\sqrt{26}$ , so $\overline{AO_1}$ , the radius of the circle through points $A$ , $B$ , and $C$ is $\sqrt{26}$ , and thus the area of the circle is $\boxed{ (C) \ 26\pi }$ .
~LeonQS

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/T2VFw2lEthYqrt
~Education, the Study of Everything

## Video Solution by The Power of Logic
https://youtu.be/2lDDbOAmW18
~math2718281828459

## Video Solution
https://youtu.be/zq3UPu4nwsE?t=1674

## Video Solution
https://youtu.be/DVuf-uXjfzY?t=211
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .