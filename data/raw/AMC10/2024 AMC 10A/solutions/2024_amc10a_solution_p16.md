# 2024 AMC 10A Problem 16

## Problem

All of the rectangles in the figure below, which is drawn to scale, are similar to the enclosing rectangle. Each number represents the area of the rectangle. What is length $AB$ ?

$\textbf{(A) }4+4\sqrt5\qquad\textbf{(B) }10\sqrt2\qquad\textbf{(C) }5+5\sqrt5\qquad\textbf{(D) }10\sqrt[4]{8}\qquad\textbf{(E) }20$

## Solution 1
Using the rectangle with area $1$ , let its short side be $x$ and the long side be $y$ . Observe that for every rectangle, since ratios of the side length of the rectangles are directly proportional to the ratios of the square roots of the areas (For example, each side of the rectangle with area $9$ is $\sqrt{9}=3$ times that of the rectangle with area $1$ ), as they are all similar to each other.
The side opposite $AB$ on the large rectangle is hence written as $6x + 4x + 2y\sqrt{2} + 3y\sqrt{2} = 10x+5y\sqrt{2}$ . However, $AB$ can be written as $4y\sqrt{2}+5x+7x = 4y\sqrt{2}+12x$ . Since the two lengths are equal, we can write $10x+5y\sqrt{2} = 4y\sqrt{2}+12x$ , or $y\sqrt{2} = 2x$ . Therefore, we can write $y=x\sqrt{2}$ .
Since $xy=1$ , we have $(x\sqrt{2})(x) = 1$ , which we can evaluate $x$ as $x=\frac{1}{\sqrt[4]{2}}$ . From this, we can plug back in to $xy=1$ to find $y=\sqrt[4]{2}$ . Substituting into $AB$ , we have $AB = 4y\sqrt{2}+12x = 4(\sqrt[4]{2})(\sqrt{2})+\frac{12}{\sqrt[4]{2}}$ which can be evaluated to $\boxed{\textbf{(D) }10\sqrt[4]{8}}$ .
~i_am_suk_at_math_2
### Remark
We know that the area is an integer, so after finding $y=x\sqrt{2}$ , AB must contain a 4th root. The only such option is $\boxed{\textbf{(D) }10\sqrt[4]{8}}$ .

## Solution 2
Let the rectangle's height be $x,$ the length $AB=y.$ The entire rectangle has an area of $200.$ We will be using this fact for ratios.
Note that the short side of the rectangle with area 32 will have a height of $\sqrt{\frac{32}{200}}\cdot x = \frac{2}{5}x.$ We use $x$ because it is apparent that the height of the rectangle with area $32$ is the shorter side, corresponding with $x.$
Similarly, the long side of the rectangle with area 36 has a height of $\sqrt{\frac{36}{200}}\cdot y = \frac{3\sqrt{2}}{10}y.$
Noting that the total height of the big rectangle has height $x,$ we have the equation $\frac25 x + \frac{3\sqrt{2}}{10}y = x \Rightarrow x=\frac{y}{\sqrt{2}}.$
Since the area $xy=\frac{y^2}{\sqrt{2}}$ is equal to 200, we have:
\begin{align*} y&=\sqrt{200\sqrt{2}} \\ &=\sqrt{100\sqrt{8}} \\ &=\boxed{\textbf{(D) }10\sqrt[4]{8}}. \end{align*}
~mathboy282

## Solution 3 - ruler (last effort)
Given that the diagram is drawn to scale, we can use a ruler to estimate the length of $AB$ .
We start by measuring the lengths of the rectangle with area $1$ , which may vary per viewing medium. For the sake of the solution, we use side lengths ~ $\frac{7}{10}$ cm and ~ $\frac{5}{10}$ cm.
To get the scale ratio from centimeters to the units in the problem, we need to find a ratio $x$ such that $\frac{7x}{10}\cdot\frac{5x}{10}=1$
Solving this equation, we get $x=\frac{10}{\sqrt{35}}$
We then measure the length of $AB$ (will vary), to get ~ $10.2$ cm. We multiply this length by our early ratio to get $\frac{10 \cdot 10.2}{\sqrt{35}} = \frac{102}{\sqrt{35}} \approx \frac{102}{6} \approx 17$
The answer choice closest to this would be $10\sqrt[4]{8}\approx16.8$ , so therefore the closest answer is $\boxed{\textbf{(D) }10\sqrt[4]{8}}$ .
~shreyan.chethan
Note: Never ever use this in an actual test
### Remark
The specific numbers used in the solution above vary per test medium, but the method should still work.

## Video Solution 1 by Pi Academy
https://youtu.be/fW7OGWee31c?si=oq7toGPh2QaksLHE

## Video Solution 2 by Power Solve
https://youtu.be/8abGnAJZ3AM

## Video Solution 3 by Innovative Minds (Similar to Solution 1 above)
https://youtu.be/EepOGN0_Rgw

## Video Solution by SpreadTheMathLove
https://youtu.be/x_Nux5ufe-k?si=shgvzOEWZ_KhEqUX

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=3068s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .