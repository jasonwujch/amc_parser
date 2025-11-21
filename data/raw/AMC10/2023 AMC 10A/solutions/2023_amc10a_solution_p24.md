# 2023 AMC 10A Problem 24

## Problem

Six regular hexagonal blocks of side length 1 unit are arranged inside a regular hexagonal frame. Each block lies along an inside edge of the frame and is aligned with two other blocks, as shown in the figure below. The distance from any corner of the frame to the nearest vertex of a block is $\frac{3}{7}$ unit. What is the area of the region inside the frame not occupied by the blocks? [asy] unitsize(1cm); draw(scale(3)*polygon(6)); filldraw(shift(dir(0)*2+dir(120)*0.4)*polygon(6), lightgray); filldraw(shift(dir(60)*2+dir(180)*0.4)*polygon(6), lightgray); filldraw(shift(dir(120)*2+dir(240)*0.4)*polygon(6), lightgray); filldraw(shift(dir(180)*2+dir(300)*0.4)*polygon(6), lightgray); filldraw(shift(dir(240)*2+dir(360)*0.4)*polygon(6), lightgray); filldraw(shift(dir(300)*2+dir(420)*0.4)*polygon(6), lightgray); [/asy] $\textbf{(A)}~\frac{13 \sqrt{3}}{3}\qquad\textbf{(B)}~\frac{216 \sqrt{3}}{49}\qquad\textbf{(C)}~\frac{9 \sqrt{3}}{2} \qquad\textbf{(D)}~ \frac{14 \sqrt{3}}{3}\qquad\textbf{(E)}~\frac{243 \sqrt{3}}{49}$

## Solution 1
[asy] unitsize(1cm); pair A, B, C, D, E, F, W,X,Y,Z; real bigSide = 3; real smallSide = 1; real angle = 60; // Each external angle for the hexagon real offset = 3/7; // Offset for the smaller hexagons // Function to draw a hexagon given a starting point and side length void drawHexagon(pair start, real side) { pair current = start; for (int i = 0; i < 6; ++i) { pair next = current + side * dir(angle * i); draw(current--next); current = next; } draw(current--start); // Close the hexagon } // Define the first vertex of the big hexagon A = (0,0); // Calculate the other vertices of the big hexagon B = A + bigSide * dir(0); C = B + bigSide * dir(angle); D = C + bigSide * dir(2*angle); E = D + bigSide * dir(3*angle); F = E + bigSide * dir(4*angle); // Draw the big hexagon drawHexagon(A, bigSide); // Function to calculate the center of a side given two vertices pair sideCenter(pair start, pair end) { return (start + end)/2; } // Draw the smaller hexagons drawHexagon(A + offset * dir(0), smallSide); drawHexagon(B - smallSide * dir(0)+offset*dir(60), smallSide); drawHexagon(C - smallSide * dir(0)-dir(60)+dir(120)*3/7, smallSide); drawHexagon(D - 2*smallSide*dir(120)-(2+3/7)*smallSide, smallSide); drawHexagon(E - 2*smallSide*dir(60)+smallSide-3/7*dir(60), smallSide); drawHexagon(F + smallSide*dir(-60)+(3/7)*dir(-60), smallSide); // Optionally, label the vertices of the big hexagon label("$A$", A, SW); label("$B$", B, SE); label("$C$", C, E); label("$D$", D, NE); label("$E$", E, NW); label("$F$", F, W); void drawTrap(pair W, real side, pen p) { X = W+(3/7)*side*dir(0); Y = X+(4/7)*side*dir(60); Z = Y - side*dir(0); draw(W--X, p); draw(X--Y,p); draw(Y--Z,p); draw(Z--W,p); } W = A+smallSide*dir(120); drawTrap(W,1, red+2); pair W2,W3,W4,W5; W2 = A+3*dir(-90); W3 = W2+dir(90)*4*sqrt(3)/7; W4 = W3+dir(0)*6/7; W5 = W2+dir(0)*6/7; drawTrap(W2,2,blue+1); draw(W2--W3,blue+0.5); draw(W4--W5,blue+0.5); label("2/7",W3,NW); label("3/7",W3,NE); W4 = W3+6/7*dir(0); label("2/7",W4,NE); label("4/7",W2+dir(160)*0.5,W); draw(A -1.5*dir(45)-- F -1.5*dir(45), green+0.5); pair J,K,L,M,N; J = ((A/10+9*F/10))-0.25*dir(45); L = ((A+F)/2)-0.25*dir(45); K = ((J+L)/2)-0.25*dir(45); M = ((L+A)/2)-0.25*dir(45); N = ((A+F)/2)-1.6*dir(45); label("3/7",J,SW); label("4/7",L,SW); label("1",K,SW); label("1",M,SW); label("3",N,SW); [/asy]
Examining the red isosceles trapezoid with $1$ and $\dfrac{3}{7}$ as two bases, we know that the side lengths are $\dfrac{4}{7}$ from $30-60-90$ triangle.
We can conclude that the big hexagon has side length 3.
Thus the target area is: area of the big hexagon - 6 * area of the small hexagon. $\dfrac{3\sqrt{3}}{2}(3^2-6\cdot1^2) = \dfrac{3\sqrt{3}}{2}(3) = \boxed{\textbf{(C)}~\frac{9 \sqrt{3}}{2}}$
~Technodoggo

## Solution 1.1
We can extend the line of the parallelogram to the end until it touches the next hexagon and it will make a small equilateral triangle and a longer parallelogram. We can prove that one side of the tiny equilateral triangle is 4/7 by playing around with angles and the parallelogram because it is parallel, we can then use the whole side of the hexagon which is one and subtract 3/7 which is one side of the equilateral triangle which is 4/7. That means the whole side of the big hexagon length is 3 and we can continue with solution 1.
[asy] unitsize(1cm); pair A, B, C, D, E, F, W,X,Y,Z; real bigSide = 3; real smallSide = 1; real angle = 60; // Each external angle for the hexagon real offset = 3/7; // Offset for the smaller hexagons // Function to draw a hexagon given a starting point and side length void drawHexagon(pair start, real side) { pair current = start; for (int i = 0; i < 6; ++i) { pair next = current + side * dir(angle * i); draw(current--next); current = next; } draw(current--start); // Close the hexagon } // Define the first vertex of the big hexagon A = (0,0); // Calculate the other vertices of the big hexagon B = A + bigSide * dir(0); C = B + bigSide * dir(angle); D = C + bigSide * dir(2*angle); E = D + bigSide * dir(3*angle); F = E + bigSide * dir(4*angle); // Draw the big hexagon drawHexagon(A, bigSide); // Function to calculate the center of a side given two vertices pair sideCenter(pair start, pair end) { return (start + end)/2; } // Draw the smaller hexagons drawHexagon(A + offset * dir(0), smallSide); drawHexagon(B - smallSide * dir(0)+offset*dir(60), smallSide); drawHexagon(C - smallSide * dir(0)-dir(60)+dir(120)*3/7, smallSide); drawHexagon(D - 2*smallSide*dir(120)-(2+3/7)*smallSide, smallSide); drawHexagon(E - 2*smallSide*dir(60)+smallSide-3/7*dir(60), smallSide); drawHexagon(F + smallSide*dir(-60)+(3/7)*dir(-60), smallSide); // Optionally, label the vertices of the big hexagon label("$A$", A, SW); label("$B$", B, SE); label("$C$", C, E); label("$D$", D, NE); label("$E$", E, NW); label("$F$", F, W); void drawTriangle(pair W, real side, pen p) { X = W+(3/7)*side*dir(0); Y = A+(3/7)*side*dir(0); draw(W--X, p); draw(W--A, p); draw(Y--X, p); draw(A--Y, p); } W = A+11/7*dir(120); drawTriangle(W,1, purple+2); draw(A -1.5*dir(45)-- F -1.5*dir(45), green+0.5); pair J,K,L,M,N; J = ((A/10+9*F/10))-0.25*dir(45); L = ((A+F)/2)-0.25*dir(45); K = ((J+L)/2)-0.25*dir(45); M = ((L+A)/2)-0.25*dir(45); N = ((A+F)/2)-1.6*dir(45); label("3/7",J,SW); label("4/7",L,SW); label("1",K,SW); label("1",M,SW); label("3",N,SW); [/asy] -BrandonChen

## Solution 1.3
An alternative diagram, perhaps slightly more intuitive, can be drawn by extending segments to form two equilateral triangles (shown in blue) with side length 1. [asy] // Asymptote code borrowed from Technodoggo's solution unitsize(1cm); pair A, B, C, D, E, F, W,X,Y,Z; real bigSide = 3; real smallSide = 1; real angle = 60; // Each external angle for the hexagon real offset = 3/7; // Offset for the smaller hexagons // Function to draw a hexagon given a starting point and side length void drawHexagon(pair start, real side) { pair current = start; for (int i = 0; i < 6; ++i) { pair next = current + side * dir(angle * i); draw(current--next); current = next; } draw(current--start); // Close the hexagon } // Define the first vertex of the big hexagon A = (0,0); // Calculate the other vertices of the big hexagon B = A + bigSide * dir(0); C = B + bigSide * dir(angle); D = C + bigSide * dir(2*angle); E = D + bigSide * dir(3*angle); F = E + bigSide * dir(4*angle); // Draw the big hexagon drawHexagon(A, bigSide); // Function to calculate the center of a side given two vertices pair sideCenter(pair start, pair end) { return (start + end)/2; } // Draw the smaller hexagons drawHexagon(A + offset * dir(0), smallSide); drawHexagon(B - smallSide * dir(0)+offset*dir(60), smallSide); drawHexagon(C - smallSide * dir(0)-dir(60)+dir(120)*3/7, smallSide); drawHexagon(D - 2*smallSide*dir(120)-(2+3/7)*smallSide, smallSide); drawHexagon(E - 2*smallSide*dir(60)+smallSide-3/7*dir(60), smallSide); drawHexagon(F + smallSide*dir(-60)+(3/7)*dir(-60), smallSide); // Optionally, label the vertices of the big hexagon label("$A$", A, SW); label("$B$", B, SE); label("$C$", C, E); label("$D$", D, NE); label("$E$", E, NW); label("$F$", F, W); pair J,K,L,M,N; J = ((A/10+9*F/10))-0.25*dir(45); L = ((A+F)/2)-0.25*dir(45); K = ((J+L)/2)-0.25*dir(45); M = ((L+A)/2)-0.25*dir(45); // Extending lines to form two triangles X = A+dir(180)*0.57+dir(60)*(1+4/7); Y = A+dir(180)*0.57; draw(X -- Y, blue+1.5); draw(Y -- A+dir(0)*(3/7), blue+1.5); draw(A+dir(0)*(3/7) -- A+dir(0)*(3/7)+dir(120)*1, blue+1.5); draw(A+dir(120)*(4/7) -- A+dir(120)*(4/7)+dir(120), blue+1.5); draw(A+dir(120)*(4/7)+dir(120) -- X, blue+1.5); draw(A+dir(120)*(4/7)+dir(120) -- A+dir(120)*(4/7)+dir(120)+dir(120), blue+1.5); draw(A+dir(120)*(4/7)+dir(120)+dir(120) -- F, red+1.5); draw(A -- A+dir(120)*(4/7), dashed+magenta+1.5+linetype("0 1.4")); draw(A -- A+dir(180)*(4/7), dashed+magenta+1.5+linetype("0 1.4")); draw(A+dir(180)*(4/7) -- A+dir(120)*(4/7), dashed+magenta+1.5+linetype("0 1.4")); [/asy]
The red segment is given to have length \(3/7\). Furthermore, we can find yet another equilateral triangle within the bottom blue triangle that has side length \(1-3/7 = 4/7\), shown in dashed magenta. Adding all four segments (red, blue, blue, magenta), we find the side length of the larger hexagon to be \(3/7+1+1+4/7 = 3\). Then we can continue with Solution 1.
~abghim
(diagram borrowed mostly from ~Technodoggo's Solution 1)

## Solution 2 (Not rigorous)
Note that one can "slide' the small hexagons along their respective edges, and either by sliding them to the center or to the corners, and thus getting that the side length of the larger hexagon is 3. The rest proceeds the same as solution 1.

## Solution 2.1 (Clarification)
Notice that when sliding the smaller hexagon along the edge, we see that the contact edge withe the smaller hexagon "in front" of it is $60^{\circ}$ , thus meaning the hexagon "in front" is pushed at a speed $\sin{60^{\circ}}$ times the actual speed of the hexagon. We can preform a similar analysis on the hexagon that is being pushed and get that the speed at which that hexagon is moving is $\frac{1}{\sin{60^{\circ}}}$ times the speed it pushed by. As we can see, the two factors cancel out and by the same argument, every small hexagon can move at the same speed while mantaining an edge of contact with the two adjacent hexagons.
[asy] unitsize(1cm); draw(scale(3)*polygon(6)); filldraw(shift(dir(0)*2+dir(120)*0.4)*polygon(6), pink); filldraw(shift(dir(60)*2+dir(180)*0.4)*polygon(6), palered); filldraw(shift(dir(120)*2+dir(240)*0.4)*polygon(6), paleyellow); filldraw(shift(dir(180)*2+dir(300)*0.4)*polygon(6), palegreen); filldraw(shift(dir(240)*2+dir(360)*0.4)*polygon(6), palecyan); filldraw(shift(dir(300)*2+dir(420)*0.4)*polygon(6), paleblue); draw(dir(120)*2+dir(240)*0.4--dir(120)*2,red+linewidth(1.5),EndArrow(size=12)); draw(dir(180)*2+dir(300)*0.4--dir(180)*2,red+linewidth(1.5),EndArrow(size=12)); draw(dir(240)*2+dir(0)*0.4--dir(240)*2,red+linewidth(1.5),EndArrow(size=12)); draw(dir(300)*2+dir(60)*0.4--dir(300)*2,red+linewidth(1.5),EndArrow(size=12)); draw(dir(0)*2+dir(120)*0.4--dir(360)*2,red+linewidth(1.5),EndArrow(size=12)); draw(dir(60)*2+dir(180)*0.4--dir(60)*2,red+linewidth(1.5),EndArrow(size=12)); [/asy] [asy] unitsize(1cm); draw(scale(3)*polygon(6)); filldraw(shift(dir(0)*2+dir(120)*0)*polygon(6), pink); filldraw(shift(dir(60)*2+dir(180)*0)*polygon(6), palered); filldraw(shift(dir(120)*2+dir(240)*0)*polygon(6), paleyellow); filldraw(shift(dir(180)*2+dir(300)*0)*polygon(6), palegreen); filldraw(shift(dir(240)*2+dir(360)*0)*polygon(6), palecyan); filldraw(shift(dir(300)*2+dir(420)*0)*polygon(6), paleblue); [/asy] Diagram by ihatemath123
### Note
The number $\frac{3}{7}$ is irrelevant to solve the problem. In fact, if the smaller hexagons have side length $x$ , the side length of the large hexagon will always be $3x$ .

## Solution 2
We put the diagram to a complex plane, with the center of the outside hexagon at the origin. We denote by $s$ the length of each side of the outside hexagon.
The complex number of the upper left vertex of the upper right small hexagon is \begin{align*} s e^{i 30^\circ} + \frac{3}{7} e^{i \left( 90^\circ + 60^\circ \right)} - \sqrt{3} . \end{align*}
The complex number of the upper right vertex of the top small hexagon is \begin{align*} s i + \frac{3}{7} e^{i \left( \pi + \frac{\pi}{6} \right)} + e^{- i \frac{\pi}{6}} . \end{align*}
The above two vertices are on the same vertical line. So their real part values are the same. By solving this equation, we get $s = 3$ .
Therefore, the area of the region not occupied by the blocks is \begin{align*} 6 \cdot \frac{\sqrt{3}}{4} s^2 - 6 \cdot 6 \cdot \frac{\sqrt{3}}{4} 1^2 = \boxed{\textbf{(C) } \frac{9 \sqrt{3}}{2}} . \end{align*}
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3 (no words)
[asy] unitsize(1cm); unitsize(5cm); draw(scale(3)*polygon(6)); filldraw(shift(dir(0)*2+dir(120)*3/7)*polygon(6), lightgray); filldraw(shift(dir(60)*2+dir(180)*3/7)*polygon(6), lightgray); filldraw(shift(dir(120)*2+dir(240)*3/7)*polygon(6), lightgray); filldraw(shift(dir(180)*2+dir(300)*3/7)*polygon(6), lightgray); filldraw(shift(dir(240)*2+dir(0)*3/7)*polygon(6), lightgray); filldraw(shift(dir(300)*2+dir(60)*3/7)*polygon(6), yellow); pair A = (0,0) + 3 * dir(300); pair B = A + 3/7 *dir(60); pair C = B + 1 * dir(180); pair D = C + 3/7 * dir(240); pair E = C + 4/7 * dir(120); pair F = E + 3/7 * dir(240); pair G = F + 4/7 * dir(240); pen p = red+linewidth(6); draw(A--B--C--D--cycle,p); draw(C--E--F--D--cycle,p); draw(F--G--D--cycle,p); label("1",(B + C)/2,dir(90)); label("1",(A + D)/2,dir(270)); label("3/7",(A + B)/2,dir(330)); label("3/7",(C + D)/2,dir(330)); label("4/7",(C+E)/2,dir(30)); label("3/7",(E+F)/2,dir(150)); label("4/7",(F+D)/2,dir(30)); label("4/7",(F+G)/2,dir(150)); label("4/7",(G+D)/2,dir(270)); [/asy]
$(3^2-6\times 1^2)\times\frac{3\sqrt{3}}{2}=(9-6\times 1)\times\frac{3\sqrt{3}}{2}=(9-6)\times\frac{3\sqrt{3}}{2}=3\times\frac{3\sqrt{3}}{2}=\boxed{\textbf{(C) } \frac{9 \sqrt{3}}{2}}$
~~By afly ~(very minor change by Marshall_Huang)

## Solution 4 (educated guessing)
Since the area of each hexagon is $\frac{3 \sqrt{3}}{2}$ , the answer is just the area of the large hexagon minus $9\sqrt{3}$ . The side length of the large hexagon should be an integer or fraction since we are given integers and fractions, and solving this problem shouldn't require any square roots. Therefore, the correct answer plus $9\sqrt{3}$ should be the product of $\frac{3 \sqrt{3}}{2}$ and a square number. Only choice $\text{C}$ satisfies this, since $\frac{9 \sqrt{3}}{2} + 9\sqrt{3}=\frac{27 \sqrt{3}}{2}=3^2\times\frac{3 \sqrt{3}}{2}$ . Alternatively, we can also deduce $\text{C}$ is correct since it is the only fraction whose denominator is ${2}$ . Therefore, the answer is (probably) $\boxed{\textbf{(C)}~\frac{9 \sqrt{3}}{2}}$
-faliure167

## Video Solution (Intuitive Animation)
https://youtu.be/K-poIoQu8l0

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=3-vQvfxtlkYOjmNo&t=5385 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=YbCV6NCV1qj0YZXp&t=9253
~Math-X

## Video Solution ⚡️ 3 min solve ⚡️
https://youtu.be/YZcxxxmnVNQ
~Education, the Study of Everything

## Video Solution by MegaMath
https://www.youtube.com/watch?v=Qe3eVv3aWEw&t=2s

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=asRnZdiTYcI

## Video Solution by OmegaLearn
https://youtu.be/pObolGKEKc0

## Video Solution by epicbird08
https://youtu.be/7XoekZvtQuU
~EpicBird08

## Video Solution
https://youtu.be/tLTTuQ7tOb4
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by TheBeautyofMath
https://youtu.be/uaNbxfuas5o
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .