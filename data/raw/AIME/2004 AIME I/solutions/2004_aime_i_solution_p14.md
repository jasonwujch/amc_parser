# 2004 AIME I Problem 14

## Problem

A unicorn is tethered by a $20$ -foot silver rope to the base of a magician's cylindrical tower whose radius is $8$ feet. The rope is attached to the tower at ground level and to the unicorn at a height of $4$ feet. The unicorn has pulled the rope taut, the end of the rope is $4$ feet from the nearest point on the tower, and the length of the rope that is touching the tower is $\frac{a-\sqrt{b}}c$ feet, where $a, b,$ and $c$ are positive integers , and $c$ is prime. Find $a+b+c.$

## Solution
Looking from an overhead view, call the center of the circle $O$ , the tether point to the unicorn $A$ and the last point where the rope touches the tower $B$ . $\triangle OAB$ is a right triangle because $OB$ is a radius and $BA$ is a tangent line at point $B$ . We use the Pythagorean Theorem to find the horizontal component of $AB$ has length $4\sqrt{5}$ .
Now look at a side view and "unroll" the cylinder to be a flat surface. Let $C$ be the bottom tether of the rope, let $D$ be the point on the ground below $A$ , and let $E$ be the point directly below $B$ . Triangles $\triangle CDA$ and $\triangle CEB$ are similar right triangles . By the Pythagorean Theorem $CD=8\cdot\sqrt{6}$ .
Let $x$ be the length of $CB$ . \[\frac{CA}{CD}=\frac{CB}{CE}\implies \frac{20}{8\sqrt{6}}=\frac{x}{8\sqrt{6}-4\sqrt{5}}\implies x=\frac{60-\sqrt{750}}{3}\]
Therefore $a=60, b=750, c=3, a+b+c=\boxed{813}$ .

## Solution 2
Note that by Power of a Point, the point the unicorn is at has power $4 \cdot 20 = 80$ which implies that the tangent from that point to the tower is of length $\sqrt{80}=4\sqrt{5},$ however this is length of the rope projected into 2-D. If we let $\theta$ be the angle between the horizontal and the rope, we have that $\cos\theta=\frac{1}{5}$ which implies that $\sin\theta=\frac{2\sqrt{6}}{5}.$ Note that the portion of rope not on the tower is $4\sqrt{5} \cdot \frac{5}{2\sqrt{6}}= \frac{5\sqrt{30}}{3},$ the requested length of rope is $20-\frac{5\sqrt{30}}{3}=\frac{60-\sqrt{750}}{3}$ thus the requested sum is $\boxed{813}.$
~ Dhillonr25
These problems are copyrighted © by the Mathematical Association of America.