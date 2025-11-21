# 2021 AIME I Problem 15

## Problem

Let $S$ be the set of positive integers $k$ such that the two parabolas \[y=x^2-k~~\text{and}~~x=2(y-20)^2-k\] intersect in four distinct points, and these four points lie on a circle with radius at most $21$ . Find the sum of the least element of $S$ and the greatest element of $S$ .

### Diagram

Graph in Desmos: https://www.desmos.com/calculator/37hsgxbygj

~MRENTHUSIASM

## Solution 1 (Inequalities and Circles)
Note that $y=x^2-k$ is an upward-opening parabola with the vertex at $(0,-k),$ and $x=2(y-20)^2-k$ is a rightward-opening parabola with the vertex at $(-k,20).$ We consider each condition separately:
1. The two parabolas intersect at four distinct points.
1. The four points of intersection lie on a circle with radius at most $21.$ For equations of circles, the coefficients of and must be the same. So, we add the equation to half the equation We expand, rearrange, and complete the squares: We need from which For Condition 2, we obtain
1. The point $(-k,20)$ is on or below the parabola $y=x^2-k.$ We need from which Moreover, the point is on the parabola when We will prove that the two parabolas intersect at four distinct points at this value of Substituting into we get Expanding and rearranging give By either the graphs of the parabolas or the Rational Root Theorem, we conclude that is a root of So, we factor its left side: By either the graphs of the parabolas or Descartes' Rule of Signs, we conclude that has two positive roots and one negative root such that So, has four distinct real roots, or the two parabolas intersect at four distinct points. For Subcondition A, we deduce that Remark for Subcondition A Recall that if then the point is above the parabola It follows that for The maximum value of for the parabola occurs at from which The minimum value of for the parabola occurs at from which Clearly, the parabola and the left half of the parabola do not intersect. Therefore, the two parabolas do not intersect at four distinct points.
1. The point $(0,-k)$ is on or below the parabola $x=2(y-20)^2-k.$ The lower half of the parabola is We need which holds for all values of For Subcondition B, we deduce that can be any positive integer.
We need $20\leq(-k)^2-k,$ from which $k\geq5.$
Moreover, the point $(-k,20)$ is on the parabola $y=x^2-k$ when $k=5.$ We will prove that the two parabolas intersect at four distinct points at this value of $k:$
Substituting $y=x^2-5$ into $x=2(y-20)^2-5,$ we get $x=2\left(\left(x^2-5\right)-20\right)^2-5.$ Expanding and rearranging give \[2x^4-100x^2-x+1245=0. \hspace{20mm}(\bigstar)\] By either the graphs of the parabolas or the Rational Root Theorem, we conclude that $x=-5$ is a root of $(\bigstar).$ So, we factor its left side: \[(x+5)\left(2x^3-10x^2-50x+249\right)=0.\] By either the graphs of the parabolas or Descartes' Rule of Signs, we conclude that $2x^3-10x^2-50x+249=0$ has two positive roots and one negative root such that $x\neq-5.$ So, $(\bigstar)$ has four distinct real roots, or the two parabolas intersect at four distinct points.
For Subcondition A, we deduce that $k\geq5.$
Remark for Subcondition A
Recall that if $1\leq k\leq 4,$ then the point $(-k,20)$ is above the parabola $y=x^2-k.$ It follows that for $-k\leq x\leq0:$
- The maximum value of $y$ for the parabola $y=x^2-k$ occurs at $x=-k,$ from which $y=k^2-k\leq12.$
- The minimum value of $y$ for the parabola $x=2(y-20)^2-k$ occurs at $x=0,$ from which $y=20-\sqrt{\frac k2}>18.$
Clearly, the parabola $x=2(y-20)^2-k$ and the left half of the parabola $y=x^2-k$ do not intersect. Therefore, the two parabolas do not intersect at four distinct points.
The lower half of the parabola $x=2(y-20)^2-k$ is $y=20-\sqrt{\frac{x+k}{2}}.$ We need $-k\leq20-\sqrt{\frac k2},$ which holds for all values of $k.$
For Subcondition B, we deduce that $k$ can be any positive integer.
For Condition 1, we obtain by taking the intersection of Subconditions A and B.
For equations of circles, the coefficients of $x^2$ and $y^2$ must be the same. So, we add the equation $y=x^2-k$ to half the equation $x=2(y-20)^2-k:$ \[y+\frac12x=x^2+(y-20)^2-\frac32k.\] We expand, rearrange, and complete the squares: \begin{align*} y+\frac12x&=x^2+y^2-40y+400-\frac32k \\ \frac32k-400&=\left(x^2-\frac12x\right)+\left(y^2-41y\right) \\ \frac32k-400+\frac{1}{16}+\frac{1681}{4}&=\left(x-\frac14\right)^2+\left(y-\frac{41}{2}\right)^2. \end{align*} We need $\frac32k-400+\frac{1}{16}+\frac{1681}{4}\leq21^2,$ from which $k\leq\left\lfloor\frac{6731}{24}\right\rfloor=280.$
For Condition 2, we obtain
Taking the intersection of Conditions 1 and 2 produces $5\leq k\leq280.$ Therefore, the answer is $5+280=\boxed{285}.$
~MRENTHUSIASM

## Solution 2 (Translations, Inequalities, Circles)
Make the translation $y \rightarrow y+20$ to obtain $20+y=x^2-k$ and $x=2y^2-k$ . Multiply the first equation by $2$ and sum, we see that $2(x^2+y^2)=3k+40+2y+x$ . Completing the square gives us $\left(y- \frac{1}{2}\right)^2+\left(x - \frac{1}{4}\right)^2 = \frac{325+24k}{16}$ ; this explains why the two parabolas intersect at four points that lie on a circle*. For the upper bound, observe that $LHS \leq 21^2=441 \rightarrow 24k \leq 6731$ , so $k \leq 280$ .
For the lower bound, we need to ensure there are $4$ intersections to begin with. (Here I'm using the un-translated coordinates.) Draw up a graph, and realize that two intersections are guaranteed, on the so called "right branch" of $y=x^2-k$ . As we increase the value of $k$ , two more intersections appear on the "left branch":
$k=4$ does not work because the "leftmost" point of $x=2(y-20)^2-4$ is $(-4,20)$ which lies to the right of $\left(-\sqrt{24}, 20\right)$ , which is on the graph $y=x^2-4$ . While technically speaking this doesn't prove that there are no intersections (why?), drawing the graph should convince you that this is the case. Clearly, $k<4$ does not work.
$k=5$ does work because the two graphs intersect at $(-5,20)$ , and by drawing the graph, you realize this is not a tangent point and there is in fact another intersection nearby, due to slope. Therefore, the answer is $5+280=\boxed{285}$ .
- In general (assuming four intersections exist), when two conics intersect, if one conic can be written as $ax^2+by^2=f(x,y)$ and the other as $cx^2+dy^2=g(x,y)$ for polynomials $f$ and $g$ of degree at most $1$ , whenever $(a,b),(c,d)$ are linearly independent (L.I.), we can combine the two equations and then complete the square to achieve $(x-p)^2+(y-q)^2=r^2$ . We can also combine these two equations to form a parabola, or a hyperbola, or an ellipse. When $(a,b),(c,d)$ are not L.I., the intersection points instead lie on a line, which is a circle of radius infinity. When the two conics only have $3,2$ or $1$ intersection point(s), the statement that all these points lie on a circle is trivially true.
~Ross Gao

## Solution 3 (Parabola's Properties)
Claim
Let the axes of two parabolas be perpendicular, their focal parameters be $p_1$ and $p_2$ and the distances from the foci to the point of intersection of the axes be $x_2$ and $y_1$ . Suppose that these parabolas intersect at four points.
Then these points lie on the circle centered at point $(p_2, p_1)$ with radius $r = \sqrt{2(p_1^2 + p_2^2 + p_1 y_1 + p_2 x_2)}.$
Proof
Let's introduce a coordinate system with the center at the point of intersection of the axes. Let the first (red) parabola have axis $x = 0,$ focal parameter $p_1$ and focus at point $A(0, –y_1), y_1 > 0.$ Let second (blue) parabola have axis $y = 0,$ focal parameter $p_2$ and focus at point $B(–x_2,0), x_2 > 0.$ Let us denote the angle between the vector connecting the focus of the first parabola and its point and the positive direction of the ordinate axis $2\theta,$ its length $\rho_1(\theta),$ the angle between the vector connecting the focus of the second parabola and its point and the positive direction of the abscissa axis $2\phi,$ its length $\rho_2(\phi).$ Then \[\rho_1(\theta) = \frac{p_1}{1 - \cos(2\theta)}, \rho_2(\phi) = \frac{p_2}{1 - \cos(2\phi)}.\]
Abscissa of the point of intersection is \begin{align*} x =\rho_1 \sin(2\theta) = p_1\cot\theta = \rho_2 \cos (2\phi) - x_2 = \frac{p_2}{2} (\cot^2\phi - 1)- x_2,\end{align*} \begin{align*} x^2 = p_1^2 \cot ^2 \theta , 2 p_1\cot\theta = p_2 \cos^2 \phi - p_2 - 2x_2 .\end{align*} Ordinate of the point of intersection is \begin{align*} y =\rho_2 \sin 2\phi = p_2\cot\phi = \rho_1 \cos 2\theta - y_1 = \frac{p_1}{2} (\cot^2\theta - 1)- y_1,\end{align*} \begin{align*} y^2 = p_2^2 \cot ^2 \phi , 2 p_2\cot\phi = p_1 \cos^2 \theta - p_1 - 2y_1 .\end{align*} The square of the distance from point of intersection to the point $(p_2, p_1)$ is \begin{align*} r^2 = (x-p_2)^2 + (y-p_1)^2 = x^2 + y^2 - 2 p_1 y - 2 p_2 x + p_1^2 + p_2^2 .\end{align*} After simple transformations, we get $r^2 = 2(p_1^2 + p_2^2 + p_1 y_1 + p_2 x_2).$
Hence, any intersection point has the same distance $r$ from the point $(p_2, p_1).$
Solution
Parameters of the parabola $y = x^2 – k$ are $p_1 = \frac{1}{2}, y_1 = 20 + k – \frac{1}{2}.$
Parameters of the parabola $\frac{x}{2} = (y – 20)^2 – \frac{k}{2}$ are $p_2 = \frac{1}{4}, x_2 = k – \frac{1}{4} \implies r^2 = 20 + \frac{3k}{2}.$
If $r \le 21, k \le \frac{842}{3},$ then integer $k \le 280.$
The vertex of the second parabola is point $(– k,20)$ can be on the parabola $y = x^2 – k$ or below the point of the parabola with the same abscissa. So \[20 \ge (– k)^2 – k \implies 5 \le k \le 280.\] Therefore, the answer is $5+280=\boxed{285}$ .
vladimir.shelomovskii@gmail.com, vvsss

## Solution 4
$\textbf{Min}:$
When $k = 4$ :
$20 = x^2-4$ $x=-\sqrt{24}$
$-\sqrt{24}<-4$ $\times$
When $k = 5$ :
$20 = x^2-5$ $x=-5$
$-5 = -5$ $\checkmark$
$\textbf{Max}:$
\begin{align*} \{ & \left.\begin{aligned} y &= x^2-k \\ x &= 2y^2-80y+800-k \end{aligned} \right. \end{align*}
$x = 2y^2+2y-82y+800-k$
$x = 2y^2+2x^2-2k-82y+800-k$
$2x^2+2y^2-x-82y+800-3k=0$
$x^2+y^2-\frac{x}{2}-41y+400-\frac{3}{2}k = 0$
$(x-\frac{1}{4})^2+(y-\frac{41}{2})^2+400-(\frac{1}{4})^2-(\frac{41}{2})^2 - \frac{3}{2}k = 0$
$(x-\frac{1}{4})^2+(y-\frac{41}{2})^2 = (\frac{1}{4})^2-(\frac{41}{2})^2 + \frac{3}{2}k - 400 \leq 441$
$\frac{1}{16}+\frac{1681}{4}+\frac{3}{2}k \leq 841$
$1+6824+24k \leq 13456$
$24k \leq 6631$
$k \leq \frac{6631}{24}$ $k_{max} = 276$
Therefore the answer is $276+5 = \boxed{281}$
-cassphe

## Video Solution
https://youtube.com/watch?v=7uwMm4b6OBw
~StressedPineapple
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .