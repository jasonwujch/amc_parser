# 2005 AMC 8 Problem 9

## Problem

In quadrilateral $ABCD$ , sides $\overline{AB}$ and $\overline{BC}$ both have length 10, sides $\overline{CD}$ and $\overline{DA}$ both have length 17, and the measure of angle $ADC$ is $60^\circ$ . What is the length of diagonal $\overline{AC}$ ?

[asy]draw((0,0)--(17,0)); draw(rotate(301, (17,0))*(0,0)--(17,0)); picture p; draw(p, (0,0)--(0,10)); draw(p, rotate(115, (0,10))*(0,0)--(0,10)); add(rotate(3)*p); draw((0,0)--(8.25,14.5), linetype("8 8")); label("$A$", (8.25, 14.5), N); label("$B$", (-0.25, 10), W); label("$C$", (0,0), SW); label("$D$", (17, 0), E);[/asy]

$\textbf{(A)}\ 13.5\qquad\textbf{(B)}\ 14\qquad\textbf{(C)}\ 15.5\qquad\textbf{(D)}\ 17\qquad\textbf{(E)}\ 18.5$

## Solutions

## Solution 1
Because $\overline{AD} = \overline{CD}$ , $\triangle ADC$ is an isosceles triangle with $\angle DAC = \angle DCA$ . Angles in a triangle add up to $180^\circ$ , and since $\angle ADC=60^\circ$ , the other two angles are also $60^\circ$ , and $\triangle ADC$ is an equilateral triangle. Therefore $\overline{AC}=\overline{DA}=\boxed{\textbf{(D)}\ 17}$ .

## Solution 2
We can divide $\overline{CD}$ in half and connect this point to A, dividing $\triangle ADC$ in half. This means the base will be $\frac{17}{2}$ and the hypotenuse will be 17. By using the Pythagorean's Theorem, we see that if the base and height are shared, the hypotenuse should be the same. This tells us that the length of $\overline{AC} = \boxed{(D) 17}$ .
~Champion1234

## Solution 3 (Easiest)
Take an equilateral triangle with side length $17$ . $\triangle ADC$ is congruent to this by $SAS$ , hence it is equilateral. The answer is $\boxed{\textbf{(D)}17}$ .
~yofro

## Video Solution by OmegaLearn
https://youtu.be/abSgjn4Qs34?t=3034
~pi_is_3.14
### See Also