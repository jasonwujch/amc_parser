# 2015 AMC 10B Problem 20

## Problem

Erin the ant starts at a given corner of a cube and crawls along exactly 7 edges in such a way that she visits every corner exactly once and then finds that she is unable to return along an edge to her starting point. How many paths are there meeting these conditions?

$\textbf{(A) }\text{6}\qquad\textbf{(B) }\text{9}\qquad\textbf{(C) }\text{12}\qquad\textbf{(D) }\text{18}\qquad\textbf{(E) }\text{24}$

## Solution 1 (Coloring)
[asy]import three; draw((1,1,1)--(1,0,1)--(1,0,0)--(0,0,0)--(0,0,1)--(0,1,1)--(1,1,1)--(1,1,0)--(0,1,0)--(0,1,1)); draw((0,0,1)--(1,0,1)); draw((1,0,0)--(1,1,0)); draw((0,0,0)--(0,1,0)); label("2",(0,0,0),S); label("A",(1,0,0),W); label("B",(0,0,1),N); label("1",(1,0,1),NW); label("3",(1,1,0),S); label("C",(0,1,0),E); label("D",(1,1,1),SE); label("4",(0,1,1),NE); [/asy]
We label the vertices of the cube as different letters and numbers shown above. We label these so that Erin can only crawl from a number to a letter or a letter to a number (this can be seen as a coloring argument). The starting point is labeled $A$ .
If we define a "move" as each time Erin crawls along a single edge from one vertex to another, we see that after 7 moves, Erin must be on a numbered vertex. Since this numbered vertex cannot be one unit away from $A$ (since Erin cannot crawl back to $A$ ), this vertex must be $4$ .
Therefore, we now just need to count the number of paths from $A$ to $4$ . To count this, we can work backwards. There are 3 choices for which vertex Erin was at before she moved to $4$ , and 2 choices for which vertex Erin was at 2 moves before $4$ . All of Erin's previous moves were forced, so the total number of legal paths from $A$ to $4$ is $3 \cdot 2 = \boxed{\textbf{(A)}\; 6}$ .

## Solution 2 (Counting and Optimal Strategy)
Position Eric on one vertex of the cube. Then, through optimal strategy, there is 3 ways for Eric to move on his first round, 2 ways for his second, 2 for his third, 2 for his fourth, 2 for his fifth, 1 for his sixth, and 1 for his seventh, giving us a grand total of 48 different paths. However, notice how some of these paths are overcounted by vertex, as positioning Eric on any one of the 8 vertices produces the same 48 cases. Therefore, we divide by the 8 vertices to get the total unique paths, which is $\frac{48}{8} = \boxed{\textbf{(A)}\; 6}$
This is problem 5 but an easier approach.
~Pinotation

## Solution 3 (3D Geometry)
Lets say that this cube is an unit cube and the given corner is $(0,0,0)$ . Because Erin cannot return back to her starting point, she cannot be on $(0,0,1)$ , $(0,1,0)$ , or $(1,0,0)$ . She cannot be on $(1,1,0)$ , $(1,0,1)$ , or $(0,1,1)$ , because after $7$ moves, the sum of all the coordinates has to be odd. Thus, Erin has to be at $(1,1,1)$ . Now, we draw a net and see that there are $3$ choices for the first move, $2$ for the second, and the rest are forced. Thus the answer is $3\cdot2 = \boxed{\textbf{(A)}\; 6}$ .
-Lcz

## Solution 4 (3D Geo & Logic)
Let's suppose the given corner on the cube is $(0,0,0)$ . Erin has 3 identical ways to proceed. Suppose she goes to $(0,1,0)$ . She now has two more identical ways to go. Let's say she goes to $(0,1,1)$ . She has to go to $(0,0,1)$ , otherwise, she will end up on that point after 7 moves. This is because once if she chooses the other path to $(1,1,1)$ , the endpoint is certain to be $(0,0,1)$ , which is directly connected to $(0,0,0)$ . After she goes to $(0,0,1)$ , the only option she has is to go to $(1,0,1)$ , then $(1,0,0)$ , after that $(1,1,0)$ , and finally $(1,1,1)$ . She is forced to go this way because she cannot end up on $(1,0,0)$ . At the start, she had 3 ways to choose, and after that 2 ways to choose, so $3\cdot2=\boxed{\textbf{(A)}\; 6}$ .
~HelloWorld21

## Solution 5 (Insight from 2006 AMC 10A Problem 25)
From the 2006 AMC 10A Problem 25, they look for more or less the same answer except the question asks for the probability that the bug will visit the 7 remaining corners exactly once after 7 moves. From each vertex of the cube, there are 3 edges emanating from it, meaning that there are a total of 3 * the number of ways the bug can visit the 7 vertices exactly once from a fixed point (we have to divide 3, though, because the question asks for the total number of PATHS — each of the 3 vertices emanating from a given vertex offers the same number of distinct paths). Since the answer to the 2006 AMC 10A problem 25 is 18 total ways, then the answer to this question is $18/3=\boxed{\textbf{(A)}\; 6}$ ways.
~Zephyrica
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .