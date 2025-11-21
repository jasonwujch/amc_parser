# 2010 AIME I Problem 9

## Problem

Let $(a,b,c)$ be the real solution of the system of equations $x^3 - xyz = 2$ , $y^3 - xyz = 6$ , $z^3 - xyz = 20$ . The greatest possible value of $a^3 + b^3 + c^3$ can be written in the form $\frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution

## Solution 1
Add the three equations to get $a^3 + b^3 + c^3 = 28 + 3abc$ . Now, let $abc = p$ . $a = \sqrt [3]{p + 2}$ , $b = \sqrt [3]{p + 6}$ and $c = \sqrt [3]{p + 20}$ , so $p = abc = (\sqrt [3]{p + 2})(\sqrt [3]{p + 6})(\sqrt [3]{p + 20})$ . Now cube both sides; the $p^3$ terms cancel out. Solve the remaining quadratic to get $p = - 4, - \frac {15}{7}$ . To maximize $a^3 + b^3 + c^3$ choose $p = - \frac {15}{7}$ and so the sum is $28 - \frac {45}{7} = \frac {196 - 45}{7}$ giving $151 + 7 = \fbox{158}$ .

## Solution 2
This is almost the same as solution 1. Note $a^3 + b^3 + c^3 = 28 + 3abc$ . Next, let $k = a^3$ . Note that $b = \sqrt [3]{k + 4}$ and $c = \sqrt [3]{k + 18}$ , so we have $28 + 3\sqrt [3]{k(k+4)(k+18)} = 28+3abc=a^3+b^3+c^3=3k+22$ . Move 28 over, divide both sides by 3, then cube to get $k^3-6k^2+12k-8 = k^3+22k^2+18k$ . The $k^3$ terms cancel out, so solve the quadratic to get $k = -2, -\frac{1}{7}$ . We maximize $abc$ by choosing $k = -\frac{1}{7}$ , which gives us $a^3+b^3+c^3 = 3k + 22 = \frac{151}{7}$ . Thus, our answer is $151+7=\boxed{158}$ .

## Solution 3
We have that $x^3 = 2 + xyz$ , $y^3 = 6 + xyz$ , and $z^3 = 20 + xyz$ . Multiplying the three equations, and letting $m = xyz$ , we have that $m^3 = (2+m)(6+m)(20+m)$ , and reducing, that $7m^2 + 43m + 60 = 0$ , which has solutions $m = -\frac{15}{7}, -4$ . Adding the three equations and testing both solutions, we find the answer of $\frac{151}{7}$ , so the desired quantity is $151 + 7 = \fbox{158}$ .

## Video Solution by OmegaLearn
https://youtu.be/SpSuqWY01SE?t=1293
~ pi_is_3.14
### Remark
It is tempting to add the equations and then use the well-known factorization $x^3+y^3+z^3-3xyz = (x+y+z)(x^2+y^2+z^2-xy-xz-yz)$ . Unfortunately such a factorization is just a red herring: it doesn't give much information on $a^3+b^3+c^3$ .
### Another Remark
The real problem with adding the equations is that $x, y, z$ are real numbers based on the problem, but the adding trick only works when $x, y, z$ are integers.

## Video Solution
https://youtu.be/LXct4j_rYfw (Video unavailable as of 20240829)
~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .