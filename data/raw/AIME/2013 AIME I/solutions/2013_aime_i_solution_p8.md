# 2013 AIME I Problem 8

## Problem

The domain of the function $f(x) = \arcsin(\log_{m}(nx))$ is a closed interval of length $\frac{1}{2013}$ , where $m$ and $n$ are positive integers and $m>1$ . Find the remainder when the smallest possible sum $m+n$ is divided by 1000.

## Solution 1
We know that the domain of $\text{arcsin}$ is $[-1, 1]$ , so $-1 \le \log_m nx \le 1$ . Now we can apply the definition of logarithms: \[m^{-1} = \frac1m \le nx \le m\] \[\implies \frac{1}{mn} \le x \le \frac{m}{n}\] Since the domain of $f(x)$ has length $\frac{1}{2013}$ , we have that \[\frac{m}{n} - \frac{1}{mn} = \frac{1}{2013}\] \[\implies \frac{m^2 - 1}{mn} = \frac{1}{2013}\]
A larger value of $m$ will also result in a larger value of $n$ since $\frac{m^2 - 1}{mn} \approx \frac{m^2}{mn}=\frac{m}{n}$ meaning $m$ and $n$ increase about linearly for large $m$ and $n$ . So we want to find the smallest value of $m$ that also results in an integer value of $n$ . The problem states that $m > 1$ . Thus, first we try $m = 2$ : \[\frac{3}{2n} = \frac{1}{2013} \implies 2n = 3 \cdot 2013 \implies n \notin \mathbb{Z}\] Now, we try $m=3$ : \[\frac{8}{3n} = \frac{1}{2013} \implies 3n = 8 \cdot 2013 \implies n = 8 \cdot 671 = 5368\] Since $m=3$ is the smallest value of $m$ that results in an integral $n$ value, we have minimized $m+n$ , which is $5368 + 3 = 5371 \equiv \boxed{371} \pmod{1000}$ .

## Solution 2
We start with the same method as above. The domain of the arcsin function is $[-1, 1]$ , so $-1 \le \log_{m}(nx) \le 1$ .
\[\frac{1}{m} \le nx \le m\] \[\frac{1}{mn} \le x \le \frac{m}{n}\] \[\frac{m}{n} - \frac{1}{mn} = \frac{1}{2013}\] \[n = 2013m - \frac{2013}{m}\]
For $n$ to be an integer, $m$ must divide $2013$ , and $m > 1$ . To minimize $n$ , $m$ should be as small as possible because increasing $m$ will decrease $\frac{2013}{m}$ , the amount you are subtracting, and increase $2013m$ , the amount you are adding; this also leads to a small $n$ which clearly minimizes $m+n$ .
We let $m$ equal $3$ , the smallest factor of $2013$ that isn't $1$ . Then we have $n = 2013*3 - \frac{2013}{3} = 6039 - 671 = 5368$
$m + n = 5371$ , so the answer is $\boxed{371}$ .

## Solution 3 (Operation Quadratics)
Note that we need $-1\le f(x)\le 1$ , and this eventually gets to $\frac{m^2-1}{mn}=\frac{1}{2013}$ . From there, break out the quadratic formula and note that \[m= \frac{n+\sqrt{n^2+4026^2}}{2013\times 2}.\] Then we realize that the square root, call it $a$ , must be an integer. Then $(a-n)(a+n)=4026^2.$
Observe carefully that $4026^2 = 2\times 2\times 3\times 3\times 11\times 11\times 61\times 61$ ! It is not difficult to see that to minimize the sum, we want to minimize $n$ as much as possible. Seeing that $2a$ is even, we note that a $2$ belongs in each factor. Now, since we want to minimize $a$ to minimize $n$ , we want to distribute the factors so that their ratio is as small as possible (sum is thus minimum). The smallest allocation of $2, 61, 61$ and $2, 11, 3, 3, 11$ fails; the next best is $2, 61, 11, 3, 3$ and $2, 61, 11$ , in which $a=6710$ and $n=5368$ . That is our best solution, upon which we see that $m=3$ , thus $\boxed{371}$ .

## Solution 4 (Factor! and slightly cheese)
By considering the range of $\arcsin$ , we obtain $-1 \leq\log_{m} (nx) \leq 1 \Rightarrow \frac{1}{mn} \leq x \leq \frac{m}{n}$ . Hence we consider the difference: $\frac{m}{n} - \frac{1}{mn} = \frac{m^2 - 1}{mn} = \frac{1}{2013}$ . Now just cross multiply to obtain $2013(m-1)(m+1) = mn$ , and that $2013 = 3 \cdot 11 \cdot 61$ . We could try a few cases: $m = 3$ , for instance, yields $n = 671 \cdot 8 = 5368$ . Adding $3$ gives $5371$ . Now, if we consider greater $m$ , we see that the term $(m-1)(m+1)$ grows very fast: this is also due to the fact that $61,11 \gg 3$ . Hence, we may just conclude that the answer is $5371 \Rightarrow \boxed{371}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .