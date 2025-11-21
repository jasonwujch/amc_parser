# 2006 AIME II Problem 11

## Problem

A sequence is defined as follows $a_1=a_2=a_3=1,$ and, for all positive integers $n, a_{n+3}=a_{n+2}+a_{n+1}+a_n.$ Given that $a_{28}=6090307, a_{29}=11201821,$ and $a_{30}=20603361,$ find the remainder when $\sum^{28}_{k=1} a_k$ is divided by 1000.

## Solutions

## Solution 1
Define the sum as $s$ . Since $a_n\ = a_{n + 3} - a_{n + 2} - a_{n + 1}$ , the sum will be:
Thus $s = \frac{a_{28} + a_{30}}{2}$ , and $a_{28},\,a_{30}$ are both given; the last four digits of their sum is $3668$ , and half of that is $1834$ . Therefore, the answer is $\boxed{834}$ .−

## Solution 2 (bash)
Since the problem only asks for the first 28 terms and we only need to calculate mod 1000, we simply bash the first 28 terms:
$a_{1}\equiv 1 \pmod {1000} \\ a_{2}\equiv 1 \pmod {1000} \\ a_{3}\equiv 1 \pmod {1000} \\ a_{4}\equiv 3 \pmod {1000} \\ a_{5}\equiv 5 \pmod {1000} \\ \cdots \\ a_{25} \equiv 793 \pmod {1000} \\ a_{26} \equiv 281 \pmod {1000} \\ a_{27} \equiv 233 \pmod {1000} \\ a_{28} \equiv 307 \pmod {1000}$
Adding all the residues shows the sum is congruent to $\boxed{834}$ mod $1000$ .
~ I-_-I

## Solution 3 (some guessing involved)/"Engineer's Induction"
All terms in the sequence are sums of previous terms, so the sum of all terms up to a certain point must be some linear combination of the first three terms. Also, we are given $a_{28}, a_{29},$ and $a_{30}$ , so we can guess that there is some way to use them in a formula. Namely, we guess that there exists some $p, q, r$ such that $\sum_{k=1}^{n}{a_k} = pa_n+qa_{n+1}+ra_{n+2}$ . From here, we list out the first few terms of the sequence and the cumulative sums, and with a little bit of substitution and algebra we see that $(p, q, r) = (\frac{1}{2}, 0, \frac{1}{2})$ , at least for the first few terms. From this, we have that $\sum_{k=1}^{28}{a_k} = \frac{a_{28}+a_{30}}{2} \equiv{\boxed{834}}\pmod {1000}$ .
Solution by zeroman; clarified by srisainandan6

## Solution 4 (if you did not know how to use the numbers given in the problem)
By the Chinese remainder theorem, each number under 1000 is uniquely determined by its mod 8 and mod 125.
We list a few terms of the sequence mod 8:
\[1,1,1,3,5,1,1,7,1,1,1,...\]
Therefore, the cycle repeats every 8 numbers, and each cycle has a sum of 4 mod 8. Therefore, the sum mod 8 is \[3 \cdot 4 + 1 + 1 + 1 + 3 = 2 \mod 8.\]
Denote \[s_n = \sum _{i=1} ^{n} a_i.\] It is easy to prove that $s_{n+3} = s_{n+2} + s_{n+1} + s_{n}.$
We write the sum ( $s_n$ ) of the first terms mod 125:
\[1,2,3,6,11,20,37,68,0,-20,48,28,56,7,91,29,2,-3,28,27,52,-18,61,-30,13,44,27,84.\]
Therefore the desired number is $84 \mod 125.$
From here, we can determine the number we are looking for is $750 + 84 = \boxed{834}.$ -sd8
These problems are copyrighted © by the Mathematical Association of America.