# 2022 AMC 8 Problem 10

## Problem

One sunny day, Ling decided to take a hike in the mountains. She left her house at $8 \, \textsc{am}$ , drove at a constant speed of $45$ miles per hour, and arrived at the hiking trail at $10 \, \textsc{am}$ . After hiking for $3$ hours, Ling drove home at a constant speed of $60$ miles per hour. Which of the following graphs best illustrates the distance between Ling’s car and her house over the course of her trip?

[asy] unitsize(12); usepackage("mathptmx"); defaultpen(fontsize(8)+linewidth(.7)); int mod12(int i) {if (i<13) {return i;} else {return i-12;}} void drawgraph(pair sh,string lab) { for (int i=0;i<11;++i) { for (int j=0;j<6;++j) { draw(shift(sh+(i,j))*unitsquare,mediumgray); } } draw(shift(sh)*((-1,0)--(11,0)),EndArrow(angle=20,size=8)); draw(shift(sh)*((0,-1)--(0,6)),EndArrow(angle=20,size=8)); for (int i=1;i<10;++i) { draw(shift(sh)*((i,-.2)--(i,.2))); } label("8\tiny{\textsc{am}}",sh+(1,-.2),S); for (int i=2;i<9;++i) { label(string(mod12(i+7)),sh+(i,-.2),S); } label("4\tiny{\textsc{pm}}",sh+(9,-.2),S); for (int i=1;i<6;++i) { label(string(30*i),sh+(0,i),2*W); } draw(rotate(90)*"Distance (miles)",sh+(-2.1,3),fontsize(10)); label("$\textbf{("+lab+")}$",sh+(-2.1,6.8),fontsize(12)); } drawgraph((0,0),"A"); drawgraph((15,0),"B"); drawgraph((0,-10),"C"); drawgraph((15,-10),"D"); drawgraph((0,-20),"E"); dotfactor=6; draw((1,0)--(3,3)--(6,3)--(8,0),linewidth(.9)); dot((1,0)^^(3,3)^^(6,3)^^(8,0)); pair sh = (15,0); draw(shift(sh)*((1,0)--(3,1.5)--(6,1.5)--(8,0)),linewidth(.9)); dot(sh+(1,0)^^sh+(3,1.5)^^sh+(6,1.5)^^sh+(8,0)); pair sh = (0,-10); draw(shift(sh)*((1,0)--(3,1.5)--(6,1.5)--(7.5,0)),linewidth(.9)); dot(sh+(1,0)^^sh+(3,1.5)^^sh+(6,1.5)^^sh+(7.5,0)); pair sh = (15,-10); draw(shift(sh)*((1,0)--(3,4)--(6,4)--(9.3,0)),linewidth(.9)); dot(sh+(1,0)^^sh+(3,4)^^sh+(6,4)^^sh+(9.3,0)); pair sh = (0,-20); draw(shift(sh)*((1,0)--(3,3)--(6,3)--(7.5,0)),linewidth(.9)); dot(sh+(1,0)^^sh+(3,3)^^sh+(6,3)^^sh+(7.5,0)); [/asy]

## Solution 1 (Analysis)
Note that:
It follows that at Ling's car was miles from her house.
It follows that at Ling's car was still miles from her house.
It follows that at Ling's car was miles from her house.
Therefore, the answer is $\boxed{\textbf{(E)}}.$
~MRENTHUSIASM

## Solution 2 (Elimination)
Ling's trip took $2$ hours, thus she traveled for $2 \times 45=90$ miles. Choices $\textbf{(B)}$ , $\textbf{(C)}$ , and $\textbf{(D)}$ are eliminated. Ling drove $45$ miles per hour (mph) to the mountains, and $60$ mph back to her house, so the rightmost slope must be steeper than the leftmost one. Choice $\textbf {(A)}$ is eliminated. This leaves us with $\boxed{\textbf{(E)}}$ .

## Solution 3 (Elimination)
Using the $\text{speed} = \frac{\text{distance}}{\text{time}}$ formula, and plugging in the values $45$ mph and $2$ hrs, we get that the distance from Ling's house to the mountains is $90$ miles. That means the first slope ends at $90,$ so choices $\textbf{(B)}, \textbf{(C)},$ and $\textbf{(D)}$ are eliminated.
Furthermore, if the distance is $90$ miles, and Ling is returning home at $60$ mph, it must have taken her $1.5$ hours. Adding $1.5$ and $3$ (how long she hiked for) to her arrival time, $10$ AM, we see she must have come back home at $2:30$ PM. Choice $\textbf{(A)}$ is eliminated, so the only valid choice left is choice $\boxed{\textbf{(E)}}.$
~ProProtractor

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/tYWp6fcUAik?si=V8hv_zOn_zYOi9E5&t=1207 ~hsnacademy

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/oUEa7AjMF2A?si=GriQR9m9WenwQVdf&t=1311
~Math-X

## Video Solution (CRITICAL THINKING!!!)
https://youtu.be/Q3G-qyCUnYI
~Education, the Study of Everything

## Video Solution
https://www.youtube.com/watch?v=Ij9pAy6tQSg&t=733
~Interstigation

## Video Solution
https://youtu.be/1xspUFoKDnU?t=332
~STEMbreezy

## Video Solution
https://youtu.be/q4hJk1HYxDk
~savannahsolver

## Video Solution
https://youtu.be/BzKZSwxJHJ0
~harungurcan

## Video Solution by Dr. David
https://youtu.be/P4SFHiKCz8Y
### See Also