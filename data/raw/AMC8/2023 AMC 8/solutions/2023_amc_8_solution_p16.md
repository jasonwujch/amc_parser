# 2023 AMC 8 Problem 16

## Problem

The letters $\text{P}, \text{Q},$ and $\text{R}$ are entered into a $20\times20$ table according to the pattern shown below. How many $\text{P}$ s, $\text{Q}$ s, and $\text{R}$ s will appear in the completed table? [asy] /* Made by MRENTHUSIASM, Edited by Kante314 */ usepackage("mathdots"); size(5cm); draw((0,0)--(6,0),linewidth(1.5)+mediumgray); draw((0,1)--(6,1),linewidth(1.5)+mediumgray); draw((0,2)--(6,2),linewidth(1.5)+mediumgray); draw((0,3)--(6,3),linewidth(1.5)+mediumgray); draw((0,4)--(6,4),linewidth(1.5)+mediumgray); draw((0,5)--(6,5),linewidth(1.5)+mediumgray); draw((0,0)--(0,6),linewidth(1.5)+mediumgray); draw((1,0)--(1,6),linewidth(1.5)+mediumgray); draw((2,0)--(2,6),linewidth(1.5)+mediumgray); draw((3,0)--(3,6),linewidth(1.5)+mediumgray); draw((4,0)--(4,6),linewidth(1.5)+mediumgray); draw((5,0)--(5,6),linewidth(1.5)+mediumgray); label(scale(.9)*"\textsf{P}", (.5,.5)); label(scale(.9)*"\textsf{Q}", (.5,1.5)); label(scale(.9)*"\textsf{R}", (.5,2.5)); label(scale(.9)*"\textsf{P}", (.5,3.5)); label(scale(.9)*"\textsf{Q}", (.5,4.5)); label("$\vdots$", (.5,5.6)); label(scale(.9)*"\textsf{Q}", (1.5,.5)); label(scale(.9)*"\textsf{R}", (1.5,1.5)); label(scale(.9)*"\textsf{P}", (1.5,2.5)); label(scale(.9)*"\textsf{Q}", (1.5,3.5)); label(scale(.9)*"\textsf{R}", (1.5,4.5)); label("$\vdots$", (1.5,5.6)); label(scale(.9)*"\textsf{R}", (2.5,.5)); label(scale(.9)*"\textsf{P}", (2.5,1.5)); label(scale(.9)*"\textsf{Q}", (2.5,2.5)); label(scale(.9)*"\textsf{R}", (2.5,3.5)); label(scale(.9)*"\textsf{P}", (2.5,4.5)); label("$\vdots$", (2.5,5.6)); label(scale(.9)*"\textsf{P}", (3.5,.5)); label(scale(.9)*"\textsf{Q}", (3.5,1.5)); label(scale(.9)*"\textsf{R}", (3.5,2.5)); label(scale(.9)*"\textsf{P}", (3.5,3.5)); label(scale(.9)*"\textsf{Q}", (3.5,4.5)); label("$\vdots$", (3.5,5.6)); label(scale(.9)*"\textsf{Q}", (4.5,.5)); label(scale(.9)*"\textsf{R}", (4.5,1.5)); label(scale(.9)*"\textsf{P}", (4.5,2.5)); label(scale(.9)*"\textsf{Q}", (4.5,3.5)); label(scale(.9)*"\textsf{R}", (4.5,4.5)); label("$\vdots$", (4.5,5.6)); label(scale(.9)*"$\dots$", (5.5,.5)); label(scale(.9)*"$\dots$", (5.5,1.5)); label(scale(.9)*"$\dots$", (5.5,2.5)); label(scale(.9)*"$\dots$", (5.5,3.5)); label(scale(.9)*"$\dots$", (5.5,4.5)); label(scale(.9)*"$\iddots$", (5.5,5.6)); [/asy] $\textbf{(A)}~132\text{ Ps, }134\text{ Qs, }134\text{ Rs}$

$\textbf{(B)}~133\text{ Ps, }133\text{ Qs, }134\text{ Rs}$

$\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}$

$\textbf{(D)}~134\text{ Ps, }132\text{ Qs, }134\text{ Rs}$

$\textbf{(E)}~134\text{ Ps, }133\text{ Qs, }133\text{ Rs}$

## Solution 1 (Finding a Pattern)
In our $5\times5$ grid, there are $8,9$ and $8$ of the letters $\text{P}, \text{Q},$ and $\text{R}$ , respectively, and in a $2\times2$ grid, there are $1,2$ and $1$ of the letters $\text{P}, \text{Q},$ and $\text{R}$ , respectively. We see that in both grids, there are $x, x+1,$ and $x$ of the $\text{P}, \text{Q},$ and $\text{R}$ , respectively. This is because in any $n\times n$ grid with $n\equiv2\pmod3$ , there are $x, x+1,$ and $x$ of the $\text{P}, \text{Q},$ and $\text{R}$ , respectively. We can see that the only answer choice which satisfies this condition is $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}.$
~CoOlPoTaToEs, apex304, SohumUttamchandani, wuwang2002, TaeKim, Cxrupptedpat, Nivaar

## Solution 2
Since $20\equiv2\pmod3$ and $\text{Q}$ is in the 2nd diagonal, it is also in the 20th diagonal, and so we find that there are $2(2 + 5 + 8 + 11 + 14 + 17) + 20 = 134 \text{Qs}$ . Since all the $\text{P}$ 's and $\text{R}$ 's are symmetric, the answer is $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}.$
~ ILoveMath31415926535

## Solution 3
Notice that rows $x$ and $x+3$ are the same, for any $1 \leq x \leq 17.$ Additionally, rows $1, 2,$ and $3$ collectively contain the same number of $\text{P}$ s, $\text{Q}$ s, and $\text{R}$ s, because the letters are just substituted for one another. Therefore, the number of $\text{P}$ s, $\text{Q}$ s, and $\text{R}$ s in the first $18$ rows is $120$ . The first row has $7$ $\text{P}$ s, $7$ $\text{Q}$ s, and $6$ $\text{R}$ s, and the second row has $6$ $\text{P}$ s, $7$ $\text{Q}$ s, and $7$ $\text{R}$ s. Adding these up, we obtain $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}$ .
~mathboy100

## Solution 4 (Brute-Force)
From the full diagram below, the answer is $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}.$ [asy] /* Made by MRENTHUSIASM, Edited by Kante314 */ usepackage("mathdots"); size(16.666cm); for (int y = 0; y<=20; ++y) { for (int x = 0; x<=20; ++x) { draw((x,0)--(x,20),linewidth(1.5)+mediumgray); draw((0,y)--(20,y),linewidth(1.5)+mediumgray); } } void drawDiagonal(string s, pair p) { while (p.x >= 0 && p.x < 20 && p.y >= 0 && p.y < 20) { label(scale(.9)*("\textsf{" + s + "}"),p); p += (1,-1); } } drawDiagonal("P", (0.5,0.5)); drawDiagonal("Q", (0.5,1.5)); drawDiagonal("R", (0.5,2.5)); drawDiagonal("P", (0.5,3.5)); drawDiagonal("Q", (0.5,4.5)); drawDiagonal("R", (0.5,5.5)); drawDiagonal("P", (0.5,6.5)); drawDiagonal("Q", (0.5,7.5)); drawDiagonal("R", (0.5,8.5)); drawDiagonal("P", (0.5,9.5)); drawDiagonal("Q", (0.5,10.5)); drawDiagonal("R", (0.5,11.5)); drawDiagonal("P", (0.5,12.5)); drawDiagonal("Q", (0.5,13.5)); drawDiagonal("R", (0.5,14.5)); drawDiagonal("P", (0.5,15.5)); drawDiagonal("Q", (0.5,16.5)); drawDiagonal("R", (0.5,17.5)); drawDiagonal("P", (0.5,18.5)); drawDiagonal("Q", (0.5,19.5)); drawDiagonal("R", (1.5,19.5)); drawDiagonal("P", (2.5,19.5)); drawDiagonal("Q", (3.5,19.5)); drawDiagonal("R", (4.5,19.5)); drawDiagonal("P", (5.5,19.5)); drawDiagonal("Q", (6.5,19.5)); drawDiagonal("R", (7.5,19.5)); drawDiagonal("P", (8.5,19.5)); drawDiagonal("Q", (9.5,19.5)); drawDiagonal("R", (10.5,19.5)); drawDiagonal("P", (11.5,19.5)); drawDiagonal("Q", (12.5,19.5)); drawDiagonal("R", (13.5,19.5)); drawDiagonal("P", (14.5,19.5)); drawDiagonal("Q", (15.5,19.5)); drawDiagonal("R", (16.5,19.5)); drawDiagonal("P", (17.5,19.5)); drawDiagonal("Q", (18.5,19.5)); drawDiagonal("R", (19.5,19.5)); [/asy] This solution is extremely time-consuming and error-prone. Please do not try it in a real competition unless you have no other options.
~MRENTHUSIASM

## Solution 5
This solution refers to the full diagram in Solution 4.
Note the $\text{Q}$ diagonals are symmetric. The $\text{R}$ and $\text{P}$ diagonals are not symmetric, but are reflections of each other about the $\text{Q}$ diagonals:
When looking at a pair of $Q$ diagonals of the same length $x,$ there is a total of $2x$ $\text{R}$ s and $\text{P}$ s next to these $2$ diagonals.
The main diagonal of $20$ $\text{Q}$ s has $19$ $\text{P}$ s and $19$ $\text{R}$ s next to it. Thus, the total is $x+1$ $\text{Q}$ s, $x$ $\text{P}$ s, $x$ $\text{R}$ s. Therefore, the answer is $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}.$
~ERMSCoach

## Solution 6 (Modular Arithmetic)
If a letter is in a horizontal position $k$ , then that same letter will appear in position $k+3m$ , for a positive integer $m$ . In other words, all positions congruent to $k$ modulo $3$ will have the same letter as $p$ .
Since $p$ is in position $1$ , $p$ will be in every position congruent to $1 \pmod 3$ . There are $7$ numbers less than or equal to $20$ that satisfy this restraint. There are also $7$ numbers less than or equal to $2$ that are congruent to $2 \pmod 3$ , but only $6$ that are multiples of $3$ .
In $p$ 's case, it will appear $7$ times in row one, only $6$ in row $2$ (as its first appearance is in position $3$ ), and $7$ in row $3$ . So in the first $3$ rows, $P$ appears $20$ times.
Therefore, in the first $18$ rows, $P$ appears $20\cdot 6 = 120$ times. Row $19$ looks identical to row $1$ , as $19\equiv 1\pmod 3$ , so $P$ appears in row $19$ $7$ times. It follows that $P$ appears in row $20$ $6$ times. There are $134 P$ s.
Counting $Q$ s is nearly identical, but $Q$ begins in position $2$ . In the first $18$ rows, there are an identical amount of $Q$ s too, namely $6(7+7+6) = 120$ . However, by a similar argument to $P$ , $Q$ appears $7+7$ times in the last two rows; because row $20$ is the same as row $2$ , $Q$ appears in position $1$ , and thus $7$ times.
Therefore, there are $120+14 = 134$ $Q$ s and $133$ $P$ . We could go through a similar argument for $R$ , or note that the only answer choice with these two options is $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}.$
-Benedict T (countmath1)

## Solution 7 (Answer Choices, Fast)
We can first observe that $P$ shows on diagonals increasing or decreasing by $3.$
It starts at $1,4,7,9...$ and increases in the form $3x-2$ . Using our answer choices, $(B)$ and $(C)$ are the only fits.
$Q$ is like this as well, increasing $2,5,8,11....$ This means $Q$ has to be in the form of $3x-1.$ Testing this out leads us with $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}.$
~andyluo

## Solution 8 (Intuitive, Fastest)
When we find the letters at the corners, we see that there are 2 other corners with Q's and 1 with R. There are 2 corners with Q and 1 with P and R. Therefore, it makes sense that there should be more Q's than other letters. Only $\boxed{\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}}$ has more Q's than other letters.
Only do it this way if there are 30 seconds left on the clock, as it may not always work!

## Solution 9 (Think and Label)
Since there are $3$ letters, there must be a multiple of 3 for the height of the array for the amount of letters to be the same. However, there is one less ( $21-1=20$ ) so there will be one less letter in each column compared to the other two. Looking at the diagram, the first column starts with a $P$ then a $Q$ . Since it will miss the third letter, $R$ , we write this as $-R$ . We do this process for the remaining 20 columns, and applying the same logic if the first three are $-R$ , $-P$ and $-Q$ , there will be one less $-Q$ meaning that there will be an extra $Q$ . The only answer that has in extra $Q$ is $\textbf{(C)}~133\text{ Ps, }134\text{ Qs, }133\text{ Rs}$
~Blue_Kite

## Video Solution 1 by Math-X
https://youtu.be/Ku_c1YHnLt0?si=Xxe3CXtrXQYGSYik&t=3081

## Video Solution 2 by CoolMathProblems
https://youtu.be/_huZfhiCBN8

## Video Solution 3 by hnsacademy
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=1453

## Video Solution 4
https://youtu.be/3DTwjLe0Pw0
~Education, the Study of Everything

## Video Solution 5
https://youtu.be/1tnMR0lNEFY
~ Star League

## Video Solution 6 by OmegaLearn (Using Cyclic Patterns)
https://youtu.be/83FnFhe4QgQ

## Video Solution 7 by Magic Square
https://youtu.be/-N46BeEKaCQ?t=3990

## Video Solution 8 by Interstigation
https://youtu.be/DBqko2xATxs&t=1845

## Video Solution 9 by WhyMath
https://youtu.be/iMhqlz0-ce0

## Video Solution 10
https://www.youtube.com/watch?v=jtHe6yLBz-4&t=20s

## Video Solution 11 by Dr. David
https://youtu.be/yeXuFQHYU7k
### See Also