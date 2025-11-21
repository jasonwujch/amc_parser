# 2011 AIME II Problem 3

## Problem

The degree measures of the angles in a convex 18-sided polygon form an increasing arithmetic sequence with integer values. Find the degree measure of the smallest angle .

## Solution

## Solution 1
The average angle in an 18-gon is $160^\circ$ . In an arithmetic sequence the average is the same as the median, so the middle two terms of the sequence average to $160^\circ$ . Thus for some positive (the sequence is increasing and thus non-constant) integer $d$ , the middle two terms are $(160-d)^\circ$ and $(160+d)^\circ$ . Since the step is $2d$ the last term of the sequence is $(160 + 17d)^\circ$ , which must be less than $180^\circ$ , since the polygon is convex. This gives $17d < 20$ , so the only suitable positive integer $d$ is 1. The first term is then $(160-17)^\circ = \fbox{143}.$

## Solution 2
Another way to solve this problem would be to use exterior angles. Exterior angles of any polygon add up to $360^{\circ}$ . Since there are $18$ exterior angles in an 18-gon, the average measure of an exterior angles is $\frac{360}{18}=20^\circ$ . We know from the problem that since the exterior angles must be in an arithmetic sequence, the median and average of them is $20$ . Since there are even number of exterior angles, the middle two must be $19^\circ$ and $21^\circ$ , and the difference between terms must be $2$ . Check to make sure the smallest exterior angle is greater than $0$ : $19-2(8)=19-16=3^\circ$ . It is, so the greatest exterior angle is $21+2(8)=21+16=37^\circ$ and the smallest interior angle is $180-37=\boxed{143}$ .

## Solution 3
The sum of the angles in a 18-gon is $(18-2) \cdot 180^\circ = 2880 ^\circ.$ Because the angles are in an arithmetic sequence, we can also write the sum of the angles as $a+(a+d)+(a+2d)+\dots+(a+17d)=18a+153d,$ where $a$ is the smallest angle and $d$ is the common difference. Since these two are equal, we know that $18a+153d = 2880 ^\circ,$ or $2a+17d = 320^\circ.$ The smallest value of $d$ that satisfies this is $d=2,$ so $a=143.$ Other values of $d$ and $a$ satisfy that equation, but if we tried any of them the last angle would be greater than $180,$ so the only value of $a$ that works is $a=\boxed{143}$ .
Note: The equation $2a+17d = 320^\circ$ can also be obtained by using the sum of an arithmetic sequence formula $\frac{2a_1+(n-1)d}{2} \cdot n$ . We set $n = 18$ and equate it to 2880, thereby achieving the same result. ~Eclipse471 ~note by cxsmi

## Solution 4
Each individual angle in a $18$ -gon is $\frac {(18-2) \cdot 180^\circ}{18} = 160^\circ$ . Since no angle in a convex polygon can be larger than $180^\circ$ , the smallest angle possible is in the set $159, 161, 157, 163, 155, 165, 153, 167, 151, 169, 149, 171, 147, 173, 145, 175, 143, 177$ .
Our smallest possible angle is $\boxed {143}$
~Arcticturn
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .