# 2018 AMC 8 Problem 24

## Problem

In the cube $ABCDEFGH$ with opposite vertices $C$ and $E,$ $J$ and $I$ are the midpoints of segments $\overline{FB}$ and $\overline{HD},$ respectively. Let $R$ be the ratio of the area of the cross-section $EJCI$ to the area of one of the faces of the cube. What is $R^2?$

[asy] size(6cm); pair A,B,C,D,EE,F,G,H,I,J; C = (0,0); B = (-1,1); D = (2,0.5); A = B+D; G = (0,2); F = B+G; H = G+D; EE = G+B+D; I = (D+H)/2; J = (B+F)/2; filldraw(C--I--EE--J--cycle,lightgray,black); draw(C--D--H--EE--F--B--cycle); draw(G--F--G--C--G--H); draw(A--B,dashed); draw(A--EE,dashed); draw(A--D,dashed); dot(A); dot(B); dot(C); dot(D); dot(EE); dot(F); dot(G); dot(H); dot(I); dot(J); label("$A$",A,E); label("$B$",B,W); label("$C$",C,S); label("$D$",D,E); label("$E$",EE,N); label("$F$",F,W); label("$G$",G,N); label("$H$",H,E); label("$I$",I,E); label("$J$",J,W); [/asy]

$\textbf{(A) } \frac{5}{4} \qquad \textbf{(B) } \frac{4}{3} \qquad \textbf{(C) } \frac{3}{2} \qquad \textbf{(D) } \frac{25}{16} \qquad \textbf{(E) } \frac{9}{4}$

## Solution 1
Note that $EJCI$ is a rhombus by symmetry. Let the side length of the cube be $s$ . By the Pythagorean theorem, $EC= s\sqrt 3$ and $JI= s\sqrt 2$ . Since the area of a rhombus is half the product of its diagonals, the area of the cross section is $\frac{s^2\sqrt 6}{2}$ . This gives $R = \frac{\sqrt 6}2$ . Thus, $R^2 = \boxed{\textbf{(C) } \frac{3}{2}}$ .

## Solution 2
This time, instead of using a variable like we did in Solution 1, $s$ , for the side length as in the above solution, choose an easy value for $s$ such as $2$ . In the above solution, $s^2$ cancels out in the end, so ultimately the answers are equivalent. ~Technodoggo

## Solution 3 (Coordinate Geometry)
If the edges of the cube have same lengths $a$ , $A$ is the origin, $\vec{AD }$ is the positive $x$ direction, $\vec{AE}$ is the positive $y$ direction, and $\vec{AB }$ is the positive $z$ direction. Therefore, we have $E(0,a,0), I(a,\frac{a}{2},0), C(a,0,a),$ and $J(0,\frac{a}{2},a)$ . Hence, we can figure out that:
\[|EC|=\sqrt{a^2 + a^2 + a^2}=\sqrt{3}a\]
\[|IJ|=\sqrt{a^2 + 0 + a^2}=\sqrt{2}a\]
Note that $EJCI$ is a rhombus, so $R=\frac{\sqrt{6}a^2}{2a^2}=\frac{\sqrt{6}}{2}$ . Finally, we can see that the answer is $R^2=\frac{6}{4}=\boxed{\textbf{(C) } \frac{3}{2}}$
~ Bloggish

## Solution 4 (AMC 10+ tactics)
We can solve this with 3D Cartesian coordinates. Assume WLOG that the sides of the square are of length $2$ . Let $C$ be the origin and let $\vec{CD}$ be the positive $x$ direction, $\vec{CG}$ be the positive $y$ direction, and $\vec{CB}$ be the positive $z$ direction. We find that $I=(2,1,0),J=(0,1,2),E=(2,2,2)$ .
Notice that $CI=CJ=EI=EJ=\sqrt{5}$ so $EJCI$ is a rhombus. Furthermore, by the distance formula, $IJ=\sqrt8$ .
By the Law of Cosines on $\triangle JCI$ we have $\cos \angle JCI=\frac{\sqrt5^2+ \sqrt5^2-\sqrt8^2}{2\cdot \sqrt5\cdot \sqrt5}=\frac 15$ . By the Law of Cosines on $\triangle JEI$ we have $\cos \angle JEI=\frac{\sqrt5^2+ \sqrt5^2-\sqrt8^2}{2\cdot \sqrt5\cdot \sqrt5}=\frac 15$ .
Bretschneider's formula states given a quadrilateral $ABCD$ with sides $a,b,c,d$ then \[[ABCD]=\sqrt{(s-a)(s-b)(s-c)(s-d)-abcd\cos^2\left({\frac{B+D}{2}}\right)}\] where $s=\frac{a+b+c+d}2$ . Using this formula, we find that \[[EJCI]=\sqrt{(2\sqrt5-\sqrt5)(2\sqrt5-\sqrt5)(2\sqrt5-\sqrt5)(2\sqrt5-\sqrt5)-\sqrt 5^4(\tfrac 15)^2}=2\sqrt{6}.\]
Using Bretschneider's formula again, we can find that $[ABCD]=\sqrt{(4-2)(4-2)(4-2)(4-2)-2^4\cdot \cos \left(\frac{90^\circ+90^\circ}2\right)}=\sqrt{16}=4$ .
The answer is thus $\left(\frac{2\sqrt6}{4}\right)^2=\frac 32$ so we circle answer choice $\boxed{\textbf{(C) } \frac{3}{2}}$
~franzliszt

## Solution 5 (Not for use in a time-limited contest)
We will use the following
Theorem: Suppose we have a quadrilateral with edges of length $a,b,c,d$ (in that order) and diagonals of length $p, q$ . Bretschneider's formula states that the area $[ABCD]=\frac{1}{4} \cdot \sqrt{4p^2q^2-(b^2+d^2-a^2-c^2)^2}$ .
Proof: Here is one of my favorite proofs of this with vector geometry.
Suppose a quadrilateral has sides $\vec{a}, \vec{b}, \vec{c}, \vec{d}$ such that $\vec{a} + \vec{b} + \vec{c} + \vec{d} = \vec{0}$ and that the diagonals of the quadrilateral are $\vec{p} = \vec{b} + \vec{c} = -\vec{a} - \vec{d}$ and $\vec{q} = \vec{a} + \vec{b} = -\vec{c} - \vec{d}$ . The area of any such quadrilateral is $\frac{1}{2} |\vec{p} \times \vec{q}|$ .
$K = \frac{1}{2} |\vec{p} \times \vec{q}|$
Lagrange's Identity states that $|\vec{a}|^2|\vec{b}|^2-(\vec{a}\cdot\vec{b})^2=|\vec{a}\times\vec{b}|^2 \implies \sqrt{|\vec{a}|^2|\vec{b}|^2-(\vec{a}\cdot\vec{b})^2}=|\vec{a}\times\vec{b}|$ . Therefore:
$K = \frac{1}{2} \sqrt{|\vec{p}|^2|\vec{q}|^2 - (\vec{p} \cdot \vec{q})^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - (2 \vec{p} \cdot \vec{q})^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [2 (\vec{b} + \vec{c}) \cdot (\vec{a} + \vec{b})]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [2 \vec{b} \cdot (\vec{a} + \vec{b}) + 2 \vec{c} \cdot (\vec{a} + \vec{b})]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [-2 \vec{b} \cdot (\vec{c} + \vec{d}) + 2 \vec{c} \cdot (\vec{a} + \vec{b})]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [-2 \vec{b} \cdot \vec{c} - 2 \vec{b} \cdot \vec{d} + 2 \vec{a} \cdot \vec{c} + 2 \vec{b} \cdot \vec{c}]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [2 \vec{a} \cdot \vec{c} - 2 \vec{b} \cdot \vec{d}]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - ([(\vec{a} + \vec{c})\cdot(\vec{a} + \vec{c}) - \vec{a}\cdot\vec{a} - \vec{c}\cdot\vec{c}] - [(\vec{b} + \vec{d})\cdot(\vec{b} + \vec{d}) - \vec{b}\cdot\vec{b} - \vec{d}\cdot\vec{d}])^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [|\vec{b}|^2 + |\vec{d}|^2 - |\vec{a}|^2 - |\vec{c}|^2 + (\vec{a} + \vec{c})\cdot(\vec{a} + \vec{c}) - (\vec{b} + \vec{d})\cdot(\vec{b} + \vec{d})]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [|\vec{b}|^2 + |\vec{d}|^2 - |\vec{a}|^2 - |\vec{c}|^2 + |\vec{a} + \vec{c}|^2 - |\vec{b} + \vec{d}|^2]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [|\vec{b}|^2 + |\vec{d}|^2 - |\vec{a}|^2 - |\vec{c}|^2 + |\vec{a} + \vec{c}|^2 - |-(\vec{a} + \vec{c})|^2]^2}$
$= \frac{1}{4} \sqrt{4 |\vec{p}|^2|\vec{q}|^2 - [|\vec{b}|^2 + |\vec{d}|^2 - |\vec{a}|^2 - |\vec{c}|^2]^2}$
Then, if $a, b, c, d$ represent $|\vec{a}|, |\vec{b}|, |\vec{c}|, |\vec{d}|$ (and are thus the side lengths) while $p, q$ represent $|\vec{p}|, |\vec{q}|$ (and are thus the diagonal lengths), the area of a quadrilateral is:
\[K = \frac{1}{4} \sqrt{4p^2q^2 - (b^2 + d^2 - a^2 - c^2)^2}\] $\square$
Back to the problem. We use vectors. WLOG suppose the cube has sides of length $2$ . Let $C$ be the origin and let $\vec{CD}$ be the $x$ direction, $\vec{CG}$ be the $y$ direction, and $\vec{CB}$ be the $z$ direction.
Then, $\vec{CI}=\vec{JE}=\begin{pmatrix} 2\\1\\0\end{pmatrix}$ and $\vec{CJ}=\vec{IE}=\begin{pmatrix} 0\\1\\2\end{pmatrix}$ . Let $\angle JCI=\theta$ . Dot product gives $\cos \theta=\left(\frac{\begin{pmatrix} 2\\1\\0\end{pmatrix} \cdot \begin{pmatrix} 0\\1\\2\end{pmatrix}}{|\begin{pmatrix} 2\\1\\0\end{pmatrix}||\begin{pmatrix} 0\\1\\2\end{pmatrix}|}\right)=\frac 15.$
Hence, $\vec {IJ}=\sqrt{|\vec{CI}|+|\vec{CJ}|-2\cdot \vec{CI}\cdot \vec{CJ}\cos \theta}=\sqrt{|\begin{pmatrix} 2\\1\\0\end{pmatrix}|+|\begin{pmatrix} 0\\1\\2\end{pmatrix}|-2\cdot \begin{pmatrix} 2\\1\\0\end{pmatrix} \cdot\begin{pmatrix} 0\\1\\2\end{pmatrix} \cdot \frac 15} \iff |\vec{IJ}|=2\sqrt2$ .
Now, notice that $\vec{CE}=\vec{CI}+\vec{CJ}=\begin{pmatrix} 2\\1\\0\end{pmatrix}+\begin{pmatrix} 0\\1\\2\end{pmatrix}=\begin{pmatrix} 2\\2\\2\end{pmatrix}$ so $|\vec{CE}|=|\begin{pmatrix} 2\\2\\2\end{pmatrix}|=2\sqrt3$ .
Using Bretschneider's formula, we obtain $[EJCI]=\frac{1}{4} \cdot \sqrt{4|\vec{IJ}|^2|\vec{CE}|^2-(|\vec{CJ}|^2+|\vec{IE}|^2-|\vec{JE}|^2-|\vec{CI}|^2)^2}=\frac 14\sqrt{4\cdot (2\sqrt2)^2\cdot (2\sqrt3)^2-(5^2+5^2-5^2-5^2)^2}=2\sqrt6$ .
Using Bretschneider's formula again, we can find that $[ABCD]=\sqrt{(4-2)(4-2)(4-2)(4-2)-2^4\cdot \cos \left(\frac{90^\circ+90^\circ}2\right)}=\sqrt{16}=4$ .
Hence, the answer is $\left(\frac{2\sqrt6}{4}\right)^2=\frac 32$ so we circle answer choice $C$ .
~franzliszt

## Solution 6
We can simply plug in values and find \( R \) to eliminate the variables and avoid the complicated algebra. Let’s assume the side length of the cube is \( 4 \). The given figure is a rhombus because all its sides are equal, but the angles are not \( 90^\circ \). To find the area of the rhombus, we need to calculate the lengths of the two diagonals.
The formula for the space diagonal of a cube is \( \sqrt{3}s \), so \( \overline{CE} = 4\sqrt{3} \). By symmetry, \( \overline{IJ} = \overline{BD} = 4\sqrt{2} \). Now, we can find the area of the rhombus using the formula for the area of a rhombus, which is the product of the diagonals divided by 2:
\begin{align*} \text{Area} &= \frac{4\sqrt{3} \cdot 4\sqrt{2}}{2} \\ &= 8\sqrt{6}. \end{align*}
Next, the area of one of the cube’s faces is simply \( 4^2 = 16 \). So, \( R \) is:
${\left(\frac{8\sqrt6}{16}\right)^2}$ = ${\boxed{\textbf{(C)}\frac{3}{2}}}$ .
-jb2015007
(Minor edits by FrankensteinQuixoteCabin)
### Note
Problem 21 of the 2008 AMC 10A was nearly identical to this question, except that in this question you have to look for the square of the area, not the actual area.

## Video Solution
https://www.youtube.com/watch?v=04pV_rZw8bg
~ Happytwin

## Video Solution
https://www.youtube.com/watch?v=ji9_6XNxyIc
~ MathEx

## Video Solution by OmegaLearn
https://youtu.be/FDgcLW4frg8?t=2823
~ pi_is_3.14

## Video Solution
https://youtu.be/IrxtHlbERe8
~savannahsolver
### See Also