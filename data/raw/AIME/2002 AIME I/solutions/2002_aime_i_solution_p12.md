# 2002 AIME I Problem 12

## Problem

Let $F(z)=\dfrac{z+i}{z-i}$ for all complex numbers $z\neq i$ , and let $z_n=F(z_{n-1})$ for all positive integers $n$ . Given that $z_0=\dfrac{1}{137}+i$ and $z_{2002}=a+bi$ , where $a$ and $b$ are real numbers, find $a+b$ .

## Solution
Iterating $F$ we get:
\begin{align*} F(z) &= \frac{z+i}{z-i}\\ F(F(z)) &= \frac{\frac{z+i}{z-i}+i}{\frac{z+i}{z-i}-i} = \frac{(z+i)+i(z-i)}{(z+i)-i(z-i)}= \frac{z+i+zi+1}{z+i-zi-1}= \frac{(z+1)(i+1)}{(z-1)(1-i)}\\ &= \frac{(z+1)(i+1)^2}{(z-1)(1^2+1^2)}= \frac{(z+1)(2i)}{(z-1)(2)}= \frac{z+1}{z-1}i\\ F(F(F(z))) &= \frac{\frac{z+1}{z-1}i+i}{\frac{z+1}{z-1}i-i} = \frac{\frac{z+1}{z-1}+1}{\frac{z+1}{z-1}-1} = \frac{(z+1)+(z-1)}{(z+1)-(z-1)} = \frac{2z}{2} = z. \end{align*}
From this, it follows that $z_{k+3} = z_k$ , for all $k$ . Thus $z_{2002} = z_{3\cdot 667+1} = z_1 = \frac{z_0+i}{z_0-i} = \frac{(\frac{1}{137}+i)+i}{(\frac{1}{137}+i)-i}= \frac{\frac{1}{137}+2i}{\frac{1}{137}}= 1+274i.$
Thus $a+b = 1+274 = \boxed{275}$ .
These problems are copyrighted © by the Mathematical Association of America.