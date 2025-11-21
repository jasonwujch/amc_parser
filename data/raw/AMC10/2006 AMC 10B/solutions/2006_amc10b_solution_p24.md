# 2006 AMC 10B Problem 24

## Problem

Circles with centers $O$ and $P$ have radii $2$ and $4$ , respectively, and are externally tangent. Points $A$ and $B$ on the circle with center $O$ and points $C$ and $D$ on the circle with center $P$ are such that $AD$ and $BC$ are common external tangents to the circles. What is the area of the concave hexagon $AOBCPD$ ?

[asy]size(200);defaultpen(linewidth(0.8)); pair X=(-6,0), O=origin, P=(6,0), B=tangent(X, O, 2, 1), A=tangent(X, O, 2, 2), C=tangent(X, P, 4, 1), D=tangent(X, P, 4, 2); pair top=X+15*dir(X--A), bottom=X+15*dir(X--B); draw(Circle(O, 2)^^Circle(P, 4)); draw(bottom--X--top); draw(A--O--B^^O--P^^D--P--C); pair point=X; label("$2$", midpoint(O--A), dir(point--midpoint(O--A))); label("$4$", midpoint(P--D), dir(point--midpoint(P--D))); label("$O$", O, SE); label("$P$", P, dir(point--P)); pair point=O; label("$A$", A, dir(point--A)); label("$B$", B, dir(point--B)); pair point=P; label("$C$", C, dir(point--C)); label("$D$", D, dir(point--D)); fill((-3,7)--(-3,-7)--(-7,-7)--(-7,7)--cycle, white);[/asy]

$\mathrm{(A) \ } 18\sqrt{3}\qquad \mathrm{(B) \ } 24\sqrt{2}\qquad \mathrm{(C) \ } 36\qquad \mathrm{(D) \ } 24\sqrt{3}\qquad \mathrm{(E) \ } 32\sqrt{2}$

## Video Solution 1
https://youtu.be/cdjZ9Xd3Yt8 [Class:Geometry] ~ Education, the Study of Everything

## Solution 1 (Similar Triangles)
When we see this problem, it practically screams similar triangles at us. Extend $OP$ to the left until it intersects lines $AD$ and $BC$ at point $E$ . Triangles $EBO$ and $ECP$ are similar, and by symmetry, so are triangles $EAO$ and $EDP$ . Then, the area of kite $EAOB$ is just $4 \sqrt{2} \times 2$ and the area of kite $EDPC$ is $8 \sqrt{2} \times 4$ (using our similarity ratios). The difference of these yields the area of hexagon $AOBCPD$ or $24\sqrt{2} \Longrightarrow \boxed{\mathrm{(B)}}$ .
~icecreamrolls8

## Solution 2 (Perpendiculars)
File is too big, so go to https://www.imgur.com/a/7aphGaa
Sorry for the wrong point names, I didn't know how to change them.
Since a tangent line is perpendicular to the radius containing the point of tangency, $\angle OAD = \angle PDA = 90^\circ$ .
Construct a perpendicular to $DP$ that goes through point $O$ . Label the point of intersection $X$ .
Clearly $OADX$ is a rectangle , so $DX=2$ and $PX=2$ . By the Pythagorean Theorem , $OX = \sqrt{6^2 - 2^2} = 4\sqrt{2}$ .
The area of $OADX$ is $2\cdot4\sqrt{2}=8\sqrt{2}$ . The area of $OXP$ is $\frac{1}{2}\cdot2\cdot4\sqrt{2}=4\sqrt{2}$ , so the area of quadrilateral $OADP$ is $8\sqrt{2}+4\sqrt{2}=12\sqrt{2}$ . Using similar steps, the area of quadrilateral $OBCP$ is also $12\sqrt{2}$ . Therefore, the area of hexagon $AOBCPD$ is $2\cdot12\sqrt{2}= 24\sqrt{2} \Longrightarrow \boxed{\mathrm{(B)}}$ .
Note: Quadrilaterals $OADP$ and $OBCP$ are congruent, so they have equal areas.

## Video Solution
https://www.youtube.com/watch?v=EmUfNAxLZ7A ~David
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .