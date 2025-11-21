# 2008 AMC 10A Problem 20

## Problem

Trapezoid $ABCD$ has bases $\overline{AB}$ and $\overline{CD}$ and diagonals intersecting at $K.$ Suppose that $AB = 9$ , $DC = 12$ , and the area of $\triangle AKD$ is $24.$ What is the area of trapezoid $ABCD$ ?

$\mathrm{(A)}\ 92\qquad\mathrm{(B)}\ 94\qquad\mathrm{(C)}\ 96\qquad\mathrm{(D)}\ 98 \qquad\mathrm{(E)}\ 100$

## Solution 1
Since $\overline{AB} \parallel \overline{DC}$ it follows that $\triangle ABK \sim \triangle CDK$ . Thus $\frac{KA}{KC} = \frac{KB}{KD} = \frac{AB}{DC} = \frac{3}{4}$ .
We now introduce the concept of area ratios : given two triangles that share the same height, the ratio of the areas is equal to the ratio of their bases. Since $\triangle AKB, \triangle AKD$ share a common altitude to $\overline{BD}$ , it follows that (we let $[\triangle \ldots]$ denote the area of the triangle) $\frac{[\triangle AKB]}{[\triangle AKD]} = \frac{KB}{KD} = \frac{3}{4}$ , so $[\triangle AKB] = \frac{3}{4}(24) = 18$ . Similarly, we find $[\triangle DKC] = \frac{4}{3}(24) = 32$ and $[\triangle BKC] = 24$ .
Therefore, the area of $ABCD = [AKD] + [AKB] + [BKC] + [CKD] = 24 + 18 + 24 + 32 = 98\ \mathrm{(D)}$ .

## Solution 2
We may consider that trapezoid to be right, as there is nothing specifying its angles. Consider D and A right. Let the length of DA be h. Now we let A be (0,0) and we compute the x-coordinate of K from lines AC and DB. $y=\frac{h}{9}x$ for line DB, $y=-\frac{h}{12}x+h$ for line AC. Solving for K, $\frac{h}{9}x=-\frac{h}{12}x+h$ simplifying, $(\frac{1}{9}+\frac{1}{12})x=1$ , $x=\frac{72}{14}=\frac{36}{7}$ . Using the fact that $\frac{1}{2}*h*x=24$ , we solve for h. $\frac{1}{2}*\frac{36}{7}*h=24, h=\frac{7}{18}*24=\frac{7*4}{3}$ . Applying trapezoid area formula: $\frac{7*4}{3}*\frac{9+12}{2}=7*7*2=98$ . Thus, the area is 98 and the answer is $\mathrm{(D)}$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .