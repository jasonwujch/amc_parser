# 1999 AMC 8 Problem 21

## Problem

The degree measure of angle $A$ is

[asy] unitsize(12); draw((0,0)--(20,0)--(1,-10)--(9,5)--(18,-8)--cycle); draw(arc((1,-10),(1+19/sqrt(461),-10+10/sqrt(461)),(25/17,-155/17),CCW)); draw(arc((19/3,0),(19/3-8/17,-15/17),(22/3,0),CCW)); draw(arc((900/83,-400/83),(900/83+19/sqrt(461),-400/83+10/sqrt(461)),(900/83 - 9/sqrt(97),-400/83 + 4/sqrt(97)),CCW)); label(rotate(30)*"$40^\circ$",(2,-8.9),ENE); label("$100^\circ$",(21/3,-2/3),SE); label("$110^\circ$",(900/83,-317/83),NNW); label("$A$",(0,0),NW); [/asy]

$\text{(A)}\ 20 \qquad \text{(B)}\ 30 \qquad \text{(C)}\ 35 \qquad \text{(D)}\ 40 \qquad \text{(E)}\ 45$

## Solution

## Solution 1
Angle-chasing using the small triangles:
Use the line below and to the left of the $110^\circ$ angle to find that the rightmost angle in the small lower-left triangle is $180 - 110 = 70^\circ$ .
Then use the small lower-left triangle to find that the remaining angle in that triangle is $180 - 70 - 40 = 70^\circ$ .
Use congruent vertical angles to find that the lower angle in the smallest triangle containing $A$ is also $70^\circ$ .
Next, use line segment $AB$ to find that the other angle in the smallest triangle containing $A$ is $180 - 100 = 80^\circ$ .
The small triangle containing $A$ has a $70^\circ$ angle and an $80^\circ$ angle. The remaining angle must be $180 - 70 - 80 = \boxed{30^\circ, B}$

## Solution 2
The third angle of the triangle containing the $100^\circ$ angle and the $40^\circ$ angle is $180^\circ - 100^\circ - 40^\circ = 40^\circ$ . It follows that $A$ is the third angle of the triangle consisting of the found $40^\circ$ angle and the given $110^\circ$ angle. Thus, $A$ is a $180^\circ - 110^\circ - 40^\circ = 30^\circ$ angle, and so the answer is $\boxed{30^\circ, \textbf{B}}$ .

## Video Solution by OmegaLearn
https://youtu.be/suaYxFnoU6E?t=99

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://youtu.be/X_SbFalrsV8?si=BLdIghVBvHNMmEIn
### See Also