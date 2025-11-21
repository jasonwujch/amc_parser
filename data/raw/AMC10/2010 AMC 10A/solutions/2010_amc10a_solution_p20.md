# 2010 AMC 10A Problem 20

## Problem

A fly trapped inside a cubical box with side length $1$ meter decides to relieve its boredom by visiting each corner of the box. It will begin and end in the same corner and visit each of the other corners exactly once. To get from a corner to any other corner, it will either fly or crawl in a straight line. What is the maximum possible length, in meters, of its path?

$\textbf{(A)}\ 4+4\sqrt{2} \qquad \textbf{(B)}\ 2+4\sqrt{2}+2\sqrt{3} \qquad \textbf{(C)}\ 2+3\sqrt{2}+3\sqrt{3} \qquad \textbf{(D)}\ 4\sqrt{2}+4\sqrt{3} \qquad \textbf{(E)}\ 3\sqrt{2}+5\sqrt{3}$

## Solution 1
The distance of an interior diagonal in this cube is $\sqrt{3}$ and the distance of a diagonal on one of the square faces is $\sqrt{2}$ . It is not possible for the fly to travel any interior diagonal twice, as then it would visit a corner more than once. So, the final sum can have at most $4$ as the coefficient of $\sqrt{3}$ . The other $4$ paths taken can be across a diagonal on one of the faces (try to find a such path!), so the maximum distance traveled is $\textbf{(D)}\ 4\sqrt{2}+4\sqrt{3}$ .

## Solution 2
The path of the fly consists of eight line segments, where each line segment goes from one corner to another corner. The distance of each such line segment is $1$ , $\sqrt{2}$ , or $\sqrt{3}$ .
The only way to obtain a line segment of length $\sqrt{3}$ is to go from one corner of the cube to the opposite corner. Since the fly visits each corner exactly once, it cannot traverse such a line segment twice. Also, the cube has exactly four such diagonals, so the path of the fly can contain at most four segments of length $\sqrt{3}$ . Hence, the length of the fly's path can be at most $\boxed{4 \sqrt{3} + 4 \sqrt{2}\text{, or D.}}$ . This length can be achieved by taking the path \[A \rightarrow G \rightarrow B \rightarrow H \rightarrow C \rightarrow E \rightarrow D \rightarrow F \rightarrow A.\]
[asy] import graph; unitsize(2 cm); draw((0,0)--(1,0)--(1,1)--(0,1)--cycle); draw((1,0)--(1.3,0.3)); draw((1,1)--(1.3,1.3)); draw((0,1)--(0.3,1.3)); draw((1.3,0.3)--(1.3,1.3)--(0.3,1.3)); draw((0,0)--(0.3,0.3),dashed); draw((0.3,0.3)--(1.3,0.3),dashed); draw((0.3,0.3)--(0.3,1.3),dashed); label("$A$", (0,0), SW); label("$B$", (1,0), SE); label("$C$", (1.3,0.3), E); label("$D$", (0.3,0.3), SE); label("$E$", (0,1), W); label("$F$", (1,1), E); label("$G$", (1.3,1.3), NE); label("$H$", (0.3,1.3), N); [/asy]

## Video Solution
https://youtu.be/rsURe5Xh-j0?t=1728
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .