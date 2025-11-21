# 2021 Fall AMC 10B Problem 11

## Problem

A regular hexagon of side length $1$ is inscribed in a circle. Each minor arc of the circle determined by a side of the hexagon is reflected over that side. What is the area of the region bounded by these $6$ reflected arcs?

$(\textbf{A})\: \frac{5\sqrt{3}}{2} - \pi\qquad(\textbf{B}) \: 3\sqrt{3}-\pi\qquad(\textbf{C}) \: 4\sqrt{3}-\frac{3\pi}{2}\qquad(\textbf{D}) \: \pi - \frac{\sqrt{3}}{2}\qquad(\textbf{E}) \: \frac{\pi + \sqrt{3}}{2}$

## Solution 1 (Best)
[asy] import olympiad; unitsize(50); pair A,B,C,D,E,F,O; A = origin; B = (-0.5,0.866025); C=(0,1.7320508); D=(1,1.7320508); E=(1.5,0.866025); F=(1,0); draw(A--B--C--D--E--F--cycle); draw(Circle((0.5,0.866025),1)); draw(A--D); draw(B--E); draw(C--F); [/asy]
This is the graph of the original Hexagon. After reflecting each minor arc over the sides of the hexagon it will look like this;
[asy] import olympiad; unitsize(50); pair A,B,C,D,E,F,O; A = origin; B = (-0.5,0.866025); C=(0,1.7320508); D=(1,1.7320508); E=(1.5,0.866025); F=(1,0); draw(A--B--C--D--E--F--cycle); draw(arc((0.5,2.598076), C, D)); draw(arc((2,1.7320508), D, E)); draw(arc((2,0), E, F)); draw(arc((0.5,-0.866025), F, A)); draw(arc((-1,0), A, B)); draw(arc((-1,1.7320508), B, C)); draw(A--D); draw(B--E); draw(C--F); [/asy]
This bounded region is the same as the area of the hexagon minus the area of each of the reflect arcs. From the first diagram, the area of each arc is the area of the $60^{\circ}$ sector minus the area of the equilateral triangle, so each arc has an area of $\frac{\pi r^2}{6} - \frac{s^2\sqrt{3}}{4} \implies \frac{\pi}{6} - \frac{\sqrt{3}}{4}$ .
There are 6 total arcs, so the total area of the arcs is $6\cdot (\frac{\pi}{6} - \frac{\sqrt{3}}{4}) = \pi - \frac{3\sqrt{3}}{2}$ .
The area of the hexagon is $6\cdot \frac{\sqrt{3}}{4} = \frac{3\sqrt{3}}{2}$ , so the area of the bounded region is: $\frac{3\sqrt{3}}{2} - (\pi - \frac{3\sqrt{3}}{2}) = 3\sqrt{3} - \pi = \boxed{B}$
~KingRavi

## Solution 2
Let the hexagon described be of area $H$ and let the circle's area be $C$ . Let the area we want to aim for be $A$ . Thus, we have that $C-H=H-A$ , or $A=2H-C$ . By some formulas, $C=\pi{r}^2=\pi$ and $H=6\cdot\frac12\cdot1\cdot(\frac12\cdot\sqrt3)=\frac{3\sqrt3}2$ . Thus, $A=3\sqrt3-\pi$ or $\boxed{(\textbf{B})}$ .
~Hefei417, or 陆畅 Sunny from China

## Solution 3
Denote by $O$ the center of this circle. Hence, the radius of this circle is 1. Denote this hexagon as $ABCDEF$ .
We have $\angle AOB = 60^\circ$ . Hence, the area of the region formed between segment $AB$ and the minor arc formed by $A$ and $B$ , denoted as $M$ , is \begin{align*} M & = \pi 1^2 \frac{60}{360} - \frac{\sqrt{3}}{4} 1^2 \\ & = \frac{\pi}{6} - \frac{\sqrt{3}}{4} . \end{align*}
Therefore, the area of the region that this problem asks us to compute is \begin{align*} \pi 1^2 - 12 M & = 3 \sqrt{3} - \pi . \end{align*}
Therefore, the answer is $\boxed{\textbf{(B) }3 \sqrt{3} - \pi}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 4
The area of the desired shape is equal to the $A($ whole hexagon $)-A($ Six arcs $).$
Since the arcs are reflected upon the sides of the hexagon, we can see that $A($ Six arcs $)=A($ Whole circle $)-A($ Whole hexagon $)$ .
The area of the circle is $\pi\cdot{1^2}$ , since the shape has side length $1$ and is inscribed within the circle (so its diameter is $2$ ).
Combining these two, we see that \[A(\text{Desired shape})=2A(\text{Hexagon})-A(\text{Circle}) \rightarrow\] \[A(\text{Desired shape})=2A(\text{Hexagon})-\pi.\] From here, three solutions can progress:

## Solution 4.1 (General polygons)
The area of a regular polygon is equal to $\frac{p\cdot{a}}{2}$ , where $p$ is the perimiter of the polygon, and $a$ is the length of its apothem.
The apothem is the distance from the center of the polygon to the midpoint of two adjacent vertices. If we were to create an equilateral triangle, whose base is at the side of the polygon, and its two sides meeting at the center, its height would be the apothem.
In this case, the side length of the hexagon is $1$ . We can now split this equlilateral into two congruent right triangles, who both have the apothem as a side. Each triangle has side lengths of $\frac{1}{2}$ ,half of the base, $1$ , the radius, and the apothem. By the pythagorean theorem, $1^2=(\frac{1}{2})^2+a^2$ , for the apothem $a$ . Solving yields $a=\frac{\sqrt{3}}{2}.$
Since $p=6$ , our formula becomes \[A=6(\frac{\sqrt{3}}{2})\cdot{\frac{1}{2}}=\frac{3\sqrt{3}}{2}.\]
Reall that the area of the figure is $2A(\text{Hexagon})-\pi.$ $2A=3\sqrt{3},$ so the sought area is $3\sqrt{3}-\pi$ , so our answer is $\boxed{\textbf{(B) }3 \sqrt{3} - \pi}$
Alternatively, we could find the length of the apothem by the formula $\frac{s}{2\text{tan}(\frac{180}{n})},$ where $s$ is the side length and $n$ is the number of sides.

## Solution 4.2 (Quick)
The area of a regular hexagon is given by the formula $\frac{3\sqrt{3}}{2}\cdot{s}$ , for the side length $s$ , which in this case, is $1$ , so the area of this hexagon is $\frac{3\sqrt{3}}{2}.$
We seek $2A(\text{Hexagon})-\pi,$ which is $\boxed{\textbf{(B) }3 \sqrt{3} - \pi}$
~Benedict T (countmath1)

## Solution 5
Use the diagrams provided in Solution $1$ .
The problem wants the area of the region bounded by the $6$ reflected arcs, a.k.a the area of the hexagon minus the area of the arcs drawn in the first figure. The area of those arcs can be calculated by taking the total area of the circle minus the total area of the hexagon.
In the end, we are looking for the value of the (area of the hexagon)-((area of the circle)-(area of the hexagon)).
The area of a hexagon with side length $1$ is $\frac{3\sqrt{3}}{2}$ . The area of a circle with radius $1$ is $\pi$ .
$\frac{3\sqrt{3}}{2}-(\pi-\frac{3\sqrt{3}}{2})=3\sqrt{3}-\pi$ .
The answer is $\boxed{\textbf{(B) }3\sqrt{3}-\pi}$ .
~avrilavigne

## Video Solution by Interstigation
https://youtu.be/xKlsLPzXsOM

## Video Solution
https://youtu.be/7AjnQPh9fU4
~Education, the Study of Everything

## Video Solution by WhyMath
https://youtu.be/KNvJV_FRPiE
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/R7TwXgAGYuw
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .