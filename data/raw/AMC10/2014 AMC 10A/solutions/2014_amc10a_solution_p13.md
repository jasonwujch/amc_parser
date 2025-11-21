# 2014 AMC 10A Problem 13

## Problem

Equilateral $\triangle ABC$ has side length $1$ , and squares $ABDE$ , $BCHI$ , $CAFG$ lie outside the triangle. What is the area of hexagon $DEFGHI$ ?

[asy] import graph; size(6cm); pen dps = linewidth(0.7) + fontsize(8); defaultpen(dps); pair B = (0,0); pair C = (1,0); pair A = rotate(60,B)*C; pair E = rotate(270,A)*B; pair D = rotate(270,E)*A; pair F = rotate(90,A)*C; pair G = rotate(90,F)*A; pair I = rotate(270,B)*C; pair H = rotate(270,I)*B; draw(A--B--C--cycle); draw(A--E--D--B); draw(A--F--G--C); draw(B--I--H--C); draw(E--F); draw(D--I); draw(I--H); draw(H--G); label("$A$",A,N); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,W); label("$E$",E,W); label("$F$",F,E); label("$G$",G,SE); label("$H$",H,SE); label("$I$",I,SW); [/asy]

$\textbf{(A)}\ \dfrac{12+3\sqrt3}4\qquad\textbf{(B)}\ \dfrac92\qquad\textbf{(C)}\ 3+\sqrt3\qquad\textbf{(D)}\ \dfrac{6+3\sqrt3}2\qquad\textbf{(E)}\ 6$

## Solution 1
The area of the equilateral triangle is $\dfrac{\sqrt{3}}{4}$ . The area of the three squares is $3\times 1=3$ .
Since $\angle C=360$ , $\angle GCH=360-90-90-60=120$ .
Dropping an altitude from $C$ to $GH$ allows to create a $30-60-90$ triangle since $\triangle GCH$ is isosceles. This means that the height of $\triangle GCH$ is $\dfrac{1}{2}$ and half the length of $GH$ is $\dfrac{\sqrt{3}}{2}$ . Therefore, the area of each isosceles triangle is $\dfrac{1}{2}\times\dfrac{\sqrt{3}}{2}=\dfrac{\sqrt{3}}{4}$ . Multiplying by $3$ yields $\dfrac{3\sqrt{3}}{4}$ for all three isosceles triangles.
Therefore, the total area is $3+\dfrac{\sqrt{3}}{4}+\dfrac{3\sqrt{3}}{4}=3+\dfrac{4\sqrt{3}}{4}=3+\sqrt{3}\implies\boxed{\textbf{(C)}\ 3+\sqrt3}$ .

## Solution 2
As seen in the previous solution, segment $GH$ is $\sqrt{3}$ . Think of the picture as one large equilateral triangle, $\triangle{JKL}$ with the sides of $2\sqrt{3}+1$ , by extending $EF$ , $GH$ , and $DI$ to points $J$ , $K$ , and $L$ , respectively. This makes the area of $\triangle{JKL}$ $\dfrac{\sqrt{3}}{4}(2\sqrt{3}+1)^2=\dfrac{12+13\sqrt{3}}{4}$ .
[asy] import graph; size(10cm); pen dps = linewidth(0.7) + fontsize(8); defaultpen(dps); pair B = (0,0); pair C = (1,0); pair A = rotate(60,B)*C; pair E = rotate(270,A)*B; pair D = rotate(270,E)*A; pair F = rotate(90,A)*C; pair G = rotate(90,F)*A; pair I = rotate(270,B)*C; pair H = rotate(270,I)*B; pair J = rotate(60,I)*D; pair K = rotate(60,E)*F; pair L = rotate(60,G)*H; draw(A--B--C--cycle); draw(A--E--D--B); draw(A--F--G--C); draw(B--I--H--C); draw(E--F); draw(D--I); draw(I--H); draw(H--G); draw(I--J--D); draw(E--K--F); draw(G--L--H); label("$A$",A,N); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,W); label("$E$",E,W); label("$F$",F,E); label("$G$",G,E); label("$H$",H,SE); label("$I$",I,SW); label("$J$",J,SW); label("$K$",K,N); label("$L$",L,SE); [/asy]
Triangles $\triangle{DIJ}$ , $\triangle{EFK}$ , and $\triangle{GHL}$ have sides of $\sqrt{3}$ , so their total area is $3(\dfrac{\sqrt{3}}{4}(\sqrt{3})^2)=\dfrac{9\sqrt{3}}{4}$ .
Now, you subtract their total area from the area of $\triangle{JKL}$ :
$\dfrac{12+13\sqrt{3}}{4}-\dfrac{9\sqrt{3}}{4}=\dfrac{12+13\sqrt{3}-9\sqrt{3}}{4}=\dfrac{12+4\sqrt{3}}{4}=3+\sqrt{3}\implies\boxed{\textbf{(C)}\ 3+\sqrt3}$

## Solution 3
We will use, $\frac{1}{2}ab\sin x$ to find the area of the following triangles. Since $\angle A=360$ , $\angle EAF=360-90-90-60=120$ .
The Area of $\triangle AEF$ is $\frac{1}{2} \cdot 1 \cdot 1 \cdot \sin(120)$ . Noting, $\sin (2x) = 2\sin (x)\cos (x)$ ,
Area of $\triangle AEF = \frac{1}{2} \cdot 1 \cdot 1 \cdot 2 \cdot \sin(60) \cdot \cos(60) = \dfrac{\sqrt{3}}{4}$ ,
Area of $\triangle ABC = \frac{1}{2} \cdot 1 \cdot 1 \cdot \sin(60) = \dfrac{\sqrt{3}}{4}$ ,
Area of square ABDE = 1,
Therefore the composite area of the entire figure is, \[3 \cdot [\triangle AEF] + [\triangle ABC] + 3 \cdot [ABDE] = 3 \dfrac{\sqrt{3}}{4} + \dfrac{\sqrt{3}}{4} + 3 \cdot 1 = 4 \dfrac{\sqrt{3}}{4} + 3 = \sqrt{3} + 3 \implies\boxed{\textbf{(C)}\ 3+\sqrt3}\]

## Solution 4
We know that the area is equal to 3*EAF+3*ACGF+ABC. We also know that ACGF and the rest of the squares' area is equal to 1. Therefore the answer is 3*EAF+ABC+3. The only one with "+3" or "3+" is C, our answer. Very unreliable. -Reality Writes

## Solution 5
$\angle{AEF} = 180- \angle{BAC} = 120$
The area of the obtuse triangle is $\frac{1}{2}\sin{120} = \frac{\sqrt{3}}{4}$
The total area is $3\left(1 + \frac{\sqrt{3}}{4}\right) + \frac{\sqrt{3}}{4} = \sqrt{3} + 3$
~mathboy282

## Solution 6
The total area is the sum of the three squares, the three (congruent) obtuse triangles, and the equilateral triangle. The area of the equilateral triangle is $\frac{\sqrt{3}}{4}$ and the area of each square is $1$ . The area of a triangle in general is $\frac{1}{2}ab\sin(c)$ where $a$ and $b$ are two sides and $c$ is the included angle. $\angle EAF$ measures $120^{\circ}$ because $\angle EAB$ and $\angle FAC$ are right, and $m\angle CAB=60^{\circ}$ . So the area of the obtuse triangle is $\frac{1}{2}\cdot1\cdot1\cdot\sin\left(120^{\circ}\right)=\frac{\sqrt{3}}{4}$ . The total area is $3\left(\frac{\sqrt{3}}{4}\right)+3\left(1\right)+\frac{\sqrt{3}}{4}=\sqrt{3}+3 \Longrightarrow \boxed{\textbf{(C )}\sqrt{3}+3}$ .
~JH. L

## Solution 7
Since $\angle C=360$ , $\angle GCH=360-90-90-60=120.$ Applying the Law of Cosines on $\angle GCH$ gives us $GH = 1.$ Since $\triangle GCH$ is isosceles, the perpendicular bisector of $\angle C$ also intersects segment $\overline{GH}$ in its median, which we can call point $M.$ Hence, we can apply the Pythagorean theorem on $\triangle CMG$ or $\triangle CMH$ to get $CM = \frac{\sqrt{3}}{4}.$ We can use this to get the area of the triangle and multiply that by three since the triangles are congruent. The result follows. ~peelybonehead

## Solution 8
First, the equilateral triangle has an area of $\dfrac{\sqrt{3}}{4}$ . The three squares have an area of $3\times 1=3$ .
Since $\angle C=360$ , $\angle GCH=360-90-90-60=120$ . Notice that the three outer isosceles triangles combine to form a new equilateral triangle $\triangle IEG$ . Because it is an equilateral triangle, the two parts of the median separated by the centroid form a ratio of 2:1. Therefore, The altitude of $\triangle IEG$ is $\dfrac{3}{2}$ . That same attitude also creates two 30-60-90 triangles meaning that half of the base of equilateral triangle $\triangle IEG$ is $\dfrac{3}{2\sqrt{3}}=\dfrac{3\sqrt{3}}{6}=\dfrac{\sqrt{3}}{2}$ . Multiplying this by the height yields the area of the triangle to be $\dfrac{{3}\sqrt{3}}{4}$ . Adding all the areas up produces $3+\dfrac{\sqrt{3}}{4}+\dfrac{3\sqrt{3}}{4}=3+\dfrac{4\sqrt{3}}{4}=3+\sqrt{3}\implies\boxed{\textbf{(C)}\ 3+\sqrt3}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .