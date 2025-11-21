# 2002 AMC 12P Problem 11

## Problem

Let $t_n = \frac{n(n+1)}{2}$ be the $n$ th triangular number. Find

\[\frac{1}{t_1} + \frac{1}{t_2} + \frac{1}{t_3} + ... + \frac{1}{t_{2002}}\]

$\text{(A) }\frac {4003}{2003} \qquad \text{(B) }\frac {2001}{1001} \qquad \text{(C) }\frac {4004}{2003} \qquad \text{(D) }\frac {4001}{2001} \qquad \text{(E) }2$

## Solution 1
We may write $\frac{1}{t_n}$ as $\frac{2}{n(n+1)}$ and do a partial fraction decomposition. Assume $\frac{2}{n(n+1)} = \frac{A_1}{n} + \frac{A_2}{n+1}$ .
Multiplying both sides by $n(n+1)$ gives $2 = A_1(n+1) + A_2(n) = (A_1 + A_2)n + A_1$ .
Equating coefficients gives $A_1 = 2$ and $A_1 + A_2 = 0$ , so $A_2 = -2$ . Therefore, $\frac{2}{n(n+1)} = \frac{2}{n} - \frac{2}{n+1}$ .
Now $\frac{1}{t_1} + \frac{1}{t_2} + ... + \frac{1}{t_{2002}} = 2((\frac{1}{1} - \frac{1}{2}) + (\frac{1}{2} - \frac{1}{3}) + ... + (\frac{1}{2002} - \frac{1}{2003})) = 2(1 - \frac{1}{2003}) = \boxed{\textbf{(C) } \frac{4004}{2003}}.$
Note: For the sake of completeness, I put the full derivation of the partial fraction decomposition of $\frac{2}{n(n+1)}$ here. However, on the contest, the decomposition step would be much faster since it is so well-known.

## Solution 2 (Cheese)
As with all telescoping problems, there is a solution that involves induction. In competition, it is sufficient to conjecture the formula but not prove it. For sake of completeness and practice, we will prove the formula for $\sum_{i=1}^{n} \frac{1}{t_n}.$
With some guess and check:
$n=1$
\begin{align*} \frac{1}{t_1}&=\frac{2}{1(2)} \\ &=\frac{2}{2} \\ \end{align*}
$n=2$
\begin{align*} \frac{1}{t_1}+\frac{1}{t_2}&=\frac{2}{2}+\frac{2}{2(3)} \\ &=\frac{4}{3} \\ \end{align*}
$n=3$
\begin{align*} \frac{1}{t_1}+\frac{1}{t_2}+\frac{1}{t_3}&=\frac{4}{3}+\frac{2}{3(4)} \\ =\frac{6}{4} \\ \end{align*}
From $\frac{2}{2}, \frac{4}{3},$ and $\frac{6}{4},$ we can conjecture $\sum_{i=1}^{n} \frac{1}{t_n} = \frac{2n}{n+1}.$ A quick check shows that for $n=4$ gives $\frac{8}{5},$ which means our inductive hypothesis is most likely correct. Thus, our answer is $\sum_{i=1}^{2002} \frac{1}{t_n} = \frac{2(2002)}{2002+1}=\boxed{\textbf{(C) } \frac{4004}{2003}}.$
We will prove this with induction for all $n \geq 1$ as promised.
Base case: $n=1.$
\begin{align*} \sum_{i=1}^{1} \frac{1}{t_n}&=\frac{1}{t_n} \\ &=\frac{2}{1(2)} \\ &=1 \\ &=\frac{2(1)}{1+1} \\ &=1 \\ \end{align*}
Since $1=1,$ the base case is proven.
Induction step: $n=k+1.$
Assume: $n=k$ $\implies$ $\sum_{i=1}^{k} \frac{1}{t_k} = \frac{2k}{k+1}.$
We want to prove: $n=k+1$ $\implies$ $\sum_{i=1}^{k+1} \frac{1}{t_k} = \frac{2(k+1)}{k+2}.$
We are given $\sum_{i=1}^{k} \frac{1}{t_k} = \frac{2k}{k+1}.$ Add $\frac{1}{t_{k+1}}$ on both sides and simplify.
\begin{align*} \sum_{i=1}^{k} \frac{1}{t_k} + \frac{1}{t_{k+1}} &= \frac{2k}{k+1} + \frac{1}{t_{k+1}} \\ \sum_{i=1}^{k+1} \frac{1}{t_k} &= \frac{2k}{k+1} + \frac{2}{(k+1)(k+2)} \\ \sum_{i=1}^{k+1} \frac{1}{t_k} &= \frac{2k(k+2)}{(k+1)(k+2)} + \frac{2}{(k+1)(k+2)} \\ \sum_{i=1}^{k+1} \frac{1}{t_k} &= \frac{2k(k+2)+2}{(k+1)(k+2)} \\ \sum_{i=1}^{k+1} \frac{1}{t_k} &= \frac{2k^2+4k+2}{(k+1)(k+2)} \\ \sum_{i=1}^{k+1} \frac{1}{t_k} &= \frac{2(k+1)^2}{(k+1)(k+2)} \\ \sum_{i=1}^{k+1} \frac{1}{t_k} &= \frac{2(k+1)}{(k+2)} \\ \end{align*}
Given the inductive hypothesis, we have proven the induction step. Thus, we have completed our proof for induction.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .