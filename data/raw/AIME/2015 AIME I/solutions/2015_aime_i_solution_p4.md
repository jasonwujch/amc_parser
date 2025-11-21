# 2015 AIME I Problem 4

## Problem

Point $B$ lies on line segment $\overline{AC}$ with $AB=16$ and $BC=4$ . Points $D$ and $E$ lie on the same side of line $AC$ forming equilateral triangles $\triangle ABD$ and $\triangle BCE$ . Let $M$ be the midpoint of $\overline{AE}$ , and $N$ be the midpoint of $\overline{CD}$ . The area of $\triangle BMN$ is $x$ . Find $x^2$ .

### Diagram

[asy] pair A = (0, 0), B = (16, 0), C = (20, 0), D = (8, 8*sqrt(3)), EE = (18, 2*sqrt(3)), M = (9, sqrt(3)), NN = (14, 4*sqrt(3)); draw(A--B--D--cycle); draw(B--C--EE--cycle); draw(A--EE); draw(C--D); draw(B--M--NN--cycle); dot(A); dot(B); dot(C); dot(D); dot(EE); dot(M); dot(NN); label("A", A, SW); label("B", B, S); label("C", C, SE); label("D", D, N); label("E", EE, N); label("M", M, NW); label("N", NN, NE); [/asy]

Diagram by RedFireTruck ( talk )

## Solution 1
Let $A$ be the origin, so $B=(16,0)$ and $C=(20,0).$ Using equilateral triangle properties tells us that $D=(8,8\sqrt3)$ and $E=(18,2\sqrt3)$ as well. Therefore, $M=(9,\sqrt3)$ and $N=(14,4\sqrt3).$ Applying the Shoelace Theorem to triangle $BMN$ gives
\[x=\dfrac 1 2 |16\sqrt3+36\sqrt3+0-(0+14\sqrt3+64\sqrt3)| =13\sqrt3,\]
so $x^2=\boxed{507}.$

## Solution 2
Note that $AB=DB=16$ and $BE=BC=4$ . Also, $\angle ABE = \angle DBC = 120^{\circ}$ . Thus, $\triangle ABE \cong \triangle DBC$ by SAS.
From this, it is clear that a $60^{\circ}$ rotation about $B$ will map $\triangle ABE$ to $\triangle DBC$ . This rotation also maps $M$ to $N$ . Thus, $BM=BN$ and $\angle MBN=60^{\circ}$ . Thus, $\triangle BMN$ is equilateral.
Using the Law of Cosines on $\triangle ABE$ , \[AE^2 = 16^2 + 4^2 - 2\cdot 16\cdot 4\cdot\left(-\frac{1}{2}\right)\] \[AE = 4\sqrt{21}\] Thus, $AM=ME=2\sqrt{21}$ .
Using Stewart's Theorem on $\triangle ABE$ , \[AM\cdot ME\cdot AE + AE\cdot BM^2 = BE^2\cdot AM + BA^2\cdot ME\] \[BM = 2\sqrt{13}\]
Calculating the area of $\triangle BMN$ , \[[BMN] = \frac{\sqrt{3}}{4} BM^2\] \[[BMN] = 13\sqrt{3}\] Thus, $x=13\sqrt{3}$ , so $x^2 = 507$ . Our final answer is $\boxed{507}$ .
Admittedly, this is much more tedious than the coordinate solutions.
I also noticed that there are two more ways of showing that $\triangle BMN$ is equilateral:
One way is to show that $\triangle ADB$ , $\triangle BMN$ , and $\triangle ECB$ are related by a spiral similarity centered at $B$ .
The other way is to use the Mean Geometry Theorem. Note that $\triangle BCE$ and $\triangle BDA$ are similar and have the same orientation. Note that $B$ is the weighted average of $B$ and $B$ , $M$ is the weighted average of $E$ and $A$ , and $N$ is the weighted average of $C$ and $D$ . The weights are the same for all three averages. (The weights are actually just $\frac{1}{2}$ and $\frac{1}{2}$ , so these are also unweighted averages.) Thus, by the Mean Geometry Theorem, $\triangle BMN$ is similar to both $\triangle BAD$ and $\triangle BEC$ , which means that $\triangle BMN$ is equilateral.
Note: A much easier way to go about finding $BM$ without having to use Stewart's Theorem is to simply drop the altitudes from M and E to AC, thus hitting AC at points X and Y. Then clearly AEY and AMX are similar with ratio 2. But we know that $AY = 18 \implies AX = 9 \implies BX = 16-9 = 7$ . Additionally, $MX = \frac{1}{2} (2\sqrt{3}) = \sqrt{3}$ from similar triangles meaning we can now just do pythagorean theorem on right triangle $MXB$ to get $MB = \sqrt{52}$ - SuperJJ

## Solution 3
$AB = BD, BE = BC, \angle ABE = \angle CBD \implies \triangle ABE \cong \triangle DBC$
Medians are equal, so $MB = BN, \angle ABM = \angle DBN \implies$ $\angle MBN = \angle ABD - \angle ABM + \angle DBN = 60^\circ \implies$
$\triangle MNB$ is equilateral triangle.
The height of $\triangle BCE$ is $2 \sqrt{3},$ distance from $A$ to midpoint $BC$ is $16 + 2 = 18 \implies \frac {AE^2}{4} =\frac{ (16 + 2)^2 +2^2 \cdot 3}{4} = 81 + 3 = 84.$
$BM$ is the median of $\triangle ABE \implies$ $BM^2 = \frac {AB^2}{2} + \frac {BE^2}{2} - \frac {AE^2}{4}=16 \cdot 8 + 4 \cdot 2 - 84 = 52.$
The area of $\triangle BMN$
\[[BMN] = \frac{\sqrt{3}}{4} BM^2 =13 \sqrt{3} \implies \boxed{\textbf{507}}.\]
vladimir.shelomovskii@gmail.com, vvsss
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .