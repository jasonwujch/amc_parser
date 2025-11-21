# 2021 Fall AMC 10A Problem 3

## Problem

What is the maximum number of balls of clay of radius $2$ that can completely fit inside a cube of side length $6$ assuming the balls can be reshaped but not compressed before they are packed in the cube?

$\textbf{(A) }3\qquad\textbf{(B) }4\qquad\textbf{(C) }5\qquad\textbf{(D) }6\qquad\textbf{(E) }7$

## Solution 1 (Inequality)
The volume of the cube is $V_{\text{cube}}=6^3=216,$ and the volume of a clay ball is $V_{\text{ball}}=\frac43\cdot\pi\cdot2^3=\frac{32}{3}\pi.$
Since the balls can be reshaped but not compressed, the maximum number of balls that can completely fit inside a cube is \[\left\lfloor\frac{V_{\text{cube}}}{V_{\text{ball}}}\right\rfloor=\left\lfloor\frac{81}{4\pi}\right\rfloor.\] Approximating with $\pi\approx3.14,$ we have $12<4\pi<13,$ or $\left\lfloor\frac{81}{13}\right\rfloor \leq \left\lfloor\frac{81}{4\pi}\right\rfloor \leq \left\lfloor\frac{81}{12}\right\rfloor.$ We simplify to get \[6 \leq \left\lfloor\frac{81}{4\pi}\right\rfloor \leq 6,\] from which $\left\lfloor\frac{81}{4\pi}\right\rfloor=\boxed{\textbf{(D) }6}.$
~NH14 ~MRENTHUSIASM

## Solution 2 (Inequality)
As shown in Solution 1, we conclude that the maximum number of balls that can completely fit inside a cube is $\left\lfloor\frac{81}{4\pi}\right\rfloor.$
By an underestimation $\pi\approx3,$ we have $4\pi>12,$ or $\frac{81}{4\pi}<6\frac34.$
By an overestimation $\pi\approx\frac{22}{7},$ we have $4\pi<\frac{88}{7},$ or $\frac{81}{4\pi}>6\frac{39}{88}.$
Together, we get \[6 < 6\frac{39}{88} < \frac{81}{4\pi} < 6\frac34 < 7,\] from which $\left\lfloor\frac{81}{4\pi}\right\rfloor=\boxed{\textbf{(D) }6}.$
~MRENTHUSIASM

## Solution 3 (Approximation)
As shown in Solution 1, we conclude that the maximum number of balls that can completely fit inside a cube is $\left\lfloor\frac{81}{4\pi}\right\rfloor.$
Approximating with $\pi\approx3,$ we have $\frac{81}{4\pi}\approx6\frac34.$ Since $\pi$ is about $5\%$ greater than $3,$ it is safe to claim that $\left\lfloor\frac{81}{4\pi}\right\rfloor=\boxed{\textbf{(D) }6}.$
~Arcticturn ~MRENTHUSIASM

## Video Solution
https://youtu.be/0WrcZI_z9IE
~savannahsolver

## Video Solution
https://youtu.be/qOiO45IsE54
~Charles3829

## Video Solution by TheBeautyofMath
https://youtu.be/o98vGHAUYjM?t=158
~IceMatrix

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/VcGR0GVqKBI
~Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .