# 2005 AIME I Problem 11

## Problem

A semicircle with diameter $d$ is contained in a square whose sides have length 8. Given the maximum value of $d$ is $m - \sqrt{n},$ find $m+n.$

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4 2.5 Solution 5

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

- 2.5 Solution 5

## Solution
We note that aligning the base of the semicircle with a side of the square is certainly non-optimal. If the semicircle is tangent to only one side of the square, we will have "wiggle-room" to increase its size. Once it is tangent to two adjacent sides of the square, we will maximize its size when it touches both other sides of the square. This can happen only when it is arranged so that the center of the semicircle lies on one diagonal of the square.
Now, let the square be $ABCD$ , and let $E \in AB$ and $F \in DA$ be the points at which the "corners" of the semicircle touch the square. Let $O$ be the center of the semicircle.

## Solution 1
We can just look at a quarter circle inscribed in a $45-45-90$ right triangle. We can then extend a radius, $r$ to one of the sides creating an $r,r, r\sqrt{2}$ right triangle. This means that we have $r + r\sqrt{2} = 8\sqrt{2}$ so $r = \frac{8\sqrt{2}}{1+\sqrt{2}} = 16 - 8\sqrt{2}$ . Then the diameter is $32 - \sqrt{512}$ giving us $32 + 512 = \boxed{544}$

## Solution 2
Define the radius of the semicircle as $r$ . Draw the perpendicular from $O$ to $AB$ , which forms a $45-45-90$ triangle. The length of the perpendicular is $\frac{r}{\sqrt{2}}$ . Note also that $AD$ is equal to the length of that perpendicular plus the radius to the point of tangency on $CD$ . Thus, $r + \frac{r}{\sqrt{2}} = 8$ , and $r = \frac{8\sqrt{2}}{\sqrt{2} + 1} \cdot (\frac{\sqrt{2} - 1}{\sqrt{2} - 1}) = 16 - 8\sqrt{2}$ . The diameter is then $2r = 32 - \sqrt{512}$ , and the solution is $32 + 512 = 544$ .

## Solution 3
By the comments above, $AE = AF = a$ . By the Pythagorean Theorem , $d^2 = 2a^2$ .
Now, if we draw a line through the center, $O$ , of the semicircle and its point of tangency with $BC$ , we see that this line is perpendicular to $BC$ and so parallel to $AB$ . Thus, by triangle similarity it cuts $AF$ in half, and so by symmetry the distance from $O$ to $AD$ is $\frac{a}{2}$ and so the distance from $O$ to $BC$ is $8 - \frac a2$ . But this latter quantity is also the radius of the semicircle, so $d = 16 - a$ .
Our two previous paragraphs give $2a^2 = (16 - a)^2$ so $a^2 + 32a - 256 = 0$ and $a = 16\sqrt{2} - 16$ (where we discard the negative root of that quadratic) and so $d = a\sqrt{2} = 32 - 16\sqrt{2} = 32 - \sqrt{512}$ , so the answer is $32 + 512 = 544$ .

## Solution 4
We proceed by finding the area of the square in 2 different ways. The square is obviously 8*8=64, but we can also find the area in terms of d. From the center of the circle, draw radii that hit the points where the square is tangent to the semicircle. Then the square's area is the area of the small square +2* the area of the trapezoids on the corners+ the area of an isoceles triangle. Adding these all up gives $64=\frac{d^2}{4}+\frac{d^2}{4}+(8-\frac{d\sqrt{2}}{2}+\frac{d}{2})(8-\frac{d}{2})$ Simplifying gives $d-16\sqrt{2}+d\sqrt{2}=0$ . Solving gives $d=32-16\sqrt{2}=32-\sqrt{512}$ so the answer is $32+512= \boxed{544}$ .

## Solution 5
It is easy after getting the image, after drawing labeling the lengths of those segments, assume the radius is $x$ , we can see $x=\sqrt{2}(8-x)$ and we get $2x=32-\sqrt{512}$ and we have the answer $\boxed{544}$ ~bluesoul
These problems are copyrighted © by the Mathematical Association of America.