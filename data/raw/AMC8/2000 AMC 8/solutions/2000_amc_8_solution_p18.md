# 2000 AMC 8 Problem 18

## Problem

Consider these two geoboard quadrilaterals. Which of the following statements is true?

[asy] for (int a = 0; a < 5; ++a) { for (int b = 0; b < 5; ++b) { dot((a,b)); } } draw((0,3)--(0,4)--(1,3)--(1,2)--cycle); draw((2,1)--(4,2)--(3,1)--(3,0)--cycle); label("I",(0.4,3),E); label("II",(2.9,1),W);[/asy]

$\text{(A)}\ \text{The area of quadrilateral I is more than the area of quadrilateral II.}$

$\text{(B)}\ \text{The area of quadrilateral I is less than the area of quadrilateral II.}$

$\text{(C)}\ \text{The quadrilaterals have the same area and the same perimeter.}$

$\text{(D)}\ \text{The quadrilaterals have the same area, but the perimeter of I is more than the perimeter of II.}$

$\text{(E)}\ \text{The quadrilaterals have the same area, but the perimeter of I is less than the perimeter of II.}$

## Solution 1
First consider the area of the two figures. Assume that the pegs are $1$ unit apart. Divide region I into two triangles by drawing a horizontal line on the second row from the top. Shifting the bottom triangle up one unit will create a square, and this square has the same area as region I. Thus, region I has an area of $1$ square unit.
Draw a horizontal line on figure II on the fourth row from the top to divide the figure into two triangles. Temporarily move the top of the higher triangle one peg to the left. This will preserve the area of the triangle, as you are keeping both the height and the base of the triangle equal. Now you have two congruent triangles that are half of the area of a unit square. Thus, region II also has an area of $1$ square unit, and the areas are equal.
To compare the perimeters, note that region I has two different side lengths: two sides are $1$ unit apart, and the other two sides are $\sqrt{2}$ apart, as they are the diagonal of a unit square. The total perimeter is $2 + 2\sqrt{2}$ .
Note that region II has three different side lengths. One side is a unit length, while two sides are $\sqrt{2}$ . For the perimeters to be equal, the last side must be of unit length. But the last side in region II is clearly longer than $1$ unit, so we can say that the perimeter of region II is greater than the perimeter of region I without calculating it.
Thus, the correct answer is $\boxed{E}$ .
(The perimeter of region II is $1 + 2\sqrt{2} + \sqrt{5}$ , since the last side is the diagonal of a 2 by 1 rectangle, and can be found with the pythagorean theorem as $\sqrt{2^2 + 1^2} = \sqrt{5}$ . This does not need to be found for this problem, as you can do a one-to-one correspondence with three of the four sides of the figure as outlined, and just compare the last remaining side of each figure.)

## Solution 2
Using the Pick’s Theorem, The area of both figures is 1. This rules out answer choices A and B. When using the Pythagorean Theorem, we find that the perimeter of I is 2 + 2( $\sqrt{2}$ ) and the perimeter of II is 1 + 2( $\sqrt{2}$ ) + $\sqrt{5}$ . Since $\sqrt{5}$ > 1, the perimeter of II is greater, therefore the correct answer is $\boxed{E}$ .

## Video Solution
https://www.youtube.com/watch?v=hdwmCc4dai0 ~David
### See Also