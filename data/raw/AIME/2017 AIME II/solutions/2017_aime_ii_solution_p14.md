# 2017 AIME II Problem 14

## Problem

A $10\times10\times10$ grid of points consists of all points in space of the form $(i,j,k)$ , where $i$ , $j$ , and $k$ are integers between $1$ and $10$ , inclusive. Find the number of different lines that contain exactly $8$ of these points.

## Solution 1
$Case \textrm{ } 1:$ The lines are not parallel to the faces
A line through the point $(a,b,c)$ must contain $(a \pm 1, b \pm 1, c \pm 1)$ on it as well, as otherwise, the line would not pass through more than 5 points. This corresponds to the 4 diagonals of the cube.
We look at the one from $(1,1,1)$ to $(10,10,10)$ . The lower endpoint of the desired lines must contain both a 1 and a 3, so it can be $(1,1,3), (1,2,3), (1,3,3)$ . If $\textrm{min} > 0$ then the point $(a-1,b-1,c-1)$ will also be on the line for example, 3 applies to the other end.
Accounting for permutations, there are $12$ ways, so there are $12 \cdot 4 = 48$ different lines for this case.
$Case \textrm{ } 2:$ The lines where the $x$ , $y$ , or $z$ is the same for all the points on the line.
WLOG, let the $x$ value stay the same throughout. Let the line be parallel to the diagonal from $(1,1,1)$ to $(1,10,10)$ . For the line to have 8 points, the $y$ and $z$ must be 1 and 3 in either order, and the $x$ value can be any value from 1 to 10. In addition, this line can be parallel to 6 face diagonals. So we get $2 \cdot 10 \cdot 6 = 120$ possible lines for this case.
The answer is, therefore, $120 + 48 = \boxed{168}$
Solution by stephcurry added to the wiki by Thedoge edited by Rapurt9 and phoenixfire

## Solution 2
Look at one pair of opposite faces of the cube. There are $4$ lines say $l_1, l_2, l_3, l_4$ with exactly $8$ collinear points on the top face. For each of these lines, draw a rectangular plane that consists of one of the $l_i$ for $1 \leq i \leq 4$ and perpendicular to the top face.
There are $16$ lines in total on this plane. $10$ of which are parallel to one of the edges of the rectangular plane and $6$ of which are diagonals. There are $3$ pairs of opposite faces. So $3 \cdot 4 \cdot 16=192$ lines.
But we are overcounting the lines of the diagonals of those rectangular planes twice. There are $4$ rectangular planes perpendicular to one pair of opposite faces. Thus $4 \cdot 6=24$ lines are overcounted.
So the answer is $192-24=\boxed{168}$ .
Solution by phoenixfire

## Solution 3
Considered the cases $(1, 2, ..., 8), (2, 3, ...,9), (3, 4, ..., 10)$ and reverse. Also, consider the constant subsequences of length 8 $(1, 1, ..., 1), (2, 2, ..., 2), ..., (10, 10, ..., 10)$ . Of all the triplets that work they cannot be extended to form another point on the line in the $10 \times 10 \times 10$ grid but we need to divide by 2 because reversing all the subsequences gives the same line. Thus the answer is \[\frac{16^3 - 14^3 - 14^3 + 12^3}{2} = \boxed{168}\]

## Solution 4
The lines can be defined as starting from $(a, b, c)$ with "slope" (vector) $(d, e, f)$ . We impose the condition that at least one of $a - d, b - e, \textrm{ or } c - f$ is outside the range of $[1, 10]$ in order to ensure that $(a, b, c)$ is the first valid point on this line. Then, the line ranges from $(a, b, c), (a + d, b + e, c + f), \ldots, (a + 7d, b + 7e, c + 7f)$ , where $1 \le a + 7d, b + 7e, c + 7f \le 10$ , in which case at least one of $a + 8d, b + 8e, \textrm{ or } c + 8f$ is outside of the range $[1, 10]$ to ensure the line does not contain more than 8 points. For $1 \le a + 7d, b + 7e, c + 7f \le 10$ to be satisfied, the pairs $(a, d), (b, e), \textrm{ and } (c, f)$ can only be $(1, 0), (2, 0), \ldots (10, 0), (1, 1), (2, 1), (3, 1), (10, -1), (9, -1), \textrm{ and } (8, -1)$ . Notice that there are only two pairs such that $a + 8d, b + 8e, \textrm{ or } c + 8f \not \in [1, 10]$ , namely $(3, 1)$ and $(8, -1)$ . Thus, our line must contain at least one of these two pairs. In addition, only the two pairs $(1, 1)$ and $(10, -1)$ satisfy $a - d, b - e, \textrm{ or } c - f \not \in [1, 10]$ . Thus, we must also include at least one of these two pairs as well. Let us call these 4 pairs "important" pairs. Finally, we can include any valid pair for our third pair.
Case 1: We repeat one of the important pairs
There are 2 ways to choose from $(3, 1)$ and $(8, -1)$ , and 2 ways to choose from $(1, 1)$ and $(10, -1)$ . Then, there are 2 ways to choose the repeated pair. Next, we can arrange these pairs $3!/2! = 3$ ways. So, we have $2 \cdot 2 \cdot 2 \cdot 3 = 24.$
Case 2: We use 3 distinct important pairs
There are ${4 \choose 3}$ ways to choose the pairs (note that by pigeonhole principle, this guarantees we get at least one of each required pair). Then, there are $3! = 6$ ways to arrange it. We obtain $4 \cdot 6 = 24$ .
Case 3: We use 3 unique pairs, one that is not important.
Again, there are $2 \cdot 2 = 4$ ways to choose the important pairs. Then, there are 12 ways to choose the non-important pair. Again, there are $3! = 6$ ways to arrange it. So, we get $4 \cdot 12 \cdot 6 = 288$ .
Summing all of it up and dividing by two (since we over counted each line and its reversal), we get $\frac{24 + 24 + 288}{2} = \boxed{168}.$
~ CrazyVideoGamez

## Video Solution
https://youtu.be/wgaJMSo61_o
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .