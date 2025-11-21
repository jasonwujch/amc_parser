# 2017 AMC 10B Problem 21

## Problem

In $\triangle ABC$ , $AB=6$ , $AC=8$ , $BC=10$ , and $D$ is the midpoint of $\overline{BC}$ . What is the sum of the radii of the circles inscribed in $\triangle ADB$ and $\triangle ADC$ ?

$\textbf{(A)}\ \sqrt{5}\qquad\textbf{(B)}\ \frac{11}{4}\qquad\textbf{(C)}\ 2\sqrt{2}\qquad\textbf{(D)}\ \frac{17}{6}\qquad\textbf{(E)}\ 3$

## Solution 1
We note that by the converse of the Pythagorean Theorem, $\triangle ABC$ is a right triangle with a right angle at $A$ . Also, the median to the hypotenuse will be half of the hypotenuse. Therefore, $AD = BD = CD = 5$ , and $[ADB] = [ADC] = 12$ . Since $A = rs,$ we have $r = \frac As$ , so the inradius of $\triangle ADB$ is $\frac{12}{(5+5+6)/2} = \frac 32$ , and the inradius of $\triangle ADC$ is $\frac{12}{(5+5+8)/2} = \frac 43$ . Adding the two together, we have $\boxed{\textbf{(D) } \frac{17}6}$ .

## Solution 2
We have [asy] draw((0,0)--(8,0)); draw((0,0)--(0,6)); draw((8,0)--(0,6)); draw((0,0)--(4,3)); label("A",(0,0),W); label("B",(0,6),N); label("C",(8,0),E); label("D",(4,3),NE); label("H",(2.3,4.2),NE); label("K",(2.3,1.8),S); draw(circle((1.54,3),1.49)); draw(circle((4,1.35),1.33)); dot((4,1.35)); dot((1.54,3)); label("F",(1.54,3),S); label("J",(4,1.35),SW); label("G",(0,3),W); label("$x$",(1,3),S); label("$y$",(4,1),E); draw((1.54,3)--(0,3)); draw((1.54,3)--(2.3,1.8)); draw((1.54,3)--(2.3,4.2)); draw((4,1.35)--(4,0)); draw((4,1.35)--(3.12,2.4)); draw((4,1.35)--(4.8,2.3)); label("L",(4.9,2.4),NE); label("E",(3.11,2.3),S); label("I",(4,0),S); [/asy] Let $x$ be the radius of circle $F$ , and let $y$ be the radius of circle $J$ . We want to find $x+y$ .
We form 6 kites: $GAKF$ , $HFKD$ , $GFHB$ , $EJIA$ , $LJIC$ , and $JEDL$ . Since $G$ and $I$ are the midpoints of $\overline{AB}$ and $\overline{AC}$ , respectively, this means that $BG = AG = \frac{6}{2} = 3$ , and $AI = IC = \frac{8}{2} = 4$ .
Since $AGFK$ is a kite, $GF = FK = x$ , and $AG = AK = 3$ . The same applies to all kites in the diagram.
Now, we see that $AK = 3$ , and $KD = 2$ , thus $AD$ is $5$ , making $\triangle ADC$ and $\triangle ABD$ isosceles. So, $DI=3$ using the Pythagorean Theorem, and $GD=4$ also using the Theorem. Hence, we know that $[ADC] = [ABD] = 12$ .
Notice that the area of the kite (if the $2$ opposite angles are right) is $\frac{s_1 \cdot s_2}{2} \cdot 2$ , where $s_1$ and $s_2$ denoting each of the 2 congruent sides. This just simplifies to $s_1 \cdot s_2$ . Hence, we have
\[4b+4b+b = 12\]
and
\[3a+3a+2a = 12\]
Solving for $a$ and $b$ , we find that $a = \frac{3}{2}$ and $b = \frac{4}{3}$ , so $a+b = \frac{3}{2} + \frac {4}{3} = \boxed{\textbf{(D)} ~\frac{17}6}$ .
~MrThinker

## Solution 3 (Stewart's)
Applying [1] gives us the length of $\overline{AD}.$ Using that length, we can find the areas of triangles $\triangle ABD$ and $\triangle ACD$ by using Heron’s formula. We can use that area to find the inradius of the circles by the inradius formula $A=sr.$ Therefore, we get $\boxed{\textbf{(D) }\frac{17}{6}}.$ Although this solution works perfectly fine, it takes time and has room for error so apply Stewart’s and Heron’s with caution.
~peelybonehead
Edited by ~Jadon_Jung

## Solution 4 (using Shoelace and general inradius)
First, start by plotting $\triangle{ABC}$ on a grid; with B at (0,0), D at (5,0), and C at (10,0).
We can now solve for the position of point A. Let point A be (a,b). We can then set up the equation a^2 + b^2 = 36 and the equation (10-a)^2 + b^2 = 64. Solving for a and b, we get that a = $\frac{18}{5}$ and b = $\frac{24}{5}$ . We can then go ahead and use the Shoelace method to get the area of $\triangle{ABD}$ , which ends up being 12. Since D is the midpoint of BC, $\triangle{ABD}$ and $\triangle{ACD}$ have the same area.
Using the distance formula once again, AD has length 5, and now we can get the semiperimeter of $\triangle{ABD}$ and $\triangle{ACD}$ , which turns out to be 8 for $\triangle{ABD}$ and 9 for $\triangle{ACD}$ . Dividing Area by Semiperimeter and adding them, we get $\frac{3}{2}$ + $\frac{4}{3}$ = $\boxed{\textbf{(D) }\frac{17}{6}}.$
~BanSpeedrun

## Video Solution
https://youtu.be/EfKFDwTDRjs
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .