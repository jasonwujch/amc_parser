# 2022 AMC 10B Problem 12

## Problem

A pair of fair $6$ -sided dice is rolled $n$ times. What is the least value of $n$ such that the probability that the sum of the numbers face up on a roll equals $7$ at least once is greater than $\frac{1}{2}$ ?

$\textbf{(A) } 2 \qquad \textbf{(B) } 3 \qquad \textbf{(C) } 4 \qquad \textbf{(D) } 5 \qquad \textbf{(E) } 6$

## Solution 1 (Complement)
Rolling a pair of fair $6$ -sided dice, the probability of getting a sum of $7$ is $\frac16:$ Regardless what the first die shows, the second die has exactly one outcome to make the sum $7.$ We consider the complement: The probability of not getting a sum of $7$ is $1-\frac16=\frac56.$ Rolling the pair of dice $n$ times, the probability of getting a sum of $7$ at least once is $1-\left(\frac56\right)^n.$
Therefore, we have $1-\left(\frac56\right)^n>\frac12,$ or \[\left(\frac56\right)^n<\frac12.\] Since $\left(\frac56\right)^4<\frac12<\left(\frac56\right)^3,$ the least integer $n$ satisfying the inequality is $\boxed{\textbf{(C) } 4}.$
~MRENTHUSIASM

## Solution 2 (Fakesolve)
Let's try the answer choices. We can quickly find that when we roll $3$ dice, either the first and second sum to $7$ , the first and third sum to $7$ , or the second and third sum to $7$ . There are $6$ ways for the first and second dice to sum to $7$ , $6$ ways for the first and third to sum to $7$ , and $6$ ways for the second and third dice to sum to $7$ . However, we overcounted (but not by much) so we can assume that the answer is $\boxed {\textbf{(C) }4}$ .
~Arcticturn

## Solution 3 (Fakesolve)
We can start by figuring out what the probability is for each die to add up to $7$ if there is only $1$ roll. We can quickly see that the probability is $\frac16$ , as there are $6$ ways to make $7$ from $2$ numbers on a die, and there are a total of $36$ ways to add $2$ numbers on a die. And since each time we roll the dice, we are adding to the probability, we can conclude that the total probability for rolling a sum of $7$ in $n$ rolls would be $\frac16$ $n$ . The smallest number that satisfies this is $\boxed {\textbf{(C) }4}$ .
~mihikamishra

## Solution 4 (Fakesolve)
On each roll, there is a $\frac 16$ chance of rolling a sum of $7$ . You would need $4$ of these rolls to get $4 \cdot \frac 16,$ which is larger than $\frac 12.$ Therefore, the answer is $\boxed {\textbf{(C) }4}.$
~dbnl

## Video Solution (⚡️Just 4 min⚡️)
https://youtu.be/rYyb3NCWBXk
~Education, the Study of Everything

## Video Solution by Interstigation
https://youtu.be/qT0hVzy7zeY

## Video Solution by TheBeautyofMath
https://youtu.be/Mi2AxPhnRno?t=207
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .