# 2005 AMC 10B Problem 12

## Problem

Twelve fair dice are rolled. What is the probability that the product of the numbers on the top faces is prime?

$\textbf{(A) } \left(\frac{1}{12}\right)^{12} \qquad \textbf{(B) } \left(\frac{1}{6}\right)^{12} \qquad \textbf{(C) } 2\left(\frac{1}{6}\right)^{11} \qquad \textbf{(D) } \frac{5}{2}\left(\frac{1}{6}\right)^{11} \qquad \textbf{(E) } \left(\frac{1}{6}\right)^{10}$

## Solution 1
In order for the product of the numbers to be prime, $11$ of the dice have to be a $1$ , and the other die has to be a prime number. There are $3$ prime numbers ( $2$ , $3$ , and $5$ ), and there is only one $1$ , and there are $\dbinom{12}{1}$ ways to choose which die will have the prime number, so the probability is $\dfrac{3}{6}\times\left(\dfrac{1}{6}\right)^{11}\times\dbinom{12}{1} = \dfrac{1}{2}\times\left(\dfrac{1}{6}\right)^{11}\times12=\left(\dfrac{1}{6}\right)^{11}\times6=\boxed{\textbf{(E) }\left(\dfrac{1}{6}\right)^{10}}$ .

## Solution 2
There are three cases where the product of the numbers is prime. One die will show $2$ , $3$ , or $5$ and each of the other $11$ dice will show a $1$ . For each of these three cases, the number of ways to order the numbers is $\dbinom{12}{1}$ = $12$ . There are $6$ possible numbers for each of the $12$ dice, so the total number of permutations is $6^{12}$ . The probability the product is prime is therefore $\frac{3\cdot 12}{6^{12}} = \frac{1}{6^{10}} =\boxed{\textbf{(E) }\left(\dfrac{1}{6}\right)^{10}}$ .
~mobius247

## Solution 3
The only way to get a product of that is a prime number is to roll all ones except for such prime, e.g: $11$ ones and $1$ two. So we seek the probability of rolling $11$ ones and $1$ prime number. The probability of rolling $11$ ones is $\frac{1}{6^{11}}$ and the probability of rolling a prime is $\frac{1}{2}$ , giving us a probability of $\frac{1}{6^{11}}\cdot\frac{1}{2}$ of this outcome occuring. However, there are $\frac{12!}{11!\cdot{1!}}=12$ ways to arrange the ones and the prime. Multiplying the previous probability by $12$ gives us $\frac{1}{6^{11}}\cdot\frac{1}{2}\cdot{6}=\frac{1}{6^{10}}=\boxed{\textbf{(E) }\left(\dfrac{1}{6}\right)^{10}}.$
-Benedict T (countmath1)

## Solution 4
The only way to get a prime number product is to roll \(1\) on all \(11\) dices and roll a prime number on the remaining one.
There are 3 prime numbers less than or equal to 6: \(2, 3, 5\). For each of the 12 dice, we can choose one to roll the prime number on, while the other 11 show 1. So, there are \(12 \times 3 = 36\) favorable outcomes.
Since each die has 6 faces and there are 12 dice, the total number of possible outcomes is \(6^{12}\).
Therefore, the probability is \[\frac{36}{6^{12}} = \left(\frac{1}{6}\right)^{10}.\]
\[\boxed{\textbf{(E) } \left(\dfrac{1}{6}\right)^{10}}\] -LittleWavelet
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .