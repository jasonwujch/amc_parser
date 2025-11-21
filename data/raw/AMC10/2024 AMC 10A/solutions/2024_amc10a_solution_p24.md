# 2024 AMC 10A Problem 24

## Problem

A bee is moving in three-dimensional space. A fair six-sided die with faces labeled $A^+, A^-, B^+, B^-, C^+,$ and $C^-$ is rolled. Suppose the bee occupies the point $(a,b,c).$ If the die shows $A^+$ , then the bee moves to the point $(a+1,b,c)$ and if the die shows $A^-,$ then the bee moves to the point $(a-1,b,c).$ Analogous moves are made with the other four outcomes. Suppose the bee starts at the point $(0,0,0)$ and the die is rolled four times. What is the probability that the bee traverses four distinct edges of some unit cube?

$\textbf{(A) }\frac{1}{54}\qquad\textbf{(B) }\frac{7}{54}\qquad\textbf{(C) }\frac{1}{6}\qquad\textbf{(D) }\frac{5}{18}\qquad\textbf{(E) }\frac{2}{5}$

### Diagrams

Diagrams have been moved to the bottom of the solutions.

## Solution 1 (Simplest)
We start by imagining the three dimensional plane.
Notice how the three dimensional plane is split into 8 different regions. There exists 8 cubes with one vertex on the point $(0,0,0)$ . We need to consider each of these cases.
We arbitrarily take a cube from one region of the three dimensional plane.
Below is a sample drawing.
Roll 1: From $(0,0,0)$ , there are 3 favorable outcomes that can occur. They are listed below.
Roll 2: WLOG, say the bee moved up one, there are then 2 ways the bee can go.
Roll 3: WLOG, say the bee moved forward one. From this point, there is again 2 ways the bee can go.
Roll 4: Finally, WLOG, say the bee moves to the left one. From that point, there are still 2 ways the bee can go.
The total probability for one cube is $\frac{3 \cdot 2 \cdot 2 \cdot 2}{6^4} \Rightarrow \frac{1}{54}$ . We have 8 of these cubes, which gives us a total probability of $\frac{8}{54}$ .
However, we have overcounted. Notice that if the bee moved down one instead of left one at roll 3, it would only have one way. This is because the bee has a choice between either the origin or a unique point. This will always occur on the third move, and because we have 8 cubes(The 3d graph has one for each quadrant), the probability of this happening is $\frac{3 \cdot 8}{6^4} = \frac{1}{54}$ .
Our probability is $\frac{8}{54} - \frac{1}{54} =$ $\boxed{\textbf{(B) }\frac{7}{54}}$ .
~Pinotation ~Minor edit by lucassf12

## Solution 2
WLOG, assume that the first two moves are equal for all possible combinations, since the direction does not matter. The first move has a $\frac{6}{6}$ probability of being along one of the $8$ unit cubes around the origin, and the second move has a $\frac{4}{6}$ chance. Now, there are two cases. We are currently on one of the points of the $2$ by $2$ squares that are aligned with the axes. The first case is if the bee moves to the corner of a cube farthest away from the origin. Here, there is a $\frac{2}{6}$ chance of this happening and a $\frac{2}{6}$ chance of the fourth move remaining on one of the cubes. The second case is if the bee moves along the same plane of the $2$ by $2$ squares previously, ending up on a point 1 away from the origin. There is a $\frac{1}{6}$ chance of this happening and a $\frac{3}{6}$ chance of remaining on one of the cubes. Now, multiply and sum for the answer. \[\frac{2}{3}\cdot(\frac{1}{3}\cdot\frac{1}{3}+\frac{1}{6}\cdot\frac{1}{2})=\frac{2}{3}\cdot(\frac{1}{9}+\frac{1}{12})\] Evaluating this gives you the answer of $\boxed{\textbf{(B) }\frac{7}{54}}$ . Solution by juwushu . Minor edits by andliu766

## Solution 3
Remove the dice. It is not necessary for this problem. It is the same problem if you instead view this problem as the bee moving one up or down in the $x, y,$ and $z$ directions.
Count the total number of ways for one cube of the 8 total ones. It is not hard to see that after the first step (which you can travel to $(1,0,0), (0,1,0),$ or $(0,0,1)$ - 3 ways), you have a total of 8 moves to traverse a face of that 1x1 cube. Hence, for each cube, you would have $8 \cdot 3 = 24$ total moves.
There are a total of 8 cubes you could have traversed, though, so multiplying this by $8$ yields $8 \cdot 8 \cdot 3.$
We have to account for overcounting. For example, when we traversed the face in the $xz$ plane $(0,0,0), (0,0,1),(1,0,0),(1,0,1),$ the number of ways that we traverse that particular face got counted twice, once from the cube in the far upper right and once from the cube in the closer upper right.
For a given face, you can go clockwise or counterclockwise, hence yielding $2$ ways. There are a total of $12$ shared faces, each one shared by exactly two faces so no additonal PIE is needed. We simply subtract $2\cdot12$ from our original count now, yielding $8 \cdot 3 \cdot 8 - 2 \cdot 12 = 168.$
With no restrictions, there are a total of $6^4$ ways to move four steps. Your probability is $\frac{168}{6^4}=\frac{7}{54}.$
~mathboy282

## Solution 4
An invariant is that the sum of all three coordinates change parity with every roll of the dice. Hence, to end up on a vertex of a unit cube, it can only be $(0,0,0)$ , $(1,1,0)$ , $(1,0,1)$ , $(0,1,1)$ , and all the negative permutations of each listed (in total, $13$ different final coordinates can be reached).
For $(0,0,0)$ , we choose two of the three coordinates to have 'cancelling' operations. Let these be $a$ , $a'$ , $b$ , $b'$ (where $a$ cancels out $a'$ , hence cannot be placed next to each other, which would be traversing the same edge). There are $3\cdot2\cdot2\cdot2=24$ ways for this (we can only have forms of $aba'b'$ or $bab'a'$ and their permutations among $a$ and $b$ ).
For $(1,1,0)$ , we must have two operations $a$ , $b$ and a pair $c$ , $c'$ . Experimenting with having $3$ of the same type of operation leads to finding a repeated edge no matter the arrangement. These can be arranged in $12$ ways (place the operations $a$ and $b$ first, placing the operations $c$ and $c'$ in the remaining spaces).
Analogously, $(-1,1,0)$ , $(1,-1,0)$ , $(-1,-1,0)$ all have the same number of ways, $12$ each (they are merely a rotation of all possibilities of $(1,1,0)$ ). Furthermore, we can generalise this to all the $8$ negative permutations of $(1,0,1)$ , $(0,1,1)$ , for a total of $12\cdot4\cdot3=144$ .
So, $\frac{24+144}{6^4}=\frac{7\cdot24}{54\cdot24}=\frac{7}{54}$ , hence we pick $\boxed{\textbf{(B) }\frac{7}{54}}$ .
-lisztepos

## Video Solution by Power Solve
https://www.youtube.com/watch?v=2uTWPiWzfB0

## Video Solution by Pi Academy (Fast and Easy ⚡️🚀)
https://youtu.be/3Dk-vmdxbrw?si=G6TcyLN2Rfwd2YYJ

## Video Solution by Innovative Minds
https://youtu.be/CxLGUPhYYDI
~i_am_suk_at_math_2

## Video Solution by SpreadTheMathLove
https://youtu.be/ryqz2nVuG34?si=T3IU_aF8TJD1qmhT

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=5535s
### Diagrams
~ Diagram by PaperMath
~ Solution diagram by juwushu Up down left right of course
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .