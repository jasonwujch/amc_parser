# 2017 AIME I Problem 14

## Problem

Let $a > 1$ and $x > 1$ satisfy $\log_a(\log_a(\log_a 2) + \log_a 24 - 128) = 128$ and $\log_a(\log_a x) = 256$ . Find the remainder when $x$ is divided by $1000$ .

## Solution 1
The first condition implies
\[a^{128} = \log_a\log_a 2 + \log_a 24 - 128\]
\[128+a^{128} = \log_a\log_a 2^{24}\]
\[a^{a^{128}a^{a^{128}}} = 2^{24}\]
\[\left(a^{a^{128}}\right)^{\left(a^{a^{128}}\right)} = 2^{24} = 8^8\]
So $a^{a^{128}} = 8$ .
Putting each side to the power of $128$ :
\[\left(a^{128}\right)^{\left(a^{128}\right)} = 8^{128} = 64^{64},\]
so $a^{128} = 64 \implies a = 2^{\frac{3}{64}}$ . Specifically,
\[\log_a(x) = \frac{\log_2(x)}{\log_2(a)} = \frac{64}{3}\log_2(x)\]
so we have that
\[256 = \log_a(\log_a(x)) = \frac{64}{3}\log_2\left(\frac{64}{3}\log_2(x)\right)\]
\[12 = \log_2\left(\frac{64}{3}\log_2(x)\right)\]
\[2^{12} = \frac{64}{3}\log_2(x)\]
\[192 = \log_2(x)\]
\[x = 2^{192}\]
We only wish to find $x\bmod 1000$ . To do this, we note that $x\equiv 0\bmod 8$ and now, by the Chinese Remainder Theorem, wish only to find $x\bmod 125$ . By Euler's Totient Theorem :
\[2^{\phi(125)} = 2^{100} \equiv 1\bmod 125\]
so
\[2^{192} \equiv \frac{1}{2^8} \equiv \frac{1}{256} \equiv \frac{1}{6} \bmod 125\]
so we only need to find the inverse of $6 \bmod 125$ . It is easy to realize that $6\cdot 21 = 126 \equiv 1\bmod 125$ , so
\[x\equiv 21\bmod 125, x\equiv 0\bmod 8.\]
Using Chinese Remainder Theorem , we get that $x\equiv \boxed{896}\bmod 1000$ , finishing the solution.

## Solution 2 (Another way to find a)
\[\log_a(\log_a(\log_a 2) + \log_a 24 - 128) = 128\]
\[\implies \log_a(\log_a 2))+\log_a(24)=a^{128}+128\]
\[\implies \log_a(\log_a 2^{24})=a^{128}+128\]
\[\implies 2^{24}=a^{a^{(a^{128}+128)}}\]
Obviously letting $a=2^y$ will simplify a lot and to make the $a^{128}$ term simpler, let $a=2^{\frac{y}{128}}$ . Then,
\[2^{24}=2^{\frac{y}{128} \cdot 2^{\frac{y}{128} \cdot (2^y+128)}}=2^{\frac{y}{128} \cdot 2^{y \cdot (2^{y-7}+1)}}\]
\[\implies 24=\frac{y}{128} \cdot 2^{y \cdot (2^{y-7}+1)}\]
\[\implies 3 \cdot 2^{10}=y \cdot 2^{y \cdot (2^{y-7}+1)}\]
Obviously, $y$ is $3$ times a power of $2$ . Testing, we see $y=6$ satisfy the equation so $a=2^{\frac{3}{64}}$ . Therefore, $x=2^{192} \equiv \boxed{896} \pmod{1000}$ ~ Ddk001

## Alternate solution 1
If you've found $x$ but you don't know that much number theory.
Note $192 = 3 * 2^6$ , so what we can do is take $2^3$ and keep squaring it (mod 1000).
\[2^3 = 8\] \[2^6 = 8*8 = 64\] \[2^{12} = 64*64 \equiv 96\bmod 1000\] \[2^{24} \equiv 96*96 \equiv 216\bmod 1000\] \[2^{48} \equiv 216*216 \equiv 656\bmod 1000\] \[2^{96} \equiv 656*656 \equiv 336\bmod 1000\] \[2^{192} \equiv 336*336 \equiv \boxed{896}\bmod 1000\]

## Alternate solution 2
Another way to find $x \bmod 1000$ using modular arithmetic. In the same way as solution $1$ , we can find that. \[x\equiv 21\bmod 125, x\equiv 0\bmod 8.\] \[x = 8m = 125n+21\] For some positive integers $m$ and $n$ . Taking the equation mod $8$ gives \[5n+5 \equiv 0\bmod 8\] \[n \equiv 7\bmod 8\] \[n = 8k-1\] For some positive integer $k$ . Plug this back into the original equation. \[8m = 125(8k-1)+21\] \[8m = 1000k-104\] \[x = 8m = 1000k - 104\] \[x \equiv -104 \equiv 896\bmod 1000\] \[x \equiv 896\bmod 1000\]
~sdfgfjh

## Video Solution by mop 2024
https://youtu.be/E-7YQ9ND5Ms
~r00tsOfUnity
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .