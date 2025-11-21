# 2025 AMC 8 Problem 12

## Problem

The region shown below consists of 24 squares, each with side length 1 centimeter. What is the area, in square centimeters, of the largest circle that can fit inside the region, possibly touching the boundaries?

[asy] size(100); void drawSquare(pair p) { draw(box(p, p + (1,1)), black); } int[][] grid = { {0, 0, 0, 0, 0, 0}, {0, 0, 1, 1, 0, 0}, {0, 1, 1, 1, 1, 0}, {1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 0}, {0, 0, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0} }; int rows = grid.length; int cols = grid[0].length; for (int i = 0; i < rows; ++i) { for (int j = 0; j < cols; ++j) { if (grid[i][j] == 1) { drawSquare((j, rows - i - 1)); } } } [/asy]

$\textbf{(A)}\ 3\pi\qquad \textbf{(B)}\ 4\pi\qquad \textbf{(C)}\ 5\pi\qquad \textbf{(D)}\ 6\pi\qquad \textbf{(E)}\ 8\pi$

## Solution 1
The largest circle that can fit inside the figure has its center in the middle of the figure and will be tangent to the figure in $8$ points. By the Pythagorean Theorem, the distance from the center to one of these $8$ points is $\sqrt{2^2 + 1^2} = \sqrt5$ , so the area of this circle is $\pi \sqrt{5}^2 = \boxed{\textbf{(C)} 5\pi}$ .
~Soupboy0

## Solution 2
Draw the circle in the grid and analyze the radius. It's radius is a little more than 2 but a lot less than 2.5, so the area is a little more than 4π. So, the area of the circle is $\boxed{\textbf{(C)} 5\pi}$ with a radius of approximately 2.23. -- leafy

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=Oe8Ka0kEZiLNXA5g&t=1096 ~hsnacademy

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI

## Video Solution 2 by Thinking Feet
https://youtu.be/PKMpTS6b988
### See Also