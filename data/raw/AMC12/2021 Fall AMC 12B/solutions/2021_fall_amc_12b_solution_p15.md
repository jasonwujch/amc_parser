# 2021 Fall AMC 12B Problem 15

## Problem

Three identical square sheets of paper each with side length $6$ are stacked on top of each other. The middle sheet is rotated clockwise $30^\circ$ about its center and the top sheet is rotated clockwise $60^\circ$ about its center, resulting in the $24$ -sided polygon shown in the figure below. The area of this polygon can be expressed in the form $a-b\sqrt{c}$ , where $a$ , $b$ , and $c$ are positive integers, and $c$ is not divisible by the square of any prime. What is $a+b+c$ ?

$(\textbf{A})\: 75\qquad(\textbf{B}) \: 93\qquad(\textbf{C}) \: 96\qquad(\textbf{D}) \: 129\qquad(\textbf{E}) \: 147$

## Solution 1
[asy] defaultpen(fontsize(8)+0.8); size(100); pair A=(0,0); pair B=(1.732,3); pair C=(3,3); pair D=(3,1.732); draw(A--(0,3)--C--(3,0)--A, lightgray+dashed); draw(A--B--C--A); draw(A--D--C, gray); label("$A$",A,W); label("$B$",B,N); label("$C$",C,NE); label("$D$",D,E); label("$E$",(0,3),NW); label("$F$",(3,0),E); [/asy] The $24$ -sided polygon is made out of $24$ shapes like $\triangle ABC$ . Then $\angle BAC=360^\circ/24=15^\circ$ , and $\angle EAC = 45^\circ$ , so $\angle{EAB} = 30^{\circ}$ . Then $EB=AE\tan 30^\circ = \sqrt{3}$ ; therefore $BC=EC-EB=3-\sqrt{3}$ . Thus \[[ABC] = \frac{BC}{EC}\cdot [ACE] = \frac{3-\sqrt{3}}{3}\cdot \frac 92\] and the required area is $24\cdot[ABC] =108-36\sqrt{3}$ . Finally $108+36+3=\boxed{(\textbf{E})\ 147}$ . ~lopkiloinm
Note: Drop an altitude from $A$ to $\overline{BC}$ to construct point $E$ . This creates right triangles. ~erringbubble

## Solution 2
As shown in Image:2021_AMC_12B_(Nov)_Problem_15,_sol.png , all 12 vertices of three squares form a regular dodecagon (12-gon). Denote by $O$ the center of this dodecagon.
Hence, $\angle AOB = \frac{360^\circ}{12} = 30^\circ$ .
Because the length of a side of a square is 6, $AO = 3 \sqrt{2}$ .
Hence, $AB = 2 AO \sin \frac{\angle AOB}{2} = 3 \left( \sqrt{3} - 1 \right)$ .
We notice that $\angle MAB = \angle MBA = 30^\circ$ . Hence, $AM = \frac{AB}{2\cos \angle MAB} = 3 - \sqrt{3}$ .
Therefore, the area of the region that three squares cover is \begin{align*} & {\rm Area} \ ABCDEFGHIJKL - 12 {\rm Area} \ \triangle MAB \\ & = 12 {\rm Area} \ \triangle OAB - 12 {\rm Area} \ \triangle MAB \\ & = 12 \cdot \frac{1}{2} OA \cdot OB \sin \angle AOB - 12 \cdot \frac{1}{2} MA \cdot MB \sin \angle AMB \\ & = 6 OA^2 \sin \angle AOB - 6 MA^2 \sin \angle AMB \\ & = 108 - 36 \sqrt{3} . \end{align*}
Therefore, the answer is $\boxed{\textbf{(E) }147}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 3 (complex number & coordinate geometry)
set A = 3+3i , A' , B' rotate 30 degree from A, B
A'= A $\cdot e^i30^\circ = (3+3i)*(\sqrt{3}/2 + 1/2 i) =( \sqrt{3}/2 - 1/2) + (1/2 + \sqrt{3}/2) i$
line A'B' $\frac{y-(1/2 + \sqrt{3}/2)}{x - ( \sqrt{3}/2 - 1/2)} = Tan(90\circ+30\circ) = -\sqrt{3}$
intersect with line y=3 at point $E_{x} = \sqrt{3}$ , then length $AE = A_{x} - E_{x} = 3- \sqrt{3}$ ,
use shoelace or $\triangle OAE$ = 1/2 * AE * AB/2 = 1/2 * $(3- \sqrt{3})$ * 3
total area = 24 * $\triangle OAE$ = = 108 - 36 $\sqrt{3}$ the answer is $\boxed{\textbf{(E) }147}$ .
~ luckuso

## Video Solution (Just 4 min!)
https://youtu.be/u_8EWGBErs8
~Education, the Study of Everything

## Video Solution by TheBeautyofMath
https://youtu.be/YD9J394zeig
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .