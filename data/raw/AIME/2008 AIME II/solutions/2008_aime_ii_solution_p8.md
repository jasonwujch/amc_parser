# 2008 AIME II Problem 8

## Problem

Let $a = \pi/2008$ . Find the smallest positive integer $n$ such that \[2[\cos(a)\sin(a) + \cos(4a)\sin(2a) + \cos(9a)\sin(3a) + \cdots + \cos(n^2a)\sin(na)]\] is an integer.

## Solution

## Solution 1
By the product-to-sum identities , we have that $2\cos a \sin b = \sin (a+b) - \sin (a-b)$ . Therefore, this reduces to a telescope series: \begin{align*} \sum_{k=1}^{n} 2\cos(k^2a)\sin(ka) &= \sum_{k=1}^{n} [\sin(k(k+1)a) - \sin((k-1)ka)]\\ &= -\sin(0) + \sin(2a)- \sin(2a) + \sin(6a) - \cdots - \sin((n-1)na) + \sin(n(n+1)a)\\ &= -\sin(0) + \sin(n(n+1)a) = \sin(n(n+1)a) \end{align*}
Thus, we need $\sin \left(\frac{n(n+1)\pi}{2008}\right)$ to be an integer; this can be only $\{-1,0,1\}$ , which occur when $2 \cdot \frac{n(n+1)}{2008}$ is an integer. Thus $1004 = 2^2 \cdot 251 | n(n+1) \Longrightarrow 251 | n, n+1$ . We know that $n$ cannot be $250$ as $250$ isn't divisible by $4$ , so 1004 doesn't divide $n(n+1) = 250 \cdot 251$ . Therefore, it is clear that $n = \boxed{251}$ is the smallest such integer.

## Solution 2
We proceed with complex trigonometry. We know that for all $\theta$ , we have $\cos \theta = \dfrac{1}{2} \left( z + \dfrac{1}{z} \right)$ and $\sin \theta = \dfrac{1}{2i} \left( z - \dfrac{1}{z} \right)$ for some complex number $z$ on the unit circle. Similarly, we have $\cos n \theta = \dfrac{1}{2} \left( z^n + \dfrac{1}{z^n} \right)$ and $\sin n \theta = \dfrac{1}{2i} \left(z^n - \dfrac{1}{z^n} \right)$ . Thus, we have $\cos n^2 a \sin n a = \dfrac{1}{4i} \left( z^{n^2} + \dfrac{1}{z^{n^2}} \right) \left( z^{n} - \dfrac{1}{z^n} \right)$
$= \dfrac{1}{4i} \left( z^{n^2 + n} - \dfrac{1}{z^{n^2 + n}} - z^{n^2 - n} + \dfrac{1}{z^{n^2 - n}} \right)$
$= \dfrac{1}{2} \left( \dfrac{1}{2i} \left(z^{n^2 + n} - \dfrac{1}{z^{n^2 + n}} \right) - \dfrac{1}{2i} \left(z^{n^2 - n} - \dfrac{1}{z^{n^2 - n}} \right) \right)$
$= \dfrac{1}{2} \left( \sin ((n^2 + n)a) - \sin ((n^2 - n)a) \right)$
$= \dfrac{1}{2} \left( \sin(((n+1)^2 - (n+1))a) - \sin((n^2 - n)a) \right)$
which clearly telescopes! Since the $2$ outside the brackets cancels with the $\dfrac{1}{2}$ inside, we see that the sum up to $n$ terms is
$\sin ((2^2 - 2)a) - \sin ((1^2 - 1)a) + \sin ((3^3 - 3)a) - \sin ((2^2 - 2)a) \cdots + \sin (((n+1)^2 - (n+1))a) - \sin ((n^2 - n)a)$
$= \sin (((n+1)^2 - (n+1))a) - \sin(0)$
$= \sin ((n^2 + n)a) - 0$
$= \sin \left( \dfrac{n(n+1) \pi}{2008} \right)$ .
This expression takes on an integer value iff $\dfrac{2n(n+1)}{2008} = \dfrac{n(n+1)}{1004}$ is an integer; that is, $1004 \mid n(n+1)$ . Clearly, $1004 = 2^2 \cdot 251$ , implying that $251 \mid n(n+1)$ . Since we want the smallest possible value of $n$ , we see that we must have ${n,n+1} = 251$ . If $n+1 = 251 \rightarrow n=250$ , then we have $n(n+1) = 250(251)$ , which is clearly not divisible by $1004$ . However, if $n = 251$ , then $1004 \mid n(n+1)$ , so our answer is $\boxed{251}$ .
It should be noted that the product-to-sum rules follow directly from complex trigonometry, so this solution is essentially equivalent to the solution above.
These problems are copyrighted © by the Mathematical Association of America.