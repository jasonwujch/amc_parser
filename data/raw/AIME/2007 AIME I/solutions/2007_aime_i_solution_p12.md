# 2007 AIME I Problem 12

## Problem

In isosceles triangle $\triangle ABC$ , $A$ is located at the origin and $B$ is located at $(20,0)$ . Point $C$ is in the first quadrant with $AC = BC$ and angle $BAC = 75^{\circ}$ . If triangle $ABC$ is rotated counterclockwise about point $A$ until the image of $C$ lies on the positive $y$ -axis, the area of the region common to the original and the rotated triangle is in the form $p\sqrt{2} + q\sqrt{3} + r\sqrt{6} + s$ , where $p,q,r,s$ are integers. Find $\frac{p-q+r-s}2$ .

## Solution
[asy] defaultpen(fontsize(12)+0.6); size(300); var theta=15; pair A=origin, B=(20,0), C=extension(A,dir(75),B/2,bisectorpoint(A,B)), Cp=rotate(theta,A)*C, Bp=rotate(theta,A)*B, X=extension(A,Bp,B,C), Y=extension(B,C,Bp,Cp); draw(A--B--C--A); draw(A--Bp--Cp--A, royalblue); markscalefactor=0.1; draw(rightanglemark(Y,X,A)); dot("$A$",A,dir(210)); dot("$B$",B,dir(-20)); dot("$C$",C,up); dot("$B'$",Bp,dir(-10)); dot("$C'$",Cp,dir(100)); MA("60^\circ",Bp,A,C,2); MA("15^\circ",B,A,Bp,5); MA("75^\circ",C,B,A,2); MA("30^\circ",A,C,B,4); MA("30^\circ",A,Cp,Bp,4); MA("45^\circ",A,extension(A,C,Bp,Cp),Bp,3); MA("15^\circ",C,Y,Cp,8); MA("15^\circ",C,A,Cp,9); [/asy]

## Solution 1
Let the new triangle be $\triangle AB'C'$ ( $A$ , the origin, is a vertex of both triangles). Let $\overline{B'C'}$ intersect with $\overline{AC}$ at point $D$ , $\overline{BC}$ intersect with $\overline{B'C'}$ at $E$ , and $\overline{BC}$ intersect with $\overline{AB'}$ at $F$ . The region common to both triangles is the quadrilateral $ADEF$ . Notice that $[ADEF] = [\triangle ADB'] - [\triangle EFB']$ , where we let $[\ldots]$ denote area.
Since $\angle B'AC'$ and $\angle BAC$ both have measures $75^{\circ}$ , both of their complements are $15^{\circ}$ , and $\angle DAB' = 90 - 2(15) = 60^{\circ}$ . We know that $\angle DB'A = 75^{\circ}$ , so $\angle ADB' = 180 - 60 - 75 = 45^{\circ}$ .
Thus $\triangle ADB'$ is a $45 - 60 - 75 \triangle$ . It can be solved by drawing an altitude splitting the $75^{\circ}$ angle into $30^{\circ}$ and $45^{\circ}$ angles, forming a $30-60-90$ right triangle and a $45-45-90$ isosceles right triangle. Since we know that $AB' = 20$ , the base of the $30-60-90$ triangle is $10$ , the base of the $45-45-90$ is $10\sqrt{3}$ , and their common height is $10\sqrt{3}$ . Thus, the total area of $[\triangle ADB'] = \frac{1}{2}(10\sqrt{3})(10\sqrt{3} + 10) = \boxed{150 + 50\sqrt{3}}$ .
Since $\triangle AFB$ is also a $15-75-90$ triangle,
and
Since $[\triangle EFB'] = \frac{1}{2} (FB' \cdot EF) = \frac{1}{2} (FB') (FB' \tan 75^{\circ})$ . With some horrendous algebra , we can calculate \begin{align*} [\triangle EFB'] &= \frac{1}{2}\tan (30 + 45) \cdot (20 - 5\sqrt{2} - 5\sqrt{6})^2 \\ &= 25 \left(\frac{\frac{1}{\sqrt{3}} + 1}{1 - \frac{1}{\sqrt{3}}}\right) \left(8 - 2\sqrt{2} - 2\sqrt{6} - 2\sqrt{2} + 1 + \sqrt{3} - 2\sqrt{6} + \sqrt{3} + 3\right) \\ &= 25(2 + \sqrt{3})(12 - 4\sqrt{2} - 4\sqrt{6} + 2\sqrt{3}) \\ [\triangle EFB'] &= \boxed{- 500\sqrt{2} + 400\sqrt{3} - 300\sqrt{6} +750}. \end{align*}
To finish, \begin{align*} [ADEF] &= [\triangle ADB'] - [\triangle EFB']\\ &= \left(150 + 50\sqrt{3}\right) - \left(-500\sqrt{2} + 400\sqrt{3} - 300\sqrt{6} + 750\right)\\ &=500\sqrt{2} - 350\sqrt{3} + 300\sqrt{6} - 600\\ \end{align*} Hence, $\frac{p-q+r-s}{2} = \frac{500 + 350 + 300 + 600}2 = \frac{1750}2 = \boxed{\boxed{875}}$ .

## Solution 2
Redefine the points in the same manner as the last time ( $\triangle AB'C'$ , intersect at $D$ , $E$ , and $F$ ). This time, notice that $[ADEF] = [\triangle AB'C'] - ([\triangle ADC'] + [\triangle EFB'])$ .
The area of $[\triangle AB'C'] = [\triangle ABC]$ . The altitude of $\triangle ABC$ is clearly $10 \tan 75 = 10 \tan (30 + 45)$ . The tangent addition rule yields $10(2 + \sqrt{3})$ (see above). Thus, $[\triangle ABC] = \frac{1}{2} 20 \cdot (20 + 10\sqrt{3}) = 200 + 100\sqrt{3}$ .
The area of $[\triangle ADC']$ (with a side on the y-axis) can be found by splitting it into two triangles, $30-60-90$ and $15-75-90$ right triangles . $AC' = AC = \frac{10}{\sin 15}$ . The sine subtraction rule shows that $\frac{10}{\sin 15} = \frac{10}{\frac{\sqrt{6} - \sqrt{2}}4} = \frac{40}{\sqrt{6} - \sqrt{2}} = 10(\sqrt{6} + \sqrt{2})$ . $AC'$ , in terms of the height of $\triangle ADC'$ , is equal to $h(\sqrt{3} + \tan 75) = h(\sqrt{3} + 2 + \sqrt{3})$ . \begin{align*} [ADC'] &= \frac 12 AC' \cdot h \\ &= \frac 12 (10\sqrt{6} + 10\sqrt{2})\left(\frac{10\sqrt{6} + 10\sqrt{2}}{2\sqrt{3} + 2}\right) \\ &= \frac{(800 + 400\sqrt{3})}{(2 + \sqrt{3})}\cdot\frac{2 - \sqrt{3}}{2-\sqrt{3}} \\ &= \frac{400\sqrt{3} + 400}8 = 50\sqrt{3} + 50 \end{align*}
The area of $[\triangle EFB']$ was found in the previous solution to be $- 500\sqrt{2} + 400\sqrt{3} - 300\sqrt{6} +750$ .
Therefore, $[ADEF]$ $= (200 + 100\sqrt{3}) - \left((50 + 50\sqrt{3}) + (-500\sqrt{2} + 400\sqrt{3} - 300\sqrt{6} +750)\right)$ $= 500\sqrt{2} - 350\sqrt{3} + 300\sqrt{6} - 600$ , and our answer is $\boxed{875}$ .

## Solution 3
Call the points of the intersections of the triangles $D$ , $E$ , and $F$ as noted in the diagram (the points are different from those in the diagram for solution 1). $\overline{AD}$ bisects $\angle EDE'$ .
Through HL congruency, we can find that $\triangle AED$ is congruent to $\triangle AE'D$ . This divides the region $AEDF$ (which we are trying to solve for) into two congruent triangles and an isosceles right triangle .
Since $FE' = AE' = AE$ , we find that $[AE'F] = \frac 12 (5\sqrt{6} + 5\sqrt{2})^2 = 100 + 50\sqrt{3}$ .
Now, we need to find $[AED] = [AE'D]$ . The acute angles of the triangles are $\frac{15}{2}$ and $90 - \frac{15}{2}$ . By repeated application of the half-angle formula , we can find that $\tan \frac{15}{2} = \sqrt{2} - \sqrt{3} + \sqrt{6} - 2$ .
The area of $[AED] = \frac 12 \left(20 \cos 15\right)^2 \left(\tan \frac{15}{2}\right)$ . Thus, $[AED] + [AE'D] = 2\left(\frac 12((5\sqrt{6} + 5\sqrt{2})^2 \cdot (\sqrt{2} - \sqrt{3} + \sqrt{6} - 2))\right)$ , which eventually simplifies to $500\sqrt{2} - 350\sqrt{3} + 300\sqrt{6} - 600$ .
Adding them together, we find that the solution is $[AEDF] = [AE'F] + [AED] + [AE'D]$ $= 100 + 50\sqrt{3} + 500\sqrt{2} - 350\sqrt{3} + 300\sqrt{6} - 600=$ $= 500\sqrt{2} - 350\sqrt{3} + 300\sqrt{6} - 600$ , and the answer is $\boxed{875}$ .

## Solution 4
From the given information, calculate the coordinates of all the points (by finding the equations of the lines, equating). Then, use the shoelace method to calculate the area of the intersection.
- $\overline{AC}$ : $y = (\tan 75) x = (2 + \sqrt{3})x$
- $\overline{AB'}$ : $y = (\tan 15) x = (2 - \sqrt{3})x$
- $\overline{BC}$ : It passes thru $(20,0)$ , and has a slope of $-\tan75 = -(2 + \sqrt{3})$ . The equation of its line is $y = (2+\sqrt{3})(20 - x)$ .
- $\overline{B'C'}$ : $AC' = AC = \frac{10}{\cos 75} = 10\sqrt{6} + 10\sqrt{2}$ , so it passes thru point $(0, 10\sqrt{6} + 10\sqrt{2})$ . It has a slope of $-\tan 60 = -\sqrt{3}$ . So the equation of its line is $y = -\sqrt{3}x + 10(\sqrt{6} + \sqrt{2})$ .
Now, we can equate the equations to find the intersections of all the points.
- $A (0,0)$
- $D$ is the intersection of $\overline{BC},\ \overline{B'C'}$ . $(2+\sqrt{3})(20-x) = -\sqrt{3}x + 10(\sqrt{6} + \sqrt{2})$ . Therefore, $x = 5(4 + 2\sqrt{3}-\sqrt{6}-\sqrt{2})$ , $y = 5(3\sqrt{6} + 5\sqrt{2}-4\sqrt{3}-6)$ .
- $E$ is the intersection of $\overline{AB'},\ \overline{BC}$ . $(2 - \sqrt{3})x =(2+\sqrt{3})(20-x)$ . Therefore, $x = 5(2+\sqrt{3})$ , $y = 5$ .
- $F$ is the intersection of $\overline{AC},\ \overline{B'C'}$ . $(2+\sqrt{3})x = -\sqrt{3}x + 10(\sqrt{6} + \sqrt{2})$ . Therefore, $x = 5\sqrt{2}$ , $y = 10\sqrt{2}+ 5\sqrt{6}$ .
We take these points and tie them together by shoelace, and the answer should come out to be $\boxed{875}$ .

## Video Solution
2007 AIME I #12
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.