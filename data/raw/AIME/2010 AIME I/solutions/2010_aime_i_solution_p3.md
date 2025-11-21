# 2010 AIME I Problem 3

## Problem

Suppose that $y = \frac34x$ and $x^y = y^x$ . The quantity $x + y$ can be expressed as a rational number $\frac {r}{s}$ , where $r$ and $s$ are relatively prime positive integers. Find $r + s$ .

## Solution 1
Substitute $y = \frac34x$ into $x^y = y^x$ and solve. \[x^{\frac34x} = \left(\frac34x\right)^x\] \[x^{\frac34x} = \left(\frac34\right)^x \cdot x^x\] \[x^{-\frac14x} = \left(\frac34\right)^x\] \[x^{-\frac14} = \frac34\] \[x = \frac{256}{81}\] \[y = \frac34x = \frac{192}{81}\] \[x + y = \frac{448}{81}\] \[448 + 81 = \boxed{529}\]

## Solution 2
We solve in general using $c$ instead of $3/4$ . Substituting $y = cx$ , we have:
Dividing by $x^x$ , we get $(x^x)^{c - 1} = c^x$ .
Taking the $x$ th root, $x^{c - 1} = c$ , or $x = c^{1/(c - 1)}$ .
In the case $c = \frac34$ , $x = \Bigg(\frac34\Bigg)^{ - 4} = \Bigg(\frac43\Bigg)^4 = \frac {256}{81}$ , $y = \frac {64}{27}$ , $x + y = \frac {256 + 192}{81} = \frac {448}{81}$ , yielding an answer of $448 + 81 = \boxed{529}$ .

## Solution 3
Taking the logarithm base $x$ of both sides, we arrive with:
Where the last two simplifications were made since $y = \frac{3}{4}x$ . Then,
Then, $y = \left(\frac{4}{3}\right)^3$ , and thus:

## Solution 4 (another version of Solution 3)
Taking the logarithm base $x$ of both sides, we arrive with: \[y = \log_x y^x \Longrightarrow \frac{y}{x} = \log_{x} y = \log_x \left(\frac{3}{4}x\right) = \frac{3}{4}\] Now we proceed by the logarithm rule $\log(ab)=\log a + \log b$ . The equation becomes: \[\log_x \frac{3}{4} + \log_x x = \frac{3}{4}\] \[\Longleftrightarrow \log_x \frac{3}{4} + 1 = \frac{3}{4}\] \[\Longleftrightarrow \log_x \frac{3}{4} = -\frac{1}{4}\] \[\Longleftrightarrow x^{-\frac{1}{4}} = \frac{3}{4}\] \[\Longleftrightarrow \frac{1}{x^{\frac{1}{4}}} = \frac{3}{4}\] \[\Longleftrightarrow x^{\frac{1}{4}} = \frac{4}{3}\] \[\Longleftrightarrow \sqrt[4]{x} = \frac{4}{3}\] \[\Longleftrightarrow x = \left(\frac{4}{3}\right)^4=\frac{256}{81}\] Then find $y$ as in solution 3, and we get $\boxed{529}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .