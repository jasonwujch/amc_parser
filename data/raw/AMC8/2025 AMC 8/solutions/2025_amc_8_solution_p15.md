# 2025 AMC 8 Problem 15

## Problem

Kei draws a $6$ -by- $6$ grid. He colors $13$ of the unit squares silver and the remaining squares gold. Kei then folds the grid in half vertically, forming pairs of overlapping unit squares. Let $m$ and $M$ equal the least and greatest possible number of gold-on-gold pairs, respectively. What is the value of $m+M$ ?

[asy] import graph; size(100); pen gridPen = black; void drawSquare(pair p) { draw(box(p, p + (1,1)), gridPen); } int[][] grid = { {1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1}, }; int rows = grid.length; int cols = grid[0].length; for (int i = 0; i < rows; ++i) { for (int j = 0; j < cols; ++j) { if (grid[i][j] == 1) { drawSquare((j, rows - i - 1)); } } } [/asy]

$\textbf{(A)}\ 12\qquad \textbf{(B)}\ 14\qquad \textbf{(C)}\ 16\qquad \textbf{(D)}\ 18 \qquad \textbf{(E)}\ 20$

## Solution 1
First, we note that there are $18$ "pairs" of squares folded on top of each other after the folding. The minimum number of gold pairs occurs when silver squares occupy the maximum number of pairs, and the maximum number of gold pairs occurs when silver squares occupy the minimum number of pairs. The former case occurs when all $13$ silver squares are placed in different pairs, resulting in $18-13=5$ gold pairs. The latter case occurs when the silver squares are paired up as much as possible, resulting in $6$ complete pairs and another square occupying another pair slot. Then there are $18-7=11$ gold pairs. Our answer is $11+5=\boxed{\textbf{(C) }16}$ . ~cxsmi

## Solution 2
We can see that the least number of gold-on-gold pairs will be obtained when the $13$ silver squares are placed on the two sides so that they don't overlap when folded over (because then it will minimize the number of gold-on-golds). We can see that if we split them up $6$ and $7$ on both sides, and then fold it, the number of gold-on-golds will be $18-13 = 5$ .
The maximum number of gold-on-golds will be achieved when the silver squares overlap when folded over, which will increase the number of gold-on-golds. If we align 6 silver squares with each other on each side, and put the last one somewhere else, we get the maximum is $18 - 7 = 11$ . Therefore, the answer is $11+5=\boxed{\textbf{(C)}~16}$ .
~Sigmacuber

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI You can contact him through his Youtube Channel

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=WhpkSTD3UJpbQ3KC&t=1572 ~hsnacademy

## Video Solution by Thinking Feet
https://youtu.be/PKMpTS6b988
### See Also