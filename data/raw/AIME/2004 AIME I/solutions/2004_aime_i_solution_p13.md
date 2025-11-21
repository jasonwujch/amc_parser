# 2004 AIME I Problem 13

## Problem

The polynomial $P(x)=(1+x+x^2+\cdots+x^{17})^2-x^{17}$ has $34$ complex roots of the form $z_k = r_k[\cos(2\pi a_k)+i\sin(2\pi a_k)], k=1, 2, 3,\ldots, 34,$ with $0 < a_1 \le a_2 \le a_3 \le \cdots \le a_{34} < 1$ and $r_k>0.$ Given that $a_1 + a_2 + a_3 + a_4 + a_5 = m/n,$ where $m$ and $n$ are relatively prime positive integers, find $m+n.$

## Solution
We see that the expression for the polynomial $P$ is very difficult to work with directly, but there is one obvious transformation to make: sum the geometric series :
\begin{align*} P(x) &= \left(\frac{x^{18} - 1}{x - 1}\right)^2 - x^{17} = \frac{x^{36} - 2x^{18} + 1}{x^2 - 2x + 1} - x^{17}\\ &= \frac{x^{36} - x^{19} - x^{17} + 1}{(x - 1)^2} = \frac{(x^{19} - 1)(x^{17} - 1)}{(x - 1)^2} \end{align*}
This expression has roots at every $17$ th root and $19$ th roots of unity , other than $1$ . Since $17$ and $19$ are relatively prime , this means there are no duplicate roots. Thus, $a_1, a_2, a_3, a_4$ and $a_5$ are the five smallest fractions of the form $\frac m{19}$ or $\frac n {17}$ for $m, n > 0$ .
$\frac 3 {17}$ and $\frac 4{19}$ can both be seen to be larger than any of $\frac1{19}, \frac2{19}, \frac3{19}, \frac 1{17}, \frac2{17}$ , so these latter five are the numbers we want to add.
$\frac1{19}+ \frac2{19}+ \frac3{19}+ \frac 1{17}+ \frac2{17}= \frac6{19} + \frac 3{17} = \frac{6\cdot17 + 3\cdot19}{17\cdot19} = \frac{159}{323}$ and so the answer is $159 + 323 = \boxed{482}$ .
These problems are copyrighted © by the Mathematical Association of America.