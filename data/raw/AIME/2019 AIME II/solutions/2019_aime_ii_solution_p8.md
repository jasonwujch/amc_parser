# 2019 AIME II Problem 8

## Problem

The polynomial $f(z)=az^{2018}+bz^{2017}+cz^{2016}$ has real coefficients not exceeding $2019$ , and $f\left(\tfrac{1+\sqrt{3}i}{2}\right)=2015+2019\sqrt{3}i$ . Find the remainder when $f(1)$ is divided by $1000$ .

## Solution 1
We have $\frac{1+\sqrt{3}i}{2} = \omega$ where $\omega = e^{\frac{i\pi}{3}}$ is a primitive 6th root of unity. Then we have
\begin{align*} f(\omega) &= a\omega^{2018} + b\omega^{2017} + c\omega^{2016}\\ &= a\omega^2 + b\omega + c \end{align*}
We wish to find $f(1) = a+b+c$ . We first look at the real parts. As $\text{Re}(\omega^2) = -\frac{1}{2}$ and $\text{Re}(\omega) = \frac{1}{2}$ , we have $-\frac{1}{2}a + \frac{1}{2}b + c = 2015 \implies -a+b + 2c = 4030$ . Looking at imaginary parts, we have $\text{Im}(\omega^2) = \text{Im}(\omega) = \frac{\sqrt{3}}{2}$ , so $\frac{\sqrt{3}}{2}(a+b) = 2019\sqrt{3} \implies a+b = 4038$ . As $a$ and $b$ do not exceed 2019, we must have $a = 2019$ and $b = 2019$ . Then $c = \frac{4030}{2} = 2015$ , so $f(1) = 4038 + 2015 = 6053 \implies f(1) \pmod{1000} = \boxed{053}$ .
-scrabbler94

## Solution 2
Denote $\frac{1+\sqrt{3}i}{2}$ with $\omega$ .
By using the quadratic formula ( $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ ) in reverse, we can find that $\omega$ is the solution to a quadratic equation of the form $ax^2+bx+c=0$ such that $2a=2$ , $-b=1$ , and $b^2-4ac=-3$ . This clearly solves to $a=1$ , $b=-1$ , and $c=1$ , so $\omega$ solves $x^2-x+1=0$ .
Multiplying $x^2-x+1=0$ by $x+1$ on both sides yields $x^3+1=0$ . Muliplying this by $x^3-1$ on both sides yields $x^6-1=0$ , or $x^6=1$ . This means that $\omega^6=1$ .
We can use this to simplify the equation $a\omega^{2018}+b\omega^{2017}+c\omega^{2016}=f(\omega)=2015+2019\sqrt{3}i$ to $a\omega^2+b\omega+c=2015+2019\sqrt{3}i.$
As in Solution 1, we use the values $\omega=\frac{1}{2}+\frac{\sqrt{3}}{2}i$ and $\omega^2=-\frac{1}{2}+\frac{\sqrt{3}}{2}i$ to find that $-\frac{1}{2}a+\frac{1}{2}b+c=2015$ and $\frac{\sqrt{3}}{2}a+\frac{\sqrt{3}}{2}b=2019\sqrt{3} \implies a+b=4038.$ Since neither $a$ nor $b$ can exceed $2019$ , they must both be equal to $2019$ . Since $a$ and $b$ are equal, they cancel out in the first equation, resulting in $c=2015$ .
Therefore, $f(1)=a+b+c=2019+2019+2015=6053$ , and $6053\bmod1000=\boxed{053}$ . ~ emerald_block

## Solution 3
Calculate the first few powers of $\frac{1+\sqrt{3}i}{2}$ .
$(\frac{1+\sqrt{3}i}{2})^1=\frac{1+\sqrt{3}i}{2}$
$(\frac{1+\sqrt{3}i}{2})^2=\frac{-1+\sqrt{3}i}{2}$
$(\frac{1+\sqrt{3}i}{2})^3=-1$
$(\frac{1+\sqrt{3}i}{2})^4=\frac{-1-\sqrt{3}i}{2}$
$(\frac{1+\sqrt{3}i}{2})^5=\frac{1-\sqrt{3}i}{2}$
$(\frac{1+\sqrt{3}i}{2})^6=1$
We figure that the power of $\frac{1+\sqrt{3}i}{2}$ repeats in a cycle 6.
$f(\frac{1+\sqrt{3}i}{2})=(a(\frac{1+\sqrt{3}i}{2})^2+b(\frac{1+\sqrt{3}i}{2})+c)(\frac{1+\sqrt{3}i}{2})^{2016}$
Since 2016 is a multiple of 6, $(\frac{1+\sqrt{3}i}{2})^{2016}=1$
$f(\frac{1+\sqrt{3}i}{2})=a(\frac{-1+\sqrt{3}i}{2})+b(\frac{1+\sqrt{3}i}{2})+c$
$f(\frac{1+\sqrt{3}i}{2})=(-\frac{1}{2}a+\frac{1}{2}b+c)+(\frac{\sqrt{3}i}{2}a+\frac{\sqrt{3}i}{2}b)=2015+2019\sqrt{3}i$
Therefore, $-\frac{1}{2}a+\frac{1}{2}b+c=2015$ and $\frac{\sqrt{3}i}{2}a+\frac{\sqrt{3}i}{2}b=2019\sqrt{3}i$
Using the first equation, we can get that $-a+b+2c=4030$ , and using the second equation, we can get that $a+b=4038$ .
Since all coefficients are less than or equal to $2019$ , $a=b=2019$ .
Therefore, $2c=4030$ and $c=2015$ .
$f(1)=a+b+c=2019+2019+2015=6053$ , and the remainder when it divides $1000$ is $\boxed{053}.$
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .