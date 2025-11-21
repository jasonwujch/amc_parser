# 2010 AIME II Problem 10

## Problem

Find the number of second-degree polynomials $f(x)$ with integer coefficients and integer zeros for which $f(0)=2010$ .

## Solution

## Solution 1
Let $f(x) = a(x-r)(x-s)$ . Then $ars=2010=2\cdot3\cdot5\cdot67$ . First consider the case where $r$ and $s$ (and thus $a$ ) are positive. There are $3^4 = 81$ ways to split up the prime factors between $a$ , $r$ , and $s$ . However, $r$ and $s$ are indistinguishable. In one case, $(a,r,s) = (2010,1,1)$ , we have $r=s$ . The other $80$ cases are double counting, so there are $40$ .
We must now consider the various cases of signs. For the $40$ cases where $|r|\neq |s|$ , there are a total of four possibilities, For the case $|r|=|s|=1$ , there are only three possibilities, $(r,s) = (1,1); (1,-1); (-1,-1)$ as $(-1,1)$ is not distinguishable from the second of those three.
You may ask: How can one of ${r, s}$ be positive and the other negative? $a$ will be negative as a result. That way, it's still $+2010$ that gets multiplied.
Thus the grand total is $4\cdot40 + 3 = \boxed{163}$ .
Note: The only reason why we can be confident that $r = s$ is the only case where the polynomials are being overcounted is because of this: We have the four configurations listed below:
$(a,r,s)\\ (a,-r,-s)\\ (-a,-r,s)\\ (-a,r,-s)$
And notice, we start by counting all the positive solutions. So $r$ and $s$ must be strictly positive, no $0$ or negatives allowed. The negative transformations will count those numbers.
So with these we can conclude that only the first and second together have a chance of being equal, and the third and fourth together. If we consider the first and second, the $x$ term would have coefficients that are always different, $-a(r + s)$ and $a(r + s)$ because of the negative $r$ and $s$ . Since the $a$ is never equal, these can never create equal $x$ coefficients. We don't need to worry about this as $r$ and $s$ are positive and so that won't have any chance.
However with the $(-a,-r,s)$ and $(-a,r,-s)$ , we have the coefficients of the $x$ term as $a(s-r)$ and $a(r-s)$ . In other words, they are equal if $s-r=r-s$ or $r=s$ . Well if $r = 1$ , then we have $s = 1$ and in the $(r,-s)$ case we have $(1,-1)$ and if we transform using $(s,-r)$ , then we have $(-1, 1)$ . So this is the only way that we could possibly overcount the equal cases, and so we need to make sure we don't count $(-1,1)$ and $(1,-1)$ twice as they will create equal sums. This is why we subtract $1$ from $41*4=164$ .
Each different transformation will give us different coordinates $(a,r,s)...$ it is just that some of them create equal coefficients for the $x$ -term, and we see that they are equal only in this case by our exploration, so we subtract $1$ to account and get $163$ .

## Solution 2
We use Burnside's Lemma . The set being acted upon is the set of integer triples $(a,r,s)$ such that $ars=2010$ . Because $r$ and $s$ are indistinguishable, the permutation group consists of the identity and the permutation that switches $r$ and $s$ . In cycle notation, the group consists of $(a)(r)(s)$ and $(a)(r \: s)$ . There are $4 \cdot 3^4$ fixed points of the first permutation (after distributing the primes among $a$ , $r$ , $s$ and then considering their signs. We have 4 ways since we can keep them all positive, first 2 negative, first and third negative, or last two negative) and $2$ fixed points of the second permutation ( $r=s=\pm 1$ ). By Burnside's Lemma, there are $\frac{1}{2} (4 \cdot 3^4+2)= \boxed{163}$ distinguishable triples $(a,r,s)$ . Note: The permutation group is isomorphic to $\mathbb{Z}/2\mathbb{Z}$ .

## Solution 3
The equation can be written in the form of $k(x-a)(x-b)$ , where $|k|$ is a divisor of $2010$ . Factor $2010=2\cdot 3\cdot 5\cdot 67$ . We divide into few cases to study.
Firstly, if $|k|=1$ , the equation can be $-(x-a)(x+b)$ or $(x-a)(x-b)$ or $(x+a)(x+b)$ , there are $2^4+2^4=32$ ways
If $|k|\in \{2,3,5,67\}$ . Take $|k|=2$ as an example, follow the procedure above, there are $2^3+2^3=16$ ways, and there are $\binom {4}{1}=4$ ways to choose $|k|$ , so there are $16\cdot 4=64$ ways
If $|k|$ is the product of two factors of $2010$ , there are $8$ ways for each. Thus there are $\binom {4}{2}\cdot 8=48$ ways
If $|k|$ is the product of three factors of $2010$ , there are $\binom {4}{3}\cdot 4=16$ ways
In the end, $|k|=2010$ , only $2010(x-1)(x-1); 2010(x+1)(x+1); -2010(x-1)(x+1)$ work, there are $3$ ways
Thus, $32+64+48+16+3=\boxed{163}$
~bluesoul
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .