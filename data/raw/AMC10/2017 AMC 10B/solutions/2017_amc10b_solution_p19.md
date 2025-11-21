# 2017 AMC 10B Problem 19

## Problem

Let $ABC$ be an equilateral triangle. Extend side $\overline{AB}$ beyond $B$ to a point $B'$ so that $BB'=3 \cdot AB$ . Similarly, extend side $\overline{BC}$ beyond $C$ to a point $C'$ so that $CC'=3 \cdot BC$ , and extend side $\overline{CA}$ beyond $A$ to a point $A'$ so that $AA'=3 \cdot CA$ . What is the ratio of the area of $\triangle A'B'C'$ to the area of $\triangle ABC$ ?

$\textbf{(A)}\ 9:1\qquad\textbf{(B)}\ 16:1\qquad\textbf{(C)}\ 25:1\qquad\textbf{(D)}\ 36:1\qquad\textbf{(E)}\ 37:1$

### Diagram

[asy] size(12cm); real a = 1; pair A = (0, 0), B = rotate(60)*A + (a, 0), C = rotate(120)*B + (a, 0); // calculate extended points pair A_prime = A + 3*(A - C); pair B_prime = B + 3*(B - A); pair C_prime = C + 3*(C - B); // draw original triangle and extended triangle draw(A--B--C--cycle); draw(A--A_prime); draw(B--B_prime); draw(C--C_prime); draw(A_prime--B_prime--C_prime--cycle); // label points dot("$A$", A, SE); dot("$B$", B, NE); dot("$C$", C, W); dot("$A'$", A_prime, SW); dot("$B'$", B_prime, NE); dot("$C'$", C_prime, W); // label sides label("$1$", (A+B)/2, S); label("$1$", (B+C)/2, E); label("$1$", (C+A)/2, W); label("$3$", (A+A_prime)/2, E); label("$3$", (B+B_prime)/2, N); label("$3$", (C+C_prime)/2, W); [/asy]

## Solution 1 (Uses Trig)
Note that by symmetry, $\triangle A'B'C'$ is also equilateral. Therefore, we only need to find one of the sides of $A'B'C'$ to determine the area ratio. WLOG, let $AB = BC = CA = 1$ . Therefore, $BB' = 3$ and $BC' = 4$ . Also, $\angle B'BC' = 120^{\circ}$ , so by the Law of Cosines, $B'C' = \sqrt{4^2 + 3^2 - 2\cdot(4)(3)\cos(120^\circ)} = \sqrt{16+9 - 24(-1/2)} = \sqrt{37}$ . Therefore, the answer is $(\sqrt{37})^2 : 1^2 = \boxed{\textbf{(E) } 37:1}$
~Edited by Shreyansh
$\angle B'AC'$ is not equal to $120^{\circ}$ but $\angle B'BC' = 120^{\circ}$

## Solution 2 (Most straightforward)
As mentioned in the first solution, $\triangle A'B'C'$ is equilateral. Without loss of generality, let $AB=2$ . Let $D$ be on the line passing through $AB$ such that $A'D$ is perpendicular to $AB$ . Note that $\triangle A'DA$ is a $30-60-90$ with right angle at $D$ . Since $AA'=6$ , $AD=3$ and $A'D=3\sqrt{3}$ . So we know that $DB'=11$ . Note that $\triangle A'DB'$ is a right triangle with right angle at $D$ . So by the Pythagorean theorem, we find $A'B'= \sqrt{(3\sqrt{3})^2 + 11^2} = 2\sqrt{37}.$ Therefore, the answer is $(2\sqrt{37})^2 : 2^2 = \boxed{\textbf{(E) } 37:1}$ .
Minor edits by mrmatthewzhang.

## Solution 3
Let $AB=BC=CA=x$ . We start by noting that we can just write $AB'$ as just $AB+BB'=4AB$ . Similarly $BC'=4BC$ , and $CA'=4CA$ . We can evaluate the area of triangle $ABC$ by simply using Heron's formula, $[ABC]=\sqrt{\frac{3x}{2}\cdot {\Bigg(\frac{3x}{2}-x\Bigg)}^3}=\frac{x^2\sqrt{3}}{4}$ . Next in order to evaluate $A'B'C'$ we need to evaluate the area of the larger triangles $AA'B',BB'C', \text{ and } CC'A'$ . In this solution we shall just compute $1$ of these as the others are trivially equivalent. In order to compute the area of $\Delta{AA'B'}$ we can use the formula $[XYZ]=\frac{1}{2}xy\cdot\sin{z}$ . Since $ABC$ is equilateral and $A$ , $B$ , $B'$ are collinear, we already know $\angle{A'AB'}=180-60=120$ Similarly from above we know $AB'$ and $A'A$ to be $4x$ , and $3x$ respectively. Thus the area of $\Delta{AA'B'}$ is $\frac{1}{2}\cdot 4x\cdot 3x \cdot \sin{120}=3x^2\cdot\sqrt{3}$ . Likewise we can find $BB'C', \text{ and } CC'A'$ to also be $3x^2\cdot\sqrt{3}$ . $[A'B'C']=[AA'B']+[BB'C']+[CC'A']+[ABC]=3\cdot3x^2\cdot\sqrt{3}+\frac{x^2\sqrt{3}}{4}=\sqrt{3}\cdot\Bigg(9x^2+\frac{x^2}{4}\Bigg)$ . Therefore the ratio of $[A'B'C']$ to $[ABC]$ is $\frac{\sqrt{3}\cdot\Bigg(9x^2+\frac{x^2}{4}\Bigg)}{\frac{x^2\sqrt{3}}{4}}=\boxed{\textbf{(E) } 37:1}$

## Solution 4 (Elimination)
Looking at the answer choices, we see that all but ${\textbf{(E)}}$ has a perfect square in the ratio. With some intuition, we can guess that the sidelength of the new triangle formed is not an integer, thus we pick $\boxed{\textbf{(E) } 37:1}$ .
Solution by sp1729

## Solution 5 (Barycentric Coordinates)
We use barycentric coordinates wrt $\triangle ABC$ , to which we can easily obtain that $A'=(4,0,-3)$ , $B'=(-3,4,0)$ , and $C'=(0,-3,4)$ . Now, since the coordinates are homogenized ( $-3+4=1$ ), we can directly apply the area formula to obtain that \[[A'B'C']=[ABC]\cdot\left| \begin{array}{ccc} 4 & 0 & -3 \\ -3 & 4 & 0 \\ 0 & -3 & 4 \end{array} \right| = (64-27)[ABC]=37[ABC],\] so the answer is $\boxed{\textbf{(E) } 37:1}$

## Solution 6 (Area Comparison)
First, comparing bases yields that $[BA'B']=3[AA'B]=9[ABC]\implies [AA'B']=12$ . By congruent triangles, \[[AA'B']=[BB'C']=[CC'A']\implies [A'B'C']=(12+12+12+1)[ABC],\] so $[A'B'C']:[ABC]=\boxed{\textbf{(E) } 37:1}$

## Solution 7 (Quick Proportionality)
Scale down the figure so that the area formulas for the $120^\circ$ and equilateral triangles become proportional with proportionality constant equivalent to the product of the corresponding sides. By the proportionality, it becomes clear that the answer is $3\cdot4\cdot3+1\cdot1=37, \boxed{\text{E}}$ .
~ solution by mathchampion1

## Solution 8 (Sin area formula)
Drawing the diagram, we see that the large triangle, $A'B'C'$ , is composed of three congruent triangles with the triangle $ABC$ at the center. Let each of the sides of triangle $ABC$ be $x$ . Therefore, using the equilateral triangle area formula, the $[ABC] = \frac{x^2\sqrt{3}}{4}$ . We also know now that the sides of the triangles are $3x$ and $3x + x$ , or $4x$ . We also know that since $BB'$ are collinear, as are the others, angle $C'BB'$ is $180 - 60$ , which is $120$ degrees. Because that angle is an included angle, we get the area of all three congruent triangle's are $\frac{12x^2\sin120}{2} \cdot 3$ . Simplifying that yields $\frac{36x^2\sqrt{3}}{4}$ . Adding that to the $[ABC]$ yields $\frac{37x^2\sqrt{3}}{4}$ . From this, we can compare the ratios by canceling everything out except for the $37$ , so the answer is $\boxed{\textbf{(E) }37:1}$
~Solution by EricShi1685

## Solution 9 (Same as Solution 8 but faster)
WLOG, let the side length of the smaller triangle be 1. The area of the big portion (A'B'A) is then $\frac{1}{2}\cdot3\cdot4\cdot\sin\left(120\right)=\frac{1}{2}\cdot3\cdot4\cdot\sin\left(60\right)=\frac{1}{2}\cdot3\cdot4\cdot\frac{\sqrt{3}}{2}=3\sqrt{3}$ . Now simply multiply by three and add $\frac{\sqrt{3}}{4}$ (the area of the small triangle) we get $\frac{37\sqrt{3}}{4}$ and so the ratio is $37:1$ . $\boxed{\textbf{(E) }37:1}$

## Solution 10 (Area Ratios)
Connect $BA', CB',$ and $AC'$ . Let $[\triangle ABC]=k$ . $\frac{[\triangle AC'C]}{[\triangle ABC]}=\frac{CC'}{BC}=3$ . So the area of $\triangle ACC'$ is equal to $3k$ . We can do the same thing for $\triangle AA'C'$ . $\frac{[\triangle A'AC']}{[\triangle ACC']}=\frac{A'A}{AC}=3$ . Thus, the area of $\triangle AA'C'$ is equal to $9k$ . We will now find the area of $\triangle A'B'C'$ in terms of $k$ . $[\triangle A'B'C']=[\triangle ABC]+[\triangle A'CC']+[\triangle B'AA']+[\triangle C'BB']=[\triangle ABC]+3[\triangle A'CC']$ . The area of $\triangle A'CC'$ is equal to the sum of the areas of $\triangle ACC'$ and $\triangle AA'C'$ , which is $12k$ . So the area of $\triangle A'B'C'$ is equal to $37k$ and the area of $\triangle ABC$ is equal to $k$ so the ratio of the area of $\triangle A'B'C'$ to the area of $\triangle ABC$ is equal to $\boxed{\textbf{(E) } 37:1}$ -Heavytoothpaste

## Solution 11 (Quick Guess If You Have No Time)
$(A)$ , $(B)$ , $(C)$ , and $(D)$ are all perfect squares, which makes them seem unlikely, so we can guess that the answer probably is $\boxed{(E)}$ as it is the only one with a side length that is implied to not be an integer.

## Solution 12 (Mass Points and Routh)
This looks like an easy application of Routh's Theorem, except we are only given information about the ratios of the cevians, not the side lengths of $\triangle A'B'C'$ .
Let's figure those out. Extend $A'A$ and $B'B$ to meet $B'C'$ and $A'C'$ at $D$ and $E$ , respectively (Note we only need to look at 2 of 3 cevians to figure everything out). Call the unknown lengths $CD=AE=x$ so our new diagram showing the cevian ratios is as follows.
[asy] size(250); real a = 1; pair A = (0, 0), B = rotate(60)*A + (a, 0), C = rotate(120)*B + (a, 0); pair shiftVector = (8, 0); // define a shift vector to the right // calculate extended points pair A_prime = A + 3*(A - C); pair B_prime = B + 3*(B - A); pair C_prime = C + 3*(C - B); pair D = extension(A, A_prime, B_prime, C_prime); pair EE = extension(B, B_prime, A_prime, C_prime); // draw original triangle and extended triangle draw(A_prime--D); draw(B_prime--EE); draw(A_prime--B_prime--C_prime--cycle); // label points dot("$A$", A, SE); dot("$D$", D, NE); dot("$E$", EE, W); dot("$A'$", A_prime, SW); dot("$B'$", B_prime, NE); dot("$C'$", C_prime, W); // label sides label(scale(0.8)*"$4$", (A+B_prime)/2, S); label(scale(0.8)*"$x+1$", (A+D)/2, E); label(scale(0.8)*"$3$", (A+A_prime)/2, E); label(scale(0.8)*"$x$", (A+EE)/2, S); // draw duplicated triangle and labels shifted to the right draw(shift(shiftVector)*A_prime--shift(shiftVector)*D); draw(shift(shiftVector)*B_prime--shift(shiftVector)*EE); draw(shift(shiftVector)*A_prime--shift(shiftVector)*B_prime--shift(shiftVector)*C_prime--cycle); // label cevian ratios label(scale(0.8)*"$4$", shift(2*shiftVector)*(A+B_prime)/2, S); label(scale(0.8)*"$x+1$", shift(2*shiftVector)*(A+D)/2, E); label(scale(0.8)*"$3$", shift(2*shiftVector)*(A+A_prime)/2, E); label(scale(0.8)*"$x$", shift(2*shiftVector)*(A+EE)/2, S); // mass point labels pair mA = shift(shiftVector)*A + scale(0.5)*SE; label(scale(0.4)*"$x+4$", mA, UnFill); draw(Circle(mA, .4), linewidth(1)); pair mB_prime = shift(shiftVector)*B_prime + scale(0.5)*E; label(scale(0.4)*"$x$", mB_prime, UnFill); draw(Circle(mB_prime, .4), linewidth(1)); pair mE = shift(shiftVector)*EE + scale(0.5)*W; label(scale(0.4)*"$4$", mE, UnFill); draw(Circle(mE, .4), linewidth(1)); pair mA_prime = shift(shiftVector)*A_prime + scale(0.5)*SW; label(scale(0.4)*"$x+1$", mA_prime, UnFill); draw(Circle(mA_prime, .4), linewidth(1)); pair mD = shift(shiftVector)*D + scale(0.5)*NE; label(scale(0.4)*"$3$", mD, UnFill); draw(Circle(mD, .4), linewidth(1)); pair mC_prime = shift(shiftVector)*C_prime + scale(0.5)*NW; label(scale(0.4)*"$3-x$", mC_prime, UnFill); draw(Circle(mC_prime, .4), linewidth(1)); // draw double right arrow between original and duplicated diagram draw((4.5,0)--(5.3,0),EndArrow(5)); [/asy]
with the balanced mass points on the right. Now by the symmetry in the original diagram, $\dfrac{A'E}{EC'}=\dfrac{C'D}{DB'}$ so:
\[\dfrac{3-x}{x+1}=\dfrac{x}{3-x} \implies x=\dfrac{9}{7} \implies \dfrac{A'E}{EC'}=\dfrac{3}{4}\]
Finally we can apply Routh's Theorem:
\[\dfrac{[\triangle ABC]}{[\triangle A'B'C']} = \frac{(x y z-1)^2}{(x y+y+1) (x z+x+1) (y z+z+1)} = \frac{(\frac{37}{64})^2}{(\frac{37}{16})^3} = \frac{1}{37}\]
Hence $[\triangle A'B'C']:[\triangle ABC] = \boxed{\textbf{(E) } 37:1}$
~ proloto

## Solution 13 (Similar Triangles)
First we have to know that the three triangles wrapping around △ABC are congruent. Why? There are many ways to prove this but I'll use SSS: C'B = C'C + CB = 4 = AB' = CA', AND BB' = AA' = CC'= 3, AND A'C' = C'B' = A'B' (△C'A'B' is an equilateral triangle). Therefore, the 3 triangles are congruent (SSS). Their areas are the same. Draw a line (goes on forever in both directions) crossing point C and perpendicular to AB intersecting AB at T. Let's organize the angles: ∠CTB = 90° , ∠C'SC = 90°, ∠TCB = ∠C'CS. △CTB ~ △CSC' (AA). From C', draw a line perpendicular to CT intersecting CT at point S Because CC' = 3, CB = 1 Therefore, the similar ratio of the 2 triangles is 1:3. Set CT as x so CS = 3x. Therefore, ST = SC + CT = 4x Area of △ABC = AB * CT / 2 = 1/2x Area of △C'BB' = BB' * ST / 2 = 6x = Area of △A'AB' = Area of △C'CA' Area of △C'A'B' = Area of △ABC + the 3 wrapping triangles = 1/2x + 18x = 37/2x Therefore, ratio = 37/2x : 1/2x = 37:1
~POISONPOISSON

## Video Solution by OmegaLearn (Law of Cosines)
https://youtu.be/4_x1sgcQCp4?t=5373
~ pi_is_3.14

## Video Solution by OmegaLearn (Meta-Solving Technique)
https://youtu.be/GmUWIXXf_uk?t=710
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .