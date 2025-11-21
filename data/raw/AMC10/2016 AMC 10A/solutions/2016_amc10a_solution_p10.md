# 2016 AMC 10A Problem 10

## Problem

A rug is made with three different colors as shown. The areas of the three differently colored regions form an arithmetic progression. The inner rectangle is one foot wide, and each of the two shaded regions is $1$ foot wide on all four sides. What is the length in feet of the inner rectangle?

[asy] size(6cm); defaultpen(fontsize(9pt)); path rectangle(pair X, pair Y){ return X--(X.x,Y.y)--Y--(Y.x,X.y)--cycle; } filldraw(rectangle((0,0),(7,5)),gray(0.5)); filldraw(rectangle((1,1),(6,4)),gray(0.75)); filldraw(rectangle((2,2),(5,3)),white); label("$1$",(0.5,2.5)); draw((0.3,2.5)--(0,2.5),EndArrow(TeXHead)); draw((0.7,2.5)--(1,2.5),EndArrow(TeXHead)); label("$1$",(1.5,2.5)); draw((1.3,2.5)--(1,2.5),EndArrow(TeXHead)); draw((1.7,2.5)--(2,2.5),EndArrow(TeXHead)); label("$1$",(4.5,2.5)); draw((4.5,2.7)--(4.5,3),EndArrow(TeXHead)); draw((4.5,2.3)--(4.5,2),EndArrow(TeXHead)); label("$1$",(4.1,1.5)); draw((4.1,1.7)--(4.1,2),EndArrow(TeXHead)); draw((4.1,1.3)--(4.1,1),EndArrow(TeXHead)); label("$1$",(3.7,0.5)); draw((3.7,0.7)--(3.7,1),EndArrow(TeXHead)); draw((3.7,0.3)--(3.7,0),EndArrow(TeXHead)); [/asy]

$\textbf{(A) } 1 \qquad \textbf{(B) } 2 \qquad \textbf{(C) } 4 \qquad \textbf{(D) } 6 \qquad \textbf{(E) }8$

## Solution
Let the length of the inner rectangle be $x$ .
Then the area of that rectangle is $x\cdot1 = x$ .
The second largest rectangle has dimensions of $x+2$ and $3$ , making its area $3x+6$ . The area of the second shaded area, therefore, is $3x+6-x = 2x+6$ .
The largest rectangle has dimensions of $x+4$ and $5$ , making its area $5x + 20$ . The area of the largest shaded region is the largest rectangle minus the second largest rectangle, which is $(5x+20) - (3x+6) = 2x + 14$ .
The problem states that $x, 2x+6, 2x+14$ is an arithmetic progression, meaning that the terms in the sequence increase by the same amount each term.
Therefore, $(2x+6) - (x) = (2x+14) - (2x+6)\implies x+6 = 8\implies x =2\implies \boxed{\textbf B}$

## Video Solutions
i) https://youtu.be/tyRN1WyasOI (Creative Thinking)
~Education, the Study of Everything
ii) https://youtu.be/XXX4_oBHuGk?t=791
~IceMatrix
iii) https://youtu.be/6lozP3dgr_0
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .