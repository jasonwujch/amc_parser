# 2018 AIME I Problem 14

## Problem

Let $SP_1P_2P_3EP_4P_5$ be a heptagon. A frog starts jumping at vertex $S$ . From any vertex of the heptagon except $E$ , the frog may jump to either of the two adjacent vertices. When it reaches vertex $E$ , the frog stops and stays there. Find the number of distinct sequences of jumps of no more than $12$ jumps that end at $E$ .

## Solution 1
This is easily solved by recursion/dynamic programming. To simplify the problem somewhat, let us imagine the seven vertices on a line $E \leftrightarrow P_4 \leftrightarrow P_5 \leftrightarrow S \leftrightarrow P_1 \leftrightarrow P_2 \leftrightarrow P_3 \leftrightarrow E$ . We can count the number of left/right (L/R) paths of length $\le 11$ that start at $S$ and end at either $P_4$ or $P_3$ .
We can visualize the paths using the common grid counting method by starting at the origin $(0,0)$ , so that a right (R) move corresponds to moving 1 in the positive $x$ direction, and a left (L) move corresponds to moving 1 in the positive $y$ direction. Because we don't want to move more than 2 units left or more than 3 units right, our path must not cross the lines $y = x+2$ or $y = x-3$ . Letting $p(x,y)$ be the number of such paths from $(0,0)$ to $(x,y)$ under these constraints, we have the following base cases:
$p(x,0) = \begin{cases} 1 & x \le 3 \\ 0 & x > 3 \end{cases} \qquad p(0,y) = \begin{cases} 1 & y \le 2 \\ 0 & y > 2 \end{cases}$
and recursive step $p(x,y) = p(x-1,y) + p(x,y-1)$ for $x,y \ge 1$ .
The filled in grid will look something like this, where the lower-left $1$ corresponds to the origin:
$\begin{tabular}{|c|c|c|c|c|c|c|c|} \hline 0 & 0 & 0 & 0 & \textbf{89} & & & \\ \hline 0 & 0 & 0 & \textbf{28} & 89 & & & \\ \hline 0 & 0 & \textbf{9} & 28 & 61 & 108 & 155 & \textbf{155} \\ \hline 0 & \textbf{3} & 9 & 19 & 33 & 47 & \textbf{47} & 0 \\ \hline \textbf{1} & 3 & 6 & 10 & 14 & \textbf{14} & 0 & 0 \\ \hline 1 & 2 & 3 & 4 & \textbf{4} & 0 & 0 & 0 \\ \hline 1 & 1 & 1 & \textbf{1} & 0 & 0 & 0 & 0 \\ \hline \end{tabular}$
The bolded numbers on the top diagonal represent the number of paths from $S$ to $P_4$ in 2, 4, 6, 8, 10 moves, and the numbers on the bottom diagonal represent the number of paths from $S$ to $P_3$ in 3, 5, 7, 9, 11 moves. We don't care about the blank entries or entries above the line $x+y = 11$ . The total number of ways is $1+3+9+28+89+1+4+14+47+155 = \boxed{351}$ .
(Solution by scrabbler94)

## Solution 2
Let $E_n$ denotes the number of sequences with length $n$ that ends at $E$ . Define similarly for the other vertices. We seek for a recursive formula for $E_n$ . \begin{align*} E_n&=P_{3_{n-1}}+P_{4_{n-1}} \\ &=P_{2_{n-2}}+P_{5_{n-2}} \\ &=P_{1_{n-3}}+P_{3_{n-3}}+S_{n-3}+P_{4_{n-3}} \\ &=(P_{3_{n-3}}+P_{4_{n-3}})+S_{n-3}+P_{1_{n-3}} \\ &=E_{n-2}+S_{n-3}+P_{1_{n-3}} \\ &=E_{n-2}+P_{1_{n-4}}+P_{5_{n-4}}+S_{n-4}+P_{2_{n-4}} \\ &=E_{n-2}+(S_{n-4}+P_{1_{n-4}})+P_{5_{n-4}}+P_{2_{n-4}} \\ &=E_{n-2}+(E_{n-1}-E_{n-3})+S_{n-5}+P_{4_{n-5}}+P_{1_{n-5}}+P_{3_{n-5}} \\ &=E_{n-2}+(E_{n-1}-E_{n-3})+(S_{n-5}+P_{1_{n-5}})+(P_{4_{n-5}}+P_{3_{n-5}}) \\ &=E_{n-2}+(E_{n-1}-E_{n-3})+(E_{n-2}-E_{n-4})+E_{n-4} \\ &=E_{n-1}+2E_{n-2}-E_{n-3} \\ \end{align*} Computing a few terms we have $E_0=0$ , $E_1=0$ , $E_2=0$ , $E_3=1$ , and $E_4=1$ .
Using the formula yields $E_5=3$ , $E_6=4$ , $E_7=9$ , $E_8=14$ , $E_9=28$ , $E_{10}=47$ , $E_{11}=89$ , and $E_{12}=155$ .
Finally adding yields $\sum_{k=0}^{12}E_k=\boxed{351}$ .
~ Nafer

## Get solution faster in Sol 2
In the 5th to last line, we have $P_{5_{n-4}}+P_{2_{n-4}}=E_{n-2}$ by shifting the index in line 2.

## Solution 3
For vertices $S, P_1, P_2, P_5,$ the number of ways to get there after $n$ jumps is the sum of the number of ways to get to the adjacent vertices after $n-1$ jumps. For vertices $P_3,$ and $P_4,$ the number of ways to get there after $n$ jumps is he number of ways to get to $P_2$ and $P_5$ after $n-1$ jumps.
$\begin{tabular}{|l|c|c|c|c|c|c|c|} \hline Jump \# & \(S\) & \(P_1\) & \(P_2\) & \(P_3\) & \(E\) & \(P_4\) & \(P_5\) \\ \hline 1 & 0 & 1 & 0 & 0 & \textbf{0} & 0 & 1 \\ \hline 2 & 2 & 0 & 1 & 0 & \textbf{0} & 1 & 0 \\ \hline 3 & 0 & 3 & 0 & 1 & \textbf{1} & 0 & 3 \\ \hline 4 & 6 & 0 & 4 & 0 & \textbf{1} & 3 & 0 \\ \hline 5 & 0 & 10 & 0 & 4 & \textbf{3} & 0 & 9 \\ \hline 6 & 19 & 0 & 14 & 0 & \textbf{4} & 9 & 0 \\ \hline 7 & 0 & 33 & 0 & 14 & \textbf{9} & 0 & 28 \\ \hline 8 & 61 & 0 & 47 & 0 & \textbf{14} & 28 & 0 \\ \hline 9 & 0 & 108 & 0 & 47 & \textbf{28} & 0 & 89 \\ \hline 10 & 197 & 0 & 155 & 0 & \textbf{47} & 89 & 0 \\ \hline 11 & 0 & 352 & 0 & 155 & \textbf{89} & 0 & 286 \\ \hline 12 & 638 & 0 & 507 & 0 & \textbf{155} & 286 & 0 \\ \hline \end{tabular}$
$0+0+1+1+3+4+9+14+28+47+89+155=\boxed{351}.$

## Video Solution
https://www.youtube.com/watch?v=uWNExJc3hok
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .