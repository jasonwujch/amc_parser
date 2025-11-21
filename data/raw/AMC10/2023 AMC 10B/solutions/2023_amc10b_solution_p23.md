# 2023 AMC 10B Problem 23

## Problem

An arithmetic sequence of positive integers has $n \ge 3$ terms, initial term $a$ , and common difference $d > 1$ . Carl wrote down all the terms in this sequence correctly except for one term, which was off by $1$ . The sum of the terms he wrote was $222$ . What is $a + d + n$ ?

$\textbf{(A) } 24 \qquad \textbf{(B) } 20 \qquad \textbf{(C) } 22 \qquad \textbf{(D) } 28 \qquad \textbf{(E) } 26$

## Solution 1
Since one of the terms was either $1$ more or $1$ less than it should have been, the sum should have been $222-1=221$ or $222+1=223.$
The formula for an arithmetic series is $an+d\left(\dfrac{(n-1)n}2\right)=\dfrac n2\left(2a+d(n-1)\right).$ This can quickly be rederived by noticing that the sequence goes $a,a+d,a+2d,a+3d,\dots,a+(n-1)d$ , and grouping terms.
We know that $\dfrac n2(2a+d(n-1))=221$ or $223$ . Let us now show that $223$ is not possible.
If $\dfrac n2(2a+d(n-1))=223$ , we can simplify this to be $n(2a+d(n-1))=223\cdot2.$ Since every expression here should be an integer, we know that either $n=2$ and $2a+d(n-1)=223$ or $n=223$ and $2a+d(n-1)=2.$ The latter is not possible, since $n\ge3,d>1,$ and $a>0.$ The former is also impossible, as $n\ge3.$ Thus, $\dfrac n2(2a+d(n-1))\neq223\implies\dfrac n2(2a+d(n-1))=221$ .
(Alternatively, we have $S=mn$ with $n$ terms and arithmetic mean $m$ , and $223=mn$ does not satisfy both $m > 1$ and $n > 1$ because it is prime.)
We can factor $221$ as $13\cdot17$ . Using similar reasoning, we see that $221\cdot2$ cannot be paired as $2$ and $221$ , but rather must be paired as $13$ and $17$ with a factor of $2$ somewhere.
Let us first try $n=13.$ Our equation simplifies to $2a+12d=34\implies a+6d=17.$ We know that $d>1,$ so we try the smallest possible value: $d=2.$ This would give us $a=17-2\cdot6=17-12=5.$ (Indeed, this is the only possible $d$ .)
There is nothing wrong with the values we have achieved, so it is reasonable to assume that this is the only valid solution (or all solutions sum to the same thing), so we answer $a+d+n=5+2+13=\boxed{\textbf{(B) }20.}$
For the sake of completeness, we can explore $n=17.$ It turns out that we reach a contradiction in this case, so we are done.
~Technodoggo

## Solution 2
There are $n$ terms, the $x$ th term is $a+(x-1)d$ , so the summation is $an+dn(n-1)/2=n(a+\frac{d(n-1)}{2})$ .
The summation of the set is $222 \pm 1 = 221,223$ . First, $221$ : its only possible factors are $1,13,17,221$ , and as said by the problem, $n\ge3$ , so $n$ must be $13,17,$ or $221$ . Let's start with $n=13$ . Then, $a+6d=17$ , and this means $a=5$ , $d=2$ . Summing gives $13+5+2=\boxed{\textbf{(B) }20}$ . We don't need to test any more cases, since the problem writes that all $a+d+n$ are the same.
-HIA2020

## Solution 3
We must have the sum of terms of the arithmetic sequence is $222\pm 1$ , which is $221$ or $223$ .
Since we have $223$ is prime, it cannot be the sum of the arithmetic sequence.
We see that $221$ is just $13\times 17$ .
We can write any arithmetic sequence with an odd amount of terms like this: $b-md,\cdots ,b-2d,b-d,b,b+d,b+2d,\cdots b+md$ where b is the middle term and d is the common difference.
By the sum of an arithmetic sequence, we have $13b=221$ and $17b=221$ and therefore $(b,n)$ $=$ $(13,17)$ or $(17,13)$ .
Then $a+d+n=b-md+d+n=30-(m-1)d$ .
We must have that m is either $\frac{17-1}{2}$ or $\frac{13-1}{2}$ , so m is either $6$ or $8$ .
So $a+d+n=30-5d$ or $30-7d$ .
Taking $\mod 7$ , we have no answer choices that give $2$ , and then taking $\mod 5$ gives the only answer that works is $20$ .
Therefore we have $a+d+n=\boxed{\textbf{(B) }20.}$
~ESAOPS

## Solution 4
The formula for the sum of an arithmetic sequence is $n(\frac{a_1+a_n}{2})$ , where $a$ is the first term, $a_n$ is the last term, and $n$ is the number of terms. Let $a$ be the first term, $d$ be the common difference, and $n$ be the number of terms of Carl's sequence. Since the sum the sequence is $1$ less or $1$ more than $222$ , we have \[n(\frac{a+d(n-1)}{2})\pm{1} = 222\] \[n(\frac{a+d(n-1)}{2}) = 222\pm{1}.\] The right-hand side is either $221$ or $223$ . We know that it has to be divisible by $n$ so we can find the factors of $221$ and $223$ . Checking all the primes less than $15$ , we find that $223$ is prime and $221=13\cdot17$ .
Because $n\ge3$ , the sum must be $221$ and the only possible values of $n$ are $13$ and $17$ . We can test both cases.
Case 1: $n=17$ Substituting for $n$ gives us $a+8d=17$ . Since the sequence consists of only positive integers, $d$ is an integer. We know that $d>1$ but if $d\ge2$ , then $8d>13$ . Hence, this case is not possible.
Case 2: $n=13$ Substituting for $n$ gives us $a+6d=17$ . Using the same logic from case 1, we get $3>d>1$ , so $d=2$ . Solving for $a$ , we get $a=5$ . Therefore, $a+d+n=5+2+13=20$ , so the answer is $\boxed{\textbf{(B) }20.}$ . ~azc1027

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=F30LJeoaNWo

## Video Solution 2
https://youtu.be/IDYnZmNh1io
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution 3 by OmegaLearn
https://youtu.be/VFHo96CKBAk?si=F94ySQaeadr1u0Ps
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .