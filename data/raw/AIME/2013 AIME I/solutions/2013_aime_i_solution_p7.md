# 2013 AIME I Problem 7

## Problem

A rectangular box has width $12$ inches, length $16$ inches, and height $\frac{m}{n}$ inches, where $m$ and $n$ are relatively prime positive integers. Three faces of the box meet at a corner of the box. The center points of those three faces are the vertices of a triangle with an area of $30$ square inches. Find $m+n$ .

## Solution 1
Let the height of the box be $x$ .
After using the Pythagorean Theorem three times, we can quickly see that the sides of the triangle are 10, $\sqrt{\left(\frac{x}{2}\right)^2 + 64}$ , and $\sqrt{\left(\frac{x}{2}\right)^2 + 36}$ . Since the area of the triangle is $30$ , the altitude of the triangle from the base with length $10$ is $6$ .
Considering the two triangles created by the altitude, we use the Pythagorean theorem twice to find the lengths of the two line segments that make up the base of $10$ .
We find: \[10 = \sqrt{\left(28+x^2/4\right)}+x/2\]
Solving for $x$ gives us $x=\frac{36}{5}$ . Since this fraction is simplified: \[m+n=\boxed{041}\]
The 3D version of the Pythagorean theorem can also be applied here. ~MC

## Solution 2 (Vectors)
We may use vectors. Let the height of the box be $2h$ . Without loss of generality, let the front bottom left corner of the box be $(0,0,0)$ . Let the center point of the bottom face be $P_1$ , the center of the left face be $P_2$ and the center of the front face be $P_3$ .
We are given that the area of the triangle $\triangle P_1 P_2 P_3$ is $30$ . Thus, by a well known formula, we note that $\frac{1}{2}|\vec{P_1P_2} \text{x} \vec{P_1P_3}|=30$ We quickly attain that $\vec{P_1P_2}=<-6,0,h>$ and $\vec{P_1P_3}=<0,-8,h>$ (We can arbitrarily assign the long and short ends due to symmetry)
Computing the cross product, we find: \[\vec{P_1P_2} x \vec{P_1P_3}=-<6h,8h,48>\]
Thus: \[\sqrt{(6h)^2+(8h)^2+48^2}=2*30=60\] \[h=3.6\] \[2h=7.2\]
\[2h=36/5\]
\[m+n=\boxed{041}\]

## Solution 3
Let the height of the box be $x$ .
After using the Pythagorean Theorem three times, we can quickly see that the sides of the triangle are 10, $\sqrt{(x/2)^2 + 64}$ , and $\sqrt{(x/2)^2 + 36}$ . Therefore, we can use Heron's formula to set up an equation for the area of the triangle.
The semiperimeter is $\left(10 + \sqrt{(x/2)^2 + 64} + \sqrt{(x/2)^2 + 36}\right)/2$ . Therefore, when we square Heron's formula, we find
\begin{align*}900 &= \frac{1}{2}\left(\left(10 + \sqrt{(x/2)^2 + 64} + \sqrt{(x/2)^2 + 36}\right)/2\right)\times\left(\left(10 + \sqrt{(x/2)^2 + 64} + \sqrt{(x/2)^2 + 36}\right)/2 - 10\right)\\&\qquad\times\left(\left(10 + \sqrt{(x/2)^2 + 64} + \sqrt{(x/2)^2 + 36}\right)/2 - \sqrt{(x/2)^2 + 64}\right)\\&\qquad\times\left(\left(10 + \sqrt{(x/2)^2 + 64} + \sqrt{(x/2)^2 + 36}\right)/2 - \sqrt{(x/2)^2 + 36}\right).\end{align*}
Solving, we get $\boxed{041}$ .

## Solution 4
It isn't hard to see that the triangle connecting the centers of the faces of the rectangular prism is congruent to the triangle connecting the midpoints of three edges that concur. So we can now apply de Gua's theorem ( https://en.wikipedia.org/wiki/De_Gua%27s_theorem ) to see that:
$30^2=24^2+(3x)^2+(4x)^2$
Where $x$ is half the desired length of the height.
Solving yields $2x=\frac{36}{5}$
And thus $36+5=\boxed{041}$
---Solution 4 contributed by Siddharth Namachivayam

## Solution 5 (PyTRIGorean)
Let half the height be $a$ (we want to find $2a$ ), then we see that the three sides of the triangle are (by Pyth Theorem) $10, \sqrt{a^2+36}, \sqrt{a^2+64}$ . Using the Law of Sines with the angle as the one included between the square roots, we see that this angle's cosine is $\frac{a^2}{\sqrt{(a^2+36)(a^2+64)}}$ by the Law of Cosines, meaning that its sine is $\frac{\sqrt{100a^2+2304}}{\sqrt{(a^2+36)(a^2+64)}}$ . Finally, multiply the two square-rooted sides by this sine and one-half, and equate to 30.
You get $\sqrt{25a^2+576} = 30$ , giving $a=\frac{18}{5}$ , so our answer is $\boxed{041}$

## Solution 6 (Heron's Formula Application)
Let $x$ be $\frac12$ the height of the box. We will solve for $x$ and then multiply by $2$ at the end. The three side lengths of the triangle, by the Pythagorean Theorem, are $\sqrt{x^2+6^2},\sqrt{x^2+8^2},$ and $10$ .
Heron's formula states that the area of the triangle is $\sqrt{s(s-a)(s-b)(s-c)}$ where $s$ is the semiperimeter. Applying difference of squares to make the formula less computational, we get $\frac{\sqrt{(a+b+c)(a+b-c)(a-b+c)(-a+b+c)}}{4}=\frac{\sqrt{(a^2+b^2+2ab-c^2)(c^2-b^2-a^2+2ab)}}4=\frac{\sqrt{4a^2b^2-(a^2+b^2-c^2)^2}}4$ .
Now, we plug in $\sqrt{x^2+6^2}$ for $a$ , $\sqrt{x^2+8^2}$ for $b$ , and $10$ for $c$ . This gives us \[\frac{\sqrt{4(x^2+6^2)(x^2+8^2)-(x^2+6^2+x^2+8^2-10^2)^2}}4=30\] \[\sqrt{4x^4+400x^2+4\cdot48^2-4x^4}=120\] \[400x^2+4\cdot48^2=120^2\] \[25x^2+24^2=30^2\] \[25x^2=6^2(5^2-4^2)\] \[25x^2=18^2\] \[5x=18\] \[x=\frac{18}5\]
Now multiplying by $2$ , we get that the height is $\frac{36}5$ , and $m+n=36+5=\boxed{041}$

## Solution 7 (Pyramids)
Let the rectangular prism be $ABCDEFGH$ with $AB=12$ , $AC=16$ , and $AD=\alpha$ edges of the cube. It is easy to notice that the triangle given by the problem is similar to the triangle $BCD$ by a ratio of $1:2$ . Thus $[BCD]=120$ .
We know that the volume of the triangular pyramid defined by $A,B,C,D$ is equal to $\frac{1}{3}\cdot12\cdot16\cdot\alpha\cdot\frac{1}{2}=32\alpha$ , and we can find the volume by using the triangle $BCD$ as the base. Letting $h$ be the distance from $A$ to $\triangle BCD$ , we find that the volume is $\frac{1}{3}\cdot h\cdot120=40h$ . Thus $h=\frac{4}{5}\alpha$ , and all that remains is to find an equation for $h$ .
Let $A$ be the origin of a three-dimensional plane, and let the line segments $AB,AC,AD$ lie on the $x,y,z$ axes respectively. We know that the equation of the plane in which $\triangle BCD$ lies can be represented by the equation $ax+by+cz=d$ , where $a,b,c,d$ are real values, and we know that $B(12,0,0),C(0,16,0),D(0,0,\alpha)$ lie on $\triangle BCD$ which in turn lies on this plane. Thus the three points are solutions to the equation. Plugging in the values yields $d=12a=16b=\alpha c$ , and inserting these values for $a,b,c$ in terms of $d$ and simplifying yields $\frac{1}{12}x+\frac{1}{16}y+\frac{1}{\alpha}z=1$ . This is the equation of the plane.
By the formula , the value of $h$ (or the distance between $A$ and $\triangle BCD$ ) is equivalent to $\frac{1}{\sqrt{\frac{1}{12^2}+\frac{1}{16^2}+\frac{1}{\alpha^2}}}$ . Plugging this value in, we find that:
\[\frac{4}{5}\alpha=\frac{1}{\sqrt{\frac{1}{12^2}+\frac{1}{16^2}+\frac{1}{\alpha^2}}}\]
\[\sqrt{\frac{1}{12^2}+\frac{1}{16^2}+\frac{1}{\alpha^2}}=\frac{5}{4\alpha}\]
\[\frac{12^2+16^2}{12^2\cdot16^2}+\frac{1}{\alpha^2}=\frac{25}{16\alpha^2}\]
\[\frac{20^2}{192^2}=\frac{9}{16\alpha^2}\]
\[\frac{20}{192}=\frac{3}{4\alpha}\]
\[\alpha=\frac{3}{4}\cdot\frac{192}{20}=\frac{36}{5}\]
Thus the answer is $36+5=\boxed{041}$ .
~eevee9406
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .