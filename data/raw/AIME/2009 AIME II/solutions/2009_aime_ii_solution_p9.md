# 2009 AIME II Problem 9

## Problem

Let $m$ be the number of solutions in positive integers to the equation $4x+3y+2z=2009$ , and let $n$ be the number of solutions in positive integers to the equation $4x+3y+2z=2000$ . Find the remainder when $m-n$ is divided by $1000$ .

## Solution

## Solution 1
It is actually reasonably easy to compute $m$ and $n$ exactly.
First, note that if $4x+3y+2z=2009$ , then $y$ must be odd. Let $y=2y'-1$ . We get $4x + 6y' - 3 + 2z = 2009$ , which simplifies to $2x + 3y' + z = 1006$ . For any pair of positive integers $(x,y')$ such that $2x + 3y' < 1006$ we have exactly one $z$ such that the equality holds. Hence we need to count the pairs $(x,y')$ .
For a fixed $y'$ , $x$ can be at most $\left\lfloor \dfrac{1005-3y'}2 \right\rfloor$ . Hence the number of solutions is
\begin{align*} m & = \sum_{y'=1}^{334} \left\lfloor \dfrac{1005-3y'}2 \right\rfloor \\ & = 501 + 499 + 498 + 496 + \cdots + 6 + 4 + 3 + 1 \\ & = 1000 + 994 + \cdots + 10 + 4 \\ & = 83834 \end{align*}
Similarly, we can compute that $n=82834$ , hence $m-n = 1000 \equiv \boxed{000} \pmod{1000}$ .

## Solution 2
We can avoid computing $m$ and $n$ , instead we will compute $m-n$ directly.
Note that $4x+3y+2z=2009$ if and only if $4(x-1)+3(y-1)+2(z-1)=2000$ . Hence there is an almost 1-to-1 correspondence between the positive integer solutions of the two equations. The only exceptions are the solutions of the first equation in which at least one of the variables is equal to $1$ . The value $m-n$ is the number of such solutions.
If $x=1$ , we get the equation $3y+2z=2005$ . The variable $y$ must be odd, and it must be between $1$ and $667$ , inclusive. For each such $y$ there is exactly one valid $z$ . Hence in this case there are $334$ valid solutions.
If $y=1$ , we get the equation $4x+2z=2006$ , or equivalently $2x+z=1003$ . The variable $x$ must be between $1$ and $501$ , inclusive, and for each such $x$ there is exactly one valid $z$ . Hence in this case there are $501$ valid solutions.
If $z=1$ , we get the equation $4x+3y=2007$ . The variable $y$ must be odd, thus let $y=2u-1$ . We get $4x+6u=2010$ , or equivalently, $2x+3u=1005$ . Again, we see that $u$ must be odd, thus let $u=2v-1$ . We get $2x+6v=1008$ , which simplifies to $x+3v=504$ . Now, we see that $v$ must be between $1$ and $167$ , inclusive, and for each such $v$ we have exactly one valid $x$ . Hence in this case there are $167$ valid solutions.
Finally, we must note that there are two special solutions: one with $x=y=1$ , and one with $y=z=1$ . We counted each of them twice, hence we have to subtract two from the total.
Therefore $m-n = 334 + 501 + 167 - 2 = 1000$ , and the answer is $1000\bmod 1000 = \boxed{000}$ .

## Solution 3
In this solution we will perform a similar operation as in Solution 2, but only on $y$ : $4x+3y+2z=2009$ if and only if $4x+3(y-3)+2z=2000$ . There is a one-to-one correspondence between the solutions of these two equations. Let $y'=y-3$ and require $y'$ to be positive as well. Then the second equation becomes $4x+3y'+2z=2000$ . Notice that there are several "extra" solutions in the first equation that cannot be included in the second equation (since that would make $y'$ non-positive). The value $m-n$ is therefore the number of "extra" solutions.
Since $y'=y-3$ , in order for $y'$ to be non-positive $1 \leq y \leq 3$ . However, equation (1) requires y to be odd, so we have two cases to consider: $y=1$ and $y=3$ . This results in the two equations $4x+3+2z=2009$ and $4x+9+2z=2009$ .
$4x+3+2z=2009$ simplifies to $2x+z=1003$ . There is exactly one valid $z$ for each $x$ ; $x$ must be between $1$ and $501$ (inclusive) to obtain positive integer solutions. Therefore, there are $501$ solutions in this case.
$4x+9+2z=2009$ simplifies to $2x+z=1000$ . There is exactly one valid $z$ for each $x$ ; $x$ must be between $1$ and $499$ (inclusive) to obtain positive integer solutions. Therefore, there are $499$ solutions in this case.
Thus, $m-n = 501 + 499 = 1000; 1000 \equiv \boxed{000} \pmod{1000}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.