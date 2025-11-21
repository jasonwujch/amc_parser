# 2003 AIME II Problem 15

## Problem

Let \[P(x) = 24x^{24} + \sum_{j = 1}^{23}(24 - j)(x^{24 - j} + x^{24 + j}).\] Let $z_{1},z_{2},\ldots,z_{r}$ be the distinct zeros of $P(x),$ and let $z_{k}^{2} = a_{k} + b_{k}i$ for $k = 1,2,\ldots,r,$ where $a_{k}$ and $b_{k}$ are real numbers. Let

where $m, n,$ and $p$ are integers and $p$ is not divisible by the square of any prime. Find $m + n + p.$

## Solution
This can be factored as:
\[P(x) = x\left( x^{23} + x^{22} + \cdots + x^2 + x + 1 \right)^2\]
Note that $\left( x^{23} + x^{22} + \cdots + x^2 + x + 1 \right) \cdot (x-1) = x^{24} - 1$ . So the roots of $x^{23} + x^{22} + \cdots + x^2 + x + 1$ are exactly all $24$ -th complex roots of $1$ , except for the root $x=1$ .
Let $\omega=\cos \frac{360^\circ}{24} + i\sin \frac{360^\circ}{24}$ . Then the distinct zeros of $P$ are $0,\omega,\omega^2,\dots,\omega^{23}$ .
We can clearly ignore the root $x=0$ as it does not contribute to the value that we need to compute.
The squares of the other roots are $\omega^2,~\omega^4,~\dots,~\omega^{24}=1,~\omega^{26}=\omega^2,~\dots,~\omega^{46}=\omega^{22}$ .
Hence we need to compute the following sum:
\[R = \sum_{k = 1}^{23} \left|\, \sin \left( k\cdot \frac{360^\circ}{12} \right) \right|\]
Using basic properties of the sine function, we can simplify this to
\[R = 4 \cdot \sum_{k = 1}^{5} \sin \left( k\cdot \frac{360^\circ}{12} \right)\]
The five-element sum is just $\sin 30^\circ + \sin 60^\circ + \sin 90^\circ + \sin 120^\circ + \sin 150^\circ$ . We know that $\sin 30^\circ = \sin 150^\circ = \frac 12$ , $\sin 60^\circ = \sin 120^\circ = \frac{\sqrt 3}2$ , and $\sin 90^\circ = 1$ . Hence our sum evaluates to:
\[R = 4 \cdot \left( 2\cdot \frac 12 + 2\cdot \frac{\sqrt 3}2 + 1 \right) = 8 + 4\sqrt 3\]
Therefore the answer is $8+4+3 = \boxed{015}$ .

## Solution 2
Note that $x^k + x^{k-1} + \dots + x + 1 = \frac{x^{k+1} - 1}{x - 1}$ . Our sum can be reformed as \[\frac{x(x^{47} - 1) + x^2(x^{45} - 1) + \dots + x^{24}(x - 1)}{x-1}\]
So \[\frac{x^{48} + x^{47} + x^{46} + \dots + x^{25} - x^{24} - x^{23} - \dots - x}{x-1} = 0\]
$x(x^{47} + x^{46} + \dots - x - 1) = 0$
$x^{47} + x^{46} + \dots - x - 1 = 0$
$x^{47} + x^{46} + \dots + x + 1 = 2(x^{23} + x^{22} + \dots + x + 1)$
$\frac{x^{48} - 1}{x - 1} = 2\frac{x^{24} - 1}{x - 1}$
$x^{48} - 1 - 2x^{24} + 2 = 0$
$(x^{24} - 1)^2 = 0$
And we can proceed as above.

## Solution 3
As in Solution 1, we find that the roots of $P(x)$ we care about are the 24th roots of unity except $1$ . Therefore, the squares of these roots are the 12th roots of unity. In particular, every 12th root of unity is counted twice, except for $1$ , which is only counted once.
The possible imaginary parts of the 12th roots of unity are $0$ , $\pm\frac{1}{2}$ , $\pm\frac{\sqrt{3}}{2}$ , and $\pm 1$ . We can disregard $0$ because it doesn't affect the sum.
$8$ squares of roots have an imaginary part of $\pm\frac{1}{2}$ , $8$ squares of roots have an imaginary part of $\pm\frac{\sqrt{3}}{2}$ , and $4$ squares of roots have an imaginary part of $\pm 1$ . Therefore, the sum equals $8\left(\frac{1}{2}\right) + 8\left(\frac{\sqrt{3}}{2}\right) + 4(1) = 8 + 4\sqrt{3}$ .
The answer is $8+4+3=\boxed{015}$ .
~rayfish

## Video Solution by Sal Khan
Part 1: https://www.youtube.com/watch?v=2eLAEMRrR7Q&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=3
Part 2: https://www.youtube.com/watch?v=TljVBB7gxbE
Part 3: https://www.youtube.com/watch?v=JTpXK2mENH4
- AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.