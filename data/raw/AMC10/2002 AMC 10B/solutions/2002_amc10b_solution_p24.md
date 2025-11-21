# 2002 AMC 10B Problem 24

## Problem

Riders on a Ferris wheel travel in a circle in a vertical plane. A particular wheel has radius $20$ feet and revolves at the constant rate of one revolution per minute. How many seconds does it take a rider to travel from the bottom of the wheel to a point $10$ vertical feet above the bottom?

$\mathrm{(A) \ } 5\qquad \mathrm{(B) \ } 6\qquad \mathrm{(C) \ } 7.5\qquad \mathrm{(D) \ } 10\qquad \mathrm{(E) \ } 15$

## Video Solution(Quick, Easy to Comprehend)
https://www.youtube.com/watch?v=H7K81Z3hvfo
~MathKatana

## Solution 1
We can let this circle represent the ferris wheel with center $O,$ and $C$ represent the desired point $10$ feet above the bottom. Draw a diagram like the one above. We find out $\triangle OBC$ is a $30-60-90$ triangle. That means $\angle BOC = 60^\circ$ and the ferris wheel has made $\frac{60}{360} = \frac{1}{6}$ of a revolution. Therefore, the time it takes to travel that much of a distance is $\frac{1}{6}\text{th}$ of a minute, or $10$ seconds. The answer is $\boxed{\mathrm{(D) \ } 10}$ . Alternatively, we could also say that $\triangle ABC$ is congruent to $\triangle OBC$ by SAS, so $AC$ is 20, and $\triangle AOC$ is equilateral, and $\angle BOC = 60^\circ$

## Solution 2 (trig)
The path that the rider takes along the Ferris wheel can be represented by a sinusoidal graph, where $x$ represents the time in seconds. Since $x=0$ is at the crest of the graph and not at the midline, we will use a cosine graph. Therefore, we will use the form: \[f(x) = A\cos(Bx - C) + D.\]
The graph starts at the lowest point at $0$ feet, then goes up to reach the highest point at $40$ feet, then comes back down. Therefore, the amplitude is $20$ (and negative since it starts at the bottom, not the top), and the vertical shift is $20$ . There is no horizontal shift since the lowest point is at $x=0$ . It takes $60$ seconds to make one full revolution (the period), so $B = \frac{2\pi}{60} = \frac{\pi}{30}.$ Now we have all the parts we need for the equation of our graph, and we can set it equal to the height we want, $10.$
\[10 = -20\cos\left(\frac{\pi}{30}x\right) + 20.\]
We get to $\frac{1}{2} = \cos\left(\frac{\pi}{30}x\right)$ and remember that the problem is looking for the first instance of $f(x) = 10$ , so $\frac{\pi}{30}x = \frac{\pi}{3}.$ Solving, we get that $x = \boxed{\mathrm{(D) \ } 10}$ .
~jp06132

## Video Solution
https://www.youtube.com/watch?v=MRZJ4jBTZZ0 ~David
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .