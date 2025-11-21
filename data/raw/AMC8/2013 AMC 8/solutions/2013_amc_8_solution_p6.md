# 2013 AMC 8 Problem 6

## Problem

The number in each box below is the product of the numbers in the two boxes that touch it in the row above. For example, $30 = 6\times5$ . What is the missing number in the top row?

[asy] unitsize(0.8cm); draw((-1,0)--(1,0)--(1,-2)--(-1,-2)--cycle); draw((-2,0)--(0,0)--(0,2)--(-2,2)--cycle); draw((0,0)--(2,0)--(2,2)--(0,2)--cycle); draw((-3,2)--(-1,2)--(-1,4)--(-3,4)--cycle); draw((-1,2)--(1,2)--(1,4)--(-1,4)--cycle); draw((1,2)--(1,4)--(3,4)--(3,2)--cycle); label("600",(0,-1)); label("30",(-1,1)); label("6",(-2,3)); label("5",(0,3)); [/asy]

$\textbf{(A)}\ 2 \qquad \textbf{(B)}\ 3 \qquad \textbf{(C)}\ 4 \qquad \textbf{(D)}\ 5 \qquad \textbf{(E)}\ 6$

## Solution 1 (Working Backwards)
Let the value in the empty box in the middle row be $x$ , and the value in the empty box in the top row be $y$ . $y$ is the answer we're looking for.
[asy] unitsize(0.8cm); draw((-1,0)--(1,0)--(1,-2)--(-1,-2)--cycle); draw((-2,0)--(0,0)--(0,2)--(-2,2)--cycle); draw((0,0)--(2,0)--(2,2)--(0,2)--cycle); draw((-3,2)--(-1,2)--(-1,4)--(-3,4)--cycle); draw((-1,2)--(1,2)--(1,4)--(-1,4)--cycle); draw((1,2)--(1,4)--(3,4)--(3,2)--cycle); label("600",(0,-1)); label("30",(-1,1)); label("6",(-2,3)); label("5",(0,3)); label("$x$",(1,1)); label("$y$",(2,3)); [/asy]
From the diagram, $600 = 30x$ , making $x = 20$ .
[asy] unitsize(0.8cm); draw((-1,0)--(1,0)--(1,-2)--(-1,-2)--cycle); draw((-2,0)--(0,0)--(0,2)--(-2,2)--cycle); draw((0,0)--(2,0)--(2,2)--(0,2)--cycle); draw((-3,2)--(-1,2)--(-1,4)--(-3,4)--cycle); draw((-1,2)--(1,2)--(1,4)--(-1,4)--cycle); draw((1,2)--(1,4)--(3,4)--(3,2)--cycle); label("600",(0,-1)); label("30",(-1,1)); label("6",(-2,3)); label("5",(0,3)); label("20",(1,1)); label("$y$",(2,3)); [/asy]
It follows that $20 = 5y$ , so $y = \boxed{\textbf{(C)}\ 4}$ .

## Solution 2 (Jumping to the Start)
Another way to do this problem is to realize what makes up the bottommost number. This method doesn't work quite as well for this problem, but in a larger tree, it might be faster. Again, let the value in the empty box in the middle row be $x$ , and the value in the empty box in the top row be $y$ . $y$ is the answer we're looking for.
[asy] unitsize(0.8cm); draw((-1,0)--(1,0)--(1,-2)--(-1,-2)--cycle); draw((-2,0)--(0,0)--(0,2)--(-2,2)--cycle); draw((0,0)--(2,0)--(2,2)--(0,2)--cycle); draw((-3,2)--(-1,2)--(-1,4)--(-3,4)--cycle); draw((-1,2)--(1,2)--(1,4)--(-1,4)--cycle); draw((1,2)--(1,4)--(3,4)--(3,2)--cycle); label("600",(0,-1)); label("30",(-1,1)); label("6",(-2,3)); label("5",(0,3)); label("$x$",(1,1)); label("$y$",(2,3)); [/asy]
We can write some equations:
$600 = 30x\\ 30 = 6\cdot 5\\ x = 5y$
Now we can substitute into the first equation using the two others:
$600 = (6\cdot5)(5y)\\ 600= 6\cdot5\cdot5\cdot y\\ 600=6\cdot25\cdot y\\ 600 = 150y\\ \boxed{\textbf{(C)}\ 4} = y$

## Video Solution
https://youtu.be/4tSvBcnv6dA ~savannahsolver
### See Also