# 2020 AMC 8 Problem 21

## Problem

A game board consists of $64$ squares that alternate in color between black and white. The figure below shows square $P$ in the bottom row and square $Q$ in the top row. A marker is placed at $P.$ A step consists of moving the marker onto one of the adjoining white squares in the row above. How many $7$ -step paths are there from $P$ to $Q?$ (The figure shows a sample path.)

[asy]//diagram by SirCalcsALot size(200); int[] x = {6, 5, 4, 5, 6, 5, 6}; int[] y = {1, 2, 3, 4, 5, 6, 7}; int N = 7; for (int i = 0; i < 8; ++i) { for (int j = 0; j < 8; ++j) { draw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--(i,j)); if ((i+j) % 2 == 0) { filldraw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--(i,j)--cycle,black); } } } for (int i = 0; i < N; ++i) { draw(circle((x[i],y[i])+(0.5,0.5),0.35)); } label("$P$", (5.5, 0.5)); label("$Q$", (6.5, 7.5)); [/asy]

$\textbf{(A) }28 \qquad \textbf{(B) }30 \qquad \textbf{(C) }32 \qquad \textbf{(D) }33 \qquad \textbf{(E) }35$

## Solution 1
Notice that, to step onto any particular white square, the marker must have come from one of the $1$ or $2$ white squares immediately beneath it (since the marker can only move on white squares). This means that the number of ways to move from $P$ to that square is the sum of the number of ways to move from $P$ to each of the white squares immediately beneath it (also called the Waterfall Method). To solve the problem, we can accordingly construct the following diagram, where each number in a square is calculated as the sum of the numbers on the white squares immediately beneath that square (and thus will represent the number of ways to remove from $P$ to that square, as already stated).
[asy] int N = 7; for (int i = 0; i < 8; ++i) { for (int j = 0; j < 8; ++j) { draw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--(i,j)); if ((i+j) % 2 == 0) { filldraw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--(i,j)--cycle,black); } } } label("$1$", (5.5, .5)); label("$1$", (4.5, 1.5)); label("$1$", (6.5, 1.5)); label("$1$", (3.5, 2.5)); label("$1$", (7.5, 2.5)); label("$2$", (5.5, 2.5)); label("$1$", (2.5, 3.5)); label("$3$", (6.5, 3.5)); label("$3$", (4.5, 3.5)); label("$4$", (3.5, 4.5)); label("$3$", (7.5, 4.5)); label("$6$", (5.5, 4.5)); label("$10$", (4.5, 5.5)); label("$9$", (6.5, 5.5)); label("$19$", (5.5, 6.5)); label("$9$", (7.5, 6.5)); label("$28$", (6.5, 7.5)); [/asy]
The answer is therefore $\boxed{\textbf{(A) }28}$ .
Note: This is a classic example of a problem involving Pascal's triangle .
~ edited by Dream9, WrenMath and algebraic_algorithmic

## Solution 2
Suppose we "extend" the chessboard infinitely with $2$ additional columns to the right, as shown below. The red line shows the right-hand edge of the original board.
[asy] int N = 7; for (int i = 0; i < 10; ++i) { for (int j = 0; j < 8; ++j) { draw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--(i,j)); if ((i+j) % 2 == 0) { filldraw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--(i,j)--cycle,black); } } } draw((8,0) -- (8,8),red); label("$P$", (5.5,.5)); label("$Q$", (6.5,7.5)); label("$X$", (8.5,3.5)); label("$Y$", (8.5,5.5)); [/asy]
The total number of paths from $P$ to $Q$ , including invalid paths which cross over the red line, is then the number of paths which make $4$ steps up-and-right and $3$ steps up-and-left, which is $\binom{4+3}{3} = \binom{7}{3} = 35$ . We need to subtract the number of invalid paths, i.e. the number of paths that pass through $X$ or $Y$ . To get to $X$ , the marker has to make $3$ up-and-right steps, after which it can proceed to $Q$ with $3$ steps up-and-left and $1$ step up-and-right. Thus, the number of paths from $P$ to $Q$ that pass through $X$ is $1 \cdot \binom{3+1}{3} = 4$ . Similarly, the number of paths that pass through $Y$ is $\binom{4+1}{1}\cdot 1 = 5$ . However, we have now double-counted the invalid paths which pass through both $X$ and $Y$ ; from the diagram, it is clear that there are only $2$ of these (as the marker can get from $X$ to $Y$ by a step up-and-left and a step-up-and-right in either order). Hence the number of invalid paths is $4+5-2=7$ , and the number of valid paths from $P$ to $Q$ is $35-7 = \boxed{\textbf{(A) }28}$ .

## Solution 3
On any white square, we may choose to go left or right, as long as we do not cross over the border of the board. Call the moves $L$ and $R$ respectively. Every single legal path consists of $4$ $R's$ and $3$ $L's$ , so now all we have to find is the number of ways to order $4 R's$ and $3 L's$ in any way, which is ${7 \choose 3}=35$ . However, we originally promised that we will not go over the border, and now we have to subtract the paths that do go over the border. The paths that go over the border are any paths that start with RRR(1 path), RR(5 paths) and LRRR(1 path) so our final number of paths is $35-7=\boxed{(A)=28}.$ ~PEKKA

## Solution 4: Intuitive Approach
We label the rows starting from the bottom. At row 1, there is $1$ way: at P. We draw all the possible ways to get to Q. There are two ways to choose for row 2, and another two ways to choose for row 3. However, you can go to the "edge" or the farthest possible square westward of Q, so you can't multiply by 2 again. Notice how, at the first step, we figured that the answer was even, so choice D and E are eliminated, and after the second row, we realized it must be a multiple of 4, so choice B is eliminated. When we get to the fourth row, we do not multiply by 2 again, since we have limited possibilities rather than multiplying by 2 again. Choice C implies that there are two possibilities per row; however, we know that if you go to the farthest possible, you only have one possibility, so it is not $2^5 = 32$ so we know that the answer is choice $\boxed{\textbf{(A)}}$ . ~hh99754539

## Solution 5
![](https://wiki-images.artofproblemsolving.com//e/eb/2020amc821solution5.png)
Say our first move is to point 1. Our path from 1 to Q must have 4 upward-right moves and 2 upward-left moves, so there are $\frac{6!}{4! \cdot 2!} = 15$ paths. From 2 to Q, our path must have 3 upward-right moves and 3 upward-left moves, so there are $\frac{6!}{3! \cdot 3!} = 20$ paths. However, our path can't go off the grid. There are 4 invalid paths from point 2 to Q (all paths starting with right right) and 3 invalid paths from point 1 to Q (all paths starting with right right right). So the answer is $20 + 15 - (4 + 3) = \boxed{\textbf{(A)} 28}$ .
~ grogg007

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=X5JGwbGqL4dqK6t0&t=4098
~Math-X

## Video Solution (🚀 Just 2 min 🚀)
https://youtu.be/AIicVBwvio0
~ Education, the Study of Everything

## Video Solution
https://youtu.be/QGXcFOqeeAQ
Please like and subscribe!

## Video Solution by OmegaLearn
https://youtu.be/CNgHB-bsqFk?t=1441
~ pi_is_3.14

## Video Solution by MathisCool
https://www.youtube.com/watch?v=LvpCYn8Ze6c

## Video Solution by North America Math Contest Go Go Go
https://www.youtube.com/watch?v=rWxhlItMAN0
~North America Math Contest Go Go Go

## Video Solution by WhyMath
https://youtu.be/YR3oghbziBA
~savannahsolver

## Video Solutions
https://youtu.be/hGCxt8G9g-s

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=1247
~Interstigation

## Video Solution by STEMbreezy
https://youtu.be/wq8EUCe5oQU
~STEMbreezy