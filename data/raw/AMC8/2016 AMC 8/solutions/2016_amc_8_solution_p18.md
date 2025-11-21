# 2016 AMC 8 Problem 18

## Problem

In an All-Area track meet, $216$ sprinters enter a $100-$ meter dash competition. The track has $6$ lanes, so only $6$ sprinters can compete at a time. At the end of each race, the five non-winners are eliminated, and the winner will compete again in a later race. How many races are needed to determine the champion sprinter?

$\textbf{(A)}\mbox{ }36\qquad\textbf{(B)}\mbox{ }42\qquad\textbf{(C)}\mbox{ }43\qquad\textbf{(D)}\mbox{ }60\qquad\textbf{(E)}\mbox{ }72$

## Solution

## Solution 1
From any $n-$ th race, only $\frac{1}{6}$ will continue on. Since we wish to find the total number of races, a column representing the races over time is ideal. Starting with the first race: \[\frac{216}{6}=36\] \[\frac{36}{6}=6\] \[\frac{6}{6}=1\] Adding all of the numbers in the second column yields $\boxed{\textbf{(C)}\ 43}$

## Solution 2
Every race eliminates $5$ players. The winner is decided when there is only $1$ runner left. You can construct the equation: $216$ - $5x$ = $1$ . Thus, $215$ players have to be eliminated. Therefore, we need $\frac{215}{5}$ games to decide the winner, or $\boxed{\textbf{(C)}\ 43}$
### See Also