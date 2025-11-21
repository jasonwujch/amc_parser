# 2001 AIME I Problem 9

## Problem

In triangle $ABC$ , $AB=13$ , $BC=15$ and $CA=17$ . Point $D$ is on $\overline{AB}$ , $E$ is on $\overline{BC}$ , and $F$ is on $\overline{CA}$ . Let $AD=p\cdot AB$ , $BE=q\cdot BC$ , and $CF=r\cdot CA$ , where $p$ , $q$ , and $r$ are positive and satisfy $p+q+r=2/3$ and $p^2+q^2+r^2=2/5$ . The ratio of the area of triangle $DEF$ to the area of triangle $ABC$ can be written in the form $m/n$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution

## Solution 1
We let $[\ldots]$ denote area; then the desired value is
Using the formula for the area of a triangle $\frac{1}{2}ab\sin C$ , we find that
and similarly that $\frac{[BDE]}{[ABC]} = q(1-p)$ and $\frac{[CEF]}{[ABC]} = r(1-q)$ . Thus, we wish to find \begin{align*}\frac{[DEF]}{[ABC]} &= 1 - \frac{[ADF]}{[ABC]} - \frac{[BDE]}{[ABC]} - \frac{[CEF]}{[ABC]} \\ &= 1 - p(1-r) - q(1-p) - r(1-q)\\ &= (pq + qr + rp) - (p + q + r) + 1 \end{align*} We know that $p + q + r = \frac 23$ , and also that $(p+q+r)^2 = p^2 + q^2 + r^2 + 2(pq + qr + rp) \Longleftrightarrow pq + qr + rp = \frac{\left(\frac 23\right)^2 - \frac 25}{2} = \frac{1}{45}$ . Substituting, the answer is $\frac 1{45} - \frac 23 + 1 = \frac{16}{45}$ , and $m+n = \boxed{061}$ .

## Solution 2
By the barycentric area formula, our desired ratio is equal to \begin{align*} \begin{vmatrix} 1-p & p & 0 \\ 0 & 1-q & q \\ r & 0 & 1-r \notag \end{vmatrix} &=1-p-q-r+pq+qr+pr\\ &=1-(p+q+r)+\frac{(p+q+r)^2-(p^2+q^2+r^2)}{2}\\ &=1-\frac{2}{3}+\frac{\frac{4}{9}-\frac{2}{5}}{2}\\ &=\frac{16}{45}, \end{align*} so the answer is $\boxed{061}$

## Solution 3 (Informal)
Since the only conditions are that $p + q + r = \frac{2}{3}$ and $p^2 + q^2 + r^2 = \frac{2}{5}$ , we can simply let one of the variables be equal to 0. In this case, let $p = 0$ . Then, $q + r = \frac{2}{3}$ and $q^2 + r^2$ = $\frac{2}{5}$ . Note that the ratio between the area of $DEF$ and $ABC$ is equivalent to $(1-q)(1-r)$ . Solving this system of equations, we get $q = \frac{1}{3} \pm \sqrt{\frac{4}{45}}$ , and $r = \frac{1}{3} \mp \sqrt{\frac{4}{45}}$ . Plugging back into $(1-q)(1-r)$ , we get $\frac{16}{45}$ , so the answer is $\boxed{061}$
### Note
Because the givens in the problem statement are all regarding the ratios of the sides, the side lengths of triangle $ABC$ , namely $13, 15, 17$ , are actually not necessary to solve the problem. This is clearly demonstrated in all of the above solutions, as the side lengths are not used at all.
These problems are copyrighted © by the Mathematical Association of America.