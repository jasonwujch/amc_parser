# 2009 AMC 8 Problem 12

## Problem

The two spinners shown are spun once and each lands on one of the numbered sectors. What is the probability that the sum of the numbers in the two sectors is prime?

[asy] unitsize(30); draw(unitcircle); draw((0,0)--(0,-1)); draw((0,0)--(cos(pi/6),sin(pi/6))); draw((0,0)--(-cos(pi/6),sin(pi/6))); label("$1$",(0,.5)); label("$3$",((cos(pi/6))/2,(-sin(pi/6))/2)); label("$5$",(-(cos(pi/6))/2,(-sin(pi/6))/2));[/asy] [asy] unitsize(30); draw(unitcircle); draw((0,0)--(0,-1)); draw((0,0)--(cos(pi/6),sin(pi/6))); draw((0,0)--(-cos(pi/6),sin(pi/6))); label("$2$",(0,.5)); label("$4$",((cos(pi/6))/2,(-sin(pi/6))/2)); label("$6$",(-(cos(pi/6))/2,(-sin(pi/6))/2));[/asy]

$\textbf{(A)}\ \frac{1}{2}\qquad\textbf{(B)}\ \frac{2}{3}\qquad\textbf{(C)}\ \frac{3}{4}\qquad\textbf{(D)}\ \frac{7}{9}\qquad\textbf{(E)}\ \frac{5}{6}$

## Solution
The possible sums are \[\begin{tabular}{c|ccc} & 1 & 3 & 5 \\ \hline 2 & 3 & 5 & 7 \\ 4 & 5 & 7 & 9 \\ 6 & 7 & 9 & 11 \end{tabular}\]
Only $9$ is not prime, so there are $7$ prime numbers and $9$ total numbers for a probability of $\boxed{\textbf{(D)}\ \frac79}$ .

## Video Solution
https://www.youtube.com/watch?v=NPTaWKEkaHs ~David
### See Also