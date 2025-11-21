# 2004 AMC 10B Problem 24

## Problem

In triangle $ABC$ we have $AB=7$ , $AC=8$ , $BC=9$ . Point $D$ is on the circumscribed circle of the triangle so that $AD$ bisects angle $BAC$ . What is the value of $\frac{AD}{CD}$ ?

$\text{(A) } \dfrac{9}{8} \qquad \text{(B) } \dfrac{5}{3} \qquad \text{(C) } 2 \qquad \text{(D) } \dfrac{17}{7} \qquad \text{(E) } \dfrac{5}{2}$

## Solution 1 (Ptolemy's Theorem)
Set $\overline{BD}$ 's length as $x$ . $\overline{CD}$ 's length must also be $x$ since $\angle BAD$ and $\angle DAC$ intercept arcs of equal length (because $\angle BAD=\angle DAC$ ). Using Ptolemy's Theorem , $7x+8x=9(AD)$ . The ratio is $\frac{5}{3}\implies\boxed{\text{(B)}}$

## Solution 2 (Similarity Proportion)
[asy] import graph; import geometry; import markers; unitsize(0.5 cm); pair A, B, C, D, E, I; A = (11/3,8*sqrt(5)/3); B = (0,0); C = (9,0); I = incenter(A,B,C); D = intersectionpoint(I--(I + 2*(I - A)), circumcircle(A,B,C)); E = extension(A,D,B,C); draw(A--B--C--cycle); draw(circumcircle(A,B,C)); draw(D--A); draw(D--B); draw(D--C); label("$A$", A, N); label("$B$", B, SW); label("$C$", C, SE); label("$D$", D, S); label("$E$", E, NE); markangle(radius = 20,B, A, C, marker(markinterval(2,stickframe(1,2mm),true))); markangle(radius = 20,B, C, D, marker(markinterval(1,stickframe(1,2mm),true))); markangle(radius = 20,D, B, C, marker(markinterval(1,stickframe(1,2mm),true))); markangle(radius = 20,C, B, A, marker(markinterval(1,stickframe(2,2mm),true))); markangle(radius = 20,C, D, A, marker(markinterval(1,stickframe(2,2mm),true))); [/asy] Let $E = \overline{BC}\cap \overline{AD}$ . Observe that $\angle ABC \cong \angle ADC$ because they both subtend arc $\overarc{AC}.$
Furthermore, $\angle BAE \cong \angle EAC$ because $\overline{AE}$ is an angle bisector, so $\triangle ABE \sim \triangle ADC$ by $\text{AA}$ similarity. Then $\dfrac{AD}{AB} = \dfrac{CD}{BE}$ . By the Angle Bisector Theorem , $\dfrac{7}{BE} = \dfrac{8}{CE}$ , so $\dfrac{7}{BE} = \dfrac{8}{9-BE}$ . This in turn gives $BE = \frac{21}{5}$ . Plugging this into the similarity proportion gives: $\dfrac{AD}{7} = \dfrac{CD}{\tfrac{21}{5}} \implies \dfrac{AD}{CD} = {\dfrac{5}{3}} = \boxed{\text{(B)}}$ .

## Solution 3 (Angle Bisector Theorem)
Similar to solution 2, let $E$ be the intersection of diagonals $AD$ and $BC$ . We know that $\overline{AD}$ bisects $\angle BAC$ , so $\angle BAD = \angle CAD$ . Additionally, $\angle BAD$ and $\angle BCD$ subtend the same arc, giving $\angle BAD = \angle BCD$ . Similarly, $\angle CAD = \angle CBD$ and $\angle ABC = \angle ADC$ .
These angle relationships tell us that $\triangle ABE\sim \triangle ADC$ by AA Similarity, so $AD/CD = AB/BE$ . By the angle bisector theorem, $AB/BE = AC/CE$ . Hence, \[\frac{AB}{BE} = \frac{AC}{CE} = \frac{AB + AC}{BE + CE} = \frac{AB + AC}{BC} = \frac{7 + 8}{9} = \frac{15}{9} = \boxed{\frac{5}{3}}.\]
--vaporwave
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .