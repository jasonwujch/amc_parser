# 2012 AIME I Problem 8

## Problem

Cube $ABCDEFGH,$ labeled as shown below, has edge length $1$ and is cut by a plane passing through vertex $D$ and the midpoints $M$ and $N$ of $\overline{AB}$ and $\overline{CG}$ respectively. The plane divides the cube into two solids. The volume of the larger of the two solids can be written in the form $\tfrac{p}{q},$ where $p$ and $q$ are relatively prime positive integers. Find $p+q.$

## Solution: think outside the box (pun intended)
Define a coordinate system with $D$ at the origin and $C,$ $A,$ and $H$ on the $x$ , $y$ , and $z$ axes respectively. Then $D=(0,0,0),$ $M=(.5,1,0),$ and $N=(1,0,.5).$ It follows that the plane going through $D,$ $M,$ and $N$ has equation $2x-y-4z=0.$ Let $Q = (1,1,.25)$ be the intersection of this plane and edge $BF$ and let $P = (1,2,0).$ Now since $2(1) - 1(2) - 4(0) = 0,$ $P$ is on the plane. Also, $P$ lies on the extensions of segments $DM,$ $NQ,$ and $CB$ so the solid $DPCN = DMBCQN + MPBQ$ is a right triangular pyramid. Note also that pyramid $MPBQ$ is similar to $DPCN$ with scale factor $.5$ and thus the volume of solid $DMBCQN,$ which is one of the solids bounded by the cube and the plane, is $[DPCN] - [MPBQ] = [DPCN] - \left(\frac{1}{2}\right)^3[DPCN] = \frac{7}{8}[DPCN].$ But the volume of $DPCN$ is simply the volume of a pyramid with base $1$ and height $.5$ which is $\frac{1}{3} \cdot 1 \cdot .5 = \frac{1}{6}.$ So $[DMBCQN] = \frac{7}{8} \cdot \frac{1}{6} = \frac{7}{48}.$ Note, however, that this volume is less than $.5$ and thus this solid is the smaller of the two solids. The desired volume is then $[ABCDEFGH] - [DMBCQN] = 1 - \frac{7}{48} = \frac{41}{48} \rightarrow p+q = \boxed{089.}$
- Another way to finish after using coordinates: Take the volume of DMBCNQ as the sum of the volumes of DMBQ and DBCNQ. Then, we have the sum of the volumes of a tetrahedron and a pyramid with a trapezoidal base. Their volumes, respectively, are $\tfrac{1}{48}$ and $\tfrac{1}{8}$ , giving the same answer as above. $\blacksquare$ ~mathtiger6

## Solution 2
Define a coordinate system with $D = (0,0,0)$ , $M = (1, \frac{1}{2}, 0)$ , $N = (0,1,\frac{1}{2})$ . The plane formed by $D$ , $M$ , and $N$ is $z = \frac{y}{2} - \frac{x}{4}$ . It intersects the base of the unit cube at $y = \frac{x}{2}$ . The z-coordinate of the plane never exceeds the height of the unit cube for $0 \leq x \leq 1, 0 \leq y \leq 1$ . Therefore, the volume of one of the two regions formed by the plane is \[\int_0^1 \int_{\frac{x}{2}}^1 \int_0^{\frac{y}{2}-\frac{x}{4}}dz\,dy\,dx = \frac{7}{48}\] Since $\frac{7}{48} < \frac{1}{2}$ , our answer is $1-\frac{7}{48} = \frac{41}{48} \rightarrow p+q = \boxed{089}$ .

## Solution 2 but slightly better
Same coordinate system, but we will use domains instead of using triple integrals. By the way, the method to obtain the equation of the plane is the cross product ( $\vec{[1,.5,0]}\times\vec{[0,1,.5]}=\vec{[.25,-.5,1]}$ ). We can multiply this vector by $-4$ to make things look cleaner and get $\vec{[-1,2,-4]}$ . We then get the desired plane, $-x+2y-4z=0$ , or $z=\frac{2y-x}{4}$ . We use a double integral with a Type I domain. Observing the diagram, the domain is where $0 \leq x \leq 1, .5x \leq y \leq 1$ . The integral is then \[.25\int_0^1\int_{.5x}^1 2y - x\] which becomes
which becomes \[.25\int_0^1 1-x+.25x^2\] which then becomes \[.25(1-\frac{1}{2}+\frac{1}{12})\] and finally \[\frac{7}{48}\] So our answer is $1^3-\frac{7}{48} = \frac{41}{48}, 41+48 = \boxed{089}$

## Alternative Solution (using calculus) : think inside the box
Let $Q$ be the intersection of the plane with edge $FB,$ then $\triangle MQB$ is similar to $\triangle DNC$ and the volume $[DNCMQB]$ is a sum of areas of cross sections of similar triangles running parallel to face $ABFE.$ Let $x$ be the distance from face $ABFE,$ let $h$ be the height parallel to $AB$ of the cross-sectional triangle at that distance, and $a$ be the area of the cross-sectional triangle at that distance. $A(x)=\frac{h^2}{4},$ and $h=\frac{x+1}{2},$ then $A=\frac{(x+1)^2}{16}$ , and the volume $[DNCMQB]$ is $\int^1_0{A(x)}\,\mathrm{d}x=\int^1_0{\frac{(x+1)^2}{16}}\,\mathrm{d}x=\frac{7}{48}.$ Thus the volume of the larger solid is $1-\frac{7}{48}=\frac{41}{48} \rightarrow p+q = \boxed{089}$

## Alternative Solution : think inside the box
The volume of a frustum is $\frac{h_2b_2 -h_1b_1}3$ where $b_i$ is the area of the base and $h_i$ is the height from the chopped off apex to the base.
We can easily see that from symmetry, the area of the smaller front base is $\frac{1}{16}$ and the area of the larger back base is $\frac{1}4$
Now to find the height of the apex.
Extend the $DM$ and (call the intersection of the plane with $FB$ G) $NG$ to meet at $x$ . Now from similar triangles $XMG$ and $XDN$ we can easily find the total height of the triangle $XDN$ to be $2$
Now straight from our formula, the volume is $\frac{7}{48}$ Thus the answer is:
$1-\text{Volume} \Longrightarrow \boxed{089}$

## Alternative Solution : think inside the box with pyramids
We will solve for the area of the smaller region, and then subtract it from 1.
Let $X$ be the point where plane $DMN$ intersects $FB$ . Then $DMBCNX$ can be split into triangular pyramid $DMBX$ and quadrilateral pyramid $BCNXD$ .
Pyramid $DMBX$ has base $DMB$ with area $\frac{1}2 \cdot 1 \div 2 = \frac{1}4$ . The height is $BX = \frac{1}4$ , so the volume of $DMBX$ is $\frac{1}4 \cdot \frac{1}4 \div 3 = \frac{1}{48}$ .
Similarly, pyramid $BCNXD$ has base $BCNX$ with area $(\frac{1}4 + \frac{1}2) \cdot 1 = \frac{3}8$ . The height is $CD = 1$ , so the volume of $BCNXD$ is $\frac{3}8 \cdot 1 \div 3 = \frac{1}8$ .
Adding up the volumes of $DMBX$ and $BCNXD$ , we find that the volume of $DMBCNX$ is $\frac{1}{48} + \frac{6}{48} = \frac{7}{48}$ . Therefore the volume of the larger solid is $1 - \frac{7}{48} = \frac{41}{48} \rightarrow p+q = \boxed{089}$
This is basically mathtiger6's solution, but you don't need coordinates or thinking outside the box.

## Solution outside visual

## Solution 7
We use a coordinate system with $C = (0,0,0)$ , $D = (1,0,0)$ , $M = (\frac{1}{2},1,0)$ , $N = (0,0,\frac{1}{2})$ . Then the plane going through $D$ , $M$ , and $N$ has equation $z = \frac{1}{2} - \frac{1}{2}x - \frac{1}{4}y$ . We set up a double integral in this coordinate system. Consider the region to be integrated over in the $xy$ -plane. From $x=0$ to $x=\frac{1}{2}$ , the upper bound of the region is $y = 1$ . From $x= \frac{1}{2}$ to $x=1$ , the upper bound of the region is $y = 2 - 2x$ . In both cases, the lower bound of the region is $y = 0$ . Thus, we have the double integral $\int_{0}^{\frac{1}{2}} \int_{0}^{1} \frac{1}{2} - \frac{1}{2}x - \frac{1}{4}y dydx + \int_{\frac{1}{2}}^{1} \int_{0}^{2-2x} \frac{1}{2} - \frac{1}{2}x - \frac{1}{4}y dydx$ . We find that this sum evaluates to $\frac{7}{48}$ . However, this is the volume of the smaller region, so the larger region's volume is that of the cube minus that of the smaller region. Since the cube has side length $1$ , its volume is $1$ , so the volume of the larger region is $1 - \frac{7}{48} = \frac{41}{48}$ . Thus, our answer is $41 + 48 = \boxed{089}$ .
~ cxsmi

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/344
~ dolphin7

## Video Solution
https://www.youtube.com/watch?v=LWUN_ZymNnw ~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .