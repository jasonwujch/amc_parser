# 2009 AIME I Problem 3

## Problem

A coin that comes up heads with probability $p > 0$ and tails with probability $1 - p > 0$ independently on each flip is flipped $8$ times. Suppose that the probability of three heads and five tails is equal to $\frac {1}{25}$ of the probability of five heads and three tails. Let $p = \frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
The probability of three heads and five tails is $\binom {8}{3}p^3(1-p)^5$ and the probability of five heads and three tails is $\binom {8}{3}p^5(1-p)^3$ .
\begin{align*} 25\binom {8}{3}p^3(1-p)^5&=\binom {8}{3}p^5(1-p)^3 \\ 25(1-p)^2&=p^2 \\ 25p^2-50p+25&=p^2 \\ 24p^2-50p+25&=0 \\ p&=\frac {5}{6}\end{align*}
Therefore, the answer is $5+6=\boxed{011}$ .

## Solution 2
We start as shown above. However, when we get to $25(1-p)^2=p^2$ , we square root both sides to get $5(1-p)=p$ . We can do this because we know that both $p$ and $1-p$ are between $0$ and $1$ , so they are both positive. Now, we have:
\begin{align*} 5(1-p)&=p \\ 5-5p&=p \\ 5&=6p \\ p&=\frac {5}{6}\end{align*}
Now, we get $5+6=\boxed{011}$ .
~Jerry_Guo

## Solution 3
Rewrite it as : $(P)^3$ $(1-P)^5=\frac {1}{25}$ $(P)^5$ $(1-P)^3$
This can be simplified as $24P^2 -50P + 25 = 0$
This can be factored into $(4P-5)(6P-5)$
This yields two solutions: $\frac54$ (ignored because it would result in $1-p<0$ ) or $\frac56$
Therefore, the answer is $5+6$ = $\boxed {011}$

## Video Solution
https://youtu.be/NL79UexadzE
~IceMatrix

## Video Solution 2
https://www.youtube.com/watch?v=P00iOJdQiL4
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.