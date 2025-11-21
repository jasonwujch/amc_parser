# 2009 AMC 10A Problem 24

## Problem

Three distinct vertices of a cube are chosen at random. What is the probability that the plane determined by these three vertices contains points inside the cube?

$\mathrm{(A)}\ \frac{1}{4} \qquad \mathrm{(B)}\ \frac{3}{8} \qquad \mathrm{(C)}\ \frac{4}{7} \qquad \mathrm{(D)}\ \frac{5}{7} \qquad \mathrm{(E)}\ \frac{3}{4}$

## Solutions

## Solution 1
First of all, the number of planes determined by any three vertices of a cube is $20$ ( $6$ faces, $6$ planes through two opposite edges, $8$ planes through three vertices forming a tetrahedron). Among these $20$ planes only the $6$ facial planes will not cut into the interior of the cube.
Secondly, to choose three vertices randomly, each of the $12$ planes that contain $4$ vertices (namely the $6$ faces plus the $6$ opposite-edge planes) will be chosen $4$ times, while each of the $8$ tetrahedral planes will be chosen once.
To conclude, the probability of a cutting plane is \[ \frac{6\cdot 4 + 8\cdot 1}{12\cdot 4 + 8\cdot 1} = \frac{24 + 8}{48 + 8} = \frac{32}{56} = \frac{4}{7}. \] Thus, the answer is $\boxed{\textbf{(C)}}$ .
---Vader10, Oct.~6 2020

## Solution 2
Pick any vertex. This influences nothing since the cube is symmetric. Note that for the plane to cross the inside of the cube, we require at least one of the two points that lie opposite to the vertex. There are two possibilities:
Body diagonal vertex: This guarantees victory. You always slice through some point inside the cube. Probability of this is $\frac{1}{7}$ .
Face diagonal vertex: In this case, the four points that lie in the same plane as the vertex and this diagonal can not be selected. We have also already counted the case where we have the body diagonal and the face diagonal, thus probability here is $\frac{3}{7}$ .
This gives total probability $\boxed{P = \frac{1}{7} + \frac{3}{7} = \frac{4}{7}}$ .

## Solution 3
We will try to use symmetry as much as possible.
Pick the first vertex $A$ , its choice clearly does not influence anything.
Pick the second vertex $B$ . With probability $3/7$ vertices $A$ and $B$ have a common edge, with probability $3/7$ they are in opposite corners of the same face, and with probability $1/7$ they are in opposite corners of the cube. We will handle each of the cases separately.
In the first case, there are $2$ faces that contain the edge $AB$ . In each of these faces there are $2$ other vertices. If one of these $4$ vertices is the third vertex $C$ , the entire triangle $ABC$ will be on a face. On the other hand, if $C$ is one of the two remaining vertices, the triangle will contain points inside the cube. Hence in this case the probability of choosing a good $C$ is $2/6 = 1/3$ .
In the second case, the triangle $ABC$ will not intersect the cube if point $C$ is one of the two points on the side that contains $AB$ . Hence the probability of $ABC$ intersecting the inside of the cube is $2/3$ .
In the third case, already the diagonal $AB$ contains points inside the cube, hence this case will be good regardless of the choice of $C$ .
Summing up all cases, the resulting probability is: \[\frac 37\cdot\frac 13 + \frac 37\cdot \frac 23 + \frac 17\cdot 1 = \boxed{\frac 47}\]

## Solution 4 (Cheap solution, same approach as Solution 3)
This problem can be approached the same way, by picking vertices, but with a much faster and kind of cheap solution: Pick any vertex A and a face it touches. For vertex B, out of the $7$ remaining vertices, $4$ of them aren't on the same face as the one chosen for vertex A, so vertex C can be placed anywhere and the plane will no matter what be in the cube. Therefore, the probability of choosing a valid vertex B is $4/7$ .

## Solution 5
There are $\binom{8}{3}=56$ ways to pick three vertices from eight total vertices; this is our denominator. In order to have three points inside the cube, they cannot be on the surface. Thus, we can use complementary probability.
There are $\binom{4}{3}=4$ ways to choose three points from the vertices of a single face. Since there are six faces, $4 \times 6 = 24$ .
Thus, the probability of what we don't want is $\frac{24}{56} = \frac{3}{7}$ . Using complementary probability,
\[1- \frac 37 = \boxed{\frac 47}\]

## The opposite of Solution 5
Since Solution 5 above describes the complementary case that doesn't fit the requirement, there'll be the direct way. Now we conduct meticulous classification for all the cases (Split the cases based on the relative positions of the three vertices.).
Case $1$ Same plane : As described in Solution 4, the 3 vertices are in the same plane. There're 24 of them.
Case $2$ Two of them are adjacent : We first pick two adjacent vertices. They have $12$ cases. Then the remaining vertex can only be located on the cubic opposite side of the two selected vertices, which has $2$ cases. So there're $12 \cdot 2=24$ of them.
Case $3$ None of them are adjacent : In this scenario, the three vertices will have one vertex surrounded. That very vertex might be any one of the 8 vertices on the cube, which leads to $8$ cases.
As there're $\binom{8}{3}=56$ overall cases and only cases 2 and 3 meet the enquirement, due to the classical probabilities, the probability is $\frac{24+8}{56} = \boxed{\frac{4}{7}}$
~Complemented by a mystery eastern egg (wtng)

## Solution 6 (Casework)
This problem is fairly simple. Start with $2$ points WLOG.
Case $1$ : You pick 2 points that are diagonally across from each other but still on the same face. This happens with probability $\frac {3}{7}$ . We notice that $4$ out of the $6$ possible outcomes include a point inside the cube. Therefore, the probability of this happening is $\frac {2}{7}$ .
Case $2$ : You pick 2 points that a directly across from each other. This happens with probability $\frac {3}{7}$ . We notice that $2$ out of the $6$ possible outcomes include a point inside the cube. Therefore, the probability of this happening is $\frac {1}{7}$ .
Case $3$ : You pick 2 points that is a space diagonal of the cube. This happens with probability $\frac {1}{7}$ . Clearly, all of the points contain a point inside the cube, so our probability is $\frac {1}{7}$ .
Adding these probabilities gives us $\boxed {\frac {4}{7}}$
~Arcticturn

## (Video solution)
Video: https://youtu.be/5PiNMIxItVQ ~DaBobWhoLikeMath1234
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .