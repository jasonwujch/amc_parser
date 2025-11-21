# 2009 AMC 10B Problem 18

## Problem

Rectangle $ABCD$ has $AB=8$ and $BC=6$ . Point $M$ is the midpoint of diagonal $\overline{AC}$ , and $E$ is on $AB$ with $\overline{ME}\perp\overline{AC}$ . What is the area of $\triangle AME$ ?

$\text{(A) } \frac{65}{8} \qquad \text{(B) } \frac{25}{3} \qquad \text{(C) } 9 \qquad \text{(D) } \frac{75}{8} \qquad \text{(E) } \frac{85}{8}$

## Solution 1 (Coordinate Geometry)
Set $A$ to $(0,0)$ . Since $M$ is the midpoint of the diagonal, it would be $(4,3)$ . The diagonal $AC$ would be the line $y = \frac{3x}{4}$ . Since $ME$ is perpendicular to $AC$ , its line would be in the form $y = -\frac{4x}{3} + b$ . Plugging in $4$ and $3$ for $x$ and $y$ would give $b = \frac{25}{3}$ . To find the x-intercept of $y = -\frac{4x}{3} + \frac{25}{3}$ we plug in $0$ for $y$ and get $x = \frac{25}{4}$ . Then, using the Shoelace Formula for $(0,0)$ , $(4,3)$ , and $(\frac{25}{4}, 0)$ , we find the area is $\frac{75}{8}$ .

## Solution 2
[asy] unitsize(0.75cm); defaultpen(0.8); pair A=(0,0), B=(8,0), C=(8,6), D=(0,6), M=(A+C)/2; path ortho = shift(M)*rotate(-90)*(A--C); pair Ep = intersectionpoint(ortho, A--B); draw( A--B--C--D--cycle ); draw( A--C ); draw( M--Ep ); filldraw( A--M--Ep--cycle, lightgray, black ); draw( rightanglemark(A,M,Ep) ); draw( C--Ep ); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,NE); label("$D$",D,NW); label("$E$",Ep,S); label("$M$",M,NW); [/asy]
By the Pythagorean theorem we have $AC=10$ , hence $AM=5$ .
The triangles $AME$ and $ABC$ have the same angle at $A$ and a right angle, thus all their angles are equal, and therefore these two triangles are similar.
The ratio of their sides is $\frac{AM}{AB} = \frac 58$ , hence the ratio of their areas is $\left( \frac 58 \right)^2 = \frac{25}{64}$ .
And as the area of triangle $ABC$ is $\frac{6\cdot 8}2 = 24$ , the area of triangle $AME$ is $24\cdot \frac{25}{64} = \boxed{ \frac{75}8 }$ .

## Solution 3 (Only Pythagorean Theorem)
[asy] unitsize(0.75cm); defaultpen(0.8); pair A=(0,0), B=(8,0), C=(8,6), D=(0,6), M=(A+C)/2; path ortho = shift(M)*rotate(-90)*(A--C); pair Ep = intersectionpoint(ortho, A--B); draw( A--B--C--D--cycle ); draw( A--C ); draw( M--Ep ); filldraw( A--M--Ep--cycle, lightgray, black ); draw( rightanglemark(A,M,Ep) ); draw( C--Ep ); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,NE); label("$D$",D,NW); label("$E$",Ep,S); label("$M$",M,NW); [/asy]
Draw $EC$ as shown from the diagram. Since $AC$ is of length $10$ , we have that $AM$ is of length $5$ , because of the midpoint $M$ . Through the Pythagorean theorem, we know that $AE^2 = AM^2 + ME^2 \implies 25 + ME^2$ , which means $AE = \sqrt{25 + ME^2}$ . Define $ME$ to be $x$ for the sake of clarity. We know that $EB = 8 - \sqrt{25 + x^2}$ . From here, we know that $CE^2 = CB^2 + BE^2 = ME^2 + MC^2$ . From here, we can write the expression $6^2 + (8 - \sqrt{25 + x^2})^2 = 5^2 + x^2 \implies 36 + (64 - 16\sqrt{25 + x^2} + 25 + x^2) = 25 + x^2 \implies 100 - 16\sqrt{25 + x^2} \implies \sqrt{25 + x^2} = \frac{25}{4} \implies 25 + x^2 = \frac{625}{16} \implies 400 + 16x^2 = 625 \implies 16x^2 = 225 \implies x = \frac{15}{4}$ . Now, remember $CE \neq \frac{15}{4}$ . $x = \frac{15}{4} = ME$ , since we set $x = ME$ in the start of the solution. Now to find the area $\frac{15}{4} \cdot 5 \cdot \frac{1}{2} = \frac{75}{8} = CE$

## Solution 4 (Similarity)
We know $AM = \frac{10}{2} = 5$ by the Pythagorean theorem, and furthermore, $\triangle AME$ is similar to $\triangle ABC$ . Therefore, $ME = 5 \cdot \frac{6}{8} = \frac{15}{4}$ , and the area of the triangle is $5 \cdot \frac{15}{4} \cdot \frac{1}{2} = \boxed{\frac{75}{8}}$ .

## Solution 5 (Pythagorean Theorem)
[asy] unitsize(0.75cm); defaultpen(0.8); pair A=(0,0), B=(8,0), C=(8,6), D=(0,6), M=(A+C)/2; path ortho = shift(M)*rotate(-90)*(A--C); pair Ep = intersectionpoint(ortho, A--B); draw( A--B--C--D--cycle ); draw( A--C ); draw( M--Ep ); filldraw( A--M--Ep--cycle, lightgray, black ); draw( rightanglemark(A,M,Ep) ); draw( C--Ep ); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,NE); label("$D$",D,NW); label("$E$",Ep,S); label("$M$",M,NW); [/asy]
By the Pythagorean Theorem , we claim that $AC = 10$ . It then follows that $AM \cong MC = 5.$
Because we have $AM \cong MC, \angle AME \cong \angle CME,$ and reflexive side $EM$ , it follows that $\triangle AME \cong \triangle CME.$ By CPCTC, we have $AE \cong EC.$ For the sake of simplicity, we'll call those side lengths $x$ . Also, since $AE = x,$ we get $BE = 8 - x.$ We can now set up the Pythagorean theorem on $\triangle EBC$ : \[(8 - x)^2 + 6^2 = x^2.\] Combining like terms and simplifying gives $-16x + 100 = 0$ so $x = \frac{25}{4}.$
It helps to think that in order to find $[AME],$ we must have $\overline{MC}$ and $\overline{EM}.$ Let $EM = y.$ Applying the Pythagorean Theorem to $\triangle CME$ gives \[5^2 + y^2 = \left(\frac{25}{4} \right)^2.\] Solving for $y$ (this is not that difficult) gives $y = \frac{15}{4}.$ So, the area of $\triangle AME$ is $\frac{\frac{15}{4} \cdot 5}{2} = \frac{75}{8} \implies \boxed{D}.$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .