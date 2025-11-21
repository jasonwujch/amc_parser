# 2017 AMC 8 Problem 10

## Problem

A box contains five cards, numbered 1, 2, 3, 4, and 5. Three cards are selected randomly without replacement from the box. What is the probability that 4 is the largest value selected?

$\textbf{(A) }\frac{1}{10}\qquad\textbf{(B) }\frac{1}{5}\qquad\textbf{(C) }\frac{3}{10}\qquad\textbf{(D) }\frac{2}{5}\qquad\textbf{(E) }\frac{1}{2}$

## Solution 1 (combinational)
There are $\binom{5}{3}$ possible groups of cards that can be selected. If $4$ is the largest card selected, then the other two cards must be either $1$ , $2$ , or $3$ , for a total $\binom{3}{2}$ groups of cards. Then, the probability is just ${\frac{{\dbinom{3}{2}}}{{\dbinom{5}{3}}}} = \boxed{{\textbf{(C) }} {\frac{3}{10}}}$ .

## Solution 2 (regular probability)
P (no 5)= $\frac{4}{5}$ * $\frac{3}{4}$ * $\frac{2}{3}$ = $\frac{2}{5}$ . This is the fraction of total cases with no fives. p (no 4 and no 5)= $\frac{3}{5}$ * $\frac{2}{4}$ * $\frac{1}{3}$ = $\frac{6}{60}$ = $\frac{1}{10}$ . This is the intersection of no fours and no fives. Subtract the fraction of no fours and no fives from that of no fives. $\frac{2}{5} - \frac{1}{10} = \frac{3}{10} = \boxed{{\textbf{(C) }} {\frac{3}{10}}}$ .

## Video Solution (CREATIVE THINKING!!!)
https://youtu.be/P-K9AEAuhNY
~Education, the Study of Everything

## Video Solutions
https://youtu.be/FN9qkU62a9U
~savannahsolver
### See Also: