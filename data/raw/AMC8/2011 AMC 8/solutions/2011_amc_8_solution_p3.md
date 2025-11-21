# 2011 AMC 8 Problem 3

## Problem

Extend the square pattern of 8 black and 17 white square tiles by attaching a border of black tiles around the square. What is the ratio of black tiles to white tiles in the extended pattern? [asy] filldraw((0,0)--(5,0)--(5,5)--(0,5)--cycle,white,black); filldraw((1,1)--(4,1)--(4,4)--(1,4)--cycle,mediumgray,black); filldraw((2,2)--(3,2)--(3,3)--(2,3)--cycle,white,black); draw((4,0)--(4,5)); draw((3,0)--(3,5)); draw((2,0)--(2,5)); draw((1,0)--(1,5)); draw((0,4)--(5,4)); draw((0,3)--(5,3)); draw((0,2)--(5,2)); draw((0,1)--(5,1)); [/asy]

$\textbf{(A) }8:17 \qquad\textbf{(B) }25:49 \qquad\textbf{(C) }36:25 \qquad\textbf{(D) }32:17 \qquad\textbf{(E) }36:17$

## Solution 1
One way of approaching this is drawing the next circle of boxes around the current square. [asy] filldraw((-1,-1)--(6,-1)--(6,6)--(-1,6)--cycle,mediumgray,black); filldraw((0,0)--(5,0)--(5,5)--(0,5)--cycle,white,black); filldraw((1,1)--(4,1)--(4,4)--(1,4)--cycle,mediumgray,black); filldraw((2,2)--(3,2)--(3,3)--(2,3)--cycle,white,black); draw((4,-1)--(4,6)); draw((3,-1)--(3,6)); draw((2,-1)--(2,6)); draw((1,-1)--(1,6)); draw((-1,4)--(6,4)); draw((-1,3)--(6,3)); draw((-1,2)--(6,2)); draw((-1,1)--(6,1)); draw((0,-1)--(0,6)); draw((-1,5)--(6,5)); draw((-1,0)--(6,0)); draw((5,-1)--(5,6)); [/asy] We can now count the number of black and white tiles; 32 black tiles and 17 white tiles. This means the answer is $\boxed{\textbf{(D) }32:17}$ .

## Solution 2
If we did not want to draw a diagram though that is probably simpler in this case, we can imagine the last border of black tiles. We see that each side length (if the side length of a square is $1$ ) increases by $2$ each time we go out one layer. Therefore, we know that the next border will have a side length of $7$ . That border has $7^2-5^2=24$ black squares in it. The other black border has $3^2-1^2=8$ squares in it, so there are $32$ black squares in all. The other ones must all be white, so there are $49-32=17$ white squares. Thus, we get our answer of $\boxed{\textbf{(D) }32:17}$ .

## Solution 3 (somewhat fake)
Notice that in total, once we add the border there will be $7^2$ squares total. So far as there is only one option that sums to 49 and we know that there are an integer number of boxes, it has to be $\boxed{\textbf{(D) }32:17}$ . ~math_genius_11

## Video Solution by WhyMath
https://youtu.be/6XNr5HWgMdI
### See Also