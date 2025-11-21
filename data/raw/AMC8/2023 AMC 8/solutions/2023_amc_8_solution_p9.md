# 2023 AMC 8 Problem 9

## Problem

Malaika is skiing on a mountain. The graph below shows her elevation, in meters, above the base of the mountain as she skis along a trail. In total, how many seconds does she spend at an elevation between $4$ and $7$ meters? [asy] // Diagram by TheMathGuyd. Found cubic, so graph is perfect. import graph; size(8cm); int i; for(i=1; i<9; i=i+1) { draw((-0.2,2i-1)--(16.2,2i-1), mediumgrey); draw((2i-1,-0.2)--(2i-1,16.2), mediumgrey); draw((-0.2,2i)--(16.2,2i), grey); draw((2i,-0.2)--(2i,16.2), grey); } Label f; f.p=fontsize(6); xaxis(-0.5,17.8,Ticks(f, 2.0),Arrow()); yaxis(-0.5,17.8,Ticks(f, 2.0),Arrow()); real f(real x) { return -0.03125 x^(3) + 0.75x^(2) - 5.125 x + 14.5; } draw(graph(f,0,15.225),currentpen+1); real dpt=2; real ts=0.75; transform st=scale(ts); label(rotate(90)*st*"Elevation (meters)",(-dpt,8)); label(st*"Time (seconds)",(8,-dpt)); [/asy] $\textbf{(A)}\ 6 \qquad \textbf{(B)}\ 8 \qquad \textbf{(C)}\ 10 \qquad \textbf{(D)}\ 12 \qquad \textbf{(E)}\ 14$

## Solution 1
We mark the time intervals in which Malaika's elevation is between $4$ and $7$ meters in red, as shown below: [asy] // Diagram by TheMathGuyd. Found cubic, so graph is perfect. import graph; size(8cm); int i; for(i=1; i<9; i=i+1) { draw((-0.2,2i-1)--(16.2,2i-1), mediumgrey); draw((2i-1,-0.2)--(2i-1,16.2), mediumgrey); draw((-0.2,2i)--(16.2,2i), grey); draw((2i,-0.2)--(2i,16.2), grey); } Label f; f.p=fontsize(6); xaxis(-0.5,17.8,Ticks(f, 2.0),Arrow()); yaxis(-0.5,17.8,Ticks(f, 2.0),Arrow()); real f(real x) { return -0.03125 x^(3) + 0.75x^(2) - 5.125 x + 14.5; } draw(graph(f,0,15.225),currentpen+1); draw(graph(f,2,4)^^graph(f,6,10)^^graph(f,12,14),red+currentpen+2); real dpt=2; real ts=0.75; transform st=scale(ts); label(rotate(90)*st*"Elevation (meters)",(-dpt,8)); label(st*"Time (seconds)",(8,-dpt)); [/asy] The requested time intervals are:
In total, Malaika spends $(4-2) + (10-6) + (14-12) = \boxed{\textbf{(B)}\ 8}$ seconds at such elevation.
~apex304, MRENTHUSIASM

## Solution 2
Notice that the entire section between the $2$ second mark and the $14$ second mark is between the $4$ and $7$ feet elevation level except the $2$ seconds where she skis just under the $4$ feet mark and when she skis just above the $7$ feet mark, making the answer $14-2-2-2=\boxed{\textbf{(B)}\ 8}.$

## Video Solution by CoolMathProblmes
https://youtu.be/Pf93RGtKo1I?feature=shared&t=615

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=499 ~hsnacademy

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/wQd1lHtkVPU
~Education the Study of everything

## Video Solution by Math-X (Let's first Understand the question)
https://youtu.be/Ku_c1YHnLt0?si=_0SCHsHavl1dJJpP&t=1364
~Math-X

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=lfyg5ZMV0gg
https://www.youtube.com/watch?v=TAa6jarbATE

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=4903

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=786

## Video Solution by harungurcan
https://www.youtube.com/watch?v=oIGy79w1H8o&t=15s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/MTYUJ1wg2q0

## Video Solution by WhyMath
https://youtu.be/cHyJB7oXgxk
### See Also