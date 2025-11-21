# 2022 AMC 8 Problem 21

## Problem

Steph scored $15$ baskets out of $20$ attempts in the first half of a game, and $10$ baskets out of $10$ attempts in the second half. Candace took $12$ attempts in the first half and $18$ attempts in the second. In each half, Steph scored a higher percentage of baskets than Candace. Surprisingly they ended with the same overall percentage of baskets scored. How many more baskets did Candace score in the second half than in the first?

[asy] size(7cm); draw((-8,27)--(72,27)); draw((16,0)--(16,35)); draw((40,0)--(40,35)); label("12", (28,3)); draw((25,6.5)--(25,12)--(31,12)--(31,6.5)--cycle); draw((25,5.5)--(31,5.5)); label("18", (56,3)); draw((53,6.5)--(53,12)--(59,12)--(59,6.5)--cycle); draw((53,5.5)--(59,5.5)); draw((53,5.5)--(59,5.5)); label("20", (28,18)); label("15", (28,24)); draw((25,21)--(31,21)); label("10", (56,18)); label("10", (56,24)); draw((53,21)--(59,21)); label("First Half", (28,31)); label("Second Half", (56,31)); label("Candace", (2.35,6)); label("Steph", (0,21)); [/asy] $\textbf{(A) } 7\qquad\textbf{(B) } 8\qquad\textbf{(C) } 9\qquad\textbf{(D) } 10\qquad\textbf{(E) } 11$

## Solution 1 (Inequalities)
Let $x$ be the number of shots that Candace made in the first half, and let $y$ be the number of shots Candace made in the second half. Since Candace and Steph took the same number of attempts, with an equal percentage of baskets scored, we have $x+y=10+15=25.$ In addition, we have the following inequalities: \[\frac{x}{12}<\frac{15}{20} \implies x<9,\] and \[\frac{y}{18}<\frac{10}{10} \implies y<18.\] Pairing this up with $x+y=25$ we see the only possible solution is $(x,y)=(8,17),$ for an answer of $17-8 = \boxed{\textbf{(C) } 9}.$
~wamofan

## Solution 2 (Answer Choices)
Clearly, Steph made $15 + 10 = 25$ shots in total. Also, due to parity reasons, the difference between the amount of shots Candace made in the first and second half must be odd. Thus, we can just test 7, 9, and 11, and after doing so we find that the answer is $\boxed{\textbf{(C) } 9}.$

## Solution 3 (Cheap but overpowered)
Steph made 75 percent of his shots in the first half. He makes all of his shots in the second half. The most baskets Candace could have made in the first half is 8 baskets. The most she could have made in the second half is 17 baskets. Steph makes 25 and misses 5 baskets and the only way for Candace to make 25 shots is to make 8 in the first half and 17 in the second. Thus, $17 - 8 = \boxed{\textbf{(C) } 9}.$

## Video Solution 1
~hsnacademy

## Video Solution 2
~Math-X

## Video Solution 3
https://youtu.be/MKzyAvby_HQ
~Education, the Study of Everything

## Video Solution 4
https://youtu.be/QF9iZEjQ4AI

## Video Solution
~ Omegalearn

## Video Solution
https://www.youtube.com/watch?v=IbsSecIq8FE
~Mathematical Dexterity

## Video Solution
https://youtu.be/Ij9pAy6tQSg?t=1995
~Interstigation

## Video Solution
https://www.youtube.com/watch?v=nXHHM1884Jo
~David

## Video Solution
https://youtu.be/0orAAUaLIO0
~STEMbreezy

## Video Solution
https://youtu.be/diWioLTXpYk
~savannahsolver

## Video Solution by Dr. David
https://youtu.be/whhYwdaedqs
### See Also