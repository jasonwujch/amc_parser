# 2002 AMC 8 Problem 22

## Problem

Six cubes, each an inch on an edge, are fastened together, as shown. Find the total surface area in square inches. Include the top, bottom, and sides.

[asy] /* AMC8 2002 #22 Problem */ draw((0,0)--(0,1)--(1,1)--(1,0)--cycle); draw((0,1)--(0.5,1.5)--(1.5,1.5)--(1,1)); draw((1,0)--(1.5,0.5)--(1.5,1.5)); draw((0.5,1.5)--(1,2)--(1.5,2)); draw((1.5,1.5)--(1.5,3.5)--(2,4)--(3,4)--(2.5,3.5)--(2.5,0.5)--(1.5,.5)); draw((1.5,3.5)--(2.5,3.5)); draw((1.5,1.5)--(3.5,1.5)--(3.5,2.5)--(1.5,2.5)); draw((3,4)--(3,3)--(2.5,2.5)); draw((3,3)--(4,3)--(4,2)--(3.5,1.5)); draw((4,3)--(3.5,2.5)); draw((2.5,.5)--(3,1)--(3,1.5));[/asy]

$\textbf{(A)}\ 18\qquad\textbf{(B)}\ 24\qquad\textbf{(C)}\ 26\qquad\textbf{(D)}\ 30\qquad\textbf{(E)}\ 36$

## Solution
Count the number of sides that are not exposed, where a cube is connected to another cube and subtract it from the total number of faces. There are $5$ places with two adjacent cubes, covering $10$ sides, and $(6)(6)=36$ faces. The exposed surface area is $36-10 = \boxed{\text{(C)}\ 26}$ .

## Solution 2
We can count the number of showing faces from each side. One thing that we notice is that the front face has the same number of squares as the back face, the side faces have the same surface area, etc. Therefore, we are looking for $2($ front surface area $+$ side surface area $+$ top surface area $)$ . We find that this is $2(5 + 4 + 4) = 2 * 13 = \boxed{\text{(C)}\ 26}$ .
Solution by ILoveMath31415926535

## Video Solution
https://www.youtube.com/watch?v=PyvyO5JMgHI ~David

## Video Solution by WhyMath
https://youtu.be/cyuum8M3hEg
### See Also