# 2012 AMC 12A Problem 12

## Problem

A square region $ABCD$ is externally tangent to the circle with equation $x^2+y^2=1$ at the point $(0,1)$ on the side $CD$ . Vertices $A$ and $B$ are on the circle with equation $x^2+y^2=4$ . What is the side length of this square?

$\textbf{(A)}\ \frac{\sqrt{10}+5}{10}\qquad\textbf{(B)}\ \frac{2\sqrt{5}}{5}\qquad\textbf{(C)}\ \frac{2\sqrt{2}}{3}\qquad\textbf{(D)}\ \frac{2\sqrt{19}-4}{5}\qquad\textbf{(E)}\ \frac{9-\sqrt{17}}{5}$

## Solution 1
The circles have radii of $1$ and $2$ . Draw the triangle shown in the figure above and write expressions in terms of $s$ (length of the side of the square) for the sides of the triangle. Because $AO$ is the radius of the larger circle, which is equal to $2$ , we can write the Pythagorean Theorem.
\begin{align*} \left( \frac{s}{2} \right) ^2 + (s+1)^2 &= 2^2\\ \frac14 s^2 + s^2 + 2s + 1 &= 4\\ \frac54 s^2 +2s - 3 &= 0\\ 5s^2 + 8s - 12 &=0 \end{align*}
Use the quadratic formula.
\[s = \frac{-8+\sqrt{8^2-4(5)(-12)}}{10} = \frac{-8+\sqrt{304}}{10} = \frac{-8+4\sqrt{19}}{10} = \boxed{\textbf{(D)}\ \frac{2\sqrt{19}-4}{5}}\]

## Solution 2
Using the diagram above, we look at the top-right vertex of the square. Let us call this point $(x,y)$ . Then, we that since the square is symmetrical over the y-axis, that the y value is equal to $2x+1$ , since we can multiply the x value(which is half of $s$ ) by two to get $s$ , and we add one since the square lies one unit above the origin. Now, all we must do is find the intersection of the larger circle, $x^2 + y^2 = 4$ , and the line $y=2x+1$ . Substituting the second equation into the first, we get:
$5x^2 +4x -3 = 0$
Using the quadratic formula, we arrive with $x=\frac{-4 \pm 2\sqrt{19}}{10}$ . However, recall that the x value is only one half of the side length. Multiplying this value by $2$ , then, and using only the positive root(since the top right vertex of the square has a positive x value), we get:
$\frac{-4 + 2\sqrt{19}}{5} \Rightarrow \boxed{\textbf{(D)}}$

## Solution 3
Like the previous solutions, we can say that the square is symmetrical with respect to the y-axis.
Point B is $\left(-x, \sqrt{4-x^2}\right)$ and Point A is $\left(x,\sqrt{4-x^2}\right)$ . Now, we see that AB = 2x and BC = $\sqrt{4-x^2}$ -1
Setting those two equal, we get the same equation as the previous solutions: $5x^2 +4x -3 = 0$ and then solve the same way.
-Conantwiz2023
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .