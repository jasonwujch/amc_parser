# 2017 AIME II Problem 12

## Problem

Circle $C_0$ has radius $1$ , and the point $A_0$ is a point on the circle. Circle $C_1$ has radius $r<1$ and is internally tangent to $C_0$ at point $A_0$ . Point $A_1$ lies on circle $C_1$ so that $A_1$ is located $90^{\circ}$ counterclockwise from $A_0$ on $C_1$ . Circle $C_2$ has radius $r^2$ and is internally tangent to $C_1$ at point $A_1$ . In this way a sequence of circles $C_1,C_2,C_3,\ldots$ and a sequence of points on the circles $A_1,A_2,A_3,\ldots$ are constructed, where circle $C_n$ has radius $r^n$ and is internally tangent to circle $C_{n-1}$ at point $A_{n-1}$ , and point $A_n$ lies on $C_n$ $90^{\circ}$ counterclockwise from point $A_{n-1}$ , as shown in the figure below. There is one point $B$ inside all of these circles. When $r = \frac{11}{60}$ , the distance from the center $C_0$ to $B$ is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

[asy] draw(Circle((0,0),125)); draw(Circle((25,0),100)); draw(Circle((25,20),80)); draw(Circle((9,20),64)); dot((125,0)); label("$A_0$",(125,0),E); dot((25,100)); label("$A_1$",(25,100),SE); dot((-55,20)); label("$A_2$",(-55,20),E); [/asy]

## Solution 1
Impose a coordinate system and let the center of $C_0$ be $(0,0)$ and $A_0$ be $(1,0)$ . Therefore $A_1=(1-r,r)$ , $A_2=(1-r-r^2,r-r^2)$ , $A_3=(1-r-r^2+r^3,r-r^2-r^3)$ , $A_4=(1-r-r^2+r^3+r^4,r-r^2-r^3+r^4)$ , and so on, where the signs alternate in groups of $2$ . The limit of all these points is point $B$ . Using the sum of infinite geometric series formula on $B$ and reducing the expression: $(1-r)-(r^2-r^3)+(r^4-r^5)-...=\frac{1-r}{1+r^2}$ , $(r-r^2)-(r^3-r^4)+(r^5-r^6)-...=\frac{r-r^2}{1+r^2}$ . Thus, we get $B=\left(\frac{1-r}{r^2+1},\frac{r-r^2}{r^2+1}\right)$ . The distance from $B$ to the origin is $\sqrt{\left(\frac{1-r}{r^2+1}\right)^2+\left(\frac{r-r^2}{r^2+1}\right)^2}=\frac{1-r}{\sqrt{r^2+1}}.$ Let $r=\frac{11}{60}$ , and the distance from the origin is $\frac{49}{61}$ . $49+61=\boxed{110}$ .

## Solution 2
Let the center of circle $C_i$ be $O_i$ . Note that $O_0BO_1$ is a right triangle, with right angle at $B$ . Also, $O_1B=\frac{11}{60}O_0B$ , or $O_0B = \frac{60}{61}O_0O_1$ . It is clear that $O_0O_1=1-r=\frac{49}{60}$ , so $O_0B=\frac{60}{61}\times\frac{49}{60}=\frac{49}{61}$ . Our answer is $49+61=\boxed{110}$
-william122

## Solution 3
Note that there is an invariance, Consider the entire figure $\mathcal{F}$ . Perform a $90^\circ$ counterclockwise rotation, then scale by $r$ with respect to $(1, 0)$ . It is easy to see that the new figure $\mathcal{F}' \cup S^1 = \mathcal{F}$ , so $B$ is invariant.
Using the invariance, Let $B = (x,y)$ . Then rotating and scaling, $B = (1-r(1+y), rx)$ . Equating, we find $x = \frac{1-r}{r^2+1}, y = \frac{r-r^2}{r^2+1}$ . The distance is thus $\frac{49}{61}$ . Our answer is $49+61=\boxed{110}$
-Isogonal

## Solution 4
Using the invariance again as in Solution 3, assume $B$ is $d$ away from the origin. The locus of possible points is a circle with radius $d$ . Consider the following diagram. [asy] size(7cm); draw(circle((0,0), 49/61)); draw((0,0)--(0.790110185, 0.144853534)); draw((0,0)--(-0.144853534, 0.790110185)); draw((-0.144853534, 0.790110185)--(1,0)); draw((0,0)--(1,0)); draw(rightanglemark((-0.144853534, 0.790110185), (0,0), (0.790110185, 0.144853534), 3)); label("$O$", (0,0), SW); label("$(1,0)$", (1,0), E); label("$B$", (0.790110185, 0.144853534), NE); label("$B'$", (-0.144853534, 0.790110185), N); label("$d$", (0.5 * 49/61, 0), S); [/asy]
Let the distance from $B$ to $(1,0)$ be $x$ . As $B$ is invariant, $x = r(BB' + x) \implies x = r\frac{d\sqrt{2}}{1-r}$ . Then by Power of a Point, $x(BB' + x) = (1-d)(1+d) \implies xr(BB' + x) = r(1-d)(1+d) \implies x^2 = r(1-d^2) \implies d^2 = \left(1 + \frac{2r}{(1-r)^2}\right)$ . Solving, $d = \frac{49}{61}$ . Our answer is $49+61=\boxed{110}$
-Isogonal

## Solution 5 (complex)
Let $A_0$ be the origin. Now note that the ratio of lengths of consecutive line segments is constant and equal to $r$ . Now accounting for rotation by $\frac{\pi}{2}$ radians, we see that the common ratio is $ri$ . Thus since our first term is $A_1=-r+ri$ , the total sum (by geometric series formula) is $\frac{-r+ri}{1-ri}=\frac{-781+538i}{3721}$ . We need the distance from $C_0=-1$ so our distance is $|B-C_0|=\sqrt{\left(\frac{-781}{3721}-(-1)\right)^2+\left(\frac{538i}{3721}\right)^2}=\sqrt{\frac{2401}{3721}}=\frac{49}{61}$ . Our answer is $49+61=\boxed{110}$
-chrisdiamond10
By the way, here's a Geogebra Diagram. ~r00tsOfUnity

## Video Solution by mop 2024
https://youtube.com/watch?v=5keaS1CZlLo
~r00tsOfUnity
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .