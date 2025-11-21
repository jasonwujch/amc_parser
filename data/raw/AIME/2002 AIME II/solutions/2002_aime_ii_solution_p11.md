# 2002 AIME II Problem 11

## Problem

Two distinct, real, infinite geometric series each have a sum of $1$ and have the same second term. The third term of one of the series is $1/8$ , and the second term of both series can be written in the form $\frac{\sqrt{m}-n}p$ , where $m$ , $n$ , and $p$ are positive integers and $m$ is not divisible by the square of any prime. Find $100m+10n+p$ .

## Solution 1
Let the second term of each series be $x$ . Then, the common ratio is $\frac{1}{8x}$ , and the first term is $8x^2$ .
So, the sum is $\frac{8x^2}{1-\frac{1}{8x}}=1$ . Thus, $64x^3-8x+1 = (4x-1)(16x^2+4x-1) = 0 \Rightarrow x = \frac{1}{4}, \frac{-1 \pm \sqrt{5}}{8}$ .
The only solution in the appropriate form is $x = \frac{\sqrt{5}-1}{8}$ . Therefore, $100m+10n+p = \boxed{518}$ .

## Solution 2
Let the two sequences be $a, ar, ar^2 ... \text{ }an^2$ and $x, xy, xy^2 ... \text{ }xy^n$ . We know for a fact that $ar = xy$ . We also know that the sum of the first sequence = $\frac{a}{1-r} = 1$ , and the sum of the second sequence = $\frac{x}{1-y} = 1$ . Therefore we have \[a+r = 1\] \[x+y = 1\] \[ar=xy\] We can then replace $r = \frac{xy}{a}$ and $y = \frac{ar}{x}$ . We plug them into the two equations $a+r = 1$ and $x+y = 1$ . We then get \[x^2 + ar = x\] \[a^2 + xy = a\] We subtract these equations, getting \[x^2 - a^2 + ar - xy = x-a\] Remember \[ar=xy\] , so \[(x-a)(x+a-1) = 0\] Then considering cases, we have either $x=a$ or $y=a$ . This suggests that the second sequence is in the form $r, ra, ra^2...$ , while the first sequence is in the form $a, ar, ar^2...$ Now we have that $ar^2 = \frac18$ and we also have that $a+r = 1$ . We can solve for $r$ and the only appropriate value for $r$ is $\frac{1+\sqrt{5}}{4}$ . All we want is the second term, which is $ar = \frac{ar^2}{r} = \frac{\frac18}{\frac{1+\sqrt{5}}{4}} = \frac{\sqrt{5} - 1}{8}$ solution by jj_ca888

## Solution 3
Let's ignore the "two distinct, real, infinite geometric series" part for now and focus on what it means to be a geometric series.
Let the first term of the series with the third term equal to $\frac18$ be $a,$ and the common ratio be $r.$ Then, we get that $\frac{a}{1-r} = 1 \implies a = 1-r,$ and $ar^2 = \frac18 \implies (1-r)(r^2) = \frac18.$
We see that this cubic is equivalent to $r^3 - r^2 + \frac18 = 0.$ Through experimenting, we find that one of the solutions is $r = \frac12.$ Using synthetic division leads to the quadratic $4x^2 - 2x - 1 = 0.$ This has roots $\dfrac{2 \pm \sqrt{4 - 4(4)(-1)}}{8},$ or, when reduced, $\dfrac{1 \pm \sqrt{5}}{4}.$
It becomes clear that the two geometric series have common ratio $\frac{1 + \sqrt{5}}{4}$ and $\frac{1 - \sqrt{5}}{4}.$ Let $\frac{1 + \sqrt{5}}{4}$ be the ratio that we are inspecting. We see that in this case, $a = \dfrac{3 - \sqrt{5}}{4}.$
Since the second term in the series is $ar,$ we compute this and have that \[ar = \left(\dfrac{3 - \sqrt{5}}{4} \right)\left(\dfrac{1+\sqrt{5}}{4}\right) = \dfrac{\sqrt{5} - 1}{8},\] for our answer of $100 \cdot 5 + 1 \cdot 10 + 8 = \boxed{518}.$
Solution by Ilikeapos
### Sidenote
One of the geometric series has first term $\frac{3 - \sqrt{5}}{4}$ and common ratio $\frac{1 + \sqrt{5}}{4}$ , and its third term is $\frac{1}{8}$ . The other series has first term $\frac{1 + \sqrt{5}}{4}$ and common ratio $\frac{3 - \sqrt{5}}{4}$ .

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=gIPLYMe6pqQ&t=15s
These problems are copyrighted © by the Mathematical Association of America.