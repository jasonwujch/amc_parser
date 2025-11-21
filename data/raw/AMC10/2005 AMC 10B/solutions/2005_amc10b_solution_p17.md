# 2005 AMC 10B Problem 17

## Problem

Suppose that $4^a = 5$ , $5^b = 6$ , $6^c = 7$ , and $7^d = 8$ . What is $a \cdot b\cdot c \cdot d$ ?

$\textbf{(A) } 1 \qquad \textbf{(B) } \frac{3}{2} \qquad \textbf{(C) } 2 \qquad \textbf{(D) } \frac{5}{2} \qquad \textbf{(E) } 3$

## Solution
\begin{align*} 8&=7^d \\ 8&=\left(6^c\right)^d\\ 8&=\left(\left(5^b\right)^c\right)^d\\ 8&=\left(\left(\left(4^a\right)^b\right)^c\right)^d\\ 8&=4^{a\cdot b\cdot c\cdot d}\\ 2^3&=2^{2\cdot a\cdot b\cdot c\cdot d}\\ 3&=2\cdot a\cdot b\cdot c\cdot d\\ a\cdot b\cdot c\cdot d&=\boxed{\textbf{(B) }\dfrac{3}{2}}\\ \end{align*}

## Solution 2 (logarithms)
We can write $a$ as $\log_4 5$ , $b$ as $\log_5 6$ , $c$ as $\log_6 7$ , and $d$ as $\log_7 8$ .
We know that $\log_b a$ can be rewritten as $\frac{\log a}{\log b}$ , so we have: \begin{align*} a\cdot b \cdot c \cdot d &= \frac{\cancel{\log5}}{\log4}\cdot\frac{\cancel{\log6}}{\cancel{\log5}}\cdot\frac{\cancel{\log7}}{\cancel{\log6}}\cdot\frac{\log8}{\cancel{\log7}} \\ a\cdot b \cdot c \cdot d &= \frac{\log8}{\log4} \\ a\cdot b \cdot c \cdot d &= \frac{3\cancel{\log2}}{2\cancel{\log2}} \\ a\cdot b \cdot c \cdot d &= \boxed{\textbf{(B) }\frac{3}{2}} \\ \end{align*}

## Solution 3 (logarithm chain rule)
As in Solution 2, we can write $a$ as $\log_4 5$ , $b$ as $\log_56$ , $c$ as $\log_67$ , and $d$ as $\log_78$ . $a\cdot b\cdot c\cdot d$ is equivalent to $(\log_4 5)\cdot (\log_5 6)\cdot (\log_6 7)\cdot (\log_7 8)$ . By the logarithm chain rule, this is equivalent to $\log_4 8$ , which evaluates to $\boxed{\textbf{(B) }\frac{3}{2}}$ .
~solver1104
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .