# 2018 AMC 8 Problem 23

## Problem

From a regular octagon, a triangle is formed by connecting three randomly chosen vertices of the octagon. What is the probability that at least one of the sides of the triangle is also a side of the octagon?

[asy] size(3cm); pair A[]; for (int i=0; i<9; ++i) { A[i] = rotate(22.5+45*i)*(1,0); } filldraw(A[0]--A[1]--A[2]--A[3]--A[4]--A[5]--A[6]--A[7]--cycle,gray,black); for (int i=0; i<8; ++i) { dot(A[i]); } [/asy]

$\textbf{(A) } \frac{2}{7} \qquad \textbf{(B) } \frac{5}{42} \qquad \textbf{(C) } \frac{11}{14} \qquad \textbf{(D) } \frac{5}{7} \qquad \textbf{(E) } \frac{6}{7}$

## Solutions

## Solution 1
Choose side "lengths" $a,b,c$ for the triangle, where "length" is how many vertices of the octagon are skipped between vertices of the triangle, starting from the shortest side, and going clockwise, and choosing $a=b$ if the triangle is isosceles: $a+b+c=5$ , where either [ $a\leq b$ and $a < c$ ] or [ $a=b=c$ (but this is impossible in an octagon)].
Options are: $a=0$ with $b,c$ in { 0,5 ; 1,4 ; 2,3 ; 3,2 ; 4,1 }, and $a=1$ with { 1,3 ; 2,2}. $\frac{5}{7}$ of these have a side with length 1, which corresponds to an edge of the octagon. So, our answer is $\boxed{\textbf{(D) } \frac 57}$

## Solution 2
We will use constructive counting to solve this. There are $2$ cases: Either all $3$ points are adjacent, or exactly $2$ points are adjacent.
If all $3$ points are adjacent, then we have $8$ choices. If we have exactly $2$ adjacent points, then we will have $8$ places to put the adjacent points and $4$ places to put the remaining point, so we have $8\cdot4$ choices. The total amount of choices is ${8 \choose 3} = 8\cdot7$ .
Thus, our answer is $\frac{8+8\cdot4}{8\cdot7}= \frac{1+4}{7}=\boxed{\textbf{(D) } \frac 57}$ .

## Solution 3
We can decide $2$ adjacent points with $8$ choices. The remaining point will have $6$ choices. However, we have counted the case with $3$ adjacent points twice, so we need to subtract this case once. The case with the $3$ adjacent points has $8$ arrangements, so our answer is
$\frac{8\cdot6-8}{{8 \choose 3 }}$ $=\frac{8\cdot6-8}{8 \cdot 7 \cdot 6 \div 6}\Longrightarrow\boxed{\textbf{(D) } \frac 57}$ .

## Solution 4 (Stars and Bars)
Let $1$ point of the triangle be fixed at the top. Then, there are ${7 \choose 2} = 21$ ways to choose the other $2$ points. There must be $3$ spaces in the points and $3$ points themselves. This leaves $2$ extra points to be placed anywhere. By stars and bars, there are $3$ triangle points ( $n$ ) and $2$ extra points ( $k-1$ ) distributed so by the stars and bars formula, ${n+k-1 \choose k-1}$ , there are ${4 \choose 2} = 6$ ways to arrange the bars and stars. Thus, the probability is $\frac{(21 - 6)}{21} = \boxed{\textbf{(D) } \frac 57}$ .

## Solution 5 (Casework)
We select a vertex of the octagon; this will be the first vertex of our triangle. Define the $distance$ of a vertex from another to be the minimum number of edges that one must travel on to get from one vertex to the other. There are three distinct cases; the second vertex is a distance of 1 away from the selected vertex (i.e. they are adjacent), the second vertex is a distance of 2 away from the selected vertex, or the second vertex is a distance of 3 or more away from the selected vertex. We consider each of these cases separately.
Case 1: The first two chosen vertices are adjacent.
There is a $\frac{2}{7}$ chance of selecting a point that is adjacent to the one we have chosen. In this case, any choice of the third vertex will result in a triangle that shares at least one side with the given octagon. Thus, this case has a $\frac{2}{7}$ case of giving us a triangle that fulfills the conditions given in the problem.
Case 2: There is a distance of 2 between the first two chosen vertices.
There is a $\frac{2}{7}$ chance of selecting a vertex that is a distance of 2 away from the first vertex. In this case, there are three vertices that will create a triangle that satisfies the condition in the problem (the one that is adjacent to both of the first two selected vertices and the two that are adjacent to only one of the first two selected vertices). There is a $\frac{1}{2}$ chance of selecting one of these three vertices from the remaining six. Thus, this case has a $\frac{2}{7} \cdot \frac{1}{2} = \frac{1}{7}$ chance of giving us a triangle that fulfills the conditions given in the problem.
Case 3: There is a distance of 3 or more between the first two chosen vertices.
There is a $\frac{3}{7}$ chance of selecting a vertex that is a distance of 3 or more away from the first vertex. In this case, there are four vertices (the two adjacent to each of the first two vertices) that may be chosen to satisfy the problem's condition. There is a $\frac{2}{3}$ chance of selecting one of these four vertices from the remaining six. Thus, this case has a $\frac{3}{7} \cdot \frac{2}{3} = \frac{2}{7}$ chance of giving us a triangle that fulfills the conditions given in the problem.
Summing the probabilities from each of the individual cases, we find that there is a $\frac{1}{7} + \frac{2}{7} + \frac{2}{7} = \boxed{\textbf{(D) } \frac 57}$ chance of acquiring a triangle which shares at least one side with the octagon.
~cxsmi

## Solution 6
We begin by finding the total number of triangles that can be formed from the 8 vertices of a regular octagon. This is simply \[\binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56.\] So there are 56 possible triangles.
We want the probability that a randomly chosen triangle has at least one side that is also a side of the octagon.
### Method 1: Count triangles that share at least one side with the octagon
We consider two cases:
Case 1: The triangle shares two sides with the octagon. This happens when the triangle is formed by three consecutive vertices of the octagon. There are 8 such sets of consecutive vertices, so there are 8 such triangles.
Case 2: The triangle shares exactly one side with the octagon. Each side of the octagon can be used in such a triangle. For a fixed side (say $AB$ ), the third vertex must not be adjacent to either $A$ or $B$ (to avoid forming a triangle with two octagon sides). There are 4 such choices for the third vertex, giving 4 triangles per side. With 8 sides, the total is \[8 \times 4 = 32\] triangles in this case.
Adding both cases, the number of triangles that share at least one side with the octagon is \[8 + 32 = 40.\]
Thus, the desired probability is \[\frac{40}{56} = \boxed{\text{(D) } \frac{5}{7}}.\]
### Method 2: Count triangles that share no side with the octagon
Instead of counting the desired cases directly, we count the number of triangles that do not share any side with the octagon.
Label the vertices of the octagon as $A, B, C, D, E, F, G, H$ in order. Consider triangle $\triangle ADF$ . This triangle does not include any side of the octagon, since $AD$ , $DF$ , and $FA$ are all chords that skip at least one vertex.
In general, a triangle with no side on the octagon must consist of three non-consecutive vertices, with none of the triangle’s sides being edges of the polygon.
By examining all such configurations, we find there are 16 triangles with no sides on the octagon (this count can be verified through casework or geometric symmetry).
Therefore, the number of triangles that do share at least one side with the octagon is \[56 - 16 = 40,\] and the desired probability is again \[\frac{40}{56} = \boxed{\text{(D) } \frac{5}{7}}.\]
### Recommendation for Competitions
Method 1 is more straightforward to explain and typically easier to compute quickly, especially with a diagram. Method 2 is a bit more abstract but can be faster if you recognize the complementary counting strategy. Both approaches lead to the same answer.
~ aoum

## Solution 7
Firstly, we calculate the amount of all possible triangles. It is $C_8^3=56$ . Then, we consider how many triangles have at least a edge which is also the edge of octagon.
If the triangle shares only one edge with the octagon, fix an edge, we can choose $4$ different vertices for the triangle. Thus, there are $8\times 4=32$ possible triangles. If the triangle shares its two edges with the octagon, obviously, there are only $8$ possible triangles. $\frac{32+8}{56}=\boxed{\textbf{(D)}\frac{5}{7}}$ .

## Solution 8
We split into two cases:
Case 1: Exactly one side is chosen. There are 4 lines that each contain 1 side of the octagon, and there are 8 points on the octagon. Thus, the total number of such lines is: \begin{align} 8 \cdot 4 &= 32. \end{align}
Case 2: Exactly two sides are chosen. The number of ways to choose 2 points on the octagon is: \begin{align} \binom{8}{1} &= 8. \end{align}
Adding the results from both cases, the total is: \begin{align} 32 + 8 &= \boxed{40}. \end{align}
This is the numerator. To find the denominator we do $C_8^3=56$ . Thus, our final answer is ${40/56= \boxed{\textbf{(D)}\frac{5}{7}}}$ .
-jb2015007
-FrankensteinQuixoteCabin

## Video Solution by OmegaLearn
https://youtu.be/5UojVH4Cqqs?t=2678
~ pi_is_3.14

## Video Solutions
https://www.youtube.com/watch?v=VNflxl7VpL0
https://youtu.be/YeYDixFXsvA
~savannahsolver
### See Also