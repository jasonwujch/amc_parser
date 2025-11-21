# 2022 AIME I Problem 10

## Problem

Three spheres with radii $11$ , $13$ , and $19$ are mutually externally tangent. A plane intersects the spheres in three congruent circles centered at $A$ , $B$ , and $C$ , respectively, and the centers of the spheres all lie on the same side of this plane. Suppose that $AB^2 = 560$ . Find $AC^2$ .

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(300); import graph3; import solids; currentprojection=orthographic((7,0.2,9)); triple A, B, C, OA, OB, OC; A = (0,0,0); B = (0,sqrt(560),0); C = intersectionpoints(Circle(A,sqrt(756),(0,0,1)),Circle(B,sqrt(960),(0,0,1)))[1]; OA = (0,0,4); OB = (0,sqrt(560),8); OC = (C.x,C.y,16); draw(shift(OC)*scale3(19)*unitsphere,green,light=Viewport); draw(shift(OA)*scale3(11)*unitsphere,red,light=Viewport); draw(shift(OB)*scale3(13)*unitsphere,yellow,light=Viewport); draw(Circle(A,sqrt(105),(0,0,1))^^Circle(B,sqrt(105),(0,0,1))^^Circle(C,sqrt(105),(0,0,1))); draw((-70,-20,0)--(-70,45,0)--(20,45,0)--(20,-20,0)--cycle); dot(OA^^OB^^OC,linewidth(4.5)); dot("$A$",A,(0,1,0),linewidth(4.5)); dot("$B$",B,(0,1,0),linewidth(4.5)); dot("$C$",C,(0,1.5,0),linewidth(4.5)); [/asy] ~MRENTHUSIASM

## Solution 1
This solution refers to the Diagram section.
We let $\ell$ be the plane that passes through the spheres and $O_A$ and $O_B$ be the centers of the spheres with radii $11$ and $13$ . We take a cross-section that contains $A$ and $B$ , which contains these two spheres but not the third, as shown below: [asy] size(400); pair A, B, OA, OB; B = (0,0); A = (-23.6643191,0); OB = (0,8); OA = (-23.6643191,4); draw(circle(OB,13)); draw(circle(OA,11)); draw((-48,0)--(24,0)); label("$\ell$",(-42,0),S); label("$A$",A,S); label("$B$",B,S); label("$O_A$",OA,N); label("$O_B$",OB,N); draw(A--OA); draw(B--OB); draw(OA--OB); draw(OA--(0,4)); draw(OA--(-33.9112699,0)); draw(OB--(10.2469508,0)); label("$24$",midpoint(OA--OB),N); label("$\sqrt{560}$",midpoint(A--B),S); label("$11$",midpoint(OA--(-33.9112699,0)),NW); label("$13$",midpoint(OB--(10.2469508,0)),NE); label("$r$",midpoint(midpoint(A--B)--A),S); label("$r$",midpoint(midpoint(A--B)--B),S); label("$r$",midpoint(A--(-33.9112699,0)),S); label("$r$",midpoint(B--(10.2469508,0)),S); label("$x$",midpoint(midpoint(B--OB)--OB),W); label("$D$",midpoint(B--OB),E); [/asy] Because the plane cuts out congruent circles, they have the same radius and from the given information, $AB = \sqrt{560}$ . Since $ABO_BO_A$ is a trapezoid, we can drop an altitude from $O_A$ to $BO_B$ to create a rectangle and triangle to use Pythagorean theorem. We know that the length of the altitude is $\sqrt{560}$ and let the distance from $O_B$ to $D$ be $x$ . Then we have $x^2 = 576-560 \implies x = 4$ .
We have $AO_A = BD$ because of the rectangle, so $\sqrt{11^2-r^2} = \sqrt{13^2-r^2}-4$ . Squaring, we have $121-r^2 = 169-r^2 + 16 - 8 \cdot \sqrt{169-r^2}$ . Subtracting, we get $8 \cdot \sqrt{169-r^2} = 64 \implies \sqrt{169-r^2} = 8 \implies 169-r^2 = 64 \implies r^2 = 105$ . We also notice that since we had $\sqrt{169-r^2} = 8$ means that $BO_B = 8$ and since we know that $x = 4$ , $AO_A = 4$ .
We take a cross-section that contains $A$ and $C$ , which contains these two spheres but not the third, as shown below: [asy] size(400); pair A, C, OA, OC, M; C = (0,0); A = (-27.4954541697,0); OC = (0,16); OA = (-27.4954541697,4); M = midpoint(A--C); draw(circle(OC,19)); draw(circle(OA,11)); draw((-48,0)--(24,0)); label("$\ell$",(-42,0),S); label("$A$",A,S); label("$C$",C,S); label("$O_A$",OA,N); label("$O_C$",OC,N); draw(A--OA); draw(C--OC); draw(OA--OC); draw(OA--(0,4)); draw(OA--(-37.8877590151,0)); draw(OC--(10.2469508,0)); label("$30$",midpoint(OA--OC),NW); label("$11$",midpoint(OA--(-37.8877590151,0)),NW); label("$19$",midpoint(OC--(10.2469508,0)),NE); label("$r$",midpoint(midpoint(M--A)--A),S); label("$r$",midpoint(midpoint(M--C)--C),S); label("$r$",midpoint(A--(-37.8877590151,0)),S); label("$r$",midpoint(C--(10.2469508,0)),S); label("$E$",(0,4),E); [/asy] We have $CO_C = \sqrt{19^2-r^2} = \sqrt{361 - 105} = \sqrt{256} = 16$ . Since $AO_A = 4$ , we have $EO_C = 16-4 = 12$ . Using Pythagorean theorem, $O_AE = \sqrt{30^2 - 12^2} = \sqrt{900-144} = \sqrt{756}$ . Therefore, $O_AE^2 = AC^2 = \boxed{756}$ .
~KingRavi

## Solution 2
Let the distance between the center of the sphere to the center of those circular intersections as $a,b,c$ separately.
According to the problem, we have $a^2-11^2=b^2-13^2=c^2-19^2; (11+13)^2-(b-a)^2=560.$ After solving we have $b-a=4,$ plug this back to $11^2-a^2=13^2-b^2,$ we have $a=4, b=8,$ and $c=16.$
The desired value is $(11+19)^2-(16-4)^2=\boxed{756}.$
~bluesoul

## Solution 3
Denote by $r$ the radius of three congruent circles formed by the cutting plane. Denote by $O_A$ , $O_B$ , $O_C$ the centers of three spheres that intersect the plane to get circles centered at $A$ , $B$ , $C$ , respectively.
Because three spheres are mutually tangent, $O_A O_B = 11 + 13 = 24$ , $O_A O_C = 11 + 19 = 30$ .
We have $O_A A^2 = 11^2 - r^2$ , $O_B B^2 = 13^2 - r^2$ , $O_C C^2 = 19^2 - r^2$ .
Because $O_A A$ and $O_B B$ are perpendicular to the plane, $O_A AB O_B$ is a right trapezoid, with $\angle O_A A B = \angle O_B BA = 90^\circ$ .
Hence, \begin{align*} O_B B - O_A A & = \sqrt{O_A O_B^2 - AB^2} \\ & = 4 . \hspace{1cm} (1) \end{align*}
Recall that \begin{align*} O_B B^2 - O_A A^2 & = \left( 13^2 - r^2 \right) - \left( 11^2 - r^2 \right) \\ & = 48 . \hspace{1cm} (2) \end{align*}
Hence, taking $\frac{(2)}{(1)}$ , we get \[ O_B B + O_A A = 12 . \hspace{1cm} (3) \]
Solving (1) and (3), we get $O_B B = 8$ and $O_A A = 4$ .
Thus, $r^2 = 11^2 - O_A A^2 = 105$ .
Thus, $O_C C = \sqrt{19^2 - r^2} = 16$ .
Because $O_A A$ and $O_C C$ are perpendicular to the plane, $O_A AC O_C$ is a right trapezoid, with $\angle O_A A C = \angle O_C CA = 90^\circ$ .
Therefore, \begin{align*} AC^2 & = O_A O_C^2 - \left( O_C C - O_A A \right)^2 \\ & = \boxed{756}. \end{align*}
$\textbf{FINAL NOTE:}$ In our solution, we do not use the condition that spheres $A$ and $B$ are externally tangent. This condition is redundant in solving this problem.
$\textbf{MORE FINAL NOTE:}$ the above note is incorrect because that condition was used at the start when claiming $O_AO_B=24$ . Perhaps the note is referring to spheres $B$ and $C$ .
~Steven Chen (www.professorcheneeu.com)
~anonymous (minor edits)

## Video Solution (Challenge 25)
https://www.youtube.com/watch?v=yeuJDQ1LTlY

## Video Solution
https://www.youtube.com/watch?v=SqLiV2pbCpY&t=15s
~Steven Chen (www.professorcheneeu.com)

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=HbBU13YiopU
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .