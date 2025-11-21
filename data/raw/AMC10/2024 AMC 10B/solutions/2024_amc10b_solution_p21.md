# 2024 AMC 10B Problem 21

## Problem

Two straight pipes (circular cylinders), with radii $1$ and $\frac{1}{4}$ , lie parallel and in contact on a flat floor. The figure below shows a head-on view. What is the sum of the possible radii of a third parallel pipe lying on the same floor and in contact with both?

[asy] size(6cm); draw(circle((0,1),1), linewidth(1.2)); draw((-1,0)--(1.25,0), linewidth(1.2)); draw(circle((1,1/4),1/4), linewidth(1.2)); [/asy]

$\textbf{(A)}~\frac{1}{9} \qquad\textbf{(B)}~1 \qquad\textbf{(C)}~\frac{10}{9} \qquad\textbf{(D)}~\frac{11}{9} \qquad\textbf{(E)}~\frac{19}{9}$

## Solution 1
Notice that the sum of radii of two circles tangent to each other will equal to the distance from center to center. Set the center of the big circle be at $(0,1).$ Since both circles are tangent to a line (in this case, $y=0$ ), the y-coordinates of the centers are just its radius.
Hence, the center of the smaller circle is at $\left(x_2, \frac14\right)$ . From the the sum of radii and distance formula, we have: \[1+\frac14 = \sqrt{x_2^2 + \left(\frac34\right)^2} \Rightarrow x_2 = 1.\]
So, the coordinates of the center of the smaller circle are $(1, \frac14).$ Now, let $(x_3,r_3)$ be the coordinates of the new circle. Then, from the fact that sum of radii of this circle and the circle with radius $1$ is equal to the distance from the two centers, you have: \[\sqrt{(x_3-0)^2+(r_3-1)^2} = 1+r_3.\] Similarly, from the fact that the sum of radii of this circle and the circle with radius $\frac14$ , you have: \[\sqrt{(x_3-1)^2+\left(r_3-\frac14\right)^2}= \frac14 + r_3.\] Squaring the first equation, you have: \[x_3^2+r_3^2-2r_3+1=1+2r_3+r_3^2 \Rightarrow 4r_3=x_3^2 \Rightarrow x_3=2\sqrt{r_3}.\] Squaring the second equation, you have: \[x_3^2-2x_3+1+r_3^2-\frac{r_3}{2}+\frac{1}{16}=\frac{1}{16}+\frac{r_3}{2}+r_3^2 \Rightarrow x_3^2-2x_3+1=r_3\] Plugging in from the first equation we have \[r_3-1=x_3^2-2x_3=4r_3-4\sqrt{r_3} \Rightarrow 3r_3-4\sqrt{r_3}+1=0 \Rightarrow (3\sqrt{r_3}-1)(\sqrt{r_3}-1)=0 \Rightarrow r_3=1, \frac19.\] Summing these two yields $\boxed{\frac{10}{9}}.$
~mathboy282
### Diagram
[asy] // By Elephant200 size(8cm); draw(circle((0,1),1), linewidth(1.2)); draw((-1,0)--(3,0), linewidth(1.2)); draw(circle((1,1/4),1/4), linewidth(1.2)); draw(circle((2/3,1/9),1/9), red+linewidth(1.2)); draw(circle((2,1),1), red+linewidth(1.2)); [/asy] ~Elephant200

## Solution 2 (Clever Manipulation)
In general, let the left and right outer circles and the center circle have radii $r_1,r_2,r_3$ . When three circles are tangent as described in the problem, we can deduce $\sqrt{r_3}=\frac{\sqrt{r_1r_2}}{\sqrt{r_1}+\sqrt{r_2}}$ by Pythagorean theorem.
Setting $r_1=1, r_2=\frac14$ we have $r_3=\frac19$ , and setting $r_1=1,r_3=\frac14$ we have $r_2=1$ . Thus our answer is $\boxed{\textbf{(C)}}$ .
~Mintylemon66

## Solution 3 (Descartes’s Theorem)
Descartes’s Theorem states that for curvatures $k_1,k_2,k_3,k_4$ we have
\[(k_1+k_2+k_3+k_4)^2=2(k_1^2+k_2^2+k_3^2+k_4^2)\]
with a curvature being the reciprocal of the radius of a circle, being positive if it is externally tangent to other circles, negative if it is internally tangent to other circles, and zero if we consider a line as a degenerate circle. Here our curvatures are $k_1=1,k_2=4,k_3=0$ , and we wish to find $k_4$ . Plugging these values into our formula yields:
\[(1+4+0+k_4)^2=2(1^2+4^2+0^2+k_4^2)\]
\[(5+k_4)^2=2(17+k_4^2)\]
\[k_4^2+10k_4+25=2k_4^2+34\]
\[k_4^2-10k_4+9=0\]
\[k_4=1,9\]
The curvature and the radius are reciprocals, so our radii must be $1$ and $\frac{1}{9}$ , and their sum is $\boxed{\textbf{(C) }\frac{10}{9}}$ .
~eevee9406

## Solution 4 (Advanced Guesswork)
Looking at the diagram, we see that there must be a circle with a radius smaller than $\frac14$ , and there must be a circle with a radius close to $1$ . Looking at the answers, we can assume that the answer choice is above $1$ , eliminating the first two answers. We can also assume that some students will only solve for the smaller circle, while others may only solve for the larger circle. It would be reasonably safe to say that one of the answers must be the radius of the smaller circle, while another must be the radius of the bigger circle. Looking at the answers, we see that $\frac19$ and $1$ are reasonably close to the radii of the missing circles in the diagram, so we add them up to get $\boxed{\textbf{(C) }\frac{10}{9}}$ .
~YTH

## Solution 5 (Essentially Solution 3)
For a problem like this with three externally tangent circles that are all tangent to a line, we can use a specific form of Descartes's Circle Theorem. Let the curvatures of the three circles be $r_1, r_2, r_3$ . The curvature of a circle is just the reciprocal of the radius. Then we get, \[(r_1 + r_2 + r_3)^2 = 2(r_1^2 + r_2^2 + r_3^2)\] Plugging in the information we already have, we get: \[(1 + 4 + r_3)^2 = 2(1^2 + 4^2 + r_3^2)\] \[(5 + r_3)^2 = 2(17 + r_3^2)\] \[25 + 10r_3 + r_3^2 = 34 + 2r_3^2\] \[r_3^2 - 10r_3 - 9 = 0\] \[(r_3 - 1)(r_3 - 9) = 0\] So, we get our two curvatures: 1 and 9. The radii equivalent are $1$ and $\frac{1}{9}$ . Adding these up, we get $\boxed{\textbf{(C) }\frac{10}{9}}$ .
~Mr.Lightning

## Solution 6 (Metasolving)
By looking at the answer choices, we realize that the answers are all sums of each other, and thus think "The AMC problem committee made the answers $\frac{1}{9}$ and $1$ so the people who only got one of the answers will pick either of the first two answers and those who counted one of the answers twice would pick either of the last two answers", and realize that the answers are most likely $1$ and $\frac{1}{9}$ . Confirming with a ruler, we get $\frac{1}{9}$ + $1$ = $\boxed{\textbf{(C) }\frac{10}{9}}$ , which is the solution.
∼Glowworm
Minor issue with this is that 10/9 is also an answer choice, and 1/9 + 10/9 = 11/9 which is also an answer choice, so it comes down to a bit of luck.
~meikh_neiht

## Solution 7(practically similar to the other solutions)
We can immediately see that we can put a circle with radius $1$ outside of the two circles already drawn that are tangent to the circles. If you brought a ruler with you, you can confirm this. We now find the radius of the circle between the circles of radius $1$ and $\frac{1}{4}$ .. By drawing out the diagram, a geometry hack is to draw lines connecting the centers of the circles. Using the fact that tangent lines to the radius are perpendicular, we can construct a trapezoid with heights of lengths $1$ and $\frac{1}{4}$ , a slant base of length $1 + \frac{1}{4} = \frac{5}{4}$ . To find the base of the trapezoid, we can construct a right triangle with the slant base as the hypotenuse and a leg of length $1 - \frac{1}{4} = \frac{3}{4}$ . Therefore, we see we have a $3-4-5$ right triangle and the length of the base of the trapezoid is conveniently just $1$ . Let the radius of the circle between the two given circles $r$ . By drawing the center of this circle and connecting the radius to the radii of the other two circles, we can construct two more trapezoids similar to the initially big one we constructed: one with perpendicular heights of lengths $1$ and $r$ and a slant base of $1 + r$ , and another with perpendicular heights of lengths $\frac{1}{4}$ and $r$ and a slant base of length $r + \frac{1}{4}$ . To find the bases of these trapezoids,(which we know sums to $1$ as we found earlier), we can use a similar trick by constructing right triangles. We can construct two right triangles: one with hypotenuse $1 + r$ and a leg of length $1 - r$ , and another with hypotenuse $r + \frac{1}{4}$ and a leg of length $\frac{1}{4} - r$ . We can use the Pythagorean Theorem to find the other legs of these right triangles and we can set the sum to equal $1$ . Conveniently, the leg lengths turns out of be $2\sqrt{r}$ and $\sqrt{r}$ , respectively, and therefore the sum will just be $3\sqrt{r}$ . Since this is equal to $1$ , we can solve $3\sqrt{r} = 1$ to get the radius to be equal to $\frac{1}{9}$ . Now, we add $1$ and $\frac{1}{9}$ to get $\frac{10}{9}$ and our answer is just $\boxed{\textbf{(C) }\frac{10}{9}}$ .
[asy] // By Elephant200 size(8cm); draw(circle((0,1),1), linewidth(1.2)); draw((-1,0)--(3,0), linewidth(1.2)); draw(circle((1,1/4),1/4), linewidth(1.2)); draw(circle((2/3,1/9),1/9), red+linewidth(1.2)); draw(circle((2,1),1), red+linewidth(1.2)); [/asy]
credit to Elephant200 for the diagram
~ilikemath247365

## Video Solution 1 by Pi Academy (In Less Than 5 Mins ⚡🚀)
https://youtu.be/5fID8UOohr0?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://youtu.be/fuZLWJtq-Lk?si=VKfzKopi-Hr9Zn09
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .