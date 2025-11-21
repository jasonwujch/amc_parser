# 2014 AMC 8 Problem 14

## Problem

Rectangle $ABCD$ and right triangle $DCE$ have the same area. They are joined to form a trapezoid, as shown. What is $DE$ ?

[asy] size(250); defaultpen(linewidth(0.8)); pair A=(0,5),B=origin,C=(6,0),D=(6,5),E=(18,0); draw(A--B--E--D--cycle^^C--D); draw(rightanglemark(D,C,E,30)); label("$A$",A,NW); label("$B$",B,SW); label("$C$",C,S); label("$D$",D,N); label("$E$",E,S); label("$5$",A/2,W); label("$6$",(A+D)/2,N); [/asy]

$\textbf{(A) }12\qquad\textbf{(B) }13\qquad\textbf{(C) }14\qquad\textbf{(D) }15\qquad\textbf{(E) }16$

## Solution 1
The area of $\bigtriangleup CDE$ is $\frac{DC\cdot CE}{2}$ . The area of $ABCD$ is $AB\cdot AD=5\cdot 6=30$ , which also must be equal to the area of $\bigtriangleup CDE$ , which, since $DC=5$ , must in turn equal $\frac{5\cdot CE}{2}$ . Through transitivity, then, $\frac{5\cdot CE}{2}=30$ , and $CE=12$ . Then, using the Pythagorean Theorem, you should be able to figure out that $\bigtriangleup CDE$ is a $5-12-13$ triangle, so $DE=\boxed{13}$ , or $\boxed{(B)}$ .

## Solution 2
The area of the rectangle is $5\times6=30.$ Since the parallel line pairs are identical, $DC=5$ . Let $CE$ be $x$ . $\dfrac{5x}{2}=30$ is the area of the right triangle. Solving for $x$ , we get $x=12.$ According to the Pythagorean Theorem, we have a $5-12-13$ triangle. So, the hypotenuse $DE$ has to be $\boxed{(B)}$ .

## Solution 3
This problem can be solved with the Pythagorean Theorem ( $a^2 + b^2 = c^2$ ). We know $AB = DC$ , so $DC = 5$ . $CE$ is twice the length of $AD$ , so $CE = 12$ . $5^2 + 12^2 = c^2$ . $5^2 = 25$ . $12^2 = 144$ . $25 + 144 = 169$ . $169$ has a square root of $13$ , so the hypotenuse or $DE$ is $13$ . The answer is $\boxed{(B)}$ .
——MiracleMaths
Note: Another way to find out that CE is 12 is by using logic. Since DC = 5, we can reason that the triangle is a 5 - 12 - 13 triangle, because the only Pythagorean Triple with 5 as a leg(not hypotenuse, as that would be the case for a 3 - 4 - 5 right triangle), is 5 - 12 - 13. We know DE is the hypotenuse, so it can’t be 12, which means CE has to be 12, which, in turn, means that DE has to be: 13 $\boxed{(B)}$ .

## Video Solution (CREATIVE THINKING)
https://youtu.be/ToM-f4WMWjQ
~Education, the Study of Everything

## Video Solution
https://youtu.be/-JsXX8WLASg ~savannahsolver

## Video Solution
https://youtu.be/j3QSD5eDpzU?t=88
~ pi_is_3.14
### See Also