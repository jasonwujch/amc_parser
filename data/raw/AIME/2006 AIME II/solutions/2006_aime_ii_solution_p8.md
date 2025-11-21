# 2006 AIME II Problem 8

## Problem

There is an unlimited supply of congruent equilateral triangles made of colored paper. Each triangle is a solid color with the same color on both sides of the paper. A large equilateral triangle is constructed from four of these paper triangles. Two large triangles are considered distinguishable if it is not possible to place one on the other, using translations, rotations, and/or reflections, so that their corresponding small triangles are of the same color.

Given that there are six different colors of triangles from which to choose, how many distinguishable large equilateral triangles may be formed?

[asy] pair A,B; A=(0,0); B=(2,0); pair C=rotate(60,A)*B; pair D, E, F; D = (1,0); E=rotate(60,A)*D; F=rotate(60,C)*E; draw(C--A--B--cycle); draw(D--E--F--cycle); [/asy]

## Solution 1
If two of our big equilateral triangles have the same color for their center triangle and the same multiset of colors for their outer three triangles, we can carry one onto the other by a combination of rotation and reflection. Thus, to make two triangles distinct, they must differ either in their center triangle or in the collection of colors which make up their outer three triangles.
There are 6 possible colors for the center triangle.
- There are ${6\choose3} = 20$ possible choices for the three outer triangles, if all three have different colors.
- There are $6\cdot 5 = 30$ (or $2 {6\choose2}$ ) possible choices for the three outer triangles, if two are one color and the third is a different color.
- There are ${6\choose1} = 6$ possible choices for the three outer triangles, if all three are the same color.
Thus, in total we have $6\cdot(20 + 30 + 6) = \boxed{336}$ total possibilities.

## Solution 2 (Burnside's Lemma)
We apply Burnside's Lemma and consider 3 rotations of 120 degrees, 240 degrees, and 0 degrees. We also consider three reflections from the three lines of symmetry in the triangle. Thus, we have to divide by $3+3=6$ for our final count.
Case 1: 0 degree rotation. This is known as the identity rotation, and there are $6^4=1296$ choices because we don't have any restrictions.
Case 2: 120 degree rotation. Note that the three "outer" sides of the triangle have to be the same during this, and the middle one can be anything. We have $6*6=36$ choices from this.
Case 3: 240 degree rotation. Similar to the 120 degree rotation, each must be the same except for the middle. We have $6*6=36$ choices from this.
Case 4: symmetry about lines. We multiply by 3 for these because the amount of colorings fixed under symmetry are the exact same each time. Two triangles do not change under this, and they must be the same. The other two triangles (1 middle and 1 outer) can be anything because they stay the same during the reflection. We have $6*6*6=216$ ways for one symmetry. There are 3 symmetries, so there are $216*3=648$ combinations in all.
Now, we add our cases up: $1296+36+36+648=2016$ . We have to divide by 6, so $2016/6=\boxed{336}$ distinguishable ways to color the triangle.

## Solution 3 (stars and bars)
There are $6$ choices for the center triangle. Note that given any $3$ colors, there is a unique way to assign them to the corner triangles. We have $6$ different colors to choose from, so the number of ways to color the corner triangles is the same as the number of ways to arrange $6 - 1 = 5$ dividers and $3$ identical items. Therefore, our answer is \[6 \binom{5 + 3}{3} = 6\binom{8}{3} = \boxed{336}.\]
-MP8148
Explanation of the bijection by WIlliamgolly: Let 1,2,3,4,5,6 be the colors, and WLOG assume that the middle triangle has a color of 6. Now, the color bijection can be formed as follows: Pick the colors to the immediate right of a divider. If there is no color to the immediate right of a divider, then that color is 6.
For example, ||12345| would represent the colors 1,1,6 as the colors chosen. Note for any three colors, there is only one way to fix it on the triangle, thus forming our stars and bars bijection.

## Solution 4 (Brute Force Casework)
If there is one color in total: there are $6$ ways.
If there are two colors in total:
Subcase 1: one color occupies 1 triangle and the other occupies 3 triangles:
Subsubcase 1: One color occupies the center triangle and the other occupies the three outer triangles: $6\cdot5=30$ ways.
Subsubcase 2: One color occupies a corner triangle and the other occupies the three other triangles: $6\cdot5=30$ ways.
Subcase 2: one color occupies 2 triangles and the other also occupies 2 triangles: this means one color must occupy the center and one outer triangle, the other color must occupy two outer triangles: $6\cdot5=30$ ways.
If there are three colors in total:
Subcase 1: one color occupies the center triangle, another occupies an outer triangle, the last color occupies the remaining two outer triangles: $6\cdot5\cdot4=120$ ways.
Subcase 2: one color occupies an outer triangle, another occupies an outer triangle, the last color occupies the center triangle and the remaining outer triangle: $6\cdot10=60$ ways.
If there are four colors in total:
Choose a color for the center triangle and choose three distinct colors from the five remaining colors to fill the three outer triangles: $6\binom{5}{3}=60$ ways.
Add the total number of ways from each case for the answer: $6+90+180+60=\boxed{336}$
-unhappyfarmer

## Video Solution
https://www.youtube.com/watch?v=dfi23WXZIug&list=PLa8j0YHOYQQIAMDRwkCILRZ5uHnIXcZiw
These problems are copyrighted © by the Mathematical Association of America.