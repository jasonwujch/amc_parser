# 2000 AIME II Problem 3

## Problem

A deck of forty cards consists of four $1$ 's, four $2$ 's,..., and four $10$ 's. A matching pair (two cards with the same number) is removed from the deck. Given that these cards are not returned to the deck, let $m/n$ be the probability that two randomly selected cards also form a pair, where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

## Solution 1
There are ${38 \choose 2} = 703$ ways we can draw two cards from the reduced deck. The two cards will form a pair if both are one of the nine numbers that were not removed, which can happen in $9{4 \choose 2} = 54$ ways, or if the two cards are the remaining two cards of the number that was removed, which can happen in $1$ way. Thus, the answer is $\frac{54+1}{703} = \frac{55}{703}$ , and $m+n = \boxed{758}$ .

## Solution 2
Instead of counting the cases and doing $\frac{\text{cases wanted}}{\text{total amount of cases}}$ we can use probability directly.
For sake of simplicity, WLOG, assume that a pair of ones were removed from the deck of forty cards. We can split it into two cases:
Case 1: The pair is ones.
The probability that a one is chosen is $\frac{2}{38}.$ The probability that a second one is chosen is $\frac{1}{37}$ because one card was removed. Therefore, the probability that the pair is ones is $\frac{2}{38} \cdot \frac{1}{37}.$
Case 2: The pair is $2-10.$
The probability that any other number is chosen is $\frac{36}{38}.$ The probability that a number that is equal to this number is chosen (for example, if two was chosen originally then another two being chosen) is $\frac{3}{37}.$ Therefore, the probability that the pair is $2-10$ is $\frac{36}{38} \cdot \frac{3}{37}.$
Adding these two probabilities gives $\frac{2}{38} \cdot \frac{1}{37} + \frac{36}{38} \cdot \frac{3}{37} = \frac{110}{38 \cdot 37} = \frac{55}{703}$ , and $m+n = \boxed{758}.$

## Video Solution by OmegaLearn
https://youtu.be/mIJ8VMuuVvA?t=59
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.