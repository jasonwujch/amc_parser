# 2018 AMC 8 Problem 18

## Problem

How many positive factors does $23,232$ have?

$\textbf{(A) }9\qquad\textbf{(B) }12\qquad\textbf{(C) }28\qquad\textbf{(D) }36\qquad\textbf{(E) }42$

## Solution 1
We can first find the prime factorization of $23,232$ , which is $2^6\cdot3^1\cdot11^2$ . Now, we add one to our powers and multiply. Therefore, the answer is $(6+1)\cdot(1+1)\cdot(2+1)=7\cdot2\cdot3=\boxed{\textbf{(E) }42}$
Note: 23232 is a large number, so we can look for shortcuts to factor it. One way to factor it quickly is to use 3 and 11 divisibility rules to observe that $23232 = 3 \cdot 7744 = 3 \cdot 11 \cdot 704 = 3 \cdot 11^2 \cdot 64 = 3^1 \cdot 11^2 \cdot 2^6$ .
Another way is to spot the "32" and compute that $23232 = 32\cdot(101 + 10000/16) = 32\cdot (101+ 5^4) = 32\cdot 726 = 32 \cdot 11 \cdot 66$ .
A third way to factor it is to observe $23232 = 24000 - 768$ . Factoring out the 3 gives us $3(8000 - 256)$ . Since $8000 = 2^6 \cdot 5^3$ and $256 = 2^8$ , we have $2^6 \cdot 3 (5^3 - 2^2) = 2^6 \cdot 3 (125-4) = 2^6 \cdot 3 \cdot 121 = 2^6 \cdot 3 \cdot 11^2$ .

## Solution 2 (Using 264^2)
Observe that $69696$ = $264^2$ , so this is $\frac{1}{3}$ of $264^2$ which is $88 \cdot 264 = 11^2 \cdot 8^2 \cdot 3 = 11^2 \cdot 2^6 \cdot 3$ , which has $3 \cdot 7 \cdot 2 = 42$ factors. The answer is $\boxed{\textbf{(E) }42}$ .

## Video Solution
https://youtu.be/44kIAfS5iJk
~Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/6xNkyDgIhEE?t=1515
~ pi_is_3.14

## Video Solution
https://youtu.be/sC2-sdUjm40
~savannahsolver
### See Also