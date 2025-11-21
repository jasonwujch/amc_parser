# 2021 Fall AMC 10A Problem 13

## Problem

Each of $6$ balls is randomly and independently painted either black or white with equal probability. What is the probability that every ball is different in color from more than half of the other $5$ balls?

$\textbf{(A) } \frac{1}{64}\qquad\textbf{(B) } \frac{1}{6}\qquad\textbf{(C) } \frac{1}{4}\qquad\textbf{(D) } \frac{5}{16}\qquad\textbf{(E) }\frac{1}{2}$

## Solution 1
Note that for this restriction to be true, there must be $3$ balls of each color. There are a total of $2^6 = 64$ ways to color the balls, and there are ${6 \choose 3} = 20$ ways for three balls chosen to be painted white. Thus, the answer is $\frac{20}{64} = \boxed{\textbf{(D) } \frac{5}{16}}$ .
-Aidensharp

## Solution 2
For this restriction to be upheld, there must be three black and three white balls. One such way for this to occur is the arrangement $BBBWWW$ , which has a $\frac{1}{2^6}$ probability of occuring. However, there are $\frac{6!}{3!\cdot{3!}}$ ways to arrange the three black and three white balls, meaning that the answer is, $\frac{1}{64}\cdot{\frac{6!}{3!\cdot{3!}}} = \boxed{\textbf{(D) } \frac{5}{16}}$ .
~Benedict T (countmath1)

## Solution 3
To get every ball different in color from more than half of the other 5 balls, we must have 3 black balls and 3 white balls.
Following from the binomial theorem, this happens with probability \[ \binom{6}{3} \left( \frac{1}{2} \right)^3 \left( 1 - \frac{1}{2} \right)^{6-3} = \frac{5}{16} . \]
Therefore, the answer is $\boxed{\textbf{(D) }\frac{5}{16}}$ .
~Steven Chen (www.professorchenedu.com)

## Video Solution
https://youtu.be/95aRRJ3jMqo
~Education, the Study of Everything

## Video Solution
https://youtu.be/zq3UPu4nwsE?t=707
~IceMatrix

## Video Solution by WhyMath
https://youtu.be/5m8zYiOagCY
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .