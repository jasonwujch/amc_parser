# 2011 AIME I Problem 6

## Problem

Suppose that a parabola has vertex $\left(\frac{1}{4},-\frac{9}{8}\right)$ and equation $y = ax^2 + bx + c$ , where $a > 0$ and $a + b + c$ is an integer. The minimum possible value of $a$ can be written in the form $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p + q$ .

## Solution
If the vertex is at $\left(\frac{1}{4}, -\frac{9}{8}\right)$ , the equation of the parabola can be expressed in the form \[y=a\left(x-\frac{1}{4}\right)^2-\frac{9}{8}.\] Expanding, we find that \[y=a\left(x^2-\frac{x}{2}+\frac{1}{16}\right)-\frac{9}{8},\] and \[y=ax^2-\frac{ax}{2}+\frac{a}{16}-\frac{9}{8}.\] From the problem, we know that the parabola can be expressed in the form $y=ax^2+bx+c$ , where $a+b+c$ is an integer. From the above equation, we can conclude that $a=a$ , $-\frac{a}{2}=b$ , and $\frac{a}{16}-\frac{9}{8}=c$ . Adding up all of these gives us \[\frac{9a-18}{16}=a+b+c.\] We know that $a+b+c$ is an integer, so $9a-18$ must be divisible by $16$ . Let $9a=z$ . If ${z-18}\equiv {0} \pmod{16}$ , then ${z}\equiv {2} \pmod{16}$ . Therefore, if $9a=2$ , $a=\frac{2}{9}$ . Adding up gives us $2+9=\boxed{011}$

## Solution 2
Complete the square. Since $a>0$ , the parabola must be facing upwards. $a+b+c=\text{integer}$ means that $f(1)$ must be an integer. The function can be recasted into $a\left(x-\frac{1}{4}\right)^2-\frac{9}{8}$ because the vertex determines the axis of symmetry and the critical value of the parabola. The least integer greater than $-\frac{9}{8}$ is $-1$ . So the $y$ -coordinate must change by $\frac{1}{8}$ and the $x$ -coordinate must change by $1-\frac{1}{4}=\frac{3}{4}$ . Thus, $a\left(\frac{3}{4}\right)^2=\frac{1}{8}\implies \frac{9a}{16}=\frac{1}{8}\implies a=\frac{2}{9}$ . So $2+9=\boxed{011}$ .

## Solution 3
To do this, we can use the formula for the minimum (or maximum) value of the $x$ coordinate at a vertex of a parabola, $-\frac{b}{2a}$ and equate this to $\frac{1}{4}$ . Solving, we get $-\frac{a}{2}=b$ . Enter $x=\frac{1}{4}$ to get $-\frac{9}{8}=\frac{a}{16}+\frac{b}{4}+c=-\frac{a}{16}+c$ so $c=\frac{a-18}{16}$ . This means that $\frac{9a-18}{16}\in \mathbb{Z}$ so the minimum of $a>0$ is when the fraction equals -1, so $a=\frac{2}{9}$ . Therefore, $p+q=2+9=\boxed{011}$ . -Gideontz

## Solution 4
Write this as $a\left( x- \frac 14 \right)^2 - \frac 98$ . Since $a+b+c$ is equal to the value of this expression when you plug $x=1$ in, we just need $\frac{9a}{16}- \frac 98$ to be an integer. Since $a>0$ , we also have $\frac{9a}{16}>0$ which means $\frac{9a}{16}- \frac 98 > -\frac{9}{8}$ . The least possible value of $a$ is when this is equal to $-1$ , or $a=\frac 29$ , which gives answer $11$ .
-bobthegod78, krwang, Simplest14

## Solution 5 (You don't remember conic section formulae)
Take the derivative to get that the vertex is at $2ax+b=0$ and note that this implies $\frac{1}{2} \cdot a = -b$ and proceed with any of the solutions above.
~Dhillonr25
$\textbf{Appendix to Solution 5 (You don't remember differential calculus)}$
Note that the quadratic formula for finding roots of parabolas is $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ , so if you average the two x-values of the roots the $\pm\sqrt{b^2-4ac}$ part will cancel out and leave you with $x=-\frac{b}{2a}$ . Then proceed as above.
~WhatdoHumanitariansEat

## Video Solution
https://www.youtube.com/watch?v=vkniYGN45F4
- AIME Problems and Solutions
- American Invitational Mathematics Examination
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .