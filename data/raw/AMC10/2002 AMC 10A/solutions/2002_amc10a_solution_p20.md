# 2002 AMC 10A Problem 20

## Problem

Points $A,B,C,D,E$ and $F$ lie, in that order, on $\overline{AF}$ , dividing it into five segments, each of length 1. Point $G$ is not on line $AF$ . Point $H$ lies on $\overline{GD}$ , and point $J$ lies on $\overline{GF}$ . The line segments $\overline{HC}, \overline{JE},$ and $\overline{AG}$ are parallel. Find $HC/JE$ .

$\text{(A)}\ 5/4 \qquad \text{(B)}\ 4/3 \qquad \text{(C)}\ 3/2 \qquad \text{(D)}\ 5/3 \qquad \text{(E)}\ 2$

## Solution 1
First we can draw an image. [asy] unitsize(0.8 cm); pair A, B, C, D, E, F, G, H, J; A = (0,0); B = (1,0); C = (2,0); D = (3,0); E = (4,0); F = (5,0); G = (-1.5,4); H = extension(D, G, C, C + G - A); J = extension(F, G, E, E + G - A); draw(A--F--G--cycle); draw(B--G); draw(C--G); draw(D--G); draw(E--G); draw(C--H); draw(E--J); label("$A$", A, SW); label("$B$", B, S); label("$C$", C, S); label("$D$", D, S); label("$E$", E, S); label("$F$", F, SE); label("$G$", G, NW); label("$H$", H, W); label("$J$", J, NE); [/asy]
Since $\overline{AG}$ and $\overline{CH}$ are parallel, triangles $\triangle GAD$ and $\triangle HCD$ are similar. Hence, $\frac{CH}{AG} = \frac{CD}{AD} = \frac{1}{3}$ .
Since $\overline{AG}$ and $\overline{JE}$ are parallel, triangles $\triangle GAF$ and $\triangle JEF$ are similar. Hence, $\frac{EJ}{AG} = \frac{EF}{AF} = \frac{1}{5}$ . Therefore, $\frac{CH}{EJ} = \left(\frac{CH}{AG}\right)\div\left(\frac{EJ}{AG}\right) = \left(\frac{1}{3}\right)\div\left(\frac{1}{5}\right) = \boxed{\frac{5}{3}}$ . The answer is $\boxed{(D) 5/3}$ .

## Solution 2
As angle F is clearly congruent to itself, we get from AA similarity, $\triangle AGF \sim \triangle EJF$ ; hence $\frac {AG}{JE} =5$ . Similarly, $\frac {AG}{HC} = 3$ . Thus, $\frac {HC}{JE}=\left(\frac{AG}{JE}\right)\left(\frac{HC}{AG}\right) = \boxed{\frac {5}{3}\Rightarrow \text{(D)}}$ .

## Solution 3
Assume an arbitrary value of $AG=15$ WLOG. $\overline{AG}$ and $\overline{CH}$ are parallel, so $\triangle GAD$ and $\triangle HCD$ are similar. So, $\frac{AD}{CD}=3=\frac{GA}{HC}$ which means $HC=5$ . By the same logic, $JE=3$ , so $\frac{HC}{JE}=\frac{5}{3}$ .

## Video Solution
https://www.youtube.com/watch?v=AU2PJeMZ7R0 ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .