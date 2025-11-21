# 2024 AMC 8 Problem 18

## Problem

Three concentric circles centered at $O$ have radii of $1$ , $2$ , and $3$ . Points $B$ and $C$ lie on the largest circle. The region between the two smaller circles is shaded, as is the portion of the region between the two larger circles bounded by central angles $BOC$ , as shown in the figure below. Suppose the shaded and unshaded regions are equal in area. What is the measure of $\angle{BOC}$ in degrees?

[asy] size(150); import graph; draw(circle((0,0),3)); real radius = 3; real angleStart = -54; // starting angle of the sector real angleEnd = 54; // ending angle of the sector label("$O$",(0,0),W); pair O = (0, 0); filldraw(arc(O, radius, angleStart, angleEnd)--O--cycle, gray); filldraw(circle((0,0),2),gray); filldraw(circle((0,0),1),white); draw((1.763,2.427)--(0,0)--(1.763,-2.427)); label("$B$",(1.763,2.427),NE); label("$C$",(1.763,-2.427),SE); [/asy] $\textbf{(A) } 108\qquad\textbf{(B) } 120\qquad\textbf{(C) } 135\qquad\textbf{(D) } 144\qquad\textbf{(E) } 150$

## Solution 1
Let $x=\angle{BOC}$ .
We see that the shaded region is the inner ring plus a sector $x^\circ$ of the outer ring. Using the formula for the area of a circle ( $A = \pi r^2$ ), we find that the area of $x$ is $\left( 4 \pi - \pi \right)+\frac{x}{360} \left( 9 \pi - 4 \pi \right)$ . This simplifies to $3 \pi + \frac{x}{360}(5 \pi)$ .
The unshaded portion is comprised of the smallest circle plus the sector $(360-x)^\circ$ of the outer ring, which evaluates to $\pi + \frac{360-x}{360}(5 \pi)$ .
We are told these are equal. Therefore, $3 \pi + \frac{x}{360}(5 \pi) = \pi + \frac{360-x}{360}(5 \pi)$ . Solving for $x$ reveals $x=\boxed{\textbf{(A) } 108}$ .
~MrThinker
~Dash11 (Edited coefficient of pi. Credit goes to MrThinker for the solution and explanation.)

## Solution 2
Notice that for the 3rd most outer ring of the circle, the ratio of the shaded region to non-shaded region is the ratio of $\angle{BOC}$ to $360-\angle{BOC}$ . With that, all we need to do is solve for the shaded region.
The inner most circle has radius $1$ , and the second circle has radius 2. Therefore, the first shaded area has $4 \pi - \pi = 3 \pi$ area. The circle has total area $9 \pi$ , so the other shaded region must have $1.5 \pi$ area, as the non-shaded and shaded area is equivalent. So for the 3rd outer ring, the total area is $9 \pi - 4 \pi = 5 \pi$ , so the non-shaded part of the outer ring is $5 \pi - 1.5 \pi = 3.5 \pi$ .
Now as said before, the ratio of these two areas is the ratio of $\angle{BOC}$ and $360 - \angle{BOC}$ . So, $\frac{3.5}{1.5} = \frac{7}{3}$ . We have $7x:3x$ where $7x+3x = 360$ , $x = 36$ , so our answer is $3x = 108, \boxed{(A) 108}$ .
~MaxyMoosy

## Solution 3 (Ruler Tool)
The AMC 8 test allows a ruler tool that you can rotate and drag. You can use the tool to make a straight segment (which we know is $180$ degrees), and we let the angle of desire be $x$ . We can estimate that $180-x$ is just about $30$ degrees short of $x$ itself, so $x-30=180-x$ , solving gives $x=105$ , therefore the closest answer is $\boxed{\textbf{(A)}\,108}$ .

## Solution 4
Suppose the desired angle is some fraction $x$ of the total degree measure of the circle. We now compile a list of the shaded and unshaded areas. The inner circle of radius $1$ is completely unshaded, so it contributes $1$ to the unshaded area. (Everything will be a multiple of $\pi$ , so we omit it.) The inner annulus has area $2^2 - 1^2 = 3$ , which it contributes to the shaded area. The outer annulus has a total area of $3^2 - 2^2 = 5$ ; the fraction $x$ is shaded, so the shaded portion of the outer annulus contributes $5x$ to the shaded area, while the other $1 - x$ fraction is unshaded, so the unshaded portion contributes $5(1-x)$ to the unshaded area. We now equate and solve. \[1 + 5(1-x) = 3 + 5x\] Upon solving, we find that $x = \frac{3}{10}$ , so the degree measure is $360 \cdot \frac{3}{10} = \boxed{\textbf{(A)} 108}$ .
~ cxsmi

## Video Solution 1 by Math-X (First fully understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=lg7OGcJ7OwdDFHAn&t=4872
~Math-X

## Video Solution 2 (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=A8VVtUidVZlXDyrN&t=2517
~hsnacademy

## Video Solution 3 (super clear!) by Power Solve
https://youtu.be/TlTN7EQcFvE

## Video Solution 4 by SpreadTheMathLove
https://www.youtube.com/watch?v=Svibu3nKB7E

## Video Solution 5 by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=V-xN8Njd_Lc

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/JZx2-QX--Os
~mr_mathman
~NiuniuMaths

## Video Solution 6 by OmegaLearn.org
https://youtu.be/b_pfNdmLp8A

## Video Solution 7 by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=ahVNjSlwKmA

## Video Solution 8 by Interstigation
https://youtu.be/ktzijuZtDas&t=2045

## Video Solution 9 by Dr. David
https://youtu.be/ySuCpQZtsZY

## Video Solution by WhyMath
https://youtu.be/v0Aba87nnA4

## Official Video Solution (Forming a trivial algebraic equation!)
https://www.youtube.com/watch?v=0bqpjCvqJsE ~TheMathGeek (Subscribe!)

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/OwJvuq6F7sQ
~Thesmartgreekmathdude
### See Also