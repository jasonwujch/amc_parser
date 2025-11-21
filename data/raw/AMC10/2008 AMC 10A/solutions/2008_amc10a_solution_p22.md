# 2008 AMC 10A Problem 22

## Problem

Jacob uses the following procedure to write down a sequence of numbers. First he chooses the first term to be 6. To generate each succeeding term, he flips a fair coin. If it comes up heads, he doubles the previous term and subtracts 1. If it comes up tails, he takes half of the previous term and subtracts 1. What is the probability that the fourth term in Jacob's sequence is an integer ?

$\mathrm{(A)}\ \frac{1}{6}\qquad\mathrm{(B)}\ \frac{1}{3}\qquad\mathrm{(C)}\ \frac{1}{2}\qquad\mathrm{(D)}\ \frac{5}{8}\qquad\mathrm{(E)}\ \frac{3}{4}$

## Solution 1
We construct a tree showing all possible outcomes that Jacob may get after $3$ flips; we can do this because there are only $8$ possibilities: \[6\quad\begin{cases} \ \text{H}: 11 &\quad \begin{cases} \ \text{H}: 21 &\quad \begin{cases} \ \text{H}: \boxed{41}\\ \ \text{T}: 9.5 \end{cases}\\ \ \text{T}: 4.5 &\quad \begin{cases} \ \text{H}: \boxed{8}\\ \ \text{T}: 1.25 \end{cases} \end{cases}\\ \ \text{T}: 2 &\quad \begin{cases} \ \text{H}: 3 &\qquad\! \begin{cases} \ \text{H}: \boxed{5}\\ \ \text{T}: 0.5 \end{cases}\\ \ \text{T}: 0 &\qquad\! \begin{cases} \ \text{H}: \boxed{-1}\\ \ \text{T}: \boxed{-1} \end{cases} \end{cases} \end{cases}\] There is a $\frac{5}{8}$ chance that the fourth term in Jacob's sequence is an integer, so the answer is $\mathrm{(D)}$ .

## Solution 2
We can see that as long as the last flip is heads, it will be an integer, so there is a $\dfrac{1}{2}$ chance of this happening.
Doing a little casework, we see that the only possibility when the last flip is tails is when the third flip brings it to 0. There is a $\dfrac{1}{8}$ chance of this happening.
Therefore, there is a $\dfrac{1}{2}+\dfrac{1}{8}=\boxed{(D)\dfrac{5}{8}}$ possibility of ending with an integer.
~nezha33

## Video Solution
https://youtu.be/2GLV1flwtUQ
~savannahsolver
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .