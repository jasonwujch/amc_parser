# 2005 AIME II Problem 10

## Problem

Given that $O$ is a regular octahedron , that $C$ is the cube whose vertices are the centers of the faces of $O,$ and that the ratio of the volume of $O$ to that of $C$ is $\frac mn,$ where $m$ and $n$ are relatively prime integers, find $m+n.$

1 Problem

- 1 Problem

- 2 Solutions 2.1 Solution 1 2.2 Solution 2

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

## Solutions

## Solution 1
Let the side of the octahedron be of length $s$ . Let the vertices of the octahedron be $A, B, C, D, E, F$ so that $A$ and $F$ are opposite each other and $AF = s\sqrt2$ . The height of the square pyramid $ABCDE$ is $\frac{AF}2 = \frac s{\sqrt2}$ and so it has volume $\frac 13 s^2 \cdot \frac s{\sqrt2} = \frac {s^3}{3\sqrt2}$ and the whole octahedron has volume $\frac {s^3\sqrt2}3$ .
Let $M$ be the midpoint of $BC$ , $N$ be the midpoint of $DE$ , $G$ be the centroid of $\triangle ABC$ and $H$ be the centroid of $\triangle ADE$ . Then $\triangle AMN \sim \triangle AGH$ and the symmetry ratio is $\frac 23$ (because the medians of a triangle are trisected by the centroid), so $GH = \frac{2}{3}MN = \frac{2s}3$ . $GH$ is also a diagonal of the cube, so the cube has side-length $\frac{s\sqrt2}3$ and volume $\frac{2s^3\sqrt2}{27}$ . The ratio of the volumes is then $\frac{\left(\frac{s^3\sqrt2}{3}\right)}{\left(\frac{2s^3\sqrt2}{27}\right)} = \frac92$ and so the answer is $\boxed{011}$ .

## Solution 2
Let the octahedron have vertices $(\pm 3, 0, 0), (0, \pm 3, 0), (0, 0, \pm 3)$ . Then the vertices of the cube lie at the centroids of the faces, which have coordinates $(\pm 1, \pm 1, \pm 1)$ . The cube has volume 8. The region of the octahedron lying in each octant is a tetrahedron with three edges mutually perpendicular and of length 3. Thus the octahedron has volume $8 \cdot \left(\frac 16 \cdot3^3\right) = 36$ , so the ratio is $\frac {36}{8} = \frac 92$ and so the answer is $\boxed{011}$ .
These problems are copyrighted © by the Mathematical Association of America.