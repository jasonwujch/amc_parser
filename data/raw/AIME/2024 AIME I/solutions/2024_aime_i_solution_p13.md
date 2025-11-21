# 2024 AIME I Problem 13

## Problem

Let $p$ be the least prime number for which there exists a positive integer $n$ such that $n^{4}+1$ is divisible by $p^{2}$ . Find the least positive integer $m$ such that $m^{4}+1$ is divisible by $p^{2}$ .

## Solution 1
If \(p=2\), then \(4\mid n^4+1\) for some integer \(n\). But \(\left(n^2\right)^2\equiv0\) or \(1\pmod4\), so it is impossible. Thus \(p\) is an odd prime.
There are two ways to do the first part:
First Method using FLT. For integer \(n\) such that \(p^2\mid n^4+1\), we have \(p\mid n^4+1\), hence \(p\nmid n^4-1\), but \(p\mid n^8-1\). By Fermat's Little Theorem , \(p\mid n^{p-1}-1\), so \begin{equation*} p\mid\gcd\left(n^{p-1}-1,n^8-1\right)=n^{\gcd(p-1,8)}-1. \end{equation*} Here, \(\gcd(p-1,8)\) mustn't be divide into \(4\) or otherwise \(p\mid n^{\gcd(p-1,8)}-1\mid n^4-1\), which contradicts. So \(\gcd(p-1,8)=8\), and so \(8\mid p-1\). The smallest such prime is clearly \(p=17=2\times8+1\).
Second Method using orders. Notice that the order modulo $p^2$ of $n^4$ must be $8$ , so $8\mid\varphi(p^2)=p(p-1)$ . Hence $8\mid p-1$ , so $p\equiv 1\pmod{8}$ . The smallest such prime is $p=17$ . ~eevee9406
So we have to find the smallest positive integer \(m\) such that \(17\mid m^4+1\). We first find the remainder of \(m\) divided by \(17\) by doing \begin{array}{|c|cccccccccccccccc|} \hline \vphantom{\tfrac11}x\bmod{17}&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16\\\hline \vphantom{\dfrac11}\left(x^4\right)+1\bmod{17}&2&0&14&2&14&5&5&0&0&5&5&14&2&14&0&2\\\hline \end{array} So \(m\equiv\pm2\), \(\pm8\pmod{17}\). If \(m\equiv2\pmod{17}\), let \(m=17k+2\), by the binomial theorem, \begin{align*} 0&\equiv(17k+2)^4+1\equiv\mathrm {4\choose 1}(17k)(2)^3+2^4+1=17(1+32k)\pmod{17^2}\\[3pt] \implies0&\equiv1+32k\equiv1-2k\pmod{17}. \end{align*} So the smallest possible \(k=9\), and \(m=155\).
If \(m\equiv-2\pmod{17}\), let \(m=17k-2\), by the binomial theorem, \begin{align*} 0&\equiv(17k-2)^4+1\equiv\mathrm {4\choose 1}(17k)(-2)^3+2^4+1=17(1-32k)\pmod{17^2}\\[3pt] \implies0&\equiv1-32k\equiv1+2k\pmod{17}. \end{align*} So the smallest possible \(k=8\), and \(m=134\).
If \(m\equiv8\pmod{17}\), let \(m=17k+8\), by the binomial theorem, \begin{align*} 0&\equiv(17k+8)^4+1\equiv\mathrm {4\choose 1}(17k)(8)^3+8^4+1=17(241+2048k)\pmod{17^2}\\[3pt] \implies0&\equiv241+2048k\equiv3+8k\pmod{17}. \end{align*} So the smallest possible \(k=6\), and \(m=110\).
If \(m\equiv-8\pmod{17}\), let \(m=17k-8\), by the binomial theorem, \begin{align*} 0&\equiv(17k-8)^4+1\equiv\mathrm {4\choose 1}(17k)(-8)^3+8^4+1=17(241-2048k)\pmod{17^2}\\[3pt] \implies0&\equiv241+2048k\equiv3+9k\pmod{17}. \end{align*} So the smallest possible \(k=11\), and \(m=179\).
In conclusion, the smallest possible \(m\) is \(\boxed{110}\).
Solution by Quantum-Phantom

## Solution 2 (Hensel's Lemma)
We know, from Solution 1, that by Fermat's Little Theorem, $p\equiv 1\pmod{8}$ , and that the smallest $p$ satisfying such is $17$ . Thus, we have $p^2=289$ and we are attempting to lift modulo $17$ to modulo $289$ .
Given in the problem, it is established that $p^2\mid m^4 +1$ holds true, so we can guarantee that $m^4\equiv 1\pmod{289}$ . Testing for roots $r_0$ modulo $17$ gives us the solutions $r_0= \pm 2$ , $\pm 8$ , which satisfy $r_0^4\equiv -1 \pmod{17}$ .
Note that we can now use Hensel's Lemma, by defining a function $f(x)=x^4+1$ , giving $f'(x)=4x^3$ . We know firstly that, though $f(r_0)$ for all roots $r_0$ we found is congruent to $0\pmod{17}$ , this does not hold true for $f'(r_0)$ , so we guarantee that there is one lift by Hensel's Lemma to $289$ that we can perform, defined for root $r_1$ that $r_1 = r_0-\frac{f(r_0)}{f'(r_0)}\pmod{p^k}$ . We now break our work into four cases:
1. $r_0 = 2$ . $f(2)=17$ and $f'(2)=32$ , so $r_1=2-\frac{17}{32}\pmod{289}$ , and we need to find the inverse of $32\equiv 15$ modulo $17$ . By the extended Euclidean algorithm, we find that $8\cdot 15\equiv 1 \pmod{17}$ , and thus $r_1=2-17\cdot 8\equiv 155 \pmod{289}$ .
1. $r_0 = -2$ , or equivalent, $15$ . $f(-2)=17$ and $f'(-2)=-32$ , so $r_1=-2+\frac{17}{32}\pmod{289}$ . We already found the inverse of $32$ modulo $17$ , so this case has $r_1=-1+17\cdot 8\equiv 134 \pmod{289}$ .
1. $r_0 = 8$ . $f(8)=4097$ and $f'(8)=2048$ , so $r_1=-2+\frac{4097}{2048}\pmod{289}$ , and we need to find the inverse of $32\equiv 8$ modulo $17$ . We already know the inverse of $8$ is $15$ , so we end up with $r_1=8-4097\cdot 15\equiv 110\pmod{289}$ .
1. $r_0 = -8$ , or equivalent, $9$ . $f(-8)=4097$ and $f'(-8)=-2048$ , so $r_1=-8+\frac{4097}{2048}\pmod{289}$ . We already found the inverse of $2048$ modulo $17$ , so this case has $r_1=-8+4097\cdot 15\equiv 179\pmod{289}$ .
Thus, out of our four values for $m$ , the smallest is $\boxed{110}$ . Solution by juwushu .

## Solution 3 (Easy, given specialized knowledge)
Note that $n^4 + 1 \equiv 0 \pmod{p}$ means $\text{ord}_{p}(n) = 8 \mid p-1.$ The smallest prime that does this is $17$ and $2^4 + 1 = 17$ for example. Now let $g$ be a primitive root of $17^2.$ The satisfying $n$ are of the form, $g^{\frac{p(p-1)}{8}}, g^{3\frac{p(p-1)}{8}}, g^{5\frac{p(p-1)}{8}}, g^{7\frac{p(p-1)}{8}}.$ So if we find one such $n$ , then all $n$ are $n, n^3, n^5, n^7.$ Consider the $2$ from before. Note $17^2 \mid 2^{4 \cdot 17} + 1$ by LTE. Hence the possible $n$ are, $2^{17}, 2^{51}, 2^{85}, 2^{119}.$ Some modular arithmetic yields that $2^{51} \equiv \boxed{110}$ is the least value.
~Aaryabhatta1

## Solution 4 (Unfinished)
We work in the ring \(\mathbb Z/289\mathbb Z\) and use the formula \[\sqrt[4]{-1}=\pm\sqrt{\frac12}\pm\sqrt{-\frac12}.\] Since \(-\frac12=144\), the expression becomes \(\pm12\pm12i\), and it is easily calculated via Hensel that \(i=38\), thus giving an answer of \(\boxed{110}\).

## Video Solution
https://www.youtube.com/watch?v=_ambewDODiA
~MathProblemSolvingSkills.com

## Video Solution 1 by OmegaLearn.org
https://youtu.be/UyoCHBeII6g

## Video Solution 2
https://youtu.be/F3pezlR5WHc
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .