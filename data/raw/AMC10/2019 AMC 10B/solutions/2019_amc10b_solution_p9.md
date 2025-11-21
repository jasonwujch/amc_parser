# 2019 AMC 10B Problem 9

## Problem

The function $f$ is defined by \[f(x) = \lfloor|x|\rfloor - |\lfloor x \rfloor|\] for all real numbers $x$ , where $\lfloor r \rfloor$ denotes the greatest integer less than or equal to the real number $r$ . What is the range of $f$ ?

$\textbf{(A) } \{-1, 0\} \qquad\textbf{(B) } \text{The set of nonpositive integers} \qquad\textbf{(C) } \{-1, 0, 1\} \qquad\textbf{(D) } \{0\} \qquad \textbf{(E) } \text{The set of nonnegative integers}$

## Solution 1
There are four cases we need to consider here.
Case 1 : $x$ is a positive integer. Without loss of generality, assume $x=1$ . Then $f(1) = 1 - 1 = 0$ .
Case 2 : $x$ is a positive fraction. Without loss of generality, assume $x=\frac{1}{2}$ . Then $f\left(\frac{1}{2}\right) = 0 - 0 = 0$ .
Case 3 : $x$ is a negative integer. Without loss of generality, assume $x=-1$ . Then $f(-1) = 1 - 1 = 0$ .
Case 4 : $x$ is a negative fraction. Without loss of generality, assume $x=-\frac{1}{2}$ . Then $f\left(-\frac{1}{2}\right) = 0 - 1 = -1$ .
Thus the range of the function $f$ is $\boxed{\textbf{(A) } \{-1, 0\}}$ .
~IronicNinja

## Solution 2
It is easily verified that when $x$ is an integer, $f(x)$ is zero. We therefore need only to consider the case when $x$ is not an integer.
When $x$ is positive, $\lfloor x\rfloor \geq 0$ , so \[\begin{split}f(x)&=\lfloor|x|\rfloor-|\lfloor x\rfloor| \\ &=\lfloor x\rfloor-\lfloor x\rfloor \\ &=0\end{split}\]
When $x$ is negative, let $x=-a-b$ be composed of integer part $a$ and fractional part $b$ (both $\geq 0$ ): \[\begin{split}f(x)&=\lfloor|-a-b|\rfloor-|\lfloor -a-b\rfloor| \\ &=\lfloor a+b\rfloor-|-a-1| \\ &=a-(a+1)=-1\end{split}\]
Thus, the range of x is $\boxed{\textbf{(A) } \{-1, 0\}}$ .
Note : One could solve the case of $x$ as a negative non-integer in this way: \[\begin{split}f(x)&=\lfloor|x|\rfloor-|\lfloor x\rfloor| \\ &=\lfloor -x\rfloor-|-\lfloor -x\rfloor-1| \\ &=\lfloor -x\rfloor-(\lfloor -x\rfloor+1) = -1\end{split}\]

## Solution 3 (Formal)
Let { $x$ } denote the fractional part of $x$ ; for example, { $2.7$ } $= 0.7$ , and { $-1.3$ } $= 0.3$ . Then for $x \geq 0$ , $x = \lfloor x \rfloor +$ { $x$ } and for $x < 0$ , $x = \lfloor x \rfloor + 1 -$ { $x$ }.
Now we can rewrite $\lfloor |x| \rfloor - |\lfloor x \rfloor|$ , breaking the expression up based on whether $x \geq 0$ or $x < 0$ .
For $x \geq 0$ , the above expression is equal to $\lfloor |\lfloor x \rfloor +$ { $x$ } $| \rfloor - | \lfloor \lfloor x \rfloor +$ { $x$ } $\rfloor | \implies \lfloor \lfloor x \rfloor +$ { $x$ } $\rfloor - | \lfloor x \rfloor |$
$\implies \lfloor x \rfloor - \lfloor x \rfloor = \mathbf{0}$ .
For $x < 0$ , the expression is equal to $\lfloor |\lfloor x \rfloor + 1 -$ { $x$ } $| \rfloor - | \lfloor \lfloor x \rfloor + 1 -$ { $x$ } $\rfloor |$
$\implies \lfloor - \lfloor x \rfloor - 1 +$ { $x$ } $\rfloor - | \lfloor x \rfloor | \implies - \lfloor x \rfloor - 1 - (- \lfloor x \rfloor) = \mathbf{-1}$ .
Therefore the only two possible values for $f(x)$ , and thus the range of the function, is $\boxed{\textbf{(A) } \{-1, 0\}}$ .
~KingRavi

## Solution 4
We have 2 cases: either $x$ is positive or $x$ is negative.
Case 1 - x is positive:
Let $x = n + f$ , where $n$ is a positive integer and $f$ is a positive real number between 0 and 1. We have \[\lfloor |x| \rfloor = \lfloor |n+f| \rfloor = \lfloor n+f \rfloor = n\] and \[|\lfloor x \rfloor| = |\lfloor n+f \rfloor| = |n| = n.\] $n-n=0$ , so the possible value of $f(x)$ if $x$ is positive is $0$ .
Case 2 - x is negative:
Let $x = -n - f$ , where $n$ is a positive integer and $f$ is a positive real number between 0 and 1. We have \[\lfloor |x| \rfloor = \lfloor |-n-f| \rfloor = \lfloor n+f \rfloor = n\] and \[|\lfloor x \rfloor| = |\lfloor -n-f \rfloor| =|-n|\:or\: |-n-1|= n \:or\: n+1.\]
$n-n=0$ and $n-(n+1) = -1$ , so the possible values of $f(x)$ if $x$ is negative are $0$ and $-1.$
Hence, the possible values of $f(x)$ are $0$ and $-1$ , so the answer is $\boxed{\textbf{(A) } \{-1, 0\}}$ . ~azc1027

## Video Solution
https://youtu.be/LffjyNNqf14
~Education, the Study of Everything

## Video Solution
https://youtu.be/PgqjsTkNYdc
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .