# 2016 AMC 10A Problem 12

## Problem

Three distinct integers are selected at random between $1$ and $2016$ , inclusive. Which of the following is a correct statement about the probability $p$ that the product of the three integers is odd?

$\textbf{(A)}\ p<\dfrac{1}{8}\qquad\textbf{(B)}\ p=\dfrac{1}{8}\qquad\textbf{(C)}\ \dfrac{1}{8}<p<\dfrac{1}{3}\qquad\textbf{(D)}\ p=\dfrac{1}{3}\qquad\textbf{(E)}\ p>\dfrac{1}{3}$

## Solution 1 (Accounts for Order)
For the product to be odd, all three factors have to be odd. The probability of this is $\frac{1008}{2016} \cdot \frac{1007}{2015} \cdot \frac{1006}{2014}$ .
$\frac{1008}{2016} = \frac{1}{2}$ , but $\frac{1007}{2015}$ and $\frac{1006}{2014}$ are slightly less than $\frac{1}{2}$ . Thus, the whole product is slightly less than $\frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$ , so $\boxed{\textbf{(A) }p<\dfrac{1}{8}}$ .

## Solution 2 (Disregards Order)
For the product to be odd, all three factors have to be odd. There are a total of $\binom{2016}{3}$ ways to choose 3 numbers at random, and there are $\binom{1008}{3}$ to choose 3 odd numbers. Therefore, the probability of choosing 3 odd numbers is $\frac{\binom{1008}{3}}{\binom{2016}{3}}$ . Simplifying this, we obtain $\frac{1008*1007*1006}{2016*2015*2014}$ , which is slightly less than $\frac{1}{8}$ , so our answer is $\boxed{\textbf{(A) }p<\dfrac{1}{8}}$ .

## Solution 3
The probability that the product is odd, allowing duplication of the integers, is just $\left( \frac{1}{2} \right) ^3 = \frac{1}{8}$ . Since forbidding duplication reduces the probability of all three integers being odd, we see $p<\dfrac{1}{8}$ and our answer is $\boxed{\textbf{(A) }}$ .

## Video Solution (CREATIVE THINKING)
https://youtu.be/rioKxSpmlnU
~Education, the Study of Everything

## Video Solution
https://youtu.be/dHY8gjoYFXU?t=300
~IceMatrix
https://youtu.be/8_clljylXwI
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .