# 2017 AIME I Problem 6

## Problem

A circle is circumscribed around an isosceles triangle whose two congruent angles have degree measure $x$ . Two points are chosen independently and uniformly at random on the circle, and a chord is drawn between them. The probability that the chord intersects the triangle is $\frac{14}{25}$ . Find the difference between the largest and smallest possible values of $x$ .

## Solution
The probability that the chord doesn't intersect the triangle is $\frac{11}{25}$ . The only way this can happen is if the two points are chosen on the same arc between two of the triangle vertices. The probability that a point is chosen on one of the arcs opposite one of the base angles is $\frac{2x}{360}=\frac{x}{180}$ (this comes from the Central Angle Theorem, which states that the central angle from two points on a circle is always twice the inscribed angle from those two points), and the probability that a point is chosen on the arc between the two base angles is $\frac{180-2x}{180}$ . Therefore, we can write \[2\left(\frac{x}{180}\right)^2+\left(\frac{180-2x}{180}\right)^2=\frac{11}{25}\] This simplifies to \[x^2-120x+3024=0\]
(Note that the simplification is quite tedious)
Which factors as \[(x-84)(x-36)=0\] So $x=84, 36$ . The difference between these is $\boxed{048}$ .
Note:
We actually do not need to spend time factoring $x^2 - 120x + 3024$ . Since the problem asks for $|x_1 - x_2|$ , where $x_1$ and $x_2$ are the roots of the quadratic, we can utilize Vieta's by noting that $(x_1 - x_2) ^ 2 = (x_1 + x_2) ^ 2 - 4x_1x_2$ . Vieta's gives us $x_1 + x_2 = 120,$ and $x_1x_2 = 3024.$ Plugging this into the above equation and simplifying gives us $(x_1 - x_2) ^ 2 = 2304,$ or $|x_1 - x_2| = 48$ .
Our answer is then $\boxed{048}$ .
Another note:
Letting $y = x/180$ , the first equation turns into $2y^2 + (1-2y)^2 = 11/25$ , heavily simplifying the otherwise messy simplification, and you can use the aforementioned note to find $|y_1 - y_2| = 4/15$ . Using $x = 180y$ , $|x_1 - x_2| = 180|y_1 - y_2|$ , so the answer is $180(4/15) = \boxed{048}$

## Solution 2 (Not Complementary Counting method)
Because we know that we have an isosceles triangle with angles of $x$ (and we know that x is an inscribed angle), that means that the arc that is intercepted by this angle is $2x$ . We form this same conclusion for the other angle $x$ , and $180-2x$ . Therefore we get $3$ arcs, namely, $2x$ , $2x$ , and $360-4x$ . To have the chords intersect the triangle, we need the two points selected (to make a chord) to be on completely different arcs. An important idea to understand is that order matters in this case, so we have the equation $2$ * $\frac{2x}{360}$ * $\frac{2x}{360}$ + $2$ * $2$ * $\frac{2x}{360}$ * $\frac{360-4x}{360}$ = $\frac{14}{25}$ which using trivial algebra gives you $x^2-120x+3024$ and factoring gives you $(x-84)(x-36)$ and so your answer is $\boxed{048}$ . ~jske25

## Solution 3 ( 3 System Algebra )
After constructing the circumscribed circle, realize that the only time when the chord does not intersect the circle is when our $2$ points fall on only one arc formed by the sides of the triangle. Thus, lets call our isosceles triangle $ABC$ , where $AB=BC$ . Thus, the arcs formed by $BC$ and $AB$ can be called $a$ , and the arc formed by $AC$ is called $b$ . So, we can create the following system
\[2a+b=1\] \[2a^2+4ab=\frac{14}{25}\] \[2a^2+b^2=\frac{11}{25}\]
Notice we are denoting $a$ and $b$ as our probabilities, which we will be converting to degrees later. The 2 remaining systems can be calculated by using our rule about intersecting arcs and chords. So, after some hairy algebra we get:
\[a=\frac{1}{5}\] if \[b=\frac{3}{5}\] \[a=\frac{7}{15}\] if \[b=\frac{1}{15}\]
From here we find the absolute difference by doing $\frac{7}{15}-\frac{1}{5} = \frac{4}{15}$ . Converting to degrees, since the angles of a triangle add up to $180^o$ , we find that $\frac{4}{15} \cdot 180 =\boxed{048}$ , which is our answer.
-Geometry285

## Video Solution
https://youtu.be/Mk-MCeVjSGc?t=690 ~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .