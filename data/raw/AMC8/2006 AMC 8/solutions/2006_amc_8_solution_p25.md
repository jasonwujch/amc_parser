# 2006 AMC 8 Problem 25

## Problem

Barry wrote 6 different numbers, one on each side of 3 cards, and laid the cards on a table, as shown. The sums of the two numbers on each of the three cards are equal. The three numbers on the hidden sides are prime numbers. What is the average of the hidden prime numbers?

[asy] path card=((0,0)--(0,3)--(2,3)--(2,0)--cycle); draw(card, linewidth(1)); draw(shift(2.5,0)*card, linewidth(1)); draw(shift(5,0)*card, linewidth(1)); label("$44$", (1,1.5)); label("$59$", shift(2.5,0)*(1,1.5)); label("$38$", shift(5,0)*(1,1.5));[/asy]

$\textbf{(A)}\ 13\qquad\textbf{(B)}\ 14\qquad\textbf{(C)}\ 15\qquad\textbf{(D)}\ 16\qquad\textbf{(E)}\ 17$

## Solution
Notice that 44 and 38 are both even, while 59 is odd. If any odd prime is added to 59, an even number will be obtained. However, the only way to obtain this even number(common sum) would be to add another even number to 44, and a different one to 38. Since there is only one even prime (2), the middle card's hidden number cannot be an odd prime, and so must be even. Therefore, the middle card's hidden number must be 2, so the constant sum is $59+2=61$ . Thus, the first card's hidden number is $61-44=17$ , and the last card's hidden number is $61-38=23$ .
Since the sum of the hidden primes is $2+17+23=42$ , the average of the primes is $\dfrac{42}{3}=\boxed{\textbf{(B)} 14}$ .

## Video solution
https://www.youtube.com/watch?v=I8E7XUYlIFI ~David

## Video Solution by WhyMath
https://youtu.be/Fa6TV3b_PzY
### See Also