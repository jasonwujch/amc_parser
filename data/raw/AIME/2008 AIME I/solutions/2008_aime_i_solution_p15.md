# 2008 AIME I Problem 15

## Problem

A square piece of paper has sides of length $100$ . From each corner a wedge is cut in the following manner: at each corner, the two cuts for the wedge each start at a distance $\sqrt{17}$ from the corner, and they meet on the diagonal at an angle of $60^{\circ}$ (see the figure below). The paper is then folded up along the lines joining the vertices of adjacent cuts. When the two edges of a cut meet, they are taped together. The result is a paper tray whose sides are not at right angles to the base. The height of the tray, that is, the perpendicular distance between the plane of the base and the plane formed by the upper edges, can be written in the form $\sqrt[n]{m}$ , where $m$ and $n$ are positive integers, $m<1000$ , and $m$ is not divisible by the $n$ th power of any prime. Find $m+n$ .

## Picture for Solutions
(Used for the following solutions)

## Solution 1
In the original picture, let $P$ be the corner, and $M$ and $N$ be the two points whose distance is $\sqrt{17}$ from $P$ . Also, let $R$ be the point where the two cuts intersect.
Using $\triangle{MNP}$ (a 45-45-90 triangle), $MN=MP\sqrt{2}\quad\Longrightarrow\quad MN=\sqrt{34}$ . $\triangle{MNR}$ is equilateral , so $MR = NR = \sqrt{34}$ . (Alternatively, we could find this by the Law of Sines .)
The length of the perpendicular from $P$ to $MN$ in $\triangle{MNP}$ is $\frac{\sqrt{17}}{\sqrt{2}}$ , and the length of the perpendicular from $R$ to $MN$ in $\triangle{MNR}$ is $\frac{\sqrt{51}}{\sqrt{2}}$ . Adding those two lengths, $PR=\frac{\sqrt{17}+\sqrt{51}}{\sqrt{2}}$ . (Alternatively, we could have used that $\sin 75^{\circ} = \sin (30+45) = \frac{\sqrt{6}+\sqrt{2}}{4}$ .)
Drop a perpendicular from $R$ to the side of the square containing $M$ and let the intersection be $G$ .
\begin{align*}PG&=\frac{PR}{\sqrt{2}}=\frac{\sqrt{17}+\sqrt{51}}{2}\\ MG=PG-PM&=\frac{\sqrt{17}+\sqrt{51}}{2}-\sqrt{17}=\frac{\sqrt{51}-\sqrt{17}}{2}\end{align*}
Let $A'B'C'D'$ be the smaller square base of the tray and let $ABCD$ be the larger square, such that $AA'$ , etc, are edges. Let $F$ be the foot of the perpendicular from $A$ to plane $A'B'C'D'$ .
We know $AA'=MR=\sqrt{34}$ and $A'F=MG\sqrt{2}=\frac{\sqrt{51}-\sqrt{17}}{\sqrt{2}}$ . Now, use the Pythagorean Theorem on triangle $AFA'$ to find $AF$ :
\begin{align*}\left(\frac{\sqrt{51}-\sqrt{17}}{\sqrt{2}}\right)^2+AF^2&=\left(\sqrt{34}\right)^2\\ \frac{51-34\sqrt{3}+17}{2}+AF^2&=34\\AF&=\sqrt{34-\frac{68-34\sqrt{3}}{2}}\\AF&=\sqrt{\frac{34\sqrt{3}}{2}}\\AF&=\sqrt[4]{867}\end{align*}
The answer is $867 + 4 = \boxed{871}$ .

## Solution 2
In the final pyramid, let $ABCD$ be the smaller square and let $A'B'C'D'$ be the larger square such that $AA'$ , etc. are edges.
It is obvious from the diagram that $\angle A'AB = \angle A'AD = 105^\circ$ .
Let $AB$ and $AD$ be the positive $x$ and $y$ axes in a 3-d coordinate system such that $A'$ has a positive $z$ coordinate. Let $\alpha$ be the angle made with the positive $x$ axis . Define $\beta$ and $\gamma$ analogously.
It is easy to see that if $P: = (x,y,z)$ , then $x = AA'\cdot \cos\alpha$ . Furthermore, this means that $\frac {x^2}{AA'^2} + \frac {y^2}{AA'^2} + \frac {z^2}{AA'^2} = \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$ .
We have that $\alpha = \beta = 105^\circ$ , so $\cos^2 105^\circ + \cos^2105^\circ + \cos^2\gamma = 1\implies \cos\gamma = \sqrt [4]{\frac {3}{4}}$ .
It is easy to see from the Law of Sines that $\frac {AA'}{\sin 45^\circ} = \frac {\sqrt {17}}{\sin 30^\circ}\implies AA' = \sqrt {34}$ .
Now, $z = AA'\cdot \cos\gamma = \sqrt [4]{34^2\cdot \frac {3}{4}} = \sqrt [4]{867}$ .
It follows that the answer is $867 + 4 = \boxed{871}$ .~Shen Kislay Kai
These problems are copyrighted © by the Mathematical Association of America.