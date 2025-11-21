# 2024 AMC 10B Problem 19

## Problem

In the following table, each question mark is to be replaced by "Possible" or "Not Possible" to indicate whether a nonvertical line with the given slope can contain the given number of lattice points (points both of whose coordinates are integers). How many of the 12 entries will be "Possible"?

$\textbf{(A) } 4 \qquad\textbf{(B) } 5 \qquad\textbf{(C) } 6 \qquad\textbf{(D) } 7 \qquad\textbf{(E) } 9$

### Diagram

~Cattycute

## Solution 1
Let's look at zero slope first. All lines of such form will be expressed in the form $y=k$ , where $k$ is some real number. If $k$ is an integer, the line passes through infinitely many lattice points. One such example is $y=1$ . If $k$ is not an integer, the line passes through $0$ lattice points. One such example is $y=1.1$ . So we have $2$ cases.
Let's now look at the second case. The line has slope $\frac{p}{q}$ , where $p$ and $q$ are relatively prime integers. The line has the form $y = \frac{p}{q}x + m$ . If the line passes through lattice point $(a,b)$ , then the line must also pass through the lattice point $(a+kq, b+kp)$ , where $a,b,k$ are all integers. Therefore, the line can pass through infinitely many lattice points but it cannot pass through exactly $1$ or $2$ . The line can pass through $0$ lattice points, such as $y=x+0.5$ . This contributes $2$ more cases.
If the line has an irrational slope, it can never pass through more than $2$ lattice points. We prove this using contradiction. Let's say the line passes through lattice points $(a,b)$ and $(c,d)$ . Then the line has slope $\frac{d-b}{c-a}$ , which is rational. However, the slope of the line is irrational. Therefore, the line can pass through at most $1$ lattice point. One example of this is $y=\sqrt{2}x$ . This line contributes $2$ final cases.
Our answer is therefore $\boxed{6}$ .
This shows examples of the six lines that are valid. - https://www.desmos.com/calculator/ypt7esdv2g
~lprado

## Solution 2
For a 0 slope: It can have 0 points (e.g. $y=1.5$ ), but it can also have infinite (e.g. y=1), which checks the two or more box.
For a nonzero slope: It can have 0 lattice points (e.g. $y=\frac23 x + \frac12$ ), or infinite (eg $y=2x$ ).
For an irrational slope: It can have 0 (e.g. $y=\sqrt3 x+\frac12$ ) or exactly 1 (e.g. $y=\sqrt3 x,$ which has an intersection at 0,0)
Hence, there are a total of 6 points.
~mathboy282, Lightning

## Solution 3
Zero Slope
A line of zero slope can intersect no lattice points (If the y-intercept isn't an integer)
It cannot intersect only one lattice point, same goes for two lattice points because if it intersects one, it has to intersect all lattice points with that y value.
It can intersect more than two lattice points (infinite)
Rational Slope $\neq0$
It can intersect no lattice points ( $y=x+0.5$ )
It cannot intersect only one or two lattice points (because then it would intersect another one once the slope "repeats" again)
It can intersect more than two lattice points (infinite)
Irrational Slope
It can intersect no lattice points (y-intercept isn't an integer)
It can intersect one lattice point (y-intercept is an integer)
It cannot intersect two or more lattice points no matter what.
Therefore, the answer is $\boxed{\text{(C) }6}$ . ~Tacos_are_yummy_1

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/c6nhclB5V1w?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=24EZaeAThuE
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .