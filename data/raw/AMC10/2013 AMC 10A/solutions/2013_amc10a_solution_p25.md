# 2013 AMC 10A Problem 25

## Problem

All $20$ diagonals are drawn in a regular octagon. At how many distinct points in the interior of the octagon (not on the boundary) do two or more diagonals intersect?

$\textbf{(A)}\ 49\qquad\textbf{(B)}\ 65\qquad\textbf{(C)}\ 70\qquad\textbf{(D)}\ 96\qquad\textbf{(E)}\ 128$

## Solution 1 (Drawing)
If you draw a clear diagram like the one below, it is easy to see that there are $\boxed{\textbf{(A) }49}$ points.
[asy] size(14cm); pathpen = brown + 1.337; // Initialize octagon pair[] A; for (int i=0; i<8; ++i) { A[i] = dir(45*i); } D(CR( (0,0), 1)); // Draw diagonals // choose pen colors pen[] colors; colors[1] = orange + 1.337; colors[2] = purple; colors[3] = green; colors[4] = black; for (int d=1; d<=4; ++d) { pathpen = colors[d]; for (int j=0; j<8; ++j) { D(A[j]--A[(j+d) % 8]); } } pathpen = blue + 2; // Draw all the intersections pointpen = red + 7; for (int x1=0; x1<8; ++x1) { for (int x2=x1+1; x2<8; ++x2) { for (int x3=x2+1; x3<8; ++x3) { for (int x4=x3+1; x4<8; ++x4) { D(IP(A[x1]--A[x2], A[x3]--A[x4])); D(IP(A[x1]--A[x3], A[x4]--A[x2])); D(IP(A[x1]--A[x4], A[x2]--A[x3])); } } } }[/asy]

## Solution 2 (Working Backwards)
Let the number of intersections be $x$ . We know that $x\le \dbinom{8}{4} = 70$ , as every $4$ vertices on the octagon forms a quadrilateral with intersecting diagonals which is an intersection point. However, four diagonals intersect in the center, so we need to subtract $\dbinom{4}{2} -1 = 5$ from this count, $70-5 = 65$ . Note that diagonals like $\overline{AD}$ , $\overline{CG}$ , and $\overline{BE}$ all intersect at the same point. There are $8$ of this type with three diagonals intersecting at the same point, so we need to subtract $2$ of the $\dbinom{3}{2}$ (one is kept as the actual intersection). In the end, we obtain $65 - 16 = \boxed{\textbf{(A) }49}$ .

## Solution 3 (Answer choices and reasoning)
We know that the amount of intersection points is at most $\dbinom{8}{4} = 70$ , as in solution $2$ . There's probably going to be more than $5$ intersections counted multiple times (to get $\textbf{(B) }65$ ), leading us to the only reasonable answer, $\boxed{\textbf{(A) }49}$ . -Lcz
Note: You can easily prove this by looking at the simple case of the diagonals intersecting in the middle of the octagon. $4$ major diagonals intersect here and only $1$ intersection point is counted so you can subtract $3$ from $70$ . Then look to the middle area of the octagon. In this area, if we label the major diagonal as the one where there are $3$ points between the two points forming the diagonal, and the semi-minor diagonal the diagonal where there is one less point between the two diagonal forming points, there are $8$ intersection points of a major diagonal and $2$ semi-minor diagonals. This means that these eight points would be, not double-counted -which the calculation by Lcz accounts for- but triple-counted. Thus, taking away one for each of these points is more than enough to see the value of the answer has to be less than or equal to $59$ . Choice A is the only answer that works.

## Solution 4 (Drawing but easier)
Like solution one, we may draw. Except note that the octagon has eight regions, and each region has an equal number of points, so drawing only one of the eight regions and the intersection points suffices. One of the eight regions contains $8$ points (not including the octagon center). However each adjacent region share one side in common and that side contains $2$ intersection points, so in actuality there are $8 - 2 = 6$ points per region. We multiply this by $8$ to get $6\cdot 8 = 48$ and add the one center point to get $48 + 1 = \boxed{\textbf{(A) }49}$ .
~skyscraper

## Solution 5 (Case Work with Drawing)
[asy] size(8cm); pathpen = black; // draw the circle pair[] A; for (int i=0; i<8; ++i) { A[i] = dir(45*i); } D(CR((0,0), 1)); // draw the octagon and diagonals // choose pen colors pen[] colors; colors[1] = yellow; colors[2] = purple; colors[3] = green; colors[4] = orange; for (int d=1; d<=4; ++d) { pathpen = colors[d]; for (int j=0; j<8; ++j) { D(A[j]--A[(j+d) % 8]); } } // draw the 3 or more line intersections pointpen = red + 5; D(IP(A[0]--A[4], A[2]--A[6])); // center of the circle for (int x1=0; x1<8; ++x1) { for (int x2=0; x2<8; ++x2) { int y1 = (x1 + 4)%8; int y2 = (x2 + 3)%8; if (x1 != x2 && y1 != y2 && x1 != y1 && x1 != y2 && x2 != y1 && x2 != y2) D(IP(A[x1]--A[y1], A[x2]--A[y2])); } } // draw the 2 line intersections pointpen = blue + 4; for (int x1 = 0; x1 < 8; ++x1) { int x2 = (x1 + 1)%8; D(IP(A[x1]--A[(x1+2)%8], A[x2]--A[(x2+2)%8])); D(IP(A[x1]--A[(x1+2)%8], A[x2]--A[(x2+3)%8])); D(IP(A[x1]--A[(x1+2)%8], A[x2]--A[(x2+4)%8])); D(IP(A[x1]--A[(x1+2)%8], A[x2]--A[(x2+5)%8])); D(IP(A[x1]--A[(x1+3)%8], A[x2]--A[(x2+5)%8])); } [/asy]
This problem is a counting problem of combinatoric geometry. There are 2 cases for the above diagram:
Case 1: Red Dots
The red dots are the intersection of 3 or more lines. It consists of 8 dots that make up an octagon and 1 dot in the center. Hence, there are $9$ red dots.
Case 2: Blue Dots
The blue dots are the intersection of 2 lines. Each vertex of the octagon has 2 purple lines, 2 green lines, and 1 orange line coming out of it. There are 5 dots of intersection on a purple line, 6 dots on a green line, and 5 dots on an orange line. There are $2 \cdot 5+2 \cdot 6+5=27$ dots that come out of 1 vertex, which includes 7 red dots already counted. So there are $27-7 = 20$ blue dots coming out of 1 vertex. There are 8 vertices, but each blue dot is the intersection of 2 lines, corresponding to $2 \cdot 2 = 4$ vertices. So there are $\frac{20 \cdot 8}{4} = 40$ blue dots.
The number of intersection dots are the sum of the number of red and blue dots. Hence, the answer is $40 + 9 = \boxed{\textbf{(A) }49}$ .
~ isabelchen

## Solution 6 (PIE)
Notice that there can be a maximum of 4 lines intersecting at any point inside the octagon. Now, let $P_2$ be the number of points where at least $2$ lines intersect, and define $P_3$ and $P_4$ similarly. By PIE, we have that the desired number of points is \[P_2 - 2P_3 + 3P_4\] We now separately count the $P_i's$ .
Case 1 (P_2): Notice that if we pick any $4$ points, there is exactly $1$ way $2$ lines can be drawn such that they intersect inside the convex hull of the $4$ points. Thus, $P_2 = {8 \choose 4} = 70$ .
Case 2 (P_3): The only ways that $3$ diagonals concur is if they are all the longest (main) diagonals in the octagon, or one of them is a main diagonal and the other $2$ intersect on said diagonal. If they are all the main diagonals, there are $4$ ways. If only one of them is a main diagonal, then there are $4(2) = 8$ ways. In total, there are $8 + 4 = 12$ such points.
Case 3 (P_4): The only way this can happen is if all $4$ diagonals intersect in the center (they are all main diagonals), giving $1$ way.
Thus, in total we have \[70 - 2(12) + 3 = \boxed{\textbf{(A)} 49}\] such points.
~mathwiz_1207

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2013amc10a/359

## Video Solution by OmegaLearn (Animated Visual Proof)
https://youtu.be/kw-fcOomE-Q
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .