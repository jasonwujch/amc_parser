# 2010 AMC 10B Problem 19

## Problem

A circle with center $O$ has area $156\pi$ . Triangle $ABC$ is equilateral, $\overline{BC}$ is a chord on the circle, $OA = 4\sqrt{3}$ , and point $O$ is outside $\triangle ABC$ . What is the side length of $\triangle ABC$ ?

$\textbf{(A)}\ 2\sqrt{3} \qquad \textbf{(B)}\ 6 \qquad \textbf{(C)}\ 4\sqrt{3} \qquad \textbf{(D)}\ 12 \qquad \textbf{(E)}\ 18$

## Solution 1
The formula for the area of a circle is $\pi r^2$ so the radius of this circle is $\sqrt{156}.$
Because $OA=4\sqrt{3}=\sqrt{48} < \sqrt{156}, A$ must be in the interior of circle $O.$
Let $s$ be the side length of the triangle, the unknown value, and let $X$ be the point on $BC$ where $OX \perp BC.$ Since $\triangle ABC$ is equilateral, $BX=\frac{s}{2}$ and $AX=\frac{s\sqrt{3}}{2}.$ We are given $AO=4\sqrt{3}.$ Use the Pythagorean Theorem and solve for $s.$
\begin{align*} (\sqrt{156})^2 &= \left(\frac{s}{2}\right)^2 + \left( \frac{s\sqrt{3}}{2} + 4\sqrt{3} \right)^2\\ 156 &= \frac14s^2 + \frac34s^2 + 12s + 48\\ 0 &= s^2 + 12s - 108\\ 0 &= (s-6)(s+18)\\ s &= \boxed{\textbf{(B)}\ 6} \end{align*}

## Solution 2
We can use the same diagram as Solution 1 and label the side length of $\triangle ABC$ as $s$ . Using congruent triangles, namely the two triangles $\triangle BOA$ and $\triangle COA$ , we get that $\angle BAO = \angle CAO \implies \angle BAO = \frac{360^\circ-60^\circ}{2} = 150^\circ$ . From this, we can use the Law of Cosines , to get \[s^2 + (4 \sqrt{3})^2 - 2 \times s \times 4 \sqrt{3} \times - \frac{\sqrt{3}}{2} = (2 \sqrt{39})^2\] Simplifying, we get \[s^2 + 12s + 48 = 156 \implies s^2 + 12s - 108 = 0\] We can factor this to get \[(x-6)(x+18)\] Lengths must be non-negative, so the answer is $\boxed{\textbf{(B)}\ 6}$ ~bryan gao

## Video Solution
https://youtu.be/FQO-0E2zUVI?t=906
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .