# 2013 AIME I Problem 12

## Problem

Let $\bigtriangleup PQR$ be a triangle with $\angle P = 75^\circ$ and $\angle Q = 60^\circ$ . A regular hexagon $ABCDEF$ with side length 1 is drawn inside $\triangle PQR$ so that side $\overline{AB}$ lies on $\overline{PQ}$ , side $\overline{CD}$ lies on $\overline{QR}$ , and one of the remaining vertices lies on $\overline{RP}$ . There are positive integers $a, b, c,$ and $d$ such that the area of $\triangle PQR$ can be expressed in the form $\frac{a+b\sqrt{c}}{d}$ , where $a$ and $d$ are relatively prime, and c is not divisible by the square of any prime. Find $a+b+c+d$ .

## Solution 1
First, find that $\angle R = 45^\circ$ . Draw $ABCDEF$ . Now draw $\bigtriangleup PQR$ around $ABCDEF$ such that $Q$ is adjacent to $C$ and $D$ . The height of $ABCDEF$ is $\sqrt{3}$ , so the length of base $QR$ is $2+\sqrt{3}$ . Let the equation of $\overline{RP}$ be $y = x$ . Then, the equation of $\overline{PQ}$ is $y = -\sqrt{3} (x - (2+\sqrt{3})) \to y = -x\sqrt{3} + 2\sqrt{3} + 3$ . Solving the two equations gives $y = x = \frac{\sqrt{3} + 3}{2}$ . The area of $\bigtriangleup PQR$ is $\frac{1}{2} * (2 + \sqrt{3}) * \frac{\sqrt{3} + 3}{2} = \frac{5\sqrt{3} + 9}{4}$ . $a + b + c + d = 9 + 5 + 3 + 4 = \boxed{021}$
Note (different ending): When you have the length of the base $QR$ , you don't need to find the equations of the lines $QP$ and $PR$ . Instead, make an altitude from $P$ to $QR$ , and call the foot $M$ . $QPM$ is a $45, 45, 90$ triangle and $PMR$ is a $30, 60, 90$ triangle. And, they both share $PM$ . So, we can set $RM$ as $x$ , so $PM$ is $x\sqrt{3}$ . Since $QPM$ is a $45, 45, 90$ triangle, $PM=MQ=x\sqrt{3}$ . The base $QR$ can be written as $QM+MR=x+x\sqrt{3}=2+\sqrt{3}$ . Solve this equation and $x=\frac{\sqrt{3}+1}{2}$ and $PM=x\sqrt{3}=\frac{\sqrt{3}+3}{2}$ . Multiply this by base $QR$ and divide by $2$ to get the area of triangle $PQR$ which is $\frac{9+5\sqrt{3}}{4}$ . So, $a + b + c + d = 9 + 5 + 3 + 4 = \boxed{021}$ -hwan

## Solution 2 (Cartesian Variation)
Use coordinates. Call $Q$ the origin and $QP$ be on the x-axis. It is easy to see that $F$ is the vertex on $RP$ . After labeling coordinates (noting additionally that $QBC$ is an equilateral triangle), we see that the area is $QP$ times $0.5$ times the coordinate of $R$ . Draw a perpendicular of $F$ , call it $H$ , and note that $QP = 1 + \sqrt{3}$ after using the trig functions for $75$ degrees.
Now, get the lines for $QR$ and $RP$ : $y=\sqrt{3}x$ and $y=-(2+\sqrt{3})x + (5+\sqrt{3})$ , whereupon we get the ordinate of $R$ to be $\frac{3+2\sqrt{3}}{2}$ , and the area is $\frac{5\sqrt{3} + 9}{4}$ , so our answer is $\boxed{021}$ .

## Solution 3 (Trig)
Angle chasing yields that both triangles $PAF$ and $PQR$ are $75$ - $60$ - $45$ triangles. First look at triangle $PAF$ . Using Law of Sines, we find:
$\frac{\frac{\sqrt{6} + \sqrt{2}}{4}}{1} = \frac{\frac{\sqrt{2}}{2}}{PA}$
Simplifying, we find $PA = \sqrt{3} - 1$ . Since $\angle{Q} = 60^\circ$ , WLOG assume triangle $BQC$ is equilateral, so $BQ = 1$ . So $PQ = \sqrt{3} + 1$ .
Apply Law of Sines again,
$\frac{\frac{\sqrt{2}}{2}}{\sqrt{3} + 1} = \frac{\frac{\sqrt{3}}{2}}{PR}$
Simplifying, we find $PR = \frac{\sqrt{6}}{2} \cdot (1 + \sqrt{3})$ .
$[PQR] = \frac{1}{2} \cdot PQ \cdot PR \cdot \sin 75^\circ$ .
Evaluating and reducing, we get $\frac{9 + 5\sqrt{3}}{4},$ thus the answer is $\boxed{021}$

## Solution 4 (Special Triangles)
As we can see, the $75^\circ$ angle of $\angle P$ can be split into a $45^\circ$ angle and a $30^\circ$ angle. This allows us to drop an altitude from point $P$ for $\triangle RPQ$ which intersects $\overline{AF}$ at point $a$ and $\overline{RQ}$ at point $b$ . The main idea of our solution is to obtain enough sides of $\triangle RPQ$ that we are able to directly figure out its area (specifically by figuring out side $\overline{RQ}$ and $\overline{Pb}$ ).
We first begin by figuring out the length of $\overline{PQ}$ . This can be easily done, since $\overline{AB}$ is simply $1$ (given in the problem) and $\overline{BQ}=1$ because $\triangle BCQ$ is an equilateral after some simple angle calculations. Now we need to find $\overline{PA}$ . This is when we bring in some simple algebra.
PREPARATION: $\overline{aF}=\overline{Pa}$ (45-45-90 Right Triangle)
$\overline{Pa}=\sqrt{3}\overline{Aa}$ (30-60-90 Right Triangle)
$\overline{PA}=2\overline{Aa}$
$\overline{Aa}+\overline{aF}=1$
SOLVING: $\overline{Aa}+\sqrt{3}\overline{Aa}=1$
so $\overline{Aa}(\sqrt{3}+1)=1$
$\overline{Aa}=\frac{1}{\sqrt{3}+1}=\frac{\sqrt{3}-1}{2}$
Finally, $\overline{PA}=2\cdot\frac{\sqrt{3}-1}{2}=\sqrt{3}-1$
Now, we can finally get the length of $\overline{PQ}$ by adding up $\overline{PA}+\overline{AB}+\overline{BQ}$ , which is simply $(\sqrt{3}-1)+(1)+(1)=\sqrt{3}+1$
To get $\overline{RQ}$ and $\overline{Pb}$ , we first work bit by bit.
$\overline{Qb}=\frac{\overline{PQ}}{2}=\frac{\sqrt{3}+1}{2}$ (30-60-90 Right Triangle)
$\overline{Pb}=\sqrt{3}\overline{Qb}=\frac{\sqrt{3}+3}{2}$ (same 30-60-90 Right Triangle)
Since $\overline{Pb}=\overline{Rb}$ because of 45-45-90 right triangles,
$\overline{Rb}=\frac{\sqrt{3}+3}{2}$ too.
Now, we can finally calculate $\overline{RQ}$ , and it is $\overline{Rb}+\overline{Qb}=\frac{\sqrt{3}+3}{2}+\frac{\sqrt{3}+1}{2}=\sqrt{3}+2$ .
Finally, the area of $\triangle PRQ$ can be calculated by $\frac{1}{2}\cdot\overline{RQ}\cdot\overline{Pb}$ , which is equal to $[\triangle PRQ]=\frac{1}{2} \cdot (\sqrt{3}+2) \cdot \frac{\sqrt{3}+3}{2} =\frac{9+5\sqrt{3}}{4}$ . So the final answer is $9+5+3+4=\fbox{021}$ .
-by What do Humanitarians Eat?

## Solution 5 (Trig)
With some simple angle chasing we can show that $\triangle OJL$ and $\triangle MPL$ are congruent. This means we have a large equilateral triangle with side length $3$ and quadrilateral $OJQN$ . We know that $[OJQN] = [\triangle NQL] - [\triangle OJL]$ . Using Law of Sines and the fact that $\angle N = 45^{\circ}$ we know that $\overline{NL} = \sqrt{6}$ and the height to that side is $\frac{\sqrt{3} -1}{\sqrt{2}}$ so $[\triangle NQL] = \frac{3-\sqrt{3}}{2}$ . Using an extremely similar process we can show that $\overline{OJ} = 2-\sqrt{3}$ which means the height to $\overline{LJ}$ is $\frac{2\sqrt{3}-3}{2}$ . So the area of $\triangle OJL = \frac{2\sqrt{3}-3}{4}$ . This means the area of quadrilateral $OJQN = \frac{3-\sqrt{3}}{2} - \frac{2\sqrt{3}-3}{4} = \frac{9-4\sqrt{3}}{4}$ . So the area of our larger triangle is $\frac{9-4\sqrt{3}}{4} + \frac{9\sqrt{3}}{4} = \frac{9+5\sqrt{3}}{4}$ . Therefore $9+5+3+4=\fbox{021}$ .

## Solution 6 (Elementary Geo)
We can find that $AF || CD || QR$ . This means that the perpendicular from $P$ to $QR$ is perpendicular to $AF$ as well, so let that perpendicular intersect $AF$ at $G$ , and the perpendicular intersect $QR$ at $H$ . Set $AP=x$ . Note that $\angle {PAG} = 60^\circ$ , so $AG=\frac{x}{2}$ and $PG = GF = \frac{x\sqrt3}{2}$ . Also, $1=AF=AG+GF=\frac{x}{2} + \frac{x\sqrt{3}}{2}$ , so $x=\sqrt{3} - 1$ . It's easy to calculate the area now, because the perpendicular from $P$ to $QR$ splits $\triangle{PQR}$ into a $30-60-90$ (PHQ) and a $45-45-90$ (PHR). From these triangles' ratios, it should follow that $QH=\frac{\sqrt{3} + 1}{2}, PH=HR=\frac{\sqrt{3}+3}{2}$ , so the area is $\frac{1}{2} * PH * QR = \frac{1}{2} * PH * (QH + HR) = \frac{1}{2} * \frac{\sqrt{3} + 3}{2} * \frac{2\sqrt{3}+4}{2} = \boxed{\frac{9+5\sqrt{3}}{4}}$ . $9+5+3+4=021$ . By Mathscienceclass

## Solution 7 (Combination of 1 & 2)
We can observe that $RD=DF$ (because $\angle R$ & $\angle RFD$ are both $45^\circ$ ). Thus we know that $RD$ is equivalent to the height of the hexagon, which is $\sqrt3$ . Now we look at triangle $\triangle AFP$ and apply the Law of Sines to it. $\frac{1}{\sin{75}}=\frac{AP}{\sin{45}}$ . From here we can solve for $AP$ and get that $AP=\sqrt{3}-1$ . Now we use the Sine formula for the area of a triangle with sides $RQ$ , $PQ$ , and $\angle {RQP}$ to get the answer. Setting $PQ=\sqrt{3}+1$ and $QR=\sqrt{3}+2$ we get the expression $\frac{(\sqrt{3}+1)(\sqrt{3}+2)(\frac{\sqrt{3}}{2})}{2}$ which is $\frac{9 + 5\sqrt{3}}{4}$ . Thus our final answer is $9+5+3+4=\fbox{021}$ . By AwesomeLife_Math

## Solution 8 (Area Ratios + Trig)
Note that $\triangle PAF \sim \triangle PQR$ . Let $X$ be the foot of an altitude dropped from $F$ to $PQ$ . Using trigonometry, we find that $PA = \sqrt3 - 1$ and $FX = \frac{\sqrt3}{2}$ , thus the area of $\triangle PAF$ is $\frac{3 - \sqrt3}{4}$ . Since $QA$ is clearly $2$ , the scale factor between $\triangle PAF$ and $\triangle PQR$ is $\frac{\sqrt3 + 1}{\sqrt3 - 1}$ , and thus $[PQR] = \frac{3 - \sqrt3}{4} \cdot \left( \frac{\sqrt3 + 1}{\sqrt3 - 1} \right)^2 = \frac{9 + 5\sqrt3}{4}$ , and we extract $\boxed{021}$ . ~ostriches88

## Solution 9 (I'm not sure if this has been posted before)
Let $F$ be the point on $RP$ . Drop the perpendicular $FD$ , and notice the length of this is $\sqrt{3}$ . Consider the $45-45-90$ triangle $\triangle FDR$ . The area is clearly $\frac{3}{2}$ . This also takes away a sixth of the original hexagon, so we add $\frac{5}{6} \cdot \frac{1^2 \sqrt{3}}{4}$ . The equilateral triangle $\triangle BCQ$ has area $\frac{3}{4}$ . Finally, the upper triangle, $\triangle PAF$ , has $1$ side facing the $75^{\circ}$ angle, so consequently by law of sines we obtain the side opposing the $45$ degree angle has side length $\sqrt{3} - 1$ (recall that $\sin 75^{\circ} = \frac{\sqrt{6} + \sqrt{2}}{4}$ ). Then, we have $\frac{1}{2} (\sqrt{3} - 1)(1) \sin(60^{\circ}) = \frac{3-\sqrt{3}}{4}$ . Adding the four areas together, we obtain $\frac{9 + 5\sqrt{3}}{4}$ . (Don't forget that the area of the 45-45-90 triangle is not in fact $3$ , unless you want a final answer of $27$ instead of the actual $\boxed{21}$ ).
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .