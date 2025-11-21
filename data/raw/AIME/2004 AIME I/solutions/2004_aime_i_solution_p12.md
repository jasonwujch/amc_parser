# 2004 AIME I Problem 12

## Problem

Let $S$ be the set of ordered pairs $(x, y)$ such that $0 < x \le 1, 0<y\le 1,$ and $\left[\log_2{\left(\frac 1x\right)}\right]$ and $\left[\log_5{\left(\frac 1y\right)}\right]$ are both even. Given that the area of the graph of $S$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers, find $m+n.$ The notation $[z]$ denotes the greatest integer that is less than or equal to $z.$

## Solution
$\left\lfloor\log_2\left(\frac{1}{x}\right)\right\rfloor$ is even when
\[x \in \left(\frac{1}{2},1\right) \cup \left(\frac{1}{8},\frac{1}{4}\right) \cup \left(\frac{1}{32},\frac{1}{16}\right) \cup \cdots\]
Likewise: $\left\lfloor\log_5\left(\frac{1}{y}\right)\right\rfloor$ is even when
\[y \in \left(\frac{1}{5},1\right) \cup \left(\frac{1}{125},\frac{1}{25}\right) \cup \left(\frac{1}{3125},\frac{1}{625}\right) \cup \cdots\]
Graphing this yields a series of rectangles which become smaller as you move toward the origin . The $x$ interval of each box is given by the geometric sequence $\frac{1}{2} , \frac{1}{8}, \frac{1}{32}, \cdots$ , and the $y$ interval is given by $\frac{4}{5} , \frac{4}{125}, \frac{4}{3125}, \cdots$
Each box is the product of one term of each sequence. The sum of these boxes is simply the product of the sum of each sequence or:
\[\left(\frac{1}{2} + \frac{1}{8} + \frac{1}{32} \ldots \right)\left(\frac{4}{5} + \frac{4}{125} + \frac{4}{3125} \ldots \right)=\left(\frac{\frac{1}{2}}{1 - \frac{1}{4}}\right)\left(\frac{\frac{4}{5}}{1-\frac{1}{25}}\right)= \frac{2}{3} \cdot \frac{5}{6} = \frac{5}{9},\] and the answer is $m+n = 5 + 9 = \boxed{014}$ .
These problems are copyrighted © by the Mathematical Association of America.