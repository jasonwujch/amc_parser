# 2004 AMC 10B Problem 21

## Problem

Let $1$ , $4$ , $7$ , $\ldots$ and $9$ , $16$ , $23$ , $\ldots$ be two arithmetic progressions. The set $S$ is the union of the first $2004$ terms of each sequence. How many distinct numbers are in $S$ ?

$\mathrm{(A) \ } 3722 \qquad \mathrm{(B) \ } 3732 \qquad \mathrm{(C) \ } 3914 \qquad \mathrm{(D) \ } 3924 \qquad \mathrm{(E) \ } 4007$

## Solution 1
The terms in the first sequence are defined by $n \equiv 1 \pmod3$ , while the terms in the second sequence are defined by $n \equiv 2 \pmod 7.$ We seek to find the solutions to this system of modular congruences.
Letting $n = 3a + 1 = 7b + 2$ for nonnegative integers $a,b$ we solve the congruence \begin{align*} 3a+1 &\equiv 7b+2 \pmod 3, \\ 1 &\equiv b + 2 \pmod 3, \\ b &\equiv 2 \pmod 3.\end{align*}
For nonnegative integer $c,$ we have that $b = 3c+2$ . Substituting back into our original equation, we have $n = 21c + 16,$ or $n \equiv 16 \pmod {21}.$
Now we have to find the largest term in the smaller sequence (first sequence), which is $2003 \cdot 3 + 1 = 6010.$ Dividing $\frac{6010}{21}$ gives that there are $286$ terms in common between the sequences.
By PIE, the answer is just $2004 + 2004 - 286 = \boxed{(A) 3722}.$

## Solution 2
The two sets of terms are $A=\{ 3k+1 : 0\leq k < 2004 \}$ and $B=\{ 7l+9 : 0\leq l<2004\}$ .
Now $S=A\cup B$ . We can compute $|S|=|A\cup B|=|A|+|B|-|A\cap B|=4008-|A\cap B|$ . We will now find $|A\cap B|$ .
Consider the numbers in $B$ . We want to find out how many of them lie in $A$ . In other words, we need to find out the number of valid values of $l$ for which $7l+9\in A$ .
The fact " $7l+9\in A$ " can be rewritten as " $1\leq 7l+9 \leq 3\cdot 2003 + 1$ , and $7l+9\equiv 1\pmod 3$ ".
The first condition gives $0\leq l\leq 857$ , the second one gives $l\equiv 1\pmod 3$ .
Thus the good values of $l$ are $\{1,4,7,\dots,856\}$ , and their count is $858/3 = 286$ .
Therefore $|A\cap B|=286$ , and thus $|S|=4008-|A\cap B|=\boxed{(A) 3722}$ .

## Solution 3
We can start by finding the first non-distinct term from both sequences. We find that that number is $16$ . Now, to find every other non-distinct terms, we can just keep adding $21$ .
We know that the last terms of both sequences are $1+3\cdot 2003$ and $9+7\cdot 2003$ . Clearly, $1+3\cdot 2003$ is smaller and that is the last possible common term of both sequences.
Now, we can create the inequality $16+21k \leq 1+3\cdot 2003$ . Using the inequality, we find that there are $286$ common terms. There are 4008 terms in total. $4008-286=\boxed{(A) 3722}$
~kempwood
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .