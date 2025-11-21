# 2020 AMC 8 Problem 17

## Problem

How many positive integer factors of $2020$ have more than $3$ factors? (As an example, $12$ has $6$ factors, namely $1,2,3,4,6,$ and $12.$ )

$\textbf{(A) }6 \qquad \textbf{(B) }7 \qquad \textbf{(C) }8 \qquad \textbf{(D) }9 \qquad \textbf{(E) }10$

## Solution 1
Since $2020 = 2^2 \cdot 5 \cdot 101$ , we can simply list its factors: \[1, 2, 4, 5, 10, 20, 101, 202, 404, 505, 1010, 2020.\] There are $12$ factors; only $1, 2, 4, 5, 101$ don't have over $3$ factors, so the remaining $12-5 = \boxed{\textbf{(B) }7}$ factors have more than $3$ factors.

## Solution 2
As in Solution 1, we prime factorize $2020$ as $2^2\cdot 5\cdot 101$ , and we recall the standard formula that the number of positive factors of an integer is found by adding $1$ to each exponent in its prime factorization, and then multiplying these. Thus $2020$ has $(2+1)(1+1)(1+1) = 12$ factors. The only number which has one factor is $1$ . For a number to have exactly two factors, it must be prime, and the only prime factors of $2020$ are $2$ , $5$ , and $101$ . For a number to have three factors, it must be a square of a prime (this follows from the standard formula mentioned above), and from the prime factorization, the only square of a prime that is a factor of $2020$ is $4$ . Thus, there are $5$ factors of $2020$ which themselves have $1$ , $2$ , or $3$ factors (namely $1$ , $2$ , $4$ , $5$ , and $101$ ), so the number of factors of $2020$ that have more than $3$ factors is $12-5=\boxed{\textbf{(B) }7}$ .

## Solution 3
Let $d(n)$ be the number of factors of n. We know by prime factorization that $d(2020) = 12$ . These $12$ numbers can be divided into unordered pairs ${a,b}$ where $ab = 2020$ . Since $d(2020) = d(a)d(b)$ , one of $d(a), d(b)$ has $3$ or less factors and the other has $4$ or more - in to total $6$ factors of $2020$ with more than $3$ factors. However, this argument has exceptions where $a$ and $b$ share a nontrivial common factor, which in this case can only be two. There are two cases - One in which $5$ and $101$ divide the same factor, WLOG assumed to be $a$ , so that $d(a) = 2^3 > 3$ and $d(b) = 2$ , as otherwise. In the other case, $a = 5\cdot2$ and $b = 101\cdot2$ , so that $d(a) = d(b) = 4$ . This adds one factor with more than $3$ factors, so the answer is $\boxed{\textbf{(B) }7}$ .

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=bHNrBwwUCMI
~NiuniuMaths

## Video Solution (🚀Just 3 min🚀)
https://youtu.be/jJnxvFJuhQw
~Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/Of-ZGiWgXyY?t=56
~ pi_is_3.14

## Video Solution by North America Math Contest Go Go
https://www.youtube.com/watch?v=tUTFLUJ6a-4
~North America Math Contest Go Go Go

## Video Solution by WhyMath
https://youtu.be/2dazhQ31I14
~savannahsolver

## Video Solution
https://youtube/VnOecUiP-SA

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=782
~Interstigation