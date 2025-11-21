# 2013 AIME I Problem 15

## Problem

Let $N$ be the number of ordered triples $(A,B,C)$ of integers satisfying the conditions (a) $0\le A<B<C\le99$ , (b) there exist integers $a$ , $b$ , and $c$ , and prime $p$ where $0\le b<a<c<p$ , (c) $p$ divides $A-a$ , $B-b$ , and $C-c$ , and (d) each ordered triple $(A,B,C)$ and each ordered triple $(b,a,c)$ form arithmetic sequences. Find $N$ .

## Solution
From condition (d), we have $(A,B,C)=(B-D,B,B+D)$ and $(b,a,c)=(a-d,a,a+d)$ . Condition $\text{(c)}$ states that $p\mid B-D-a$ , $p | B-a+d$ , and $p\mid B+D-a-d$ . We subtract the first two to get $p\mid-d-D$ , and we do the same for the last two to get $p\mid 2d-D$ . We subtract these two to get $p\mid 3d$ . So $p\mid 3$ or $p\mid d$ . The second case is clearly impossible, because that would make $c=a+d>p$ , violating condition $\text{(b)}$ . So we have $p\mid 3$ , meaning $p=3$ . Condition $\text{(b)}$ implies that $(b,a,c)=(0,1,2)$ or $(a,b,c)\in (1,0,2)\rightarrow (-2,0,2)\text{ }(D\equiv 2\text{ mod 3})$ . Now we return to condition $\text{(c)}$ , which now implies that $(A,B,C)\equiv(-2,0,2)\pmod{3}$ . Now, we set $B=3k$ for increasing positive integer values of $k$ . $B=0$ yields no solutions. $B=3$ gives $(A,B,C)=(1,3,5)$ , giving us $1$ solution. If $B=6$ , we get $2$ solutions, $(4,6,8)$ and $(1,6,11)$ . Proceeding in the manner, we see that if $B=48$ , we get 16 solutions. However, $B=51$ still gives $16$ solutions because $C_\text{max}=2B-1=101>100$ . Likewise, $B=54$ gives $15$ solutions. This continues until $B=96$ gives one solution. $B=99$ gives no solution. Thus, $N=1+2+\cdots+16+16+15+\cdots+1=2\cdot\frac{16(17)}{2}=16\cdot 17=\boxed{272}$ .

## Solution 2
Let $(A, B, C)$ = $(B-x, B, B+x)$ and $(b, a, c) = (a-y, a, a+y)$ . Now the 3 differences would be \begin{align} \label{1} &A-a = B-x-a \\ \label{2} &B - b = B-a+y \\ \label{3} &C - c = B+x-a-y \end{align}
Adding equations $(1)$ and $(3)$ would give $2B - 2a - y$ . Then doubling equation $(2)$ would give $2B - 2a + 2y$ . The difference between them would be $3y$ . Since $p|\{(1), (2), (3)\}$ , then $p|3y$ . Since $p$ is prime, $p|3$ or $p|y$ . However, since $p > y$ , we must have $p|3$ , which means $p=3$ .
If $p=3$ , the only possible values of $(b, a, c)$ are $(0, 1, 2)$ . Plugging this into our differences, we get \begin{align*} &A-a = B-x-1 \hspace{4cm}(4)\\ &B - b = B \hspace{5.35cm}(5)\\ &C - c = B+x-2 \hspace{4cm}(6) \end{align*} The difference between $(4)$ and $(5)$ is $x+1$ , which should be divisible by 3. So $x \equiv 2 \mod 3$ . Also note that since $3|(5)$ , $3|B$ . Now we can try different values of $x$ and $B$ :
When $x=2$ , $B=3, 6, ..., 96 \Rightarrow 32$ triples.
When $x=5$ , $B=6, 9, ..., 93\Rightarrow 30$ triples..
... and so on until
When $x=47$ , $B=48, 51\Rightarrow 2$ triple.
So the answer is $32 + 30 + \cdots + 2 = \boxed{272}$
~SoilMilk
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .