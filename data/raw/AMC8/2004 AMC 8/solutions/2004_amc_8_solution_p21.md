# 2004 AMC 8 Problem 21

## Problem

Spinners $A$ and $B$ are spun. On each spinner, the arrow is equally likely to land on each number. What is the probability that the product of the two spinners' numbers is even?

[asy] pair A=(0,0); pair B=(3,0); draw(Circle(A,1)); draw(Circle(B,1)); draw((-1,0)--(1,0)); draw((0,1)--(0,-1)); draw((3,0)--(3,1)); draw((3+sqrt(3)/2,-.5)--(3,0)); draw((3,0)--(3-sqrt(3)/2,-.5)); label("$A$",(-1,1)); label("$B$",(2,1)); label("$1$",(-.4,.4)); label("$2$",(.4,.4)); label("$3$",(.4,-.4)); label("$4$",(-.4,-.4)); label("$1$",(2.6,.4)); label("$2$",(3.4,.4)); label("$3$",(3,-.5)); [/asy]

$\textbf{(A)}\ \frac14\qquad \textbf{(B)}\ \frac13\qquad \textbf{(C)}\ \frac12\qquad \textbf{(D)}\ \frac23\qquad \textbf{(E)}\ \frac34$

## Solution
An even number comes from multiplying an even and even, even and odd, or odd and even. Since an odd number only comes from multiplying an odd and odd, there are less cases and it would be easier to find the probability of spinning two odd numbers from $1$ . Multiply the independent probabilities of each spinner getting an odd number together and subtract it from $1$ .
\[1-\frac24 \cdot \frac23 = 1- \frac13 = \boxed{\textbf{(D)}\ \frac23}\]

## Solution 2
We can make a chart and the we see that the 12 possibilities: 1, 2, 3, 2, 4, 6, 3, 6, 9, 4, 8, and 12. Out of these only 8 work; thus the probability is \[\boxed{\textbf{(D)}\ \frac23}\]

## Solution 3
We do a little bit of casework. In order to get a product that's even, we need at least one even number. First, we consider the probability of getting an even number on the first spinner, and then multiply by 1 because the second spinner can be anything. \[\frac12 \cdot 1 = \frac12\] Next, we look at the chance that we don't get an even on the first spinner, but get an even on the second spinner (we don't do the probability of even on the second spinner multiplied by one because we would be double counting both spinners are even). \[\frac12 \cdot \frac13 = \frac16\] Add these two together to get the total probability, and we get \[\frac12 + \frac16 = \frac46 = \boxed{\textbf{(D)}\ \frac23}\]
~ligonmathkid2
### See Also