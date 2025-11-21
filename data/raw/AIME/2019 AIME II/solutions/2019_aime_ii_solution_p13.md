# 2019 AIME II Problem 13

## Problem

Regular octagon $A_1A_2A_3A_4A_5A_6A_7A_8$ is inscribed in a circle of area $1.$ Point $P$ lies inside the circle so that the region bounded by $\overline{PA_1},\overline{PA_2},$ and the minor arc $\widehat{A_1A_2}$ of the circle has area $\tfrac{1}{7},$ while the region bounded by $\overline{PA_3},\overline{PA_4},$ and the minor arc $\widehat{A_3A_4}$ of the circle has area $\tfrac{1}{9}.$ There is a positive integer $n$ such that the area of the region bounded by $\overline{PA_6},\overline{PA_7},$ and the minor arc $\widehat{A_6A_7}$ of the circle is equal to $\tfrac{1}{8}-\tfrac{\sqrt2}{n}.$ Find $n.$

## Solution 1
The actual size of the diagram doesn't matter. To make calculation easier, we discard the original area of the circle, \(1\), and assume the side length of the octagon is \(2\).
Let \(r\) denote the radius of the circle, \(O\) be the center of the circle. Then: \[r^2= 1^2 + \left(\sqrt{2}+1\right)^2= 4+2\sqrt{2}.\]
Now, we need to find the "D" shape, the small area enclosed by one side of the octagon and \(\frac{1}{8}\) of the circumference of the circle: \[D= \frac{1}{8} \pi r^2 - [A_1 A_2 O]=\frac{1}{8} \pi \left(4+2\sqrt{2}\right)- \left(\sqrt{2}+1\right)\]
Let \(PU\) be the height of \(\triangle A_1 A_2 P\), \(PV\) be the height of \(\triangle A_3 A_4 P\), \(PW\) be the height of \(\triangle A_6 A_7 P\). From the \(\frac{1}{7}\) and \(\frac{1}{9}\) condition we have \[\triangle P A_1 A_2= \frac{\pi r^2}{7} - D= \frac{1}{7} \pi \left(4+2\sqrt{2}\right)-\left(\frac{1}{8} \pi \left(4+2\sqrt{2}\right)- \left(\sqrt{2}+1\right)\right)\] \[\triangle P A_3 A_4= \frac{\pi r^2}{9} - D= \frac{1}{9} \pi \left(4+2\sqrt{2}\right)-\left(\frac{1}{8} \pi \left(4+2\sqrt{2}\right)- \left(\sqrt{2}+1\right)\right)\] which gives \(PU= \left(\frac{1}{7}-\frac{1}{8}\right) \pi \left(4+ 2\sqrt{2}\right) + \sqrt{2}+1\) and \(PV= \left(\frac{1}{9}-\frac{1}{8}\right) \pi \left(4+ 2\sqrt{2}\right) + \sqrt{2}+1\).
Now, let \(A_1 A_2\) intersects \(A_3 A_4\) at \(X\), \(A_1 A_2\) intersects \(A_6 A_7\) at \(Y\),\(A_6 A_7\) intersects \(A_3 A_4\) at \(Z\).
Clearly, \(\triangle XYZ\) is an isosceles right triangle, with right angle at \(X\) and the height with regard to which shall be \(3+2\sqrt2\). Now \(\frac{PU}{\sqrt{2}} + \frac{PV}{\sqrt{2}} + PW = 3+2\sqrt2\) which gives:
\begin{align*} PW&= 3+2\sqrt2-\frac{PU}{\sqrt{2}} - \frac{PV}{\sqrt{2}} \\ &=3+2\sqrt{2}-\frac{1}{\sqrt{2}}\left(\left(\frac{1}{7}-\frac{1}{8}\right) \pi \left(4+ 2\sqrt{2}\right) + \sqrt{2}+1+\left(\frac{1}{9}-\frac{1}{8}\right) \pi \left(4+ 2\sqrt{2}\right) + \sqrt{2}+1\right)\\ &=1+\sqrt{2}- \frac{1}{\sqrt{2}}\left(\frac{1}{7}+\frac{1}{9}-\frac{1}{4}\right)\pi\left(4+2\sqrt{2}\right) \end{align*}
Now, we have the area for \(D\) and the area for \(\triangle P A_6 A_7\), so we add them together:
\begin{align*} \text{Target Area} &= \frac{1}{8} \pi \left(4+2\sqrt{2}\right)- \left(\sqrt{2}+1\right) + \left(1+\sqrt{2}\right)- \frac{1}{\sqrt{2}}\left(\frac{1}{7}+\frac{1}{9}-\frac{1}{4}\right)\pi\left(4+2\sqrt{2}\right)\\ &=\left(\frac{1}{8} - \frac{1}{\sqrt{2}}\left(\frac{1}{7}+\frac{1}{9}-\frac{1}{4}\right)\right)\text{Total Area} \end{align*}
The answer should therefore be \(\frac{1}{8}- \frac{\sqrt{2}}{2}\left(\frac{16}{63}-\frac{16}{64}\right)=\frac{1}{8}- \frac{\sqrt{2}}{504}\). The answer is \(\boxed{504}\).
SpecialBeing2017

## Solution 2
Instead of considering the actual values of the areas, consider only the changes in the areas that result from moving point $P$ from the center of the circle. We will proceed by coordinates. Set the origin at the center of the circle and refer to the following diagram, where the octagon is oriented so as $A_1A_2$ is horizontal (and therefore $A_3A_4$ is vertical). Note that the area bounded by $\overline{A_iA_j}$ and the arc $\widehat{A_iA_j}$ is fixed, so we only need to consider the relevant triangles.
[asy] size(7cm); draw(Circle((0,0),1)); pair P = (0.1,-0.15); filldraw(P--dir(112.5)--dir(112.5-45)--cycle,yellow,red); filldraw(P--dir(112.5-90)--dir(112.5-135)--cycle,yellow,red); filldraw(P--dir(112.5-225)--dir(112.5-270)--cycle,green,red); dot(P); for(int i=0; i<8; ++i) { draw(dir(22.5+45i)--dir(67.5+45i)); draw((0,0)--dir(22.5+45i),gray+dashed); } draw(dir(135)--dir(-45),blue+linewidth(1)); label("$P$", P, dir(-75)); label("$A_1$", dir(112.5), dir(112.5)); label("$A_2$", dir(112.5-45), dir(112.5-45)); label("$A_3$", dir(112.5-90), dir(112.5-90)); label("$A_4$", dir(112.5-135), dir(112.5-135)); label("$A_5$", dir(112.5-180), dir(112.5-180)); label("$A_6$", dir(112.5-225), dir(112.5-225)); label("$A_7$", dir(112.5-270), dir(112.5-270)); label("$A_8$", dir(112.5-315), dir(112.5-315)); dot(dir(112.5)^^dir(112.5-45)^^dir(112.5-90)^^dir(112.5-135)^^dir(112.5-180)^^dir(112.5-225)^^dir(112.5-270)^^dir(112.5-315)); [/asy]
Define one arbitrary unit as the distance that you need to move $P$ from $A_1A_2$ to change the area of $\triangle PA_1A_2$ by $1$ . We can see that $P$ was moved down by $\tfrac{1}{7}-\tfrac{1}{8}=\tfrac{1}{56}$ units to make the area defined by $P$ , $A_1$ , and $A_2$ $\tfrac{1}{7}$ . Similarly, $P$ was moved right by $\tfrac{1}{8}-\tfrac{1}{9}=\tfrac{1}{72}$ to make the area defined by $P$ , $A_3$ , and $A_4$ $\tfrac{1}{9}$ . This means that $P$ has coordinates $(\tfrac{1}{72},-\tfrac{1}{56})$ .
Now, we need to consider how this displacement in $P$ affected the area defined by $P$ , $A_6$ , and $A_7$ . This is equivalent to finding the shortest distance between $P$ and the blue line in the diagram (as $K=\tfrac{1}{2}bh$ and the blue line represents $h$ while $b$ is fixed). Using an isosceles right triangle, one can find the that shortest distance between $P$ and this line is $\tfrac{\sqrt{2}}{2}(\tfrac{1}{56}-\tfrac{1}{72})=\tfrac{\sqrt{2}}{504}$ .
Remembering the definition of our unit, this yields a final area of \[\frac{1}{8}-\frac{\sqrt{2}}{\boxed{504}}.\]
-Archeon

## Video Solution by MOP 2024
https://youtube.com/watch?v=CHJ15nlpZZk
~r00tsOfUnity

## Video Solution by On the Spot STEM
https://youtu.be/B_Drjjn0vv0
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .