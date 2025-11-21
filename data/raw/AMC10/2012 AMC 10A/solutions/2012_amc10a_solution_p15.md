# 2012 AMC 10A Problem 15

## Problem

Three unit squares and two line segments connecting two pairs of vertices are shown. What is the area of $\triangle ABC$ ?

$\textbf{(A)}\ \frac16 \qquad\textbf{(B)}\ \frac15 \qquad\textbf{(C)}\ \frac29 \qquad\textbf{(D)}\ \frac13 \qquad\textbf{(E)}\ \frac{\sqrt{2}}{4}$

## Solution 1
$AC$ intersects $BC$ at a right angle, (this can be proved by noticing that the slopes of the two lines are negative reciprocals of each other) so $\triangle ABC \sim \triangle BED$ . The hypotenuse of right triangle $BED$ is $\sqrt{1^2+2^2}=\sqrt{5}$ .
\[\frac{AC}{BC}=\frac{BD}{ED} \Rightarrow \frac{AC}{BC} = \frac21 \Rightarrow AC=2BC\]
\[\frac{AC}{AB}=\frac{BD}{BE} \Rightarrow \frac{AC}{1}=\frac{2}{\sqrt{5}} \Rightarrow AC=\frac{2}{\sqrt{5}}\]
Since $AC=2BC$ , $BC=\frac{1}{\sqrt{5}}$ . $\triangle ABC$ is a right triangle so the area is just $\frac12 \cdot AC \cdot BC = \frac12 \cdot \frac{2}{\sqrt{5}} \cdot \frac{1}{\sqrt{5}} = \boxed{\textbf{(B)}\ \frac15}$

## Solution 2 (coordbash)
Let $\text{E}$ be the origin. Then, $\text{D}=(1, 0)$ $\text{A}=(0, 2)$ $\text{B}=(1, 2)$ $\text{F}=(2, 1)$
${EB}$ can be represented by the line $y=2x$ Also, ${AF}$ can be represented by the line $y=-\frac{1}{2}x+2$
Subtracting the second equation from the first gives us $\frac{5}{2}x-2=0$ . Thus, $x=\frac{4}{5}$ . Plugging this into the first equation gives us $y=\frac{8}{5}$ .
Since $\text{C} (0.8, 1.6)$ , $G$ is $(0.8, 2)$ ,
${AB}=1$ and ${CG}=0.4$ .
Thus, $[ABC]=\frac{1}{2} \cdot {AB} \cdot {CG}=\frac{1}{2} \cdot 1 \cdot 0.4=0.2=\frac{1}{5}$ . The answer is $\boxed{\textbf{(B)}\ \frac15}$ .
Note: Once you have determined that $\text{C} (0.8, 1.6)$ , you can use Shoelace Theorem to determine the area of triangle ABC.

## Solution 3
Triangle $EAB$ is similar to triangle $EHI$ ; line $HI = 1/2$
Triangle $ACB$ is similar to triangle $FCI$ and the ratio of line $AB$ to line $IF = 1 : \frac{3}{2} = 2: 3$ .
Based on similarity the length of the height of $GC$ is thus $\frac{2}{5}\cdot1 = \frac{2}{5}$ .
Thus, $[ABC]=\frac{1}{2} \cdot {AB} \cdot {CG}=\frac{1}{2} \cdot 1 \cdot \frac{2}{5}=\frac{1}{5}$ . The answer is $\boxed{\textbf{(B)}\ \frac15}$

## Solution 4
Let $L$ be the point where the diagonal and the end of the unit square meet, on the right side of the diagram. Let $K$ be the top right corner of the top right unit square, where segment $ABL$ is 2 units in length.
Because of the Pythagorean Theorem, since $AC = 2$ and $LK$ = 1, the diagonal of triangle $ALK$ is $\sqrt{5}$ .
Triangle $ALK$ is clearly a similar triangle to triangle $ABC$ . Segment $AB$ is the hypotenuse of triangle $ABC$ . So, we can write down:
\[AK/AB = LK/BC\] , which is equal to: \[\frac{\sqrt{5}}{1} = \frac{1}{BC}\] Solving this equation yields:
\[BC = \frac{1}{\sqrt{5}}\]
By Pythagorean theorem, we can now find segment $AC$ \[(\frac{1}{\sqrt{5}})^2 + AC^2 = 1\] Solving this yields:
\[AC^2 = \frac{4}{5}\] , so $AC = \frac{2}{\sqrt{5}}$
So then we can use \[A = \frac{1}{2} * b * a.\] So \[A = \frac{1}{2} * \frac{1}{\sqrt{5}} * \frac{2}{\sqrt{5}}\]
\[= \boxed{\textbf{(B)}\ \frac15}\]

## Video Solution
https://youtu.be/HVesU8cTjRU
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/4_x1sgcQCp4?t=1717
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .