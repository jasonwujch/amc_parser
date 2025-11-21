# 2019 AMC 10A Problem 23

## Problem

Travis has to babysit the terrible Thompson triplets. Knowing that they love big numbers, Travis devises a counting game for them. First Tadd will say the number $1$ , then Todd must say the next two numbers ( $2$ and $3$ ), then Tucker must say the next three numbers ( $4$ , $5$ , $6$ ), then Tadd must say the next four numbers ( $7$ , $8$ , $9$ , $10$ ), and the process continues to rotate through the three children in order, each saying one more number than the previous child did, until the number $10,000$ is reached. What is the $2019$ th number said by Tadd?

$\textbf{(A)}\ 5743 \qquad\textbf{(B)}\ 5885 \qquad\textbf{(C)}\ 5979 \qquad\textbf{(D)}\ 6001 \qquad\textbf{(E)}\ 6011$

## Solution 1
Define a round as one complete rotation through each of the three children, and define a turn as the portion when one child says his numbers (similar to how a game is played).
We create a table to keep track of what numbers each child says for each round.
$\begin{tabular}{||c c c c||} \hline Round & Tadd & Todd & Tucker \\ [0.5ex] \hline\hline 1 & 1 & 2-3 & 4-6 \\ \hline 2 & 7-10 & 11-15 & 16-21 \\ \hline 3 & 22-28 & 29-36 & 37-45 \\ \hline 4 & 46-55 & 56-66 & 67-78 \\ [1ex] \hline \end{tabular}$
Tadd says $1$ number in round 1, $4$ numbers in round 2, $7$ numbers in round 3, and in general $3n - 2$ numbers in round n. At the end of round n, the number of numbers Tadd has said so far is $1 + 4 + 7 + \dots + (3n - 2) = \frac{n(3n-1)}{2}$ , by the sum of arithmetic series formula.
We find that $\dfrac{37(110)}{2}=2035$ , so Tadd says his 2035th number at the end of his turn in round 37. That also means that Tadd says his 2019th number in round 37. At the end of Tadd's turn in round 37, the children have, in total, completed $36+36+37=109$ turns. In general, at the end of turn $n$ , the nth triangular number is said, or $\dfrac{n(n+1)}{2}$ . So at the end of turn 109 (or the end of Tadd's turn in round 37), Tadd says the number $\dfrac{109(110)}{2}=5995$ . Recalling that this was the 2035th number said by Tadd, so the 2019th number he said was $5995-16=5979$ .
Thus, the answer is $\boxed{\textbf{(C) }5979}$ .

## Solution 2
Firstly, as in Solution 1, we list how many numbers Tadd says, Todd says, and Tucker says in each round.
Tadd: $1, 4, 7, 10, 13 \cdots$
Todd: $2, 5, 8, 11, 14 \cdots$
Tucker: $3, 6, 9, 12, 15 \cdots$
We can find a general formula for the number of numbers each of the kids say after the $n$ th round. For Tadd, we can either use the arithmetic series sum formula (like in Solution 1) or standard summation results to get $\sum_{i=1}^n 3n-2=-2n+3\sum_{i=1}^n n=-2n+\frac{3n(n+1)}{2}=\frac{3n^2-n}{2}$ .
Now, to find the number of rotations Tadd and his siblings go through before Tadd says his $2019$ th number, we know the inequality $\frac{3n^2-n}{2}<2019$ must be satisfied, and testing numbers gives the maximum integer value of $n$ as $36$ .
The next main insight, in order to simplify the computation process, is to notice that the $2019$ th number Tadd says is simply the number of numbers Todd and Tucker say plus the $2019$ Tadd says, which will be the answer since Tadd goes first.
Carrying out the calculation thus becomes quite simple:
\[\left(\sum_{i=1}^{36} 3n+\sum_{i=1}^{36} 3n-1\right)+2019=\left(\sum_{i=1}^{36} 6n-1\right)+2019=(5+11+17...+215)+2019=\frac{36(220)}{2}+2019\]
At this point, we can note that the last digit of the answer is $9$ , which gives $\boxed{\textbf{(C) }5979}$ . (Completing the calculation will confirm the answer, if you have time.)

## Solution 3
Think of a turn as adding a block or an interval of numbers to each person. Here are the first couple "blocks" that Tadd has (a block will be denoted in interval notation): [ $1$ ], [ $7$ - $10$ ], [ $22$ - $28$ ], [ $46$ - $55$ ]. From simple inspection, we can notice two things.
$1$ ) The start points of each interval is increasing arithmetically by $9$ .
$2$ ) The length of each "block" is increasing by $3$ .
Since each block length is increasing by 3, then we want $1$ + $4$ + $7$ +.. $3n-2$ = $2019$ or $n(3n-1)/2 = 2019$ , where $n$ is the amount of blocks we have. In a short amount of time, you will see that $n$ is not an integer from that equation, but thats perfectly okay since we can just find an $n$ that gets it close to 2019, then we can work from there. From inspection, you will see that a good n value that does that exact job is $37$ .
We can then deduce that the start point of the $37$ th block will be $1+(6+15+24..+321) = 5887$ if we refer to fact $1$ . We can easily find the length of 37th block by $36*3+1 = 109$ if we refer to fact $2$ . Remember that the length increases by $3$ for each block. So we then can deduce that our endpoint for the 37th block is $5887+109-1 = 5995$ . The endpoint of the $37$ th block will be the $2035$ th number said because we can plug $37$ into $n(3n-1)/2$ , which tells us how many numbers Tadd has said where $n$ is the number of blocks Tadd has. From there we know that the $2019$ th number is in $37$ th block, so that means we can take our endpoint and subtract $2035-2019 = 16$ from the endpoint of the $37$ th block, which is $5995$ , so we get $5995-16 = 5979$ or $\boxed{\textbf{(C) }5979}$ . ~~triggod

## Solution 4 (Logic)
Tadd first starts with number, says 4 numbers after, then 7, etc.
Notice how the difference between each one is 3, and therefore the total numbers said on each iteration would be $3x - 1$ . Obviouisly, $2019$ is unobtainable from the sum of the first $n$ numbers, so at most, we want another number that is an iteration of $3x$ . Therefore we want a number that satisfies both \( 2019 \mod 3 \equiv 0 \) and \( x \mod 3 \equiv 0 \).
The only number that works is $\boxed{\textbf{(C) }5979}$
~Pinotation
### Note
The statement that says that the max number is 10000 is pretty much useless. You can just ignore it, as it has no effect on the problem.

## Video Solutions

## Video Solution 1 By Richard Rusczyk
https://www.youtube.com/watch?v=xWma2YbSa30

## Video Solution 2 by TheBeautyofMath
https://youtu.be/gej8HVPXAS4?t=187
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .