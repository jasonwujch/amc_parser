# 2014 AMC 10B Problem 14

## Problem

Danica drove her new car on a trip for a whole number of hours, averaging $55$ miles per hour. At the beginning of the trip, $abc$ miles was displayed on the odometer, where $abc$ is a $3$ -digit number with $a\ge1$ and $a+b+c\le7$ . At the end of the trip, the odometer showed $cba$ miles. What is $a^2+b^2+c^2$ ?

$\textbf {(A) } 26 \qquad \textbf {(B) } 27 \qquad \textbf {(C) } 36 \qquad \textbf {(D) } 37 \qquad \textbf {(E) } 41$

## Solution 1
Let $h$ be the number of hours Danica drove. Note that $abc$ can be expressed as $100\cdot a+10\cdot b+c$ . From the given information, we have $100a+10b+c+55h=100c+10b+a$ . This can be simplified into $99a+55h=99c$ by subtraction, which can further be simplified into $9a+5h=9c$ by dividing both sides by $11$ . Thus we must have $h\equiv0\pmod9$ . However, if $h\ge 15$ , then $\text{min}\{c\}\ge\frac{9+5(15)}{9}>9$ , which is impossible since $c$ must be a digit. The only value of $h$ divisible by $9$ and less than or equal to $14$ is $h=9$ .
From this information, $9a+5(9)=9c\Rightarrow a+5=c$ . Combining this with the inequalities $a+b+c\le7$ and $a\ge1$ , we have $a+b+a+5\le7\Rightarrow 2a+b\le2$ , which implies $a=1$ , so $b=0$ , and $c=6$ . Thus $a^2+b^2+c^2=1+0+36=\fbox{37 \textbf{(D)}}$

## Solution 2
Danica drives $m$ miles, such that $m>0$ and $m$ is a multiple of 55. Therefore, $m$ must have an units digit of either $0$ or $5.$ If the units digit of $m$ is $0,$ then $a=c$ which would imply that Danica did not drive at all. Thus, $c>a.$ Therefore, $|a-c|=5,$ and because $a+b+c\leq7, c>a,$ we have $(a,c)=(1,6).$ Finally, $b$ then must be $0$ due to $a+b+c\leq 7,$ and $a^2+b^2+c^2=1^2+0^2+6^2=\fbox{\textbf{(D) }37}$

## Solution 3
We can set up an algebraic equation for this problem.
From what's given, we have that $100c+10b+a=55x+100a+10b+c$
This simplifies to be $0=55x+99a-99c\implies -55x=99a-99c$
Factoring, we get that $-55x=99(a-c)\implies x=-\frac{9(a-c)}{5}$
Hence, notice that we want $a-c=-5$ so that $x=9$
The only pair that works for this problem that satisfies the original requirements is $(1,6)$
Hence, $a=1, b=0, c=6$
Checking, we have that $106+55(9)=601\implies 601=601$
Hence, the answer is $1^2+0^2+6^2=37\implies\boxed{D}$

## Video Solution
https://youtu.be/C0erYBsw5KI
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .