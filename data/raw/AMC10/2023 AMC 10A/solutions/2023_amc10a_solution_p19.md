# 2023 AMC 10A Problem 19

## Problem

The line segment formed by $A(1, 2)$ and $B(3, 3)$ is rotated to the line segment formed by $A'(3, 1)$ and $B'(4, 3)$ about the point $P(r, s)$ . What is $|r-s|$ ?

$\textbf{(A) } \frac{1}{4} \qquad \textbf{(B) } \frac{1}{2} \qquad \textbf{(C) } \frac{3}{4} \qquad \textbf{(D) } \frac{2}{3} \qquad \textbf{(E) } 1$

## Solution 1
Due to rotations preserving an equal distance, we can bash the answer with the distance formula. $D(A, P) = D(A', P)$ , and $D(B, P) = D(B',P)$ . Thus we will square our equations to yield: $(1-r)^2+(2-s)^2=(3-r)^2+(1-s)^2$ , and $(3-r)^2+(3-s)^2=(4-r)^2+(3-s)^2$ . Canceling $(3-s)^2$ from the second equation makes it clear that $r$ equals $3.5$ .
Substituting will yield
\begin{align*}(2.5)^2+(2-s)^2 &= (-0.5)^2+(1-s)^2 \\ 6.25+4-4s+s^2 &= 0.25+1-2s+s^2 \\ 2s &= 9 \\ s &=4.5 \\ \end{align*} .
Now $|r-s| = |3.5-4.5| = \boxed{\textbf{(E) } 1}$ .
-Antifreeze5420

## Solution 2
Due to rotations preserving distance, we have that $BP = B^\prime P$ , as well as $AP = A^\prime P$ . From here, we can see that P must be on the perpendicular bisector of $\overline{BB^\prime}$ due to the property of perpendicular bisectors keeping the distance to two points constant.
From here, we proceed to find the perpendicular bisector of $\overline{BB^\prime}$ . We can see that this is just a horizontal line segment with midpoint at $(3.5, 3)$ . This means that the equation of the perpendicular bisector is $x = 3.5$ .
Similarly, we find the perpendicular bisector of $\overline{AA^\prime}$ . We find the slope to be $\frac{1-2}{3-1} = -\frac12$ , so our new slope will be $2$ . The midpoint of $A$ and $A^\prime$ is $(2, \frac32)$ , which we can use with our slope to get another equation of $y = 2x - \frac52$ .
Now, point P has to lie on both of these perpendicular bisectors, meaning that it has to satisfy both equations. Plugging in the value of $x$ we found earlier, we find that $y=4.5$ . This means that $|r - s| = |3.5 - 4.5| = \boxed{\textbf{(E) } 1}$ .
-DEVSAXENA

## Solution 3 (Coordinate Geometry)
To find the center of rotation, we find the intersection point of the perpendicular bisectors of $\overline{AA^\prime}$ and $\overline{BB^\prime}$ . (this is because $\overline{PA}$ is equal to $\overline{PA^\prime}$ and same with $B$ and $B^\prime$
We can find that the equation of the line $\overline{AA^\prime}$ is $y = -\frac{1}{2}x + \frac{5}{2}$ , and that the equation of the line $\overline{BB^\prime}$ is $y = 3$ .
When we solve for the perpendicular bisector of $y = -\frac{1}{2}x + \frac{5}{2}$ , we determine that it has a slope of 2, and it runs through $(2, 1.5)$ . Plugging in $1.5 = 2(2)-n$ , we get than $n = \frac{5}{2}$ . Therefore our perpendicular bisector is $y=2x-\frac{5}{2}$ . Next, we solve for the perpendicular of $y = 3$ . We know that it has an undefined slope, and it runs through $(3.5, 3)$ . We can determine that our second perpendicular bisector is $x = 3.5$ .
Setting the equations equal to each other, we get $y = \frac{9}{2}$ . Therefore, $|r - s| = |3.5 - 4.5| = \boxed{\textbf{(E) } 1}$ .
[asy] pair A=(1,2); pair B=(3,3); pair A1=(3,1); pair B1=(4,3); dot("A",A,NW); dot("B",B,S); dot("A'",A1,S); dot("B'",B1,E); draw(A--A1); draw(B--B1); draw((3.5,0)--(3.5,6),BeginArrow(5),EndArrow(5)); draw((1,-0.5)--(4,5.5),BeginArrow(5),EndArrow(5)); pair P=(3.5,4.5); dot("P",P,NW); [/asy]
~aydenlee & wuwang2002 ~minor explanations by pungent_muskrat

## Solution 4
We use the complex numbers approach to solve this problem. Denote by $\theta$ the angle that $AB$ rotates about $P$ in the counterclockwise direction.
Thus, $A' - P = e^{i \theta} \left( A - P \right)$ and $B' - P = e^{i \theta} \left( B - P \right)$ .
Taking ratio of these two equations, we get \[ \frac{A' - P}{A - P} = \frac{B' - P}{B - P} . \]
By solving this equation, we get $P = \frac{7}{2} + i \frac{9}{2}$ . Therefore, $|s-t| = \left| \frac{7}{2} - \frac{9}{2} \right| = \boxed{\textbf{(E) 1}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 5 (Overkill Trigonometry)
First, we need to find the coordinates of point \( P(r, s) \) such that rotating the line segment from \( A(1,2) \) to \( B(3,3) \) about \( P \) maps it to the line segment from \( A'(3,1) \) to \( B'(4,3) \). After finding \( r \) and \( s \), we will compute \( |r - s| \).
When a point \( (x, y) \) is rotated about another point \( (r, s) \) by an angle \( \theta \), the new coordinates \( (x', y') \) are given by:
\begin{cases} x' = r + (x - r) \cos \theta - (y - s) \sin \theta \\ y' = s + (x - r) \sin \theta + (y - s) \cos \theta \end{cases}
We apply the rotation to points \( A \) and \( B \):
For \( A(1,2) \) mapping to \( A'(3,1) \):
\begin{cases} 3 = r + (1 - r) \cos \theta - (2 - s) \sin \theta \quad \text{(1)} \\ 1 = s + (1 - r) \sin \theta + (2 - s) \cos \theta \quad \text{(2)} \end{cases}
For \( B(3,3) \) mapping to \( B'(4,3) \):
\begin{cases} 4 = r + (3 - r) \cos \theta - (3 - s) \sin \theta \quad \text{(3)} \\ 3 = s + (3 - r) \sin \theta + (3 - s) \cos \theta \quad \text{(4)} \end{cases}
Now, we subtract equations to eliminate variables:
Subtract equation (1) from equation (3):
\[(4 - 3) = [r + (3 - r) \cos \theta - (3 - s) \sin \theta] - [r + (1 - r) \cos \theta - (2 - s) \sin \theta]\]
Simplifying yields:
\[1 = 2 \cos \theta - \sin \theta \quad \text{(A)}\]
Similarly, subtract equation (2) from equation (4):
\[(3 - 1) = [s + (3 - r) \sin \theta + (3 - s) \cos \theta] - [s + (1 - r) \sin \theta + (2 - s) \cos \theta]\]
Simplifying further:
\[2 = 2 \sin \theta + \cos \theta \quad \text{(B)}\]
Now, using equations (A) and (B):
\begin{cases} 2 \cos \theta - \sin \theta = 1 \\ \cos \theta + 2 \sin \theta = 2 \end{cases}
We now express \( \cos \theta \) from the second equation:
\[\cos \theta = 2 - 2 \sin \theta\]
Substituting this into the first equation, we get:
\[2(2 - 2 \sin \theta) - \sin \theta = 1 \\ 4 - 4 \sin \theta - \sin \theta = 1 \\ -5 \sin \theta = -3 \\ \sin \theta = \frac{3}{5}\]
Now, we find $\cos \theta$ as follows:
\[\cos \theta = 2 - 2 \left( \frac{3}{5} \right) = \frac{4}{5}\]
Substituting $\cos \theta$ and $\sin \theta$ back into equations (1) and (2):
Equation (1):
\[3 - r = (1 - r) \left( \frac{4}{5} \right) - (2 - s) \left( \frac{3}{5} \right)\]
Multiply both sides by 5:
\[5(3 - r) = 4(1 - r) - 3(2 - s)\]
Simplify:
\[15 - 5r = 4 - 4r - 6 + 3s \\ 15 - 5r = -2 - 4r + 3s \\ -5r + 4r - 3s = -2 - 15 \\ -r - 3s = -17 \quad \text{(C)}\]
Equation (2):
\[1 - s = (1 - r) \left( \frac{3}{5} \right) + (2 - s) \left( \frac{4}{5} \right)\]
Multiply both sides by 5:
\[5(1 - s) = 3(1 - r) + 4(2 - s)\]
Simplifying more:
\[5 - 5s = 3 - 3r + 8 - 4s \\ 5 - 5s = 11 - 3r - 4s \\ -5s + 4s + 3r = 11 - 5 \\ 3r - s = 6 \quad \text{(D)}\]
From equations (C) and (D):
\[\begin{cases} -r - 3s = -17 \\ 3r - s = 6 \end{cases}\]
We then multiply the first equation by 3:
\[-3r - 9s = -51\]
Add this to the second equation multiplied by 9:
\[27r - 9s = 54\]
Subtract:
\[(27r - 9s) - (-3r - 9s) = 54 - (-51) \\ 30r = 105 \\ r = \frac{105}{30} = \frac{7}{2} = 3.5\]
Now find \( s \):
\[3(3.5) - s = 6 \\ 10.5 - s = 6 \\ s = 4.5\]
Therefore, we have the following:
\[|r - s| = |3.5 - 4.5| = |-1| = \boxed{\textbf{(E) } 1}.\]
~dbnl

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=8YX-h2OqRiF8j2y4&t=4238 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=UCyIECgDXCoSakc0&t=5831
~Math-X

## Video Solution
https://youtu.be/aYHwBpdWkAk

## Video Solution by
https://www.youtube.com/watch?v=fIzCR4x4x-M

## Video Solution 1 by OmegaLearn
https://youtu.be/88F18qth0xI

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=oHMJwiEwOS0

## Video Solution
https://youtu.be/va3ZCFeKfzg
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by TheBeautyofMath
https://youtu.be/Q_4uMxMbQlI
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .