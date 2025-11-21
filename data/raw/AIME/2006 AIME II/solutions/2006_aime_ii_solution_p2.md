# 2006 AIME II Problem 2

## Problem

The lengths of the sides of a triangle with positive area are $\log_{10} 12$ , $\log_{10} 75$ , and $\log_{10} n$ , where $n$ is a positive integer. Find the number of possible values for $n$ .

## Solution
By the Triangle Inequality and applying the well-known logarithmic property $\log_{c} a + \log_{c} b = \log_{c} ab$ , we have that
$\log_{10} 12 + \log_{10} n > \log_{10} 75$
$\log_{10} 12n > \log_{10} 75$
$12n > 75$
$n > \frac{75}{12} = \frac{25}{4} = 6.25$
Also,
$\log_{10} 12 + \log_{10} 75 > \log_{10} n$
$\log_{10} 12\cdot75 > \log_{10} n$
$n < 900$
Combining these two inequalities:
\[6.25 < n < 900\]
Thus $n$ is in the set $(6.25 , 900)$ ; the number of positive integer $n$ which satisfies this requirement is $\boxed{893}$ .
These problems are copyrighted © by the Mathematical Association of America.