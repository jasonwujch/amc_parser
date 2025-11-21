# 2017 AMC 8 Problem 19

## Problem

For any positive integer $M$ , the notation $M!$ denotes the product of the integers $1$ through $M$ . What is the largest integer $n$ for which $5^n$ is a factor of the sum $98!+99!+100!$ ?

$\textbf{(A) }23 \qquad \textbf{(B) }24 \qquad \textbf{(C) }25 \qquad \textbf{(D) }26 \qquad \textbf{(E) }27$

## Solution 1
Factoring out $98!+99!+100!$ , we have $98! (1+99+99*100)$ , which is $98! (10000)$ . Next, $98!$ has $\left\lfloor\frac{98}{5}\right\rfloor + \left\lfloor\frac{98}{25}\right\rfloor = 19 + 3 = 22$ factors of $5$ . The $19$ is because of all the multiples of $5$ .The $3$ is because of all the multiples of $25$ . Now, $10,000$ has $4$ factors of $5$ , so there are a total of $22 + 4 = \boxed{\textbf{(D)}\ 26}$ factors of $5$ .
~CHECKMATE2021
Note: Do you know what formula this uses? Most AMC 8 test takers won't know it. It's Legendre's Formula .

## Video Solution (Omega Learn)
https://www.youtube.com/watch?v=HISL2-N5NVg&t=817s
~ GeometryMystery
### See Also