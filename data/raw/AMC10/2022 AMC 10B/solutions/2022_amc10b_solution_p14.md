# 2022 AMC 10B Problem 14

## Problem

Suppose that $S$ is a subset of $\left\{ 1, 2, 3, \ldots , 25 \right\}$ such that the sum of any two (not necessarily distinct) elements of $S$ is never an element of $S.$ What is the maximum number of elements $S$ may contain?

$\textbf{(A)}\ 12 \qquad\textbf{(B)}\ 13 \qquad\textbf{(C)}\ 14 \qquad\textbf{(D)}\ 15 \qquad\textbf{(E)}\ 16$

## Solution 1 (Pigeonhole Principle)
Let $M$ be the largest number in $S$ . We categorize numbers $\left\{ 1, 2, \ldots , M-1 \right\}$ (except $\frac{M}{2}$ if $M$ is even) into $\left\lfloor \frac{M-1}{2} \right\rfloor$ groups, such that the $i$ th group contains two numbers $i$ and $M-i$ .
Recall that $M \in S$ and the sum of two numbers in $S$ cannot be equal to $M$ , and the sum of numbers in each group above is equal to $S$ . Thus, each of the above $\left\lfloor \frac{M-1}{2} \right\rfloor$ groups can have at most one number in $S$ . Therefore, \begin{align*} |S| & \leq 1 + \left\lfloor \frac{M-1}{2} \right\rfloor \\ & \leq 1 + \left\lfloor \frac{25}{2} \right\rfloor \\ & = 13. \end{align*}
Next, we construct an instance of $S$ with $|S| = 13$ . Let $S = \left\{ 13, 14, \ldots , 25 \right\}$ . Thus, this set is feasible. Therefore, the most number of elements in $S$ is $\boxed{\textbf{(B) }13}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 2 (Pigeonhole v2)
We construct a possible subset $S$ with $13$ elements by including all odd integers from $1$ to $25$ , inclusive. $S=\left\{ 1, 3, 5, \cdots , 25 \right\}$ . The sum of any $2$ elements is even, and thus cannot be an element of $S$ .
To show that $S$ cannot have more than $13$ elements, assume for sake of contradiction that $|S| \geq 14$ . Let $S=\left\{ x_1, x_2, \cdots , x_n \right\}$ where $n \geq 14$ and $x_1 < x_2 < \cdots < x_n$ . Because the sums of any $2$ (not necessarily distinct) elements do not appear in $S$ , $x_1+x_i$ is not an element of $S$ for all $1 \leq i \leq n$ . So, $x_1, x_2, \cdots , x_n , x_1+x_1, x_1+x_2, \cdots , x_1+x_n$ are all distinct integers. Let these integers be elements of the set $T$ . $|T|=2n$ , and because $n \geq 14$ , $|T| \geq 28$ . But all elements of $T$ must be $\geq x_1$ and $\leq x_1+x_n \leq x_1+25$ , leaving only 26 possible values for the elements in $T$ . By the Pigeonhole Principle, the elements cannot be distinct, and we have a contradiction.
Thus, $\boxed{\textbf{(B) }13}$ is the maximum possible size of $S$ .
~starwars101

## Solution 3 (Intuitive and Fast)
Notice how \( 24 + 25 > 25 \), \( 23 + 24 > 25 \), and this continues backward until \( n + n+1 > 25 \). We then see that \( 2n+1 > 25 \rightarrow 2n > 24 \rightarrow n > 12 \).
Thus the elements in the set must have the property \( n > 12 : n \in \mathbb{Z}^+ \) and therefore our set is \( \{13, 14, 15, \dots, 25\} \) in which there is \( 25 - 13 + 1 \Rightarrow \) $\boxed{\textbf{(B) }13}$ elements.
~Pinotation

## Video Solution
https://youtu.be/_K29sOequlY
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by Interstigation
https://youtu.be/in3N3Os5kGw

## Video Solution by TheBeautyofMath
https://youtu.be/Mi2AxPhnRno?t=1056
~IceMatrix
### See Also
2025 AMC 10A Q21/AMC 12A Q15
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .