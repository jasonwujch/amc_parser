# 2017 AMC 8 Problem 16

## Problem

In the figure below, choose point $D$ on $\overline{BC}$ so that $\triangle ACD$ and $\triangle ABD$ have equal perimeters. What is the area of $\triangle ABD$ ?

[asy]draw((0,0)--(4,0)--(0,3)--(0,0)); label("$A$", (0,0), SW); label("$B$", (4,0), ESE); label("$C$", (0, 3), N); label("$3$", (0, 1.5), W); label("$4$", (2, 0), S); label("$5$", (2, 1.5), NE);[/asy]

$\textbf{(A) }\frac{3}{4}\qquad\textbf{(B) }\frac{3}{2}\qquad\textbf{(C) }2\qquad\textbf{(D) }\frac{12}{5}\qquad\textbf{(E) }\frac{5}{2}$

## Solution 1
We know that the perimeters of the two small triangles are $3+CD+AD$ and $4+BD+AD$ . Setting both equal and using $BD+CD = 5$ , we have $BD = 2$ and $CD = 3$ . Now, we simply have to find the area of $\triangle ABD$ . Since $\frac{BD}{CD} = \frac{2}{3}$ , we must have $\frac{[ABD]}{[ACD]} = 2/3$ . Combining this with the fact that $[ABC] = [ABD] + [ACD] = \frac{3\cdot4}{2} = 6$ , we get $[ABD] = \frac{2}{5}[ABC] = \frac{2}{5} \cdot 6 = \boxed{\textbf{(D) } \frac{12}{5}}$ .

## Solution 2
Since $\overline{AC}$ is $1$ less than $\overline{BC}$ , $\overline{CD}$ must be $1$ more than $\overline{BD}$ to equate the perimeter. Hence, $\overline{BD}+\overline{BD}+1=5$ , so $\overline{BD}=2$ . Therefore, the area of $\triangle ABD$ is $\frac{(2)(4)(\sin B)}{2}=4(\frac{3}{5})=\boxed{\textbf{(D) } \frac{12}{5}}$
~megaboy6679

## Video Solution by the RMM Club
https://youtu.be/itz3JyoZQYg
### See Also