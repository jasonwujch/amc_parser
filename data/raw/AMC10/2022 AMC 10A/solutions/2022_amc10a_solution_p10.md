# 2022 AMC 10A Problem 10

## Problem

Daniel finds a rectangular index card and measures its diagonal to be $8$ centimeters. Daniel then cuts out equal squares of side $1$ cm at two opposite corners of the index card and measures the distance between the two closest vertices of these squares to be $4\sqrt{2}$ centimeters, as shown below. What is the area of the original index card? [asy] // Diagram by MRENTHUSIASM, edited by Djmathman size(200); defaultpen(linewidth(0.6)); draw((489.5,-213) -- (225.5,-213) -- (225.5,-185) -- (199.5,-185) -- (198.5,-62) -- (457.5,-62) -- (457.5,-93) -- (489.5,-93) -- cycle); draw((206.29,-70.89) -- (480.21,-207.11), linetype ("6 6"),Arrows(size=4,arrowhead=HookHead)); draw((237.85,-182.24) -- (448.65,-95.76),linetype ("6 6"),Arrows(size=4,arrowhead=HookHead)); label("$1$",(450,-80)); label("$1$",(475,-106)); label("$8$",(300,-103)); label("$4\sqrt 2$",(300,-173)); [/asy] $\textbf{(A) } 14 \qquad \textbf{(B) } 10\sqrt{2} \qquad \textbf{(C) } 16 \qquad \textbf{(D) } 12\sqrt{2} \qquad \textbf{(E) } 18$

## Solution 1
[asy] /* Edited by MRENTHUSIASM */ size(250); real x, y; x = 6; y = 3; draw((0,0)--(x,0)); draw((0,0)--(0,y)); draw((0,y)--(x,y)); draw((x,0)--(x,y)); draw((0.5,0)--(0.5,0.5)--(0,0.5)); draw((x-0.5,y)--(x-0.5,y-0.5)--(x,y-0.5)); draw((0.5,0.5)--(x-0.5,y-0.5),dashed,Arrows()); draw((x,0)--(0,y),dashed,Arrows()); label("$1$",(x-0.5,y-0.25),W); label("$1$",(x-0.25,y-0.5),S); label("$8$",midpoint((0.5,y-0.5)--(x/2,y/2)),(0,2.5)); label("$4\sqrt{2}$",midpoint((0.5,0.5)--(x/2,y/2)),S); label("$A$",(0,0),SW); label("$E$",(0,0.5),W); label("$F$",(0.5,0),S); label("$I$",(0.5,0.5),N); label("$D$",(x,y),NE); label("$G$",(x-0.5,y),N); label("$H$",(x,y-0.5),E); label("$J$",(x-0.5,y-0.5),S); Label L1 = Label("$w$", align=(0,0), position=MidPoint, filltype=Fill(3,0,white)); Label L2 = Label("$\ell$", align=(0,0), position=MidPoint, filltype=Fill(0,3,white)); draw((0,-1)--(x,-1), L=L1, arrow=Arrows(),bar=Bars(15)); draw((x+1,0)--(x+1,y), L=L2, arrow=Arrows(),bar=Bars(15)); [/asy] Label the bottom left corner of the larger rectangle (without the square cut out) as $A$ and the top right as $D$ . $w$ is the width of the rectangle and $\ell$ is the length. Now we have vertices $E, F, G, H$ as vertices of the irregular octagon created by cutting out the squares. Let $I, J$ be the two closest vertices formed by the squares. The distance between the two closest vertices of the squares is thus $IJ=\left(4\sqrt{2}\right).$ Substituting, we get:
\[(IJ)^2 = (w-2)^2 + (\ell-2)^2 = \left(4\sqrt{2}\right)^2 = 32 \implies w^2+\ell^2-4w-4\ell = 24.\] Using the fact that the diagonal of the rectangle is $8,$ we get: \[w^2+\ell^2 = 64.\] Subtracting the first equation from the second equation, we get: \[4w+4\ell=40 \implies w+\ell = 10.\] Squaring yields: \[w^2 + 2w\ell + \ell^2 = 100.\] Subtracting the second equation from this, we get: $2w\ell = 36,$ and thus the area of the original rectangle is $w\ell = \boxed{\textbf{(E) } 18}.$
~USAMO333
Edits and Diagram by ~KingRavi and ~MRENTHUSIASM
Minor edit by yanes04

## Solution 2
https://youtu.be/SRV4e74qsM8
Let x be the width of the original rectangle and y be the height. Through observation and logic, we can then conclude that \[(x-2)^2 + (y-2)^2 = 32.\] After expanding and simplifying the expressions, you end up with $x+y=10.$ If you then solve for x in terms of y, you end up with $x=10-y.$ Since 8 is the diagonal of the original rectangle, we can write that \[(10-y)^2+y^2=64.\] Use the quadratic formula to solve for y, and then solve for x. Using either root, yields a product of the difference of squares, $25-7=18.$ Therefore, 18 (E) is our solution!
~Namya
Note: I just changed it into Latex as it looked a little bit unclear.
~moonwatcher0201
Note: This is incredibly similar to Solution 1. In fact, the only difference is the method of Algebra used to calculate the final answer, which in my opinion doesn’t really constitute a whole new solution.
~ilee0820

## Video Solution
https://youtu.be/BIy0Koe4D4s
~Education, the Study of Everything

## Video Solution 1 Clear
https://www.youtube.com/watch?v=rDE8Yyx20ZI

## Video Solution 2 (Pythagorean Theorem & Square of Binomial)
https://www.youtube.com/watch?v=rJ61GqU6NWM&list=PLmpPPbOoDfgj5BlPtEAGcB7BR_UA5FgFj&index=5