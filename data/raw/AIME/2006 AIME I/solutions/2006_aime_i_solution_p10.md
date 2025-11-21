# 2006 AIME I Problem 10

## Problem

Eight circles of diameter 1 are packed in the first quadrant of the coordinate plane as shown. Let region $\mathcal{R}$ be the union of the eight circular regions. Line $l,$ with slope 3, divides $\mathcal{R}$ into two regions of equal area. Line $l$ 's equation can be expressed in the form $ax=by+c,$ where $a, b,$ and $c$ are positive integers whose greatest common divisor is 1. Find $a^2+b^2+c^2.$ [asy] size(150);defaultpen(linewidth(0.7)); draw((6.5,0)--origin--(0,6.5), Arrows(5)); int[] array={3,3,2}; int i,j; for(i=0; i<3; i=i+1) { for(j=0; j<array[i]; j=j+1) { draw(Circle((1+2*i,1+2*j),1)); }} label("x", (7,0)); label("y", (0,7));[/asy]

## Solutions
[asy] size(150);defaultpen(linewidth(0.7)); draw((6.5,0)--origin--(0,6.5), Arrows(5)); int[] array={3,3,2}; int i,j; for(i=0; i<3; i=i+1) { for(j=0; j<array[i]; j=j+1) { draw(Circle((1+2*i,1+2*j),1)); }} label("x", (7,0)); label("y", (0,7)); draw((5/3,0)--(23/6,6.5),blue);[/asy]

## Solution 1
The line passing through the tangency point of the bottom left circle and the one to its right and through the tangency of the top circle in the middle column and the one beneath it is the line we are looking for: a line passing through the tangency of two circles cuts congruent areas, so our line cuts through the four aforementioned circles splitting into congruent areas, and there are an additional two circles on each side. The line passes through $\left(1,\frac 12\right)$ and $\left(\frac 32,2\right)$ , which can be easily solved to be $6x = 2y + 5$ . Thus, $a^2 + b^2 + c^2 = \boxed{065}$ .

## Solution 2
Assume that if unit squares are drawn circumscribing the circles, then the line will divide the area of the concave hexagonal region of the squares equally (as of yet, there is no substantiation that such would work, and definitely will not work in general). Denote the intersection of the line and the x-axis as $(x, 0)$ .
The line divides the region into 2 sections. The left piece is a trapezoid , with its area $\frac{1}{2}((x) + (x+1))(3) = 3x + \frac{3}{2}$ . The right piece is the addition of a trapezoid and a rectangle , and the areas are $\frac{1}{2}((1-x) + (2-x))(3)$ and $2 \cdot 1 = 2$ , totaling $\frac{13}{2} - 3x$ . Since we want the two regions to be equal, we find that $3x + \frac 32 = \frac {13}2 - 3x$ , so $x = \frac{5}{6}$ .
We have that $\left(\frac 56, 0\right)$ is a point on the line of slope 3, so $y - 0 = 3\left(x - \frac 56\right) \Longrightarrow 6x = 2y + 5$ . Our answer is $2^2 + 5^2 + 6^2 = 65$ .
We now assess the validity of our starting assumption. We can do that by seeing that our answer passes through the tangency of the two circles, cutting congruent areas, a result explored in solution 1.

## Solution 3
This problem looks daunting at a first glance, but we can make geometric inequality inferences by drawing lines that simplify the problem by removing sections of the total area. To begin, we can eliminate the possibility of the line intersecting the circle on the top left (call it circle A), or the circle on the bottom right (call it circle B). This is can be seen visually by drawing a line with slope 3 that is tangent to either of these circles. The area is clearly larger on one side; this can be proven by counting full circles. We can go on with the same mindset and eliminate the circle below circle A and the circle above circle B. By removing pairs of circles and proving the line will never intersect with them, we can safely work with whatever is remaining. By now you should have 4 circles making an L shape (waluigi style). Now the two biggest contenders for this method are the two circles on the bottom row. Using the same strategy, we can see that a line that goes through the tangent point of these two circles also goes through the tangent point of the other two circles. This clearly will cut the 4 circles into two regions of equal area. Using super advanced linear algebra we get: $6x = 2y + 5$ . The answer is then $6^2 + 2^2 + 5^2 = \boxed{065}$ . This solution is an alternate explanation to solution 1.
-jackshi2006
These problems are copyrighted © by the Mathematical Association of America.