# 2023 AIME I Problem 4

## Problem

The sum of all positive integers $m$ such that $\frac{13!}{m}$ is a perfect square can be written as $2^a3^b5^c7^d11^e13^f,$ where $a,b,c,d,e,$ and $f$ are positive integers. Find $a+b+c+d+e+f.$

## Video Solution by MegaMath
https://www.youtube.com/watch?v=EqLTyGanr4s&t=136s

## Solution 1
We first rewrite $13!$ as a prime factorization, which is $2^{10}\cdot3^5\cdot5^2\cdot7\cdot11\cdot13.$
For the fraction to be a square, it needs each prime to be an even power. This means $m$ must contain $7\cdot11\cdot13$ . Also, $m$ can contain any even power of $2$ up to $2^{10}$ , any odd power of $3$ up to $3^{5}$ , and any even power of $5$ up to $5^{2}$ . The sum of $m$ is \[(2^0+2^2+2^4+2^6+2^8+2^{10})(3^1+3^3+3^5)(5^0+5^2)(7^1)(11^1)(13^1) =\] \[1365\cdot273\cdot26\cdot7\cdot11\cdot13 = 2\cdot3^2\cdot5\cdot7^3\cdot11\cdot13^4.\] Therefore, the answer is $1+2+1+3+1+4=\boxed{012}$ .
~chem1kall

## Solution 2
The prime factorization of $13!$ is \[2^{10} \cdot 3^5 \cdot 5^2 \cdot 7 \cdot 11 \cdot 13.\] To get $\frac{13!}{m}$ a perfect square, we must have $m = 2^{2x} \cdot 3^{1 + 2y} \cdot 5^{2z} \cdot 7 \cdot 11 \cdot 13$ , where $x \in \left\{ 0, 1, \cdots , 5 \right\}$ , $y \in \left\{ 0, 1, 2 \right\}$ , $z \in \left\{ 0, 1 \right\}$ .
Hence, the sum of all feasible $m$ is \begin{align*} \sum_{x=0}^5 \sum_{y=0}^2 \sum_{z=0}^1 2^{2x} \cdot 3^{1 + 2y} \cdot 5^{2z} \cdot 7 \cdot 11 \cdot 13 & = \left( \sum_{x=0}^5 2^{2x} \right) \left( \sum_{y=0}^2 3^{1 + 2y} \right) \left( \sum_{z=0}^1 5^{2z} \right) 7 \cdot 11 \cdot 13 \\ & = \frac{4^6 - 1}{4-1} \cdot \frac{3 \cdot \left( 9^3 - 1 \right)}{9 - 1} \cdot \frac{25^2 - 1}{25 - 1} \cdot 7 \cdot 11 \cdot 13 \\ & = 2 \cdot 3^2 \cdot 5 \cdot 7^3 \cdot 11 \cdot 13^4 . \end{align*}
Therefore, the answer is \begin{align*} 1 + 2 + 1 + 3 + 1 + 4 & = \boxed{012} . \end{align*}
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3 (Educated Guess and Engineer's Induction (Fake solve))
Try smaller cases. There is clearly only one $m$ that makes $\frac{2!}{m}$ a square, and this is $m=2$ . Here, the sum of the exponents in the prime factorization is just $1$ . Furthermore, the only $m$ that makes $\frac{3!}{m}$ a square is $m = 6 = 2^13^1$ , and the sum of the exponents is $2$ here. Trying $\frac{4!}{m}$ and $\frac{5!}{m}$ , the sums of the exponents are $3$ and $4$ . Based on this, we (incorrectly!) conclude that, when we are given $\frac{n!}{m}$ , the desired sum is $n-1$ . The problem gives us $\frac{13!}{m}$ , so the answer is $13-1 = \boxed{012}$ .
-InsetIowa9
However...
The induction fails starting at $n = 9$ ! The actual answers $f(n)$ for small $n$ are: $0, 1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 11, 12$ In general, $f(p) = f(p-1)+1$ if p is prime, $n=4,6,8$ are "lucky", and the pattern breaks down after $n=8$
-"fake" warning by oinava

## Video Solutions
I also somewhat try to explain how the formula for sum of the divisors works, not sure I succeeded. Was 3 AM lol. https://youtube.com/MUYC2fBF2U4
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .