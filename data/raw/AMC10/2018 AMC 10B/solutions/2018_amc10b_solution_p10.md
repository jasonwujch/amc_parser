# 2018 AMC 10B Problem 10

## Problem

In the rectangular parallelepiped shown, $AB$ = $3$ , $BC$ = $1$ , and $CG$ = $2$ . Point $M$ is the midpoint of $\overline{FG}$ . What is the volume of the rectangular pyramid with base $BCHE$ and apex $M$ ?

[asy] size(250); defaultpen(fontsize(10pt)); pair A =origin; pair B = (4.75,0); pair E1=(0,3); pair F = (4.75,3); pair G = (5.95,4.2); pair C = (5.95,1.2); pair D = (1.2,1.2); pair H= (1.2,4.2); pair M = ((4.75+5.95)/2,3.6); draw(E1--M--H--E1--A--B--E1--F--B--M--C--G--H); draw(B--C); draw(F--G); draw(A--D--H--C--D,dashed); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,E); label("$D$",D,W); label("$E$",E1,W); label("$F$",F,SW); label("$G$",G,NE); label("$H$",H,NW); label("$M$",M,N); dot(A); dot(B); dot(E1); dot(F); dot(G); dot(C); dot(D); dot(H); dot(M); label("3",A/2+B/2,S); label("2",C/2+G/2,E); label("1",C/2+B/2,SE); [/asy]

$\textbf{(A) } 1 \qquad \textbf{(B) } \frac{4}{3} \qquad \textbf{(C) } \frac{3}{2} \qquad \textbf{(D) } \frac{5}{3} \qquad \textbf{(E) } 2$

## Solution 1
Consider the cross-sectional plane and label its area $b$ . Note that the volume of the triangular prism that encloses the pyramid is $\frac{bh}{2}=3$ , and we want the rectangular pyramid that shares the base and height with the triangular prism. The volume of the pyramid is $\frac{bh}{3}$ , so the answer is $\boxed{(E) 2}$ .(AOPS12142015)

## Solution 2
We can start by finding the total volume of the parallelepiped. It is $2 \cdot 3 \cdot 1 = 6$ , because a rectangular parallelepiped is a rectangular prism.
Next, we can consider the wedge-shaped section made when the plane $BCHE$ cuts the figure. We can find the volume of the triangular pyramid with base $EFB$ and apex $M$ . The area of $EFB$ is $\frac{1}{2} \cdot 2 \cdot 3 = 3$ . Since $\overline{BC}$ is given to be $1$ , we have that $\overline{FM}$ is $\frac{1}{2}$ . Using the formula for the volume of a triangular pyramid, we have $V = \frac{1}{3} \cdot \frac{1}{2} \cdot 3 = \frac{1}{2}$ . Also, since the triangular pyramid with base $HGC$ and apex $M$ has the exact same dimensions, it has volume $\frac{1}{2}$ as well.
The original wedge we considered in the last step has volume $3$ , because it is half of the volume of the parallelepiped. We can subtract out the parts we found to have $3 - \frac{1}{2} \cdot 2 = 2$ . Thus, the volume of the figure we are trying to find is $2$ . This means that the correct answer choice is $\boxed{E}$ .
Written by: Archimedes15
NOTE: For those who think that it isn't a rectangular prism, please read the problem. It says "rectangular parallelepiped." If a parallelepiped is such that all of the faces are rectangles, it is a rectangular prism.

## Solution 3 (Competition Speed)
Notice that the volume of the rectangular prism is \( lwh = 3 \cdot 1 \cdot 2 = 6 \)
We first see that the triangular prism EHCBA is just half the volume of the rectangular prism which is just \( 6/2 = 3 \).
We next notice that to get the pyramid with apex \( M \), we need to subtract another pyramid \( GHMC \) that is right behind the pyramid we wish to find. We notice the gap between the answer choices, and realize we can assume a formula for pyramid \( GHMC \).
So we say that the formula is \( V = \frac{1}{3} Bh \), \( B \) is the base area and \( h \) is the height.
The length \( MG \) is just \( 1/2 \), and to find \( B \) we do \( \frac{1}{2} \cdot \frac{1}{2} \cdot 2 = \frac{1}{2} \). The volume of pyramid \( GHMC \) is \( V = \frac{1}{3} \cdot \frac{1}{2} \cdot 3 = \frac{1}{2} \).
We subtract the total volume 6 by the combined volume \( 3 + \frac{1}{2} = \frac{7}{2} \) to get \( \frac{12}{2} - \frac{7}{2} = \frac{5}{2} \). \( \frac{5}{2} \) is just 2.5, and the closest answer choice is $\boxed{\textbf{E } 2}$ .
~Pinotation

## Solution 4
If you look carefully, you will see that on the either side of the pyramid in question, there are two congruent tetrahedra. The volume of one is $\frac{1}{3}Bh$ , with its base being half of one of the rectangular prism's faces and its height being half of one of the edges, so its volume is $\frac{1}{3} (3 \times 2/2 \times \frac{1}{2})=\frac{1}{2}$ . We can obtain the answer by subtracting twice this value from the diagonal half prism, or $(\frac{1}{2} \times 3 \times 2 \times 1) - (2 \times \frac{1}{2})=$ $\boxed{2}$

## Solution 5
You can calculate the volume of the rectangular pyramid by using the formula, $\frac{Ah}{3}$ . $A$ is the area of the base, $BCHE$ , and is equal to $BC * BE$ . The height, $h$ , is equal to the height of triangle $FBE$ drawn from $F$ to $BE$ .
$BE=\sqrt{BF^2 + EF^2}=\sqrt{13}$ Area of $BCHE = BC * BE = \sqrt{13}$
$h = 2 *$ Area of $FBE / BE$ (since Area $= \frac{1}{2}bh$ ).
Area of $FBE = \frac{1}{2} * FB * FE = 3$
$h = 2 * 3 / \sqrt{13} = \frac{6}{\sqrt{13}}$
Volume of pyramid $=\frac{1}{3} * \sqrt{13} * \frac{6}{\sqrt{13}} = 2$
Answer is $\boxed{\textbf{E } 2}$
~OlutosinNGA

## Solution 6
We can start by identifying the information we need. We need to find the area of rectangle $EHCB$ and the height of rectangular prism $EHCBM$ .
In order to find the area of $EHCB,$ we can use the Pythagorean Theorem. We find that $EB = \sqrt{13}$ , so the area of rectangle $EHCB = \sqrt{13}$ . We shall refer to this as $x$ .
In order to find the height of rectangular prism $EHCBM$ , we can examine triangle $EFB$ . We can use the Geometric Mean Theorem to find that when an altitude is dropped from point $F,$ $\overline{EB}$ is split into segments of length $\dfrac{4 \cdot \sqrt{13}}{13}$ and $\dfrac{9 \cdot \sqrt{13}}{13}$ . Taking the geometric mean of these numbers, we find that the altitude has length $\dfrac{6 \cdot \sqrt{13}}{13}$ . This is also the height of the rectangular prism, which we shall refer to as $y$ .
Plugging $x$ and $y$ into the formula $V = \dfrac{b \cdot h}{3},$ we find that the volume is $\boxed{2}$ . The answer is $\boxed{E}$ .

## Solution 7
We start by setting the formula for the volume of a rectangular pyramid: $\frac{1}{3}Bh$ . By the Pythagorean Theorem, we know that $BE = \sqrt{BF^2 + EF^2} = \sqrt{13}$ . Therefore, the area of the base is $1 \times \sqrt{13} = \sqrt{13}$ . Next, we would like to know the height of the pyramid. We can observe that the altitude from point $F$ in $\triangle EFB$ is parallel to the height of the pyramid and therefore congruent because those two altitudes are on the same plane of base $EBCH$ . From this, we only need to find the altitude from point $F$ in $\triangle EFB$ and plug it into our formula for the volume of a rectangular pyramid. This is easy because we already know the area of $\triangle EFB$ and the base from point $F$ , so all we need to do is divide: $\frac{2 \times 3}{\sqrt{13}} = \frac{6}{\sqrt{13}} = \frac{6\sqrt{13}}{13}$ . Now all we need to do is plug in all our known values into the volume formula: $\frac{1}{3}Bh = \frac{\sqrt{13} \times \frac{6\sqrt{13}}{13}}{3} = \boxed{(E) 2}$
~ellpet

## Solution 8
Using the Pythagorean Theorem, we can easily find that $EB = \sqrt{2^2 + 3^2} = \sqrt{13}$ . Quickly computing, we find the area of the base, $BCHE = \sqrt{13} \cdot 1 = \sqrt{13}$ . Now we can make the following adjustments to our 3d shape as shown in the diagram. All we need now is to solve for the height, or $XM$ . We can set up to following equation due to our knowledge of altitudes(of the hypotenuse)in right triangles. We can set up the following equations: \begin{align*} b(a+b) &= (MH_1)^2 \\ a(a+b) &= (MH_2)^2 \\ b\sqrt{13} &= 3^2 \\ a\sqrt{13} &= 2^2 \\ b &= \dfrac{9}{\sqrt{13}} \\ a &= \dfrac{4}{\sqrt{13}} \\ (MX)^2 &= ab \\ (MX)^2 &= \dfrac{9 \cdot 4}{13} \\ MX &= \dfrac {3 \cdot 2}{\sqrt{13}} \\ \end{align*} Thus $\triangle V_{BCHEM} = \dfrac{\text{(height)}\cdot \text{(base)}}{3} = \dfrac{MX \cdot BCHE}{3} = \dfrac {\sqrt{13} \cdot \dfrac{3 \cdot 2}{\sqrt{13}}}{3}$ $= \boxed{\textbf{(E) } 2}$
~ Wiselion :)

## Solution 9 (Basic Coordinate Geometry)
First of all, we can quickly calculate the base area $EBCH$ to be $\sqrt{13}$ , since $BC = 1$ (given) and $EB = \sqrt{2^2+3^2} = \sqrt{13}$ (Pythagorean Theorem).
Now all we need is to find the height of $EBCHM$ , which we can denote as $h$ . We know that the length of the altitude from $M$ , $F$ , and $G$ to base $EBCH$ is $h$ , and that's the length that will be easiest to use to find the height. To make this problem simpler, you can turn this 3D model into a 2D one (look at face $EABF$ ).
Looking at face $EABF$ , $h$ would be equal to the length of the altitude from $F$ to $EB$ . To find this, we can find the coordinates of $F$ and the point where the altitude from $F$ touches $EB$ , which we will call point $X$ . Immediately, we know that the coordinates of $F$ are $(3,2)$ , given the values on the rectangle, and we can find the coordinates of point $X$ by first noticing that the equation of $EB$ is $y = \dfrac{-2x}{3}+2$ . Because of perpendicular slopes being the inverse reciprocal of the original slope, the equation for FX is $y = \dfrac{3x}{2}-\dfrac{5}{2}$ . From this, $y = \dfrac{3x}{2}+b$ , and $2=\dfrac{3(3)}{2}+b$ , so $b = \dfrac{-5}{2}$ . Now the intersection of these two equations can be found to be $(\dfrac{27}{13},\dfrac{8}{13})$ . We can use the distance formula to find the distance between the two points. $\sqrt{(3-\dfrac{27}{13})^2 + (2-\dfrac{8}{13})^2} = \sqrt{(\dfrac{12}{13})^2+(\dfrac{8}{13})^2} = \dfrac{\sqrt{468}}{13}$ .
Now that we know the height length and base area of the pyramid $EBCHM$ , we can use the volume formula for it: $\dfrac{\text{(base area)} \cdot \text{(height length)}}{3} = \dfrac{\dfrac{\sqrt{468}}{13} \cdot \sqrt{13}}{3}$ $= \boxed{\textbf{(E) } 2}$
~Nate1212121

## Solution 10 (Point-line distance formula)
In the rectangular parallelepiped, we are given \[AB = 3,\quad BC = 1,\quad CG = 2.\] The base of the pyramid is the quadrilateral $BCHE$ .
Since opposite edges are perpendicular, $BCHE$ is a rectangle with \[BC = 1 \quad \text{and} \quad BE = \sqrt{AB^2 + AE^2} = \sqrt{3^2 + 2^2} = \sqrt{13}.\] So the area is \[[BCHE] = BC \cdot BE = 1 \cdot \sqrt{13} = \sqrt{13}.\]
Project the solid into the 2D plane containing $B, E,$ and $M$ . Use the coordinates \[B = (3,0),\quad E = (0,2),\quad M = (3,2).\] The slope of $\overline{BE}$ is \[\frac{2-0}{0-3} = -\frac{2}{3},\] so its equation is \[y = -\frac{2}{3}x + 2.\] Rewriting in standard form: \[2x + 3y - 6 = 0.\]
Using the point-to-line distance formula, the perpendicular distance from $M = (3,2)$ to this line is \[\frac{|2(3) + 3(2) - 6|}{\sqrt{2^2 + 3^2}} = \frac{6}{\sqrt{13}}.\] This is the height of the pyramid.
The volume of a pyramid is \[V = \frac{1}{3} \cdot (\text{base area}) \cdot (\text{height}).\] Thus, \[V = \frac{1}{3} \cdot \sqrt{13} \cdot \frac{6}{\sqrt{13}} = \frac{6}{3} = 2.\]
~ Prqtection

## Video Solution (HOW TO THINK CREATIVELY)
https://youtu.be/tlbbP_NdPmc
~Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .