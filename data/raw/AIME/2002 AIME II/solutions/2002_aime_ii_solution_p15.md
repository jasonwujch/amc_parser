# 2002 AIME II Problem 15

## Problem

Circles $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ intersect at two points, one of which is $(9,6)$ , and the product of the radii is $68$ . The x-axis and the line $y = mx$ , where $m > 0$ , are tangent to both circles. It is given that $m$ can be written in the form $a\sqrt {b}/c$ , where $a$ , $b$ , and $c$ are positive integers, $b$ is not divisible by the square of any prime, and $a$ and $c$ are relatively prime. Find $a + b + c$ .

## Solution 1
Let the smaller angle between the $x$ -axis and the line $y=mx$ be $\theta$ . Note that the centers of the two circles lie on the angle bisector of the angle between the $x$ -axis and the line $y=mx$ . Also note that if $(x,y)$ is on said angle bisector, we have that $\frac{y}{x}=\tan{\frac{\theta}{2}}$ . Let $\tan{\frac{\theta}{2}}=m_1$ , for convenience. Therefore if $(x,y)$ is on the angle bisector, then $x=\frac{y}{m_1}$ . Now let the centers of the two relevant circles be $(a/m_1 , a)$ and $(b/m_1 , b)$ for some positive reals $a$ and $b$ . These two circles are tangent to the $x$ -axis, so the radii of the circles are $a$ and $b$ respectively. We know that the point $(9,6)$ is a point on both circles, so we have that
\[(9-\frac{a}{m_1})^2+(6-a)^2=a^2\]
\[(9-\frac{b}{m_1})^2+(6-b)^2=b^2\]
Expanding these and manipulating terms gives
\[\frac{1}{m_1^2}a^2-[(18/m_1)+12]a+117=0\]
\[\frac{1}{m_1^2}b^2-[(18/m_1)+12]b+117=0\]
It follows that $a$ and $b$ are the roots of the quadratic
\[\frac{1}{m_1^2}x^2-[(18/m_1)+12]x+117=0\]
It follows from Vieta's Formulas that the product of the roots of this quadratic is $117m_1^2$ , but we were also given that the product of the radii was 68. Therefore $68=117m_1^2$ , or $m_1^2=\frac{68}{117}$ . Note that the half-angle formula for tangents is
\[\tan{\frac{\theta}{2}}=\sqrt{\frac{1-\cos{\theta}}{1+\cos{\theta}}}\]
Therefore
\[\frac{68}{117}=\frac{1-\cos{\theta}}{1+\cos{\theta}}\]
Solving for $\cos{\theta}$ gives that $\cos{\theta}=\frac{49}{185}$ . It then follows that $\sin{\theta}=\sqrt{1-\cos^2{\theta}}=\frac{12\sqrt{221}}{185}$ .
It then follows that $m=\tan{\theta}=\frac{12\sqrt{221}}{49}$ . Therefore $a=12$ , $b=221$ , and $c=49$ . The desired answer is then $12+221+49=\boxed{282}$ .

## Solution 2 (Alcumus)
Let $r_1$ and $r_2$ be the radii of the circles. Then the centers of the circles are of the form $(kr_1,r_1)$ and $(kr_2,r_2)$ for the same constant $k,$ since the two centers are collinear with the origin. Since $(9,6)$ lies on both circles, \[(kr_i - 9)^2 + (r_i - 6)^2 = r^2,\] where $r_i$ represents either radius. Expanding, we get \[k^2 r^2 - (18k + 12) r + 117 = 0.\] We are told the product of the circles is 68, so by Vieta's formulas, $\frac{117}{k^2} = 68.$ Hence, $k^2 = \frac{117}{68},$ and $k = \sqrt{\frac{117}{68}}.$
[asy] unitsize(0.25 cm); pair[] O; real[] r; pair P; r[1] = 4.096; r[2] = 16.6; O[1] = (r[1]/(2/3*sqrt(17/13)),r[1]); O[2] = (r[2]/(2/3*sqrt(17/13)),r[2]); P = reflect(O[1],O[2])*(9,6); draw(Circle(O[1],r[1])); //draw(Circle(O[2],r[2])); draw(arc(O[2],r[2],130,300)); draw((0,0)--(8,12*sqrt(221)/49*8)); draw((0,0)--(30,0)); draw((0,0)--O[1]--(O[1].x,0)); draw(O[1]--(O[1] + reflect((0,0),(10,12*sqrt(221)/49*10))*(O[1]))/2); label("$y = mx$", (8,12*sqrt(221)/49*8), N); dot("$(9,6)$", (9,6), NE); dot("$(kr,r)$", O[1], N); dot(P,red); [/asy]
Since the circle is tangent to the line $y = mx,$ the distance from the center $(kr,r)$ to the line is $r.$ We can write $y = mx$ as $y - mx = 0,$ so from the distance formula, \[\frac{|r - krm|}{\sqrt{1 + m^2}} = r.\] Squaring both sides, we get \[\frac{(r - krm)^2}{1 + m^2} = r^2,\] so $(r - krm)^2 = r^2 (1 + m^2).$ Since $r \neq 0,$ we can divide both sides by r, to get \[(1 - km)^2 = 1 + m^2.\] Then $1 - 2km + k^2 m^2 = 1 + m^2,$ so $m^2 (1 - k^2) + 2km = 0.$ Since $m \neq 0,$ \[m(1 - k^2) + 2k = 0.\] Hence, \[m = \frac{2k}{k^2 - 1} = \frac{2 \sqrt{\frac{117}{68}}}{\frac{117}{68} - 1} = \frac{12 \sqrt{221}}{49}.\] Our answer is thus $12 + 221 + 49 = \boxed{282}$

## Solution 3
Let the centers of $C_1$ and $C_2$ be $A$ and $B$ , respectively, and let the point $(9, 6)$ be $P$ .
Because both $C_1$ and $C_2$ are tangent to the x-axis, and both of them pass through $P$ , both $A$ and $B$ must be equidistant from $P$ and the x-axis. Therefore, they must both be on the parabola with $P$ as the focus and the x-axis as the directrix. Since the coordinates of $P$ is $(9, 6)$ , we see that this parabola is the graph of the function \[y=\frac{1}{12}(x-9)^2+3=\frac{1}{12}x^2-\frac{3}{2}x+\frac{39}{4}.\]
Let $AB$ be $y=kx$ . Because $C_1$ and $C_2$ are both tangent to the x-axis, the y-coordinates of $A$ and $B$ are $r_1$ and $r_2$ , respectively, so the x-coordinates of $A$ and $B$ are $\frac{r_1}{k}$ and $\frac{r_2}{k}$ . But since $A$ and $B$ are also on the graph of the function $y=\frac{1}{12}x^2-\frac{3}{2}x+\frac{39}{4}$ , the x-coordinates of $A$ and $B$ are also the roots of the equation $kx=\frac{1}{12}x^2-\frac{3}{2}x+\frac{39}{4}$ , and by Vieta's Formulas, their product is $\frac{\frac{39}{4}}{\frac{1}{12}}=117$ . So we have $\frac{r_1}{k}\cdot \frac{r_2}{k}=117$ .
We are also given that $r_1r_2=68$ , so $k^2=\frac{r_1r_2}{117}=\frac{68}{117}$ , which means that $k=\sqrt{\frac{68}{117}}$ . Note that the line $AB$ is the angle bisector of the angle between the line $y=mx$ and the x-axis. Therefore, we apply the double-angle formula for tangents and get \[m=\frac{2k}{1-k^2}=\frac{2\sqrt{\frac{68}{117}}}{1-\frac{68}{117}}=\frac{12\sqrt{221}}{49}.\] Thus, the answer is $12+221+49=\boxed{282}$ .
### Sidenote
The two circles are centered at \[\left (\frac{1}{13}\left (117 + 4 \sqrt{221} \pm 2 \sqrt{13(18 \sqrt{221} - 49)} \right), \frac{2}{39} \left(68 + 9 \sqrt {221} \pm 2 \sqrt{17(18 \sqrt{221} - 49)} \right) \right)\]
These problems are copyrighted © by the Mathematical Association of America.