# 2008 AMC 8 Problem 21

## Problem

Jerry cuts a wedge from a $6$ -cm cylinder of bologna as shown by the dashed curve. Which answer choice is closest to the volume of his wedge in cubic centimeters?

[asy] defaultpen(linewidth(0.65)); real d=90-63.43494882; draw(ellipse((origin), 2, 4)); fill((0,4)--(0,-4)--(-8,-4)--(-8,4)--cycle, white); draw(ellipse((-4,0), 2, 4)); draw((0,4)--(-4,4)); draw((0,-4)--(-4,-4)); draw(shift(-2,0)*rotate(-d-5)*ellipse(origin, 1.82, 4.56), linetype("10 10")); draw((-4,4)--(-8,4), dashed); draw((-4,-4)--(-8,-4), dashed); draw((-4,4.3)--(-4,5)); draw((0,4.3)--(0,5)); draw((-7,4)--(-7,-4), Arrows(5)); draw((-4,4.7)--(0,4.7), Arrows(5)); label("$8$ cm", (-7,0), W); label("$6$ cm", (-2,4.7), N);[/asy]

$\textbf{(A)} \ 48 \qquad \textbf{(B)} \ 75 \qquad \textbf{(C)} \ 151\qquad \textbf{(D)} \ 192 \qquad \textbf{(E)} \ 603$

## Solution
The slice is cutting the cylinder into two equal wedges with equal volume. The cylinder's volume is $\pi r^2 h = \pi (4^2)(6) = 96\pi$ . The volume of the wedge is half this which is $48\pi \approx \boxed{\textbf{(C)}\ 151}$ .

## Video Solution by Omega Learn
https://youtu.be/FDgcLW4frg8?t=2556
~ pi_is_3.14
https://www.youtube.com/watch?v=q7OCpOn1abY ~David
### See Also