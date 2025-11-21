# 2016 AIME I Problem 3

## Problem

A regular icosahedron is a $20$ -faced solid where each face is an equilateral triangle and five triangles meet at every vertex. The regular icosahedron shown below has one vertex at the top, one vertex at the bottom, an upper pentagon of five vertices all adjacent to the top vertex and all in the same horizontal plane, and a lower pentagon of five vertices all adjacent to the bottom vertex and all in another horizontal plane. Find the number of paths from the top vertex to the bottom vertex such that each part of a path goes downward or horizontally along an edge of the icosahedron, and no vertex is repeated.

[asy] size(3cm); pair A=(0.05,0),B=(-.9,-0.6),C=(0,-0.45),D=(.9,-0.6),E=(.55,-0.85),F=(-0.55,-0.85),G=B-(0,1.1),H=F-(0,0.6),I=E-(0,0.6),J=D-(0,1.1),K=C-(0,1.4),L=C+K-A; draw(A--B--F--E--D--A--E--A--F--A^^B--G--F--K--G--L--J--K--E--J--D--J--L--K); draw(B--C--D--C--A--C--H--I--C--H--G^^H--L--I--J^^I--D^^H--B,dashed); dot(A^^B^^C^^D^^E^^F^^G^^H^^I^^J^^K^^L); [/asy]

## Solution
Think about each plane independently. From the top vertex, we can go down to any of 5 different points in the second plane. From that point, there are 9 ways to go to another point within the second plane: rotate as many as 4 points clockwise or as many 4 counterclockwise, or stay in place. Then, there are 2 paths from that point down to the third plane. Within the third plane, there are 9 paths as well (consider the logic from the second plane). Finally, there is only one way down to the bottom vertex. Therefore there are $5 \cdot 9 \cdot 2 \cdot 9 \cdot 1=\boxed{810}$ paths.

## Solution 2: Casework
Assume an ant is on the top of this icosahedron. Note that the icosahedron has two pentagon planes and two points where the ant starts and ends. Also note that when the ant hits a vertex of the pentagon, there is only two ways to go down. When the ant ends up at the last vertex and is about to head down, there is only one way to go down.
Case $1$ : The ant move down to the first pentagon, then the next pentagon, and finally to the last point in a total of four moves; there are a total of $5 \cdot 2 \cdot 1 = 10$ ways to achieve this.
Case $2$ : The ant goes to the first pentagon and moves to another vertex in the same pentagon. The ant has a total of $8$ paths doing this since it may go through $1, 2, 3,$ or $4$ edges from either two directions when going across the edges of the pentagon (recall the ant may not repeat a move to another vertex) . Now the ant moves to the second pentagon below. The ant again has a total of $8$ moves if he wanders around the pentagon. Finally, the ant moves down after wandering to the last vertex. There is a total of $5 \cdot 8 \cdot 2 \cdot 8 = 640$ ways.
Case $3$ : Assume the ant goes to the first pentagon and wanders around. Then the ant goes the next pentagon and then heads directly to the last vertex. There are $5 \cdot 8 \cdot 2 = 80$ ways.
Case $4$ : Now let the ant go to the first pentagon and then go directly down to the next pentagon. The ant wanders around the second pentagon before heading to the last vertex. Like case $3$ above, there are $5 \cdot 2 \cdot 8 = 80$ ways.
Adding up all four cases, we get $10 + 640 + 80 + 80 =\boxed{810}$ total paths, as desired. ~skyscraper

## Solution 3
Go to 2020 AMC 10A #19 , and connect all of the centers of the faces on the dodecahedron to get the icosahedron. The answer is $\boxed{810}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .