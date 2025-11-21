# 2017 AMC 8 Problem 22

## Problem

In the right triangle $ABC$ , $AC=12$ , $BC=5$ , and angle $C$ is a right angle. A semicircle is inscribed in the triangle as shown. What is the radius of the semicircle?

[asy] draw((0,0)--(12,0)--(12,5)--(0,0)); draw(arc((8.67,0),(12,0),(5.33,0))); label("$A$", (0,0), W); label("$C$", (12,0), E); label("$B$", (12,5), NE); label("$12$", (6, 0), S); label("$5$", (12, 2.5), E);[/asy]

$\textbf{(A) }\frac{7}{6}\qquad\textbf{(B) }\frac{13}{5}\qquad\textbf{(C) }\frac{59}{18}\qquad\textbf{(D) }\frac{10}{3}\qquad\textbf{(E) }\frac{60}{13}$

## Solution 1 (Pythagorean Theorem)
We can draw another radius from the center to the point of tangency. This angle, $\angle{ODB}$ , is $90^\circ$ . Label the center $O$ , the point of tangency $D$ , and the radius $r$ . [asy] draw((0,0)--(12,0)--(12,5)--(0,0)); draw(arc((8.67,0),(12,0),(5.33,0))); label("$A$", (0,0), W); label("$C$", (12,0), E); label("$B$", (12,5), NE); label("$12$", (6, 0), S); label("$5$", (12, 2.5), E); draw((8.665,0)--(7.4,3.07)); label("$O$", (8.665, 0), S); label("$D$", (7.4, 3.1), NW); label("$r$", (11, 0), S); label("$r$", (7.6, 1), W); [/asy]
Since $ODBC$ is a kite, then $DB=CB=5$ . Also, $AD=13-5=8$ . By the Pythagorean Theorem , $r^2 + 8^2=(12-r)^2$ . Solving, $r^2+64=144-24r+r^2 \Rightarrow 24r=80 \Rightarrow \boxed{\textbf{(D) }\frac{10}{3}}$ .
~MrThinker

## Solution 2 (Basic Trigonometry)
If we reflect triangle $ABC$ over line $AC$ , we will get isosceles triangle $ABD$ . By the Pythagorean Theorem , we are capable of finding out that the $AB = AD = 13$ . Hence, $\tan \frac{\angle BAD}{2} = \tan \angle BAC = \frac{5}{12}$ . Therefore, as of triangle $ABD$ , the radius of its inscribed circle $r = \frac{tan \frac{\angle BAD}{2}\cdot (AB + AD - BD)}{2} = \frac{\frac{5}{12} \cdot 16}{2} = \boxed{\textbf{(D) }\frac{10}{3}}$
~ Bloggish

## Solution 3
Like solution 2, we reflect $\triangle ABC$ over line $\overline{AC}$ and label the reflection of point $B$ as $D$ . As $AB = AD = 13$ by the Pythagorean Theorem, we use the formula $rs=A$ , where $r$ is the inradius (what we're trying to find), $s$ is the semiperimeter ( $\frac{\overline{AB}+\overline{AD}+\overline{BD}}{2}$ ), and $A$ is the area of the triangle in which the incircle is inscribed in. Substitution gives: \[r=\frac{\frac{10\cdot12}{2}}{\frac{13+13+10}{2}}\] \[r=\frac{60}{18}\] \[r=\boxed{\textbf{(D) }\frac{10}{3}}\]
~megaboy6679

## Video Solution by Pi Academy (Fast and Easy!)
https://youtu.be/qZJNi-WM0XY?si=AL2FANuanWBAQu17
~ Pi Academy

## Video Solution
https://youtu.be/KtmLUlCpj-I
- savannahsolver

## Video Solution
https://www.youtube.com/watch?v=sOF1Okc0jMc
### See Also