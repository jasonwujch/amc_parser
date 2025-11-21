# 2003 AIME I Problem 14

## Problem

The decimal representation of $m/n,$ where $m$ and $n$ are relatively prime positive integers and $m < n,$ contains the digits $2, 5$ , and $1$ consecutively and in that order. Find the smallest value of $n$ for which this is possible.

## Solution
To find the smallest value of $n$ , we consider when the first three digits after the decimal point are $0.251\ldots$ .
Otherwise, suppose the number is in the form of $\frac{m}{n} = 0.X251 \ldots$ , where $X$ is a string of $k$ digits and $n$ is small as possible. Then $10^k \cdot \frac{m}{n} - X = \frac{10^k m - nX}{n} = 0.251 \ldots$ . Since $10^k m - nX$ is an integer and $\frac{10^k m - nX}{n}$ is a fraction between $0$ and $1$ , we can rewrite this as $\frac{10^k m - nX}{n} = \frac{p}{q}$ , where $q \le n$ . Then the fraction $\frac pq = 0.251 \ldots$ suffices.
Thus we have $\frac{m'}{n} = 0.251\ldots$ , or
As $4m' > n$ , we know that the minimum value of $4m' - n$ is $1$ ; hence we need $250 < 2n \Longrightarrow 125 < n$ . Since $4m' - n = 1$ , we need $n + 1$ to be divisible by $4$ , and this first occurs when $n = \boxed{ 127 }$ (note that if $4m'-n > 1$ , then $n > 250$ ). Indeed, this gives $m' = 32$ and the fraction $\frac {32}{127}\approx 0.25196 \ldots$ ).

## Solution 2
Rewrite the problem as having the smallest $n$ such that we can find an positive integer $m$ such that $0<\frac{m}{n}-\frac{251}{1000}<\frac{1}{1000}$ .
We can rewrite the expression as $\frac{1000m-251n}{1000n}$ , and we need $251n+x$ (where $x$ is the difference in the fraction, and ranging from (1,2,...n-1) to be $0$ mod $1000$ . We see that $n$ must be $3$ mod $4$ to have this happen (as this reduces the distance between the expression and $1000$ .
Rewriting $n$ as $4k+3$ , we get that $251(4k+3)+(4k+2)$ turns into $8k+755$ , and this has to be greater than or equal to $1000$ . The least $k$ that satisfies this is $31$ , and we consequently get that the least value of $n$ is $127$ . -dragoon -minor edits by Mathkiddie
These problems are copyrighted © by the Mathematical Association of America.