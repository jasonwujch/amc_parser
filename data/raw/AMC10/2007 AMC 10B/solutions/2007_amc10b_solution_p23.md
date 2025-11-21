# 2007 AMC 10B Problem 23

## Problem

A pyramid with a square base is cut by a plane that is parallel to its base and $2$ units from the base. The surface area of the smaller pyramid that is cut from the top is half the surface area of the original pyramid. What is the altitude of the original pyramid?

$\textbf{(A) } 2 \qquad\textbf{(B) } 2+\sqrt{2} \qquad\textbf{(C) } 1+2\sqrt{2} \qquad\textbf{(D) } 4 \qquad\textbf{(E) } 4+2\sqrt{2}$

## Solution
Since the two pyramids are similar, the ratio of the altitudes is the square root of the ratio of the surface areas.
If $a$ is the altitude of the larger pyramid, then $a-2$ is the altitude of the smaller pyramid.
\[\frac{a}{a-2}=\sqrt{\frac21}=\frac{\sqrt{2}}{1} \longrightarrow a= a\sqrt{2} - 2\sqrt{2} \longrightarrow a\sqrt{2}-a=2\sqrt{2}\] \[a=\frac{2\sqrt{2}}{\sqrt{2}-1} = \frac{4+2\sqrt{2}}{2-1} = \boxed{\textbf{(E) \ } 4+2\sqrt{2}}.\]

## Solution 2 (Playing with the answers)
Instead of actually solving this problem, we can play with the answers. The ratios of the altitudes squared is the ratio of the surface areas, so the answer choice has to be larger than $4$ because an original height of $4$ would give the ratio $1:4$ for the surface area and only choice $E$ is larger than $4$ , so the answer is $E$ .

## Solution 3 (Note)
Like in Solution 1, we used the fact that the ratio of surface area is the ratio of side lengths squared . However, with this, we can go two ways.
1. (Solution 1) The ratio of the surface area of the large pyramid to the surface area of the small pyramid is $\frac 21$ , so the ratio of their altitudes is $\sqrt{\frac21}=\frac{\sqrt{2}}{1}=\sqrt2$ .
2. (Another way) The ratio of the surface area of the small pyramid to the surface area of the large pyramid is $\frac 12$ , so the ratio of their altitudes is $\sqrt{\frac12}=\frac{1}{\sqrt2}=\frac{\sqrt2}{2}$ .
Then, we can set up variables based on these ratios and solve for the variable, hence getting the altitude of the large triangle, or $\boxed{\textbf{(E)}~4+2\sqrt 2}.$
~BakedPotato66

## Solution 4
The ratio of the surface area of the smaller pyramid to the surface area of the larger pyramid is the same as the ratio of the area of the square face of the smaller pyramid to that of the larger pyramid. We take the cross-section through the apex of the larger pyramid, revealing a triangle with a line segment parallel to its base passing through it. Suppose the triangle has height $h$ (the original pyramid has altitude $h$ ) and base $s$ (the original pyramid's square base has side length $s$ ). Suppose further that the length of the line segment going through the triangle is $s_2$ (the smaller pyramid's square base has side length $s_2$ ). By similar triangles, we have the ratio $\frac{s}{h} = \frac{s_2}{h-2} \implies s_2 = \frac{s(h-2)}{h}$ . Then we have $s_2^2 = \frac{1}{2}s^2 \implies (\frac{s(h-2)}{h})^2 = \frac{1}{2}s^2 \implies (h-2)^2 = \frac{1}{2}h^2$ . Solving this equation, we get the solutions $h = 4 + 2\sqrt{2}$ and $h = 4 - 2\sqrt{2}$ . However, with the second solution, the smaller pyramid would have a height that is two less than this, which would result in a negative number ( $2 - 2\sqrt{2}$ ). Thus, we discard the second solution, and our only solution is $\boxed{\textbf{(E)}~4 + 2\sqrt{2}}$ .
~ cxsmi
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .