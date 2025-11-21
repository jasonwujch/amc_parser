# 2005 AIME II Problem 9

## Problem

For how many positive integers $n$ less than or equal to $1000$ is $(\sin t + i \cos t)^n = \sin nt + i \cos nt$ true for all real $t$ ?

## Solution

## Solution 1
We know by De Moivre's Theorem that $(\cos t + i \sin t)^n = \cos nt + i \sin nt$ for all real numbers $t$ and all integers $n$ . So, we'd like to somehow convert our given expression into a form from which we can apply De Moivre's Theorem.
Recall the trigonometric identities $\cos \left(\frac{\pi}2 - u\right) = \sin u$ and $\sin \left(\frac{\pi}2 - u\right) = \cos u$ hold for all real $u$ . If our original equation holds for all $t$ , it must certainly hold for $t = \frac{\pi}2 - u$ . Thus, the question is equivalent to asking for how many positive integers $n \leq 1000$ we have that $\left(\sin\left(\frac\pi2 - u\right) + i \cos\left(\frac\pi 2 - u\right)\right)^n = \sin n \left(\frac\pi2 -u \right) + i\cos n \left(\frac\pi2 - u\right)$ holds for all real $u$ .
$\left(\sin\left(\frac\pi2 - u\right) + i \cos\left(\frac\pi 2 - u\right)\right)^n = \left(\cos u + i \sin u\right)^n = \cos nu + i\sin nu$ . We know that two complex numbers are equal if and only if both their real part and imaginary part are equal. Thus, we need to find all $n$ such that $\cos n u = \sin n\left(\frac\pi2 - u\right)$ and $\sin nu = \cos n\left(\frac\pi2 - u\right)$ hold for all real $u$ .
$\sin x = \cos y$ if and only if either $x + y = \frac \pi 2 + 2\pi \cdot k$ or $x - y = \frac\pi2 + 2\pi\cdot k$ for some integer $k$ . So from the equality of the real parts we need either $nu + n\left(\frac\pi2 - u\right) = \frac\pi 2 + 2\pi \cdot k$ , in which case $n = 1 + 4k$ , or we need $-nu + n\left(\frac\pi2 - u\right) = \frac\pi 2 + 2\pi \cdot k$ , in which case $n$ will depend on $u$ and so the equation will not hold for all real values of $u$ . Checking $n = 1 + 4k$ in the equation for the imaginary parts, we see that it works there as well, so exactly those values of $n$ congruent to $1 \pmod 4$ work. There are $\boxed{250}$ of them in the given range.

## Solution 2
This problem begs us to use the familiar identity $e^{it} = \cos(t) + i \sin(t)$ . Notice, $\sin(t) + i \cos(t) = i(\cos(t) - i \sin(t)) = i e^{-it}$ since $\sin(-t) = -\sin(t)$ . Using this, $(\sin(t) + i \cos(t))^n = \sin(nt) + i \cos(nt)$ is recast as $(i e^{-it})^n = i e^{-itn}$ . Hence we must have $i^n = i \Rightarrow i^{n-1} = 1 \Rightarrow n \equiv 1 \bmod{4}$ . Thus since $1000$ is a multiple of $4$ exactly one quarter of the residues are congruent to $1$ hence we have $\boxed{250}$ .

## Solution 3
We can rewrite $\sin(t)$ as $\cos\left(\frac{\pi}{2}-t\right)$ and $\cos(t)$ as $\sin\left(\frac{\pi}{2}-t\right)$ . This means that $\sin t + i\cos t = e^{i\left(\frac{\pi}{2}-t\right)}=\frac{e^{\frac{\pi i}{2}}}{e^{it}}$ . This theorem also tells us that $e^{\frac{\pi i}{2}}=i$ , so $\sin t + i\cos t = \frac{i}{e^{it}}$ . By the same line of reasoning, we have $\sin nt + i\cos nt = \frac{i}{e^{int}}$ .
For the statement in the question to be true, we must have $\left(\frac{i}{e^{it}}\right)^n=\frac{i}{e^{int}}$ . The left hand side simplifies to $\frac{i^n}{e^{int}}$ . We cancel the denominators and find that the only thing that needs to be true is that $i^n=i$ . This is true if $n\equiv1\pmod{4}$ , and there are $\boxed{250}$ such numbers between $1$ and $1000$ . Solution by Zeroman

## Solution 4
We are using degrees in this solution instead of radians. I just process stuff better that way.
We can see that the LHS is $cis(n(90^{\circ}-t))$ , and the RHS is $cis(90^{\circ}-nt)$ So, $n(90-t) \equiv 90-nt \mod 360$ Expanding and canceling the nt terms, we will get $90n \equiv 90 \mod 360$ . Canceling gets $n \equiv 1 \mod 4$ , and thus there are $\boxed{250}$ values of n.
-AlexLikeMath

## Solution 5(CHEAP)
Let $t=0$ . Then, we have $i^n=i$ which means $n\equiv 1\pmod{4}$ . Thus, the answer is $\boxed{250}$ .

## Solution 6
We factor out $i^n$ from $(\sin t + i \cos t)^n = i^n (\cos(t) - i \sin t)= i^n(\cos(nt) - i\sin nt).$ We know the final expression must be the same as $\sin nt + i \cos nt$ so we must have $i^n(\cos(nt) - i\sin nt) = \sin nt + i \cos nt$ in which testing yields $n \equiv 1 \pmod{4}$ is the only mod that works, so we have a total of $1000 \cdot\frac{1}{4} = \boxed{250}$ integers $n$ that work.

## Solution 7
Note that this looks like de Moivre's except switched around. Using de Moivre's as motivation we try to convert the given expression into de Moivre's. Note that $\sin t = \cos(90 - t)$ and $\cos t = \sin(90 - t)$ . So we rewrite the expression and setting it equal to the given expression in the problem, we get $\cos(90 - nt) + i\sin(90 - nt) = \cos(90n - nt) + i\sin(90n - nt)$ . Now we can just look at the imaginary parts. Doing so and simplifying, we see that $1 + 4k= n$ . From this we see that $n \equiv 1\pmod{4}$ . So there are $\boxed{250}$ solutions.
~coolmath_2018

## Solution 8
$(\sin\theta + i\cos\theta)^{n} = i^{n} (\cos\theta - i\sin\theta)^n$
Hence the required condition is just $i^{n} = i$ which is true for exactly 1 in 4 consecutive numbers. Thus $\boxed{250}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.