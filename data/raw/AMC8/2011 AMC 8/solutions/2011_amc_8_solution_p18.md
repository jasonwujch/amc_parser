# 2011 AMC 8 Problem 18

## Problem

A fair $6$ sided die is rolled twice. What is the probability that the first number that comes up is greater than or equal to the second number?

$\textbf{(A) }\dfrac16\qquad\textbf{(B) }\dfrac5{12}\qquad\textbf{(C) }\dfrac12\qquad\textbf{(D) }\dfrac7{12}\qquad\textbf{(E) }\dfrac56$

## Solution
There are $6\cdot6=36$ ways to roll the two dice, and 6 of them result in two of the same number. Out of the remaining $36-6=30$ ways, the number of rolls where the first dice is greater than the second should be the same as the number of rolls where the second dice is greater than the first. In other words, there are $30/2=15$ ways the first roll can be greater than the second. The probability the first number is greater than or equal to the second number is
\[\frac{15+6}{36}=\frac{21}{36}=\boxed{\textbf{(D)}\ \frac{7}{12}}\]

## Solution 2
If we list out some ways the first dice is greater than the second dice, we might see a pattern.
If dice $2$ is $1$ , then dice $1$ can be $1, 2, 3, 4, 5,$ or $6$ .
If dice $2$ is $2$ , then dice $1$ can be $2, 3, 4, 5,$ or $6$ .
If dice $2$ is $3$ , then dice $1$ can be $3, 4, 5,$ or $6$ .
In the first case, dice $1$ had six values it could land on. In the second case, dice $1$ had five values it could land on. In the third case, dice $1$ had four values it could land on. If we keep going, we would eventually get the pattern $6+5+4+3+2+1=21$ as the number of total values dice $1$ could land on if it's greater or equal to dice $2$ . Since there are $36$ ways two dice could land, our answer is $\frac{21}{36}$ , or $\boxed{\textbf{(D)} \frac{7}{12}}$ .

## Video Solution by OmegaLearn
https://youtu.be/6xNkyDgIhEE?t=139
~ pi_is_3.14

## Video Solution
https://youtu.be/lfrofNkOol0 . Soo, DRMS, NM

## Video Solution by WhyMath
https://youtu.be/OWrMcByO3QQ
~savannahsolver

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=mYn6tNxrWBU
### See Also