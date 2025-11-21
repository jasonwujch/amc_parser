# 2021 AMC 10B Problem 8

## Problem

Mr. Zhou places all the integers from $1$ to $225$ into a $15$ by $15$ grid. He places $1$ in the middle square (eighth row and eighth column) and places other numbers one by one clockwise, as shown in part in the diagram below. What is the sum of the greatest number and the least number that appear in the second row from the top? [asy] /* Made by samrocksnature */ add(grid(7,7)); label("$\dots$", (0.5,0.5)); label("$\dots$", (1.5,0.5)); label("$\dots$", (2.5,0.5)); label("$\dots$", (3.5,0.5)); label("$\dots$", (4.5,0.5)); label("$\dots$", (5.5,0.5)); label("$\dots$", (6.5,0.5)); label("$\dots$", (1.5,0.5)); label("$\dots$", (0.5,1.5)); label("$\dots$", (0.5,2.5)); label("$\dots$", (0.5,3.5)); label("$\dots$", (0.5,4.5)); label("$\dots$", (0.5,5.5)); label("$\dots$", (0.5,6.5)); label("$\dots$", (6.5,0.5)); label("$\dots$", (6.5,1.5)); label("$\dots$", (6.5,2.5)); label("$\dots$", (6.5,3.5)); label("$\dots$", (6.5,4.5)); label("$\dots$", (6.5,5.5)); label("$\dots$", (0.5,6.5)); label("$\dots$", (1.5,6.5)); label("$\dots$", (2.5,6.5)); label("$\dots$", (3.5,6.5)); label("$\dots$", (4.5,6.5)); label("$\dots$", (5.5,6.5)); label("$\dots$", (6.5,6.5)); label("$17$", (1.5,1.5)); label("$18$", (1.5,2.5)); label("$19$", (1.5,3.5)); label("$20$", (1.5,4.5)); label("$21$", (1.5,5.5)); label("$16$", (2.5,1.5)); label("$5$", (2.5,2.5)); label("$6$", (2.5,3.5)); label("$7$", (2.5,4.5)); label("$22$", (2.5,5.5)); label("$15$", (3.5,1.5)); label("$4$", (3.5,2.5)); label("$1$", (3.5,3.5)); label("$8$", (3.5,4.5)); label("$23$", (3.5,5.5)); label("$14$", (4.5,1.5)); label("$3$", (4.5,2.5)); label("$2$", (4.5,3.5)); label("$9$", (4.5,4.5)); label("$24$", (4.5,5.5)); label("$13$", (5.5,1.5)); label("$12$", (5.5,2.5)); label("$11$", (5.5,3.5)); label("$10$", (5.5,4.5)); label("$25$", (5.5,5.5)); [/asy]

$\textbf{(A)} ~367 \qquad\textbf{(B)} ~368 \qquad\textbf{(C)} ~369 \qquad\textbf{(D)} ~379 \qquad\textbf{(E)} ~380$

## Solution 1 (Observations and Patterns: Considers Only 5 Squares)
In the diagram below, the red arrows indicate the progression of numbers. In the second row from the top, the greatest number and the least number are $D$ and $E,$ respectively. Note that the numbers in the yellow cells are consecutive odd perfect squares, as we can prove by induction. [asy] /* Made by MRENTHUSIASM */ size(11.5cm); for (real i=7.5; i<=14.5; ++i) { fill((i+0.5,i+0.5)--(i-0.5,i+0.5)--(i-0.5,i-0.5)--(i+0.5,i-0.5)--cycle,yellow); } fill((2,14)--(1,14)--(1,13)--(2,13)--cycle,green); fill((1,14)--(0,14)--(0,13)--(1,13)--cycle,green); label("$A$",(14.5,14.5)); label("$B$",(13.5,13.5)); label("$C$",(0.5,14.5)); label("$E$",(1.5,13.5)); label("$D$",(0.5,13.5)); add(grid(15,15,linewidth(1.25))); draw((1.5,13.5)--(14.5,13.5)--(14.5,0.5)--(0.5,0.5)--(0.5,14.5)--(14.5,14.5),red+linewidth(1.125),EndArrow); [/asy] By observations, we proceed as follows: \begin{alignat*}{6} A=15^2=225, \ B=13^2=169 \quad &\implies \quad &C &= \hspace{1mm}&&A-14\hspace{1mm} &= 211& \\ \quad &\implies \quad &D &= &&C-1 &= 210& \\ \quad &\implies \quad &E &= &&B-12 &= 157&. \end{alignat*} Therefore, the answer is $D+E=\boxed{\textbf{(A)} ~367}.$
~MRENTHUSIASM

## Solution 2 (Observations and Patterns: Considers Only 7 Squares)
In the diagram below, the red arrows indicate the progression of numbers. In the second row from the top, the greatest number and the least number are $C$ and $G,$ respectively. [asy] /* Made by MRENTHUSIASM */ size(11.5cm); fill((2,14)--(1,14)--(1,13)--(2,13)--cycle,green); fill((1,14)--(0,14)--(0,13)--(1,13)--cycle,green); label("$A$",(14.5,14.5)); label("$B$",(0.5,14.5)); label("$C$",(0.5,13.5)); label("$D$",(0.5,0.5)); label("$E$",(14.5,0.5)); label("$F$",(14.5,13.5)); label("$G$",(1.5,13.5)); add(grid(15,15,linewidth(1.25))); draw((1.5,13.5)--(14.5,13.5)--(14.5,0.5)--(0.5,0.5)--(0.5,14.5)--(14.5,14.5),red+linewidth(1.125),EndArrow); [/asy] By observations, we proceed as follows: \begin{alignat*}{6} A=15^2=225 \quad &\implies \quad &B &= \hspace{1mm}&&A-14\hspace{1mm} &= 211& \\ \quad &\implies \quad &C &= &&B-1 &= 210& \\ \quad &\implies \quad &D &= &&C-13 &= 197& \\ \quad &\implies \quad &E &= &&D-14 &= 183& \\ \quad &\implies \quad &F &= &&E-13 &= 170& \\ \quad &\implies \quad &G &= &&F-13 &= 157&. \end{alignat*} Therefore, the answer is $C+G=\boxed{\textbf{(A)} ~367}.$
~MRENTHUSIASM ~Dynosol

## Solution 3 (Brute Force: Draws All 225 Squares Out)
From the full diagram below, the answer is $210+157=\boxed{\textbf{(A)} ~367}.$ [asy] /* Made by MRENTHUSIASM */ size(11.5cm); fill((2,14)--(1,14)--(1,13)--(2,13)--cycle,green); fill((1,14)--(0,14)--(0,13)--(1,13)--cycle,green); add(grid(15,15,linewidth(1.25))); int adj = 1; int curDown = 2; int curLeft = 4; int curUp = 6; int curRight = 8; label("$1$",(7.5,7.5)); for (int len = 3; len<=15; len+=2) { for (int i=1; i<=len-1; ++i) { label("$"+string(curDown)+"$",(7.5+adj,7.5+adj-i)); label("$"+string(curLeft)+"$",(7.5+adj-i,7.5-adj)); label("$"+string(curUp)+"$",(7.5-adj,7.5-adj+i)); label("$"+string(curRight)+"$",(7.5-adj+i,7.5+adj)); ++curDown; ++curLeft; ++curUp; ++curRight; } ++adj; curDown = len^2 + 1; curLeft = len^2 + len + 2; curUp = len^2 + 2*len + 3; curRight = len^2 + 3*len + 4; } [/asy] This solution is extremely time-consuming and error-prone. Please do not try it in a real competition unless you have no other options.
~MRENTHUSIASM ~Taco12

## Video Solution by OmegaLearn (Using Pattern Finding)
https://youtu.be/bb4HB7pwO3Q
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/GYpAm8v1h-U?t=412
~IceMatrix

## Video Solution by Interstigation
https://youtu.be/DvpN56Ob6Zw?t=667
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .