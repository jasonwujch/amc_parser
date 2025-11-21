# 2003 AIME I Problem 2

## Problem

One hundred concentric circles with radii $1, 2, 3, \dots, 100$ are drawn in a plane. The interior of the circle of radius $1$ is colored red, and each region bounded by consecutive circles is colored either red or green, with no two adjacent regions the same color. The ratio of the total area of the green regions to the area of the circle of radius $100$ can be expressed as $m/n,$ where $m$ and $n$ are relatively prime positive integers . Find $m + n.$

## Solution 1
To get the green area, we can color all the circles of radius $100$ or below green, then color all those with radius $99$ or below red, then color all those with radius $98$ or below green, and so forth. This amounts to adding the area of the circle of radius $100$ , but subtracting the circle of radius $99$ , then adding the circle of radius $98$ , and so forth.
The total green area is thus given by $100^{2} \pi - 99^{2} \pi + 98^{2} \pi - \ldots - 1^{2} \pi$ , while the total area is given by $100^{2} \pi$ , so the ratio is \[\frac{100^{2}\pi - 99^{2}\pi + 98^{2}\pi - \ldots - 1^{2}\pi}{100^{2}\pi}\]
For any $a$ , $a^{2}-(a-1)^{2}=a^{2}-(a^{2}-2a+1)=2a-1$ . We can cancel the factor of pi from the numerator and denominator and simplify the ratio to
\[\frac{(2\cdot100 - 1)+(2\cdot98 - 1) + \ldots + (2\cdot 2 - 1)}{100^{2}} = \frac{2\cdot(100 + 98 + \ldots + 2) - 50}{100^2}.\]
Using the formula for the sum of an arithmetic series , we see that this is equal to
\[\frac{2(50)(51)-50}{100^{2}}=\frac{50(101)}{100^{2}}=\frac{101}{200},\]
so the answer is $101 + 200 =\boxed{301}$ .
Alternatively, we can determine a pattern through trial-and-error using smaller numbers.
- For $2$ circles, the ratio is $3/4$ .
- For $4$ circles, the ratio is $5/8$ .
- For $6$ circles, the ratio is $7/12$ .
- For $8$ circles, the ratio is $9/16$ .
Now the pattern for each ratio is clear. Given $x$ circles, the ratio is $\frac{x+1}{2x}$ . For the $100$ circle case (which is what this problem is), $x=100$ , and the ratio is $\frac{101}{200}$ .
Also, using the difference of squares, the expression simplifies to $\frac{100 + 99 + 98 + 97 + ... + 1}{100^2}$ . We can easily determine the sum with $\frac{100(101)}{2} = 5050$ . Simplifying gives us $\frac{5050}{100^2} = \frac{101}{200}$ and the answer is $101 + 200 =\boxed{301}$ .

## Solution 2 (synergy)
We want to find $\frac{\sum\limits_{n=1}^{50} (4n-1)\pi}{10000\pi}=\frac{\sum\limits_{n=1}^{50} (4n-1)}{10000}=\frac{(\sum\limits_{n=1}^{50} (4n) )-50}{10000}=\frac{101}{200} \rightarrow 101+200=\boxed{301}$

## Solution 3 (Alcumus)
The sum of the areas of the green regions is
\[\left[(2^2-1^2)+(4^2-3^2)+(6^2-5^2)+\cdots+(100^2-99^2)\right]\pi\] \[=\left[(2+1)+(4+3)+(6+5)+\cdots+(100+99)\right]\pi\] \[={1\over2}\cdot100\cdot101\pi.\]
Thus the desired ratio is \[{1\over2}\cdot{{100\cdot101\pi}\over{100^2\pi}}={101\over200},\] and $m+n=\boxed{301}$ .
These problems are copyrighted © by the Mathematical Association of America.