# 2009 AIME II Problem 3

## Problem

In rectangle $ABCD$ , $AB=100$ . Let $E$ be the midpoint of $\overline{AD}$ . Given that line $AC$ and line $BE$ are perpendicular, find the greatest integer less than $AD$ .

## Solution

## Solution 1
From the problem, $AB=100$ and triangle $FBA$ is a right triangle. As $ABCD$ is a rectangle, triangles $BCA$ , and $ABE$ are also right triangles. By $AA$ , $\triangle FBA \sim \triangle BCA$ , and $\triangle FBA \sim \triangle ABE$ , so $\triangle ABE \sim \triangle BCA$ . This gives $\frac {AE}{AB}= \frac {AB}{BC}$ . $AE=\frac{AD}{2}$ and $BC=AD$ , so $\frac {AD}{2AB}= \frac {AB}{AD}$ , or $(AD)^2=2(AB)^2$ , so $AD=AB \sqrt{2}$ , or $100 \sqrt{2}$ , so the answer is $\boxed{141}$ .

## Solution 2
Let $x$ be the ratio of $BC$ to $AB$ . On the coordinate plane, plot $A=(0,0)$ , $B=(100,0)$ , $C=(100,100x)$ , and $D=(0,100x)$ . Then $E=(0,50x)$ . Furthermore, the slope of $\overline{AC}$ is $x$ and the slope of $\overline{BE}$ is $-x/2$ . They are perpendicular, so they multiply to $-1$ , that is, \[x\cdot-\frac{x}{2}=-1,\] which implies that $-x^2=-2$ or $x=\sqrt 2$ . Therefore $AD=100\sqrt 2\approx 141.42$ so $\lfloor AD\rfloor=\boxed{141}$ .

## Solution 3
Similarly to Solution 2, let the positive x-axis be in the direction of ray $BC$ and let the positive y-axis be in the direction of ray $BA$ . Thus, the vector $BE=(x,100)$ and the vector $AC=(2x,-100)$ are perpendicular and thus have a dot product of 0. Thus, calculating the dot product:
\[x\cdot2x+(100)\cdot(-100)=2x^2-10000=0\] \[2x^2-10000=0\rightarrow x^2=5000\]
Substituting AD/2 for x: \[(AD/2)^2=5000\rightarrow AD^2=20000\] \[AD=100\sqrt2\]

## Solution 4
Draw $CX$ and $EX$ to form a parallelogram $AEXC$ . Since $EX \parallel AC$ , $\angle BEX=90^\circ$ by the problem statement, so $\triangle BEX$ is right. Letting $AE=y$ , we have $BE=\sqrt{100^2+y^2}$ and $AC=EX=\sqrt{100^2+(2y)^2}$ . Since $CX=EA$ , $\sqrt{100^2+y^2}^2+\sqrt{100^2+(2y)^2}=(3y)^2$ . Solving this, we have \[100^2+ 100^2 + y^2 + 4y^2 = 9y^2\] \[2\cdot 100^2 = 4y^2\] \[\frac{100^2}{2}=y^2\] \[\frac{100}{\sqrt{2}}=y\] \[\frac{100\sqrt{2}}{2}=y\] \[100\sqrt{2}=2y=AD\] , so the answer is $\boxed{141}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.