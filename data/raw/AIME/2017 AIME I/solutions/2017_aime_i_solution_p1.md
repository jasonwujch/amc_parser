# 2017 AIME I Problem 1

## Problem

Fifteen distinct points are designated on $\triangle ABC$ : the 3 vertices $A$ , $B$ , and $C$ ; $3$ other points on side $\overline{AB}$ ; $4$ other points on side $\overline{BC}$ ; and $5$ other points on side $\overline{CA}$ . Find the number of triangles with positive area whose vertices are among these $15$ points.

## Solution 1
Every triangle is uniquely determined by 3 points. There are $\binom{15}{3}=455$ ways to choose 3 points, but that counts the degenerate triangles formed by choosing three points on a line. There are $\binom{5}{3}$ invalid cases on segment $AB$ , $\binom{6}{3}$ invalid cases on segment $BC$ , and $\binom{7}{3}$ invalid cases on segment $CA$ for a total of $65$ invalid cases. The answer is thus $455-65=\boxed{390}$ .

## Solution 2
We simply choose $3$ points from $15$ to begin with since a triangle consists of $3$ points and there are $15$ points total. That gives us $\binom{15}{3}$ . Now, we need to subtract of the degenerate triangles. These are just the triangles that are collinear. We can count the number of degenerate triangles on each side of $ABC$ , then subtract is from $\binom{15}{3}$ . For $\overline{AB}$ , we have $\binom{5}{3}$ degenerate triangles (dont forget $A$ and $B$ ), for $\overline{BC}$ , we have $\binom{6}{3}$ degenerate triangles, and for $\overline{AC}$ , we have $\binom{7}{3}$ degenerate triangles. So, our final answer is $\binom{15}{3} - \binom{7}{3} - \binom{6}{3} - \binom{5}{3} = \boxed{390}$
-jb2015007

## Video Solution
https://youtu.be/BiiKzctXDJg ~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .