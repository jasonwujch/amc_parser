# 2020 AIME II Problem 14

## Problem

For a real number $x$ let $\lfloor x\rfloor$ be the greatest integer less than or equal to $x$ , and define $\{x\} = x - \lfloor x \rfloor$ to be the fractional part of $x$ . For example, $\{3\} = 0$ and $\{4.56\} = 0.56$ . Define $f(x)=x\{x\}$ , and let $N$ be the number of real-valued solutions to the equation $f(f(f(x)))=17$ for $0\leq x\leq 2020$ . Find the remainder when $N$ is divided by $1000$ .

## Solution 1
Note that the upper bound for our sum is $2019,$ and not $2020,$ because if it were $2020$ then the function composition cannot equal to $17.$ From there, it's not too hard to see that, by observing the function composition from right to left, $N$ is (note that the summation starts from the right to the left): \[\sum_{x=17}^{2019} \sum_{y=x}^{2019} \sum_{z=y}^{2019} 1 .\] One can see an easy combinatorical argument exists which is the official solution, but I will present another solution here for the sake of variety.
Applying algebraic manipulation and the hockey-stick identity $3$ times gives
\[\sum_{x=17}^{2019} \sum_{y=x}^{2019} \sum_{z=y}^{2019} 1\]
\[=\sum_{x=17}^{2019} \sum_{y=x}^{2019} \sum_{z=y}^{2019} \binom{z-y}{0}\]
\[=\sum_{x=17}^{2019} \sum_{y=x}^{2019} \binom{2020-y}{1}\]
\[=\sum_{x=17}^{2019} \binom{2021-x}{2}\]
\[=\binom{2005}{3}\]
Hence, \[N = \frac{2005 \cdot 2004 \cdot 2003}{3 \cdot 2\cdot 1} \equiv \boxed{010} (\mathrm{mod} \hskip .2cm 1000)\]

## Solution 2
To solve $f(f(f(x)))=17$ , we need to solve $f(x) = y$ where $f(f(y))=17$ , and to solve that we need to solve $f(y) = z$ where $f(z) = 17$ .
It is clear to see for some integer $a \geq 17$ there is exactly one value of $z$ in the interval $[a, a+1)$ where $f(z) = 17$ . To understand this, imagine the graph of $f(z)$ on the interval $[a, a+1)$ The graph starts at $0$ , is continuous and increasing, and approaches $a+1$ . So as long as $a+1 > 17$ , there will be a solution for $z$ in the interval.
Using this logic, we can find the number of solutions to $f(x) = y$ . For every interval $[a, a+1)$ where $a \geq \left \lfloor{y}\right \rfloor$ there will be one solution for $x$ in that interval. However, the question states $0 \leq x \leq 2020$ , but because $x=2020$ doesn't work we can change it to $0 \leq x < 2020$ . Therefore, $\left \lfloor{y}\right \rfloor \leq a \leq 2019$ , and there are $2020 - \left \lfloor{y}\right \rfloor$ solutions to $f(x) = y$ .
We can solve $f(y) = z$ similarly. $0 \leq y < 2020$ to satisfy the bounds of $x$ , so there are $2020 - \left \lfloor{z}\right \rfloor$ solutions to $f(y) = z$ , and $0 \leq z < 2020$ to satisfy the bounds of $y$ .
Going back to $f(z) = 17$ , there is a single solution for z in the interval $[a, a+1)$ , where $17 \leq a \leq 2019$ . (We now have an upper bound for $a$ because we know $z < 2020$ .) There are $2003$ solutions for $z$ , and the floors of these solutions create the sequence $17, 18, 19, ..., 2018, 2019$
Lets first look at the solution of $z$ where $\left \lfloor{z}\right \rfloor = 17$ . Then $f(y) = z$ would have $2003$ solutions, and the floors of these solutions would also create the sequence $17, 18, 19, ..., 2018, 2019$ .
If we used the solution of $y$ where $\left \lfloor{y}\right \rfloor = 17$ , there would be $2003$ solutions for $f(x) = y$ . If we used the solution of $y$ where $\left \lfloor{y}\right \rfloor = 18$ , there would be $2002$ solutions for $x$ , and so on. So for the solution of $z$ where $\left \lfloor{z}\right \rfloor = 17$ , there will be $2003 + 2002 + 2001 + ... + 2 + 1 = \binom{2004}{2}$ solutions for $x$
If we now look at the solution of $z$ where $\left \lfloor{z}\right \rfloor = 18$ , there would be $\binom{2003}{2}$ solutions for $x$ . If we looked at the solution of $z$ where $\left \lfloor{z}\right \rfloor = 19$ , there would be $\binom{2002}{2}$ solutions for $x$ , and so on.
The total number of solutions to $x$ is $\binom{2004}{2} + \binom{2003}{2} + \binom{2002}{2} + ... + \binom{3}{2} + \binom{2}{2}$ . Using the hockey stick theorem, we see this equals $\binom{2005}{3}$ , and when we take the remainder of that number when divided by $1000$ , we get the answer, $\boxed{10}$
~aragornmf

## Solution 3 (Official MAA)
For any nonnegative integer $n$ , the function $f$ increases on the interval $[n,n+1)$ , with $f(n)=0$ and $f(x)<n+1$ for every $x$ in this interval. On this interval $f(x)=x(x-n)$ , which takes on every real value in the interval $[0,n+1)$ exactly once. Thus for each nonnegative real number $y$ , the equation $f(x) = y$ has exactly one solution $x \in [n, n+1)$ for every $n \ge \lfloor y \rfloor$ .
For each integer $a\geq 17$ there is exactly one $x$ with $\lfloor x\rfloor=a$ such that $f(x)=17$ ; likewise for each integer $b\geq a\geq 17$ there is exactly one $x$ with $\lfloor f(x)\rfloor=a$ and $\lfloor x\rfloor=b$ such that $f(f(x))=17$ . Finally, for each integer $c \ge b \ge a \ge 17$ there is exactly one $x$ with $\lfloor f(f(x)) \rfloor = a$ , $\lfloor f(x)\rfloor=b$ , and $\lfloor x\rfloor=c$ such that $f(f(f(x)))=17$ .
Thus $f(f(f(x)))=17$ has exactly one solution $x$ with $0\leq x\leq 2020$ for each triple of integers $(a,b,c)$ with $17\leq a\leq b\leq c<2020$ , noting that $x=2020$ is not a solution. This nondecreasing ordered triple can be identified with a multiset of three elements of the set of $2003$ integers $\{17,18,19,\ldots,2019\}$ , which can be selected in $\binom{2005}3$ ways. Thus \[N=\frac{2005\cdot 2004\cdot 2003}{6}\equiv 10\hskip -.2cm \pmod{1000}.\]

## Video Solution 1
https://youtu.be/bz5N-jI2e0U?t=515

## Video Solution 2
https://youtu.be/YWKlWuwDwmI
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .