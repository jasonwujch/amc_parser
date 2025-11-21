# 2000 AIME I Problem 6

## Problem

For how many ordered pairs $(x,y)$ of integers is it true that $0 < x < y < 10^6$ and that the arithmetic mean of $x$ and $y$ is exactly $2$ more than the geometric mean of $x$ and $y$ ?

## Solutions

## Solution 1
\begin{eqnarray*} \frac{x+y}{2} &=& \sqrt{xy} + 2\\ x+y-4 &=& 2\sqrt{xy}\\ y - 2\sqrt{xy} + x &=& 4\\ \sqrt{y} - \sqrt{x} &=& \pm 2\end{eqnarray*}
Because $y > x$ , we only consider $+2$ .
For simplicity, we can count how many valid pairs of $(\sqrt{x},\sqrt{y})$ that satisfy our equation.
The maximum that $\sqrt{y}$ can be is $\sqrt{10^6} - 1 = 999$ because $\sqrt{y}$ must be an integer (this is because $\sqrt{y} - \sqrt{x} = 2$ , an integer). Then $\sqrt{x} = 997$ , and we continue this downward until $\sqrt{y} = 3$ , in which case $\sqrt{x} = 1$ . The number of pairs of $(\sqrt{x},\sqrt{y})$ , and so $(x,y)$ is then $\boxed{997}$ .

## Solution 2
Let $a^2$ = $x$ and $b^2$ = $y$ , where $a$ and $b$ are positive.
Then \[\frac{a^2 + b^2}{2} = \sqrt{{a^2}{b^2}} +2\] \[a^2 + b^2 = 2ab + 4\] \[(a-b)^2 = 4\] \[(a-b) = \pm 2\]
This makes counting a lot easier since now we just have to find all pairs $(a,b)$ that differ by 2.
Because $\sqrt{10^6} = 10^3$ , then we can use all positive integers less than 1000 for $a$ and $b$ .
We know that because $x < y$ , we get $a < b$ .
We can count even and odd pairs separately to make things easier*:
Odd: \[(1,3) , (3,5) , (5,7) . . . (997,999)\]
Even: \[(2,4) , (4,6) , (6,8) . . . (996,998)\]
This makes $499$ odd pairs and $498$ even pairs, for a total of $\boxed{997}$ pairs.
$*$ Note: We are counting the pairs for the values of $a$ and $b$ , which, when squared, translate to the pairs of $(x,y)$ we are trying to find.

## Solution 3
Since the arithmetic mean is 2 more than the geometric mean, $\frac{x+y}{2} = 2 + \sqrt{xy}$ . We can multiply by 2 to get $x + y = 4 + 2\sqrt{xy}$ . Subtracting 4 and squaring gives \[((x+y)-4)^2 = 4xy\] \[((x^2 + 2xy + y^2) + 16 - 2(4)(x+y)) = 4xy\] \[x^2 - 2xy + y^2 + 16 - 8x - 8y = 0\]
Notice that $((x-y)-4)^2 = x^2 - 2xy + y^2 + 16 - 8x +8y$ , so the problem asks for solutions of \[(x-y-4)^2 = 16y\] Since the left hand side is a perfect square, and 16 is a perfect square, $y$ must also be a perfect square. Since $0 < y < (1000)^2$ , $y$ must be from $1^2$ to $999^2$ , giving at most 999 options for $y$ .
However if $y = 1^2$ , you get $(x-5)^2 = 16$ , which has solutions $x = 9$ and $x = 1$ . Both of those solutions are not less than $y$ , so $y$ cannot be equal to 1. If $y = 2^2 = 4$ , you get $(x - 8)^2 = 64$ , which has 2 solutions, $x = 16$ , and $x = 0$ . 16 is not less than 4, and $x$ cannot be 0, so $y$ cannot be 4. However, for all other $y$ , you get exactly 1 solution for $x$ , and that gives a total of $999 - 2 = \boxed{997}$ pairs.
- asbodke

## Solution 4 (Similar to Solution 3)
Rearranging our conditions to
\[x^2-2xy+y^2+16-8x-8y=0 \implies\] \[(y-x)^2=8(x+y-2).\]
Thus, $4|y-x.$
Now, let $y = 4k+x.$ Plugging this back into our expression, we get
\[(k-1)^2=x.\]
There, a unique value of $x, y$ is formed for every value of $k$ . However, we must have
\[y<10^6 \implies (k+1)^2< 10^6-1\]
and
\[x=(k-1)^2+1>0.\]
Therefore, there are only $\boxed{997}$ pairs of $(x,y).$
Solution by Williamgolly

## Solution 5
First we see that our condition is $\frac{x+y}{2} = 2 + \sqrt{xy}$ . Then we can see that $x+y = 4 + 2\sqrt{xy}$ . From trying a simple example to figure out conditions for $x,y$ , we want to find $x-y$ so we can isolate for $x$ . From doing the example we can note that we can square both sides and subtract $4xy$ : $(x-y)^2 = 16 + 16\sqrt{xy} \implies x-y = -2( \sqrt{1+\sqrt{xy}})$ (note it is negative because $y > x$ . Clearly the square root must be an integer, so now let $\sqrt{xy} = a^2-1$ . Thus $x-y = -2a$ . Thus $x = 2 + \sqrt{xy} - a = 2 + a^2 - 1 -2a$ . We can then find $y$ , and use the quadratic formula on $x,y$ to ensure they are $>0$ and $<10^6$ respectively. Thus we get that $y$ can go up to 999 and $x$ can go down to $3$ , leaving $997$ possibilities for $x,y$ .
These problems are copyrighted © by the Mathematical Association of America.