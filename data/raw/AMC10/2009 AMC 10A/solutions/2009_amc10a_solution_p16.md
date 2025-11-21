# 2009 AMC 10A Problem 16

## Problem

Let $a$ , $b$ , $c$ , and $d$ be real numbers with $|a-b|=2$ , $|b-c|=3$ , and $|c-d|=4$ . What is the sum of all possible values of $|a-d|$ ?

$\mathrm{(A)}\ 9 \qquad \mathrm{(B)}\ 12 \qquad \mathrm{(C)}\ 15 \qquad \mathrm{(D)}\ 18 \qquad \mathrm{(E)}\ 24$

## Solution 1
From $|a-b|=2$ we get that $a=b\pm 2$
Similarly, $b=c\pm3$ and $c=d\pm4$ .
Substitution gives $a=d\pm 4\pm 3\pm 2$ . This gives $|a-d|=|\pm 4\pm 3\pm 2|$ . There are $2^3=8$ possibilities for the value of $\pm 4\pm 3\pm2$ :
$4+3+2=9$ ,
$4+3-2=5$ ,
$4-3+2=3$ ,
$-4+3+2=1$ ,
$4-3-2=-1$ ,
$-4+3-2=-3$ ,
$-4-3+2=-5$ ,
$-4-3-2=-9$
Therefore, the only possible values of $|a-d|$ are $9$ , $5$ , $3$ , and $1$ . Their sum is $\boxed{\textbf{(D) } 18}$ .

## Solution 2
If we add the same constant to all of $a$ , $b$ , $c$ , and $d$ , we will not change any of the differences. Hence we can assume that $a=0$ .
From $|a-b|=2$ we get that $|b|=2$ , hence $b\in\{-2,2\}$ .
If we multiply all four numbers by $-1$ , we will not change any of the differences. (This is due to the fact that we are calculating $|d|$ at the end ~Williamgolly) WLOG we can assume that $b=2$ .
From $|b-c|=3$ we get that $c\in\{-1,5\}$ .
From $|c-d|=4$ we get that $d\in\{-5,1,3,9\}$ .
Hence $|a-d|=|d|\in\{1,3,5,9\}$ , and the sum of possible values is $1+3+5+9 = \boxed{\textbf{(D) }18}$ .

## Solution 3
Let \[\begin{cases} |a-b| = 2, \\ |b-c| = 3, \\ |c-d| = 4, \\ |d-a| = X. \\ \end{cases}\] Note that we have \[\begin{cases} a-b = \pm 2, \\ b-c = \pm 3, \\ c-d = \pm 4 \\ d-a = \pm X, \\ \end{cases} \ \ \implies\] \[\pm X \pm 2 \pm 3 \pm 4 = 0, \ \ \implies X \pm 2 \pm 3 \pm 4 = 0,\] from which it follows that \[X = \pm 4 \pm 3 \pm 2.\]
Note that $X = |a-d|$ must be positive however, the only arrangements of $+$ and $-$ signs on the RHS which make $X$ positive are \[(4, 3, 2) \ \ \implies \ \ X = 9\] \[(4, 3, -2) \ \ \implies \ \ X = 5\] \[(4, -3, 2) \ \ \implies \ \ X = 3\] \[(-4, 3, 2) \ \ \implies \ \ X = 1.\] (There are no cases with $2$ or more negative as $4-3-2<0.$ )
Thus, the answer is \[1+3+5+9 = \boxed{\textbf{(D) }18}.\]

## Solution 4
Let $a=0$ .
Then $\begin{cases} b=2 \\ b=-2 \\ \end{cases}$
Thus $\begin{cases} c=5 \\ c=-1 \\ c=1 \\ c=-5 \\ \end{cases}$
Therefore $\begin{cases} d=9 \\ d=1 \\ d=3 \\ d=-5 \\ d=5 \\ d=-3 \\ d=-1 \\ d=-9 \\ \end{cases}$
So $|a-d|=1, 9, 3, 5$ and the sum is $\boxed{\textbf{(D) } 18}$ .
~JH. L

## Video Solution
https://youtu.be/z_W-Z9CHPR4
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .