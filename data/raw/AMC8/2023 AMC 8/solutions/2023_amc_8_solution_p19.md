# 2023 AMC 8 Problem 19

## Problem

An equilateral triangle is placed inside a larger equilateral triangle so that the region between them can be divided into three congruent trapezoids, as shown below. The side length of the inner triangle is $\frac23$ the side length of the larger triangle. What is the ratio of the area of one trapezoid to the area of the inner triangle?

[asy] // Diagram by TheMathGuyd pair A,B,C; A=(0,1); B=(sqrt(3)/2,-1/2); C=-conj(B); fill(2B--3B--3C--2C--cycle,grey); dot(3A); dot(3B); dot(3C); dot(2A); dot(2B); dot(2C); draw(2A--2B--2C--cycle); draw(3A--3B--3C--cycle); draw(2A--3A); draw(2B--3B); draw(2C--3C); [/asy]

$\textbf{(A) } 1 : 3 \qquad \textbf{(B) } 3 : 8 \qquad \textbf{(C) } 5 : 12 \qquad \textbf{(D) } 7 : 16 \qquad \textbf{(E) } 4 : 9$

## Solution 1
All equilateral triangles are similar. For the outer equilateral triangle to the inner equilateral triangle, since their side-length ratio is $\frac32,$ their area ratio is $\left(\frac32\right)^2=\frac94.$ It follows that the area ratio of three trapezoids to the inner equilateral triangle is $\frac94-1=\frac54,$ so the area ratio of one trapezoid to the inner equilateral triangle is \[\frac54\cdot\frac13=\frac{5}{12}=\boxed{\textbf{(C) } 5 : 12}.\] ~apex304, SohumUttamchandani, wuwang2002, TaeKim, Cxrupptedpat, MRENTHUSIASM

## Solution 2
Subtracting the larger equilateral triangle from the smaller one yields the sum of the three trapezoids. Since the ratio of the side lengths of the larger to the smaller one is $3:2$ , we can set the side lengths as $3$ and $2$ , respectively. So, the sum of the trapezoids is $\frac{9\sqrt{3}}{4}-\frac{4\sqrt{3}}{4}=\frac{5}{4}\sqrt{3}$ . We are also told that the three trapezoids are congruent, thus the area of each of them is $\frac{1}{3} \cdot \frac{5}{4}\sqrt{3}=\frac{5}{12}\sqrt{3}$ . Hence, the ratio is $\frac{\frac{5}{12}\sqrt{3}}{\sqrt{3}}=\frac{5}{12}=\boxed{\textbf{(C) } 5 : 12}$ .
~MrThinker

## Video Solution by Math-X (Quick and Simple Under 30 seconds)
https://youtu.be/Ku_c1YHnLt0?si=AtiMigHKcdyC8nw9&t=4074 ~Math-X

## Video Solution by CoolMathProblems
https://youtu.be/ycBjF78BAOs

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=2008 ~hsnacademy

## Video Solution
https://youtu.be/u0Qa3A3jFFU
~Education, the Study of Everything

## Video Solution by OmegaLearn (Using Similar Triangles)
https://youtu.be/bGN-uBsVm0E

## Animated Video Solution
https://youtu.be/Xq4LdJJtbDk

## Video Solution by SpreadTheMathLove using Area-Similarity Relationship
https://www.youtube.com/watch?v=92hAg3JjqZI
~Star League ( https://starleague.us )

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=3360

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=24

## Video Solution by WhyMath
https://youtu.be/gjc3Dslaimg
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=Ki4tPSGAapU&t=350s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/dTi_0SpcKnc

## Video Solution by WhyMath
https://youtu.be/YnpnKbm68tg
### See Also