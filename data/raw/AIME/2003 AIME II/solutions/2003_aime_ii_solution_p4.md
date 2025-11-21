# 2003 AIME II Problem 4

## Problem

In a regular tetrahedron the centers of the four faces are the vertices of a smaller tetrahedron. The ratio of the volume of the smaller tetrahedron to that of the larger is $m/n$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Video Solution by Sal Khan

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Video Solution by Sal Khan

## Solution

## Solution 1
Embed the tetrahedron in 4-space to make calculations easier. Its vertices are $(1,0,0,0)$ , $(0,1,0,0)$ , $(0,0,1,0)$ , $(0,0,0,1)$ .
To get the center of any face, we take the average of the three coordinates of that face. The vertices of the center of the faces are: $(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}, 0)$ , $(\frac{1}{3}, \frac{1}{3},0, \frac{1}{3})$ , $(\frac{1}{3},0, \frac{1}{3}, \frac{1}{3})$ , $(0,\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$ .
The side length of the large tetrahedron is $\sqrt{2}$ by the distance formula. The side length of the smaller tetrahedron is $\frac{\sqrt{2}}{3}$ by the distance formula.
Their ratio is $1:3$ , so the ratio of their volumes is $\left(\frac{1}{3}\right)^3 = \frac{1}{27}$ .
$m+n = 1 + 27 = \boxed{28}$ .

## Solution 2
Let the large tetrahedron be $ABCD$ , and the small tetrahedron be $WXYZ$ , with $W$ on $ABC$ , $X$ on $BCD$ , $Y$ on $ACD$ , and $Z$ on $ABD$ . Clearly, the two regular tetrahedrons are similar, so if we can find the ratio of the sides, we can find the ratio of the volumes. Let $AB=1$ , for our convenience. Dropping an altitude from $W$ to $BC$ , and calling the foot $M$ , we have $WM=XM=\frac{\sqrt3}{6}$ . Since $\cos\angle{WMX}=\cos\angle{AMX}=MX/AM=1/3$ . By Law of Cosines, we have $WX=\sqrt{1/12+1/12-2(1/12)(1/3)}=1/3$ . Hence, the ratio of the volumes is $\left(\frac{1}{3}\right)^3=1/27$ . $m+n=1+27=\boxed{028}$

## Solution 3
Consider the large tetrahedron $ABCD$ and the smaller tetrahedron $WXYZ$ . Label the points as you wish, but dropping an altitude from the top vertex of $ABCD$ , we see it hits the center of the base face of $ABCD$ . This center is also one vertex of $WXYZ$ . Consider a "side" face of $ABCD$ , and the center of that face, which is another vertex of $WXYZ$ . Draw the altitude of this side face (which is an equilateral triangle). These two altitudes form a right triangle. Since the center of the Side face splits the altitude of the side face into segments in the ratio of $2:1$ (centroid), and since the bases of $WXYZ$ and $ABCD$ are parallel, we can say that the altitudes of tetrahedron $ABCD$ and $WXYZ$ are in the ratio $3:1$ . Thus we compute $\left(\frac{1}{3}\right)^3$ , and find $\frac{1}{27}$ . The sum of the numerator and denominator is thus $28$ .

## Video Solution by Sal Khan
Part 1: https://www.youtube.com/watch?v=gXnHodHNusg&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=15
Part 2: https://www.youtube.com/watch?v=wQ34EIfd-5A&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=21
- AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.