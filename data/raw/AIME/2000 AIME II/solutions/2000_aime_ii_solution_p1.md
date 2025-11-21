# 2000 AIME II Problem 1

## Problem

The number

can be written as $\frac mn$ where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution

## Solution 1
$\frac 2{\log_4{2000^6}} + \frac 3{\log_5{2000^6}}$
$=\frac{\log_4{16}}{\log_4{2000^6}}+\frac{\log_5{125}}{\log_5{2000^6}}$
$=\frac{\log{16}}{\log{2000^6}}+\frac{\log{125}}{\log{2000^6}}$
$=\frac{\log{2000}}{\log{2000^6}}$
$=\frac{\log{2000}}{6\log{2000}}$
$=\frac{1}{6}$
Therefore, $m+n=1+6=\boxed{007}$

## Solution 2
Alternatively, we could've noted that, because $\frac 1{\log_a{b}} = \log_b{a}$
\begin{align*} \frac 2{\log_4{2000^6}} + \frac 3{\log_5{2000^6}} &= 2 \cdot \frac{1}{\log_4{2000^6}} + 3\cdot \frac {1}{\log_5{2000^6} }\\ &=2{\log_{2000^6}{4}} + 3{\log_{2000^6}{5}} \\ &={\log_{2000^6}{4^2}} + {\log_{2000^6}{5^3}}\\ &={\log_{2000^6}{4^2 \cdot 5^3}}\\ &={\log_{2000^6}{2000}}\\ &= {\frac{1}{6}}.\end{align*}
Therefore our answer is $1 + 6 = \boxed{007}$ .

## Solution 3
We know that $2 = \log_4{16}$ and $3 = \log_5{125}$ , and by base of change formula, $\log_a{b} = \frac{\log_c{b}}{\log_c{a}}$ . Lastly, notice $\log a + \log b = \log ab$ for all bases. \begin{align*} \frac 2{\log_4{2000^6}} + \frac 3{\log_5{2000^6}} = \log_{2000^6}{16} + \log_{2000^6}{125} = \log_{2000^6}{2000} = \frac16 \implies \boxed{007} \end{align*}
$\bold{Solution}$ $\bold{written}$ $\bold{by}$
~ $\bold{PaperMath}$

## Solution 4
\[\frac{2}{\log_4 2000^6} + \frac{3}{\log_5 2000^6}\] \[= \frac{1}{3\log_4 2000} + \frac{1}{2\log_5 2000}\] \[= \frac{1}{3} \log_{2000} 4 + \frac{1}{2} \log_{2000} 5\] \[= \log_{2000} (\sqrt[3]{4} \cdot \sqrt{5}) = x\] \[\implies 2^{4x} \cdot 5^{3x} = 2^{\frac{2}{3}} \cdot 5^{\frac{1}{2}}\] \[\implies 4x + (3\log_2 5)x = \frac{2}{3}+\frac{1}{2} \log_2 5\] \[\implies x = \frac{\frac{2}{3} + \frac{1}{2} \log_2 5}{4 + 3\log_2 5}\] \[\implies 6x = \frac{4 + 3\log_2 5}{4 + 3\log_2 5}\] \[\implies x = \frac{1}{6}\] \[\implies m + n = \boxed{007}\]
~ cxsmi

## Video Solution by Pi Academy
https://youtu.be/ucn9yfcu1QY?si=r3ebuzJNd2uAq0kV
~ Pi Academy
These problems are copyrighted © by the Mathematical Association of America.