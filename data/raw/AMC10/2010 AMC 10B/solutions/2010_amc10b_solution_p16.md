# 2010 AMC 10B Problem 16

## Problem

A square of side length $1$ and a circle of radius $\dfrac{\sqrt{3}}{3}$ share the same center. What is the area inside the circle, but outside the square?

$\textbf{(A)}\ \dfrac{\pi}{3}-1 \qquad \textbf{(B)}\ \dfrac{2\pi}{9}-\dfrac{\sqrt{3}}{3} \qquad \textbf{(C)}\ \dfrac{\pi}{18} \qquad \textbf{(D)}\ \dfrac{1}{4} \qquad \textbf{(E)}\ \dfrac{2\pi}{9}$

## Solution 1
The radius of the circle is $\frac{\sqrt{3}}{3} = \sqrt{\frac{1}{3}}$ . Half the diagonal of the square is $\frac{\sqrt{1^2+1^2}}{2} = \frac{\sqrt{2}}{2} = \sqrt{\frac12}$ . We can see that the circle passes outside the square, but the square is NOT completely contained in the circle. Therefore the picture will look something like this:
Then we proceed to find: 4 $\cdot$ (area of sector marked off by the two radii - area of the triangle with sides on the square and the two radii).
First we realize that the radius perpendicular to the side of the square between the two radii marking off the sector splits $AB$ in half. Let this half-length be $a$ . Also note that $OX=\frac12$ because it is half the side length of the square. Because this is a right triangle, we can use the Pythagorean Theorem to solve for $a.$
\[a^2+\left( \frac12 \right) ^2 = \left( \frac{\sqrt{3}}{3} \right) ^2\]
Solving, $a= \frac{\sqrt{3}}{6}$ and $2a=\frac{\sqrt{3}}{3}$ . Since $AB=AO=BO$ , $\triangle AOB$ is an equilateral triangle and the central angle is $60^{\circ}$ . Therefore the sector has an area $\pi \left( \frac{\sqrt{3}}{3} \right) ^2 \left( \frac{60}{360} \right) = \frac{\pi}{18}$ .
Now we turn to the triangle. Since it is equilateral, we can use the formula for the area of an equilateral triangle which is
\[\frac{s^2\sqrt{3}}{4} = \frac{\frac13 \sqrt{3}}{4} = \frac{\sqrt{3}}{12}\]
Putting it together, we get the answer to be $4\cdot\left( \frac{\pi}{18}-\frac{\sqrt{3}}{12} \right)= \boxed{\textbf{(B)}\ \frac{2\pi}{9}-\frac{\sqrt{3}}{3}}$

## Solution 2 (Answer Choices)
At once, we can eliminate $(C)$ , $(D)$ , and $(E)$ because the answer should be $a \times \pi + b$ , where $a$ and $b$ are real numbers (not necessarily rational) not equal to $0$ . Now, all that's left is $\frac{\pi}{3}-1$ and $\frac{2 \pi}{9} - \frac{\sqrt{3}}{3}$ . $\frac{\pi}{3}-1$ is simply the area of the circle minus the square, which is definitely wrong, so the answer is $\boxed{\textbf{(B)} \frac{2 \pi}{9} - \frac{\sqrt{3}}{3}}$

## Video Solution
https://youtu.be/FQO-0E2zUVI
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .