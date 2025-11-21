# 2008 AIME II Problem 5

## Problem

In trapezoid $ABCD$ with $\overline{BC}\parallel\overline{AD}$ , let $BC = 1000$ and $AD = 2008$ . Let $\angle A = 37^\circ$ , $\angle D = 53^\circ$ , and $M$ and $N$ be the midpoints of $\overline{BC}$ and $\overline{AD}$ , respectively. Find the length $MN$ .

## Solution

## Solution 1
Extend $\overline{AB}$ and $\overline{CD}$ to meet at a point $E$ . Then $\angle AED = 180 - 53 - 37 = 90^{\circ}$ .
As $\angle AED = 90^{\circ}$ , note that the midpoint of $\overline{AD}$ , $N$ , is the center of the circumcircle of $\triangle AED$ . We can do the same with the circumcircle about $\triangle BEC$ and $M$ (or we could apply the homothety to find $ME$ in terms of $NE$ ). It follows that
\[NE = ND = \frac {AD}{2} = 1004, \quad ME = MC = \frac {BC}{2} = 500.\]
Thus $MN = NE - ME = \boxed{504}$ .
For purposes of rigor we will show that $E,M,N$ are collinear. Since $\overline{BC} \parallel \overline{AD}$ , then $BC$ and $AD$ are homothetic with respect to point $E$ by a ratio of $\frac{BC}{AD} = \frac{125}{251}$ . Since the homothety carries the midpoint of $\overline{BC}$ , $M$ , to the midpoint of $\overline{AD}$ , which is $N$ , then $E,M,N$ are collinear .

## Solution 2
Let $F,G,H$ be the feet of the perpendiculars from $B,C,M$ onto $\overline{AD}$ , respectively. Let $x = NH$ , so $DG = 1004 - 500 - x = 504 - x$ and $AF = 1004 - (500 - x) = 504 + x$ . Also, let $h = BF = CG = HM$ .
By AA~, we have that $\triangle AFB \sim \triangle CGD$ , and so \[\frac{BF}{AF} = \frac {DG}{CG} \Longleftrightarrow \frac{h}{504+x} = \frac{504-x}{h} \Longrightarrow x^2 + h^2 = 504^2.\]
By the Pythagorean Theorem on $\triangle MHN$ , \[MN^{2} = x^2 + h^2 = 504^2,\] so $MN = \boxed{504}$ .

## Solution 3
If you drop perpendiculars from $B$ and $C$ to $AD$ , and call the points where they meet $\overline{AD}$ , $E$ and $F$ respectively, then $FD = x$ and $EA = 1008-x$ , and so you can solve an equation in tangents. Since $\angle{A} = 37$ and $\angle{D} = 53$ , you can solve the equation [by cross-multiplication]:
\begin{align*}\tan{37}\times (1008-x) &= \tan{53} \times x\\ \frac{(1008-x)}{x} &= \frac{\tan{53}}{\tan{37}} = \frac{\sin{53}}{\cos{53}} \times\frac{\cos{37}}{\sin{37}}\end{align*}
However, we know that $\cos{90-x} = \sin{x}$ and $\sin{90-x} = \cos{x}$ are co-functions. Applying this,
\begin{align*}\frac{(1008-x)}{x} &= \frac{\sin^2{53}}{\cos^2{53}} \\ x\sin^2{53} &= 1008\cos^2{53} - x\cos^2{53}\\ x(\sin^2{53} + \cos^2{53}) &= 1008\cos^2{53}\\ x = 1008\cos^2{53} &\Longrightarrow 1008-x = 1008\sin^2{53} \end{align*} Now, if we can find $1004 - (EA + 500)$ , and the height of the trapezoid, we can create a right triangle and use the Pythagorean Theorem to find $MN$ .
The leg of the right triangle along the horizontal is:
\[1004 - 1008\sin^2{53} - 500 = 504 - 1008\sin^2{53}.\]
Now to find the other leg of the right triangle (also the height of the trapezoid), we can simplify the following expression:
\begin{align*}\tan{37} \times 1008 \sin^2{53} = \tan{37} \times 1008 \cos^2{37} = 1008\cos{37}\sin{37} = 504\sin74\end{align*}
Now we used Pythagorean Theorem and get that $MN$ is equal to:
\begin{align*}&\sqrt{(1008\sin^2{53} + 500 -1004)^2 + (504\sin{74})^2} = 504\sqrt{1-2\sin^2{53} + \sin^2{74}} \end{align*}
However, $1-2\sin^2{53} = \cos^2{106}$ and $\sin^2{74} = \sin^2{106}$ so now we end up with:
\[504\sqrt{\cos^2{106} + \sin^2{106}} =\fbox{504}.\]

## Solution 4
Plot the trapezoid such that $B=\left(1000\cos 37^\circ, 0\right)$ , $C=\left(0, 1000\sin 37^\circ\right)$ , $A=\left(2008\cos 37^\circ, 0\right)$ , and $D=\left(0, 2008\sin 37^\circ\right)$ .
The midpoints of the requested sides are $\left(500\cos 37^\circ, 500\sin 37^\circ\right)$ and $\left(1004\cos 37^\circ, 1004\sin 37^\circ\right)$ .
To find the distance from $M$ to $N$ , we simply apply the distance formula and the Pythagorean identity $\sin^2 x + \cos^2 x = 1$ to get $MN=\boxed{504}$ .

## Solution 5
Similar to solution 1; Notice that it forms a right triangle. Remembering that the median to the hypotenuse is simply half the length of the hypotenuse, we quickly see that the length is $\frac{2008}{2}-\frac{1000}{2}=504$ .

## Solution 6
Obviously, these angles are random--the only special thing about them is that they add up to 90. So we might as well let the given angles equal 45 and 45, and now the answer is trivially $\boxed{504}$ . (The trapezoid is isosceles, and you see two 45-45-90 triangles;from there you can get the answer.)

## Solution 7
Let the height be h. Note that if $\overline{NH} = x$ then if we draw perpendiculars like in solution 1, $\overline{FN} = 500 - x, \overline{AF} = 504 + x, \overline{HG} = 500, \overline{GD} = 504 - x.$ Note that we wish to find $\overline{MN} = \sqrt{x^2 + h^2}.$ Let's find $\tan(53)$ in two ways. Finding $\tan(53)$ from $\triangle BAF$ yields $\tan(53) = \frac{504+x}{h}.$ Finding it from $\triangle CDG$ yields $\frac{h}{504-x}.$ Setting these equal yields \[\frac{504+x}{h}=\frac{h}{504-x} \rightarrow h^2 = 504^2-x^2 \rightarrow \sqrt{x^2+h^2} = \sqrt{504^2} = \boxed{504}\]

## Solution 8
Rotate trapezoid $MNCD$ 180 degrees around point $N$ so that $AN$ coincides with $ND$ . Let the image of trapezoid $MNCD$ be $ANM'C'$ . Since angles are preserved during rotations, $\angle BAC' = 37^{\circ} + 53 ^{\circ} =90 ^{\circ}$ . Since $BM=CM=C'M'$ and $BM || C'M'$ , $BMM'C'$ is a parallelogram. Thus, $MM'=BC'$ . Let the point where $BC'$ intersects $AD$ be $E$ . Since $BMNE$ is a parallelogram, $AE=AN-BM=1004-500-504$ . Since $BE=EC$ and $\angle BAC= 90^{\circ}$ , $AE$ is a median to the hypotenuse of $BAC'$ . Therefore, $BC'=2 AE= 1008$ , and $BE=MN=\boxed{504}.$

## Solution 9 (Also similar to Solution 1)
Draw line $ME$ from point $M$ parallel to $CD$ that intersects $AD$ . Draw $MF$ from point $M$ parallel to $BA$ that intersects $AD$ . Note that triangle $EMF$ is a right triangle because $\angle BAC' = 90^{\circ}$ . $EN$ has length $DN - CM = 1004 - 500 = 504$ because $CDEM$ is a parallelogram. Similarly, $FN$ has length $AN - BM = 504$ so N is the midpoint of the hypotenuse of right triangle $EMF$ . The midpoint of the hypotenuse in a right triangle is equidistant from all three vertices, so $MN = \boxed{504}$ .

## Solution 10 (Lazy Solution/Guesstimation)
Drop perpendiculars on $AD$ from $B$ and $C$ at $X$ and $Y$
You can see $XY = 2008-1000 = 1008$ .
Let $YD = a$ and $MN = BX = CY = h$ .
Let $AX = 1008 - a$ .
We will also get $YCD = XAB = 37°$ .
Observe that: \[\tan 37^\circ = \frac{h}{1008-a} = \frac{a}{h}\]
Solving for h:
\[h = \sqrt{(a)(1008-a)}\]
To obtain h from $0 \leq h \leq 999$ , only possible natural value of $h$ is $504$ when $(1008-a) = a$
Hence $\boxed{h = 504}$
Note: You can also complete the square in the above equation and then see that the only solution is 504.
- USAMTS Year 18 Problem 2
These problems are copyrighted © by the Mathematical Association of America.