# 2013 AMC 8 Problem 8

## Problem

A fair coin is tossed 3 times. What is the probability of at least two consecutive heads?

$\textbf{(A)}\frac{1}{8} \qquad \textbf{(B)}\frac{1}{4} \qquad \textbf{(C)}\frac{3}{8} \qquad \textbf{(D)}\frac{1}{2} \qquad \textbf{(E)}\frac{3}{4}$

## Solution 1
There are $2^3 = 8$ ways to flip the coins, in order. There are two ways to get exactly two consecutive heads: HHT and THH. There is only one way to get three consecutive heads: HHH. Therefore, the probability of flipping at least two consecutive heads is $\boxed{\textbf{(C)}\frac{3}{8}}$ .

## Solution 2
Let's use complementary counting . To start with, the unfavorable outcomes (in this case, not getting 2 consecutive heads) are: TTT, HTH, and THT. The probability of these three outcomes is $\frac{1}{8}$ , $\frac{1}{4}$ , and $\frac{1}{4}$ , respectively. So the rest is exactly the probability of flipping at least two consecutive heads: $1-\frac{1}{8}-\frac{1}{4}-\frac{1}{4}=\frac{3}{8}$ . It is the answer $\boxed{\textbf{(C)}\frac{3}{8}}$ .
~LarryFlora

## Solution 3
We can list out all the ways to flip a coin three times: HHH,HHT,HTH,THH,HTT,THT,TTH,TTT. Out of them, only HHH,HHT,THH, have at least two consecutive heads. Since there are three ways to flip at least two consecutive heads, and eight total choices, the answer is $\boxed{\textbf{(C)}\frac{3}{8}}$ .
~andliu766

## Video Solution
https://youtu.be/2lynqd2bRZY ~savannahsolver https://youtu.be/6xNkyDgIhEE?t=44
~ pi_is_3.14
### See Also