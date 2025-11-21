# 2022 AIME II Problem 9

## Problem

Let $\ell_A$ and $\ell_B$ be two distinct parallel lines. For positive integers $m$ and $n$ , distinct points $A_1, A_2, \allowbreak A_3, \allowbreak \ldots, \allowbreak A_m$ lie on $\ell_A$ , and distinct points $B_1, B_2, B_3, \ldots, B_n$ lie on $\ell_B$ . Additionally, when segments $\overline{A_iB_j}$ are drawn for all $i=1,2,3,\ldots, m$ and $j=1,\allowbreak 2,\allowbreak 3, \ldots, \allowbreak n$ , no point strictly between $\ell_A$ and $\ell_B$ lies on more than 2 of the segments. Find the number of bounded regions into which this figure divides the plane when $m=7$ and $n=5$ . The figure shows that there are 8 regions when $m=3$ and $n=2$ . [asy] import geometry; size(10cm); draw((-2,0)--(13,0)); draw((0,4)--(10,4)); label("$\ell_A$",(-2,0),W); label("$\ell_B$",(0,4),W); point A1=(0,0),A2=(5,0),A3=(11,0),B1=(2,4),B2=(8,4),I1=extension(B1,A2,A1,B2),I2=extension(B1,A3,A1,B2),I3=extension(B1,A3,A2,B2); draw(B1--A1--B2); draw(B1--A2--B2); draw(B1--A3--B2); label("$A_1$",A1,S); label("$A_2$",A2,S); label("$A_3$",A3,S); label("$B_1$",B1,N); label("$B_2$",B2,N); label("1",centroid(A1,B1,I1)); label("2",centroid(B1,I1,I3)); label("3",centroid(B1,B2,I3)); label("4",centroid(A1,A2,I1)); label("5",(A2+I1+I2+I3)/4); label("6",centroid(B2,I2,I3)); label("7",centroid(A2,A3,I2)); label("8",centroid(A3,B2,I2)); dot(A1); dot(A2); dot(A3); dot(B1); dot(B2); [/asy]

## Solution 1
We can use recursion to solve this problem:
1. Fix 7 points on $\ell_A$ , then put one point $B_1$ on $\ell_B$ . Now, introduce a function $f(x)$ that indicates the number of regions created, where x is the number of points on $\ell_B$ . For example, $f(1) = 6$ because there are 6 regions.
2. Now, put the second point $B_2$ on $\ell_B$ . Join $A_1~A_7$ and $B_2$ will create $7$ new regions (and we are not going to count them again), and split the existing regions. Let's focus on the spliting process: line segment formed between $B_2$ and $A_1$ intersect lines $\overline{B_1A_2}$ , $\overline{B_1A_3}$ , ..., $\overline{B_1A_7}$ at $6$ points $\Longrightarrow$ creating $6$ regions (we already count one region at first), then $5$ points $\Longrightarrow$ creating $5$ regions (we already count one region at first), 4 points, etc. So, we have: \[f(2) = f(1) + 7 + (6+5+...+1) = 34.\]
3. If you still need one step to understand this: $A_1~A_7$ and $B_3$ will still create $7$ new regions. Intersecting \[\overline{A_2B_1}, \overline{A_2B_2};\] \[\overline{A_3B_1}, \overline{A_3B_2};\] \[...\] \[\overline{A_7B_1}, \overline{A_7B_2}\] at $12$ points, creating $12$ regions, etc. Thus, we have: \[f(3) = f(2)+7+(12+10+8+...+2)=34+7+6\cdot 7=83.\]
Yes, you might already notice that: \[f(n+1) = f(n)+7+(6+5+...+1)\cdot n = f(n) + 7 + 21n.\]
5. Finally, we have $f(4) = 153$ , and $f(5)=244$ . Therefore, the answer is $\boxed{244}$ .
Note: we could deduce a general formula of this recursion: $f(n+1)=f(n)+N_a+\frac{n\cdot (N_a) \cdot (N_a-1)}{2}$ , where $N_a$ is the number of points on $\ell_A$

## Solution 2
We want to derive a general function $f(m,n)$ that indicates the number of bounded regions. Observing symmetry, we know this is a symmetric function about $m$ and $n$ . Now let's focus on $f(m+1, n)-f(m, n)$ , which is the difference caused by adding one point to the existing $m$ points of line $\ell_A$ . This new point, call it #m, when connected to point #1 on $\ell_B$ , crosses $m*(n-1)$ lines, thus making additional $m*(n-1)+1$ bounded regions; when connected to point #2 on $\ell_B$ , it crosses $m*(n-2)$ lines, thus making additional $m*(n-2)+1$ bounded regions; etc. By simple algebra/recursion methods, we see
$f(m+1, n)-f(m, n)=m*\frac{n(n-1)}{2} +n$
Notice $f(1,n)=n-1$ . Not very difficult to figure out:
$f(m, n)=\frac{m(m-1)n(n-1)}{4} +mn-1$
The fact that $f(3,2)=8$ makes us more confident about the formula. Now plug in $m=5, n=7$ , we get the final answer of $\boxed{244}$ .

## Solution 3
Let some number of segments be constructed. We construct a new segment. We start from the straight line $l_B.$ WLOG from point $B_3.$ Segment will cross several existing segments (points $A,B,C,...$ ) and enter one of the points of the line $l_A (A_1).$
Each of these points adds exactly 1 new bounded region (yellow bounded regions).
The exception is the only first segment $(A_1 B_1),$ which does not create any bounded region. Thus, the number of bounded regions is $1$ less than the number of points of intersection of the segments plus the number of points of arrival of the segments to $l_A.$
Each point of intersection of two segments is determined uniquely by the choice of pairs of points on each line.
The number of such pairs is $\dbinom{n}{2} \cdot \dbinom{m}{2}.$
Exactly one segment comes to each of the $n$ points of the line $l_A$ from each of the $m$ points of the line $l_B.$ The total number of arrivals is equal to $mn.$ Hence, the total number of bounded regions is $N = \dbinom{n}{2} \cdot \dbinom{m}{2} + mn – 1.$
We plug in $m=5, n=7$ , we get the final answer of $\boxed{244}$ .
vladimir.shelomovskii@gmail.com, vvsss

## Solution 4 (Recursion and Complementary Counting)
When a new point is added to a line, the number of newly bounded regions it creates with each line segment will be one more than the number of intersection points the line makes with other lines.
Case 1: If a new point $P$ is added to the right on a line when both lines have an equal amount of points.
WLOG, let the point be on line $\ell_A$ . We consider the complement, where new lines don't intersect other line segments. Simply observing, we see that the only line segments that don't intersect with the new lines are lines attached to some point that a new line does not pass through. If we look at a series of points on line $\ell_B$ from left to right and a line connects $P$ to an arbitrary point, then the lines formed with that point and with remaining points on the left of that point never intersect with the line with $P$ . Let there be $s$ points on lines $\ell_A$ and $\ell_B$ before $P$ was added. For each of the $s$ points on $\ell_B$ , we subtract the total number of lines formed, which is $s^2$ , not counting $P$ . Considering all possible points on $\ell_B$ , we get $(s^2-s)+(s^2-2s)\cdots(s^2-s^2)$ total intersections. However, for each of the lines, there is one more bounded region than number of intersections, so we add $s$ . Simplifying, we get $s^3-s\sum_{i=1}^{s}{i}+s\Longrightarrow s(s^2-\sum_{i=1}^{s}{i}+1)$ . Note that this is only a recursion formula to find the number of new regions added for a new point $P$ added to $\ell_A$ .
Case 2: If a new point $P$ is added to the right of a line that has one less point than the other line.
Continuing on case one, let this point $P$ be on line $\ell_B$ . With similar reasoning, we see that the idea remains the same, except $s+1$ lines are formed with $P$ instead of just $s$ lines. Once again, each line from $P$ to a point on line $\ell_A$ creates $s$ non-intersecting lines for that point and each point to its left. Subtracting from $s(s+1)$ lines and considering all possible lines created by $P$ , we get $(s(s+1)-s)+(s(s+1)-2s)\cdots(s(s+1)-s(s+1)$ intersections. However, the number of newly bounded regions is the number of intersections plus the number of points on line $\ell_A$ . Simplying, we get $s(s+1)^2-s\sum_{i=1}^{s+1}{i}+(s+1)$ newly bounded regions.
For the base case $s=2$ for both lines, there are $4$ bounded regions. Next, we plug in $s=2,3,4$ for both formulas and plug $s=5$ for the first formula to find the number of regions when $m=6$ and $n=5$ . Notice that adding a final point on $\ell_A$ is a variation of our Case 1. The only difference is for each of the $s$ lines formed by $P$ , there are $s+1$ points that can form a non-intersecting line. Therefore, we are subtracting a factor of $s+1$ lines instead of $s$ lines from a total of $s(s+1)$ lines. However, the number of lines formed by $P$ remains the same so we still add $s$ at the end when considering intersection points. Thus, the recursive equation becomes $(s(s+1)-(s+1))+(s(s+1)-2(s+1))\cdots(s(s+1)-s(s+1))+s\Longrightarrow s^2(s+1)-(s+1)\sum_{i=1}^{s}{i}+s$ . Plugging $s=5$ into this formula and adding the values we obtained from the other formulas, the final answer is $4+4+9+12+22+28+45+55+65=\boxed{244}$ .
~ Magnetoninja

## Solution 5 (Euler's Graph Formula, similar to solution 3)
We know the by Euler's Formula for planar graphs that $F-E+V=2$ , where $F$ is the number of bounded faces, plus the outer region, $E$ is the number of edges, and $V$ is the number of vertices. Temporarily disregarding the intersections between the lines, we can easily calculate that:
$V_{i}=7+5=12$
$E_{i}=6+4+7\cdot5=45$
However, the resulting graph is not planar, as the edges clearly intersect. To account for this, we must turn all intersection points into vertices, and update our values accordingly.
Observe that each intersection point can be mapped to two points on either line, and analogously, two points on either line can be mapped to one intersection point, uniquely. Thus, to count intersection points, we simply calculate:
${7 \choose 2}{5 \choose 2} = 210$
And thus,
$V=V_{i}+210=222$
We must also account for the edges. Observe that each intersection point turns the two edges that make it into four, that is, each intersection point adds $2$ to the number of edges. Therefore,
$E=E_{i}+2\cdot210=465$
Plugging these into Euler's Formula we get: $F-E+V=2$
$F-465+222=2$
$F=245$
Disregarding the outer region, we conclude that our answer is $F-1=245-1=\boxed {244}$
~ Shadowleafy

## Video Solution
https://youtu.be/OWNHkKlEo2A
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .