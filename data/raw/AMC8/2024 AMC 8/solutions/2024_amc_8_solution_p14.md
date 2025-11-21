# 2024 AMC 8 Problem 14

## Problem

The one-way routes connecting towns $A,M,C,X,Y,$ and $Z$ are shown in the figure below(not drawn to scale).The distances in kilometers along each route are marked. Traveling along these routes, what is the shortest distance from A to Z in kilometers?

[asy] /* AMC8 P14 2024, by NUMANA: BUI VAN HIEU */ import graph; unitsize(2cm); real r=0.25; // Define the nodes and their positions pair[] nodes = { (0,0), (2,0), (1,1), (3,1), (4,0), (6,0) }; string[] labels = { "A", "M", "X", "Y", "C", "Z" }; // Draw the nodes as circles with labels for(int i = 0; i < nodes.length; ++i) { draw(circle(nodes[i], r)); label("$" + labels[i] + "$", nodes[i]); } // Define the edges with their node indices and labels int[][] edges = { {0, 1}, {0, 2}, {2, 1}, {2, 3}, {1, 3}, {1, 4}, {3, 4}, {4, 5}, {3, 5} }; string[] edgeLabels = { "8", "5", "2", "10", "6", "14", "5", "10", "17" }; pair[] edgeLabelsPos = { S, SE, SW, S, SE, S, SW, S, NE}; // Draw the edges with labels for (int i = 0; i < edges.length; ++i) { pair start = nodes[edges[i][0]]; pair end = nodes[edges[i][1]]; draw(start + r*dir(end-start) -- end-r*dir(end-start), Arrow); label("$" + edgeLabels[i] + "$", midpoint(start -- end), edgeLabelsPos[i]); } // Draw the curved edge with label draw(nodes[1]+r * dir(-45)..controls (3, -0.75) and (5, -0.75)..nodes[5]+r * dir(-135), Arrow); label("$25$", midpoint(nodes[1]..controls (3, -0.75) and (5, -0.75)..nodes[5]), 2S); [/asy]

$\textbf{(A)}\ 28 \qquad \textbf{(B)}\ 29 \qquad \textbf{(C)}\ 30 \qquad \textbf{(D)}\ 31 \qquad \textbf{(E)}\ 32$

### Note / Warning

As tempting as it may seem, these diagrams are not drawn to scale. What may visually look like the shortest distance may not be the shortest in terms of the distance shown. I know it may be obvious after some time, but many people are at first lured to path $A \rightarrow M \rightarrow C \rightarrow Z$ just because visually it looks like the shortest distance. This could potentially lead to the incorrect answer $\textbf{(E)}\ 32$ .

~s.khunti

## Solution 1
We can simply see that path $A \rightarrow X \rightarrow M \rightarrow Y \rightarrow C \rightarrow Z$ will give us the smallest value. Adding, $5+2+6+5+10 = \boxed{28}$ . This is nice as it’s also the smallest value, solidifying our answer.
You can also simply brute-force it or sort of think ahead - for example, getting from A to M can be done $2$ ways; $A \rightarrow X \rightarrow M$ ( $5+2$ ) or $A \rightarrow M (8)$ , so you should take the shorter route ( $5+2$ ). Another example is M to C, two ways - one is $6+5$ and the other is $14$ . Take the shorter route. After this, you need to consider a few more times - consider if $5+10$ ( $Y \rightarrow C \rightarrow Z$ ) is greater than $17 (Y \rightarrow Z$ ), which it is not, and consider if $25 (M \rightarrow Z$ ) is greater than $14+10$ ( $M \rightarrow C \rightarrow Z$ ) or $6+5+10$ ( $M \rightarrow Y \rightarrow C \rightarrow Z$ ) which it is not. TLDR: $5+2+6+5+10 = \boxed{28}$ . [Note: This is probably just the thinking behind the solution.] {Double-note: As MaxyMoosy said, since this answer is the smallest one, it has to be the right answer.}
~MaxyMoosy ~HACKER2022

## Solution 2 (Advanced)
We can execute Dijkstra's algorithm by hand to find the shortest path from $A$ to every other town, including $Z$ . This effectively proves that, assuming we execute the algorithm correctly, that we will have found the shortest distance. The distance estimates for each step of the algorithm (from $A$ to each node) are shown below:
\[\begin{array}{|c|c|c|c|c|c|c|} \hline \text{Current node} & A & M & C & X & Y & Z \\ \hline A & 0 & 8 & \infty & 5 & \infty & \infty \\ X & 0 & 7 & \infty & 5 & 15 & \infty \\ M & 0 & 7 & 21 & 5 & 13 & 32 \\ Y & 0 & 7 & 18 & 5 & 13 & 30 \\ C & 0 & 7 & 18 & 5 & 13 & 28 \\ Z & 0 & 7 & 18 & 5 & 13 & \textbf{28} \\ \hline \end{array}\] The steps are as follows: starting with the initial node $A$ , set $d(A)=0$ and $d(v)=\infty$ for all $v \in \{M,C,X,Y,Z\}$ where $d(v)$ indicates the distance from $A$ to $v$ . Consider the outgoing edges $(A,X)$ and $(A,M)$ and update the distance estimates $d(X)=5$ and $d(M)=8$ , completing the first row of the table.
The node $X$ is the unvisited node with the lowest distance estimate, so we will consider $X$ and its outgoing edges $(X,Y)$ and $(X,M)$ . The distance estimate $d(Y)$ equals $d(X)+10=15$ , and the distance estimate $d(M)$ updates to $d(X)+2=7$ , because $7 < 8$ . This completes the second row of the table. Repeating this process for each unvisited node (in order of its distance estimate) yields the correct distance $d(Z) = \boxed{\textbf{(A) } 28}$ once the algorithm is complete.
~scrabbler94

## Solution 3 (Variant of Solution 1)
From $A$ , we want to find the shortest route to $Z$ , so we want to try to find the shortest path through each node (not necessarily all of them). We should follow the arrows, since all of them lead to $Z$ . From $A$ , there are $2$ paths we can take, to $M$ $(8)$ , or to $X$ $(5)$ . We travel to $X$ , since $5 < 8$ . From $X$ , we go to $M$ $(2 < 10)$ , we go to $Y$ $6 < 14 < 25$ , we go to $C$ , $(5 < 17)$ and finally go to $Z$ . Adding up gives $5 + 2 + 6 + 5 + 10 = 28 = \boxed{\textbf{(A)}}$ .
~SpeedCuber7

## Solution 4 (On paper)
We can cross off a few routes:
Finally, we are left with a single path AXMYCZ from A to Z which adding it up gives $28 = \boxed{\textbf{(A)}}.$
### Video by MathTalks😉
https://youtu.be/qAwRUj2N46c?si=QDUY8ZUVFP29Eg4c

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/cNh9BBB5AIo
~mr_mathman

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=y_YVZFC4DQdB2qhM&t=3280
~Math-X

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=2XXS3hZobif8ohhH&t=1553 ~hsnacademy

## Video Solution 1 (easy to digest) by Power Solve
https://youtu.be/2AVrraozwF8

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=RRTxlduaDs8

## Video Solution 3 by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=V-xN8Njd_Lc
~NiuniuMaths

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=bAxLRYT6SCw

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=1405

## Video Solution by Dr. David
https://youtu.be/NFYvG_K59rQ

## Video Solution by WhyMath
https://youtu.be/s-i00y3W5i4

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/qJqrFauo3lQ
~Thesmartgreekmathdude
### See Also