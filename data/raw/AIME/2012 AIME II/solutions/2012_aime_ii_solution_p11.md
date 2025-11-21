# 2012 AIME II Problem 11

## Problem

Let $f_1(x) = \frac23 - \frac3{3x+1}$ , and for $n \ge 2$ , define $f_n(x) = f_1(f_{n-1}(x))$ . The value of $x$ that satisfies $f_{1001}(x) = x-3$ can be expressed in the form $\frac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
After evaluating the first few values of $f_k (x)$ , we obtain $f_4(x) = f_1(x) = \frac{2}{3} - \frac{3}{3x+1} = \frac{6x-7}{9x+3}$ . Since $1001 \equiv 2 \mod 3$ , $f_{1001}(x) = f_2(x) = \frac{3x+7}{6-9x}$ . We set this equal to $x-3$ , i.e.
$\frac{3x+7}{6-9x} = x-3 \Rightarrow x = \frac{5}{3}$ . The answer is thus $5+3 = \boxed{008}$ .

## Video Solution
https://www.youtube.com/watch?v=zBKm3M71K4c&t=47s
This video is now private.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .