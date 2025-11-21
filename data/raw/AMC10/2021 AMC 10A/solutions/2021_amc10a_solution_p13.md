# 2021 AMC 10A Problem 13

## Problem

What is the volume of tetrahedron $ABCD$ with edge lengths $AB = 2$ , $AC = 3$ , $AD = 4$ , $BC = \sqrt{13}$ , $BD = 2\sqrt{5}$ , and $CD = 5$ ?

$\textbf{(A)} ~3 \qquad\textbf{(B)} ~2\sqrt{3} \qquad\textbf{(C)} ~4\qquad\textbf{(D)} ~3\sqrt{3}\qquad\textbf{(E)} ~6$

## Solution 1 (Three Right Triangles)
Drawing the tetrahedron out and testing side lengths, we realize that the $\triangle ACD, \triangle ABC,$ and $\triangle ABD$ are right triangles by the Converse of the Pythagorean Theorem. It is now easy to calculate the volume of the tetrahedron using the formula for the volume of a pyramid. If we take $\triangle ADC$ as the base, then $\overline{AB}$ must be the altitude. The volume of tetrahedron $ABCD$ is $\dfrac{1}{3} \cdot \dfrac{3 \cdot 4}{2} \cdot 2=\boxed{\textbf{(C)} ~4}.$
~Icewolf10 ~Bakedpotato66 ~MRENTHUSIASM

## Solution 2 (One Right Triangle)
We will place tetrahedron $ABCD$ in the $xyz$ -plane. By the Converse of the Pythagorean Theorem, we know that $\triangle ACD$ is a right triangle. Without the loss of generality, let $A=(0,0,0), C=(3,0,0), D=(0,4,0),$ and $B=(x,y,z).$
We apply the Distance Formula to $\overline{BA},\overline{BC},$ and $\overline{BD},$ respectively: \begin{align*} x^2+y^2+z^2&=2^2, &(1) \\ (x-3)^2+y^2+z^2&=\sqrt{13}^2, &(2) \\ x^2+(y-4)^2+z^2&=\left(2\sqrt5\right)^2. &\hspace{1mm} (3) \end{align*} Subtracting $(1)$ from $(2)$ gives $-6x+9=9,$ from which $x=0.$
Subtracting $(1)$ from $(3)$ gives $-8y+16=16,$ from which $y=0.$
Substituting $(x,y)=(0,0)$ into $(1)$ produces $z^2=4,$ or $|z|=2.$
Let the brackets denote areas. Finally, we find the volume of tetrahedron $ABCD$ using $\triangle ACD$ as the base: \begin{align*} V_{ABCD}&=\frac13\cdot[ACD]\cdot h_B \\ &=\frac13\cdot\left(\frac12\cdot AC \cdot AD\right)\cdot |z| \\ &=\boxed{\textbf{(C)} ~4}. \end{align*} ~MRENTHUSIASM

## Solution 3 (Trirectangular Tetrahedron)
https://mathworld.wolfram.com/TrirectangularTetrahedron.html
Given the observations from Solution 1, where $\triangle ACD, \triangle ABC,$ and $\triangle ABD$ are right triangles, the base is $\triangle ABD.$ We can apply the information about a trirectangular tetrahedron (all of the face angles are right angles), which states that the volume is \begin{align*} V&=\frac16\cdot AB\cdot AC\cdot BD \\ &=\frac16\cdot2\cdot4\cdot3 \\ &=\boxed{\textbf{(C)} ~4}. \end{align*} ~AMC60 (Solution)
~MRENTHUSIASM (Revision)
### Remark
Here is a similar problem from another AMC test: 2015 AMC 10A Problem 21 .

## Video Solution (Simple & Quick)
https://youtu.be/bRrchiDCrKE
~ Education, the Study of Everything

## Video Solution by Omega Learn (Using Pythagorean Theorem, 3D Geometry: Tetrahedron)
https://youtu.be/i4yUaXVUWKE
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/t-EEP2V4nAE?t=813
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .