# 2010 AIME II Problem 2

## Problem

A point $P$ is chosen at random in the interior of a unit square $S$ . Let $d(P)$ denote the distance from $P$ to the closest side of $S$ . The probability that $\frac{1}{5}\le d(P)\le\frac{1}{3}$ is equal to $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
Any point outside the square with side length $\frac{1}{3}$ that has the same center and orientation as the unit square and inside the square with side length $\frac{3}{5}$ that has the same center and orientation as the unit square has $\frac{1}{5}\le d(P)\le\frac{1}{3}$ .
Since the area of the unit square is $1$ , the probability of a point $P$ with $\frac{1}{5}\le d(P)\le\frac{1}{3}$ is the area of the shaded region, which is the difference of the area of two squares.
$\left(\frac{3}{5}\right)^2-\left(\frac{1}{3}\right)^2=\frac{9}{25}-\frac{1}{9}=\frac{56}{225}$
Thus, the answer is $56 + 225 = \boxed{281}.$

## Solution 2
First, let's figure out $d(P) \geq \frac{1}{3}$ which is \[\left(\frac{3}{5}\right)^2=\frac{9}{25}.\] Then, $d(P) \geq \frac{1}{5}$ is a square inside $d(P) \geq \frac{1}{3}$ , so \[\left(\frac{1}{3}\right)^2=\frac{1}{9}.\] Therefore, the probability that $\frac{1}{5}\le d(P)\le\frac{1}{3}$ is \[\frac{9}{25}-\frac{1}{9}=\frac{56}{225}\] So, the answer is $56+225=\boxed{281}$

## Solution 3
First, lets assume that point $P$ is closest to a side $S$ of the square. If it is $\frac{1}{5}$ far from $S$ , then it should be at least $\frac{1}{5}$ from both the adjacent sides of $S$ in the square. This leaves a segment of $1 - 2 \cdot \frac{1}{5} = \frac{3}{5}$ . If the distance from $P$ to $S$ is $\frac{1}{3}$ , then notice the length of the side-ways segment for $P$ is $1 - 2 \cdot \frac{1}{3} = \frac{1}{3}$ . Notice that as the distance from $P$ to $S$ increases, the possible points for the side-ways decreases. This produces a trapezoid with parallel sides $\frac{3}{5}$ and $\frac{1}{3}$ with height $\frac{1}{3} - \frac{1}{5} = \frac{2}{15}$ . This trapezoid has area (or probability for one side) $\frac{1}{2} \cdot \left(\frac{1}{3}+\frac{3}{5}\right)\cdot \frac{2}{15} = \frac{14}{225}$ . Since the square has $4$ sides, we multiply by $4$ . Hence, the probability is $\frac{56}{225}$ . The answer is $\boxed{281}$ . ~Saucepan_man02
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .