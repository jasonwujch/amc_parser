# 2017 AMC 10A Problem 22

## Problem

Sides $\overline{AB}$ and $\overline{AC}$ of equilateral triangle $ABC$ are tangent to a circle at points $B$ and $C$ respectively. What fraction of the area of $\triangle ABC$ lies outside the circle?

$\textbf{(A) } \frac{4\sqrt{3}\pi}{27}-\frac{1}{3}\qquad \textbf{(B) } \frac{\sqrt{3}}{2}-\frac{\pi}{8}\qquad \textbf{(C) } \frac{1}{2} \qquad \textbf{(D) } \sqrt{3}-\frac{2\sqrt{3}\pi}{9}\qquad \textbf{(E) } \frac{4}{3}-\frac{4\sqrt{3}\pi}{27}$

## Solution 1
[asy] real sqrt3 = 1.73205080757; draw(Circle((4, 4), 4)); draw((4-2*sqrt3,6)--(4,4)--(4+2*sqrt3,6)--(4-2*sqrt3,6)--(4,12)--(4+2*sqrt3,6)); label("A", (4, 12.4)); label("B", (-.3, 6.3)); label("C", (8.3, 6.3)); label("O", (4, 3.4)); [/asy] Let the radius of the circle be $r$ , and let its center be $O$ . Since $\overline{AB}$ and $\overline{AC}$ are tangent to circle $O$ , then $\angle OBA = \angle OCA = 90^{\circ}$ , so $\angle BOC = 120^{\circ}$ . Therefore, since $\overline{OB}$ and $\overline{OC}$ are equal to $r$ , then (pick your favorite method) $\overline{BC} = r\sqrt{3}$ . The area of the equilateral triangle is $\frac{(r\sqrt{3})^2 \sqrt{3}}4 = \frac{3r^2 \sqrt{3}}4$ , and the area of the sector we are subtracting from it is $\frac 13 \pi r^2 - \frac 12 \cdot r\sqrt{3} \cdot \frac{r}2 = \frac{\pi r^2}3 -\frac{r^2 \sqrt{3}}4$ . The area outside of the circle is $\frac{3r^2 \sqrt{3}}4-\left(\frac{\pi r^2}3 -\frac{r^2 \sqrt{3}}4\right) = r^2 \sqrt{3} - \frac{\pi r^2}3$ . Therefore, the answer is \[\frac{r^2 \sqrt{3} - \frac{\pi r^2}3}{\frac{3r^2 \sqrt{3}}4} = \boxed{\textbf{(E) } \frac 43 - \frac{4\sqrt 3 \pi}{27}}\]
### Note
The sector angle is $120$ because $\angle B$ and $\angle C$ are both 90 degrees meaning $\angle B + \angle C = 180^\circ$ , so $ABCO$ is cyclic. Thus, the angle is $180-60=120^\circ$
~mathboy282
Alternately, $\angle ABC$ is $60^\circ$ and $\angle ABO$ is $90^\circ$ , making $\angle CBO$ $30^\circ$ . Symmetry allows us to use the same argument to get $\angle BCO = 30^\circ$ . Since the interior angles of $\triangle BCO$ must sum to $180^\circ$ , that leaves $120^\circ$ for central angle $\angle BOC$ .
— wescarroll
~ Shreyansh
### Multiple Choice Shortcut
Assuming WLoG that the equilateral triangle's side length $s$ and therefore area $A$ are algebraic (" $\pi$ -free"):
The "crust" is a circle sector minus a triangle, so its area is $a \pi - b$ , where $a$ and $b$ are algebraic. Thus the answer is $(A - (a \pi -b))/A = (A+b)/A - a\pi/A$ .
Once you see that $s$ is $\sqrt{3} \times$ the circle's radius, and that the circle's 30°-30°-120° triangle is two halves of an equilateral triangle, infer that the smaller circle-sector triangle's area is $A/(\sqrt 3)^2 = A/3$ , and so the algebraic part of the answer $(A+b)/A = (A - (-A/3)) /A = 4/3$ .
The transcendental (" $\pi$ ") part of the answer is $-a \pi /A$ , and since $a$ and $A$ are algebraic, $\textbf{(E)}$ is the only compatible answer choice.

## Solution 2
[asy] real sqrt3 = 1.73205080757; draw(Circle((4, 4), 4)); draw((4-2*sqrt3,6)--(4,4)--(4+2*sqrt3,6)--(4-2*sqrt3,6)--(4,12)--(4+2*sqrt3,6)); draw((4, 6)--(4, 4)); label("A", (4, 12.4)); label("B", (-.3, 6.3)); label("C", (8.3, 6.3)); label("O", (4, 3.4)); label("D", (4, 6.6)); [/asy] (same diagram as Solution 1)
Without the Loss of Generality, let the side length of the triangle be $1$ .
Then, the area of the triangle is $\frac{\sqrt{3}}{4}$ . We are looking for the area of the portion inside the triangle but outside the circle divided by the area of the triangle. Since $m\angle ABO = 90^{\circ}=m\angle ACO = 90^{\circ}$ , and $m\angle ABC = m\angle ACB = 60^{\circ}$ , we know $m\angle OBC=m\angle OCB=30^{\circ}$ , and $m\angle BOC = 120^{\circ}$ . Drop an angle bisector of $O$ onto $BC$ , call the point of intersection $D$ . By SAS congruence, $\triangle BDO \cong \triangle CDO$ , by CPCTC (Congruent Parts of Congruent Triangles are Congruent) $BD \cong DC$ and they both measure $\frac{1}{2}$ . By 30-60-90 triangle, $OC = BO = \frac{\sqrt{3}}{3}$ . The area of the sector bounded by arc BC is one-third the area of circle O, whose area is $\left(\frac{\sqrt{3}}{3}\right)^{2}\pi=\frac{1}{3}\pi$ . Therefore, the area of the sector bounded by arc BC is $\frac{1}{3}\cdot\frac{1}{3}\pi=\frac{\pi}{9}$ .
We are nearly there. By 30-60-90 triangle, we know $DO = \frac{\sqrt{3}}{6}$ , so the area of $\triangle BOC$ is $\frac{1\cdot\frac{\sqrt{3}}{6}}{2}=\frac{\sqrt{3}}{12}$ . The area of the region inside both the triangle and circle is the area of the sector bounded by arc BC minus the area of $\triangle BOC$ : $\frac{\pi}{9}-\frac{\sqrt{3}}{12}$ . The area of the region outside of the circle but inside the triangle is $\frac{\sqrt{3}}{4}-\left(\frac{\pi}{9}-\frac{\sqrt{3}}{12}\right)=\frac{\sqrt{3}}{4}-\frac{\pi}{9}+\frac{\sqrt{3}}{12}=\frac{\sqrt{3}}{3}-\frac{\pi}{9}$ and the ratio is $\frac{\frac{\sqrt{3}}{3}-\frac{\pi}{9}}{\frac{\sqrt{3}}{4}}=\left(\frac{\sqrt{3}}{3}-\frac{\pi}{9}\right)\cdot\frac{4}{\sqrt{3}}=\frac{4\sqrt{3}}{3\sqrt{3}}-\frac{4\pi}{9\sqrt{3}}=\frac{4}{3}-\frac{4\sqrt{3}\pi}{27} \Longrightarrow \boxed{\textbf{(E) } \frac 43 - \frac{4\sqrt 3 \pi}{27}}$ .
~JH. L

## Video Solution by Pi Academy
https://youtu.be/kWuHeHeroz0?si=xctneBvOXPE23YxC
~ Pi Academy

## Video Solution
https://www.youtube.com/watch?v=GnJDNtjd57k&feature=youtu.be
https://youtu.be/ADDAOhNAsjQ -Video Solution by Richard Rusczyk
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .