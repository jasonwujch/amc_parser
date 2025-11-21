# 2012 AMC 8 Problem 25

## Problem

A square with area $4$ is inscribed in a square with area $5$ , with each vertex of the smaller square on a side of the larger square. A vertex of the smaller square divides a side of the larger square into two segments, one of length $a$ , and the other of length $b$ . What is the value of $ab$ ?

[asy] draw((0,2)--(2,2)--(2,0)--(0,0)--cycle); draw((0,0.3)--(0.3,2)--(2,1.7)--(1.7,0)--cycle); label("$a$",(-0.1,0.15)); label("$b$",(-0.1,1.15));[/asy]

$\textbf{(A)}\hspace{.05in}\frac{1}5\qquad\textbf{(B)}\hspace{.05in}\frac{2}5\qquad\textbf{(C)}\hspace{.05in}\frac{1}2\qquad\textbf{(D)}\hspace{.05in}1\qquad\textbf{(E)}\hspace{.05in}4$

## Solution 1 - Recommended for Contest
The total area of the four congruent triangles formed by the squares is $5-4 = 1$ . Therefore, the area of one of these triangles is $\frac{1}{4}$ . The height of one of these triangles is $a$ and the base is $b$ . Using the formula for area of the triangle, we have $\frac{ab}{2} = \frac{1}{4}$ . Multiply by $2$ on both sides to find that the value of $ab$ is $\boxed{\textbf{(C)}\ \frac{1}2}$ .

## Solution 2 (Algebra)
We see that we want $ab$ , so instead of solving for $a$ and $b$ , we find a way to get an expression with $ab$ .
By the Triple Perpendicularity Model, all four triangles are congruent.
By the Pythagorean Theorem,
$\sqrt{a^2+b^2} = \sqrt{4}$
Thus, $\sqrt{a^2+b^2} = 2$
As $a+b=\sqrt{5}$ ,
$a^2+2ab+b^2 = 5$
So, $\sqrt{5-2ab} = 2$
Simplifying,
$5-2ab = 4$
$-2ab=-1$
$ab=\frac{1}{2}$ or $\boxed{\textbf{(C)} \frac{1}{2}}$
~ lovelearning999

## Solution 3 (similar to solution 2)
We know that each side of a square is equal, and each the area of a square can be expressed as the side squared. We can let the outside square with area 5's side be $x$ . We get the equation $x^2 = 5$ . Simplifying this we get $x=\sqrt5$ .
We can then create the equation $a+b=\sqrt5$ .
Using the same tactic we get that the side length of the inner square is $2$ . By the Pythagorean Theorem,
$a^2 + b^2 = 2^2$ .
We can then express this expression as
$(a+b)^2 - 2ab = 4$ .
We recall that $a+b=\sqrt5$ and substitute it into our current equation:
$(\sqrt5)^2 - 2ab = 4$ .
We further simplify this to $ab=1/2$ which is $\boxed{\textbf{(C)} \frac {1}{2}}$ .

## Solution 4 (The Long Way)
Visually, $a+b=\sqrt5$ (1) and we can tell that all the triangles are congruent. That means the long side of all the triangles is $b$ and the short side will always be $a$ . Notice that the hypotenuse is the side of the smaller square (2). Using the Pythagorean theorem, $a^2+b^2=2^2$ or $a^2+b^2=4$ (2).
Now we just have a system of equations:
Isolate b in (1) -> $b=\sqrt5-a$ , and plug it in to (2).
$a^2+(5-a)^2=4$ , Simplifying should get you to $2a^2-2a\sqrt5+1=0$
Using the quadratic formula, $a=\frac{2\sqrt5 \pm \sqrt{20-8}}{4}$
Simplifying the squareroots, $a=\frac{\sqrt5+\sqrt3}{2}$ .
This yields b to be $\frac{\sqrt5-\sqrt3}{2}$ via substituting into (1)
$ab=\frac{(\sqrt5+\sqrt3)(\sqrt5-\sqrt3)}{2*2}$ (difference of squares) $= \frac{5-3}{4} = \boxed{\textbf{(C)} \frac {1}{2}}$
~RandomMathGuy500

## Solution 3 (Pythagorean Theorem & Vieta's Formula)
Proceed as in solution 3 until you get the equation $2a^2-2a\sqrt5+1=0$ . The two solutions to this equation will be the long and short side of the triangle we are looking for, or $a$ and $b$ from the problem statement. Using Vieta's formula, their product is the constant term divided by the quadratic term, or $\boxed{\textbf{(C)} \frac {1}{2}}$ .
~nbeaudrot

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=2

## Video Solution 2
https://youtu.be/MhxGq1sSA6U ~savannahsolver
~ pi_is_3.14
### See Also