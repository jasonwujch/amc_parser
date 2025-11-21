# 2001 AIME I Problem 5

## Problem

An equilateral triangle is inscribed in the ellipse whose equation is $x^2+4y^2=4$ . One vertex of the triangle is $(0,1)$ , one altitude is contained in the y-axis, and the square of the length of each side is $\sqrt{\frac{m}{n}}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4 2.5 Solution 5 2.6 Solution 6

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

- 2.5 Solution 5

- 2.6 Solution 6

## Solution

## Solution 1
Denote the vertices of the triangle $A,B,$ and $C,$ where $B$ is in quadrant 4 and $C$ is in quadrant $3.$
Note that the slope of $\overline{AC}$ is $\tan 60^\circ = \sqrt {3}.$ Hence, the equation of the line containing $\overline{AC}$ is \[y = x\sqrt {3} + 1.\] This will intersect the ellipse when \begin{eqnarray*}4 = x^{2} + 4y^{2} & = & x^{2} + 4(x\sqrt {3} + 1)^{2} \\ & = & x^{2} + 4(3x^{2} + 2x\sqrt {3} + 1) \implies x(13x+8\sqrt 3)=0\implies x = \frac { - 8\sqrt {3}}{13}. \end{eqnarray*} We ignore the $x=0$ solution because it is not in quadrant 3.
Since the triangle is symmetric with respect to the y-axis, the coordinates of $B$ and $C$ are now $\left(\frac {8\sqrt {3}}{13},y_{0}\right)$ and $\left(\frac { - 8\sqrt {3}}{13},y_{0}\right),$ respectively, for some value of $y_{0}.$
It is clear that the value of $y_{0}$ is irrelevant to the length of $BC$ . Our answer is \[BC = 2 \cdot \frac {8\sqrt {3}}{13}=\sqrt {4\left(\frac {8\sqrt {3}}{13}\right)^{2}} = \sqrt {\frac {768}{169}}\implies m + n = \boxed{937}.\]

## Solution 2
Solving for $y$ in terms of $x$ gives $y=\sqrt{4-x^2}/2$ , so the two other points of the triangle are $(x,\sqrt{4-x^2}/2)$ and $(-x,\sqrt{4-x^2}/2)$ , which are a distance of $2x$ apart. Thus $2x$ equals the distance between $(x,\sqrt{4-x^2}/2)$ and $(0,1)$ , so by the distance formula we have
\[2x=\sqrt{x^2+(1-\sqrt{4-x^2}/2)^2}.\]
Squaring both sides and simplifying through algebra yields $x^2=192/169$ , so $2x=\sqrt{768/169}$ and the answer is $\boxed{937}$ .

## Solution 3
Since the altitude goes along the $y$ axis, this means that the base is a horizontal line, which means that the endpoints of the base are $(x,y)$ and $(-x,y)$ , and WLOG, we can say that $x$ is positive.
Now, since all sides of an equilateral triangle are the same, we can do this (distance from one of the endpoints of the base to the vertex and the length of the base):
$\sqrt{x^2 + (y-1)^2} = 2x$
Square both sides,
$x^2 + (y-1)^2 = 4x^2\implies (y-1)^2 = 3x^2$
Now, with the equation of the ellipse: $x^2 + 4y^2 = 4$
$x^2 = 4-4y^2$
$3x^2 = 12-12y^2$
Substituting,
$12-12y^2 = y^2 - 2y +1$
Moving stuff around and solving:
$y = \frac{-11}{13}, 1$
The second is found to be extraneous, so, when we go back and figure out $x$ and then $2x$ (which is the side length), we find it to be:
$\sqrt{\frac{768}{169}}$
and so we get the desired answer of $\boxed{937}$ .

## Solution 4
Denote $(0,1)$ as vertex $A,$ $B$ as the vertex to the left of the $y$ -axis and $C$ as the vertex to the right of the $y$ -axis. Let $D$ be the intersection of $BC$ and the $y$ -axis.
Let $x_0$ be the $x$ -coordinate of $C.$ This implies \[C=\left(x_0 , \sqrt{\frac{4-x_0^2}{4}}\right)\] and \[B=\left(-x_0 , \sqrt{\frac{4-x_0^2}{4}}\right).\] Note that $BC=2x_0$ and \[\frac{BC}{\sqrt3}=AD=1-\sqrt{\frac{4-x_0^2}{4}}.\] This yields \[\frac{2x_0}{\sqrt3}=1-\sqrt{\frac{4-x_0^2}{4}}.\] Re-arranging and squaring, we have \[\frac{4-x_0^2}{4}=\frac{4x_0^2}{3}-\frac{4x_0}{\sqrt3} +1.\] Simplifying and solving for $x_0$ , we have \[x_0=\frac{48}{13\sqrt 3}.\] As the length of each side is $2x_0,$ our desired length is \[4x_0^2=\frac{768}{169}\] which means our desired answer is \[768+169=\boxed{937}\]
~ASAB

## Solution 5
Notice that $x^2+4y^2=4$ can be rewritten as $(x)^2+(2y)^2=2^2$ . The points of the triangle are $(0, 1)$ , $(-x, 1-x\sqrt{3})$ , and $(x, 1-x\sqrt{3})$ . When plugging the second coordinate into the equation, we get $x^2+4-8x\sqrt{3}+12x^2=4$ , which equals $13x^2-8x\sqrt{3}=0$ . This yields $x(13x-8\sqrt{3})=0$ . Obviously x can't be 0, so $x=\frac{8\sqrt{3}}{13}$ . The side length of the equilateral triangle is twice of this, so $\frac{16\sqrt{3}}{13}$ . This can be rewritten as $\sqrt{\frac{256\cdot3}{169}}=\sqrt{\frac{768}{169}}$ . $768+169=\boxed{937}$ . ~ MC413551

## Solution 6
Consider the transformation $(x,y)$ to $(x/2, y).$ This sends the ellipse to the unit circle. If we let $n$ be one-fourth of the side length of the triangle, the equilateral triangle is sent to an isosceles triangle with side lengths $2n, n\sqrt{13}, n\sqrt{13}.$ Let the triangle be $ABC$ such that $AB=AC.$ Let the foot of the altitude from A be $X.$ Then $BX=n,$ and $AX=2n\sqrt{3}.$ Let $C$ be a point such that $AC$ is a diameter of the unit circle. Then $XC=2-2n\sqrt{3}.$ Using power of a point on X, \[n^2=2n\sqrt{3}(2-2n\sqrt{3})\] Simplifying gets us to $13n^2=4n\sqrt{3}.$ Then, $n=\dfrac{4\sqrt{3}}{13}$ which means the side length is $\dfrac{16\sqrt{3}}{13}=\sqrt{\dfrac{768}{169}}.$ Thus, the answer is $768+169=\boxed{937}.$
These problems are copyrighted © by the Mathematical Association of America.