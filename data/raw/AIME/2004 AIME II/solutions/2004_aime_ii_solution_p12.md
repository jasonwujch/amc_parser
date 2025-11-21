# 2004 AIME II Problem 12

## Problem

Let $ABCD$ be an isosceles trapezoid , whose dimensions are $AB = 6, BC=5=DA,$ and $CD=4.$ Draw circles of radius 3 centered at $A$ and $B,$ and circles of radius 2 centered at $C$ and $D.$ A circle contained within the trapezoid is tangent to all four of these circles. Its radius is $\frac{-k+m\sqrt{n}}p,$ where $k, m, n,$ and $p$ are positive integers , $n$ is not divisible by the square of any prime , and $k$ and $p$ are relatively prime . Find $k+m+n+p.$

## Solution
Let the radius of the center circle be $r$ and its center be denoted as $O$ .
Clearly line $AO$ passes through the point of tangency of circle $A$ and circle $O$ . Let $y$ be the height from the base of the trapezoid to $O$ . From the Pythagorean Theorem , \[3^2 + y^2 = (r + 3)^2 \Longrightarrow y = \sqrt {r^2 + 6r}.\]
We use a similar argument with the line $DO$ , and find the height from the top of the trapezoid to $O$ , $z$ , to be $z = \sqrt {r^2 + 4r}$ .
Now $y + z$ is simply the height of the trapezoid. Let $D'$ be the foot of the perpendicular from $D$ to $AB$ ; then $AD' = 3 - 2 = 1$ . By the Pythagorean Theorem, $(AD')^2 + (DD')^2 = (AD)^2 \Longrightarrow DD' = \sqrt{24}$ so we need to solve the equation $\sqrt {r^2 + 4r} + \sqrt {r^2 + 6r} = \sqrt {24}$ . We can solve this by moving one radical to the other side, and squaring the equation twice to end with a quadratic equation .
Solving this, we get $r = \frac { - 60 + 48\sqrt {3}}{23}$ , and the answer is $k + m + n + p = 60 + 48 + 3 + 23 = \boxed{134}$ .
These problems are copyrighted © by the Mathematical Association of America.