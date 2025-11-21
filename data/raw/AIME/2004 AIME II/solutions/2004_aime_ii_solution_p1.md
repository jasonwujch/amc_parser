# 2004 AIME II Problem 1

## Problem

A chord of a circle is perpendicular to a radius at the midpoint of the radius. The ratio of the area of the larger of the two regions into which the chord divides the circle to the smaller can be expressed in the form $\frac{a\pi+b\sqrt{c}}{d\pi-e\sqrt{f}},$ where $a, b, c, d, e,$ and $f$ are positive integers , $a$ and $e$ are relatively prime , and neither $c$ nor $f$ is divisible by the square of any prime . Find the remainder when the product $abcdef$ is divided by 1000.

## Solution
Let $r$ be the length of the radius of the circle. A right triangle is formed by half of the chord, half of the radius (since the chord bisects it), and the radius. Thus, it is a $30^\circ$ - $60^\circ$ - $90^\circ$ triangle , and the area of two such triangles is $2 \cdot \frac{1}{2} \cdot \frac{r}{2} \cdot \frac{r\sqrt{3}}{2} = \frac{r^2\sqrt{3}}{4}$ . The central angle which contains the entire chord is $60 \cdot 2 = 120$ degrees , so the area of the sector is $\frac{1}{3}r^2\pi$ ; the rest of the area of the circle is then equal to $\frac{2}{3}r^2\pi$ .
The smaller area cut off by the chord is equal to the area of the sector minus the area of the triangle. The larger area is equal to the area of the circle not within the sector and the area of the triangle. Thus, the desired ratio is $\frac{\frac{2}{3}r^2\pi + \frac{r^2\sqrt{3}}{4}}{\frac{1}{3}r^2\pi - \frac{r^2\sqrt{3}}{4}} = \frac{8\pi + 3\sqrt{3}}{4\pi - 3\sqrt{3}}$
Therefore, $abcdef = 2^53^4 = 2592 \Longrightarrow \boxed{592}$ .
These problems are copyrighted © by the Mathematical Association of America.