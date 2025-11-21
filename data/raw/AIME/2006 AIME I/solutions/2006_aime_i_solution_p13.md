# 2006 AIME I Problem 13

## Problem

For each even positive integer $x$ , let $g(x)$ denote the greatest power of 2 that divides $x.$ For example, $g(20)=4$ and $g(16)=16.$ For each positive integer $n,$ let $S_n=\sum_{k=1}^{2^{n-1}}g(2k).$ Find the greatest integer $n$ less than 1000 such that $S_n$ is a perfect square .

## Solution 1
Given $g : x \mapsto \max_{j : 2^j | x} 2^j$ , consider $S_n = g(2) + \cdots + g(2^n)$ . Define $S = \{2, 4, \ldots, 2^n\}$ . There are $2^0$ elements of $S$ that are divisible by $2^n$ , $2^1 - 2^0 = 2^0$ elements of $S$ that are divisible by $2^{n-1}$ but not by $2^n, \ldots,$ and $2^{n-1}-2^{n-2} = 2^{n-2}$ elements of $S$ that are divisible by $2^1$ but not by $2^2$ .
Thus \begin{align*} S_n &= 2^0\cdot2^n + 2^0\cdot2^{n-1} + 2^1\cdot2^{n-2} + \cdots + 2^{n-2}\cdot2^1\\ &= 2^n + (n-1)2^{n-1}\\ &= 2^{n-1}(n+1).\end{align*} Let $2^k$ be the highest power of $2$ that divides $n+1$ . Thus by the above formula, the highest power of $2$ that divides $S_n$ is $2^{k+n-1}$ . For $S_n$ to be a perfect square, $k+n-1$ must be even. If $k$ is odd, then $n+1$ is even, hence $k+n-1$ is odd, and $S_n$ cannot be a perfect square. Hence $k$ must be even. In particular, as $n<1000$ , we have five choices for $k$ , namely $k=0,2,4,6,8$ .
If $k=0$ , then $n+1$ is odd, so $k+n-1$ is odd, hence the largest power of $2$ dividing $S_n$ has an odd exponent, so $S_n$ is not a perfect square.
In the other cases, note that $k+n-1$ is even, so the highest power of $2$ dividing $S_n$ will be a perfect square. In particular, $S_n$ will be a perfect square if and only if $(n+1)/2^{k}$ is an odd perfect square.
If $k=2$ , then $n<1000$ implies that $\frac{n+1}{4} \le 250$ , so we have $n+1 = 4, 4 \cdot 3^2, \ldots, 4 \cdot 13^2, 4\cdot 3^2 \cdot 5^2$ .
If $k=4$ , then $n<1000$ implies that $\frac{n+1}{16} \le 62$ , so $n+1 = 16, 16 \cdot 3^2, 16 \cdot 5^2, 16 \cdot 7^2$ .
If $k=6$ , then $n<1000$ implies that $\frac{n+1}{64}\le 15$ , so $n+1=64,64\cdot 3^2$ .
If $k=8$ , then $n<1000$ implies that $\frac{n+1}{256}\le 3$ , so $n+1=256$ .
Comparing the largest term in each case, we find that the maximum possible $n$ such that $S_n$ is a perfect square is $4\cdot 3^2 \cdot 5^2 - 1 = \boxed{899}$ .

## Solution 2
First note that $g(k)=1$ if $k$ is odd and $2g(k/2)$ if $k$ is even. so $S_n=\sum_{k=1}^{2^{n-1}}g(2k). = \sum_{k=1}^{2^{n-1}}2g(k) = 2\sum_{k=1}^{2^{n-1}}g(k) = 2\sum_{k=1}^{2^{n-2}} g(2k-1)+g(2k).$ $2k-1$ must be odd so this reduces to $2\sum_{k=1}^{2^{n-2}}1+g(2k) = 2(2^{n-2}+\sum_{k=1}^{2^{n-2}}g(2k)).$ Thus $S_n=2(2^{n-2}+S_{n-1})=2^{n-1}+2S_{n-1}.$ Further noting that $S_0=1$ we can see that $S_n=2^{n-1}\cdot (n-1)+2^n\cdot S_0=2^{n-1}\cdot (n-1)+2^{n-1}\cdot2=2^{n-1}\cdot (n+1).$ which is the same as above. To simplify the process of finding the largest square $S_n$ we can note that if $n-1$ is odd then $n+1$ must be exactly divisible by an odd power of $2$ . However, this means $n+1$ is even but it cannot be. Thus $n-1$ is even and $n+1$ is a large even square. The largest even square $< 1000$ is $900$ so $n+1= 900 => n= \boxed{899}$

## Solution 3 (Finding patterns and using recursion)
At first, this problem looks kind of daunting, but we can easily solve this problem by finding patterns, recursion and algebraic manipulations.
We first simplify all the messy notation in the $S_n$ term. Note that the problem asks us to find the smallest value of $n<1000$ such that there exists an integer $k$ that satisfies
\[k^2 = g(2) + g(4) + \cdots + g(2^n)\] .
Since there is no obvious way to approach this problem, we start by experimenting with small values of $n$ to evaluate some $S_n$ .
We play with these values:
\[S_1 = g(2) = 2\]
\[S_2 = g(2) + g(4) = 2+4 = 6\]
\[S_3 = g(2) + g(4) + g(6) + g(8) = 16\]
\[S_4 = g(2) + g(4) + g(6) + g(8) + g(10) +g(12)+g(14)+g(16) = 40\]
We are certainly not going to expand all of this out... so let's look for patterns from these $4$ values!
Using a little bit of ingenuity, we note that
\[S_2 = 2+4 = S_1 + 4\]
\[S_3 = 2+4+2+8 = 8+8 = S_2 + S_1 + 8\]
\[S_4 = 2+4+2+8+2+4+2+16 = S_3 + S_2 + S_1 + 16\]
Aha! We see powers of two in each of our terms! Therefore, we can say that
\[S_2 = S_1 + 2^2\]
\[S_3 = S_2+S_1 + 2^3\]
\[S_4 = S_3 + S_2 + S_1 + 2^4\]
Hooray! We have a recursion! Realistically, we would want to prove that the recursion works, but I currently don't know how to prove it.
On the actual AIME, go with whatever patterns you see, because most likely those are the patterns that the test-makers want the students to see.
So we may generalize a formula for $S_n$ :
\[S_n = 2^n + S_{n-1} + S_{n-2} + \cdots + S_2 + S_1\]
Uh oh... this formula is not in closed form. Looks like we'll have to use our recursion to develop one manually. We do so by using our recursion for $S_{n-1}$ :
\[S_n = 2^n + (2^{n-1} + S_{n-2} + S_{n-3} + \cdots + S_2 + S_1) + S_{n-2} + S_{n-3} + \cdots + S_2 + S_1\]
\[S_n = 2^n + 2^{n-1} + 2 (S_{n-2} + S_{n-3} + \cdots + S_2 + S_1\]
Let's simplify a bit further, where we use our recursion for $S_{n-2}$ .
\[S_n = 2^n + 2^{n-1} +(2S_{n-2}) + 2(S_{n-3} + S_{n-4} + \cdots + S_2 + S_1)\]
\[S_n = 2^n + 2^{n-1} + 2(2^{n-2}) + 2(S_{n-3} + S_{n-4} + \cdots + S_2 + S_1) + 2(S_{n-3} + S_{n-4} + \cdots + S_2 + S_1)\]
\[S_n = 2^n + 2^{n-1} + 2^{n-1} + 4(S_{n-3} + S_{n-4} + \cdots + S_2 + S_1)\]
We now see a pattern! Using the exact same logic, we can condense this whole messy thing into a closed form:
\[S_n = 2^n + \underbrace{2^{n-1}}_{n-2} + 2^{n-2}(S_1)\]
\[S_n = 2^n + 2^{n-1}(n-2) + 2^{n-1}\]
\[S_n = 2^n + 2^{n-1}(n-1)\]
\[S_n = 2^{n-1}(2 + (n-1)\]
\[S_n = 2^{n-1}(n+1)\]
We have our closed form, so now we can find the largest value of $n$ such that $S_n$ is a perfect square.
In order for $S_n$ to be a perfect square, we must have $n-1$ even and $n+1$ be a perfect square.
Since $n<1000$ , we have $n+1 < 1001$ . We first try $n+1 = 31^2 = 961$ (since it is the smallest square below $1000$ , which gives us $n=960$ . But $n-1$ isn't even, so we discard this value.
Next, we try the second smallest value, which is $n = 30^2 = 900$ , which tells us that $n=899$ . $n-1$ is indeed even, and $n+1$ is a perfect square, so the largest value of $n$ such that $S_n$ is a perfect square is $899$ .
Our answer is $\boxed{899}$ .
-FIREDRAGONMATH16
First, we set intervals. Say that a number $N$ falls strictly within $[2^k, 2^{k+1}]$ .
$N<2^{k+1}=2^k+2^k$
We can generalize this:
If a number is in the form $N=2^k+2^{R}O$ where $O$ is a positive odd number, $R<k$ :
$N<2^{k+1}=2^k+2^k\Longrightarrow O<2^{k-R}$ so there are $2^{k-R-1}$ numbers that satisfy this form. For all numbers that satisfy this form, $g(N)=2^R$ . The sum of $g(N)$ for all $N$ in this form and interval is $2^{k-1}$ . $R$ can vary between $1$ and $k-1$ , so the total sum is $\underbrace{2^{k-1}+2^{k-1}\cdots 2^{k-1}}_{k-1}=(k-1)2^{k-1}$ . The domain of the function we are trying to find is all even integers in the interval $[2^1, 2^n]$ so there are $n-1$ values of $k$ . Now we have the sum $\sum_{k=1}^{n-1}{(k-1)2^{k-1}}=\sum_{i=1}^{n-2}{k\cdot2^{k}}$ . However, we did not consider powers of two yet(since our interval was strictly between powers of 2), so we have to add $\sum_{k=1}^{n}{2^k}$ . Note that $\sum_{i=1}^{n-2}{k\cdot2^{k}}=(2^1+2^2\cdots 2^{n-2})+(2^2+2^3\cdots 2^{n-2})\cdots +(2^{n-3}+2^{n-2})+2^{n-2}=2^1(2^{n-2}-1)+2^2(2^{n-3}-1)\cdots +2^{n-3}(2^2-1)+2^{n-2}(2^1-1)=(n-2)(2^{n-1})-\sum_{k=1}^{n-2}{2^k}=(n-2)(2^{n-1})-2(2^{n-2}-1)=(n-3)(2^{n-1})+2$ . Adding $\sum_{k=1}^{n}{2^k}=2(2^n-1)$ , we get $(n+1)(2^{n-1})$ . If this sum is a perfect square, $n\not\equiv0\pmod2$ , since that would make $2^{n-1}$ not a perfect square, and $n+1$ odd so it cannot contribute a factor of 2 to make the power of 2 a perfect square.
We want the least odd number less than $1000$ such that $(n+1)$ is an even perfect square. The greatest even square less than $1000$ is $30^2=900$ so $n+1=900 \Longrightarrow n=\boxed{899}$
These problems are copyrighted © by the Mathematical Association of America.