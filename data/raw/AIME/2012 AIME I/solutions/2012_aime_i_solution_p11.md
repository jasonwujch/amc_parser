# 2012 AIME I Problem 11

## Problem

A frog begins at $P_0 = (0,0)$ and makes a sequence of jumps according to the following rule: from $P_n = (x_n, y_n),$ the frog jumps to $P_{n+1},$ which may be any of the points $(x_n + 7, y_n + 2),$ $(x_n + 2, y_n + 7),$ $(x_n - 5, y_n - 10),$ or $(x_n - 10, y_n - 5).$ There are $M$ points $(x, y)$ with $|x| + |y| \le 100$ that can be reached by a sequence of such jumps. Find the remainder when $M$ is divided by $1000.$

## Solution
First of all, it is easy to see by induction that for any $P(x,y)$ in the frog's jump sequence, $x+y$ will be a multiple of $3$ and $x-y$ will be a multiple of $5.$ The base case $(x,y) = (0,0)$ obviously satisfies the constraints and if $x+y = 3n$ and $x-y = 5m,$ any of the four transformations will sustain this property:
\begin{align*} (x+7)+(y+2) = x+y+9 \rightarrow 3(n+3) &\text{ and } (x+7)-(y+2) = x-y+5 \rightarrow 5(m+1)\\ (x+2)+(y+7) = x+y+9 \rightarrow 3(n+3) &\text{ and } (x+2)-(y+7) = x-y-5 \rightarrow 5(m-1)\\ (x-5)+(y-10) = x+y-15 \rightarrow 3(n-5) &\text{ and } (x-5)-(y-10) = x-y+5 \rightarrow 5(m+1)\\ (x-10)+(y-5) = x+y-15 \rightarrow 3(n-5) &\text{ and } (x-10)-(y-5) = x-y-5 \rightarrow 5(m-1).\\ \end{align*} So we know that any point the frog can reach will satisfy $x+y = 3n$ and $x-y = 5m.$
$\textbf{Lemma:}$ Any point $(x,y)$ such that there exists 2 integers $m$ and $n$ that satisfy $x+y = 3n$ and $x-y = 5m$ is reachable.
$\textbf{Proof:}$ Denote the total amounts of each specific transformation in the frog's jump sequence to be $a,$ $b,$ $c,$ and $d$ respectively. Then
$x=7a+2b-5c-10d$ ,
$y=2a+7b-10c-5d$ ,
$x+y = 9(a+b)-15(c+d) = 3n$ , and
$x-y = 5(a-b)+5(c-d) = 5m$
together must have integral solutions. But
$3(a+b)-5(c+d) = n$ implies
$(c+d) \equiv n \mod 3$ and thus
$(a+b) = \lfloor{n/3}\rfloor + 2(c+d).$
Similarly, $(a-b)+(c-d) = m$ implies that $(a-b)$ and $(c-d)$ have the same parity. Now in order for an integral solution to exist, there must always be a way to ensure that the pairs $(a+b)$ and $(a-b)$ and $(c+d)$ and $(c-d)$ have identical parities. The parity of $(a+b)$ is completely dependent on $n,$ so the parities of $(a-b)$ and $(c-d)$ must be chosen to match this value. But the parity of $(c+d)$ can then be adjusted by adding or subtracting $3$ until it is identical to the parity of $(c-d)$ as chosen before, so we conclude that it is always possible to find an integer solution for $(a,b,c,d)$ and thus any point that satisfies $x+y = 3n$ and $x-y = 5m$ can be reached by the frog.
To count the number of such points in the region $|x| + |y| \le 100,$ we first note that any such point will lie on the intersection of one line of the form $y=x-5m$ and another line of the form $y=-x+3n.$ The intersection of two such lines will yield the point $\left(\frac{3n+5m}{2},\frac{3n-5m}{2}\right),$ which will be integral if and only if $m$ and $n$ have the same parity. Now since $|x| + |y| = |x \pm y|,$ we find that
\begin{align*} |x + y| = |3n| \le 100 &\rightarrow -33 \le n \le 33\\ |x - y| = |5m| \le 100 &\rightarrow -20 \le m \le 20. \end{align*}
So there are $34$ possible odd values and $33$ possible even values for $n,$ and $20$ possible odd values and $21$ possible even values for $m.$ Every pair of lines described above will yield a valid accessible point for all pairs of $m$ and $n$ with the same parity, and the number of points $M$ is thus $34 \cdot 20 + 33 \cdot 21 = 1373 \rightarrow \boxed{373}$ .

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/351
~ dolphin7
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .