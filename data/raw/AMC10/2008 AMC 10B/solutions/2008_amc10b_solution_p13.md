# 2008 AMC 10B Problem 13

## Problem

For each positive integer $n$ , the mean of the first $n$ terms of a sequence is $n$ . What is the $2008^{\text{th}}$ term of the sequence?

$\mathrm{(A)}\ {{{2008}}} \qquad \mathrm{(B)}\ {{{4015}}} \qquad \mathrm{(C)}\ {{{4016}}} \qquad \mathrm{(D)}\ {{{4,030,056}}} \qquad \mathrm{(E)}\ {{{4,032,064}}}$

## Solution 1
Since the mean of the first $n$ terms is $n$ , the sum of the first $n$ terms is $n^2$ . Thus, the sum of the first $2007$ terms is $2007^2$ and the sum of the first $2008$ terms is $2008^2$ . Hence, the $2008^{\text{th}}$ term of the sequence is $2008^2-2007^2=(2008+2007)(2008-2007)=4015\Rightarrow \boxed{\textbf{(B) 4015}}$
Note that $n^2$ is the sum of the first n odd integers.

## Solution 2
Let $a_1, a_2, a_3, \cdots, a_n$ be the terms of the sequence. We know $\frac{a_1 + a_2 + a_3 + \cdots + a_n}{n} = n$ , so we must have $a_1 + a_2 + a_3 + \cdots + a_n = n^2$ . The sum of consecutive odd numbers down to $1$ is a perfect square, if you don't believe me, try drawing squares with the sum, so $a_1 = 1, a_2 = 3, a_3 = 5, \cdots , a_n = 2(n-1) + 1$ , so the answer is $a_{2008} = 2(2007) + 1 = \boxed{\textbf{(B) 4015}}$ .

## Solution 3
Let the mean be $\frac{(a)+(a+d)+(a+2d)+...+(a+(n-1)) \cdot d)}{n}$ $=\frac{n \cdot a}{n} + \frac{(1+2+3+...+(n-1)) \cdot d}{n}$ $=a + \frac{n \cdot (n-1) \cdot d}{2n}$ $=a+ \frac{(n-1) \cdot d}{2}$
Note that this is also equal to n
$a+ \frac{(n-1) \cdot d}{2}=n$ $\therefore 2a+ (n-1) \cdot d=2n$
1st term + nth term $=2n=2 \cdot 2008=4016$ Now note that, from previous solutions, the first term is 1, hence the 2008th term is $4016-1=\boxed{\textbf{(B) 4015}}$
~anshulb

## Solution 4 (Using Answer Choices)
From inspection, we see that the sum of the sequence is $n^2$ . We also notice that $n^2$ is the sum of the first $n$ odd integers. Because $4015$ is the only odd integer, $\boxed{\textbf{(B) 4015}}$ is the answer.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .