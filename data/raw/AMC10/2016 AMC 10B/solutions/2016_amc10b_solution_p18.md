# 2016 AMC 10B Problem 18

## Problem

In how many ways can $345$ be written as the sum of an increasing sequence of two or more consecutive positive integers?

$\textbf{(A)}\ 1\qquad\textbf{(B)}\ 3\qquad\textbf{(C)}\ 5\qquad\textbf{(D)}\ 6\qquad\textbf{(E)}\ 7$

## Solution 1
Factor $345=3\cdot 5\cdot 23$ .
Suppose we take an odd number $k$ of consecutive integers, with the median as $m$ . Then $mk=345$ with $\tfrac12k<m$ . Looking at the factors of $345$ , the possible values of $k$ are $3,5,15,23$ with medians as $115,69,23,15$ respectively.
Suppose instead we take an even number $2k$ of consecutive integers, with median being the average of $m$ and $m+1$ . Then $k(2m+1)=345$ with $k\le m$ . Looking again at the factors of $345$ , the possible values of $k$ are $1,3,5$ with medians $(172,173),(57,58),(34,35)$ respectively.
Thus the answer is $\boxed{\textbf{(E) }7}$ .

## Solution 2
We need to find consecutive numbers (an arithmetic sequence that increases by $1$ ) that sums to $345$ . This calls for the sum of an arithmetic sequence given that the first term is $k$ , the last term is $g$ and with $n$ elements, which is: $\frac {n \cdot (k+g)}{2}$ .
We look for sequences of $n$ consecutive numbers starting at $k$ and ending at $k+n-1$ . We can now substitute $g$ with $k+n-1$ . Now we substitute our new value of $g$ into $\frac {n \cdot (k+g)}{2}$ to get that the sum is $\frac {n \cdot (k+k+n-1)}{2} = 345$ .
This simplifies to $\frac {n \cdot (2k+n-1)}{2} = 345$ . This gives a nice equation. We multiply out the 2 to get that $n \cdot (2k+n-1)=690$ . This leaves us with 2 integers that multiply to $690$ which leads us to think of factors of $690$ . We know the factors of $690$ are: $1,2,3,5,6,10,15,23,30,46,69,115,138,230,345,690$ . So through inspection (checking), we see that only $2,3,5,6,10,15$ and $23$ work. This gives us the answer of $\boxed{\textbf{(E) }7}$ ways.
~~jk23541
An alternate way to finish.
Let \begin{align*} 2k+n-1 &=\frac{690}{k} \\ n &= k \\ \end{align*} where $k$ is a factor of $690.$ We find $2k = 1+\frac{690}{k}-k$ so we need $\frac{690}{k} - k$ to be positive and odd. Fortunately, regardless of the parity of $k$ we see that $\frac{690}{k} - k$ is odd. Furthermore, we need $\frac{690}{k} >k$ which eliminates exact half of the factors. Now, since we need more than $1$ integer to sum up we need $k \ge 2$ which eliminates one more case. There were $16$ cases to begin with, so our answer is $\frac{16}{2}-1 = \boxed{\textbf{(E) }7}$ ways.

## Solution 2.1
At the very end of Solution 2, where we find the factors of 690, instead of inspection, notice that all numbers will work until you get to $30$ , and that is because $\frac{345}{30}=11.5$ , which means $11$ and $12$ must be the middle 2 numbers; however, a sequence of length $30$ with middle numbers $11$ and $12$ that consists only of integers would go into the negatives, so any number from 30 onwards wouldn't work, and since $1$ is a trivial, non-counted solution, we get $\boxed{\textbf{(E) }7}$ -ColtsFan10

## Solution 3 (Fast And Clean)
The median of the sequence $m$ is either an integer or a half integer. Let $m=\frac{i}{2}, i \in N$ , then $P=i\cdot n=2\cdot 3 \cdot 5 \cdot 23$ .
On the other hand we have two constraints:
1) $m \geq \frac{n+1}{2} \iff i>n$ because the integers in the sequence are all positive, and $n>1$ ;
2) If $n$ is odd then $m$ is an integer, $i$ is even; if $n$ is even then $m$ is a half integer, $i$ is odd. Therefore, $n$ and $i$ have opposite parity.
Now $P$ has $16$ factors and it is not a perfect square. There are $8-1=7$ choices for $1 < n < \sqrt{P}$ . Also since $2|P, 4\nmid P$ , we know $n$ and $\frac{P}{n}$ must have opposite parity. Therefore the answer is $\boxed{\textbf{(E) }7}$ .
~ asops

## Video Solution 1
https://youtu.be/dwEm_PcmaYg
~savannahsolver

## Video Solution 2
https://youtu.be/ZhAZ1oPe5Ds?t=950
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .