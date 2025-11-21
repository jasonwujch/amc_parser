# 2018 AMC 8 Problem 4

## Problem

The twelve-sided figure shown has been drawn on $1 \text{ cm}\times 1 \text{ cm}$ graph paper. What is the area of the figure in $\text{cm}^2$ ?

[asy] unitsize(8mm); for (int i=0; i<7; ++i) { draw((i,0)--(i,7),gray); draw((0,i+1)--(7,i+1),gray); } draw((1,3)--(2,4)--(2,5)--(3,6)--(4,5)--(5,5)--(6,4)--(5,3)--(5,2)--(4,1)--(3,2)--(2,2)--cycle,black+2bp); [/asy]

$\textbf{(A) } 12 \qquad \textbf{(B) } 12.5 \qquad \textbf{(C) } 13 \qquad \textbf{(D) } 13.5 \qquad \textbf{(E) } 14$

## Solution 1
We count $3 \cdot 3=9$ unit squares in the middle, and $8$ small triangles, which gives 4 rectangles each with an area of $1$ . Thus, the answer is $9+4=\boxed{\textbf{(C) } 13}$ .

## Solution 2
We can see here that there are $9$ total squares in the middle. We also see that the triangles that make the corners of the shape have an area half the squares' area. Then, we can easily find that each corner has an area of one square and there are $4$ corners so we add that to the original 9 squares to get $9+4=\boxed{\textbf{(C) } 13}$ . That is how I did it.

## Solution 3
We can apply Pick's Theorem here. There are $8$ lattice points, and $12$ lattice points on the boundary. Then,
\[8 + 12 \div 2 - 1 = \boxed {\textbf{(C) }13}.\]

## Solution 4
Use the Shoelace Theorem and get $\boxed{\textbf{(C) } 13}$ .
~SaxStreak

## Video Solution (CRITICAL THINKING!!!)
https://youtu.be/7qY99daRZUA
~Education, the Study of Everything

## Video Solution
https://youtu.be/huLjsiLQS90
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/51K3uCzntWs?t=1338
~ pi_is_3.14
### See Also