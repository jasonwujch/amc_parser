# 2023 AMC 10A Problem 18

## Problem

A rhombic dodecahedron is a solid with $12$ congruent rhombus faces. At every vertex, $3$ or $4$ edges meet, depending on the vertex. How many vertices have exactly $3$ edges meet?

$\textbf{(A) }5\qquad\textbf{(B) }6\qquad\textbf{(C) }7\qquad\textbf{(D) }8\qquad\textbf{(E) }9$

## Solution 1
Note Euler's formula where $\text{Vertices}+\text{Faces}-\text{Edges}=2$ . There are $12$ faces. There are $24$ edges, because there are 12 faces each with four edges and each edge is shared by two faces. Now we know that there are $2-12+24=14$ vertices. Now note that the sum of the degrees of all the points is $48$ (the number of edges times 2). Let $x=$ the number of vertices with $3$ edges. Now we know $\frac{3x+4(14-x)}{2}=24$ . Solving this equation gives $x = \boxed{\textbf{(D) }8}$ . ~aiden22gao ~zgahzlkw (LaTeX) ~ESAOPS (Simplified)

## Solution 2
Let $x$ be the number of vertices with 3 edges, and $y$ be the number of vertices with 4 edges. Since there are $\frac{4*12}{2}=24$ edges on the polyhedron, we can see that $\frac{3x+4y}{2}=24$ . Then, $3x+4y=48$ . Notice that by testing the answer choices, (D) is the only one that yields an integer solution for $y$ . Thus, the answer is $\boxed{\textbf{(D) }8}$ .
~Mathkiddie

## Solution 3
With $12$ rhombi, there are $4\cdot12=48$ total boundaries. Each edge is used as a boundary twice, once for each face on either side. Thus we have $\dfrac{48}2=24$ total edges.
Let $A$ be the number of vertices with $3$ edges (this is what the problem asks for) and $B$ be the number of vertices with $4$ edges. We have $3A + 4B = 48$ .
Euler's formula states that, for all convex polyhedra, $V-E+F=2$ . In our case, $V-24+12=2\implies V=14.$ We know that $A+B$ is the total number of vertices as we are given that all vertices are connected to either $3$ or $4$ edges. Therefore, $A+B=14.$
We now have a system of two equations. Solving the system yields $A=\boxed{\textbf{(D) }8}$ .
Even without Euler's formula, we can do a bit of answer guessing. From $3A+4B=48$ , we take mod $4$ on both sides.
\[3A+4B\equiv48\pmod{4}\] \[3A\equiv0\pmod{4}\]
We know that $3A$ must be divisible by $4$ . We know that the factor of $3$ will not affect the divisibility by $4$ of $3A$ , so we remove the $3$ . We know that $A$ is divisible by $4$ . Checking answer choices, the only one divisible by $4$ is indeed $A=\boxed{\textbf{(D) }8}$ .
~Technodoggo ~zgahzlkw (small edits) ~ESAOPS (LaTeX)

## Solution 4
Note that Euler's formula is $V+F-E=2$ . We know $F=12$ from the question. We also know $E = \frac{12 \cdot 4}{2} = 24$ because every face has $4$ edges and every edge is shared by $2$ faces. We can solve for the vertices based on this information.
Using the formula we can find: \[V + 12 - 24 = 2\] \[V = 14\] Let $t$ be the number of vertices with $3$ edges and $f$ be the number of vertices with $4$ edges. We know $t+f = 14$ from the question and $3t + 4f = 48$ . The second equation is because the total number of points is $48$ because there are 12 rhombuses of $4$ vertices. Now, we just have to solve a system of equations. \[3t + 4f = 48\] \[3t + 3f = 42\] \[f = 6\] \[t = 8\] Our answer is simply just $t$ , which is $\boxed{\textbf{(D) }8}$ ~musicalpenguin

## Solution 5
Each of the twelve rhombi has two pairs of angles across from each other that must be congruent. If both pairs of angles occur at $4$ -point intersections, we have a grid of squares. If both occur at $3$ -point intersections, we would have a cube with six square faces. Therefore, two of the points must occur at a $3$ -point intersection and two at a $4$ -point intersection.
Since each $3$ -point intersection has $3$ adjacent rhombuses, we know the number of $3$ -point intersections must equal the number of $3$ -point intersections per rhombus times the number of rhombuses over $3$ . Since there are $12$ rhombuses and two $3$ -point intersections per rhombus, this works out to be:
$\frac{2\cdot12}{3}$
Hence: $\boxed{\textbf{(D) }8}$ ~hollph27 ~Minor edits by FutureSphinx

## Solution 6 (Based on previous knowledge)
Note that a rhombic dodecahedron is formed when a cube is turned inside out (as seen here), thus there are 6 4-vertices (corresponding to each face of the cube) and 8 3-vertices (corresponding to each corner of the cube). Thus the answer is $\boxed{\textbf{(D) }8}$

## Solution 7 (Dual)
Note that a rhombic dodecahedron is the dual of a cuboctahedron. A cuboctahedron has $8$ triangular faces, which correspond to $\boxed{\textbf{(D) }8}$ vertices on a rhombic dodecahedron that have $3$ edges.

## Solution 8 (Uses Solution 2)
Continue through solution 2 until you get $3x+4y=48$ . Then we have that $3x = 48-4y = 4(12-y) = \text{multiple of 4}$ so $x$ is a multiple of $4.$ The only multiple of 4 answer choice is $8 = \boxed{(D)}$
~KindToucan

## Video Solution (Easy To Follow)
https://www.youtube.com/watch?v=SFxfxXsJaN8&t=7s

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=KLoAqmdqx_C55pEq&t=4063 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=fFif-OiVZnkdTTv0&t=5105
~Math-X

## Video Solution
https://youtu.be/5OuzPFvJPEY

## Video Solution
https://www.youtube.com/watch?v=Z-OCnHUwnj0

## Video Solution by OmegaLearn
https://youtu.be/0AG5XmWY-D8

## Video Solution by TheBeautyofMath
https://www.youtube.com/watch?v=zvKijDeiYUs

## Video Solution
https://youtu.be/0ssjr8KjOzk
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
### See Also
https://en.wikipedia.org/wiki/Rhombic_dodecahedron
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .