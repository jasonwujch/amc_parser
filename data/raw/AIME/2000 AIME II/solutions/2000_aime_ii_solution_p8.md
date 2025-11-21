# 2000 AIME II Problem 8

## Problem

In trapezoid $ABCD$ , leg $\overline{BC}$ is perpendicular to bases $\overline{AB}$ and $\overline{CD}$ , and diagonals $\overline{AC}$ and $\overline{BD}$ are perpendicular. Given that $AB=\sqrt{11}$ and $AD=\sqrt{1001}$ , find $BC^2$ .

## Solution

## Solution 1
Let $x = BC$ be the height of the trapezoid, and let $y = CD$ . Since $AC \perp BD$ , it follows that $\triangle BAC \sim \triangle CBD$ , so $\frac{x}{\sqrt{11}} = \frac{y}{x} \Longrightarrow x^2 = y\sqrt{11}$ .
Let $E$ be the foot of the altitude from $A$ to $\overline{CD}$ . Then $AE = x$ , and $ADE$ is a right triangle . By the Pythagorean Theorem ,
\[x^2 + \left(y-\sqrt{11}\right)^2 = 1001 \Longrightarrow x^4 - 11x^2 - 11^2 \cdot 9 \cdot 10 = 0\]
The positive solution to this quadratic equation is $x^2 = \boxed{110}$ .

## Solution 2
Let $BC=x$ . Dropping the altitude from $A$ and using the Pythagorean Theorem tells us that $CD=\sqrt{11}+\sqrt{1001-x^2}$ . Therefore, we know that vector $\vec{BD}=\langle \sqrt{11}+\sqrt{1001-x^2},-x\rangle$ and vector $\vec{AC}=\langle-\sqrt{11},-x\rangle$ . Now we know that these vectors are perpendicular, so their dot product is 0. \[\vec{BD}\cdot \vec{AC}=-11-\sqrt{11(1001-x^2)}+x^2=0\] \[(x^2-11)^2=11(1001-x^2)\] \[x^4-11x^2-11\cdot 990=0.\] As above, we can solve this quadratic to get the positve solution $BC^2=x^2=\boxed{110}$ .

## Solution 3
Let $BC=x$ and $CD=y+\sqrt{11}$ . From Pythagoras with $AD$ , we obtain $x^2+y^2=1001$ . Since $AC$ and $BD$ are perpendicular diagonals of a quadrilateral, then $AB^2+CD^2=BC^2+AD^2$ , so we have \[\left(y+\sqrt{11}\right)^2+11=x^2+1001.\] Substituting $x^2=1001-y^2$ and simplifying yields \[y^2+\sqrt{11}y-990=0,\] and the quadratic formula gives $y=9\sqrt{11}$ . Then from $x^2+y^2=1001$ , we plug in $y$ to find $x^2=\boxed{110}$ .

## Solution 4
Let $E$ be the intersection of the diagonals. Since the diagonals are perpendicular, applying the Pythagorean Theorem multiple times we have \begin{align*} BC^2&=BE^2+CE^2 \\ &=(AB^2-AE^2)+(CD^2-DE^2) \\ &=CD^2+\sqrt{11}^2-(AE^2+DE^2) \\ &=CD^2+11-AD^2 \\ &=CD^2-990 \end{align*} Followed by dropping the perpendicular like in solution 1, we obtain system of equation \[BC^2=CD^2-990\] \[BC^2+CD^2-2\sqrt{11}CD=990\] Rearrange the first equation yields \[CD^2-BC^2=990\] Equating it with the second equation we have \[CD^2-BC^2=BC^2+CD^2-2\sqrt{11}CD\] Which gives $CD=\frac{BC^2}{\sqrt{11}}$ . Substituting into equation 1 obtains the quadratic in terms of $BC^2$ \[(BC^2)^2-11BC^2-11\cdot990=0\] Solving the quadratic to obtain $BC^2=\boxed{110}$ .
~Nafer ~edits by fermat_sLastAMC
These problems are copyrighted © by the Mathematical Association of America.