# 2013 AMC 10B Problem 12

## Problem

Let $S$ be the set of sides and diagonals of a regular pentagon. A pair of elements of $S$ are selected at random without replacement. What is the probability that the two chosen segments have the same length?

$\textbf{(A) }\frac{2}5\qquad\textbf{(B) }\frac{4}9\qquad\textbf{(C) }\frac{1}2\qquad\textbf{(D) }\frac{5}9\qquad\textbf{(E) }\frac{4}5$

## Solutions

## Solution 1
In a regular pentagon, there are 5 sides with the same length and 5 diagonals with the same length. Picking an element at random will leave 4 elements with the same length as the element picked, with 9 total elements remaining. Therefore, the probability is $\boxed{\textbf{(B) }\frac{4}{9}}$ .

## Solution 2
We can divide this problem into two cases. Case 1: Side; In this case, there is a $\frac{5}{10}$ chance of picking a side, and a $\frac{4}{9}$ chance of picking another side. Case 2: Diagonal; This case is similar to the first, for again, there is a $\frac{5}{10}$ chance of picking a diagonal, and a $\frac{4}{9}$ chance of picking another diagonal.
Summing these cases up gives us a probability of $\boxed{\textbf{(B) }\frac{4}{9}}$ .

## Solution 3
One way to do this is to use combinations. We know that there are $\binom{10}{2} = 45$ ways to select two segments. The ways in which you get 2 segments of the same length are if you choose two sides, or two diagonals. Thus, there are $2 \times \binom{5}{2}$ = 20 ways in which you end up with two segments of the same length. $\frac{20}{45}$ is equivalent to $\boxed{\textbf{(B) }\frac{4}{9}}$ .

## Solution 4
The problem is simply asking how many ways are there to choose two sides or two diagonals. Hence, the probability is \[\dfrac{\binom{5}{2} + \binom{5}{2}}{\binom{10}{2}} = \dfrac{10+10}{45} = \dfrac{20}{45}=\boxed{\textbf{(B) }\dfrac49}\] .
~MrThinker
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .