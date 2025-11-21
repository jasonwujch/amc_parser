# 2016 AIME I Problem 7

## Problem

For integers $a$ and $b$ consider the complex number \[\frac{\sqrt{ab+2016}}{ab+100}-\left({\frac{\sqrt{|a+b|}}{ab+100}}\right)i\]

Find the number of ordered pairs of integers $(a,b)$ such that this complex number is a real number.

## Solution
We consider two cases:
Case 1: $ab \ge -2016$ .
In this case, if \[0 = \text{Im}\left({\frac{\sqrt{ab+2016}}{ab+100}-\left({\frac{\sqrt{|a+b|}}{ab+100}}\right)i}\right) = -\frac{\sqrt{|a+b|}}{ab+100}\] then $ab \ne -100$ and $|a + b| = 0 = a + b$ . Thus $ab = -a^2$ so $a^2 < 2016$ . Thus $a = -44,-43, ... , -1, 0, 1, ..., 43, 44$ , yielding $89$ values. However since $ab = -a^2 \ne -100$ , we have $a \ne \pm 10$ . Thus there are $87$ allowed tuples $(a,b)$ in this case.
Case 2: $ab < -2016$ .
In this case, we want \[0 = \text{Im}\left({\frac{\sqrt{ab+2016}}{ab+100}-\left({\frac{\sqrt{|a+b|}}{ab+100}}\right)i}\right) = \frac{\sqrt{-ab-2016} - \sqrt{|a+b|}}{ab+100}\] Squaring, we have the equations $ab \ne -100$ (which always holds in this case) and \[-(ab + 2016)= |a + b|.\] Then if $a > 0$ and $b < 0$ , let $c = -b$ . If $c > a$ , \[ac - 2016 = c - a \Rightarrow (a - 1)(c + 1) = 2015 \Rightarrow (a,b) = (2, -2014), (6, -402), (14, -154), (32, -64).\] Note that $ab < -2016$ for every one of these solutions. If $c < a$ , then \[ac - 2016 = a - c \Rightarrow (a + 1)(c - 1) = 2015 \Rightarrow (a,b) = (2014, -2), (402, -6), (154, -14), (64, -32).\] Again, $ab < -2016$ for every one of the above solutions. This yields $8$ solutions. Similarly, if $a < 0$ and $b > 0$ , there are $8$ solutions. Thus, there are a total of $16$ solutions in this case.
Thus, the answer is $87 + 16 = \boxed{103}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .