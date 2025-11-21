# 2009 AMC 10A Problem 21

## Problem

Many Gothic cathedrals have windows with portions containing a ring of congruent circles that are circumscribed by a larger circle, In the figure shown, the number of smaller circles is four. What is the ratio of the sum of the areas of the four smaller circles to the area of the larger circle?

[asy] unitsize(6mm); defaultpen(linewidth(.8pt)); draw(Circle((0,0),1+sqrt(2))); draw(Circle((sqrt(2),0),1)); draw(Circle((0,sqrt(2)),1)); draw(Circle((-sqrt(2),0),1)); draw(Circle((0,-sqrt(2)),1)); [/asy]

$\mathrm{(A)}\ 3-2\sqrt2 \qquad \mathrm{(B)}\ 2-\sqrt2 \qquad \mathrm{(C)}\ 4(3-2\sqrt2) \qquad \mathrm{(D)}\ \frac12(3-\sqrt2) \qquad \mathrm{(E)}\ 2\sqrt2-2$

## Solution
Draw some of the radii of the small circles as in the picture below.
[asy] unitsize(12mm); defaultpen(linewidth(.8pt)); draw(Circle((0,0),1+sqrt(2))); draw(Circle((sqrt(2),0),1)); draw(Circle((0,sqrt(2)),1)); draw(Circle((-sqrt(2),0),1)); draw(Circle((0,-sqrt(2)),1)); draw( (sqrt(2),0) -- (0,sqrt(2)) -- (-sqrt(2),0) -- (0,-sqrt(2)) -- cycle ); draw( (0,sqrt(2)) -- (0,1+sqrt(2)) ); draw( (0,-sqrt(2)) -- (0,-1-sqrt(2)) ); draw( (0,sqrt(2)) -- (0,-sqrt(2)), dashed ); [/asy]
Out of symmetry, the quadrilateral in the center must be a square. Its side is $2r$ , and therefore its diagonal is $2r\sqrt{2}$ . We can now compute the length of the vertical diameter of the large circle as $2r + 2r\sqrt{2}$ . Hence $2R=2r + 2r\sqrt{2}$ , and thus $R=r+r\sqrt{2}=r(1+\sqrt{2})$ .
Then the area of the large circle is $L = \pi R^2 = \pi r^2 (1+\sqrt 2)^2 = \pi r^2 (3+2\sqrt 2)$ . The area of four small circles is $S = 4\pi r^2$ . Hence their ratio is:
\begin{align*} \frac SL & = \frac{4\pi r^2}{\pi r^2 (3+2\sqrt 2)} \\ & = \frac 4{3+2\sqrt 2} \\ & = \frac 4{3+2\sqrt 2} \cdot \frac{3-2\sqrt 2}{3 - 2\sqrt 2} \\ & = \frac{4(3 - 2\sqrt 2)}{3^2 - (2\sqrt 2)^2} \\ & = \frac{4(3 - 2\sqrt 2)}1 \\ & = \boxed{4(3 - 2\sqrt 2)} \end{align*}

## Solution 2
Draw the center of the large circle, and connect it with two adjacent centers of the smaller circles. Draw the line between the centers. Then, let the line connecting the center of the smaller circle to the center of the larger circle be $x.$
By the Pythagorean Theorem, we have that \[x^2 + x^2 = (1+1)^2\]
Simplifying, we have \begin{align*} x &= \sqrt{\frac{(1+1)^2}{2}} \\ &= \sqrt{\frac{4}{2}} \\ &= \sqrt{2} \end{align*}
Thus, the radius is \[1 + x = 1 + \sqrt{2}\]
The answer we desire is \[\frac{4 \cdot \left(\pi \cdot 1^2 \right)}{\pi \cdot (1+\sqrt{2})^2}\]
Simplifying, we have that \begin{align*} \frac{4 \cdot \left(\pi \cdot 1^2 \right)}{\pi \cdot (1+\sqrt{2})^2} &= \frac{4 \cdot \pi}{\pi \cdot (1 + \sqrt{2})^2} \\ &= \frac{\pi \cdot 4}{\pi \cdot (1+\sqrt{2})^2} \\ &= \frac{4}{(1+\sqrt{2})^2} \\ &= \frac{4}{1^2 + 2 \cdot 1 \cdot \sqrt{2} + (\sqrt{2})^2} \\ &= \frac{4}{1 + 2 \sqrt{2} + 2} \\ &= \frac{4}{3 + 2 \sqrt{2}} \\ &= \frac{4 (3 - 2\sqrt{2})}{(3 + 2 \sqrt{2})(3 - 2\sqrt{2})} \\ &= \frac{4 (3 - 2\sqrt{2})}{3^2 - (2\sqrt{2})^2} \\ &= \frac{4 (3 - 2\sqrt{2})}{9 - 8} \\ &= \frac{4 (3 - 2\sqrt{2})}{1} \\ &= \boxed{\textbf{(C) } 4 (3 - 2\sqrt{2})} \end{align*}
~mathboy282
### See Also