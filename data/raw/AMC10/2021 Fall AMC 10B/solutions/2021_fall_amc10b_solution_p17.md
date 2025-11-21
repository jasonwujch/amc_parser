# 2021 Fall AMC 10B Problem 17

## Problem

Distinct lines $\ell$ and $m$ lie in the $xy$ -plane. They intersect at the origin. Point $P(-1, 4)$ is reflected about line $\ell$ to point $P'$ , and then $P'$ is reflected about line $m$ to point $P''$ . The equation of line $\ell$ is $5x - y = 0$ , and the coordinates of $P''$ are $(4,1)$ . What is the equation of line $m?$

$(\textbf{A})\: 5x+2y=0\qquad(\textbf{B}) \: 3x+2y=0\qquad(\textbf{C}) \: x-3y=0\qquad(\textbf{D}) \: 2x-3y=0\qquad(\textbf{E}) \: 5x-3y=0$

## Solution 1
Denote $O$ as the origin.
Even though the problem is phrased as a coordinate bash, that looks disgusting. Instead, let's try to phrase this problem in terms of Euclidean geometry, using the observation that $\angle POP'' = 90^{\circ}$ , and that both $\ell$ and $m$ must pass through $O$ in order to preserve the distance from $P$ to the origin. [asy] unitsize(1.4cm); draw((0,3)--(0,0)--(3,0), dashed); dot((0,3)); dot((3,0)); label("$P$", (0,3), W); label("$P''$", (3,0), S); draw((0,0)--(1.5,4.5)); label("$\ell$", (1.5,4.5), N); draw((0,0)--(4,2)); label("$m$", (4,2), E); dot((1.8,2.4)); label("$P'$", (1.8,2.4), N); label("$O$",(0,0)); dot((1,3)); dot((2.5,1.25)); label("$A$", (1,3), E); label("$B$", (2.5,1.25), N); [/asy] ( $A$ and $B$ are just defined as points on lines $\ell$ and $m$ .) Because of how reflections work, we have that $\angle AOP' = \angle POA$ and $\angle P'OB = \angle BOP''$ ; adding these two equations together and using angle addition, we have that $\angle AOB = \angle POA + \angle BOP''$ . Since the sum of both sides combined must be $90^{\circ}$ by angle addition, \[\angle AOB = 45^{\circ}.\] This is helpful! We can now return to using coordinates, with this piece of information in mind: [asy] unitsize(0.2cm); markscalefactor = 0.08; import graph; Label f; f.p=fontsize(9); xaxis(-2,6,Ticks(f, 2.0)); yaxis(-1,6,Ticks(f, 2.0)); dot((-1,4)); label("$P$", (-1,4), W); dot((4,1)); label("$P''$", (4,1), W); draw((0,0)--(1.2,6)); label("$\ell$", (1.2,6), N); dot((0.5,2.5));label("$(0.5,2.5)$", (0.5,2.5), E);label("$A$", (0.5,2.5), W); dot((3,2));label("$B$", (3,2), E); draw((0.5,2.5)--(3,2), dashed); draw((0,0)--(6,4)); label("$m$", (6,4), E); draw(anglemark((6, 4), (0, 0), (1, 5))); label("$45^{\circ}$", (0.54,0.75)); [/asy] The $45^{\circ}$ angle is a little bit unwieldy in the coordinate plane, so we should try to make a $45-45-90$ triangle. Let $A$ be a point on $\ell$ ; to make $A$ fit nicely in the diagram, let it be $(0.5,2.5)$ . Now, let's draw a perpendicular to $\ell$ through point $A$ , intersecting $m$ at point $B$ . $OAB$ is a $45-45-90$ triangle, so $B$ is a $90$ degree counterclockwise rotation from $O$ about $A$ . Therefore, the coordinates of $B$ are \[(0.5+2.5,2.5-0.5) = (3,2).\] So, $(3,2)$ is a point on line $m$ , which we already know passes through the origin; therefore, $m$ 's equation is $y=\frac{2x}{3} \implies \boxed{\textbf{(D) } 2x-3y = 0}.$
~ihatemath123
(We never actually had to use the information of the exact coordinates of $P$ ; as long as $\angle POP'' = 90^{\circ}$ , when we move $P$ around, this will not affect $m$ 's equation.)
### Supplement
In case you are confused about the coordinates of B, first transform O, A, and B such that A is the origin A'(0,0) in a new coordinate system. From there it is not too hard to see that O now has the coordinates O' (-0.5,-2.5). Thus point B, from a 90 deg CCW rotation around origin A, will have a coordinate of B' (2.5, -0.5).
Now in order to go from this new coord system A'(0,0) to its original point A(0.5,2.5), we have to +0.5,+2.5 to the x and y coordinates respectively. Doing this with B' to B, we have (2.5+0.5,-0.5+2.5)=B (3,2) as desired.
~mathboy282

## Solution 2
It is well known that the composition of 2 reflections , one after another, about two lines $l$ and $m$ , respectively, that meet at an angle $\theta$ is a rotation by $2\theta$ around the intersection of $l$ and $m$ .
Now, we note that $(4,1)$ is a 90 degree rotation clockwise of $(-1,4)$ about the origin, which is also where $l$ and $m$ intersect. So $m$ is a 45 degree rotation of $l$ about the origin clockwise.
To rotate $l$ 90 degrees clockwise, we build a square with adjacent vertices $(0,0)$ and $(1,5)$ . The other two vertices are at $(5,-1)$ and $(6,4)$ . The center of the square is at $(3,2)$ , which is the midpoint of $(1,5)$ and $(5,-1)$ . The line $m$ passes through the origin and the center of the square we built, namely at $(0,0)$ and $(3,2)$ . Thus the line is $y = \frac{2}{3} x$ . The answer is $\boxed{\textbf{(D) } 2x-3y = 0}$ .
~hurdler
~minor edits by nightshade2526

## Solution 3
We know that the equation of line $\ell$ is $y = 5x$ . This means that $P'$ is $(-1,4)$ reflected over the line $y = 5x$ . This means that the line with $P$ and $P'$ is perpendicular to $\ell$ , so it has slope $-\frac{1}{5}$ . Then the equation of this perpendicular line is $y = -\frac{1}{5}x + c$ , and plugging in $(-1,4)$ for $x$ and $y$ yields $c = \frac{19}{5}$ .
The midpoint of $P'$ and $P$ lies at the intersection of $y = 5x$ and $y = -\frac{1}{5}x + \frac{19}{5}$ . Solving, we get the x-value of the intersection is $\frac{19}{26}$ and the y-value is $\frac{95}{26}$ . Let the x-value of $P'$ be $x'$ - then by the midpoint formula, $\frac{x' - 1}{2} = \frac{19}{26} \implies x' = \frac{32}{13}$ . We can find the y-value of $P'$ the same way, so $P' = (\frac{32}{13},\frac{43}{13})$ .
Now we have to reflect $P'$ over $m$ to get to $(4,1)$ . The midpoint of $P'$ and $P''$ will lie on $m$ , and this midpoint is, by the midpoint formula, $(\frac{42}{13},\frac{28}{13})$ . $y = mx$ must satisfy this point, so $m = \frac{\frac{28}{13}}{\frac{42}{13}} = \frac{28}{42} = \frac{2}{3}$ .
Now the equation of line $m$ is $y = \frac{2}{3}x \implies 2x-3y = 0 = \boxed{D}$
~KingRavi

## Solution 4
First, use Solution 1's method to get $\angle POP'' = 90^\circ$ and that the angle between lines $\ell$ and $m$ is $45^\circ$ . From here, note that the slope of line $m$ is less than that of line $\ell$ as otherwise $P''$ wouldn't even be close to $(4, 1)$ . Thus, line $m$ is a $45^\circ$ clockwise rotation of line $\ell$ . Line $\ell$ makes an angle of $\tan^{-1}(5)$ with the positive x axis. Thus, line $m$ makes an angle of $\tan^{-1}(5) - 45^\circ$ with the positive x axis. Thus, the slope of line $m$ is \[\tan (\tan^{-1}(5) - 45^\circ) = \frac{5 - 1}{1 + 5\cdot 1} = \frac{2}{3},\] by the tangent addition formula. Since the slope of line $m$ is $\frac{2}{3}$ , its equation is $y = \frac{2}{3}x \implies 2x - 3y = 0$ , which is choice $\boxed{\textbf{D}}$ .

## Solution 5(cheese)
When we graph all the lines and points with a ruler, you can see that a slope of $\frac{5}{3}$ is too big while $\frac{1}{3}$ is too small. We also see that the slope cannot be negative, therefore the answer is $\boxed{D}.$ ~ agentdabber

## Video Solution 2 (by Interstigation)
https://www.youtube.com/watch?v=KdrYlPmqqv0
~Interstigation

## Video Solution by WhyMath
https://youtu.be/Wwzqihd3cUg
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/YOpyq7Zu_hA

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=PgFX55o6h1g
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .