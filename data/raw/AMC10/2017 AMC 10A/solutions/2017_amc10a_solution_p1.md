# 2017 AMC 10A Problem 1

## Problem

What is the value of $(2(2(2(2(2(2+1)+1)+1)+1)+1)+1)$ ?

$\textbf{(A)}\ 70\qquad\textbf{(B)}\ 97\qquad\textbf{(C)}\ 127\qquad\textbf{(D)}\ 159\qquad\textbf{(E)}\ 729$

## Solution 1
Notice this is the term $a_6$ in a recursive sequence, defined recursively as $a_1 = 3, a_n = 2a_{n-1} + 1.$ Thus: \[\begin{split} a_2 = 3 \cdot 2 + 1 = 7.\\ a_3 = 7 \cdot 2 + 1 = 15.\\ a_4 = 15 \cdot 2 + 1 = 31.\\ a_5 = 31 \cdot 2 + 1 = 63.\\ a_6 = 63 \cdot 2 + 1 = \boxed{\textbf{(C)}\ 127} \end{split}\]
Minor LaTeX edits by fasterthanlight

## Solution 2
Starting to compute the inner expressions, we see the results are $1, 3, 7, 15, \ldots$ . This is always $1$ less than a power of $2$ . The only admissible answer choice by this rule is thus $\boxed{\textbf{(C)}\ 127}$ .

## Solution 3
Working our way from the innermost parenthesis outwards and directly computing, we have $\boxed{\textbf{(C) } 127}$ .

## Solution 4
If you distribute this you get a sum of the powers of $2$ . The largest power of $2$ in the series is $64$ , so the sum is $\boxed{\textbf{(C)}\ 127}$ .

## Solution 5
$(2(2(2(2(2(2+1)+1)+1)+1)+1)+1)$ $=(2(2(2(2(2(3)+1)+1)+1)+1)+1)$ $=(2(2(2(2(6+1)+1)+1)+1)+1)$ $=(2(2(2(2(7)+1)+1)+1)+1)$ $=(2(2(2(14+1)+1)+1)+1)$ $=(2(2(2(15)+1)+1)+1)$ $=(2(2(30+1)+1)+1)$ $=(2(2(31)+1)+1)$ $=(2(62+1)+1)$ $=(2(63)+1)$ $=(126+1)$ $=127 \Longrightarrow \boxed{\textbf{(C)}\ 127}$ .

## Solution 6 (quickest)
Notice that $x^6 + x^5 + x^4 + x^3 + x^2 + x + 1 = x (x (x (x (x (x + 1) + 1) + 1) + 1) + 1) + 1$ . Substituting $2$ for $x$ , we get \[2(2(2(2(2(2+1)+1)+1)+1)+1)+1 = 2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2 + 1 = 2^7 - 1 \Longrightarrow \boxed{\textbf{(C)}\ 127}\]

## Solution 7 (Fast)
Notice that there are 5 instances where the sum is multiplied by $2$ . That gives us $2^5 = 32$ . Separate the addition part into $3$ and the $1$ . Multiply the $3$ by $32$ , giving $96$ . Then notice that the $1$ is multiplied by increasing powers of two; therefore, it is equal to $2^5-1$ . Then add these two parts. $96+31=\boxed{\textbf{(C)}\ 127}$

## Video Solution
https://youtu.be/str7kmcRMY8
https://youtu.be/kA6W8SwjitA
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .