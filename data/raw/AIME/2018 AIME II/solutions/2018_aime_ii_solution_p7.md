# 2018 AIME II Problem 7

## Problem

Triangle $ABC$ has side lengths $AB = 9$ , $BC =$ $5\sqrt{3}$ , and $AC = 12$ . Points $A = P_{0}, P_{1}, P_{2}, ... , P_{2450} = B$ are on segment $\overline{AB}$ with $P_{k}$ between $P_{k-1}$ and $P_{k+1}$ for $k = 1, 2, ..., 2449$ , and points $A = Q_{0}, Q_{1}, Q_{2}, ... , Q_{2450} = C$ are on segment $\overline{AC}$ with $Q_{k}$ between $Q_{k-1}$ and $Q_{k+1}$ for $k = 1, 2, ..., 2449$ . Furthermore, each segment $\overline{P_{k}Q_{k}}$ , $k = 1, 2, ..., 2449$ , is parallel to $\overline{BC}$ . The segments cut the triangle into $2450$ regions, consisting of $2449$ trapezoids and $1$ triangle. Each of the $2450$ regions has the same area. Find the number of segments $\overline{P_{k}Q_{k}}$ , $k = 1, 2, ..., 2450$ , that have rational length.

## Solution 1
For each $k$ between $2$ and $2450$ , the area of the trapezoid with $\overline{P_kQ_k}$ as its bottom base is the difference between the areas of two triangles, both similar to $\triangle{ABC}$ . Let $d_k$ be the length of segment $\overline{P_kQ_k}$ . The area of the trapezoid with bases $\overline{P_{k-1}Q_{k-1}}$ and $P_kQ_k$ is $\left(\frac{d_k}{5\sqrt{3}}\right)^2 - \left(\frac{d_{k-1}}{5\sqrt{3}}\right)^2 = \frac{d_k^2-d_{k-1}^2}{75}$ times the area of $\triangle{ABC}$ . (This logic also applies to the topmost triangle if we notice that $d_0 = 0$ .) However, we also know that the area of each shape is $\frac{1}{2450}$ times the area of $\triangle{ABC}$ . We then have $\frac{d_k^2-d_{k-1}^2}{75} = \frac{1}{2450}$ . Simplifying, $d_k^2-d_{k-1}^2 = \frac{3}{98}$ . However, we know that $d_0^2 = 0$ , so $d_1^2 = \frac{3}{98}$ , and in general, $d_k^2 = \frac{3k}{98}$ and $d_k = \frac{\sqrt{\frac{3k}{2}}}{7}$ . The smallest $k$ that gives a rational $d_k$ is $6$ , so $d_k$ is rational if and only if $k = 6n^2$ for some integer $n$ .The largest $n$ such that $6n^2$ is less than $2450$ is $20$ , so $k$ has $\boxed{020}$ possible values.
Solution by zeroman

## Solution 2
We have that there are $2449$ trapezoids and $1$ triangle of equal area, with that one triangle being $AP_1Q_1$ . Notice, if we "stack" the trapezoids on top of $\bigtriangleup AP_1Q_1$ the way they already are, we'd create a similar triangle, all of which are similar to $\bigtriangleup ABC$ , and since the trapezoids and $\bigtriangleup AP_1Q_1$ have equal area, each of these similar triangles $AP_kQ_k$ have area $\frac{k}{2450}\left[ ABC\right]$ , and so $\frac{\left[ AP_kQ_k\right]}{\left[ABC\right]}=\frac{k}{2450}$ . We want the ratio of the side lengths $P_kQ_k:BC$ . Since area is a 2-dimensional unit of measurement, and side lengths are 1-dimensional, the ratio is simply the square root of the areas, or \[\frac{P_kQ_k}{BC}=\sqrt{\frac{k}{2450}}\] \[\implies P_kQ_k=BC\cdot \sqrt{\frac{k}{2450}}=5\sqrt{3}\cdot\sqrt{\frac{k}{2450}}=\frac{1}{7}\cdot \sqrt{\frac{3k}{2}}=\frac{3}{7}\sqrt{\frac{k}{6}}\] \[\implies k=6n^2<2450\] \[\implies 0<n\leq 20\] so there are $\boxed{020}$ solutions.
~Solution by ktong
~Beautified by jdong2006

## Solution 3
Let $T_1$ stand for $AP_1Q_1$ , and $T_k = AP_kQ_k$ . All triangles $T$ are similar by AA. Let the area of $T_1$ be $x$ . The next trapezoid will also have an area of $x$ , as given. Therefore, $T_k$ has an area of $kx$ . The ratio of the areas is equal to the square of the scale factor for any plane figure and its image. Therefore, $P_k Q_k=P_1 Q_1\cdot \sqrt{k}$ , and the same if $Q$ is substituted for $P$ throughout. We want the side $P_k Q_k$ to be rational. Setting up proportions: \[5\sqrt{3} : \sqrt{2450}=35\sqrt{2}\] \[\sqrt{6} : 14\] which shows that $P_1 Q_1=\frac{\sqrt{6}}{14}$ . In order for $\sqrt{k} P_1 Q_1$ to be rational, $\sqrt{k}$ must be some rational multiple of $\sqrt{6}$ . This is achieved at $\sqrt{k}=\sqrt{6}, 2\sqrt{6}, \ldots, 20\sqrt{6}$ . We end there as $21\sqrt{6}=\sqrt{2646}$ . There are 20 numbers from 1 to 20, so there are $\boxed{020}$ solutions.
Solution by a1b2
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .