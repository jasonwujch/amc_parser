# 2001 AIME II Problem 7

## Problem

Let $\triangle{PQR}$ be a right triangle with $PQ = 90$ , $PR = 120$ , and $QR = 150$ . Let $C_{1}$ be the inscribed circle . Construct $\overline{ST}$ with $S$ on $\overline{PR}$ and $T$ on $\overline{QR}$ , such that $\overline{ST}$ is perpendicular to $\overline{PR}$ and tangent to $C_{1}$ . Construct $\overline{UV}$ with $U$ on $\overline{PQ}$ and $V$ on $\overline{QR}$ such that $\overline{UV}$ is perpendicular to $\overline{PQ}$ and tangent to $C_{1}$ . Let $C_{2}$ be the inscribed circle of $\triangle{RST}$ and $C_{3}$ the inscribed circle of $\triangle{QUV}$ . The distance between the centers of $C_{2}$ and $C_{3}$ can be written as $\sqrt {10n}$ . What is $n$ ?

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 (analytic) 2.2 Solution 2 (synthetic) 2.3 Solution 3 2.4 Note 2.5 Solution 4 (easy but hard to see)

- 3 See also

- 2.1 Solution 1 (analytic)

- 2.2 Solution 2 (synthetic)

- 2.3 Solution 3

- 2.4 Note

- 2.5 Solution 4 (easy but hard to see)

## Solution

## Solution 1 (analytic)
Let $P = (0,0)$ be at the origin. Using the formula $A = rs$ on $\triangle PQR$ , where $r_{1}$ is the inradius (similarly define $r_2, r_3$ to be the radii of $C_2, C_3$ ), $s = \frac{PQ + QR + RP}{2} = 180$ is the semiperimeter , and $A = \frac 12 bh = 5400$ is the area, we find $r_{1} = \frac As = 30$ . Or, the inradius could be directly by using the formula $\frac{a+b-c}{2}$ , where $a$ and $b$ are the legs of the right triangle and $c$ is the hypotenuse. (This formula should be used only for right triangles .) Thus $ST, UV$ lie respectively on the lines $y = 60, x = 60$ , and so $RS = 60, UQ = 30$ .
Note that $\triangle PQR \sim \triangle STR \sim \triangle UQV$ . Since the ratio of corresponding lengths of similar figures are the same, we have
\[\frac{r_{1}}{PR} = \frac{r_{2}}{RS} \Longrightarrow r_{2} = 15\ \text{and} \ \frac{r_{1}}{PQ} = \frac{r_{3}}{UQ} \Longrightarrow r_{3} = 10.\]
Let the centers of $\odot C_2, C_3$ be $O_2 = (0 + r_{2}, 60 + r_{2}) = (15, 75), O_3 = (60 + r_{3}, 0 + r_{3}) = (70,10)$ , respectively; then by the distance formula we have $O_2O_3 = \sqrt{55^2 + 65^2} = \sqrt{10 \cdot 725}$ . Therefore, the answer is $n = \boxed{725}$ .

## Solution 2 (synthetic)
We compute $r_1 = 30, r_2 = 15, r_3 = 10$ as above. Let $A_1, A_2, A_3$ respectively the points of tangency of $C_1, C_2, C_3$ with $QR$ .
By the Two Tangent Theorem , we find that $A_{1}Q = 60$ , $A_{1}R = 90$ . Using the similar triangles, $RA_{2} = 45$ , $QA_{3} = 20$ , so $A_{2}A_{3} = QR - RA_2 - QA_3 = 85$ . Thus $(O_{2}O_{3})^{2} = (15 - 10)^{2} + (85)^{2} = 7250\implies n=\boxed{725}$ .

## Solution 3
The radius of an incircle is $r=A_t/\text{semiperimeter}$ . The area of the triangle is equal to $\frac{90\times120}{2} = 5400$ and the semiperimeter is equal to $\frac{90+120+150}{2} = 180$ . The radius, therefore, is equal to $\frac{5400}{180} = 30$ . Thus using similar triangles the dimensions of the triangle circumscribing the circle with center $C_2$ are equal to $120-2(30) = 60$ , $\frac{1}{2}(90) = 45$ , and $\frac{1}{2}\times150 = 75$ . The radius of the circle inscribed in this triangle with dimensions $45\times60\times75$ is found using the formula mentioned at the very beginning. The radius of the incircle is equal to $15$ .
Defining $P$ as $(0,0)$ , $C_2$ is equal to $(60+15,15)$ or $(75,15)$ . Also using similar triangles, the dimensions of the triangle circumscribing the circle with center $C_3$ are equal to $90-2(30)$ , $\frac{1}{3}\times120$ , $\frac{1}{3}\times150$ or $30,40,50$ . The radius of $C_3$ by using the formula mentioned at the beginning is $10$ . Using $P$ as $(0,0)$ , $C_3$ is equal to $(10, 60+10)$ or $(10,70)$ . Using the distance formula, the distance between $C_2$ and $C_3$ : $\sqrt{(75-10)^2 +(15-70)^2}$ this equals $\sqrt{7250}$ or $\sqrt{725\times10}$ , thus $n$ is $\boxed{725}$ .
### Note
The problem can be reduced to a $3-4-5$ triangle for the initial calculations, where $C_2$ is calculated to be ( $\frac{5}{2}, \frac{1}{2})$ , and $C_3$ is calculated to be ( $\frac{1}{3}, \frac{7}{3})$ . After we find the incenters the points can be scaled up by a factor of $30$ for the final distance calculation.

## Solution 4 (easy but hard to see)
We can calculate the inradius of each triangle as with the previous solutions. Now, notice that the hexagon $PSTVU$ is a square with its corner cut off. We literally complete the square and mark the last corner as point X. Now, construct right triangle with $C_3C_2$ as its hypotenuse. The right angle will be at point $Y$ . We will now find the length of each leg and use the Pythagorean Theorem to compute the desired length. We see that the length of $C_3Y$ is $50 + 15 = 65$ , as seen by the inradius of $C_2$ and $10$ less than the square's side length. $C_2Y$ is $45 + 10 = 55$ , which is $15$ less than the square plus the inradius of $C_3$ . Our final answer is $\sqrt{65^2 + 55^2} = \sqrt{7250} = \sqrt{(10)(725)} \rightarrow \boxed{725}$ .
These problems are copyrighted © by the Mathematical Association of America.