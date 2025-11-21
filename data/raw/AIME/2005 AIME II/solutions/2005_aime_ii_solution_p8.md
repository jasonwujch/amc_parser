# 2005 AIME II Problem 8

## Problem

Circles $C_1$ and $C_2$ are externally tangent , and they are both internally tangent to circle $C_3.$ The radii of $C_1$ and $C_2$ are 4 and 10, respectively, and the centers of the three circles are all collinear . A chord of $C_3$ is also a common external tangent of $C_1$ and $C_2.$ Given that the length of the chord is $\frac{m\sqrt{n}}p$ where $m,n,$ and $p$ are positive integers, $m$ and $p$ are relatively prime , and $n$ is not divisible by the square of any prime , find $m+n+p.$

## Solution
Let $O_1, O_2, O_3$ be the centers and $r_1 = 4, r_2 = 10,r_3 = 14$ the radii of the circles $C_1, C_2, C_3$ . Let $T_1, T_2$ be the points of tangency from the common external tangent of $C_1, C_2$ , respectively, and let the extension of $\overline{T_1T_2}$ intersect the extension of $\overline{O_1O_2}$ at a point $H$ . Let the endpoints of the chord/tangent be $A,B$ , and the foot of the perpendicular from $O_3$ to $\overline{AB}$ be $T$ . From the similar right triangles $\triangle HO_1T_1 \sim \triangle HO_2T_2 \sim \triangle HO_3T$ ,
\[\frac{HO_1}{4} = \frac{HO_1+14}{10} = \frac{HO_1+10}{O_3T}.\]
It follows that $HO_1 = \frac{28}{3}$ , and that $O_3T = \frac{58}{7}\dagger$ . By the Pythagorean Theorem on $\triangle ATO_3$ , we find that
\[AB = 2AT = 2\left(\sqrt{r_3^2 - O_3T^2}\right) = 2\sqrt{14^2 - \frac{58^2}{7^2}} = \frac{8\sqrt{390}}{7}\]
and the answer is $m+n+p=\boxed{405}$ .
$\dagger$ Alternatively, drop an altitude from $O_1$ to $O_3T$ at $O_3'$ , and to $O_2T_2$ at $O_2'$ . Then, $O_2O_2'=10-4=6$ , and $O_1O_2=14$ . But $O_1O_3O_3'$ is similar to $O_1O_2O_2'$ so $O_3O_3'=\frac{6}{14} \cdot 10=\frac{30}{7}$ . From rectangles, $O_3'T=O_1T_1=4$ so $O_3T=4+\frac{30}{7}=\frac{58}{7}$ .

## Solution 2
Call our desired length $x$ . Note for any $X$ on $\overline{AB}$ and $Y$ on $\overline{O_1O_2}$ such that $\overline{XY}\perp\overline{AB}$ that the function $f$ such that $f(\overline{O_1Y})=\overline{XY}$ is linear. Since $(0,4)$ and $(14,10)$ , we can quickly interpolate that $f(10)=\overline{O_3T}=\frac{58}{7}$ . Then, extend $\overline{O_3T}$ until it reaches the circle on both sides; call them $P,Q$ . By Power of a Point, $\overline{PT}\cdot\overline{TQ}=\overline{AT}\cdot\overline{TB}$ . Since $\overline{AT}=\overline{TB}=\frac{1}{2}x$ , \[(\overline{PO_3}-\overline{O_3T})(\overline{QO_3}+\overline{O_3T})=\frac{1}{4}x^2\] \[\left(14+\frac{58}{7}\right)\left(14-\frac{58}{7}\right)=\frac{1}{4}x^2\] After solving for $x$ , we get $x=\frac{8\sqrt{390}}{7}$ , so our answer is $8+390+7=\boxed{405}$
These problems are copyrighted © by the Mathematical Association of America.