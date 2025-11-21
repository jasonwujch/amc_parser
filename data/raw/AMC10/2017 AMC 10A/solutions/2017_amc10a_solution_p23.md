# 2017 AMC 10A Problem 23

## Problem

How many triangles with positive area have all their vertices at points $(i,j)$ in the coordinate plane, where $i$ and $j$ are integers between $1$ and $5$ , inclusive?

$\textbf{(A)}\ 2128 \qquad\textbf{(B)}\ 2148 \qquad\textbf{(C)}\ 2160 \qquad\textbf{(D)}\ 2200 \qquad\textbf{(E)}\ 2300$

## Solution 1
We can solve this by finding all the combinations, then subtracting the ones that are on the same line. There are $25$ points in all, from $(1,1)$ to $(5,5)$ , so $\dbinom{25}3$ is $\frac{25\cdot 24\cdot 23}{3\cdot 2 \cdot 1}$ , which simplifies to $2300$ . Now we count the ones that are on the same line. We see that any three points chosen from $(1,1)$ and $(1,5)$ would be on the same line, so $\dbinom53$ is $10$ , and there are $5$ rows, $5$ columns, and $2$ long diagonals, so that results in $120$ . We can also count the ones with $4$ on a diagonal. That is $\dbinom43$ , which is 4, and there are $4$ of those diagonals, so that results in $16$ . We can count the ones with only $3$ on a diagonal, and there are $4$ diagonals like that, so that results in $4$ . We can also count the ones with a slope of $\frac12$ , $2$ , $-\frac12$ , or $-2$ , with $3$ points in each. Note that there are $3$ such lines, for each slope, present in the grid. In total, this results in $12$ . Finally, we subtract all the ones in a line from $2300$ , so we have $2300-120-16-4-12=\boxed{(\textbf{B})\ 2148}$

## Solution 2
There are $5 \times 5 = 25$ total points in all. So, there are $\dbinom{25}3 = 2300$ ways to choose the three vertices for the triangle. However, there are some cases where they 3 points chosen results in a straight line.
There are $10 \times 10 = 100$ cases where the 3 points chosen make up a vertical or horizontal line.
There are $2\left(1+\dbinom{4}3+\dbinom{5}3+\dbinom{4}3+1\right)=40$ cases where the 3 points all land on the diagonals of the square.
There are $3 \times 4=12$ ways where the 3 points make the a slope of $\frac{1}{2}$ , $-\frac{1}{2}$ , $2$ , and $-2$ .
Hence, there are $100+40+12=152$ cases where the chosen 3 points make a line. The answer would be $2300-152=\boxed{(\textbf{B})\ 2148}$
~MrThinker

## Video Solution by Pi Academy
https://youtu.be/7XAw78CZ3fY?si=HxmOK65niihjrpmq
~ Pi Academy

## Video Solutions
Video Solutions:
https://www.youtube.com/watch?v=wfWsolGGfNY
https://www.youtube.com/watch?v=LCvDL-SMknI
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .