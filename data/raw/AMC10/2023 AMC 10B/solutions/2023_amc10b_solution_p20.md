# 2023 AMC 10B Problem 20

## Problem

Four congruent semicircles are drawn on the surface of a sphere with radius $2$ , as shown, creating a close curve that divides the surface into two congruent regions. The length of the curve is $\pi\sqrt{n}$ . What is $n$ ?

$\textbf{(A) } 32 \qquad \textbf{(B) } 12 \qquad \textbf{(C) } 48 \qquad \textbf{(D) } 36 \qquad \textbf{(E) } 27$

## Solution 1
Focus on 2 of the points. Let the center of the Sphere be \( A \). Label two points that form the diameter of one of the four semicircles \( M \) and \( C \) respectively.
Triangle \( AMC \) is a right triangle through the inscribed right triangle theorem, with \( AM = AC = 2 \).
This is a 45-45-90 triangle, so the length of the diameter \( MC \) is just the hypotenuse of the triangle \( AMC \), which is \( 2\sqrt{2} \). This means the radius is \( \sqrt{2} \).
The circumference of the semicircle is \( \frac{1}{2} \cdot 2\sqrt{2} \cdot \pi = \pi\sqrt{2} \), and because there are four congruent semicircles, the length of the semicircular region is \( 4\sqrt{2}\pi = \pi \cdot 4\sqrt{2} \).
The solution is in the form \( \pi\sqrt{n} \), so we convert \( \pi \cdot 4\sqrt{2} \) to \( \pi\sqrt{16}\sqrt{2} \) to get \( \pi\sqrt{32} \). \( n =\) $\boxed{\textbf{(A) 32}}$ .
~Pinotation
~Diagram by Pinotation

## Solution 2
There are four marked points on the diagram; let us examine the top two points and call them $A$ and $B$ . Similarly, let the bottom two dots be $C$ and $D$ , as shown:
[asy] import graph; import geometry; unitsize(1cm); pair A = (-1.41, 1.41); pair B = (1.41, 1.41); pair C = (1.41, -1.41); pair D = (-1.41, -1.41); pair O = (0, 0); draw(circle(O,2)); draw(A--O--B,black+dashed); draw(C--O--D,black+dashed); dot(A);dot(B);dot(C);dot(D);dot(O); label("$A$", A, NW); label("$B$", B, NE); label("$C$", C, SE); label("$D$", D, SW); label("$O$", (0,0.1), N); [/asy]
This is a cross-section of the sphere seen from the side. We know that ${AO}={BO}={CO}={DO}=2$ , and by Pythagorean Theorem, length of $\overline{AB}=2\sqrt2.$
Each of the four congruent semicircles has the length $AB$ as a diameter (since $\overline{AB}$ is congruent to $\overline{BC},\overline{CD},$ and $\overline{DA}$ ), so its radius is $\dfrac{2\sqrt2}2=\sqrt2.$ Each one's arc length is thus $\pi\cdot\sqrt2=\sqrt2\pi.$
We have $4$ of these, so the total length is $4\sqrt2\pi=\sqrt{32}\pi$ , so thus our answer is $\boxed{\textbf{(A) }32.}$
~Technodoggo ~minor edits by JiuruAops
Note:
TLDR:
The radius of $2$ gives us a line segment connecting diagonal vertices of the semi-circles with a measure of $4$ , giving us through $45^{\circ}-45^{\circ}-90^{\circ}$ relations and Pythagorean theorem a diameter for each semi-circle of $2\sqrt{2}$ , which we can use to bash out the circumference of a full circle, multiply by $2$ , and move inside and under the root to get $32$ .
~Aryan Mukherjee

## Solution 3
Assume $A$ , $B$ , $C$ , and $D$ are the four points connecting the semicircles. By law of symmetry, we can pretty confidently assume that $ABCD$ is a square. Then, $\overline{AB} = 2\sqrt2.$ , and the rest is the same as the second half of solution $1$ .
~jonathanzhou18

## Solution 4
We put the sphere to a coordinate space by putting the center at the origin. The four connecting points of the curve have the following coordinates: $A = \left( 0, 0, 2 \right)$ , $B = \left( 2, 0, 0 \right)$ , $C = \left( 0, 0, -2 \right)$ , $D = \left( -2, 0, 0 \right)$ .
Now, we compute the radius of each semicircle. Denote by $M$ the midpoint of $A$ and $B$ . Thus, $M$ is the center of the semicircle that ends at $A$ and $B$ . We have $M = \left( 1, 0, 1 \right)$ . Thus, $OM = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{2}$ .
In the right triangle $\triangle OAM$ , we have $MA = \sqrt{OA^2 - OM^2} = \sqrt{2}$ .
Therefore, the length of the curve is \begin{align*} 4 \cdot \frac{1}{2} 2 \pi \cdot MA = \pi \sqrt{32} . \end{align*}
Therefore, the answer is $\boxed{\textbf{(A) 32}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 5
Note that each of the diameters are the chord of the sphere of a quarter arc. Thus, the semicircles diameter's length is $2\sqrt{2}$ . Thus, the entire curve is $2\sqrt{2} \cdot \pi \cdot \frac{1}{2} \cdot 4 = 4\sqrt{2} \pi = \sqrt{32} \pi$ . Therefore, the answer is $\boxed{\textbf{(A) 32}}$ . ~andliu766

## Solution 6 (Cheese! Narrow it down to 2 choices!) and actual way (this one is stupid)
Cheese: You can immediately say that the answer choice is either ${\text{(A) }32}$ or ${\text{(C) }48}$ because there are four semicircles in that curve; there are $4 = \sqrt{16}$ semicircles in the curve, so n has to be a multiple of 16, and if you don't know how to do this problem, just guess one of ${\text{(A)}}$ or ${\text{(C)}}$ . Actual way: Take a cross-section of the sphere to get four different points equidistant from the center $O$ of the sphere, $A$ , $B$ , $C$ , $D$ such that $AO = BO = CO = DO = 2$ , and so $ABCD$ is a square with side length $2\sqrt{2}$ , and proceed as in Solution 2 to get $\boxed{\textbf{(A) 32}}$ .
~get-rickrolled ~minor edits by MW2014

## Video Solution 1 by OmegaLearn
https://youtu.be/bQfD2S1HS4c

## Video Solution
https://youtu.be/nkwCDGYAkiw
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .