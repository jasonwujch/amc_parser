# 2009 AMC 10B Problem 10

## Problem

A flagpole is originally $5$ meters tall. A hurricane snaps the flagpole at a point $x$ meters above the ground so that the upper part, still attached to the stump, touches the ground $1$ meter away from the base. What is $x$ ?

$\text{(A) } 2.0 \qquad \text{(B) } 2.1 \qquad \text{(C) } 2.2 \qquad \text{(D) } 2.3 \qquad \text{(E) } 2.4$

## Solution 1
The broken flagpole forms a right triangle with legs $1$ and $x$ , and hypotenuse $5-x$ . The Pythagorean theorem now states that $1^2 + x^2 = (5-x)^2$ , hence $10x = 24$ , and $x=\boxed{2.4}$ .
(Note that the resulting triangle is the well-known $5-12-13$ right triangle, scaled by $1/5$ .)

## Solution 2
A right triangle is formed with the bottom of the flagpole, the snapped part, and the ground. One leg is of length $1$ and the other is length $x$ . By the Pythagorean theorem , we know that $\sqrt{x^2+1^2}$ must be the length of the snapped part of the flagpole. Observe that all the answer choices are rational. If $x$ is rational, $5-x$ , which is the snapped part, must also be rational. Therefore, $1, x, 5-x$ must form a scaled Pythagorean triple. We know that $10, 24, 26$ is a Pythagorean triple, so the corresponding answer must be $1, 2.4, 2.6$ . Adding together the $x$ and the snapped part, this does indeed equal $5$ , so our solution is done.

## Solution 3
Let $AB$ represent the flagpole in the diagram above. After the flagpole breaks at point $D$ , its tip lies at point $C$ . Since none of the flagpole is destroyed, we know that $DA=DC$ . Therefore, triangle $\triangle ADC$ is isosceles.
Draw the altitude $DE \perp AC$ . Since $\triangle ADC$ is isosceles, we know that $AE = EC$ . Also note that $\triangle AED \sim \triangle ABC$ . Therefore, \begin{align*} AD &= AE \times \frac{AD}{AE} \\ &= \frac{AC}{2} \times \frac{AC}{AB} \\ &= \frac{AC^2}{2 AB} \\ &= \frac{AB^2 + BC^2}{2 AB} \end{align*}
Since $AB = 5$ and $BC = 1$ , we have that $AD = \frac{5^2 + 1^2}{2 \cdot 5} = 2.6$ , and thus $x = AB - AD = \boxed{2.4}$ .

## Video Solution
There is currently no video solution on Youtube. A wrong link was posted here.
(I sent a request to BeautyofMath so there may be one on his channel soon)
~ ssr-07
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .