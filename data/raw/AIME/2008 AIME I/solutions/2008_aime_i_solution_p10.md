# 2008 AIME I Problem 10

## Problem

Let $ABCD$ be an isosceles trapezoid with $\overline{AD}||\overline{BC}$ whose angle at the longer base $\overline{AD}$ is $\dfrac{\pi}{3}$ . The diagonals have length $10\sqrt {21}$ , and point $E$ is at distances $10\sqrt {7}$ and $30\sqrt {7}$ from vertices $A$ and $D$ , respectively. Let $F$ be the foot of the altitude from $C$ to $\overline{AD}$ . The distance $EF$ can be expressed in the form $m\sqrt {n}$ , where $m$ and $n$ are positive integers and $n$ is not divisible by the square of any prime. Find $m + n$ .

## Solution 1
Key observation. $AD = 20\sqrt{7}$ .
Proof 1. By the triangle inequality , we can immediately see that $AD \geq 20\sqrt{7}$ . However, notice that $10\sqrt{21} = 20\sqrt{7}\cdot\sin\frac{\pi}{3}$ , so by the law of sines, when $AD = 20\sqrt{7}$ , $\angle ACD$ is right and the circle centered at $A$ with radius $10\sqrt{21}$ , which we will call $\omega$ , is tangent to $\overline{CD}$ . Thus, if $AD$ were increased, $\overline{CD}$ would have to be moved even farther outwards from $A$ to maintain the angle of $\frac{\pi}{3}$ and $\omega$ could not touch it, a contradiction.
Proof 2. Again, use the triangle inequality to obtain $AD \geq 20\sqrt{7}$ . Let $x = AD$ and $y = CD$ . By the law of cosines on $\triangle ADC$ , $2100 = x^2+y^2-xy \iff y^2-xy+(x^2-2100) = 0$ . Viewing this as a quadratic in $y$ , the discriminant $\Delta$ must satisfy $\Delta = x^2-4(x^2-2100) = 8400-3x^2 \geq 0 \iff x \leq 20\sqrt{7}$ . Combining these two inequalities yields the desired conclusion.
This observation tells us that $E$ , $A$ , and $D$ are collinear, in that order.
Then, $\triangle ADC$ and $\triangle ACF$ are $30-60-90$ triangles. Hence $AF = 15\sqrt {7}$ , and
Finally, the answer is $25+7=\boxed{032}$ .

## Solution 2
Extend $\overline {AB}$ through $B$ , to meet $\overline {DC}$ (extended through $C$ ) at $G$ . $ADG$ is an equilateral triangle because of the angle conditions on the base.
If $\overline {GC} = x$ then $\overline {CD} = 40\sqrt{7}-x$ , because $\overline{AD}$ and therefore $\overline{GD}$ $= 40\sqrt{7}$ .
By simple angle chasing, $CFD$ is a 30-60-90 triangle and thus $\overline{FD} = \frac{40\sqrt{7}-x}{2}$ , and $\overline{CF} = \frac{40\sqrt{21} - \sqrt{3}x}{2}$
Similarly $CAF$ is a 30-60-90 triangle and thus $\overline{CF} = \frac{10\sqrt{21}}{2} = 5\sqrt{21}$ .
Equating and solving for $x$ , $x = 30\sqrt{7}$ and thus $\overline{FD} = \frac{40\sqrt{7}-x}{2} = 5\sqrt{7}$ .
$\overline{ED}-\overline{FD} = \overline{EF}$
$30\sqrt{7} - 5\sqrt{7} = 25\sqrt{7}$ and $25 + 7 = \boxed{032}$
How do you assume $\overline{AD}$ $= 40\sqrt{7}$ .
~polya_mouse.
(how is this a P10 what)

## Video Solution
2008 AIME I #10
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.