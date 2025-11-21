# 2020 AIME II Problem 12

## Problem

Let $m$ and $n$ be odd integers greater than $1.$ An $m\times n$ rectangle is made up of unit squares where the squares in the top row are numbered left to right with the integers $1$ through $n$ , those in the second row are numbered left to right with the integers $n + 1$ through $2n$ , and so on. Square $200$ is in the top row, and square $2000$ is in the bottom row. Find the number of ordered pairs $(m,n)$ of odd integers greater than $1$ with the property that, in the $m\times n$ rectangle, the line through the centers of squares $200$ and $2000$ intersects the interior of square $1099$ .

## Solution 1
Let us take some cases. Since $m$ and $n$ are odds, and $200$ is in the top row and $2000$ in the bottom, $m$ has to be $3$ , $5$ , $7$ , or $9$ . Also, taking a look at the diagram, the slope of the line connecting those centers has to have an absolute value of $< 1$ . Therefore, $m < 1800 \mod n < 1800-m$ .
If $m=3$ , $n$ can range from $667$ to $999$ . However, $900$ divides $1800$ , so looking at mods, we can easily eliminate $899$ and $901$ . Now, counting these odd integers, we get $167 - 2 = 165$ .
Similarly, let $m=5$ . Then $n$ can range from $401$ to $499$ . However, $450|1800$ , so one can remove $449$ and $451$ . Counting odd integers, we get $50 - 2 = 48$ .
Take $m=7$ . Then, $n$ can range from $287$ to $333$ . However, $300|1800$ , so one can verify and eliminate $299$ and $301$ . Counting odd integers, we get $24 - 2 = 22$ .
Let $m = 9$ . Then $n$ can vary from $223$ to $249$ . However, $225|1800$ . Checking that value and the values around it, we can eliminate $225$ . Counting odd integers, we get $14 - 1 = 13$ .
Add all of our cases to get \[165+48+22+13 = \boxed{248}\]
-Solution by thanosaops

## Solution 2 (Official MAA)
Because square $2000$ is in the bottom row, it follows that $\frac{2000}m \le n < \frac{2000}{m-1}$ . Moreover, because square $200$ is in the top row, and square $2000$ is not in the top row, $1 < m \le 10$ . In particular, because the number of rows in the rectangle must be odd, $m$ must be one of $3, 5, 7,$ or $9.$
For each possible choice of $m$ and $n$ , let $\ell_{m,n}$ denote the line through the centers of squares $200$ and $2000.$ Note that for odd values of $m$ , the line $\ell_{m,n}$ passes through the center of square $1100.$ Thus $\ell_{m,n}$ intersects the interior of cell $1099$ exactly when its slope is strictly between $-1$ and $1$ . The line $\ell_{m,n}$ is vertical whenever square $2000$ is the $200$ th square in the bottom row of the rectangle. This would happen for $m = 3, 5, 7, 9$ when $n = 900, 450, 300, 225$ , respectively. When $n$ is 1 greater than or 1 less than these numbers, the slope of $\ell_{m,n}$ is $1$ or $-1$ , respectively. In all other cases the slope is strictly between $-1$ and $1.$ The admissible values for $n$ for each possible value of $m$ are given in the following table. \[\begin{tabular}{|c|c|c|c|c|}\hline m & minimum n & maximum n & avoided n & number of odd n\\\hline 3&667&999&899, 900, 901&165\\\hline 5&400&499&449, 450, 451&48\\\hline 7&286&333&299, 300, 301&22\\\hline 9&223&249&224, 225, 226&13\\\hline \end{tabular}\] This accounts for $165 + 48 + 22 + 13 = 248$ rectangles.

## Video Solution 1
https://www.youtube.com/watch?v=MrtKoO16XLQ ~ MathEx

## Video Solution 2
https://youtu.be/v58SLOoAKTw

## Video Solution 3
https://youtu.be/pu_79SSh3mM
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .