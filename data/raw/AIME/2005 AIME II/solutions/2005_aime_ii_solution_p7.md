# 2005 AIME II Problem 7

## Problem

Let $x=\frac{4}{(\sqrt{5}+1)(\sqrt[4]{5}+1)(\sqrt[8]{5}+1)(\sqrt[16]{5}+1)}.$ Find $(x+1)^{48}$ .

## Solution 1
We note that in general,
${} (\sqrt[2^n]{5} + 1)(\sqrt[2^n]{5} - 1) = (\sqrt[2^n]{5})^2 - 1^2 = \sqrt[2^{n-1}]{5} - 1$ .
It now becomes apparent that if we multiply the numerator and denominator of $\frac{4}{ (\sqrt{5}+1) (\sqrt[4]{5}+1) (\sqrt[8]{5}+1) (\sqrt[16]{5}+1) }$ by $(\sqrt[16]{5} - 1)$ , the denominator will telescope to $\sqrt[1]{5} - 1 = 4$ , so
$x = \frac{4(\sqrt[16]{5} - 1)}{4} = \sqrt[16]{5} - 1$ .
It follows that $(x + 1)^{48} = (\sqrt[16]5)^{48} = 5^3 = \boxed{125}$ .

## Solution 2 (Bashing)
Let $y=\sqrt[16]{5}$ , then expanding the denominator results in: \[(y^8+1)(y^4+1) =(y^{12}+y^8+y^4+1)\] \[(y^{12}+y^8+y^4+1)(y^2+1)=(y^{14}+y^{12}+y^{10}+y^8+y^6+y^4+y^2+1)\] \[(y^{14}+y^{12}+y^{10}+y^8+y^6+y^4+y^2+1)(y+1) = (y^{15}+y^{14}+y^{13}+y^{12}+y^{11}+y^{10}+y^9+y^8+y^7+y^6+y^5+y^4+y^3+y^2+y+1)=\frac{y^{16}-1}{y-1}\]
Therefore: \[\frac{4}{(y^{16}-1)/(y-1)} = \frac{4(y-1)}{y^{16}-1}=\frac{4(y-1)}{4} = y-1\]
It is evident that $x+1 = (y-1)+1 = \sqrt[16]5$ as Solution 1 states.

## Solution 3
Like Solution $2$ , let $z=\sqrt[16]{5}$ Then, the expression becomes
$x=\frac{4}{(z+1)(z^2+1)(z^4+1)(z^8+1)}$ Now, multiplying by the conjugate of each binomial in the denominator, we obtain...
$x=\frac{4(z-1)(z^2-1)(z^4-1)(z^8-1)}{(z^2-1)(z^4-1)(z^8-1)(z^{16}-1)}\implies x=\frac{4(z-1)}{z^{16}-1}$ Plugging back in,
$x=\frac{4({\sqrt[16]{5}-1)}}{5-1}\implies x=\sqrt[16]{5}-1$
Hence, after some basic exponent rules, we find the answer is $\boxed{125}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.