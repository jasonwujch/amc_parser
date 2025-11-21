# 2002 AMC 12P Problem 24

## Problem

Let $ABCD$ be a regular tetrahedron and Let $E$ be a point inside the face $ABC.$ Denote by $s$ the sum of the distances from $E$ to the faces $DAB, DBC, DCA,$ and by $S$ the sum of the distances from $E$ to the edges $AB, BC, CA.$ Then $\frac{s}{S}$ equals

$\text{(A) }\sqrt{2} \qquad \text{(B) }\frac{2 \sqrt{2}}{3} \qquad \text{(C) }\frac{\sqrt{6}}{2} \qquad \text{(D) }2 \qquad \text{(E) }3$

## Solution
Assume points $P$ , $Q$ , and $R$ are on faces $ABD$ , $ACD$ , and $BCD$ respectively such that $EP \perp ABD$ , $EQ \perp ACD$ , and $ER \perp BCD$ .
Assume points $S$ , $T$ , and $U$ are on edges $AB$ , $AC$ , and $BC$ respectively such that $ES \perp AB$ , $ET \perp AC$ , and $EU \perp BC$ .
Consider triangles $EPS$ , $EQT$ , and $ERU$ . Each of these triangles have a right angle and an angle equal to the dihedral angle of the tetrahedron, so they are all similar by AA similarity. In particular, we know that $\frac{EP}{ES} = \frac{EQ}{ET} = \frac{ER}{EU} = \frac{EP+EQ+ER}{ES+ET+EU} = \frac{s}{S}$ .
It remains to find $\frac{EP}{ES}$ , or equivalently, $\sin(\angle DSE)$ .
We know $SE = \frac{1}{3}DS$ by the centroid property. Therefore, $\cos(\angle DSE) = \frac{1}{3}$ , so $\sin(\angle DSE) = \sqrt{1-\left(\frac{1}{3}\right)^2} = \boxed {\text{(B) }\frac{2 \sqrt{2}}{3}}$ .

## Solution 2(Cheesy)
Continue to assume points $P$ , $Q$ , and $R$ are on faces $ABD$ , $ACD$ , and $BCD$ respectively such that $EP \perp ABD$ , $EQ \perp ACD$ , and $ER \perp BCD$ and assume points $S$ , $T$ , and $U$ are on edges $AB$ , $AC$ , and $BC$ respectively such that $ES \perp AB$ , $ET \perp AC$ , and $EU \perp BC$ .
Now, because they never specify where E has to be or how long the tetrahedron's sides must be, WLOG, assume E is the centroid/incenter/circumcenter/orthocenter of triangle ABC and the side length of the tetrahedron is $2$ Note that the inradius of ABC is the same as $ES=ET=EU.$ Then the inradius of $\triangle\text{ABC}$ are $\frac{\sqrt3}{6}\cdot 2=\frac{\sqrt3}{3}.$
Next, take cross section $\triangle\text{SDC}.$ Since $ES$ is an inradius, $ES=\frac{\sqrt3}{3}.$ Since $SD$ is an altitude of $\triangle\text{DAB}$ and $SC$ is an altitude of $\triangle\text{ABC}$ , $SC=SD=\frac{\sqrt3}{2}\cdot 2=\sqrt3.$ Thus, by the Pythagorean theorem, $ED=\sqrt{SD^2-ES^2}=\sqrt{\sqrt{3}^2-\frac{\sqrt{3}^2}{3^2}}=\sqrt{3-\frac13}=\sqrt{\frac83}=\frac{2\sqrt6}{3}.$
Then, because $\angle{SED}=\angle{SQE}=90^\circ$ and $\angle{ESD}=\angle{QSE},$ $\triangle{SED}~\triangle{SQE}$ by AA Similarity. Then, since $ES=\frac{SD}3=\frac{\sqrt3}3,$ $EQ=\frac{ED}3=\frac{\frac{2\sqrt6}3}{3}=\frac{2\sqrt6}9.$
Then, $s=3\cdot EQ=3\cdot\frac{2\sqrt6}9=\frac{2\sqrt6}3$ and $S=3\cdot\text{inradius}=3\cdot\frac{\sqrt3}3=\sqrt3.$ Thus, $\frac{s}{S}=\frac{\frac{2\sqrt6}3}{\sqrt3}=\frac{2\sqrt2}3=\boxed{\text{(B)}}.$
~~AndrewZhong2012~~
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .