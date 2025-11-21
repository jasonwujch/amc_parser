# 2020 AMC 10B Problem 20

## Problem

Let $B$ be a right rectangular prism (box) with edges lengths $1,$ $3,$ and $4$ , together with its interior. For real $r\geq0$ , let $S(r)$ be the set of points in $3$ -dimensional space that lie within a distance $r$ of some point in $B$ . The volume of $S(r)$ can be expressed as $ar^{3} + br^{2} + cr +d$ , where $a,$ $b,$ $c,$ and $d$ are positive real numbers. What is $\frac{bc}{ad}?$

$\textbf{(A) } 6 \qquad\textbf{(B) } 19 \qquad\textbf{(C) } 24 \qquad\textbf{(D) } 26 \qquad\textbf{(E) } 38$

## Solution
Split $S(r)$ into 4 regions:
1. The rectangular prism itself
2. The extensions of the faces of $B$
3. The quarter cylinders at each edge of $B$
4. The one-eighth spheres at each corner of $B$
Region 1: The volume of $B$ is $1 \cdot 3 \cdot 4 = 12$ , so $d=12$ .
Region 2: This volume is equal to the surface area of $B$ times $r$ (these "extensions" are just more boxes). The volume is then $\text{SA} \cdot r=2(1 \cdot 3 + 1 \cdot 4 + 3 \cdot 4)r=38r$ to get $c=38$ .
Region 3: We see that there are 12 quarter-cylinders, 4 of each type. We have 4 quarter-cylinders of height 1, 4 quarter-cylinders of height 3, 4 quarter-cylinders of height 4. Since 4 quarter-cylinders make a full cylinder, the total volume is $4 \cdot \dfrac{1\pi r^2}{4} + 4 \cdot \dfrac{3\pi r^2}{4} + 4 \cdot \dfrac{4 \pi r^2}{4}=8 \pi r^2$ . Therefore, $b=8\pi$ .
Region 4: There is an eighth-sphere of radius $r$ at each corner of $B$ . Since there are 8 corners, these eighth-spheres add up to 1 full sphere of radius $r$ . The volume of this sphere is then $\frac{4}{3}\pi \cdot r^3$ , so $a=\frac{4\pi}{3}$ .
Using these values, $\dfrac{bc}{ad}=\frac{(8\pi)(38)}{(4\pi/3)(12)} = \boxed{\textbf{(B) }19}$ .
To see a diagram of $S(r)$ , view TheBeautyofMath's explanation video (Video Solution 2).
~DrJoyo
~Edits by BakedPotato66

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/SIwp-70zu7o
~Education, the Study of Everything

## Video Solution
https://youtu.be/3BvJeZU3T-M?t=1351

## Video Solution
https://www.youtube.com/watch?v=NAZTdSecBvs
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .