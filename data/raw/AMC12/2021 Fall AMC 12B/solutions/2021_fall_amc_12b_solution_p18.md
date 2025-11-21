# 2021 Fall AMC 12B Problem 18

## Problem

Set $u_0 = \frac{1}{4}$ , and for $k \ge 0$ let $u_{k+1}$ be determined by the recurrence \[u_{k+1} = 2u_k - 2u_k^2.\]

This sequence tends to a limit; call it $L$ . What is the least value of $k$ such that \[|u_k-L| \le \frac{1}{2^{1000}}?\]

$\textbf{(A)}\: 10\qquad\textbf{(B)}\: 87\qquad\textbf{(C)}\: 123\qquad\textbf{(D)}\: 329\qquad\textbf{(E)}\: 401$

## Solution 1
Note that terms of the sequence $(u_k)$ lie in the interval $\left(0,\frac12\right)$ and are strictly increasing.
Since the sequence $(u_k)$ tends to the limit $L,$ we set $u_{k+1}=u_k=L>0.$
The given equation becomes \[L=2L-2L^2,\] from which $L=\frac12.$
The given inequality becomes \[\frac12-\frac{1}{2^{1000}} \leq u_k \leq \frac12+\frac{1}{2^{1000}},\] and we only need to consider $\frac12-\frac{1}{2^{1000}} \leq u_k.$
We have \begin{alignat*}{8} u_0 &= \phantom{1}\frac14 &&= \frac{2^1-1}{2^2}, \\ u_1 &= \phantom{1}\frac38 &&= \frac{2^2-1}{2^3}, \\ u_2 &= \ \frac{15}{32} &&= \frac{2^4-1}{2^5}, \\ u_3 &= \frac{255}{512} &&= \frac{2^8-1}{2^9}, \\ & \phantom{1111} \vdots \end{alignat*} By induction, it can be proven that \[u_k=\frac{2^{2^k}-1}{2^{2^k+1}}=\frac12-\frac{1}{2^{2^k+1}}.\] We substitute this into the inequality, then solve for $k:$ \begin{align*} \frac12-\frac{1}{2^{1000}} &\leq \frac12-\frac{1}{2^{2^k+1}} \\ -\frac{1}{2^{1000}} &\leq -\frac{1}{2^{2^k+1}} \\ 2^{1000} &\leq 2^{2^k+1} \\ 1000 &\leq 2^k+1. \end{align*} Since $2^9+1 \leq 1000 \leq 2^{10}+1,$ the least such value of $k$ is $\boxed{\textbf{(A)}\: 10}.$
~MRENTHUSIASM

## Solution 2
If we list out the first few values of $k$ , we get the series $\frac{1}{4}, \frac{3}{8}, \frac{15}{32}, \frac{255}{512}$ , which always seems to be a negative power of $2$ away from $\frac{1}{2}$ . We can test this out by setting $u_k=\frac{1}{2}-\frac{1}{2^{n_k}}$ , where $n_0=2$ .
Now, we get \begin{align*} u_{k+1} &= 2\cdot\left(\frac{1}{2}-\frac{1}{2^{n_{k}}}\right)-2\cdot\left(\frac{1}{2}-\frac{1}{2^{n_{k}}}\right)^2 \\ &= 1-\frac{1}{2^{n_k - 1}}-2\cdot\left(\frac{1}{4}-\frac{1}{2^{n_k}}+\frac{1}{2^{2 \cdot n_k}}\right)\\ &= 1-\frac{1}{2^{n_k - 1}}-\frac{1}{2}+\frac{1}{2^{n_k-1}}-\frac{1}{2^{2 \cdot n_k-1}} \\ &= \frac{1}{2}-\frac{1}{2^{2 \cdot n_k-1}}. \end{align*} This means that this series approaches $\frac{1}{2}$ , as the second term is decreasing. In addition, we find that $n_{k+1}=2 \cdot n_k-1$ .
We claim that $n_k = 2^k+1$ , which can be proven by induction:
Base Case
We have $n_0=2=2^0+1$ .
Induction Step
Assuming that the claim is true, we have $n_{k+1}=2 \cdot (2^k+1)-1=2^{k+1}+1$ .
It follows that $n_{10}=2^{10}+1>1000$ and $n_9=2^9+1<1000$ . Therefore, the least value of $k$ would be $\boxed{\textbf{(A)}\: 10}$ .
~ConcaveTriangle

## Solution 3
We are given $u_{k+1} = 2u_k - 2{u_k}^2$ . Multiply this equation by $2$ and subtract $1$ from both sides. The equations can then be written nicely as $2u_{k+1} - 1 = -(2u_k-1)^2$ . Let $v_k = 2u_k - 1$ so that $v_{k+1} = -(v_k)^2$ .
Clearly, $v_0 = 2u_0 - 1 = -\frac{1}{2}$ . Since the magnitude of $v_0$ is less than $1$ and because our recursive relation for $v_k$ squares the previous term (and negates it), we see that as $k \rightarrow \infty, 2u_k - 1 = v_k \rightarrow 0$ . This means $u_k \rightarrow \frac{1}{2}$ , so $L = \frac{1}{2}$ .
Isolating $u_k$ in our relation $2u_k - 1 = v_k$ gives us $u_k = \frac{v_k + 1}{2}$ . Substituting into the inequality, we have $\left|\frac{v_k + 1}{2}-\frac{1}{2}\right| \le \frac{1}{2^{1000}}$ . Rewriting this, we get $|v_k| \le \frac{1}{2^{999}}$ .
The sequence $\{v_k\}$ is much easier to handle because of its simple recursive relation. Writing out a few terms shows that $|v_k| = \frac{1}{2^{2^k}}$ . Now it just comes down to having $2^k > 999$ , so $k = \boxed{\textbf{(A)}\: 10}$ .
~chezpotato

## Video Solution
https://youtu.be/ZfHql_vhNes
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .