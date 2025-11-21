# 2022 AMC 10A Problem 13

## Problem

Let $\triangle ABC$ be a scalene triangle. Point $P$ lies on $\overline{BC}$ so that $\overline{AP}$ bisects $\angle BAC.$ The line through $B$ perpendicular to $\overline{AP}$ intersects the line through $A$ parallel to $\overline{BC}$ at point $D.$ Suppose $BP=2$ and $PC=3.$ What is $AD?$

$\textbf{(A) } 8 \qquad \textbf{(B) } 9 \qquad \textbf{(C) } 10 \qquad \textbf{(D) } 11 \qquad \textbf{(E) } 12$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(300); real r = 4*sqrt(114)/13; pair A, B, C, D, P, X, Y; A = origin; B = (2,r); C = (3/2*sqrt(2^2+r^2),0); D = A + 2*(C-B); P = B + 2*dir(C-B); X = intersectionpoint(B--D,A--P); Y = intersectionpoint(B--D,A--C); dot("$A$",A,1.5*W,linewidth(4)); dot("$B$",B,1.5*N,linewidth(4)); dot("$C$",C,1.5*E,linewidth(4)); dot("$P$",P,1.5*dir(P),linewidth(4)); dot("$D$",D,1.5*dir(D),linewidth(4)); dot(X^^Y,linewidth(4)); markscalefactor=0.03; draw(rightanglemark(B,X,A),red); draw(anglemark(P,A,B,20), red); draw(anglemark(C,A,P,20), red); add(pathticks(anglemark(P,A,B,20), n = 1, r = 0.1, s = 7, red)); add(pathticks(anglemark(C,A,P,20), n = 1, r = 0.1, s = 7, red)); draw(A--B--C--cycle^^A--P^^B--D^^A--D); draw(B--C,MidArrow(0.3cm,Fill(red))); draw(A--D,MidArrow(0.3cm,Fill(red))); label("$2$",midpoint(B--P),rotate(90)*dir(midpoint(P--B)--P),red); label("$3$",midpoint(P--C),rotate(90)*dir(midpoint(C--P)--C),red); [/asy] ~MRENTHUSIASM

## Solution 1 (Angle Bisector Theorem and Similar Triangles)
Suppose that $\overline{BD}$ intersects $\overline{AP}$ and $\overline{AC}$ at $X$ and $Y,$ respectively. By Angle-Side-Angle, we conclude that $\triangle ABX\cong\triangle AYX.$
Let $AB=AY=2x.$ By the Angle Bisector Theorem, we have $AC=3x,$ or $YC=x.$
By alternate interior angles, we get $\angle YAD=\angle YCB$ and $\angle YDA=\angle YBC.$ Note that $\triangle ADY \sim \triangle CBY$ by the Angle-Angle Similarity, with the ratio of similitude $\frac{AY}{CY}=2.$ It follows that $AD=2CB=2(BP+PC)=\boxed{\textbf{(C) } 10}.$
~MRENTHUSIASM

## Solution 2 (No Angle Bisectors!)
We can draw lines from \( C \) to a new point \( E \), and extend the line \( BC \) to a point \( F \) such that the lines \( FD \), \( CE \) and \( AB \) are parallel.
Notice how we have two parallelograms, but more specifically, these parallelograms are just made up of \( 2 \times \triangle ABC \). We see that the parallelograms \( ABCE \) and \( ECFD \) are congruent, and therefore \( BC \cong AE \cong CF \cong ED \). \( BC = 5 \), so \( AE = 5 \), and because \( AE \cong ED \), we have \( ED = 5 \).
Finally, we have \( AE + ED = AD \), so \( AD = 5 + 5 =\) $\boxed{\textbf{(C) } 10}.$
And just like that! No angle bisectors needed! 😁
~Pinotation
~Image adopted from MRENTHUSIASM, thank you so much!

## Solution 3 (Auxiliary Lines)
Let the intersection of $AC$ and $BD$ be $M$ , and the intersection of $AP$ and $BD$ be $N$ . Draw a line from $M$ to $BC$ , and label the point of intersection $O$ .
By adding this extra line, we now have many pairs of similar triangles. We have $\triangle BPN \sim \triangle BOM$ , with a ratio of $2$ , so $BO = 4$ and $OC = 1$ . We also have $\triangle COM \sim \triangle CAP$ with ratio $3$ . Additionally, $\triangle BPN \sim \triangle ADN$ (with an unknown ratio). It is also true that $\triangle BAN \cong \triangle MAN$ .
Suppose the area of $\triangle COM$ is $x$ . Then, $[\triangle CAP] = 9x$ . Because $\triangle CAP$ and $\triangle BAP$ share the same height and have a base ratio of $3:2$ , $[\triangle BAP] = 6x$ . Because $\triangle BOM$ and $\triangle COM$ share the same height and have a base ratio of $4:1$ , $[\triangle BOM] = 4x$ , $[\triangle BPN] = x$ , and thus $[OMNP] = 4x - x = 3x$ . Thus, $[\triangle MAN] = [\triangle BAN] = 5x$ .
Finally, we have $\frac{[\triangle BAN]}{[\triangle BPN]} = \frac{5x}{x} = 5$ , and because these triangles share the same height $\frac{AN}{PN} = 5$ . Notice that these side lengths are corresponding side lengths of the similar triangles $BPN$ and $ADN$ . This means that $AD = 5\cdot BP = \boxed{\textbf{(C) } 10}$ .
~mathboy100

## Solution 4 (Slopes)
Let point $B$ be the origin, with $C$ being on the positive $x$ -axis and $A$ being in the first quadrant.
By the Angle Bisector Theorem, $AB:AC = 2:3$ . Thus, assume that $AB = 4$ , and $AC = 6$ .
Let the perpendicular from $A$ to $BC$ be $AM$ .
Using Heron's formula, \[[ABC] = \sqrt{\frac{15}{2}\left(\frac{15}{2}-4\right)\left(\frac{15}{2}-5\right)\left(\frac{15}{2}-6\right)} = \frac{15}{4}\sqrt{7}.\]
Hence, \[AM = \frac{\frac{15}{4}\sqrt{7}}{\frac{5}{2}} = \frac{3}{2}\sqrt{7}.\]
Next, we have \[BM^2 + AM^2 = AB^2\] \[\therefore BM = \sqrt{16 - \frac{63}{4}} = \sqrt{\frac{1}{4}} = \frac{1}{2} \textrm{ and } PM = \frac{3}{2}.\]
The slope of line $AP$ is thus \[\frac{-\frac{3}{2}\sqrt{7}}{\frac{3}{2}} = -\sqrt{7}.\]
Therefore, since the slopes of perpendicular lines have a product of $-1$ , the slope of line $BD$ is $\frac{1}{\sqrt{7}}$ . This means that we can solve for the coordinates of $D$ :
\[y = \frac{3}{2}\sqrt{7}\] \[y = \frac{1}{\sqrt{7}}x\] \[\frac{1}{\sqrt{7}}x = \frac{3}{2}\sqrt{7}\] \[x = \frac{7 \cdot 3}{2} = \frac{21}{2}\] \[D = \left(\frac{21}{2}, \frac{3}{2}\sqrt{7}\right).\]
We also know that the coordinates of $A$ are $\left(\frac{1}{2}, \frac{3}{2}\sqrt{7}\right)$ , because $BM = \frac{1}{2}$ and $AM = \frac{3}{2}\sqrt{7}$ .
Since the $y$ -coordinates of $A$ and $D$ are the same, and their $x$ -coordinates differ by $10$ , the distance between them is $10$ . Our answer is $\boxed{\textbf{(C) }10}.$
~mathboy100

## Solution 5 (Assumption)
[asy] size(300); pair A, B, C, P, XX, D; B = (0,0); P = (2,0); C = (5,0); A=(0,4.47214); D = A + (10,0); draw(A--B--C--cycle, linewidth(1)); dot("$A$", A, N); dot("$B$", B, SW); dot("$C$", C, E); dot("$P$", P, S); dot("$D$", D, E); markscalefactor = 0.1; draw(anglemark(B,A,P)); markscalefactor = 0.12; draw(anglemark(P,A,C)); draw(P--A--D--B, linewidth(1)); XX = intersectionpoints(A--P,B--D)[0]; dot("$X$", XX, dir(150)); markscalefactor = 0.03; draw(rightanglemark(A,B,C)); draw(rightanglemark(D,XX,P)); [/asy] Since there is only one possible value of $AD$ , we assume $\angle{B}=90^{\circ}$ . By the angle bisector theorem, $\frac{AB}{AC}=\frac{2}{3}$ , so $AB=2\sqrt{5}$ and $AC=3\sqrt{5}$ . Now observe that $\angle{BAD}=90^{\circ}$ . Let the intersection of $BD$ and $AP$ be $X$ . Then $\angle{ABD}=90^{\circ}-\angle{BAX}=\angle{APB}$ . Consequently, \[\bigtriangleup DAB \sim \bigtriangleup ABP\] and therefore $\frac{DA}{AB} = \frac{AB}{BP}$ , so $AD=\boxed{\textbf{(C) }10}$ , and we're done!
~ Bxiao31415

## Video Solution 1
https://youtu.be/m1-7E8T_i_E
~Education, the Study of Everything

## Video Solution 3
https://youtu.be/77JIN0iVizA

## Video Solution 4
https://youtu.be/G8NRcVxSdz0

## Video Solution 5 by SpreadTheMathLove
https://www.youtube.com/watch?v=nhlpSATltRU
~Ismail.maths93

## Video Solution 6 by Lucas637
https://www.youtube.com/watch?v=R1CtcZ2pWVk
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .