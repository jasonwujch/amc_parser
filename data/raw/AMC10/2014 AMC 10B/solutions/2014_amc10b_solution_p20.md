# 2014 AMC 10B Problem 20

## Problem

For how many integers $x$ is the number $x^4-51x^2+50$ negative?

$\textbf {(A) } 8 \qquad \textbf {(B) } 10 \qquad \textbf {(C) } 12 \qquad \textbf {(D) } 14 \qquad \textbf {(E) } 16$

## Solution 1
First, note that $50+1=51$ , so we factor the polynomial as $(x^2-50)(x^2-1)$ .
Since this expression is negative, one term must be negative and the other positive. We note that the first term is a lot smaller than the second, so we get $x^2-50<0<x^2-1$ .
Solving this inequality, we find $1<x^2<50$ . There are exactly $12$ integers $x$ that satisfy this inequality, $\pm \{2,3,4,5,6,7\}$ .
Thus our answer is $\boxed{\textbf {(C) } 12}$ .
~Clarity edits by SwordAxe

## Solution 2
Since the $x^4-51x^2$ part of $x^4-51x^2+50$ has to be less than $-50$ (because we want $x^4-51x^2+50$ to be negative), we have the inequality $x^4-51x^2<-50 \rightarrow x^2(x^2-51) <-50$ . $x^2$ has to be positive, so $(x^2-51)$ is negative. Then we have $x^2<51$ . We know that if we find a positive number that works, it's parallel negative will work. Therefore, we just have to find how many positive numbers work, then multiply that by $2$ . If we try $1$ , we get $1^4-51(1)^4+50 = -50+50 = 0$ , and $0$ therefore doesn't work. Test two on your own, and then proceed. Since two works, all numbers above $2$ that satisfy $x^2<51$ work, that is the set { ${2,3,4,5,6,7}$ }. That equates to $6$ numbers. Since each numbers' negative counterparts work, $6\cdot2=\boxed{\textbf{(C) }12}$ .

## Solution 3 (Graph)
As with Solution $1$ , note that the quartic factors to $(x^2-50)\cdot(x^2-1)$ , which means that it has roots at $-5\sqrt{2}$ , $-1$ , $1$ , and $5\sqrt{2}$ . Now, because the original equation is of an even degree and has a positive leading coefficient, both ends of the graph point upwards, meaning that the graph dips below the $x$ -axis between $-5\sqrt{2}$ and $-1$ as well as $1$ and $5\sqrt{2}$ . $5\sqrt{2}$ is a bit more than $7$ ( $1.4\cdot 5=7$ ) and therefore means that $-7,-6,-5,-4,-3,-2,2,3,4,5,6,7$ all give negative values.

## Solution 4
Let $x^{2}=u$ . Then the expression becomes $u^{2}-51u+50$ which can be factored as $\left(u-1\right)\left(u-50\right)$ . Since the expression is negative, one of $\left(u-1\right)$ and $\left(u-50\right)$ need to be negative. $u-1>u-50$ , so $u-1>0$ and $u-50<0$ , which yields the inequality $50>u>1$ . Remember, since $u=x^{2}$ where $x$ is an integer, this means that $u$ is a perfect square between $1$ and $50$ . There are $6$ values of $u$ that satisfy this constraint, namely $4$ , $9$ , $16$ , $25$ , $36$ , and $49$ . Solving each of these values for $x$ yields $12$ values (as $x$ can be negative or positive) $\Longrightarrow \boxed{\textbf {(C) } 12}$ . ~JH. L
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .