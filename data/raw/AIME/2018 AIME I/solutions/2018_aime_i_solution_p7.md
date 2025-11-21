# 2018 AIME I Problem 7

## Problem

A right hexagonal prism has height $2$ . The bases are regular hexagons with side length $1$ . Any $3$ of the $12$ vertices determine a triangle. Find the number of these triangles that are isosceles (including equilateral triangles).

## Solution 1
We can consider two cases: when the three vertices are on one base, and when the vertices are on two bases.
Case 1: vertices are on one base. Then we can call one of the vertices $A$ for distinction. Either the triangle can have sides $1, 1, \sqrt{3}$ with 6 cases or $\sqrt{3}, \sqrt{3}, \sqrt{3}$ with 2 cases. This can be repeated on the other base for $16$ cases.
Case 2: The vertices span two bases. WLOG call the only vertex on one of the bases $X$ . Call the closest vertex on the other base $B$ , and label clockwise $C, D, E, F, G$ . We will multiply the following scenarios by $12$ , because the top vertex can have $6$ positions and the top vertex can be on the other base. We can have $XCG, XDF$ , but we are not done! Don't forget that the problem statement implies that the longest diagonal in a base is $2$ and the height is $2$ , so $XBE$ is also correct! Those are the only three cases, so there are $12*3=36$ cases for this case.
In total there's $\boxed{052}$ cases.

## Solution 2
If there are two edges on a single diameter, there would be six diameters. There are four ways to put the third number, and four equilateral triangles. There are $4+ 2 \cdot 2\cdot 6 = 28$ ways. Then, if one length was $\sqrt{3}$ but no side on the diameter, there would be twelve was to put the $\sqrt{3}$ side, and two ways to put the other point. $2 \cdot 12 = 24$ for four ways to put the third point. Adding the number up, the final answer is $24+28 = \boxed{052}.$
~kevinmathz~

## Solution 3
To start, let's find the distances from any vertex (call it A, doesn't matter since the prism is symmetrical) to all the other 11 vertices. Using Pythagorean relations, we find that the distances are $1$ , $\sqrt{3}$ , $2$ , $\sqrt{3}$ , $1$ , $\sqrt{7}$ , $\sqrt{5}$ , $2$ , $\sqrt{5}$ , $\sqrt{7}$ , and $\sqrt{8}$ .
We can clearly form an isosceles triangle using any vertex and any two neighboring edges that are equal. There are 12 total vertices, all of which are symmetrical to the vertex A. Thus, for each vertex, we can form 5 isosceles triangles (with neighboring edges $1$ - $1$ , $2$ - $2$ , $\sqrt{3}$ - $\sqrt{3}$ , $\sqrt{5}$ - $\sqrt{5}$ , and $\sqrt{7}$ - $\sqrt{7}$ ) , so have so far $12 \times 5 = 60$ isosceles triangles.
To check for overcounting, note that isosceles triangles can be split into two major categories: equilateral isosceles, and non-equilateral isosceles. We only counted non-equilateral isosceles triangles once since there is only one vertex whose two neighboring edges are equal. But equilateral triangles were counted three times (namely once for each vertex).
By observation, there are only 4 equilateral triangles (1-1-1 side lengths), two on each hexagonal face. Since we counted each two more times than we should of (three instead of once), we will subtract ( $4$ eq. triangles) $\times$ ( $2$ overcounts per eq. triangle) = $8$ overcounts.
Finally, we have $60 - 8$ overcounts = $\boxed{052}$ isoceles triangles.

## Solution 4
Start by drawing the hexagonal prism. Start from one of the points, let's call it $A$ . From simple inspection, we can see that each point we choose creates $4$ isosceles triangles; $A$ and the two adjacent points, $A$ and the two points adjacent to those, $A$ and the adjacent point on the other face, and $A$ and the two points adjacent to those. Here, we have $12\cdot4\Rightarrow48$ isosceles triangles.
Next, notice that you can create an isosceles triangle with the bases of the hexagonal prism. Let's say that our base, starting from the very left-most point of the hexagon, has points $A, B, C, D, E, F$ , rotating counter-clockwise. We can create a triangle with either points $\bigtriangleup{BCE}$ or $\bigtriangleup{BCF}$ . WLOG, assuming we use $\bigtriangleup{BCE}$ , we can use the Law of Cosines and find that $\overline{CE}$ = $\sqrt{3}$ . Thus, this would mean $\overline{CF}$ is $2$ , which is the exactly the same length as the height of the hexagonal prism. There are $4$ possibilities of this case, so our final solution is $48+4=\boxed{052}$ .
Solution by IronicNinja~

## Solution 5 (Official MAA)
There are $2$ equilateral and $6$ other isosceles triangles on each base, providing a total of $16$ triangles when all $3$ vertices are chosen from the same base. To count the rest of the isosceles triangles, there are $2$ ways to choose the base that will contain $2$ vertices. Assume that $2$ vertices have been chosen from the bottom base. Then there are no isosceles triangles if the $2$ vertices on the bottom base are adjacent vertices of the hexagon, $6\cdot 2=12$ isosceles triangles if the $2$ vertices on the bottom base have $1$ vertex between them on the hexagon, and $3\cdot2=6$ isosceles triangles if the $2$ vertices on the bottom base have $2$ vertices between them on the hexagon.
The total number of isosceles triangles is $16+2(12+6)=52.$

## Solution 6 (easy)
possible options for the side lengths of the triange are: $(2,2,\sqrt8); (\sqrt3, \sqrt3, \sqrt3); (\sqrt3, \sqrt5, \sqrt5); (\sqrt3, \sqrt7, \sqrt7); (1,1,\sqrt3).$ do casework to get $12+12+12+12+4$ where $4$ is for the number of equilateral triangles.
~YBSuburbanTea

## Video Solution by Punxsutawney Phil
https://www.youtube.com/watch?v=oc-cDRIEzoo
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .