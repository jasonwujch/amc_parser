# 2022 AMC 10B Problem 3

## Problem

How many three-digit positive integers have an odd number of even digits?

$\textbf{(A) }150\qquad\textbf{(B) }250\qquad\textbf{(C) }350\qquad\textbf{(D) }450\qquad\textbf{(E) }550$

## Solution 1
We use simple case work to solve this problem.
Case 1: even, even, even = $4 \cdot 5 \cdot 5 = 100$
Case 2: even, odd, odd = $4 \cdot 5 \cdot 5 = 100$
Case 3: odd, even, odd = $5 \cdot 5 \cdot 5 = 125$
Case 4: odd, odd, even = $5 \cdot 5 \cdot 5 = 125$
Simply sum up the cases to get your answer, $100 + 100 + 125 + 125 = \boxed{\textbf{(D)~}450}$ .
- Wesseywes7254

## Solution 2 (Bijection)
We will show that the answer is $450$ by proving a bijection between the three digit integers that have an even number of even digits and the three digit integers that have an odd number of even digits. For every even number with an odd number of even digits, we increment the number's last digit by $1$ , unless the last digit is $9$ , in which case it becomes $0$ . It is very easy to show that every number with an even number of even digits is mapped to every number with an odd number of even digits, and vice versa. Thus, the answer is half the number of three digit numbers, or $\boxed{\textbf{(D)~}450}$
~mathboy100

## Video Solution 1 (🚀Just 2 min🚀)
https://youtu.be/rAad-1GMgIs
~Education, the Study of Everything

## Video Solution by Interstigation
https://youtu.be/_KNR0JV5rdI?t=167
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .