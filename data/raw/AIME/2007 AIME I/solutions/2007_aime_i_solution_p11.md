# 2007 AIME I Problem 11

## Problem

For each positive integer $p$ , let $b(p)$ denote the unique positive integer $k$ such that $|k-\sqrt{p}| < \frac{1}{2}$ . For example, $b(6) = 2$ and $b(23) = 5$ . If $S = \sum_{p=1}^{2007} b(p),$ find the remainder when $S$ is divided by 1000.

## Solution 1
$\left(k- \frac 12\right)^2=k^2-k+\frac 14$ and $\left(k+ \frac 12\right)^2=k^2+k+ \frac 14$ . Therefore $b(p)=k$ if and only if $p$ is in this range, or $k^2-k<p\leq k^2+k$ . There are $2k$ numbers in this range, so the sum of $b(p)$ over this range is $(2k)k=2k^2$ . $44<\sqrt{2007}<45$ , so all numbers $1$ to $44$ have their full range. Summing this up with the formula for the sum of the first $n$ squares ( $\frac{n(n+1)(2n+1)}{6}$ ), we get $\sum_{k=1}^{44}2k^2=2\frac{44(44+1)(2*44+1)}{6}=58740$ . We need only consider the $740$ because we are working with modulo $1000$ .
Now consider the range of numbers such that $b(p)=45$ . These numbers are $\left\lceil\frac{44^2 + 45^2}{2}\right\rceil = 1981$ to $2007$ . There are $2007 - 1981 + 1 = 27$ (1 to be inclusive) of them. $27*45=1215$ , and $215+740= \boxed{955}$ , the answer.

## Solution 2
Let $p$ be in the range of $a^2 \le p < (a+1)^2$ . Then, we need to find the point where the value of $b(p)$ flips from $k$ to $k+1$ . This will happen when $p$ exceeds $(a+\frac{1}{2})^2$ or $a(a+1)+\frac{1}{4}$ . Thus, if $a^2 \le p \le a(a+1)$ then $b(p)=a$ . For $a(a+1) < p < (a+1)^2$ , then $b(p)=a+1$ . There are $a+1$ terms in the first set of $p$ , and $a$ terms in the second set. Thus, the sum of $b(p)$ from $a^2 \le p <(a+1)^2$ is $2a(a+1)$ or $4\cdot\binom{a+1}{2}$ . For the time being, consider that $S = \sum_{p=1}^{44^2-1} b(p)$ . Then, the sum of the values of $b(p)$ is $4\binom{2}{2}+4\binom{3}{2}+\cdots +4\binom{44}{2}=4\left(\binom{2}{2}+\binom{3}{2}+\cdots +\binom{44}{2}\right)$ . We can collapse this to $4\binom{45}{3}=56760$ . Now, we have to consider $p$ from $44^2 \le p < 2007$ . Considering $p$ from just $44^2 \le p \le 1980$ , we see that all of these values have $b(p)=44$ . Because there are $45$ values of $p$ in that range, the sum of $b(p)$ in that range is $45\cdot44=1980$ . Adding this to $56760$ we get $58740$ or $740$ mod $1000$ . Now, take the range $1980 < p \le 2007$ . There are $27$ values of $p$ in this range, and each has $b(p)=45$ . Thus, that contributes $27*45=1215$ or $215$ to the sum. Finally, adding $740$ and $215$ we get $740+215=\boxed{955}$ .
~firebolt360

## Video Solution
2007 AIME I #11
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.