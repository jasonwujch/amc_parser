# 2002 AMC 12P Problem 2

## Problem

The function $f$ is given by the table

\[\begin{tabular}{|c||c|c|c|c|c|} \hline x & 1 & 2 & 3 & 4 & 5 \\ \hline f(x) & 4 & 1 & 3 & 5 & 2 \\ \hline \end{tabular}\]

If $u_0=4$ and $u_{n+1} = f(u_n)$ for $n \ge 0$ , find $u_{2002}$

$\text{(A) }1 \qquad \text{(B) }2 \qquad \text{(C) }3 \qquad \text{(D) }4 \qquad \text{(E) }5$

## Solution 1
We can guess that the series given by the problem is periodic in some way. Starting off, $u_0=4$ is given. $u_1=u_{0+1}=f(u_0)=f(4)=5,$ so $u_1=5.$ $u_2=u_{1+1}=f(u_1)=f(5)=2,$ so $u_2=2.$ $u_3=u_{2+1}=f(u_2)=f(2)=1,$ so $u_3=1.$ $u_4=u_{3+1}=f(u_3)=f(1)=4,$ so $u_4=4.$ Plugging in $4$ will give us $5$ as found before, and plugging in $5$ will give $2$ and so on. This means that our original guess of the series being periodic was correct. Summing up our findings in a nice table,
\[\begin{tabular}{|c||c|c|c|c|c|c|} \hline n & 0 & 1 & 2 & 3 & 4 & ...\\ \hline un & 4 & 5 & 2 & 1 & 4 & ...\\ \hline \end{tabular}\]
in which the next $u_n$ is found by simply plugging in the number from the last box into $f(x).$ The function is periodic every $4$ terms. $2002 \equiv 2\pmod{4}$ , and counting $4$ starting from $u_1$ will give us our answer of $\boxed{\textbf{(B) } 2}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .