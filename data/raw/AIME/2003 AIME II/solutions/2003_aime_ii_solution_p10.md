# 2003 AIME II Problem 10

## Problem

Two positive integers differ by $60$ . The sum of their square roots is the square root of an integer that is not a perfect square. What is the maximum possible sum of the two integers?

## Solution
Call the two integers $b$ and $b+60$ , so we have $\sqrt{b}+\sqrt{b+60}=\sqrt{c}$ . Square both sides to get $2b+60+2\sqrt{b^2+60b}=c$ . Thus, $b^2+60b$ must be a square, so we have $b^2+60b=n^2$ , and $(b+n+30)(b-n+30)=900$ . The sum of these two factors is $2b+60$ , so they must both be even. To maximize $b$ , we want to maximixe $b+n+30$ , so we let it equal $450$ and the other factor $2$ , but solving gives $b=196$ , which is already a perfect square, so we have to keep going. In order to keep both factors even, we let the larger one equal $150$ and the other $6$ , which gives $b=48$ . This checks, so the solution is $48+108=\boxed{156}$ .
Video Solution from Khan Academy: https://www.youtube.com/watch?v=Hh3iY4tdkGI
These problems are copyrighted © by the Mathematical Association of America.