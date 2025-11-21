# 2023 AMC 8 Problem 4

## Problem

The numbers from $1$ to $49$ are arranged in a spiral pattern on a square grid, beginning at the center. The first few numbers have been entered into the grid below. Consider the four numbers that will appear in the shaded squares, on the same diagonal as the number $7.$ How many of these four numbers are prime? [asy] /* Made by MRENTHUSIASM */ size(175); void ds(pair p) { filldraw((0.5,0.5)+p--(-0.5,0.5)+p--(-0.5,-0.5)+p--(0.5,-0.5)+p--cycle,mediumgrey); } ds((0.5,4.5)); ds((1.5,3.5)); ds((3.5,1.5)); ds((4.5,0.5)); add(grid(7,7,grey+linewidth(1.25))); int adj = 1; int curUp = 2; int curLeft = 4; int curDown = 6; label("$1$",(3.5,3.5)); for (int len = 3; len<=3; len+=2) { for (int i=1; i<=len-1; ++i) { label("$"+string(curUp)+"$",(3.5+adj,3.5-adj+i)); label("$"+string(curLeft)+"$",(3.5+adj-i,3.5+adj)); label("$"+string(curDown)+"$",(3.5-adj,3.5+adj-i)); ++curDown; ++curLeft; ++curUp; } ++adj; curUp = len^2 + 1; curLeft = len^2 + len + 2; curDown = len^2 + 2*len + 3; } draw((4,4)--(3,4)--(3,3)--(5,3)--(5,5)--(2,5)--(2,2)--(6,2)--(6,6)--(1,6)--(1,1)--(7,1)--(7,7)--(0,7)--(0,0)--(7,0),linewidth(2)); [/asy] $\textbf{(A)}\ 0 \qquad \textbf{(B)}\ 1 \qquad \textbf{(C)}\ 2 \qquad \textbf{(D)}\ 3 \qquad \textbf{(E)}\ 4$

## Solution 1
We fill out the grid, as shown below: [asy] /* Made by MRENTHUSIASM */ size(175); void ds(pair p) { filldraw((0.5,0.5)+p--(-0.5,0.5)+p--(-0.5,-0.5)+p--(0.5,-0.5)+p--cycle,mediumgrey); } ds((0.5,4.5)); ds((1.5,3.5)); ds((3.5,1.5)); ds((4.5,0.5)); add(grid(7,7,grey+linewidth(1.25))); int adj = 1; int curUp = 2; int curLeft = 4; int curDown = 6; int curRight = 8; label("$1$",(3.5,3.5)); for (int len = 3; len<=7; len+=2) { for (int i=1; i<=len-1; ++i) { label("$"+string(curUp)+"$",(3.5+adj,3.5-adj+i)); label("$"+string(curLeft)+"$",(3.5+adj-i,3.5+adj)); label("$"+string(curDown)+"$",(3.5-adj,3.5+adj-i)); label("$"+string(curRight)+"$",(3.5-adj+i,3.5-adj)); ++curDown; ++curLeft; ++curUp; ++curRight; } ++adj; curUp = len^2 + 1; curLeft = len^2 + len + 2; curDown = len^2 + 2*len + 3; curRight = len^2 + 3*len + 4; } draw((4,4)--(3,4)--(3,3)--(5,3)--(5,5)--(2,5)--(2,2)--(6,2)--(6,6)--(1,6)--(1,1)--(7,1)--(7,7)--(0,7)--(0,0)--(7,0),linewidth(2)); [/asy] From the four numbers that appear in the shaded squares, $\boxed{\textbf{(D)}\ 3}$ of them are prime: $19,23,$ and $47.$
~MathFun1000, MRENTHUSIASM

## Solution 2
Note that given time constraint, it's better to only count from perfect squares (in pink), as shown below: [asy] /* Grid Made by MRENTHUSIASM */ /* Squares pattern solution input by TheMathGuyd */ size(175); void ds(pair p) { filldraw((0.5,0.5)+p--(-0.5,0.5)+p--(-0.5,-0.5)+p--(0.5,-0.5)+p--cycle,mediumgrey); } void ps(pair p) { filldraw((0.5,0.5)+p--(-0.5,0.5)+p--(-0.5,-0.5)+p--(0.5,-0.5)+p--cycle,pink+opacity(0.3)); } real ts = 0.5; ds((0.5,4.5));label("$39$",(0.5,4.5)); ds((1.5,3.5));label("$19$",(1.5,3.5)); ds((3.5,1.5));label("$23$",(3.5,1.5)); ds((4.5,0.5));label("$47$",(4.5,0.5)); ps((3.5,3.5));label("$1$",(3.5,3.5)); ps((4.5,2.5));label("$9$",(4.5,2.5)); ps((5.5,1.5));label("$25$",(5.5,1.5)); ps((6.5,0.5));label("$49$",(6.5,0.5)); ps((3.5,4.5));label("$4$",(3.5,4.5)); ps((2.5,5.5));label("$16$",(2.5,5.5)); ps((1.5,6.5));label("$36$",(1.5,6.5)); label(scale(ts)*"$\leftarrow$",(1,6),NE); label(scale(ts)*"$+1$",(1,6),NW); label(scale(ts)*"$\downarrow$",(1,6),SW); label(scale(ts)*"$+2$",(1,5),NW); label(scale(ts)*"$\downarrow$",(1,5),SW); label(scale(ts)*"$+3$",(1,4),NW); label(scale(ts)*"$+1$",(2,5),NW); label(scale(ts)*"$\downarrow$",(2,5),SW); label(scale(ts)*"$+2$",(2,4),NW); label(scale(ts)*"$\downarrow$",(2,4),SW); label(scale(ts)*"$+3$",(2,3),NW); label(scale(ts)*"$\leftarrow$",(5,1),NE); label(scale(ts)*"$-1$",(5,1),NW); label(scale(ts)*"$\leftarrow$",(4,1),NE); label(scale(ts)*"$-2$",(4,1),NW); label(scale(ts)*"$\leftarrow$",(6,0),NE); label(scale(ts)*"$-1$",(6,0),NW); label(scale(ts)*"$\leftarrow$",(5,0),NE); label(scale(ts)*"$-2$",(5,0),NW); add(grid(7,7,grey+linewidth(1.25))); //USES OLYMPIAD.ASY draw((4,4)--(3,4)--(3,3)--(5,3)--(5,5)--(2,5)--(2,2)--(6,2)--(6,6)--(1,6)--(1,1)--(7,1)--(7,7)--(0,7)--(0,0)--(7,0),linewidth(2)); [/asy] From the four numbers that appear in the shaded squares, $\boxed{\textbf{(D)}\ 3}$ of them are prime: $19,23,$ and $47.$
~TheMathGuyd

## Solution 3
Since the last shaded square is very close to the final number, which is 49, we can easily subtract two instead of having to count all the way there. Then, we can count (:P).
~AliceDubbleYou

## Video Solution by CoolMathProblems
https://youtu.be/Pf93RGtKo1I?feature=shared&t=190

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=158 ~hsnacademy

## Simple, Intuitive Solution by MathTalks_Now
https://studio.youtube.com/video/PMOeiGLkDH0/edit

## Video Solution (How to Creatively THINK!!!)
https://youtu.be/7gwhzjySKl0
~Education the Study of everything

## Video Solution by Math-X (Smart and Simple)
https://youtu.be/Ku_c1YHnLt0?si=cc_Ii2j2pmT6wOuZ&t=412
~Math-X

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=5392

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=EcrktBc8zrM

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=233

## Video Solution by WhyMath
https://youtu.be/1qwfPJDNYGc
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=35BW7bsm_Cg&t=402s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/9ynYd5V0r88
### See Also