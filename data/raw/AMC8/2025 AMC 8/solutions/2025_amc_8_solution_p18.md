# 2025 AMC 8 Problem 18

## Problem

The circle shown below on the left has a radius of 1 unit. The region between the circle and the inscribed square is shaded. In the circle shown on the right, one quarter of the region between the circle and the inscribed square is shaded. The shaded regions in the two circles have the same area. What is the radius $R$ , in units, of the circle on the right?

[asy] unitsize(40); real a = 0.707; fill(circle((a,a), 1), grey); fill((0,0)--(0,1.414)--(1.414,1.414)--(1.414,0)--cycle, white); draw((0,0)--(0,1.414)--(1.414,1.414)--(1.414,0)--cycle); draw(circle((a,a), 1)); draw((0.707,0.707)--(1.414,1.414)); dot((0.707,0.707)); label("$1$", (1,1), SE); fill(circle((4+a, a), 2*a), grey); fill(shift((4+a,a)) * ((-2,-2)--(1,-2)--(1,2)--(-2,2)--cycle), white); draw(shift((4+a,a)) * ((-1,-1)--(1,-1)--(1,1)--(-1,1)--cycle)); draw(circle((4+a, a), 2*a)); draw((4+a,a)--(5+a,1+a)); dot((4+a,a)); label("$R$", (a+4.5,a+0.5), SE); [/asy]

$\textbf{(A)}\ \sqrt2\qquad \textbf{(B)}\ 2\qquad \textbf{(C)}\ 2\sqrt2\qquad \textbf{(D)}\ 4\qquad \textbf{(E)}\ 4\sqrt2$

## Solution
The area of the shaded region in the circle on the left is the area of the circle minus the area of the square, or $\big(\pi-2)$ . The shaded area in the circle on the right is $\dfrac{1}{4}$ of the area of the circle minus the area of the square, or $\dfrac{\pi R^2-2R^2}{4}$ , which can be factored as $\dfrac{R^2(\pi-2)}{4}$ . Since the shaded areas are equal to each other, we have $\pi-2=\dfrac{R^2(\pi-2)}{4}$ , which simplifies to $R^2=4$ . Taking the square root, we have $R=\boxed{\text{(B)\ 2}}$
~mrtnvlknv

## Solution (Trig)
The side length of the smaller square is $\sqrt{2}$ , which follows from the Pythagorean Theorem since the square is inscribed in a circle of radius $1$ , making the diagonal equal to $2$ . Thus, the area of the square is $(\sqrt{2})^2 = 2$ . The circle in which the square is inscribed has radius $1$ , so its area is $\pi \cdot 1^2 = \pi$ . Therefore, the area of the shaded region (the part of the circle not covered by the square) is $\pi - 2$ .
Now, consider the larger square, which is inscribed in a circle of radius $R$ . This square can be divided into four congruent right triangles by drawing lines from the center of the circle to the vertices of the square. Each triangle has legs of length $R$ and includes a $90^\circ$ angle at the center. Using the triangle area formula $\frac{1}{2}ab\sin(C)$ with $a = b = R$ and $C = 90^\circ$ , each triangle has area $\frac{1}{2}R^2$ . Since there are four such triangles, the area of the square is $4 \cdot \frac{1}{2}R^2 = 2R^2$ . The area of the circle is $\pi R^2$ , so the area of the shaded region (the part of the circle outside the square) is $\frac{1}{4}(\pi R^2 - 2R^2) = \frac{1}{4}R^2(\pi - 2)$ .
We are told that this shaded region also has area equal to $\pi - 2$ , so we set up the equation $\frac{1}{4}R^2(\pi - 2) = \pi - 2$ . Assuming $\pi - 2 \neq 0$ , we divide both sides by $\pi - 2$ , giving $\frac{1}{4}R^2 = 1$ , which leads to $R^2 = 4$ , and finally $R = 2$ . Thus, the answer is $\boxed{\text{(B) } 2}$ .
~ GREATEST ~

## Solution 2
We start with the first area. Since the square is inscribed, its diagonal is $2\implies$ its side length is $\sqrt{2}\implies$ its area is $2$ , therefore the first area is $\pi-2$ . The second area is $\dfrac{R^2\pi-2R^2}{4}$ , found in a similar manner. Writing and solving the equation, we have \[\pi-2=\dfrac{R^2\pi-2R^2}{4}\implies4(\pi-2)=R^2(\pi-2)\implies R=2.\] The answer is $\boxed{\text{(B) }2}$ ~Tacos_are_yummy_1

## Solution 3 (Using similarity)
Since the two figures are similar, and the 4 regions in the first circle are equal in area to one of the four regions in the second circle, the second figure's area is $4$ times the first figure's area. Therefore, the side lengths are multiplied by a factor of $\sqrt{4} = 2$ , so the answer is $1 \cdot 2 = \boxed{\textbf{(B)} 2}$ .
~alwaysgonnagiveyouup

## Solution 4
(Really similar to Solution 1, but has a more larger explanation for the answer) First find the area of the smaller circle with the known radius. Since the radius is $1$ , the area of the circle is $\pi$ , and finding the side length of the square would equal to $\sqrt{2}$ . Squaring that gives us the area of the square which is $2$ , and the shaded area of the first one is equal to $\pi - 2$ . The second area can be shortened to $\frac{R^2\pi}{4} - \frac{\left(\sqrt{2R^2}\right)^2}{4}$ , since we only need $\frac{1}{4}$ th of the sections. We then make them equal, which makes this equation:
$\pi - 2 = \frac{R^2\pi}{4} - \frac{\left(\sqrt{2R^2}\right)^2}{4}$
Simplifying this equation would be $4\pi - 8 = R^2\pi - 2R^2$ . We can factor out the $R^2$ which makes $4\pi - 8 = R^2\left(\pi - 2\right)$ . Dividing out the $\pi - 2$ would give us $4$ on the left side. $4 = R^2$ which leaves us to choice $\boxed{\text{(B) }2}$ . ~Imhappy62789

## Solution 5
We are given two circles, each with an inscribed square. In the first circle, the radius is 1 unit, and the region between the circle and the inscribed square is shaded. In the second circle, one quarter of the region between the circle and the inscribed square is shaded. The shaded areas in both circles are the same. Our goal is to determine the radius $R$ of the second circle.
Step 1: Set up a ratio for the areas of the shaded regions
We know that the shaded region in the first circle (with radius 1) and the shaded region in the second circle (with radius $R$ ) are proportional in terms of the total area between the circle and the inscribed square. The shaded area in the second circle is one quarter of the total area between the circle and the square, while the shaded area in the first circle is the entire region.
Step 2: Relate the areas to the radius
Let’s recall that the area between the circle and the inscribed square is proportional to the square of the radius of the circle because the square's side length scales with the radius of the circle.
So, in the first circle with radius 1: \[\text{Area between circle and square} \propto 1^2 = 1\] and the shaded area is proportional to the entire area between the circle and the square, i.e., 1.
In the second circle with radius $R$ : \[\text{Area between circle and square} \propto R^2\] and the shaded area is one-quarter of this total area, so it is proportional to $\frac{1}{4} R^2$ .
Step 3: Set up the ratio of shaded areas
We are told that the shaded areas in both circles are the same, so we set up the following equation: \[1 = \frac{1}{4} R^2\]
Step 4: Solve for
Multiply both sides of the equation by 4: \[4 = R^2\] Taking the square root of both sides: \[R = 2\]
Thus, the radius of the second circle is $\boxed{\text{(B) 2}}$ .
~ aoum

## Solution 6
Notice that if you shaded the rest of the region between the square and the circle, then the area would be $4$ times the area of the shaded region in the smaller circle. Since the radius changes by a factor of $k^2$ , $k^2 = 4$ , solving for gets you $2$ . Hence, the answer is $\fbox{\textbf{(B)}\ 2}$
~Avy11

## Video Solution by Pi Academy (Clever)
https://youtu.be/Iv_a3Rz725w?si=E0SI_h1XT8msWgkK

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=wti8JNhNkM77LtdZ&t=2146 ~hsnacademy

## Video Solution by Thinking Feet
https://youtu.be/PKMpTS6b988
### See Also