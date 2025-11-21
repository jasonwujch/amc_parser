# 2008 AIME II Problem 11

## Problem

In triangle $ABC$ , $AB = AC = 100$ , and $BC = 56$ . Circle $P$ has radius $16$ and is tangent to $\overline{AC}$ and $\overline{BC}$ . Circle $Q$ is externally tangent to $P$ and is tangent to $\overline{AB}$ and $\overline{BC}$ . No point of circle $Q$ lies outside of $\triangle ABC$ . The radius of circle $Q$ can be expressed in the form $m - n\sqrt {k}$ , where $m$ , $n$ , and $k$ are positive integers and $k$ is the product of distinct primes. Find $m + nk$ .

## Solution
Let $X$ and $Y$ be the feet of the perpendiculars from $P$ and $Q$ to $BC$ , respectively. Let the radius of $\odot Q$ be $r$ . We know that $PQ = r + 16$ . From $Q$ draw segment $\overline{QM} \parallel \overline{BC}$ such that $M$ is on $PX$ . Clearly, $QM = XY$ and $PM = 16-r$ . Also, we know $QPM$ is a right triangle.
To find $XC$ , consider the right triangle $PCX$ . Since $\odot P$ is tangent to $\overline{AC},\overline{BC}$ , then $PC$ bisects $\angle ACB$ . Let $\angle ACB = 2\theta$ ; then $\angle PCX = \angle QBX = \theta$ . Dropping the altitude from $A$ to $BC$ , we recognize the $7 - 24 - 25$ right triangle , except scaled by $4$ .
So we get that $\tan(2\theta) = 24/7$ . From the half-angle identity , we find that $\tan(\theta) = \frac {3}{4}$ . Therefore, $XC = \frac {64}{3}$ . By similar reasoning in triangle $QBY$ , we see that $BY = \frac {4r}{3}$ .
We conclude that $XY = 56 - \frac {4r + 64}{3} = \frac {104 - 4r}{3}$ .
So our right triangle $QPM$ has sides $r + 16$ , $r - 16$ , and $\frac {104 - 4r}{3}$ .
By the Pythagorean Theorem , simplification, and the quadratic formula , we can get $r = 44 - 6\sqrt {35}$ , for a final answer of $\fbox{254}$ .

## Solution 2
First let $\theta = \angle{PCB}$ ; now connect the points as shown in the first solution's diagram ; realise that $\tan\theta = r/x = 16/y = r + 16/(x+y)$ where $x = BY$ and $y = CX$ (the 2 tangents) ; then we have that $QM = 64r = 56 - x - y \implies (x+y) = 56 - 64r$ hence $r/x = 16+r/(56-64r)$ ; now drop altitude $AY$ to solve for $\tan{2\theta}$ ; now since we know $\tan{2\theta}$ we know $\tan \theta = r/x$ in terms of $r$ hence solve the resulting equation in $r$ .

## Solution 3 (pure synthetic)
Refer to the above diagram. Let the larger circle have center $O_1$ , the smaller have center $O_2$ , and the incenter be $I$ . We can easily calculate that the area of $\triangle ABC = 2688$ , and $s = 128$ and $R = 21$ , where $R$ is the inradius.
Now, Line $\overline{AI}$ is the perpendicular bisector of $\overline{BC}$ , as $\triangle ABC$ is isosceles. Letting the point of intersection be $X$ , we get that $BX = 28$ and $IX = 21$ , and $B, O_2, I$ are collinear as $O_2$ is equidistant from $\overline{AB}$ and $\overline{BC}$ . By Pythagoras, $BI = 35$ , and we notice that $\triangle BIX$ is a 3-4-5 right triangle.
Letting $r$ be the desired radius and letting $Y$ be the projection of $O_2$ onto $\overline{BC}$ , we find that $BY = \frac{4r}{3}$ . Similarly, we find that the distance between the projection from $O_1$ onto $\overline{BC}$ , $W$ , and $C$ , is $\frac{64}{3}$ . From there, we let the projection of $O_2$ onto $\overline{O_1W}$ be $Z$ , and we have $O_2Z = 28 - \frac{4r}{3} + \frac{20}{3}$ , $O_1Z = 16 - r$ , and $O_1O_2 = 16 + r$ . We finish with Pythagoras on $\triangle O_1O_2Z$ , whence we get the desired answer of $\boxed{254}$ . - Spacesam

## Solution 4
Let the incenter be O and the altitude from A to $\overline{BC}$ be T. Note that by AA, $\triangle BQY \sim \triangle OBT$ and $\triangle PXC \sim \triangle OTC.$ Note that from $A = rs$ , the inradius of the big triangle is $21$ Using ravi substitution(or noticing that $\overline{AT}$ is an altitude), we then have that $TB = TC = 28.$ From similar triangles, we can now find $\overline{BY}.$ We have \[\frac{\overline{BY}}{QY} = \frac{7}{{21}} \rightarrow \overline{BY} = \frac{4}{3} r\] Now, note that as in solution 1, drawing the perpendicular from Q to $\overline{PX}$ (call it Z) yields $\overline{PZ} = 16 - r, \overline{ZX} = r.$ Then, from this, \[\overline{QZ} = \overline{YX} = \sqrt{(\overline{PQ})^2 - (\overline{PZ})^2} = \sqrt{(16+r)^2-(16-r)^2} = 8\sqrt{r}\] Using similar similarity as was done to find $\overline{BY}$ we have $\frac{\overline{PX}}{\overline{XC}} = \frac{\overline{OT}}{\overline{TC}} \rightarrow \frac{16}{\overline{XC}} = \frac{21}{28} \rightarrow \overline{XC} = \frac{64}{3}$ . Now adding all these up and equating them to $\overline{BC}$ yields \[\frac{4}{3}r + 8\sqrt{r}+ \frac{16}{3} = 56 \rightarrow r = 44 - 6\sqrt{35} \rightarrow 44 + 6\cdot 35 = \boxed{254}\]
These problems are copyrighted © by the Mathematical Association of America.