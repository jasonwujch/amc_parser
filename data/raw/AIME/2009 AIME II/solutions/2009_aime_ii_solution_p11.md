# 2009 AIME II Problem 11

## Problem

For certain pairs $(m,n)$ of positive integers with $m\geq n$ there are exactly $50$ distinct positive integers $k$ such that $|\log m - \log k| < \log n$ . Find the sum of all possible values of the product $mn$ .

## Solution 1
We have $\log m - \log k = \log \left( \frac mk \right)$ , hence we can rewrite the inequality as follows: \[- \log n < \log \left( \frac mk \right) < \log n\] We can now get rid of the logarithms, obtaining: \[\frac 1n < \frac mk < n\] And this can be rewritten in terms of $k$ as \[\frac mn < k < mn\]
From $k<mn$ it follows that the $50$ solutions for $k$ must be the integers $mn-1, mn-2, \dots, mn-50$ . This will happen if and only if the lower bound on $k$ is in a suitable range -- we must have $mn-51 \leq \frac mn < mn-50$ .
Obviously there is no solution for $n=1$ . For $n>1$ the left inequality can be rewritten as $m\leq\dfrac{51n}{n^2-1}$ , and the right one as $m > \dfrac{50n}{n^2-1}$ .
Remember that we must have $m\geq n$ . However, for $n\geq 8$ we have $\dfrac{51n}{n^2-1} < n$ , and hence $m<n$ , which is a contradiction. This only leaves us with the cases $n\in\{2,3,4,5,6,7\}$ .
- For $n=2$ we have $\dfrac{100}3 < m \leq \dfrac{102}3$ with a single integer solution $m=\dfrac{102}3=34$ .
- For $n=3$ we have $\dfrac{150}8 < m \leq \dfrac{153}8$ with a single integer solution $m=\dfrac{152}8=19$ .
- For $n=4,5,6,7$ our inequality has no integer solutions for $m$ .
Therefore the answer is $34\cdot 2 + 19\cdot 3 = 68 + 57 = \boxed{125}$ .

## Solution 2 (Coincidence)
Realize that the question has the number "50" in it, where a "5" can be taken out. Then look at the year, which is 2009; subtract 2000 from 2009 to get 9, whose square root is 3. Then you get 5 to the power of 3, which is $\boxed{125}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.