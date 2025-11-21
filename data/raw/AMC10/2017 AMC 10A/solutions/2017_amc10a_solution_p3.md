# 2017 AMC 10A Problem 3

## Problem

Tamara has three rows of two $6$ -feet by $2$ -feet flower beds in her garden. The beds are separated and also surrounded by $1$ -foot-wide walkways, as shown on the diagram. What is the total area of the walkways, in square feet?

[asy] draw((0,0)--(0,10)--(15,10)--(15,0)--cycle); fill((0,0)--(0,10)--(15,10)--(15,0)--cycle, lightgray); draw((1,1)--(1,3)--(7,3)--(7,1)--cycle); fill((1,1)--(1,3)--(7,3)--(7,1)--cycle, white); draw((1,4)--(1,6)--(7,6)--(7,4)--cycle); fill((1,4)--(1,6)--(7,6)--(7,4)--cycle, white); draw((1,7)--(1,9)--(7,9)--(7,7)--cycle); fill((1,7)--(1,9)--(7,9)--(7,7)--cycle, white); draw((8,1)--(8,3)--(14,3)--(14,1)--cycle); fill((8,1)--(8,3)--(14,3)--(14,1)--cycle, white); draw((8,4)--(8,6)--(14,6)--(14,4)--cycle); fill((8,4)--(8,6)--(14,6)--(14,4)--cycle, white); draw((8,7)--(8,9)--(14,9)--(14,7)--cycle); fill((8,7)--(8,9)--(14,9)--(14,7)--cycle, white); defaultpen(fontsize(8, lineskip=1)); label("2", (1.2, 2)); label("6", (4, 1.2)); defaultpen(linewidth(.2)); draw((0,8)--(1,8), arrow=Arrows); draw((7,8)--(8,8), arrow=Arrows); draw((14,8)--(15,8), arrow=Arrows); draw((11,0)--(11,1), arrow=Arrows); draw((11,3)--(11,4), arrow=Arrows); draw((11,6)--(11,7), arrow=Arrows); label("1", (.5,7.8)); label("1", (7.5,7.8)); label("1", (14.5,7.8)); label("1", (10.8,.5)); label("1", (10.8,3.5)); label("1", (10.8,6.5)); [/asy]

$\textbf{(A)}\ 72\qquad\textbf{(B)}\ 78\qquad\textbf{(C)}\ 90\qquad\textbf{(D)}\ 120\qquad\textbf{(E)}\ 150$

## Solution 1
Finding the area of the shaded walkway can be achieved by computing the total area of Tamara's garden and then subtracting the combined area of her six flower beds.
Since the width of Tamara's garden contains three margins, the total width is $2\cdot 6+3\cdot 1 = 15$ feet.
Similarly, the height of Tamara's garden is $3\cdot 2+4\cdot 1 = 10$ feet.
Therefore, the total area of the garden is $15\cdot 10 =150$ square feet.
Finally, since the six flower beds each have an area of $2\cdot 6 = 12$ square feet, the area we seek is $150 - 6\cdot 12$ , and our answer is $\boxed{\textbf{(B)}\ 78}$

## Solution 2 (probably much less efficient than solution 1)
The long horizontal walkways have an area of $15 ft^{2}$ each, and there are $4$ of them $\longrightarrow 60 ft^{2}$ .
The short vertical walkways have an area of $2 ft^{2}$ each, and there are $9$ of them $\longrightarrow 18 ft^{2}$ .
Adding the areas together, we have $60 ft^{2} + 18 ft^{2} = 78 ft^{2} \Longrightarrow \boxed{\textbf{(B)}\ 78}$ . ~JH. L

## Video Solution
https://youtu.be/str7kmcRMY8
https://youtu.be/B7UuRDIfXkQ
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .