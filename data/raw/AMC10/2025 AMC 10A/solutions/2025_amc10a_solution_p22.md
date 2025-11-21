# 2025 AMC 10A Problem 22

## Problem

A circle of radius $r$ is surrounded by three circles, whose radii are 1, 2, and 3, all externally tangent to the inner circle and externally tangent to each other, as shown in the diagram below.

[asy] import olympiad; size(260); // radii (outer ones specified: 1,2,3; inner r0 = 6/23) real r0 = 6/23.0; real r1 = 1.0; real r2 = 2.0; real r3 = 3.0; // distances from origin real d1 = r0 + r1; real d2 = r0 + r2; real d3 = r0 + r3; // angles found numerically (radians) real t1 = 0; real t2 = 1.9857887796653; real t3 = -2.0480149718113; // centers pair O = (0,0); pair C1 = d1*dir(degrees(t1)); pair C2 = d2*dir(degrees(t2)); pair C3 = d3*dir(degrees(t3)); // draw the circles draw(circle(O, r0), black+0.9); draw(circle(C1, r1), black+0.9); draw(circle(C2, r2), black+0.9); draw(circle(C3, r3), black+0.9); // tight crop, no box currentpicture.fit(); [/asy]

What is $r$ ?

$\textbf{(A) }\frac{1}{4}\qquad\textbf{(B) }\frac{6}{23}\qquad\textbf{(C) }\frac{3}{11}\qquad\textbf{(D) }\frac{5}{17}\qquad\textbf{(E) }\frac{3}{10}$

1 Diagram

- 1 Diagram

- 2 Solution 1

- 3 Solution 2 (Descartes’ Theorem, Detailed Derivation)

- 4 Solution 3(Heron's)

- 5 Solution 4 (Variation of Solution 3)

- 6 Solution 5 (Coordinate Geometry)

- 7 A note about factoring

- 8 Solution 6 (Trig, LoC)

- 9 Video Solution 1 by OmegaLearn.org

- 10 Video Solution (In 3 Mins)

- 11 Video Solution

- 12 Video Solution

- 13 Video Solution by SpreadTheMathLove

- 14 See Also

### Diagram

[asy] import olympiad; size(260); // radii (outer ones specified: 1,2,3; inner r0 = 6/23) real r0 = 6/23.0; real r1 = 1.0; real r2 = 2.0; real r3 = 3.0; // distances from origin real d1 = r0 + r1; real d2 = r0 + r2; real d3 = r0 + r3; // angles found numerically (radians) real t1 = 0; real t2 = 1.9857887796653; real t3 = -2.0480149718113; // centers pair O = (0,0); pair C1 = d1*dir(degrees(t1)); pair C2 = d2*dir(degrees(t2)); pair C3 = d3*dir(degrees(t3)); // draw the circles draw(circle(O, r0), black+0.9); draw(circle(C1, r1), black+0.9); draw(circle(C2, r2), black+0.9); draw(circle(C3, r3), black+0.9); // tight crop, no box currentpicture.fit(); [/asy] ~Avs2010

## Solution 1
Descartes' Circle Formula (curvatures $k_i = \frac{1}{r_i}$ ) \[k_4 = k_1 + k_2 + k_3 \pm 2\sqrt{k_1k_2 + k_2k_3 + k_3k_1}.\]
For radii 1, 2, 3 we have \[k_1 = 1,\quad k_2 = \frac{1}{2},\quad k_3 = \frac{1}{3}.\]
Compute the sum and the square-root term \[k_1+k_2+k_3 = \frac{11}{6},\qquad k_1k_2+k_2k_3+k_3k_1 = 1.\]
Therefore \[k_4 = \frac{11}{6} \pm 2.\]
Choose the plus sign for the small circle tangent externally to the three given circles \[k_4 = \frac{11}{6} + 2 = \frac{23}{6}, \qquad r_4 = \frac{1}{k_4} = \boxed{\textbf{(B) }\frac{6}{23}}.\] ~Jonathanmo

## Solution 2 (Descartes’ Theorem, Detailed Derivation)
We are given the radii of three circles and are asked to find an external tangent to the radius of the circle.
We can use Descartes’ Theorem to find it using curvatures (reciprocals of the radii). The curvatures are \[k_1 = 1, \quad k_2 = \tfrac{1}{2}, \quad k_3 = \tfrac{1}{3}.\]
Descartes' Circle Formula states \[(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2).\]
Plugging in, we get \[\left(1 + \tfrac{1}{2} + \tfrac{1}{3} + k_4\right)^2 = 2\left(1 + \tfrac{1}{4} + \tfrac{1}{9} + k_4^2\right).\]
Simplifying, \[\left(\tfrac{11}{6} + k_4\right)^2 = 2\left(\tfrac{49}{36} + k_4^2\right).\] \[\tfrac{121}{36} + \tfrac{11}{3}k_4 + k_4^2 = \tfrac{49}{18} + 2k_4^2.\] \[k_4^2 - \tfrac{11}{3}k_4 - \tfrac{23}{36} = 0.\]
Using the quadratic formula, \[k_4 = \frac{\tfrac{11}{3} \pm \sqrt{\tfrac{121}{9} - (-\tfrac{23}{9})}}{2} = \frac{\tfrac{11}{3} \pm \sqrt{\tfrac{144}{9}}}{2} = \frac{\tfrac{11}{3} \pm \tfrac{12}{3}}{2} = \tfrac{23}{6}, -\tfrac{1}{6}.\]
Since the curvature is the reciprocal of the radius, the two tangent circles possible are \[r = \frac{1}{|k_4|} = \frac{6}{23} \text{ and } 6.\]
The circle with radius 6 is the one that contains all of the three tangent circles inside it, so the answer is \[\boxed{(B)\ \tfrac{6}{23}}.\]
Note: Instead of solving the quadratic directly, we can multiply it by $36$ and then use the rational root theorem to note that the solution must have a numerator of either $1$ or $23$ , meaning that the denominator of the radius must be $1$ or $23$ . It can't be $1$ , since then the radius would be greater than $1$ (which is impossible, looking at answer choices), so the denominator is $23$ , and there is only one answer choice whose denominator is $23$ , $\boxed{(B)\ \tfrac{6}{23}}$
~AlgeBruh16 ~Minor LaTeX fix by scjh999999 ~Minor edit by S3yurek ~Note by ZingiberiMaracandae

## Solution 3(Heron's)
Let the center of the circle radius 2 be $A$ , radius 1 be $B$ , radius 3 be $C$ . Let the unknown circle's center be $P$ and radius be $r$ .
We know $\overline{AB}=2+1=3, \overline{AC}=3+2=5, \overline{BC}=1+3=4.$
Thus, $\triangle ABC$ is a 3-4-5 triangle, where $\angle B=90^\circ$ .
Let $X,Y$ be on $\overline{AB},\overline{BC}$ respectively such that $\angle{PXB}=\angle{PYB}=90^\circ$ .
By Heron's formula, the area of $\triangle BPC$ is \[\sqrt{s(s-\overline{BP})(s-\overline{CP})(s-\overline{BC})}=\sqrt{(4+r)\cdot 1\cdot 3\cdot r}=\sqrt{3r^2+12r}.\] By using the simpler area formula, we can find $\overline{PY}$ . \[\overline{PY}=\frac{[BPC]}{\overline{BC}/2}=\frac{\sqrt{3r^2+12r}}{2}.\]
Since $\angle{PXB}=\angle{B}=\angle{PYB}=90^\circ$ , $XPYB$ is a rectangle, and we can say \[\overline{PX}^2=\overline{BP}^2-\overline{PY}^2,\] or \[\overline{PX}^2=(1+r)^2-\frac{3r^2+12r}{4}=\frac{r^2-4r+4}{4}\]
\[\Rightarrow \overline{PX}=\frac{|r-2|}{2}.\]
We then find the area of $ABP$ via Heron's formula, and again, by the simple area formula we have that \[\overline{PX}=\frac{[ABP]}{\overline{AB}/2}=\frac{2\sqrt{2r^2+6r}}{3}\]
Now we can equate the two and solve the equation:
\begin{align*} \frac{|r-2|}{2}&=\frac{2\sqrt{2r^2+6r}}{3} \\ \Rightarrow 3(|r-2|)&=4\sqrt{2r^2+6r} \\ \Rightarrow 9r^2-36r+36&=32r^2+96r \\ \Rightarrow 23r^2+132r-36&=0 \end{align*}
Utilizing the quadratic formula, the only positive root is $r=\frac{6}{23}=\boxed{B}.$
Note: By the rational root theorem, a rational root of the final quadratic must have denominator $1$ or $23$ in simplest form, which eliminates all choices except B.
~bluedolphin36,eggon ~aldzandrtc(minor edit, added logical steps)
Edited by GarudS

## Solution 4 (Variation of Solution 3)
Follow the same starting steps as solution 3 (drawing right triangle ABC connecting the centers of the three larger circles and connecting points A, B, and C to the center of the smaller circle). Using Heron's formula, we can easily find the areas of the three smaller triangles that make up triangle ABC in terms of $r$ . Since the sum of these terms is an integer, or 6, we can theorize that the square roots have to simplify out into rational numbers. Out of all the answer choices, $\boxed{(B)}$ , or $\dfrac{6}{23}$ , is the only one that works. (will add more later)
~stjwyl

## Solution 5 (Coordinate Geometry)
Let the center of the circle radius 2 be $A$ , radius 1 be $B$ , radius 3 be $C$ . Let the unknown circle's center be $P$ . Since $AB^2+BC^2=AC^2$ , $\triangle ABC$ is a right triangle, with right angle at $B$ . Let $B=(0, 0), A=(3, 0), C=(0, 4),$ and $P=(x, y)$ . Since the large circles are tangent to the small one, we have, if the radius of the smallest circle is $r$ , \[x^2+y^2 = (r+1)^2 = r^2+2r+1 \\\] \[(x-3)^2+y^2 = (r+2)^2 = r^2+4r+4 \\\] \[x^2+(y-4)^2 = (r+3)^2 = r^2+6r+9\] Subtracting (1) from (2) and (1) from (3), we get \[-6x+9=2r+3 \implies -3x=r-3\\\] \[-8y+16=4r+8 \implies -2y=r-2\] To avoid fractions, we multiply (1) to get $36r^2+72r+36=36x^2+36y^2=4(r-3)^2+9(r-2)^2 = 13r^2-60r+72$ . Combining like terms, we have $23r^2+132r-36$ . Solving via quadratic formula, we get $\boxed{\frac{6}{23}}$ .
Note: Like the last solution, you can just notice that $B$ is the only answer choice with 23 in the denominator.
### A note about factoring
You don't need to save a lot of time by abusing multiple choice to cheese the root of $23r^2+132r-36$ .
$23r^2+132r-36$ = $(Ax+B)(Cx+D)$ . Since $23$ is prime, $B=1$ and $D=23$ , WLOG.
Theorem you can prove and learn: in $Px^2 + Qx + R = (Ax+B)(Cx+D)$ : if $n \vert Q$ and $n^2 \vert R$ , then $n\vert C$ and $n \vert D$ . (This is equivalent to substituting $y=x/n$ .) Symmetrically, if $n \vert Q$ and $n^2 \vert P$ , then $n\vert A$ and $n \vert B$ . (This is equivalent to substituting $y=nx$ .)
Back to our problem: Since $6 \vert 132$ and $6^2 \vert 36$ , then $6 \vert A$ and $6 \vert B$ . $6 \cdot 6 =36$ so the factoring is done, up to placing the minus sign: $(23r-6)(r+6)$ .
Considering the signed-distance geometry of the original equations in $r$ , the positive root $\boxed{6/23}$ is the internally tangent circle's radius, and the absolute value $6$ of negative root $-6$ is the externally tangent circle's radius.
~oinava

## Solution 6 (Trig, LoC)
Start with the same setup as Solution 3. Now, set $\angle PBC$ as $\theta$ . Law of Cosine on $\triangle PBC$ , you get:
\[\cos(\theta )=\frac{PC^2-PB^2-BC^2}{2\cdot PB\cdot BC}\]
\[=\frac{(3+r)^2-(1+r)^2-16}{8+8r}\]
\[=\frac{r-2}{2+2r}\]
Similarly, use LoC on $\triangle APB$ :
\[\cos(90^\circ -\theta )=\sin(\theta )=\frac{PA^2-PB^2-AB^2}{2\cdot PB\cdot AB}\]
\[=\frac{(2+r)^2-(1+r)^2-9}{6+6r}\]
\[=\frac{r-3}{3+3r}\]
Now, Pythagorean Identity,
\[\sin ^2(\theta)+\cos ^2(\theta)=1\]
\[\Rightarrow \left( \frac{r-2}{2+2r}\right) ^2+\left( \frac{r-3}{3+3r}\right) ^2=1\]
\[\Rightarrow \frac{13r^2-60r+72}{36x^2+72x+36}=1\]
\[\Rightarrow 23r^2+132x-36=0\]
Solving, you get $r=\boxed{\frac{6}{23}}$ .
~Bluedolphin36

## Video Solution 1 by OmegaLearn.org
https://youtu.be/XlnZptQumSo

## Video Solution (In 3 Mins)
https://youtu.be/BD-AUw_m65U?si=f8deq2OpR5LdOpr9 ~ Pi Academy

## Video Solution
https://www.youtube.com/watch?v=OGr0NVDt9lI ~ ABIRGH
- This video was posted 2 years ago as an explanation of Descartes' theorem, and it was coincidentally used on the test. There were no known leaks.

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .