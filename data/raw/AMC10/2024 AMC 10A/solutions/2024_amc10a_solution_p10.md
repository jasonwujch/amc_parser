# 2024 AMC 10A Problem 10

## Problem

Consider the following operation. Given a positive integer $n$ , if $n$ is a multiple of $3$ , then you replace $n$ by $\frac{n}{3}$ . If $n$ is not a multiple of $3$ , then you replace $n$ by $n+10$ . Then continue this process. For example, beginning with $n=4$ , this procedure gives $4 \to 14 \to 24 \to 8 \to 18 \to 6 \to 2 \to 12 \to \cdots$ . Suppose you start with $n=100$ . What value results if you perform this operation exactly $100$ times?

$\textbf{(A) }10\qquad\textbf{(B) }20\qquad\textbf{(C) }30\qquad\textbf{(D) }40\qquad\textbf{(E) }50$

## Solution 1 (Fast Solution)
Let $s$ be the number of times the operation is performed. Notice the sequence goes $100 \to 110 \to 120 \to 40 \to 50 \to 60 \to 20 \to 30 \to 10 \to 20 \to \cdots$ . Thus, for $s \equiv 1 \pmod{3}$ , the value is $30$ . Since $100 \equiv 1 \pmod{3}$ , the answer is $\boxed{\textbf{(C) }30}$ .
~andliu766 ~minor fix by MID_HAT

## Solution 2 (More Explanatory)
Looking at the first few values of our operation, we get $100 \to 110 \to 120 \to 40 \to 50 \to 60 \to 20 \to 30 \to 10 \to 20$ . We can see that $30$ goes to $10$ , then to $20$ , then back to $30$ , and the loop resets. After 7 operations, we reach $30$ . We still have 93 operations left, so because the loop will run exactly $31$ times $(93/3)$ , we will reach $30$ again. So, the answer is $\boxed{\textbf{(C) } 30}$ .
~Moonwatcher22

## Solution 3 (very slightly different than previous)
Calculating the first few values, we get $100 \to 110 \to 120 \to 40 \to 50 \to 60 \to 20 \to 30 \to 10 \to 20$ . We can see that $20$ will go to $30$ , then to $10$ , then back to $20$ , and then the loop resets. After $6$ moves, we reach $20$ , the start of the cycle. We still have $100-5$ moves to go, so to find what number we land on after $95$ more steps, we can do $95 \pmod {3} \equiv (9 + 4) \pmod {3} = 1$ , meaning we go from $20 \to \boxed{\textbf{(C) } 30}$ .
~yuvag
~a lot of credit to Moonwatcher22

## Video Solution(Faster!)
https://youtu.be/l3VrUsZkv8I

## Video Solution by Pi Academy
https://youtu.be/6qYaJsgqkbs?si=K2Ebwqg-Ro8Yqoiv

## Video Solution 1 by Power Solve
https://youtu.be/wamtu7xm0eU

## Video Solution by Daily Dose of Math
https://youtu.be/17-o9qiprI0
~Thesmartgreekmathdude

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=_o5zagJVe1U

## Video Solution by Just Math⚡
https://www.youtube.com/watch?v=lqZUYJPq_Jo

## Video Solution by Dr. David
https://youtu.be/Q0LBITGGkGc

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=1547s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .