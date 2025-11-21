# 2005 AIME II Problem 1

## Problem

A game uses a deck of $n$ different cards, where $n$ is an integer and $n \geq 6.$ The number of possible sets of 6 cards that can be drawn from the deck is 6 times the number of possible sets of 3 cards that can be drawn. Find $n.$

## Video Solution
https://youtu.be/IRyWOZQMTV8?t=150
~ pi_is_3.14

## Solution
The number of ways to draw six cards from $n$ is given by the binomial coefficient ${n \choose 6} = \frac{n\cdot(n-1)\cdot(n-2)\cdot(n-3)\cdot(n-4)\cdot(n-5)}{6\cdot5\cdot4\cdot3\cdot2\cdot1}$ .
The number of ways to choose three cards from $n$ is ${n\choose 3} = \frac{n\cdot(n-1)\cdot(n-2)}{3\cdot2\cdot1}$ .
We are given that ${n\choose 6} = 6 {n \choose 3}$ , so $\frac{n\cdot(n-1)\cdot(n-2)\cdot(n-3)\cdot(n-4)\cdot(n-5)}{6\cdot5\cdot4\cdot3\cdot2\cdot1} = 6 \frac{n\cdot(n-1)\cdot(n-2)}{3\cdot2\cdot1}$ .
Cancelling like terms, we get $(n - 3)(n - 4)(n - 5) = 720$ .
We must find a factorization of the left-hand side of this equation into three consecutive integers . Since 720 is close to $9^3=729$ , we try 8, 9, and 10, which works, so $n - 3 = 10$ and $n = \boxed{13}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.