# 2005 AMC 10A Problem 22

## Problem

Let $S$ be the set of the $2005$ smallest positive multiples of $4$ , and let $T$ be the set of the $2005$ smallest positive multiples of $6$ . How many elements are common to $S$ and $T$ ?

$\textbf{(A) } 166\qquad \textbf{(B) } 333\qquad \textbf{(C) } 500\qquad \textbf{(D) } 668\qquad \textbf{(E) } 1001$

## Solution 1
Since the least common multiple of $4$ and $6$ is $12$ , the elements that are common to $S$ and $T$ are all multiples of $12$ . Moreover, as the largest element of $S$ is $4 \cdot 2005$ , while that of $T$ is $6 \cdot 2005$ , which is larger, several of the multiples of $12$ that are in $T$ will not be in $S$ , whereas all the multiples of $12$ that are in $S$ will be in $T$ .
Thus we only need to find the number of multiples of $12$ that are in $S$ , and so we observe that as $4 \cdot 3 = 12$ , these multiples of $12$ are precisely every $3$ rd element of $S$ . It follows that there are $\left\lfloor\frac{2005}{3}\right \rfloor = \boxed{\textbf{(D) } 668}$ such elements.

## Solution 2
As in Solution $1$ , we find that the elements common to $S$ and $T$ are precisely the multiples of $12$ . As $S$ has exactly $2005$ elements, these must range from $4 \cdot 1 = 4$ to $4 \cdot 2005 = 8020$ , and similarly the elements of $T$ range from $6 \cdot 1 = 6$ to $6 \cdot 2005 = 12030$ . This means any element $n \in S \cap T$ must satisfy both $4 \leq n \leq 8020$ and $6 \leq n \leq 12030$ , which reduces to simply $6 \leq n \leq 8020$ .
Accordingly, as $12 \cdot 0 = 0 < 6 < 12 \cdot 1 = 12$ and $12 \cdot 668 = 8016 < 8020 < 12 \cdot 669 = 8028$ , the multiples of $12$ in the required interval range from $12 \cdot 1$ to $12 \cdot 668$ , so there are precisely $\boxed{\textbf{(D) } 668}$ of them.

## Video Solution
https://youtu.be/D6tjMlXd_0U
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .