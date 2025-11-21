# 2019 AMC 10A Problem 13

## Problem

Let $\triangle ABC$ be an isosceles triangle with $BC = AC$ and $\angle ACB = 40^{\circ}$ . Construct the circle with diameter $\overline{BC}$ , and let $D$ and $E$ be the other intersection points of the circle with the sides $\overline{AC}$ and $\overline{AB}$ , respectively. Let $F$ be the intersection of the diagonals of the quadrilateral $BCDE$ . What is the degree measure of $\angle BFC ?$

$\textbf{(A) } 90 \qquad\textbf{(B) } 100 \qquad\textbf{(C) } 105 \qquad\textbf{(D) } 110 \qquad\textbf{(E) } 120$

## Solution 1
[asy] unitsize(40);draw((-1,0)--(1,0)--(0,2.75)--cycle);draw(circumcircle((-1,0),(0,0),(0,2.75)));label("$A$",(1,0),SE);label("$C$",(0,2.75),N);label("$B$",(-1,0),SW);label("$E$",(0,0),S);label("$D$",(0.77,0.64),E);draw((0,0)--(0,2.75));draw((-1,0)--(0.77,0.64));[/asy]
Drawing it out, we see $\angle BDC$ and $\angle BEC$ are right angles, as they are inscribed in a semicircle. Using the fact that it is an isosceles triangle, we find $\angle ABC=70^{\circ}$ . We can find $\angle ECB=20^{\circ}$ and $\angle DBC=50^{\circ}$ by the triangle angle sum on $\triangle ECB$ and $\triangle DBC$ .
\[\angle BDC+\angle DCB+\angle DBC=180^{\circ}\implies90^{\circ}+40^{\circ}+\angle DBC=180^{\circ}\implies\angle DBC=50^{\circ}\]
\[\angle BEC+\angle EBC+\angle ECB=180^{\circ}\implies90^{\circ}+70^{\circ}+\angle ECB=180^{\circ}\implies\angle ECB=20^{\circ}\]
Then, we take triangle $BFC$ , and find $\angle BFC=180^{\circ}-50^{\circ}-20^{\circ}=\boxed{\textbf{(D) } 110^{\circ}}.$

## Solution 2
Alternatively, we could have used similar triangles. We start similarly to Solution 1.
Drawing it out, we see $\angle BDC$ and $\angle BEC$ are right angles, as they are inscribed in a semicircle. Therefore, \[\angle BDA = 180^{\circ} - \angle BDC = 180^{\circ} - 90^{\circ} = 90^{\circ}.\]
So, $\triangle BEF \sim BDA$ by AA Similarity, since $\angle EBF = \angle DBA$ and $\angle BEC = 90^{\circ} = \angle BDA$ . Thus, we know \[\angle EFB = \angle DAB = \angle CAB = 70^{\circ}.\]
Finally, we deduce \[\angle BFC = 180^{\circ} - \angle EFB = 180^{\circ} - 70^{\circ} = \boxed{\textbf{(D) } 110^{\circ}}.\]

## Solution 3 (outside angles)
Through the property of angles formed by intersecting chords, we find that \[m\angle BFC=\frac{m\overarc{BC}+m\overarc{DE}}{2}\]
Through the Outside Angles Theorem, we find that \[m\angle CAB = \frac{m\overarc{BC}-m\overarc{DE}}{2}\]
Adding the two equations gives us \[m\angle BFC + m\angle CAB = m\overarc{BC}\implies m\angle BFC=m\overarc{BC} - m\angle CAB\]
Since $\overarc{BC}$ is the diameter, $m\overarc{BC}=180^{\circ}$ , and because $\triangle ABC$ is isosceles and $m\angle ACB=40^{\circ}$ , we have $m\angle CAB=70^{\circ}$ . Thus \[m\angle BFC=180^{\circ}-70^{\circ}=\boxed{\textbf{(D) } 110^{\circ}}\]

## Solution 4
Notice that if $\angle BEC = 90^{\circ}$ , then $\angle BCE$ and $\angle ACE$ must be $20^{\circ}$ . Using cyclic quadrilateral properties (or the properties of a subtended arc), we can find that $\angle EBD \cong \angle ECD = 20^{\circ}$ . Thus $\angle CBF = 70 - 20 = 50^{\circ}$ , and so $\angle BFC = 180 - 20 - 50 = 110^{\circ}$ , which is $\boxed{\textbf{(D)}}$ .

## Solution 5
$\triangle{ABC}$ is isosceles so $\angle{CAB}=70^{\circ}$ . Since $CB$ is a diameter, $\angle{CDB}=\angle{CEB}=90^{\circ}$ . Quadrilateral $ADFE$ is cyclic since $\angle{ADF}+\angle{AEF}=180^{\circ}$ . Therefore $\angle{BFC}=\angle{DFE}=180^{\circ}-\angle{CAB}=\boxed{110^{\circ}}$

## Solution 6 (Different approach to solution 3)
Label the center of the circle \( M \). Then, we can say that angle \( DME \) must be congruent to angle \( DAE \) as they both share the same arc \( DE \). So therefore angle \( DME = 70^\circ \). The angle \( CFB \) is inscribed on the diameter, but it doesn't touch the circumference of the circle. Therefore angle \( DME \) is supplementary to angle \( CFB \), so our answer is \( 180^\circ - DME = 180^\circ - 70^\circ = \) $\boxed{110^{\circ}}$ .
~Pinotation

## Solution 7 (Properties of an isosceles triangle)
$\angle{BEC}=90$ (Thales Theorem)
$\angle{BEC} bisects \angle{ACB}$ (Properties of the altitude of an isosceles triangle)
~I don't know what this is specifically called but the altitude is perpendicular and bisects the angle, forming two congruent right triangles
$\angle{ECD}=20$
$\angle{BDC}=90$ (Thales Theorem)
$\angle{CFD} = 180 - 90 - 20 = 70$ (Interior angles of a triangle)
$\boxed{\angle{BFC} = 110}$ (Linear Pair)

## Video Solution by OmegaLearn
https://youtu.be/O_o_-yjGrOU?t=849
~ pi_is_3.14

## Video Solution
https://youtu.be/GmQIEX4Izt4
Education, the Study of Everything

## Video Solution by TheBeautyofMath
https://youtu.be/KXwjFdwrfqk Includes small notebook concept summary, and where to learn the concepts in longer format.
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .