# 2018 AMC 10B Problem 22

## Problem

Real numbers $x$ and $y$ are chosen independently and uniformly at random from the interval $[0,1]$ . Which of the following numbers is closest to the probability that $x,y,$ and $1$ are the side lengths of an obtuse triangle?

$\textbf{(A)} \text{ 0.21} \qquad \textbf{(B)} \text{ 0.25} \qquad \textbf{(C)} \text{ 0.29} \qquad \textbf{(D)} \text{ 0.50} \qquad \textbf{(E)} \text{ 0.79}$

## Solution 1
The Pythagorean Inequality tells us that in an obtuse triangle, $a^{2} + b^{2} < c^{2}$ . The triangle inequality tells us that $a + b > c$ . So, we have two inequalities: \[x^2 + y^2 < 1\] \[x + y > 1\] The first equation is $\frac14$ of a circle with radius $1$ , and the second equation is a line from $(0, 1)$ to $(1, 0)$ . So, the area is $\frac{\pi}{4} - \frac12$ which is approximately $\boxed{\textbf{(C)} ~0.29}$

## Solution 2 (Trig)
Note that the obtuse angle in the triangle has to be opposite the side that is always length $1$ . This is because the largest angle is always opposite the largest side, and if two sides of the triangle were $1$ , the last side would have to be greater than $1$ to make an obtuse triangle. Using this observation, we can set up a law of cosines where the angle is opposite $1$ :
\[1^2=x^2+y^2-2xy\cos(\theta)\]
where $x$ and $y$ are the sides that go from $[0,1]$ and $\theta$ is the angle opposite the side of length $1$ .
By isolating $\cos(\theta)$ , we get:
\[\frac{1-x^2-y^2}{-2xy} = \cos(\theta)\]
For $\theta$ to be obtuse, $\cos(\theta)$ must be negative. Therefore, $\frac{1-x^2-y^2}{-2xy}$ is negative. Since $x$ and $y$ must be positive, $-2xy$ must be negative, so we must make $1-x^2-y^2$ positive. From here, we can set up the inequality \[x^2+y^2<1\] Additionally, to satisfy the definition of a triangle, we need: \[x+y>1\] The solution should be the overlap between the two equations in the first quadrant.
By observing that $x^2+y^2<1$ is the equation for a circle, the amount that is in the first quadrant is $\frac{\pi}{4}$ . The line can also be seen as a chord that goes from $(0, 1)$ to $(1, 0)$ . By cutting off the triangle of area $\frac{1}{2}$ that is not part of the overlap, we get $\frac{\pi}{4} - \frac{1}{2} \approx \boxed{\textbf{(C)} ~0.29}$ .
..why would you do this? for what purpose? its much more complicated and this is the AMC 10! -Orion 2010

## Video Solution & More by MegaMath
https://www.youtube.com/watch?v=d6oFfN5N_70

## Video Solution by OmegaLearn
https://youtu.be/LwtoLiBwO-E?t=316
~ pi_is_3.14

## Video Solution
https://youtu.be/tWkE_c3Fa3I -- Geometric Probability and Inequalities!
https://www.youtube.com/watch?v=GHAMU60rI5c
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .