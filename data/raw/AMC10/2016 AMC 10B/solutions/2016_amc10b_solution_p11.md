# 2016 AMC 10B Problem 11

## Problem

Carl decided to fence in his rectangular garden. He bought $20$ fence posts, placed one on each of the four corners, and spaced out the rest evenly along the edges of the garden, leaving exactly $4$ yards between neighboring posts. The longer side of his garden, including the corners, has twice as many posts as the shorter side, including the corners. What is the area, in square yards, of Carl’s garden?

$\textbf{(A)}\ 256\qquad\textbf{(B)}\ 336\qquad\textbf{(C)}\ 384\qquad\textbf{(D)}\ 448\qquad\textbf{(E)}\ 512$

## Solution 1
If the dimensions are $4a\times 4b$ , then one side will have $a+1$ posts (including corners) and the other $b+1$ (including corners).
The total number of posts is $2(a+b)=20$ .
This diagram represents the number of posts around the garden. [asy]size(7cm);fill((0,0)--(5,0)--(5,7)--(0,7)--cycle,lightgreen); for(int i=0;i<5;++i)dot((i,0),red);for(int i=0;i<7;++i)dot((5,i),blue);dot((5,7)); draw(arc((0,0),.5,-90,-270)--arc((4,0),.5,90,-90)--cycle,gray+dotted); draw(arc((5,0),.5,-180,0)--arc((5,6),.5,0,180)--cycle,gray+dotted); draw((0,-1)--(5,-1),Arrows);draw((6,0)--(6,7),Arrows); label("$a+1$",(0,-1)--(5,-1),S);label("$b+1$",(6,0)--(6,7),E); label("$a$",(1,1));label("$b$",(4,5)); [/asy]
We solve the system $\begin{cases}b+1=2(a+1)\\a+b=10\end{cases}$ to get $a=3,\ b=7$ . Then the area is $4a\cdot 4b=336$ which is $\boxed{\textbf{(B) } 336}$ .
~Edits by BakedPotato66

## Solution 2
To do this problem, we have to draw a rectangle. We also have to keep track of the fence posts. Putting a post on each corner leaves us with only $16$ posts. Now there are twice as many posts on the longer side then the shorter side. From this, we can see that we can put $8$ posts on the longer side and $4$ posts on the shorter side. On the shorter side, we have $3$ spaces between the $4$ posts. On the longer side, we have $7$ spaces between the $8$ fence posts. There are $4$ yards between each post. Therefore, the answer is $12\times28=\boxed{\textbf{(B)}\ 336}$ .

## Video Solution
https://youtu.be/yVAQ-bt7s-U
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .