# 2023 AMC 10A Problem 14

## Problem

A number is chosen at random from among the first $100$ positive integers, and a positive integer divisor of that number is then chosen at random. What is the probability that the chosen divisor is divisible by $11$ ?

$\textbf{(A)}~\frac{4}{100}\qquad\textbf{(B)}~\frac{9}{200} \qquad \textbf{(C)}~\frac{1}{20} \qquad\textbf{(D)}~\frac{11}{200}\qquad\textbf{(E)}~\frac{3}{50}$

## Solution 1
In order for the divisor chosen to be a multiple of $11$ , the original number chosen must also be a multiple of $11$ . Among the first $100$ positive integers, there are 9 multiples of 11; 11, 22, 33, 44, 55, 66, 77, 88, 99. We can now perform a little casework on the probability of choosing a divisor which is a multiple of 11 for each of these 9, and see that the probability is 1/2 for each. The probability of choosing these 9 multiples in the first place is $\frac{9}{100}$ , so the final probability is $\frac{9}{100} \cdot \frac{1}{2} = \frac{9}{200}$ , so the answer is $\boxed{\textbf{(B)}~\frac{9}{200}}.$
$11 = 1, 11 \Rightarrow \frac{1}{2}\\ 22 = 2 \times 11: 1, 2, 11, 22 \Rightarrow \frac{1}{2}\\ 33 = 3 \times 11: 1, 3, 11, 33 \Rightarrow \frac{1}{2}\\ 44 = 2^2 \times 11: 1, 2, 4, 11, 22, 44 \Rightarrow \frac{1}{2}\\ 55 = 5 \times 11: 1, 5, 11, 55 \Rightarrow \frac{1}{2}\\ 66 = 2 \times 3 \times 11: 1, 2, 3, 6, 11, 22, 33, 66 \Rightarrow \frac{1}{2}\\ 77 = 7 \times 11: 1, 7, 11, 77 \Rightarrow \frac{1}{2}\\ 88 = 2^3 \times 11: 1, 2, 4, 8, 11, 22, 44, 88 \Rightarrow \frac{1}{2}\\ 99 = 3^2 \times 11: 1, 3, 9, 11, 33, 99 \Rightarrow \frac{1}{2}$
~vaisri
~walmartbrian
~Shontai
~(minor formatting changes by Marshall_Huang)
~Formatting changes to avoid confusion by SHREYU.MEDATATI

## Solution 2
There are $\left\lfloor\frac{100}{11}\right\rfloor = 9$ multiples of $11$ under $100$ . Because all of these numbers are multiples of $11$ to the first power and first power only, their factors can either have $11$ as a factor ( $11^{1}$ ) or not have $11$ as a factor ( $11^{0}$ ), resulting in a $\frac{1}{2}$ chance of a factor chosen being divisible by $11$ . The chance of choosing any factor of $11$ under $100$ is $\frac{9}{100}$ , so the final answer is $\frac{9}{100} \cdot \frac{1}{2} = \boxed{\textbf{(B)}~\frac{9}{200}}.$
~Failure.net

## Solution 3 (generalized)
Let $N$ be the positive integer in question. Since $N$ is a multiple of $11$ , we can write $N = 11^{e_1}p_1^{e_2}\cdots p_{k-1}^{e_k},$ the prime factorization of $N$ . To find the total number of divisors divisible by $11$ , observe that there are $(e_2 + 1)(e_3 + 1)\cdots (e_k + 1)$ divisors not divisible by $11$ . For each power of $11$ greater than $1$ , of which there are $e_1$ , it can be paired with any of these other divisors. Therefore, there are \[e_1(e_2+1)(e_3 + 1)\cdots (e_k + 1)\] divisors of $N$ that are divisible by $11$ . The total number of divisors of $N$ is \[(e_1 + 1)(e_2 + 1)\cdots (e_k + 1),\] so the probability of choosing a divisor that is divisible by $11$ is \[\frac{e_1(e_2+1)(e_3 + 1)\cdots (e_k + 1)}{(e_1 + 1)(e_2 + 1)\cdots (e_k + 1)} = \frac{e_1}{e_1 + 1}.\] For each positive integer less than or equal to $100$ , the highest power of $11$ that divides it is $11$ , so $e_1 = 1$ , meaning that the probability of choosing a divisor (that is divisible by $11$ ) of a fixed $N$ is $\frac{1}{2}.$ The probability of choosing any $N$ from the first $100$ positive integers is $\frac{1}{100},$ so the probability of choosing any of these divisors is $\frac{1}{100}\cdot \frac{1}{2}.$ There are $9$ multiples of $11$ less than or equal to $100$ , so the total probability is \[9\cdot \frac{1}{100}\cdot \frac{1}{2} = \boxed{\textbf{(B)}\ \frac{9}{200}}.\]
-Benedict T (countmath1)

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=BATFbSs7VssVJpvm&t=3050 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=J8YkZnOt7AoOgUcS&t=3530 ~Math-X

## Video Solution ⚡️ 1 min solution ⚡️
https://youtu.be/CP0Arc_82Y8
~Education, the Study of Everything

## Video Solution
https://www.youtube.com/watch?v=uaf46N6qP54

## Video Solution
https://youtu.be/O_P3E9hDrYY
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .