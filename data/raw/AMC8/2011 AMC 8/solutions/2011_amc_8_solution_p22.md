# 2011 AMC 8 Problem 22

## Problem

What is the tens digit of $7^{2011}$ ?

$\textbf{(A) }0\qquad\textbf{(B) }1\qquad\textbf{(C) }3\qquad\textbf{(D) }4\qquad\textbf{(E) }7$

## Solution 1
Since we want the tens digit, we can find the last two digits of $7^{2011}$ . We can do this by using modular arithmetic. \[7^1\equiv 07 \pmod{100}.\] \[7^2\equiv 49 \pmod{100}.\] \[7^3\equiv 43 \pmod{100}.\] \[7^4\equiv 01 \pmod{100}.\] We can write $7^{2011}$ as $(7^4)^{502}\times 7^3$ . Using this, we can say: \[7^{2011}\equiv (7^4)^{502}\times 7^3\equiv 7^3\equiv 343\equiv 43\pmod{100}.\] From the above, we can conclude that the last two digits of $7^{2011}$ are 43. Since they have asked us to find the tens digit, our answer is $\boxed{\textbf{(D)}\ 4}$ .
-Ilovefruits

## Video Solution by OmegaLearn
https://youtu.be/7an5wU9Q5hk?t=1710

## Video Solution
https://youtu.be/lxtYmUzQQ8w ~David
### See Also