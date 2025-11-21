# 2001 AIME I Problem 12

## Problem

A sphere is inscribed in the tetrahedron whose vertices are $A = (6,0,0), B = (0,4,0), C = (0,0,2),$ and $D = (0,0,0).$ The radius of the sphere is $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

## Solution 1
[asy] import three; currentprojection = perspective(-2,9,4); triple A = (6,0,0), B = (0,4,0), C = (0,0,2), D = (0,0,0); triple E = (2/3,0,0), F = (0,2/3,0), G = (0,0,2/3), L = (0,2/3,2/3), M = (2/3,0,2/3), N = (2/3,2/3,0); triple I = (2/3,2/3,2/3); triple J = (6/7,20/21,26/21); draw(C--A--D--C--B--D--B--A--C); draw(L--F--N--E--M--G--L--I--M--I--N--I--J); label("$I$",I,W); label("$A$",A,S); label("$B$",B,S); label("$C$",C,W*-1); label("$D$",D,W*-1); [/asy]
The center $I$ of the insphere must be located at $(r,r,r)$ where $r$ is the sphere's radius. $I$ must also be a distance $r$ from the plane $ABC$
The signed distance between a plane and a point $I$ can be calculated as $\frac{(I-G) \cdot P}{|P|}$ , where G is any point on the plane, and P is a vector perpendicular to ABC.
A vector $P$ perpendicular to plane $ABC$ can be found as $V=(A-C)\times(B-C)=\langle 8, 12, 24 \rangle$
Thus $\frac{(I-C) \cdot P}{|P|}=-r$ where the negative comes from the fact that we want $I$ to be in the opposite direction of $P$
\begin{align*}\frac{(I-C) \cdot P}{|P|}&=-r\\ \frac{(\langle r, r, r \rangle-\langle 0, 0, 2 \rangle) \cdot P}{|P|}&=-r\\ \frac{\langle r, r, r-2 \rangle \cdot \langle 8, 12, 24 \rangle}{\langle 8, 12, 24 \rangle}&=-r\\ \frac{44r -48}{28}&=-r\\ 44r-48&=-28r\\ 72r&=48\\ r&=\frac{2}{3} \end{align*}
Finally $2+3=\boxed{005}$

## Solution 2
Notice that we can split the tetrahedron into $4$ smaller tetrahedrons such that the height of each tetrahedron is $r$ and the base of each tetrahedron is one of the faces of the original tetrahedron. This is because the bases of the tetrahedrons are tangent to the sphere, so the line from the center to the foot of the perpendicular to the bases hits the tangency points. Letting volume be $V$ and surface area be $F$ , using the volume formula for each pyramid(base times height divided by 3) we have $\dfrac{rF}{3}=V$ . The surface area of the pyramid is $\dfrac{6\cdot{4}+6\cdot{2}+4\cdot{2}}{2}+[ABC]=22+[ABC]$ . We know triangle ABC's side lengths, $\sqrt{2^{2}+4^{2}}, \sqrt{2^{2}+6^{2}},$ and $\sqrt{4^{2}+6^{2}}$ , so using the expanded form of heron's formula, \begin{align*}[ABC]&=\sqrt{\dfrac{2(a^{2}b^{2}+b^{2}c^{2}+a^{2}c^{2})-a^{4}-b^{4}-c^{4}}{16}}\\ &=\sqrt{2(5\cdot{13}+10\cdot{5}+13\cdot{10})-5^{2}-10^{2}-13^{2}}\\ &=\sqrt{196}\\ &=14\end{align*} Therefore, the surface area is $14+22=36$ , and the volume is $\dfrac{[BCD]\cdot{6}}{3}=\dfrac{4\cdot{2}\cdot{6}}{3\cdot{2}}=8$ , and using the formula above that $\dfrac{rF}{3}=V$ , we have $12r=8$ and thus $r=\dfrac{2}{3}$ , so the desired answer is $2+3=\boxed{005}$ .
(Solution by Shaddoll)

## Solution 3
The intercept form equation of the plane $ABC$ is $\frac{x}{6}+\dfrac{y}{4}+\dfrac{z}{2}=1.$ Its normal form is $\dfrac{2}{7}x+\dfrac{3}{7}y+\dfrac{6}{7}z-\dfrac{12}{7}=0$ (square sum of the coefficients equals 1). The distance from $(r,r,r)$ to the plane is $\left |\dfrac{2}{7}r+\dfrac{3}{7}r+\dfrac{6}{7}r-\dfrac{12}{7}\right |$ . Since $(r,r,r)$ and $(0,0,0)$ are on the same side of plane, the value in the absolute value sign is negative (same as the one by plugging in $(0,0,0)$ ). Therefore we have $-\left (\dfrac{2}{7}r+\dfrac{3}{7}r+\dfrac{6}{7}r-\dfrac{12}{7}\right )=r.$ So $r=\dfrac{2}{3},$ which solves the problem.
Additionally, if $(r,r,r)$ is on the other side of $ABC$ , we have $\left (\dfrac{2}{7}r+\dfrac{3}{7}r+\dfrac{6}{7}r-\dfrac{12}{7}\right )=r$ , which yields $r=\dfrac{12}{5},$ corresponding an "ex-sphere" that is tangent to face $ABC$ as well as the extensions of the other 3 faces.
-JZ

## Solution 4
First let us find the equation of the plane passing through $(6,0,0), (0,0,2), (0,4,0)$ . The "point-slope form" is $A(6-x1)+B(0-y1)+C(0-z1)=0.$ Plugging in $(0,0,2)$ gives $A(6)+B(0)+C(-2)=0.$ Plugging in $(0,4,0)$ gives $A(6)+B(-4)+C(0)=0.$ We can then use Cramer's rule/cross multiplication to get $A/(0-8)=-B/(0+12)=C/(-24)=k.$ Solve for A, B, C to get $2k, 3k, 6k$ respectively. We can then get $2k(x-x1)+3k(y-y1)+6k(z-z1)=0.$ Cancel out k on both sides. Next, let us substitute $(0,0,2)$ . We can then get $2x+3y+6z=12$ as the equation of the plane. We can divide the equation by its magnitude to get the normal form of the plane. We get $2x/7+2y/7+6z/7=12/7$ to be the normal form. Note that the point is going to be at $(r,r,r).$ We find the distance from $(r,r,r)$ to the plane as $2/7r+3/7r+6/7r-12/7/(\sqrt{(4/49+9/49+36/49)})$ , which is $+/-(11r/7-12/7)$ . We take the negative value of this because if we plug in $(0,0,0)$ to the equation of the plane we get a negative value. We equate that value to r and we get the equation $-(11r/7-12/7)=r$ to solve $r={2/3}$ , so the answer is $\boxed{005}$ .

## Solution 5
Clearly, if the radius of the sphere is $r$ , the center of the sphere lies on $(r, r, r)$ .
We find the equation of plane $ABC$ to be $\frac16 x+\frac14 y+\frac12 z=1$ . From the definition of the insphere, it must be true that the distance from the center of the sphere to plane $ABC$ is equal to the length of the radius of the sphere. By point-to-plane, we have \[r=\frac{|\frac16 r+\frac14 r+\frac12 r-1|}{\sqrt{\left(\frac16\right)^2+\left(\frac14\right)^2+\left(\frac12\right)^2}} \implies r=\frac23,\] so the answer is $\boxed{005}$ .
-pqr.

## Solution 6(Formula Bash)
The radius of the insphere in a tetrahedron can be calculated using the formula $r = \frac{3V}{A}$ , where $r$ is the radius, $V$ is the volume of the tetrahedron, and $A$ is the total surface area of the tetrahedron.
We calculate the volume of the tetrahedron as: \[V = \frac{2 \times 4 \times 6}{6} = 8\]
Next, we find the total surface area as the sum of the areas of the four triangular faces: \[\text{Surface Area} = [ABD] + [BDC] + [ACD] + [ABC] = 12 + 4 + 6 + [ABC]\]
The side lengths of triangle $ABC$ are $\sqrt{52}$ , $\sqrt{40}$ , and $\sqrt{20}$ . Constructing an altitude from $A$ and using the system of equations $x^2 + h^2 = 40$ and $(2\sqrt{5} - x)^2 + h^2 = 20$ , we solve for $h$ and get: \[h = \frac{14\sqrt{5}}{5}\]
Thus, the area of triangle $ABC$ is: \[\text{Area of } [ABC] = 14\]
Now, the total surface area is: \[A = 12 + 4 + 6 + 14 = 36\] Finally, using the formula for the radius, we have: \[r = \frac{3 \times 8}{36} = \frac{2}{3}\] $\boxed{005}$
These problems are copyrighted © by the Mathematical Association of America.