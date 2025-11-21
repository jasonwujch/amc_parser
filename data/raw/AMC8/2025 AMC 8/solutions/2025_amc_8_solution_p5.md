# 2025 AMC 8 Problem 5

## Problem

Betty drives a truck to deliver packages in a neighborhood whose street map is shown below. Betty starts at the factory (labled $F$ ) and drives to location $A$ , then $B$ , then $C$ , before returning to $F$ . What is the shortest distance, in blocks, she can drive to complete the route?

[asy] unitsize(20); add(grid(8,6)); path w = circle((0,0),0.4); fill(w, white); draw(w); label("$B$",(0,0)); fill(shift((2,4)) * w, white); draw(shift((2,4)) * w); label("$C$",(2,4)); fill(shift((7,3)) * w, white); draw(shift((7,3)) * w); label("$A$",(7,3)); fill(shift((6,5)) * w, white); draw(shift((6,5)) * w); label("$F$",(6,5)); draw((6,-0.2)--(7,-0.2), EndArrow(3)); draw((7,-0.2)--(6,-0.2), EndArrow(3)); draw(shift(6.5, -0.48) * scale(0.03) * texpath("1 block")); draw((8.2,1)--(8.2,2), EndArrow(3)); draw((8.2,2)--(8.2,1), EndArrow(3)); draw(shift(8.88, 1.5) * scale(0.03) * texpath("1 block")); [/asy]

$\textbf{(A)}\ 20 \qquad \textbf{(B)}\ 22 \qquad \textbf{(C)}\ 24 \qquad \textbf{(D)}\ 26\qquad \textbf{(E)}\ 28$

## Solution 1
Each shortest possible path from $A$ to $B$ follows the edges of the rectangle. The following path outlines a path of $\boxed{\textbf{(C)}\ 24}$ units:
[asy] unitsize(20); add(grid(8,6)); draw((6,5)--(7,5)--(7,0)--(0,0)--(0,4)--(2,4)--(2,5)--cycle,green); path w = circle((0,0),0.4); fill(w, white); draw(w); label("$B$",(0,0)); fill(shift((2,4)) * w, white); draw(shift((2,4)) * w); label("$C$",(2,4)); fill(shift((7,3)) * w, white); draw(shift((7,3)) * w); label("$A$",(7,3)); fill(shift((6,5)) * w, white); draw(shift((6,5)) * w); label("$F$",(6,5)); [/asy]
~ zhenghua

## Solution 2
We can find the shortest distance using a line diagonally from one point to the other, creating a sort of slope, then find the sum of rise and run of the slope, which happens to be the shortest distance, repeat this process until you get back to Point $F$ , and you should get $2 + 1 + 3 + 7 + 4 + 2 + 1 + 4$ , which is equal to $\boxed{\textbf{(C)}\ 24}$ . ~Imhappy62789

## Video Solution 1
~ ChillGuyDoesMath

## Video Solution 2 by Daily Dose of Math
~Thesmartgreekmathdude

## Video Solution 3
https://youtu.be/VP7g-s8akMY?si=2TfegPRg-_k1DEcz&t=257 ~hsnacademy

## Video Solution 4 by Thinking Feet
https://youtu.be/PKMpTS6b988

## Video Solution 5 by Pi Academy
https://youtu.be/Iv_a3Rz725w?si=E0SI_h1XT8msWgkK

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC
### See Also