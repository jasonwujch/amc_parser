# 2010 AIME I Problem 11

## Problem

Let $\mathcal{R}$ be the region consisting of the set of points in the coordinate plane that satisfy both $|8 - x| + y \le 10$ and $3y - x \ge 15$ . When $\mathcal{R}$ is revolved around the line whose equation is $3y - x = 15$ , the volume of the resulting solid is $\frac {m\pi}{n\sqrt {p}}$ , where $m$ , $n$ , and $p$ are positive integers, $m$ and $n$ are relatively prime , and $p$ is not divisible by the square of any prime. Find $m + n + p$ .

## Solution
The inequalities are equivalent to $y \ge x/3 + 5, y \le 10 - |x - 8|$ . We can set them equal to find the two points of intersection, $x/3 + 5 = 10 - |x - 8| \Longrightarrow |x - 8| = 5 - x/3$ . This implies that one of $x - 8, 8 - x = 5 - x/3$ , from which we find that $(x,y) = \left(\frac 92, \frac {13}2\right), \left(\frac{39}{4}, \frac{33}{4}\right)$ . The region $\mathcal{R}$ is a triangle , as shown above. When revolved about the line $y = x/3+5$ , the resulting solid is the union of two right cones that share the same base and axis.
Let $h_1,h_2$ denote the height of the left and right cones, respectively (so $h_1 > h_2$ ), and let $r$ denote their common radius. The volume of a cone is given by $\frac 13 Bh$ ; since both cones share the same base, then the desired volume is $\frac 13 \cdot \pi r^2 \cdot (h_1 + h_2)$ . The distance from the point $(8,10)$ to the line $x - 3y + 15 = 0$ is given by $\left|\frac{(8) - 3(10) + 15}{\sqrt{1^2 + (-3)^2}}\right| = \frac{7}{\sqrt{10}}$ . The distance between $\left(\frac 92, \frac {13}2\right)$ and $\left(\frac{39}{4}, \frac{33}{4}\right)$ is given by $h_1 + h_2 = \sqrt{\left(\frac{18}{4} - \frac{39}{4}\right)^2 + \left(\frac{26}{4} - \frac{33}{4}\right)^2} = \frac{7\sqrt{10}}{4}$ . Thus, the answer is $\frac{343\sqrt{10}\pi}{120} = \frac{343\pi}{12\sqrt{10}} \Longrightarrow 343 + 12 + 10 = \boxed{365}$ . (Note to MAA: Is it a coincidence that this is the number of days in a non-leap year?)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .