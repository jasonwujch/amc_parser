# 2008 AMC 10B Problem 17

## Problem

A poll shows that $70\%$ of all voters approve of the mayor's work. On three separate occasions a pollster selects a voter at random. What is the probability that on exactly one of these three occasions the voter approves of the mayor's work?

$\mathrm{(A)}\ {{{0.063}}} \qquad \mathrm{(B)}\ {{{0.189}}} \qquad \mathrm{(C)}\ {{{0.233}}} \qquad \mathrm{(D)}\ {{{0.333}}} \qquad \mathrm{(E)}\ {{{0.441}}}$

## Solution 1
Letting Y stand for a voter who approved of the work, and N stand for a person who didn't approve of the work, the pollster could select responses in $3$ different ways: $\text{YNN, NYN, and NNY}$ . The probability of each of these is $(0.7)(0.3)^2=0.063$ . Thus, the answer is $3\cdot0.063=0.189$ , or $\boxed{B}$

## Solution 2
In more concise terms, this problem is an extension of the binomial distribution. We find the number of ways only 1 person approves of the mayor multiplied by the probability 1 person approves and 2 people disapprove: ${3\choose 1} \cdot(0.7)^1\cdot(1-0.7)^{(3-1)}=3\cdot0.7\cdot0.09=\boxed{\mathrm{(B)}\ {{{0.189}}}}$

## Solution 3 (combinatorics)
The probability of getting the first voter to approve is $\frac{7}{10} * \frac{3}{10} * \frac{3}{10}$ .
This first voter, using combinations, can be arranged in 3 choose 1 ways, which simplifies into 3 ways.
Multiplying $3$ by $\frac{7}{10} * \frac{3}{10} * \frac{3}{10}$ gives (B).
~PeterDoesPhysics
PS: For a more challenging practice problem akin to this one, look to 2012 AMC 12A Problem 11.

## Video Solution by TheBeautyofMath
With explanation of how it helps on future problems, emphasizing "Don't Memorize, Understand" https://youtu.be/PO3XZaSchJc
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .