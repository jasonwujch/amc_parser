# 2021 Fall AMC 10B Problem 22

## Problem

For each integer $n\geq 2$ , let $S_n$ be the sum of all products $jk$ , where $j$ and $k$ are integers and $1\leq j<k\leq n$ . What is the sum of the 10 least values of $n$ such that $S_n$ is divisible by $3$ ?

$\textbf{(A)}\ 196\qquad\textbf{(B)}\ 197\qquad\textbf{(C)}\ 198\qquad\textbf{(D)}\ 199\qquad\textbf{(E)}\ 200$

## Solution 1
To get from $S_n$ to $S_{n+1}$ , we add $1(n+1)+2(n+1)+\cdots +n(n+1)=(1+2+\cdots +n)(n+1)=\frac{n(n+1)^2}{2}$ .
Now, we can look at the different values of $n$ mod $3$ . For $n\equiv 0\pmod{3}$ and $n\equiv 2\pmod{3}$ , then we have $\frac{n(n+1)^2}{2}\equiv 0\pmod{3}$ . However, for $n\equiv 1\pmod{3}$ , we have \[\frac{1\cdot {2}^2}{2}\equiv 2\pmod{3}.\]
Clearly, $S_2\equiv 2\pmod{3}.$ Using the above result, we have $S_5\equiv 1\pmod{3}$ , and $S_8$ , $S_9$ , and $S_{10}$ are all divisible by $3$ . After $3\cdot 3=9$ , we have $S_{17}$ , $S_{18}$ , and $S_{19}$ all divisible by $3$ , as well as $S_{26}, S_{27}, S_{28}$ , and $S_{35}$ . Thus, our answer is $8+9+10+17+18+19+26+27+28+35=27+54+81+35=162+35=\boxed{\mathrm{(B)}\ 197} .$ -BorealBear
-minor edit by Yiyj1

## Solution 2 (bash)
Since we have a wonky function, we start by trying out some small cases and see what happens. If $j$ is $1$ and $k$ is $2$ , then there is one case. We have $2$ mod $3$ for this case. If $N$ is $3$ , we have $1 \cdot 2 + 1 \cdot 3 + 2 \cdot 3$ which is still $2$ mod $3$ . If $N$ is $4$ , we have to add $1 \cdot 4 + 2 \cdot 4 + 3 \cdot 4$ which is a multiple of $3$ , meaning that we are still at $2$ mod $3$ . If we try a few more cases, we find that when $N$ is $8$ , we get a multiple of $3$ . When $N$ is $9$ , we are adding $0$ mod $3$ , and therefore, we are still at a multiple of $3$ .
When $N$ is $10$ , then we get $0$ mod $3$ + $10(1+2+3+...+9)$ which is $10$ times a multiple of $3$ . Therefore, we have another multiple of $3$ . When $N$ is $11$ , so we have $2$ mod $3$ . So, every time we have $-1$ mod $9$ , $0$ mod $9$ , and $1$ mod $9$ , we always have a multiple of $3$ . Think about it: When $N$ is $1$ , it will have to be $0 \cdot 1$ , so it is a multiple of $3$ . Therefore, our numbers are $8, 9, 10, 17, 18, 19, 26, 27, 28, 35$ . Adding the numbers up, we get $\boxed{\textbf{(B) 197}}$
~Arcticturn

## Solution 3
Denote $A_{n, <} = \left\{ \left( j , k \right) : 1 \leq j < k \leq n \right\}$ , $A_{n, >} = \left\{ \left( j , k \right) : 1 \leq k < j \leq n \right\}$ and $A_{n, =} = \left\{ \left( j , k \right) : 1 \leq j = k \leq n \right\}$ .
Hence, $\sum_{\left( j , k \right) \in A_{n,<}} jk = \sum_{\left( j , k \right) \in A_{n,>}} jk = S_n$ .
Therefore, \begin{align*} S_n & = \frac{1}{2} \left( \sum_{\left( j , k \right) \in A_{n,<}} jk = \sum_{\left( j , k \right) \in A_{n,>}} jk \right) \\ & = \frac{1}{2} \left( \sum_{1 \leq j, k \leq n} jk - {\left( j , k \right) \in A_{n,=}} jk \right) \\ & = \frac{1}{2} \left( \sum_{j=1}^n \sum_{k=1}^n jk - \sum_{j=1}^n j^2 \right) \\ & = \frac{1}{2} \left( \frac{n^2 \left( n + 1 \right)^2}{4} - \frac{n \left( n + 1 \right) \left( 2 n + 1 \right) }{6} \right) \\ & = \frac{\left( n - 1 \right) n \left( n + 1 \right) \left( 3 n + 2 \right)}{24} . \end{align*}
Hence, $S_n$ is divisible by 3 if and only if $\left( n - 1 \right) n \left( n + 1 \right) \left( 3 n + 2 \right)$ is divisible by $24 \cdot 3 = 8 \cdot 9$ .
First, $\left( n - 1 \right) n \left( n + 1 \right) \left( 3 n + 2 \right)$ is always divisible by 8. Otherwise, $S_n$ is not even an integer.
Second, we find conditions for $n$ , such that $\left( n - 1 \right) n \left( n + 1 \right) \left( 3 n + 2 \right)$ is divisible by 9.
Because $3 n + 2$ is not divisible by 3, it cannot be divisible by 9.
Hence, we need to find conditions for $n$ , such that $\left( n - 1 \right) n \left( n + 1 \right)$ is divisible by 9. This holds of $n \equiv 0, \pm 1 \pmod{9}$ .
Therefore, the 10 least values of $n$ such that $\left( n - 1 \right) n \left( n + 1 \right)$ is divisible by 9 (equivalently, $S_n$ is divisible by 3) are 8, 9, 10, 17, 18, 19, 26, 27, 28, 35. Their sum is 197.
Therefore, the answer is $\boxed{\textbf{(B) }197}$ .
~Steven Chen (www.professorchenedu.com)

## Video Solution by Interstigation
https://youtu.be/_PDIrta6r8s
~Interstigation

## Video Solution 2 by WhyMath
https://youtu.be/M8tF1uSOfXA
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .