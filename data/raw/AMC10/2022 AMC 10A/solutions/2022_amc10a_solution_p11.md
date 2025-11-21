# 2022 AMC 10A Problem 11

## Problem

Ted mistakenly wrote $2^m\cdot\sqrt{\frac{1}{4096}}$ as $2\cdot\sqrt[m]{\frac{1}{4096}}.$ What is the sum of all real numbers $m$ for which these two expressions have the same value?

$\textbf{(A) } 5 \qquad \textbf{(B) } 6 \qquad \textbf{(C) } 7 \qquad \textbf{(D) } 8 \qquad \textbf{(E) } 9$

## Solution 1
We are given that \[2^m\cdot\sqrt{\frac{1}{4096}} = 2\cdot\sqrt[m]{\frac{1}{4096}}.\] Converting everything into powers of $2$ and equating exponents, we have \begin{align*} 2^m\cdot(2^{-12})^{\frac12} &= 2\cdot (2^{-12})^{\frac1m} \\ 2^{m-6} &= 2^{1-\frac{12}{m}} \\ m-6 &= 1-\frac{12}{m}. \end{align*} We multiply both sides by $m,$ then rearrange as \[m^2-7m+12=0.\] By Vieta's Formulas, the sum of such values of $m$ is $\boxed{\textbf{(C) } 7}.$
Note that $m=3$ or $m=4$ from the quadratic equation above.
~MRENTHUSIASM ~KingRavi

## Solution 2 (Logarithms)
We can rewrite the equation using fractional exponents and take logarithms of both sides: \[\log_2{(2^{m}\cdot4096^{-1/2}}) = \log_2{(2\cdot4096^{-1/m})}.\] We can then use the additive properties of logarithms to split them up: \[\log_2{(2^{m})} + \log_2{(4096^{-1/2})} = \log_2{2} + \log_2{(4096^{-1/m})}.\] Using the power rule, the fact that $4096 = 2^{12},$ and bringing the exponents down, we get \begin{align*} m - 6 &= 1 - \frac{12}{m} \\ m + \frac{12}{m} &= 7 \\ m^{2} + 12 &= 7m \\ m^{2} - 7m + 12 &= 0 \\ (m-3)(m-4) &= 0, \end{align*} from which $m = 3$ or $m = 4$ . Therefore, the answer is $3+4 = \boxed{\textbf{(C) } 7}.$
- youtube.com/indianmathguy

## Solution 3
Since third roots are conventionally positive integers, assume $m$ is an integer, so $m$ can only be $1$ , $2$ , $3$ , $4$ , $6$ , and $12$ . $\sqrt{\frac{1}{4096}}=\frac{1}{64}$ . Testing out $m$ , we see that only $3$ and $4$ work. Hence, $3+4=\boxed{\textbf{(C) }7}$ .
~MrThinker

## Video Solution 1
https://youtu.be/UmaCmhwbZMU
~Education, the Study of Everything

## Video Solution 2
https://youtu.be/x716XmDDY9w

## Video Solution by TheBeautyofMath
https://youtu.be/0kkc4-y8TkU
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .