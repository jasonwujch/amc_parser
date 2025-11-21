# 2014 AMC 10B Problem 15

## Problem

In rectangle $ABCD$ , $DC = 2 \cdot CB$ and points $E$ and $F$ lie on $\overline{AB}$ so that $\overline{ED}$ and $\overline{FD}$ trisect $\angle ADC$ as shown. What is the ratio of the area of $\triangle DEF$ to the area of rectangle $ABCD$ ?

[asy] draw((0, 0)--(0, 1)--(2, 1)--(2, 0)--cycle); draw((0, 0)--(sqrt(3)/3, 1)); draw((0, 0)--(sqrt(3), 1)); label("A", (0, 1), N); label("B", (2, 1), N); label("C", (2, 0), S); label("D", (0, 0), S); label("E", (sqrt(3)/3, 1), N); label("F", (sqrt(3), 1), N); [/asy]

$\textbf{(A)}\ \ \frac{\sqrt{3}}{6}\qquad\textbf{(B)}\ \frac{\sqrt{6}}{8}\qquad\textbf{(C)}\ \frac{3\sqrt{3}}{16}\qquad\textbf{(D)}\ \frac{1}{3}\qquad\textbf{(E)}\ \frac{\sqrt{2}}{4}$

## Solution 1
Let the length of $AD$ be $x$ , so that the length of $AB$ is $2x$ and $\text{[}ABCD\text{]}=2x^2$ .
Because $ABCD$ is a rectangle, $\angle ADC=90^{\circ}$ , and so $\angle ADE=\angle EDF=\angle FDC=30^{\circ}$ . Thus $\triangle DAE$ is a $30-60-90$ right triangle; this implies that $\angle DEF=180^{\circ}-60^{\circ}=120^{\circ}$ , so $\angle EFD=180^{\circ}-(120^{\circ}+30^{\circ})=30^{\circ}$ . Now drop the altitude from $E$ of $\triangle DEF$ , forming two $30-60-90$ triangles.
Because the length of $AD$ is $x$ , from the properties of a $30-60-90$ triangle the length of $AE$ is $\frac{x\sqrt{3}}{3}$ and the length of $DE$ is thus $\frac{2x\sqrt{3}}{3}$ . Thus the altitude of $\triangle DEF$ is $\frac{x\sqrt{3}}{3}$ , and its base is $2x$ , so its area is $\frac{1}{2}(2x)\left(\frac{x\sqrt{3}}{3}\right)=\frac{x^2\sqrt{3}}{3}$ .
To finish, $\frac{\text{[}\triangle DEF\text{]}}{\text{[}ABCD\text{]}}=\frac{\frac{x^2\sqrt{3}}{3}}{2x^2}=\boxed{\textbf{(A) }\frac{\sqrt{3}}{6}}$ .

## Solution 2
WLOG, let $AD = 1$ and $DC = 2$ . Furthermore, drop an an altitude from $F$ to $CD$ , which meets $CD$ at $X$ . Since $\angle ADC$ is right and has been trisected, it follows that $\triangle ADE$ and $\triangle DXF$ are both $30-60-90$ triangles. Therefore, $AE = \frac{\sqrt{3}}{3}$ , and $DX = AF = \sqrt{3}$ . Hence, it follows that $EF = \sqrt{3} - \frac{\sqrt{3}}{3}= \frac{2\sqrt{3}}{3}$ . Since $\angle ADE$ is right, the height and base of $\triangle DEF$ are $1$ and $\frac{2\sqrt{3}}{3}$ , respectively. Thus, the area of $\triangle DEF$ is $\frac{\sqrt{3}}{3}$ , and the area of rectengle $ABCD$ is $2$ , so the ratio beween the area of $\triangle DEF$ and $ABCD$ is $\boxed{\textbf{(A) }\frac{\sqrt{3}}{6}}$ . Note that we are able to assume that $AD=1$ and $DC = 2$ because we were asked to find the ratio between two areas.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .