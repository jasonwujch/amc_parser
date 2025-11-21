# 2005 AIME I Problem 2

## Problem

For each positive integer $k$ , let $S_k$ denote the increasing arithmetic sequence of integers whose first term is $1$ and whose common difference is $k$ . For example, $S_3$ is the sequence $1,4,7,10,\ldots.$ For how many values of $k$ does $S_k$ contain the term $2005$ ?

## Solution
Suppose that the $n$ th term of the sequence $S_k$ is $2005$ . Then $1+(n-1)k=2005$ so $k(n-1)=2004=2^2\cdot 3\cdot 167$ . The ordered pairs $(k,n-1)$ of positive integers that satisfy the last equation are $(1,2004)$ , $(2,1002)$ , $(3,668)$ , $(4,501)$ , $(6,334)$ , $(12,167)$ , $(167,12)$ , $(334,6)$ , $(501,4)$ , $(668,3)$ , $(1002,2)$ and $(2004,1)$ , and each of these gives a possible value of $k$ . Thus the requested number of values is $12$ , and the answer is $\boxed{012}$ .
Alternatively, notice that the formula for the number of divisors states that there are $(2 + 1)(1 + 1)(1 + 1) = 12$ divisors of $2^2\cdot 3^1\cdot 167^1$ .

## Solution 2
Any term in the sequence $S_k$ can be written as 1+kx. If this is to equal 2005, then the remainder when 2005 is divided by k is 1.
Now all we have to do is find the numbers of factors of 2004. There are $(2 + 1)(1 + 1)(1 + 1) = \boxed{012}$ divisors of $2^2\cdot 3^1\cdot 167^1$ .
Note that although the remainder when 2005 divided by 1 is not 1, it still works- $S_1$ would be the sequence of all positive integers, in which 2005 must appear.

## Video Solution by OmegaLearn
https://youtu.be/qL0OOYZiaqA?t=83
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.