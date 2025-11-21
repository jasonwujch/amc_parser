# 2023 AMC 8 Problem 7

## Problem

A rectangle, with sides parallel to the $x$ -axis and $y$ -axis, has opposite vertices located at $(15, 3)$ and $(16, 5)$ . A line is drawn through points $A(0, 0)$ and $B(3, 1)$ . Another line is drawn through points $C(0, 10)$ and $D(2, 9)$ . How many points on the rectangle lie on at least one of the two lines? [asy] usepackage("mathptmx"); size(9cm); draw((0,-.5)--(0,11),EndArrow(size=.15cm)); draw((1,0)--(1,11),mediumgray); draw((2,0)--(2,11),mediumgray); draw((3,0)--(3,11),mediumgray); draw((4,0)--(4,11),mediumgray); draw((5,0)--(5,11),mediumgray); draw((6,0)--(6,11),mediumgray); draw((7,0)--(7,11),mediumgray); draw((8,0)--(8,11),mediumgray); draw((9,0)--(9,11),mediumgray); draw((10,0)--(10,11),mediumgray); draw((11,0)--(11,11),mediumgray); draw((12,0)--(12,11),mediumgray); draw((13,0)--(13,11),mediumgray); draw((14,0)--(14,11),mediumgray); draw((15,0)--(15,11),mediumgray); draw((16,0)--(16,11),mediumgray); draw((-.5,0)--(17,0),EndArrow(size=.15cm)); draw((0,1)--(17,1),mediumgray); draw((0,2)--(17,2),mediumgray); draw((0,3)--(17,3),mediumgray); draw((0,4)--(17,4),mediumgray); draw((0,5)--(17,5),mediumgray); draw((0,6)--(17,6),mediumgray); draw((0,7)--(17,7),mediumgray); draw((0,8)--(17,8),mediumgray); draw((0,9)--(17,9),mediumgray); draw((0,10)--(17,10),mediumgray); draw((-.13,1)--(.13,1)); draw((-.13,2)--(.13,2)); draw((-.13,3)--(.13,3)); draw((-.13,4)--(.13,4)); draw((-.13,5)--(.13,5)); draw((-.13,6)--(.13,6)); draw((-.13,7)--(.13,7)); draw((-.13,8)--(.13,8)); draw((-.13,9)--(.13,9)); draw((-.13,10)--(.13,10)); draw((1,-.13)--(1,.13)); draw((2,-.13)--(2,.13)); draw((3,-.13)--(3,.13)); draw((4,-.13)--(4,.13)); draw((5,-.13)--(5,.13)); draw((6,-.13)--(6,.13)); draw((7,-.13)--(7,.13)); draw((8,-.13)--(8,.13)); draw((9,-.13)--(9,.13)); draw((10,-.13)--(10,.13)); draw((11,-.13)--(11,.13)); draw((12,-.13)--(12,.13)); draw((13,-.13)--(13,.13)); draw((14,-.13)--(14,.13)); draw((15,-.13)--(15,.13)); draw((16,-.13)--(16,.13)); label(scale(.7)*"$1$", (1,-.13), S); label(scale(.7)*"$2$", (2,-.13), S); label(scale(.7)*"$3$", (3,-.13), S); label(scale(.7)*"$4$", (4,-.13), S); label(scale(.7)*"$5$", (5,-.13), S); label(scale(.7)*"$6$", (6,-.13), S); label(scale(.7)*"$7$", (7,-.13), S); label(scale(.7)*"$8$", (8,-.13), S); label(scale(.7)*"$9$", (9,-.13), S); label(scale(.7)*"$10$", (10,-.13), S); label(scale(.7)*"$11$", (11,-.13), S); label(scale(.7)*"$12$", (12,-.13), S); label(scale(.7)*"$13$", (13,-.13), S); label(scale(.7)*"$14$", (14,-.13), S); label(scale(.7)*"$15$", (15,-.13), S); label(scale(.7)*"$16$", (16,-.13), S); label(scale(.7)*"$1$", (-.13,1), W); label(scale(.7)*"$2$", (-.13,2), W); label(scale(.7)*"$3$", (-.13,3), W); label(scale(.7)*"$4$", (-.13,4), W); label(scale(.7)*"$5$", (-.13,5), W); label(scale(.7)*"$6$", (-.13,6), W); label(scale(.7)*"$7$", (-.13,7), W); label(scale(.7)*"$8$", (-.13,8), W); label(scale(.7)*"$9$", (-.13,9), W); label(scale(.7)*"$10$", (-.13,10), W); dot((0,0),linewidth(4)); label(scale(.75)*"$A$", (0,0), NE); dot((3,1),linewidth(4)); label(scale(.75)*"$B$", (3,1), NE); dot((0,10),linewidth(4)); label(scale(.75)*"$C$", (0,10), NE); dot((2,9),linewidth(4)); label(scale(.75)*"$D$", (2,9), NE); draw((15,3)--(16,3)--(16,5)--(15,5)--cycle,linewidth(1.125)); dot((15,3),linewidth(4)); dot((16,3),linewidth(4)); dot((16,5),linewidth(4)); dot((15,5),linewidth(4)); [/asy] $\textbf{(A)}\ 0 \qquad \textbf{(B)}\ 1 \qquad \textbf{(C)}\ 2 \qquad \textbf{(D)}\ 3 \qquad \textbf{(E)}\ 4$

## Solution 1
If we extend the lines, we have the following diagram: [asy] usepackage("mathptmx"); size(9cm); draw((0,-.5)--(0,11),EndArrow(size=.15cm)); draw((1,0)--(1,11),mediumgray); draw((2,0)--(2,11),mediumgray); draw((3,0)--(3,11),mediumgray); draw((4,0)--(4,11),mediumgray); draw((5,0)--(5,11),mediumgray); draw((6,0)--(6,11),mediumgray); draw((7,0)--(7,11),mediumgray); draw((8,0)--(8,11),mediumgray); draw((9,0)--(9,11),mediumgray); draw((10,0)--(10,11),mediumgray); draw((11,0)--(11,11),mediumgray); draw((12,0)--(12,11),mediumgray); draw((13,0)--(13,11),mediumgray); draw((14,0)--(14,11),mediumgray); draw((15,0)--(15,11),mediumgray); draw((16,0)--(16,11),mediumgray); draw((-.5,0)--(17,0),EndArrow(size=.15cm)); draw((0,1)--(17,1),mediumgray); draw((0,2)--(17,2),mediumgray); draw((0,3)--(17,3),mediumgray); draw((0,4)--(17,4),mediumgray); draw((0,5)--(17,5),mediumgray); draw((0,6)--(17,6),mediumgray); draw((0,7)--(17,7),mediumgray); draw((0,8)--(17,8),mediumgray); draw((0,9)--(17,9),mediumgray); draw((0,10)--(17,10),mediumgray); draw((-.13,1)--(.13,1)); draw((-.13,2)--(.13,2)); draw((-.13,3)--(.13,3)); draw((-.13,4)--(.13,4)); draw((-.13,5)--(.13,5)); draw((-.13,6)--(.13,6)); draw((-.13,7)--(.13,7)); draw((-.13,8)--(.13,8)); draw((-.13,9)--(.13,9)); draw((-.13,10)--(.13,10)); draw((1,-.13)--(1,.13)); draw((2,-.13)--(2,.13)); draw((3,-.13)--(3,.13)); draw((4,-.13)--(4,.13)); draw((5,-.13)--(5,.13)); draw((6,-.13)--(6,.13)); draw((7,-.13)--(7,.13)); draw((8,-.13)--(8,.13)); draw((9,-.13)--(9,.13)); draw((10,-.13)--(10,.13)); draw((11,-.13)--(11,.13)); draw((12,-.13)--(12,.13)); draw((13,-.13)--(13,.13)); draw((14,-.13)--(14,.13)); draw((15,-.13)--(15,.13)); draw((16,-.13)--(16,.13)); label(scale(.7)*"$1$", (1,-.13), S); label(scale(.7)*"$2$", (2,-.13), S); label(scale(.7)*"$3$", (3,-.13), S); label(scale(.7)*"$4$", (4,-.13), S); label(scale(.7)*"$5$", (5,-.13), S); label(scale(.7)*"$6$", (6,-.13), S); label(scale(.7)*"$7$", (7,-.13), S); label(scale(.7)*"$8$", (8,-.13), S); label(scale(.7)*"$9$", (9,-.13), S); label(scale(.7)*"$10$", (10,-.13), S); label(scale(.7)*"$11$", (11,-.13), S); label(scale(.7)*"$12$", (12,-.13), S); label(scale(.7)*"$13$", (13,-.13), S); label(scale(.7)*"$14$", (14,-.13), S); label(scale(.7)*"$15$", (15,-.13), S); label(scale(.7)*"$16$", (16,-.13), S); label(scale(.7)*"$1$", (-.13,1), W); label(scale(.7)*"$2$", (-.13,2), W); label(scale(.7)*"$3$", (-.13,3), W); label(scale(.7)*"$4$", (-.13,4), W); label(scale(.7)*"$5$", (-.13,5), W); label(scale(.7)*"$6$", (-.13,6), W); label(scale(.7)*"$7$", (-.13,7), W); label(scale(.7)*"$8$", (-.13,8), W); label(scale(.7)*"$9$", (-.13,9), W); label(scale(.7)*"$10$", (-.13,10), W); draw((0,10)--(17,1.5),blue); draw((0,0)--(17,17/3),blue); dot((0,0),linewidth(4)); label(scale(.75)*"$A$", (0,0), NE); dot((3,1),linewidth(4)); label(scale(.75)*"$B$", (3,1), NE); dot((0,10),linewidth(4)); label(scale(.75)*"$C$", (0,10), NE); dot((2,9),linewidth(4)); label(scale(.75)*"$D$", (2,9), NE); draw((15,3)--(16,3)--(16,5)--(15,5)--cycle,linewidth(1.125)); dot((15,3),linewidth(4)); dot((16,3),linewidth(4)); dot((16,5),linewidth(4)); dot((15,5),linewidth(4)); [/asy] Therefore, we see that the answer is $\boxed{\textbf{(B)}\ 1}.$
~MrThinker

## Solution 2
Note that the $y$ -intercepts of line $AB$ and line $CD$ are $0$ and $10$ . If the analytic expression for line $AB$ is $y=k_{1}x$ , and the analytic expression for line $CD$ is $y=k_{2}x+10$ , we have equations: $3k_{1} = 1$ and $2k_{2} + 10 = 9$ . Solving these equations, we can find out that $k_{1} = \frac{1}{3}$ and $k_{2} = -\frac{1}{2}$ . Therefore, we can determine that the expression for line $AB$ is $y=\frac{1}{3}x$ and the expression for line $CD$ is $y=-\frac{1}{2}x + 10$ . When $x=15$ , the coordinates that line $AB$ and line $CD$ pass through are $(15, 5)$ and $\left(15, \frac{5}{2}\right)$ , and $(15, 5)$ lies perfectly on one vertex of the rectangle while the $y$ coordinate of $\left(15, \frac{5}{2}\right)$ is out of the range $3 \leq y \leq 5$ (lower than the bottom left corner of the rectangle $(15, 3)$ ). Considering that the $y$ value of the line $CD$ will only decrease, and the $y$ value of the line $AB$ will only increase, there will not be another point on the rectangle that lies on either of the two lines. Thus, we can conclude that the answer is $\boxed{\textbf{(B)}\ 1}.$
~ Bloggish

## Video Solution by CoolMathProblmes
https://youtu.be/Pf93RGtKo1I?feature=shared&t=436

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=362 ~hsnacademy

## Video Solution (How to CREATIVELY THINK!!!)
https://youtu.be/NUaes2N_4pM ~Education the Study of everything

## Video Solution by Math-X (Smart and Simple)
https://youtu.be/Ku_c1YHnLt0?si=P3DtuhzhiVr2Jv0r&t=947 ~Math-X

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=5151

## Video Solution
https://www.youtube.com/watch?v=EcrktBc8zrM&ab_channel=SpreadTheMathLove (@11:08)

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=534

## Video Solution by WhyMath
https://youtu.be/jCjF9duTQxk
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=35BW7bsm_Cg&t=778s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/LMeg3r3VFdE
### See Also