# 2015 AMC 8 Problem 21

## Problem

In the given figure, hexagon $ABCDEF$ is equiangular, $ABJI$ and $FEHG$ are squares with areas $18$ and $32$ respectively, $\triangle JBK$ is equilateral and $FE=BC$ . What is the area of $\triangle KBC$ ?

[asy] draw((-4,6*sqrt(2))--(4,6*sqrt(2))); draw((-4,-6*sqrt(2))--(4,-6*sqrt(2))); draw((-8,0)--(-4,6*sqrt(2))); draw((-8,0)--(-4,-6*sqrt(2))); draw((4,6*sqrt(2))--(8,0)); draw((8,0)--(4,-6*sqrt(2))); draw((-4,6*sqrt(2))--(4,6*sqrt(2))--(4,8+6*sqrt(2))--(-4,8+6*sqrt(2))--cycle); draw((-8,0)--(-4,-6*sqrt(2))--(-4-6*sqrt(2),-4-6*sqrt(2))--(-8-6*sqrt(2),-4)--cycle); label("$I$",(-4,8+6*sqrt(2)),dir(100)); label("$J$",(4,8+6*sqrt(2)),dir(80)); label("$A$",(-4,6*sqrt(2)),dir(280)); label("$B$",(4,6*sqrt(2)),dir(250)); label("$C$",(8,0),W); label("$D$",(4,-6*sqrt(2)),NW); label("$E$",(-4,-6*sqrt(2)),NE); label("$F$",(-8,0),E); draw((4,8+6*sqrt(2))--(4,6*sqrt(2))--(4+4*sqrt(3),4+6*sqrt(2))--cycle); label("$K$",(4+4*sqrt(3),4+6*sqrt(2)),E); draw((4+4*sqrt(3),4+6*sqrt(2))--(8,0),dashed); label("$H$",(-4-6*sqrt(2),-4-6*sqrt(2)),S); label("$G$",(-8-6*sqrt(2),-4),W); label("$32$",(-10,-8),N); label("$18$",(0,6*sqrt(2)+2),N); [/asy]

$\textbf{(A) }6\sqrt{2}\quad\textbf{(B) }9\quad\textbf{(C) }12\quad\textbf{(D) }9\sqrt{2}\quad\textbf{(E) }32$ .

## Solution 1
Clearly, since $\overline{FE}$ is a side of a square with area $32$ , $\overline{FE} = \sqrt{32} = 4 \sqrt{2}$ . Now, since $\overline{FE} = \overline{BC}$ , we have $\overline{BC} = 4 \sqrt{2}$ .
We know that $\overline{JB}$ is a side of a square with area $18$ , so $\overline{JB} = \sqrt{18} = 3 \sqrt{2}$ . Since $\Delta JBK$ is equilateral, $\overline{BK} = \overline{JB} = 3 \sqrt{2}$ .
Lastly, $\Delta KBC$ is a right triangle. We see that $\angle JBA + \angle ABC + \angle CBK + \angle KBJ = 360^{\circ} \rightarrow 90^{\circ} + 120^{\circ} + \angle CBK + 60^{\circ} = 360^{\circ} \rightarrow \angle CBK = 90^{\circ}$ , so $\Delta KBC$ is a right triangle with legs $3 \sqrt{2}$ and $4 \sqrt{2}$ . Now, its area is $\dfrac{3 \sqrt{2} \cdot 4 \sqrt{2}}{2} = \dfrac{24}{2} = \boxed{\textbf{(C)}~12}$ .

## Solution 2
Since $\overline{FE} = \sqrt{32}$ , and $\overline{FE} = \overline{BC}$ , $\overline{BC} = 4\sqrt{2}$ . Meanwhile, $\overline{JB} = 3\sqrt{2}$ , and since $\triangle JBK$ is equilateral, $\overline{BK} = 3\sqrt{2}$ . If $ABCDEF$ is equiangular, $\angle ABC = \frac{180 \cdot (n-2)}{n} = 120^{\circ}$ , where $n$ is the number of sides of the shape. Adding all the angles around $B$ gives $270^{\circ}$ , so $\angle KBC = 360 - 90 = 270^{\circ}$ . Because $\triangle KBC$ is right, the area of $\triangle KBC = \frac{4\sqrt{2} \cdot 3\sqrt{2}} {2} = 12$ . Therefore, the answer is $\boxed{\textbf{(C)}~12}$ . ~strongstephen
Note: Another more complicated way to find out if angle KBC is right, is that we can extend line AB to a point L on triangle KBC. Now, since we know that angle IJB is right, and we know that line IJ now acts as a transversal to lines IJ and AL. That means angle IJB(90 degrees) must be equal to angle JBL by the alternate-exterior angle rule. Since we know that triangle JKB is equilateral, angle JBK will be 60 degrees, hence angle KBL will be 90 - 60 = 30 degrees. Now, we move on to figure ABCDEF. Through the solution above, we know that angle ABC is 120 degrees, so we can use the same line AL which will result in the formation of a linear pair of angles: angles ABC and CBL. Since the angles in a linear pair always add up to 180, and angle ABC is 120, angle CBL = 180 - 120 = 60 degrees. Notice that angle CBL and angle KBL together make up angle KBC. Hence, by the value of 30 degrees derived for angle KBL, angle KBC = angle KBL + angle CBL = 30 degrees + 60 degrees = 90 degrees.

## Video Solution
https://youtu.be/mUBhWTlvuLQ
~savannahsolver
### See Also