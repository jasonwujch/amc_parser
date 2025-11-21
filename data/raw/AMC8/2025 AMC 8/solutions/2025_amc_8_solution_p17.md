# 2025 AMC 8 Problem 17

## Problem

In the land of Markovia, there are three cities: $A$ , $B$ , and $C$ . There are 100 people who live in $A$ , 120 who live in $B$ , and 160 who live in $C$ . Everyone works in one of the three cities, and a person may work in the same city where they live. In the figure below, an arrow pointing from one city to another is labeled with the fraction of people living in the first city who work in the second city. (For example, $\frac{1}{4}$ of the people who live in $A$ work in $B$ .) How many people work in $A$ ?

[asy] import graph; unitsize(2cm); real r=0.15; pair A, B, C;B = (0,0);C = (2,0);A = (1,sqrt(3)); // Drawing the nodes draw(circle(A,r)); label("$A$", A); draw(circle(B,r)); label("$B$", B); draw(circle(C,r)); label("$C$", C); guide AB=A+r*dir(-135)..{down}B+r*dir(90), BA=B+r*dir(60)..{up}A+r*dir(-105), BC=B+r*dir(0)..(1,-0.2)..C+r*dir(180), CB=C+r*dir(150)..(1,0.3)..B+r*dir(30), CA=C+r*dir(90){up}..A+r*dir(-45), AC=A+r*dir(-75){down}..C+r*dir(120); draw(AB,L=Label("$1/4$", MidPoint, W),Arrow(HookHead)); draw(BA,L=Label("$1/3$", MidPoint, W),Arrow(HookHead)); draw(BC,L=Label("$1/6$", MidPoint, S),Arrow(HookHead)); draw(CB,L=Label("$1/10$", MidPoint, S),Arrow(HookHead)); draw(CA,L=Label("$1/8$", MidPoint, E),Arrow(HookHead)); draw(AC,L=Label("$1/5$", MidPoint, E),Arrow(HookHead)); [/asy]

$\textbf{(A)}\ 55\qquad \textbf{(B)}\ 60\qquad \textbf{(C)}\ 85\qquad \textbf{(D)}\ 115\qquad \textbf{(E)}\ 160$

## Solution 1
THere are $100 \cdot (\frac{1}{4} + \frac{1}{5}) = 100 \cdot \frac{9}{20} = 45$ people who do not work in city $A$ that live in city $A$ , meaning that $100 - 45 = 55$ people who live in city $A$ work in city $A$ . There are $\frac{1}{3} \cdot 120 = 40$ people who live in city $B$ and work in $A$ , as well as $\frac{1}{8} \cdot 160 = 20$ people who live in city $C$ that work in city $A$ . Therefore, the answer is $55 + 40 + 20 = \boxed{\textbf{(D)}\ 115}$ .
~ alwaysgonnagiveyouup
### Remark
This model is known as the Markov Chain , a type of stochastic process that models systems where the next state depends only on the current state, not on the sequence of events that preceded it. This is known as the Markov property (memoryless property).

## Video Solution by Pi Academy
https://youtu.be/Iv_a3Rz725w?si=E0SI_h1XT8msWgkK

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=fV-dPbMPVzWTkSV3&t=2020 ~hsnacademy

## Video Solution by Thinking Feet
https://youtu.be/PKMpTS6b988
### See Also