# 2025 AMC 8 Problem 16

## Problem

Five distinct integers from $1$ to $10$ are chosen, and five distinct integers from $11$ to $20$ are chosen. No two numbers differ by exactly $10$ . What is the sum of the ten chosen numbers?

$\textbf{(A)}\ 95 \qquad \textbf{(B)}\ 100 \qquad \textbf{(C)}\ 105 \qquad \textbf{(D)}\ 110 \qquad \textbf{(E)}\ 115$

## Solution
Note that for no two numbers to differ by , every number chosen must have a different units digit . To make computations easier, we can choose $(1, 2, 3, 4, 5)$ from the first group and $(16, 17, 18, 19, 20)$ from the second group. Then the sum evaluates to $1+2+3+4+5+16+17+18+19+20 = \boxed{\text{(C)\ 105}}$ .
~Soupboy0
### Another Way To Compute
For $1+2+3+4+5+16+17+18+19+20$ , we can add the first term and the last term, which is $21$ . If we add the second term and the second-to-last term it is also $21$ . There are $5$ pairs that sum to $21$ , so the answer is $21 \times 5$ which equals $\boxed{\text{(C)\ 105}}$ .
- leafy

## Similar solution
One efficient method is to quickly add $(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)$ , which is $55$ . Then because you took $50$ in total away from $(16, 17, 18, 19, 20)$ , you add $50$ . $55+50= \boxed{\text{(C)\ 105}}$ .
~Bepin999

## Solution 4 (effecient)
To solve this problem, I started with the easiest/smallest case possible. In my opinion, that was
$1+2+3+4+5+16+17+18+19+20$ .
I then solved this equation quickly using Little Gauss's method, rearranging that into
$1+19+2+18+3+17+4+16+5+20$ .
I simplified this into
$20+20+20+20+25$ .
Solving this simple equation gives us the answer, which is $\boxed{\text{(C)\ 105}}$ .
~Kapurnicus
~Minor edit by NYCnerd

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC

## Video Solution by Pi Academy
https://youtu.be/Iv_a3Rz725w?si=E0SI_h1XT8msWgkK

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=DtG8sG4CK4RrUlVz&t=1815 ~hsnacademy

## Video Solution by Thinking Feet
https://youtu.be/PKMpTS6b988
### See Also