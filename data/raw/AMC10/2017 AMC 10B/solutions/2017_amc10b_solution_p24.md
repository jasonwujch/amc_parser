# 2017 AMC 10B Problem 24

## Problem

The vertices of an equilateral triangle lie on the hyperbola $xy=1$ , and a vertex of this hyperbola is the centroid of the triangle. What is the square of the area of the triangle?

$\textbf{(A)}\ 48\qquad\textbf{(B)}\ 60\qquad\textbf{(C)}\ 108\qquad\textbf{(D)}\ 120\qquad\textbf{(E)}\ 169$

### Diagram

[asy] size(15cm); Label f; f.p=fontsize(6); xaxis(-8,8,Ticks(f, 2.0)); yaxis(-8,8,Ticks(f, 2.0)); real f(real x) { return 1/x; } draw(graph(f,-8,-0.125)); draw(graph(f,0.125,8)); [/asy]

## Solution 1 (Law of Cosines)
WLOG, let the centroid of $\triangle ABC$ be $I = (-1,-1)$ . The centroid of an equilateral triangle is the same as the circumcenter. It follows that the circumcircle must intersect the graph exactly three times. Therefore, $A = (1,1)$ , so $AI = BI = CI = 2\sqrt{2}$ , so since $\triangle AIB$ is isosceles and $\angle AIB = 120^{\circ}$ , then by the Law of Cosines , $AB = 2\sqrt{6}$ . Alternatively, we can use the fact that the circumradius of an equilateral triangle is equal to $\frac {s}{\sqrt{3}}$ . Therefore, the area of the triangle is $\frac{(2\sqrt{6})^2\sqrt{3}}4 = 6\sqrt{3}$ , so the square of the area of the triangle is $\boxed{\textbf{(C) } 108}$ .
Note: We could’ve also noticed that the centroid divides the median into segments of ratio $2:1.$ ~peelybonehead

## Solution 2
WLOG, let the centroid of $\triangle ABC$ be $G = (-1,-1)$ . Then, one of the vertices must be the other curve of the hyperbola. WLOG, let $A = (1,1)$ . Then, point $B$ must be the reflection of $C$ across the line $y=x$ , so let $B = \left(a,\frac{1}{a}\right)$ and $C=\left(\frac{1}{a},a\right)$ , where $a <-1$ . Because $G$ is the centroid, the average of the $x$ -coordinates of the vertices of the triangle is $-1$ . So we know that $a + 1/a+ 1 = -3$ . Multiplying by $a$ and solving gives us $a=-2-\sqrt{3}$ . So $B=(-2-\sqrt{3},-2+\sqrt{3})$ and $C=(-2+\sqrt{3},-2-\sqrt{3})$ . So $BC=2\sqrt{6}$ , and finding the square of the area gives us $\boxed{\textbf{(C) } 108}$ . $\newline$ Alternatively, from $a + \frac{1}{a} = -4$ , we obtain $a^2 - 2 + \frac{1}{a^2} = (-4)^2 - 4 \implies \left|a - \frac{1}{a} \right| = \sqrt{12}$ . Since $BC$ lies on the line $x + y = -4$ , which forms an isosceles right triangle with the coordinate axes, $BC = \sqrt{12} \sqrt{2} = \sqrt{24}$ . Hence the squared area is $\left(\frac{\sqrt{3}}{4} s^2 \right)^2 = \frac{3}{16} \cdot 24^2 = \boxed{108}$ .

## Solution 3
Without loss of generality, let the centroid of $\triangle ABC$ be $G = (1, 1)$ and let point $A$ be $(-1, -1)$ . It is known that the centroid is equidistant from the three vertices of $\triangle ABC$ . Because we have the coordinates of both $A$ and $G$ , we know that the distance from $G$ to any vertex of $\triangle ABC$ is $\sqrt{(1-(-1))^2+(1-(-1))^2} = 2\sqrt{2}$ . Therefore, $AG=BG=CG=2\sqrt{2}$ . It follows that from $\triangle ABG$ , where $AG=BG=2\sqrt{2}$ and $\angle AGB = \dfrac{360^{\circ}}{3} = 120^{\circ}$ , $[\triangle ABG]= \dfrac{(2\sqrt{2})^2 \cdot \sin(120)}{2} = 4 \cdot \dfrac{\sqrt{3}}{2} = 2\sqrt{3}$ using the formula for the area of a triangle with sine $\left([\triangle ABC]= \dfrac{1}{2} AB \cdot BC \sin(\angle ABC)\right)$ . Because $\triangle ACG$ and $\triangle BCG$ are congruent to $\triangle ABG$ , they also have an area of $2\sqrt{3}$ . Therefore, $[\triangle ABC] = 3(2\sqrt{3}) = 6\sqrt{3}$ . Squaring that gives us the answer of $\boxed{\textbf{(C) }108}$ .

## Solution 4
Without loss of generality, let the centroid of $\triangle ABC$ be $G = (1, 1)$ . Assuming we don't know one vertex is $(-1, -1)$ we let the vertices be $A\left(x_1, \frac{1}{x_1}\right), B\left(x_2, \frac{1}{x_2}\right), C\left(x_3, \frac{1}{x_3}\right).$
Since the centroid coordinates are the average of the vertex coordinates, we have that $\frac{x_1+x_2+x_3}{3}=1$ and $\frac{\frac{1}{x_1}+\frac{1}{x_2}+\frac{1}{x_3}}{3}=1.$
We also know that the centroid is the orthocenter in an equilateral triangle, so $CG \perp AB.$ Examining slopes, we simplify the equation to $x_1x_2x_3 = -1$ . From the equation $\frac{\frac{1}{x_1}+\frac{1}{x_2}+\frac{1}{x_3}}{3}=1,$ we get that $x_1x_2+x_1x_3+x_2x_3 = -3$ . These equations are starting to resemble Vieta's:
$x_1+x_2+x_3=3$
$x_1x_2+x_1x_3+x_2x_3 = -3$
$x_1x_2x_3=-1$
$x_1,x_2,x_3$ are the roots of the equation $x^3 - 3x^2 - 3x + 1 = 0$ . This factors as $(x+1)(x^2-4x+1)=0 \implies x = -1, 2 \pm \sqrt3,$ for the points $(-1, -1), (2+\sqrt3, 2-\sqrt3), (2-\sqrt3, 2+\sqrt3)$ . The side length is clearly $\sqrt{24}$ , so the square of the area is $\boxed{108}.$
$\sim\textbf{Leonard\_my\_dude}\sim$

## Solution 5 (kinda sketchy but also fast)
WLOG, assume that the centroid is $G = (-1, -1)$ . We can *intuitively* see that the equilateral triangle must have a vertex at $A = (1, 1)$ , the other vertex of the hyperbola. Thus, $AG = 2\sqrt{2}$ . If the other two vertices of the equilateral triangle are $B$ and $C$ , then we can see that $\triangle{}AGB$ is a $120-30-30$ triangle, and thus $s = AB = AG\sqrt{3} = 2\sqrt{6},$ where $s$ is the side length of $\triangle{}ABC$ . Thus, $[\triangle{}ABC]^2 = \left(\frac{s^2\sqrt{3}}{4}\right)^2 = (6\sqrt{3})^2 = \boxed{\textbf{(C) } 108}$ . ~PojoDotCom
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .