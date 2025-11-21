# 2019 AIME I Problem 14

## Problem

Find the least odd prime factor of $2019^8+1$ .

## Video Solution & More by MegaMath
https://www.youtube.com/watch?v=E6Vs5uf49Fc

## Solution
We know that $2019^8 \equiv -1 \pmod{p}$ for some prime $p$ . We want to find the smallest odd possible value of $p$ . By squaring both sides of the congruence, we find $2019^{16} \equiv 1 \pmod{p}$ .
Since $2019^{16} \equiv 1 \pmod{p}$ , the order of $2019$ modulo $p$ is a positive divisor of $16$ .
However, if the order of $2019$ modulo $p$ is $1, 2, 4,$ or $8,$ then $2019^8$ will be equivalent to $1 \pmod{p},$ which contradicts the given requirement that $2019^8\equiv -1\pmod{p}$ .
Therefore, the order of $2019$ modulo $p$ is $16$ . Because all orders modulo $p$ divide $\phi(p)$ , we see that $\phi(p)$ is a multiple of $16$ . As $p$ is prime, $\phi(p) = p\left(1 - \dfrac{1}{p}\right) = p - 1$ . Therefore, $p\equiv 1 \pmod{16}$ . The two smallest primes equivalent to $1 \pmod{16}$ are $17$ and $97$ . Because $16 | p - 1$ , and $p - 1 \geq 16$ , each possible value of $p$ must be verified by manual calculation to make sure that $p | 2019^8+1$ . As $2019^8 \not\equiv -1 \pmod{17}$ and $2019^8 \equiv -1 \pmod{97}$ , the smallest possible $p$ is thus $\boxed{097}$ .

## Note to solution
$\phi(k)$ is the Euler Totient Function of integer $k$ . $\phi(k)$ is the number of positive integers less than $k$ relatively prime to $k$ . Define the numbers $k_1,k_2,k_3,\cdots,k_n$ to be the prime factors of $k$ . Then, we have \[\phi(k)=k\cdot \prod^n_{i=1}\left(1-\dfrac{1}{k_i}\right).\] A property of the Totient function is that, for any prime $p$ , $\phi(p)=p-1$ .
Euler's Totient Theorem states that \[a^{\phi(k)} \equiv 1\pmod k\] if $\gcd(a,k)=1$ .
Furthermore, the order $a$ modulo $n$ for an integer $a$ relatively prime to $n$ is defined as the smallest positive integer $d$ such that $a^{d} \equiv 1\pmod n$ . An important property of the order $d$ is that $d|\phi(n)$ . It's important to remember that the order $d \leq \phi(n)$ , and Euler's Totient Theorem does not guarantee equality. That's why in this problem we had to test primes such that $d=16 | (p-1)$ , and find the smallest such prime $p$ . ~First

## Solution 2 (Basic Modular Arithmetic)
In this solution, $k$ will represent an arbitrary nonnegative integer.
We will show that any potential prime $p$ must be of the form $16k+1$ through a proof by contradiction. Suppose that there exists some prime $p$ that can not be expressed in the form $16k+1$ that is a divisor of $2019^8+1$ . First, note that if the prime $p$ is a divisor of $2019$ , then $2019^8$ is a multiple of $p$ and $2019^8+1$ is not. Thus, $p$ is not a divisor of $2019$ .
Because $2019^8+1$ is a multiple of $p$ , $2019^8+1\equiv0\pmod{p}$ . This means that $2019^8\equiv-1\pmod{p}$ , and by raising both sides to an arbitrary odd positive integer, we have that $2019^{16k+8}\equiv-1\pmod{p}$ .
Then, since the problem requires an odd prime, $p$ can be expressed as $16k+m$ , where $m$ is an odd integer ranging from $3$ to $15$ , inclusive. By Fermat's Little Theorem, $2019^{p-1}\equiv1\pmod{p}$ , and plugging in values, we get $2019^{16k+n}\equiv1\pmod{p}$ , where $n=m-1$ and is thus an even integer ranging from $2$ to $14$ , inclusive.
If $n=8$ , then $2019^{16k+8}\equiv1\pmod{p}$ , which creates a contradiction. If $n$ is not a multiple of $8$ but is a multiple of $4$ , squaring both sides of $2019^{16k+n}\equiv1\pmod{p}$ also results in the same contradictory equivalence. For all remaining $n$ , raising both sides of $2019^{16k+n}\equiv1\pmod{p}$ to the $4$ th power creates the same contradiction. (Note that $32k$ and $64k$ can both be expressed in the form $16k$ .)
Since we have proved that no value of $n$ can work, this means that a prime must be of the form $16k+1$ in order to be a factor of $2019^8+1$ . The smallest prime of this form is $17$ , and testing it, we get \[2019^8+1\equiv13^8+1\equiv169^4+1\equiv(-1)^4+1\equiv1+1\equiv2\pmod{17},\] so it does not work. The next smallest prime of the required form is $97$ , and testing it, we get \[2019^8+1\equiv(-18)^8+1\equiv324^4+1\equiv33^4+1\equiv1089^2+1\equiv22^2+1\equiv484+1\equiv-1+1\equiv0\pmod{97},\] so it works. Thus, the answer is $\boxed{097}$ . ~ emerald_block

## Solution 3 (Official MAA)
Suppose prime $p>2$ divides $2019^8+1.$ Then $2019^8\equiv -1\pmod p.$ Squaring gives $2019^{16}\equiv 1\pmod p.$ If $2019^m\equiv 1 \pmod p$ for some $0<m<16,$ it follows that \[2019^{\gcd(m,16)}\equiv 1\pmod p.\] But $2019^8\equiv -1\pmod p,$ so $\gcd(m,16)$ cannot divide $8,$ which is a contradiction. Thus $2019^{16}$ is the least positive power congruent to $1\pmod p.$ By Fermat's Little Theorem, $2019^{p-1}\equiv 1\pmod p.$ It follows that $p=16k+1$ for some positive integer $k.$ The least two primes of this form are $17$ and $97.$ The least odd factor of $2019^8+1$ is not $17$ because \[2019\equiv 13\pmod{17}\qquad \text{and}\qquad 13^2\equiv 169\equiv -1\pmod{17},\] which implies $2019^8\equiv 1\not\equiv -1\pmod {17}.$ But $2019\equiv -18\pmod{97},$ so \begin{align*} (-18)^2=324&\equiv 33\pmod{97}, \\ 33^2=1089&\equiv 22\pmod{97},\,\text{and} \\ 22^2=484&\equiv -1\pmod{97}.\end{align*} Thus the least odd prime factor is $97.$
In fact, $2019^8+1=2\cdot97\cdot p,$ where $p$ is the $25$ -digit prime \[1423275002072658812388593.\]

## Solution 4
Let $n$ represent the least odd prime that the question is asking for.
We can see that $2019^8\equiv -1\pmod n.$
Squaring both sides we get $2019^{16}\equiv 1\pmod n.$
From Fermat's Little Theorem $a^{n-1}\equiv 1\pmod n$ , we know that $n-1$ has to be a multiple of 16. So we want to test prime numbers that fit this.
The first prime we get is 17 and when we try it in $2019^8\equiv -1\pmod n,$
$2019^{8}\equiv 13^8\pmod {17}$
$169^{4}\equiv 16^4\pmod {17}$
$256^2\equiv 1\pmod {17}$
$1+1=2$
We see that 17 does not work. The next number that works from the application of Fermat's Little Theorem is 97 and when we try that,
$2019^{8}\equiv 79^8\pmod {97}$
$6241^{4}\equiv 33^4\pmod {97}$
$1089^2\equiv 22^2\pmod {97}$
$484\equiv -1\pmod {97}$
$-1+1=0$
Thus our answer is $\boxed{097}$ . ~pengf

## Video Solution
On The Spot STEM:
https://youtu.be/_vHq5_5qCd8
https://youtu.be/IF88iO5keFo

## Video Solution by The Power Of Logic
https://youtu.be/hqg5kCz6rnQ
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .