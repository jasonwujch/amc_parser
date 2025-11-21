# 2016 AMC 10B Problem 25

## Problem

Let $f(x)=\sum_{k=2}^{10}(\lfloor kx \rfloor -k \lfloor x \rfloor)$ , where $\lfloor r \rfloor$ denotes the greatest integer less than or equal to $r$ . How many distinct values does $f(x)$ assume for $x \ge 0$ ?

$\textbf{(A)}\ 32\qquad\textbf{(B)}\ 36\qquad\textbf{(C)}\ 45\qquad\textbf{(D)}\ 46\qquad\textbf{(E)}\ \text{infinitely many}$

## Solution 1
Since $x = \lfloor x \rfloor + \{ x \}$ , we have
\[f(x) = \sum_{k=2}^{10} (\lfloor k \lfloor x \rfloor +k \{ x \} \rfloor - k \lfloor x \rfloor)\]
The function can then be simplified into
\[f(x) = \sum_{k=2}^{10} ( k \lfloor x \rfloor + \lfloor k \{ x \} \rfloor - k \lfloor x \rfloor)\]
which becomes
\[f(x) = \sum_{k=2}^{10} \lfloor k \{ x \} \rfloor\]
We can see that for each value of $k$ , $\lfloor k \{ x \} \rfloor$ can equal integers from $0$ to $k-1$ .
Clearly, the value of $\lfloor k \{ x \} \rfloor$ changes only when $\{ x \}$ is equal to any of the fractions $\frac{1}{k}, \frac{2}{k} \dots \frac{k-1}{k}$ .
So we want to count how many distinct fractions less than $1$ have the form $\frac{m}{n}$ where $n \le 10$ . Explanation for this is provided below. We can find this easily by computing
\[\sum_{k=2}^{10} \phi(k)\]
where $\phi(k)$ is the Euler Totient Function . Basically $\phi(k)$ counts the number of fractions with $k$ as its denominator (after simplification). This comes out to be $31$ .
Because the value of $f(x)$ is at least $0$ and can increase $31$ times, there are a total of $\fbox{\textbf{(A)}\ 32}$ different possible values of $f(x)$ .
### Explanation:
Arrange all such fractions in increasing order and take a current $\frac{m}{n}$ to study. Let $p$ denote the previous fraction in the list and $x_\text{old}$ ( $0 \le x_\text{old} < k$ for each $k$ ) be the largest so that $\frac{x_\text{old}}{k} \le p$ . Since $\text{ }\text{ }\frac{m}{n} > p$ , we clearly have all $x_\text{new} \ge x_\text{old}$ . Therefore, the change must be nonnegative.
But among all numerators coprime to $n$ so far, $m$ is the largest. Therefore, choosing $\frac{m}{n}$ as ${x}$ increases the value $\lfloor n \{ x \} \rfloor$ . Since the overall change in $f(x)$ is positive as fractions $m/n$ increase, we deduce that all such fractions correspond to different values of the function.
Minor Latex Edits made by MathWizard10.
### Supplement
Here are all the distinct $\frac{m}{n}$ and $\phi(k):$
When $n=2$ , $\frac{m}{n}=\frac{1}{2}$ . $\phi(2)=1$
When $n=3$ , $\frac{m}{n}=\frac{1}{3}$ , $\frac{2}{3}$ . $\phi(3)=2$
When $n=4$ , $\frac{m}{n}=\frac{1}{4}$ , $\frac{3}{4}$ . $\phi(4)=2$
When $n=5$ , $\frac{m}{n}=\frac{1}{5}$ , $\frac{2}{5}$ , $\frac{3}{5}$ , $\frac{4}{5}$ . $\phi(5)=4$
When $n=6$ , $\frac{m}{n}=\frac{1}{6}$ , $\frac{5}{6}$ . $\phi(6)=2$
When $n=7$ , $\frac{m}{n}=\frac{1}{7}$ , $\frac{2}{7}$ , $\frac{3}{7}$ , $\frac{4}{7}$ , $\frac{5}{7}$ , $\frac{6}{7}$ . $\phi(7)=6$
When $n=8$ , $\frac{m}{n}=\frac{1}{8}$ , $\frac{3}{8}$ , $\frac{5}{8}$ , $\frac{7}{8}$ . $\phi(8)=4$
When $n=9$ , $\frac{m}{n}=\frac{1}{9}$ , $\frac{2}{9}$ , $\frac{4}{9}$ , $\frac{5}{9}$ , $\frac{7}{9}$ , $\frac{8}{9}$ . $\phi(9)=6$
When $n=10$ , $\frac{m}{n}=\frac{1}{10}$ , $\frac{3}{10}$ , $\frac{7}{10}$ , $\frac{9}{10}$ . $\phi(10)=4$
$\sum_{k=2}^{10} \phi(k)=31$
$31+1=\fbox{\textbf{(A)}\ 32}$
~ isabelchen

## Solution 2
$x = \lfloor x \rfloor + \{ x \}$ so we have \[f(x) = \sum_{k=2}^{10} \lfloor k \{ x \} \rfloor.\] Clearly, the value of $\lfloor k \{ x \} \rfloor$ changes only when $x$ is equal to any of the fractions $\frac{1}{k}, \frac{2}{k} \dots \frac{k-1}{k}$ . To get all the fractions, graphing this function gives us $46$ different fractions. But on average, about one is every three fractions are repetitions of another fraction (see below). This means there are a total of $\fbox{\textbf{(A)}\ 32}$ different possible values of $f(x)$ .
Note: This is because all fractions with denominators $2\le k \le 5$ are repetitions of another fraction with denominator $2k,$ which is about $\frac{1}{4}$ of all the fractions. Also, some other repeated fractions are scattered around the fractions with higher denominators. This means that we can safely estimate that about $\frac{1}{3}$ of the fractions are repetitions of another fraction.

## Solution 3 (Casework)
Solution $1$ is abstract. In this solution I will give a concrete explanation.
WLOG, for example, when $x$ increases from $\frac{2}{3}-\epsilon$ to $\frac{2}{3}$ , $\lfloor 3 \{ x \} \rfloor$ will increase from $1$ to $2$ , $\lfloor 6 \{ x \} \rfloor$ will increase from $3$ to $4$ , $\lfloor 9 \{ x \} \rfloor$ will increase from $5$ to $6$ . In total, $f(x)$ will increase by $3$ . Because $\frac{1}{3}=\frac{2}{6}=\frac{3}{9}$ , these $3$ numbers are actually $1$ distinct number to cause $f(x)$ to change. In general, when $x$ increases from $\frac{m}{n}-\epsilon$ to $\frac{m}{n}$ , $\lfloor k \{ x \} \rfloor$ will increse from $k \cdot \frac{m}{n} -1$ to $k \cdot \frac{m}{n}$ if $k \cdot \frac{m}{n}$ is an integer, and the value of $f(x)$ will change. So the total number of distinct values $f(x)$ could take is equal to the number of distinct values of $\frac{m}{n}$ , where $0 < \frac{m}{n}<1$ and $2 \le n \le 10$ .
Solution $1$ uses Euler Totient Function to count the distinct number of $\frac{m}{n}$ , I am going to use casework to count the distinct values of $\frac{m}{n}$ by not counting the duplicate ones.
When $n=10$ , $\frac{m}{n}=\frac{1}{10}$ , $\frac{2}{10}$ , $...$ , $\frac{9}{10}$ $\Longrightarrow 9$
When $n=9$ , $\frac{m}{n}=\frac{1}{9}$ , $\frac{2}{9}$ , $...$ , $\frac{8}{9}$ $\Longrightarrow 8$
When $n=8$ , $\frac{m}{n}=\frac{1}{8}$ , $\frac{2}{8}$ , $...$ , $\frac{7}{8}$ $\Longrightarrow 6$ ( $\frac{4}{8}$ is duplicate)
When $n=7$ , $\frac{m}{n}=\frac{1}{7}$ , $\frac{2}{7}$ , $...$ , $\frac{6}{7}$ $\Longrightarrow 6$
When $n=6$ , $\frac{m}{n}=\frac{1}{6}$ , $\frac{5}{6}$ $\Longrightarrow 2$ ( $\frac{2}{6}$ , $\frac{3}{6}$ , and $\frac{4}{6}$ is duplicate)
When $n=5$ , $4$ , $3$ , $2$ , all the $\frac{m}{n}$ is duplicate.
$9+8+6+6+2=31$ , $31+1=\fbox{\textbf{(A)}\ 32}$
~ isabelchen

## Solution 4
By Hermite's Identity ,
\begin{align*} & \lfloor kx \rfloor = \lfloor x \rfloor + \lfloor x + \frac1k \rfloor + \lfloor x + \frac2k \rfloor + \dots + \lfloor x + \frac{k-1}{k} \rfloor\\ & \lfloor kx \rfloor -k \lfloor x \rfloor = \lfloor x + \frac1k \rfloor + \lfloor x + \frac2k \rfloor + \dots + \lfloor x + \frac{k-1}{k} \rfloor - (k-1) \lfloor x \rfloor \end{align*}
Therefore, \begin{align*} \sum_{k=2}^{10}(\lfloor kx \rfloor -k \lfloor x \rfloor) & \\ &= \sum_{k=2}^{10}(\lfloor x + \frac1k \rfloor + \lfloor x + \frac2k \rfloor + \dots + \lfloor x + \frac{k-1}{k} \rfloor - (k-1) \lfloor x \rfloor)\\ &= \sum_{k=2}^{10}\sum_{i=1}^{k-1}( \lfloor x + \frac{i}{k} \rfloor - \lfloor x \rfloor)\\ &= \sum_{k=2}^{10}\sum_{i=1}^{k-1}( \lfloor \{ x \} + \frac{i}{k} \rfloor) \end{align*}
$0 \le \{ x \} < 1$ , $0 < \frac{j}{k}<1$ $\Longrightarrow$ $0 < \lfloor \{ x \} + \frac{i}{k} \rfloor < 2$ $\Longrightarrow$ $\lfloor \{ x \} + \frac{i}{k} \rfloor = 0 \text{ or } 1$
$\{ x \} + \frac{i}{k} \ge 1$ $\Longrightarrow$ $\{ x \} \ge 1 - \frac{j}{k}$
Arrange $1 - \frac{i_j}{k_j}$ from small to large, $\{ x \}$ must fall in one interval. WLOG, suppose $1 - \frac{i_n}{k_n} \le \{ x \} < 1- \frac{i_{n+1}}{k_{n+1}}$ .
if $j \le n$ , \[\lfloor \{ x \} + \frac{i_j}{k_j} \rfloor = 1\]
if $j > n$ , \[\lfloor \{ x \} + \frac{i_j}{k_j} \rfloor = 0\]
Therefore, every distinct value of $\sum_{k=2}^{10}\sum_{i=1}^{k-1}( \lfloor \{ x \} + \frac{i}{k} \rfloor)$ has one to one correspondence with a distinct value of $\frac{i}{k}$ , $\frac{i}{k}$ is not reducible, $(i, k) = 1$ .
Using the Euler Totient Function as in Solution 1's Supplement , the answer is $\fbox{\textbf{(A)}\ 32}$
~ isabelchen

## Solution 5 (No Euler Totient Function)
Solution without the Euler Totient Function
Proceed in the same way as Solution 1 until you reach \[f(x) = \sum_{k=2}^{10} \lfloor k \{ x \} \rfloor\] .
We first count the case where all values of $\lfloor kx_f \rfloor$ is 0. Now, notice that the value of $n/k$ can take $k-1$ values (excluding 0) since $n$ must be strictly less than $k$ . If we add up all $k-1$ for $2<=k<=10$ , we get $1+2+3+...+9 = 45$ .
Some might be tempted to mark $45$ or $46$ now, but there can be repeating values. Notice that whenever the value of $(1/2)x_f$ changes, the value of $(1/8)x_f$ must change. This means that every case in $k=2$ is covered by $k=8$ . This is extended to every number that is a factor of another (3 and 9, 5 and 10). Therefore, we can eliminate $k=2,3,4,5$ as they are all factors of other values of $k$ , which eliminates 10 cases.
Within the remaining numbers, there are a couple of numbers that can still have repeating values. These are $(6, 9)$ , $(6, 8)$ , and $(8,10)$ . The first one repeats when $n/k$ is equal to $1/3$ or $2/3$ , eliminating 2 cases, and the second and third repeat whenever $n/k$ is equal to $1/2$ . This eliminates another 2 cases.
Therefore, our final answer is $45+1-10-2-2=32$ , which is $\fbox{\textbf{(A)}\ 32}$ .
### Remark
This problem is similar to 1985 AIME Problem 10 . Both problems use the Euler Totient Function to find the number of distinct values of $\lfloor k \{ x \} \rfloor$ .
~ isabelchen

## Video Solution
https://www.youtube.com/watch?v=zXJrdDtZNbw
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .