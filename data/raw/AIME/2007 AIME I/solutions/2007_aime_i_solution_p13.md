# 2007 AIME I Problem 13

## Problem

A square pyramid with base $ABCD$ and vertex $E$ has eight edges of length $4$ . A plane passes through the midpoints of $AE$ , $BC$ , and $CD$ . The plane's intersection with the pyramid has an area that can be expressed as $\sqrt{p}$ . Find $p$ .

## Solution

## Solution 1
Note first that the intersection is a pentagon .
Use 3D analytical geometry, setting the origin as the center of the square base and the pyramid’s points oriented as shown above. $A(-2,2,0),\ B(2,2,0),\ C(2,-2,0),\ D(-2,-2,0),\ E(0,0,2\sqrt{2})$ . Using the coordinates of the three points of intersection $(-1,1,\sqrt{2}),\ (2,0,0),\ (0,-2,0)$ , it is possible to determine the equation of the plane. The equation of a plane resembles $ax + by + cz = d$ , and using the points we find that $2a = d \Longrightarrow d = \frac{a}{2}$ , $-2b = d \Longrightarrow d = \frac{-b}{2}$ , and $-a + b + \sqrt{2}c = d \Longrightarrow -\frac{d}{2} - \frac{d}{2} + \sqrt{2}c = d \Longrightarrow c = d\sqrt{2}$ . It is then $x - y + 2\sqrt{2}z = 2$ .
[asy]import three; pointpen = black; pathpen = black+linewidth(0.7); currentprojection = perspective(2.5,-12,4); triple A=(-2,2,0), B=(2,2,0), C=(2,-2,0), D=(-2,-2,0), E=(0,0,2*2^.5), P=(A+E)/2, Q=(B+C)/2, R=(C+D)/2, Y=(-3/2,-3/2,2^.5/2),X=(3/2,3/2,2^.5/2); draw(A--B--C--D--A--E--B--E--C--E--D); label("A",A, SE); label("B",B,(1,0,0)); label("C",C, SE); label("D",D, W); label("E",E,N); label("P",P, NW); label("Q",Q,(1,0,0)); label("R",R, S); label("Y",Y,NW); label("X",X,NE); draw(P--X--Q--R--Y--cycle,linetype("6 6")+linewidth(0.7)); [/asy] [asy] pointpen = black; pathpen = black+linewidth(0.7); pair P = (0, 2.5^.5), X = (3/2^.5,0), Y = (-3/2^.5,0), Q = (2^.5,-2.5^.5), R = (-2^.5,-2.5^.5); D(MP("P",P,N)--MP("X",X,NE)--MP("Q",Q)--MP("R",R)--MP("Y",Y,NW)--cycle); D(X--Y,linetype("6 6") + linewidth(0.7)+blue); D(P--(0,-P.y),linetype("6 6") + linewidth(0.7) + red); MP("\color{blue}{3\sqrt{2}}",(X+Y)/2); MP("2\sqrt{2}",(Q+R)/2); MP("\color{red}{\sqrt{\frac{5}{2}}}",(0,-P.y/2),E); MP("\color{red}{\sqrt{\frac{5}{2}}}",(0,2*P.y/5),E); [/asy]
Write the equation of the lines and substitute to find that the other two points of intersection on $\overline{BE}$ , $\overline{DE}$ are $\left(\frac{\pm 3}{2},\frac{\pm 3}{2},\frac{\sqrt{2}}{2}\right)$ . To find the area of the pentagon, break it up into pieces (an isosceles triangle on the top, an isosceles trapezoid on the bottom). Using the distance formula ( $\sqrt{a^2 + b^2 + c^2}$ ), it is possible to find that the area of the triangle is $\frac{1}{2}bh \Longrightarrow \frac{1}{2} 3\sqrt{2} \cdot \sqrt{\frac 52} = \frac{3\sqrt{5}}{2}$ . The trapezoid has area $\frac{1}{2}h(b_1 + b_2) \Longrightarrow \frac 12\sqrt{\frac 52}\left(2\sqrt{2} + 3\sqrt{2}\right) = \frac{5\sqrt{5}}{2}$ . In total, the area is $4\sqrt{5} = \sqrt{80}$ , and the solution is $\boxed{080}$ .

## Solution 2
Use the same coordinate system as above, and let the plane determined by $\triangle PQR$ intersect $\overline{BE}$ at $X$ and $\overline{DE}$ at $Y$ . Then the line $\overline{XY}$ is the intersection of the planes determined by $\triangle PQR$ and $\triangle BDE$ .
Note that the plane determined by $\triangle BDE$ has the equation $x=y$ , and $\overline{PQ}$ can be described by $x=2(1-t)-t,\ y=t,\ z=t\sqrt{2}$ . It intersects the plane when $2(1-t)-t=t$ , or $t=\frac{1}{2}$ . This intersection point has $z=\frac{\sqrt{2}}{2}$ . Similarly, the intersection between $\overline{PR}$ and $\triangle BDE$ has $z=\frac{\sqrt{2}}{2}$ . So $\overline{XY}$ lies on the plane $z=\frac{\sqrt{2}}{2}$ , from which we obtain $X=\left( \frac{3}{2},\frac{3}{2},\frac{\sqrt{2}}{2}\right)$ and $Y=\left( -\frac{3}{2},-\frac{3}{2},\frac{\sqrt{2}}{2}\right)$ . The area of the pentagon $EXQRY$ can be computed in the same way as above.

## Solution 3
[asy]import three; import math; pointpen = black; pathpen = black+linewidth(0.7); currentprojection = perspective(2.5,-12,4); triple A=(-2,2,0), B=(2,2,0), C=(2,-2,0), D=(-2,-2,0), E=(0,0,2*2^.5), P=(A+E)/2, Q=(B+C)/2, R=(C+D)/2, Y=(-3/2,-3/2,2^.5/2),X=(3/2,3/2,2^.5/2), H=(4,2,0), I=(-2,-4,0); draw(A--B--C--D--A--E--B--E--C--E--D); draw(B--H--Q, linetype("6 6")+linewidth(0.7)+blue); draw(X--H, linetype("6 6")+linewidth(0.7)+blue); draw(D--I--R, linetype("6 6")+linewidth(0.7)+blue); draw(Y--I, linetype("6 6")+linewidth(0.7)+blue); label("A",A, SE); label("B",B,NE); label("C",C, SE); label("D",D, W); label("E",E,N); label("P",P, NW); label("Q",Q,(1,0,0)); label("R",R, S); label("Y",Y,NW); label("X",X,NE); label("H",H,NE); label("I",I,S); draw(P--X--Q--R--Y--cycle,linetype("6 6")+linewidth(0.7)); [/asy]
Extend $\overline{RQ}$ and $\overline{AB}$ . The point of intersection is $H$ . Connect $\overline{PH}$ . $\overline{EB}$ intersects $\overline{PH}$ at $X$ . Do the same for $\overline{QR}$ and $\overline{AD}$ , and let the intersections be $I$ and $Y$
Because $Q$ is the midpoint of $\overline{BC}$ , and $\overline{AB}\parallel\overline{DC}$ , so $\triangle{RQC}\cong\triangle{HQB}$ . $\overline{BH}=2$ .
Because $\overline{BH}=2$ , we can use mass point geometry to get that $\overline{PX}=\overline{XH}$ . $|\triangle{XHQ}|=\frac{\overline{XH}}{\overline{PH}}\cdot\frac{\overline{QH}}{\overline{HI}}\cdot|\triangle{PHI}|=\frac{1}{6}\cdot|\triangle{PHI}|$
Using the same principle, we can get that $|\triangle{IYR}|=\frac{1}{6}|\triangle{PHI}|$
Therefore, the area of $PYRQX$ is $\frac{2}{3}\cdot|\triangle{PHI}|$
$\overline{RQ}=2\sqrt{2}$ , so $\overline{IH}=6\sqrt{2}$ . Using the law of cosines, $\overline{PH}=\sqrt{28}$ . The area of $\triangle{PHI}=\frac{1}{2}\cdot\sqrt{28-18}\cdot6\sqrt{2}=6\sqrt{5}$
Using this, we can get the area of $PYRQX = \sqrt{80}$ so the answer is $\fbox{080}$ .

## Video Solution
2007 AIME I #13
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.