# 2015 AMC 10A Problem 3

## Problem

Ann made a $3$ -step staircase using $18$ toothpicks as shown in the figure. How many toothpicks does she need to add to complete a $5$ -step staircase?

$\textbf{(A)}\ 9\qquad\textbf{(B)}\ 18\qquad\textbf{(C)}\ 20\qquad\textbf{(D)}\ 22\qquad\textbf{(E)}\ 24$

[asy] size(150); defaultpen(linewidth(0.8)); path h = ellipse((0.5,0),0.45,0.015), v = ellipse((0,0.5),0.015,0.45); for(int i=0;i<=2;i=i+1) { for(int j=0;j<=3-i;j=j+1) { filldraw(shift((i,j))*h,black); filldraw(shift((j,i))*v,black); } }[/asy]

## Solution
We can see that a $1$ -step staircase requires $4$ toothpicks and a $2$ -step staircase requires $10$ toothpicks. Thus, to go from a $1$ -step to $2$ -step staircase, $6$ additional toothpicks are needed and to go from a $2$ -step to $3$ -step staircase, $8$ additional toothpicks are needed. Applying this pattern, to go from a $3$ -step to $4$ -step staircase, $10$ additional toothpicks are needed and to go from a $4$ -step to $5$ -step staircase, $12$ additional toothpicks are needed. Our answer is $10+12=\boxed{\textbf{(D)}\ 22}$

## Solution 2
Alternatively, we can see with the $3$ -step staircase has $2[2(3)+2+1]=18$ toothpicks. Generalizing, we see that a staircase with $x$ steps has $2[2x+(x-1)+(x-2)+...+1]$ toothpicks. So, for $x=5$ steps, we have $2[2(5)+4+3+2+1]=40$ toothpicks. So our answer is $40-18=22$ or $D$ .

## Solution 3
If one is too lazy to derive a formula for the number of picks needed for a given number of steps, one can simply see that to get to $4$ steps, we add two blobs that have three picks each (the top and the right), and two more blobs that have two blocks each to form the steps. This adds $2\cdot3+2\cdot2=10$ picks. Then, to get to $5$ steps, we add two more edge blobs with $3$ picks each and $3$ more blobs that have two picks each. We add $2\cdot3+3\cdot2=12$ more for a total increase of $10+12=\boxed{\textbf{(D)}~22}.$
~Technodoggo

## Video Solution (CREATIVE THINKING)
~Education, the Study of Everything

## Video Solution
https://youtu.be/9BinymGHcUI
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .