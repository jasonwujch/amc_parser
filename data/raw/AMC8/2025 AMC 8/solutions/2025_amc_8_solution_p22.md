# 2025 AMC 8 Problem 22

## Problem

A classroom has a row of 35 coat hooks. Paulina likes coats to be equally spaced, so that there is the same number of empty hooks before the first coat, after the last coat, and between every coat and the next one. Suppose there is at least 1 coat and at least 1 empty hook. How many different numbers of coats can satisfy Paulina's pattern?

An image is supposed to go here. You can help us out by creating one and editing it in. Thanks.

$\textbf{(A)}\ 2\qquad \textbf{(B)}\ 4\qquad \textbf{(C)}\ 5\qquad \textbf{(D)}\ 7\qquad \textbf{(E)}\ 9$

## Solution 1
Suppose there are $c$ coats on the rack. Notice that there are $c+1$ "gaps" formed by these coats, each of which must have the same number of empty spaces (say, $k$ ). Then the values $k$ and $c$ must satisfy $c+k(c+1)=35 \implies kc+k+c=35$ . We now use Simon's Favorite Factoring Trick as follows: \[kc+k+c=35\] \[\implies kc+k+c+1=36\] \[\implies (k+1)(c+1)=36\] Our only restrictions now are that $k>0 \implies k+1 > 1$ and $c>0 \implies c+1>1$ . Other than that, each factor pair of $36$ produces a valid solution $(k,c)$ , which in turn uniquely determines an arrangement. Since $36$ has $9$ factors, our answer is $9-2=\boxed{\textbf{(D)}~7}$ . ~cxsmi

## Solution 2
Say Paulina placed $n$ coats. That will divide the 35 hooks into $n+1$ spaces and $35-n$ empty hooks. Therefore, \[n+1|35-n.\] The values of $n$ that satisfy this are \[n\in{1,2,3,5,8,11,17}\] The answer is $\boxed{\text{(D) }7}$ .

## Solution 3
Let the number of empty hooks before the first coat be denoted as $n$ .
This means that there are $n$ empty hooks between all the coats. In every situation, there are $n + 1$ gaps, since $n$ cannot be zero.
To solve the problem, subtract $2n$ from 35 (accounting for the $n$ empty hooks at the beginning and $n$ empty hooks at the end). Then subtract 1 (for the first occupied hook). After that, divide the remaining number of hooks by $n + 1$ (the number of hooks between coats). We do this because the first occupied hook is always after $n$ hooks; we just need to check if the remaining hooks can be evenly divided by the number of gaps.
To clarify:
\begin{align*} 35 - 2n &= 33 \\ 33 - 1 &= 32 \\ \frac{32}{n + 1} &= 16 \end{align*}
Since 16 is an integer, this situation satisfies the conditions.
We can skip the the third step, as each time you add 1 to $n$ , it decreases by 2 from the previous situation.
\[\frac{30}{n + 1} = 16\]
This situation also satisfies the conditions.
Continue this process until the difference exceeds $35 - (2n + 1)$ . We find that 7 situations satisfy the conditions. Therefore, the answer is 7.
Note: This method is slow but easy to check and understand.
~ aoum

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=q76L7lqj8IXEUGuL&t=3152 ~hsnacademy

## Video Solution by Thinking Feet
https://youtu.be/PKMpTS6b988

## Video Solution by Dr. David
https://youtu.be/ZIBTG4XzETI
### See Also