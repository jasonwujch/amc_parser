# 2015 AMC 8 Problem 12

## Problem

How many pairs of parallel edges, such as $\overline{AB}$ and $\overline{GH}$ or $\overline{EH}$ and $\overline{FG}$ , does a cube have?

[asy] import three; currentprojection=orthographic(1/2,-1,1/2); /* three - currentprojection, orthographic */ draw((0,0,0)--(1,0,0)--(1,1,0)--(0,1,0)--cycle); draw((0,0,0)--(0,0,1)); draw((0,1,0)--(0,1,1)); draw((1,1,0)--(1,1,1)); draw((1,0,0)--(1,0,1)); draw((0,0,1)--(1,0,1)--(1,1,1)--(0,1,1)--cycle); label("$D$",(0,0,0),S); label("$A$",(0,0,1),N); label("$H$",(0,1,0),S); label("$E$",(0,1,1),N); label("$C$",(1,0,0),S); label("$B$",(1,0,1),N); label("$G$",(1,1,0),S); label("$F$",(1,1,1),N); [/asy]

$\textbf{(A) }6\qquad\textbf{(B) }12\qquad\textbf{(C) }18\qquad\textbf{(D) }24\qquad \textbf{(E) }36$

## Solutions

## Solution 1
We first count the number of pairs of parallel lines that are in the same direction as $\overline{AB}$ . The pairs of parallel lines are $\overline{AB}\text{ and }\overline{EF}$ , $\overline{CD}\text{ and }\overline{GH}$ , $\overline{AB}\text{ and }\overline{CD}$ , $\overline{EF}\text{ and }\overline{GH}$ , $\overline{AB}\text{ and }\overline{GH}$ , and $\overline{CD}\text{ and }\overline{EF}$ . These are $6$ pairs total. We can do the same for the lines in the same direction as $\overline{AE}$ and $\overline{AD}$ . This means there are $6\cdot 3=\boxed{\textbf{(C) } 18}$ total pairs of parallel lines.

## Solution 2
Look at any edge, let's say $\overline{AB}$ . There are three ways we can pair $\overline{AB}$ with another edge. $\overline{AB}\text{ and }\overline{EF}$ , $\overline{AB}\text{ and }\overline{HG}$ , and $\overline{AB}\text{ and }\overline{DC}$ . There are 12 edges on a cube. 3 times 12 is 36. We have to divide by 2 because every pair is counted twice, so $\frac{36}{2}$ is $\boxed{\textbf{(C) } 18}$ total pairs of parallel lines.

## Solution 3
We can use the feature of 3-Dimension in a cube to solve the problem systematically. For example, in the 3-D of the cube, $\overline{AB}$ , $\overline{BC}$ , and $\overline{BF}$ have $4$ different parallel edges respectively. So it gives us the total pairs of parallel lines are $\binom{4}{2}\cdot3 =\boxed{\textbf{(C) } 18}$ .
--LarryFlora

## Solution 4
Our first case are lines on the same plane. There are two pairs of parallel lines for a square, and there are 6 squares, which give us $6\cdot2=12$ cases.
The next cases we need to analyze are the parallel lines on opposite planes (lines such as $\overline{EF}\text{ and } \overline{DC}$ ). There are 2 pairs for every 2 planes, and there are 6 planes in total, giving us $2\cdot3=6$ cases.
Adding up the cases, we get $12+6 = \boxed{\textbf{(C) } 18}$

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/iJC0Wqd1ZcU
~Education, the Study of Everything

## Video Solution 2
https://youtu.be/7bgsUa62d4g
~savannahsolver
### See Also