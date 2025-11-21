# 2000 AIME II Problem 14

## Problem

Every positive integer $k$ has a unique factorial base expansion $(f_1,f_2,f_3,\ldots,f_m)$ , meaning that $k=1!\cdot f_1+2!\cdot f_2+3!\cdot f_3+\cdots+m!\cdot f_m$ , where each $f_i$ is an integer, $0\le f_i\le i$ , and $0<f_m$ . Given that $(f_1,f_2,f_3,\ldots,f_j)$ is the factorial base expansion of $16!-32!+48!-64!+\cdots+1968!-1984!+2000!$ , find the value of $f_1-f_2+f_3-f_4+\cdots+(-1)^{j+1}f_j$ .

## Solution

## Solution 1
Note that $1+\sum_{k=1}^{n-1} {k\cdot k!} = 1+\sum_{k=1}^{n-1} {((k+1) \cdot k!- k!)} = 1+\sum_{k=1}^{n-1} {((k+1)!- k!)}$
$= 1 + ((2! - 1!) + (3! - 2!) + \cdots + (n! - (n-1)!)) = n!$ .
Thus for all $m\in\mathbb{N}$ ,
$(32m+16)!-(32m)! = \left(1+\sum_{k=1}^{32m+15} {k\cdot k!}\right)-\left(1+\sum_{k=1}^{32m-1} {k\cdot k!}\right) = \sum_{k=32m}^{32m+15}k\cdot k!.$
So now,
\begin{align*} 16!-32!+48!-64!+\cdots+1968!-1984!+2000!&=16!+(48!-32!)+(80!-64!)\cdots+(2000!-1984!)\\ &=16! +\sum_{m=1}^{62}\left((32m+16)!-(32m)!\right)\\ &=16! +\sum_{m=1}^{62}\sum_{k=32m}^{32m+15}k\cdot k! \end{align*}
Therefore we have $f_{16} = 1$ , $f_k=k$ if $32m\le k \le 32m+15$ for some $m=1,2,\ldots,62$ , and $f_k = 0$ for all other $k$ .
Therefore we have:
\begin{align*} f_1-f_2+f_3-f_4+\cdots+(-1)^{j+1}f_j &= (-1)^{17}\cdot 1 + \sum_{m=1}^{62}\sum_{k=32m}^{32m+15}(-1)^{k+1}k\\ &= -1 + \sum_{m=1}^{62}\left[\sum_{j=16m}^{16m+7}(-1)^{2j+1}2j+\sum_{j=16m}^{16m+7}(-1)^{2j+2}(2j+1)\right]\\ &= -1 + \sum_{m=1}^{62}\sum_{j=16m}^{16m+7}[(-1)^{2j+1}2j+(-1)^{2j+2}(2j+1)]\\ &= -1 + \sum_{m=1}^{62}\sum_{j=16m}^{16m+7}[-2j+(2j+1)]\\ &= -1 + \sum_{m=1}^{62}\sum_{j=16m}^{16m+7}1\\ &= -1 + \sum_{m=1}^{62}8\\ &= -1 + 8\cdot 62\\ &= \boxed{495}. \end{align*}

## Solution 2 (informal)
This is equivalent to Solution 1. I put up this solution merely for learners to see the intuition.
Let us consider a base $n$ number system. It’s a well known fact that when we take the difference of two integral powers of $n$ , (such as $10000_{10} - 100_{10}$ ) the result will be an integer in base $n$ composed only of the digits $n - 1$ and $0$ (in this example, $9900$ ). More specifically, the difference $(n^k)_n - (n^j)_n$ , $j<k$ , is an integer $k$ digits long (note that $(n^k)_n$ has $k + 1$ digits). This integer is made up of $(k-j)$ $(n - 1)$ ’s followed by $j$ $0$ ’s.
It should make sense that this fact carries over to the factorial base, albeit with a modification. Whereas in the general base $n$ , the largest digit value is $n - 1$ , in the factorial base, the largest digit value is the argument of the factorial in that place. (for example, $321_!$ is a valid factorial base number, as is $3210_!$ . However, $31_!$ is not, as $3$ is greater than the argument of the second place factorial, $2$ . $31_!$ should be represented as $101_!$ , and is $7_{10}$ .) Therefore, for example, $1000000_! - 10000_!$ is not $990000_!$ , but rather is $650000_!$ . Thus, we may add or subtract factorials quite easily by converting each factorial to its factorial base expression, with a $1$ in the argument of the factorial’s place and $0$ ’s everywhere else, and then using a standard carry/borrow system accounting for the place value.
With general intuition about the factorial base system out of the way, we may tackle the problem. We use the associative property of addition to regroup the terms as follows: $(2000! - 1984!) + (1968! - 1952!) + \cdots + (48! - 32!) + 16!$ we now apply our intuition from paragraph 2. $2000!_{10}$ is equivalent to $1$ followed by $1999$ $0$ ’s in the factorial base, and $1984!$ is $1$ followed by $1983$ $0$ ’s, and so on. Therefore, $2000! - 1984! = (1999)(1998)(1997)\cdots(1984)$ followed by $1983$ $0$ ’s in the factorial base. $1968! - 1952! = (1967)(1966)\cdots(1952)$ followed by $1951$ $0$ ’s, and so on for the rest of the terms, except $16!$ , which will merely have a $1$ in the $16!$ place followed by $0$ ’s. To add these numbers, no carrying will be necessary, because there is only one non-zero value for each place value in the sum. Therefore, the factorial base place value $f_k$ is $k$ for all $32m \leq k \leq 32m+15$ if $1\leq m \in\mathbb{Z} \leq 62$ , $f_{16} = 1$ , and $f_k = 0$ for all other $k$ .
Therefore, to answer, we notice that $1999 - 1998 = 1997 - 1996 = 1$ , and this will continue. Therefore, $f_{1999} - f_{1998} + \cdots - f_{1984} = 8$ . We have 62 sets that sum like this, and each contains $8$ pairs of elements that sum to $1$ , so our answer is almost $8 \cdot 62$ . However, we must subtract the $1$ in the $f_{16}$ place, and our answer is $8 \cdot 62 - 1 = \boxed{495}$ .

## Solution 3 (less formality)
Let $S = 16!-32!+\cdots-1984!+2000!$ . Note that since $|S - 2000!| << 2000!$ (or $|S - 2000!| = 1984! + \cdots$ is significantly smaller than $2000!$ ), it follows that $1999! < S < 2000!$ . Hence $f_{2000} = 0$ . Then $2000! = 2000 \cdot 1999! = 1999 \cdot 1999! + 1999!$ , and as $S - 2000! << 1999!$ , it follows that $1999 \cdot 1999! < S < 2000 \cdot 1999!$ . Hence $f_{1999} = 1999$ , and we now need to find the factorial base expansion of
\[S_2 = S - 1999 \cdot 1999! = 1999! - 1984! + 1962! - 1946! + \cdots + 16!\]
Since $|S_2 - 1999!| << 1999!$ , we can repeat the above argument recursively to yield $f_{1998} = 1998$ , and so forth down to $f_{1985} = 1985$ . Now $S_{16} = 1985! - 1984! + 1962! + \cdots = 1984 \cdot 1984! + 1962! + \cdots$ , so $f_{1984} = 1984$ .
The remaining sum is now just $1962! - 1946! + \cdots + 16!$ . We can repeatedly apply the argument from the previous two paragraphs to find that $f_{16} = 1$ , and $f_k=k$ if $32m\le k \le 32m+15$ for some $m=1,2,\ldots,62$ , and $f_k = 0$ for all other $k$ .
Now for each $m$ , we have $-f_{32m} + f_{32m+1} - f_{32m+2} + \cdots + f_{32m + 31}$ $= -32m + (32m + 1) - (32m + 2) + \cdots - (32m - 30) + (32 m + 31)$ $= 1 + 1 + \cdots + 1 + 1$ $= 8$ . Thus, our answer is $-f_{16} + 8 \cdot 62 = \boxed{495}$ .

## Solution 4 (my brain can't comprehend the other solutions)
First consider how we would express $48!-32!$ . We can't use any multiples of $48!$ , since we'll never be able to make the $-32!$ . Instead, we have to start with using $47!$ s. Having $47\cdot47!$ is the closest we can get to $48!$ , since $48! = 48\cdot 47!$ . Thus, $f_{47}=47$ .
Now consider what we have left to express. We wanted to express $48!-32!$ , and now we have $47\cdot 47!$ . This gives us $47!-32!$ left. Clearly, we can't use anymore $47!$ s, so we have to use $46!$ s. The most $46!$ s we could use is $46$ of them. Thus, $f_{46}=46$ . Since $47!=47\cdot 46!$ , we are left with $46!-32!$ to express. Clearly, each time, we have $f_n = n$ , leaving us with $n!-32!$ to express.
Eventually, we will get down to needing to express $34!-32!$ . We will need $33$ $33!$ s, leaving $33!-32!$ to be expressed. Since $33!=33\cdot 32!$ , $33!-32! = 32\cdot 32!$ . Thus, $48!-32!$ can be expressed as $\sum_{i=32}^{47} i\cdot (i!)$ .
Returning to the problem, notice we can break the expression into groups of $2$ , having $16!+(48!-32!)+(80!-64!)+...(2000!-1984!)$ . Each pair has an alternating sum of $8$ , and since there are $62$ pairs, the sum is $496$ . Including the $16!$ at the start, which accounts for $-1$ , we get $\boxed{495}$ .
-skibbysiggy
These problems are copyrighted © by the Mathematical Association of America.