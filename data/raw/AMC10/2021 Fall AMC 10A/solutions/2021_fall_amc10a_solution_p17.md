# 2021 Fall AMC 10A Problem 17

## Problem

An architect is building a structure that will place vertical pillars at the vertices of regular hexagon $ABCDEF$ , which is lying horizontally on the ground. The six pillars will hold up a flat solar panel that will not be parallel to the ground. The heights of pillars at $A$ , $B$ , and $C$ are $12$ , $9$ , and $10$ meters, respectively. What is the height, in meters, of the pillar at $E$ ?

$\textbf{(A) }9 \qquad\textbf{(B) } 6\sqrt{3} \qquad\textbf{(C) } 8\sqrt{3} \qquad\textbf{(D) } 17 \qquad\textbf{(E) }12\sqrt{3}$

### Diagrams

### Three-Dimensional Diagram

[asy] /* Made by MRENTHUSIASM */ size(225); import graph3; import solids; currentprojection=orthographic((0.1,-0.7,0.2)); triple A, B, C, D, E, F, A1, B1, C1, D1, E1, F1; A = (7.5*Cos(240),7.5*Sin(240),0); B = (7.5*Cos(300),7.5*Sin(300),0); C = (7.5*Cos(0),7.5*Sin(0),0); D = (7.5*Cos(60),7.5*Sin(60),0); E = (7.5*Cos(120),7.5*Sin(120),0); F = (7.5*Cos(180),7.5*Sin(180),0); A1 = (7.5*Cos(240),7.5*Sin(240),12); B1 = (7.5*Cos(300),7.5*Sin(300),9); C1 = (7.5*Cos(0),7.5*Sin(0),10); D1 = (7.5*Cos(60),7.5*Sin(60),14); E1 = (7.5*Cos(120),7.5*Sin(120),17); F1 = (7.5*Cos(180),7.5*Sin(180),16); draw(surface(A--B--C--D--E--F--cycle),yellow); draw(surface(A1--B1--C1--D1--E1--F1--cycle),red); draw(A--A1^^B--B1^^C--C1,blue); dot("$A$",A,A/3.75,linewidth(4.5)); dot("$B$",B,B/3.75,linewidth(4.5)); dot("$C$",C,C/3.75,linewidth(4.5)); dot("$D$",D,D/3.75,linewidth(4.5)); dot("$E$",E,E/3.75,linewidth(4.5)); dot("$F$",F,F/3.75,linewidth(4.5)); dot(A1^^B1^^C1^^D1^^E1^^F1,linewidth(4.5)); draw(F--F1^^F--A--B--C^^A1--B1--C1--D1--E1--F1--cycle); draw(C--D--E--F^^D--D1^^E--E1,dashed); label("$12$",midpoint(A--A1),1.5*W,blue); label("$9$",midpoint(B--B1),1.5*W,blue); label("$10$",midpoint(C--C1),1.5*(1,0),blue); [/asy] ~MRENTHUSIASM

### Two-Dimensional Diagram

[asy] /* Made by ihatemath123, Edited by MRENTHUSIASM */ path P; P = polygon(6); fill(P,yellow); draw(P); dot("$A,12$",dir(240),1.5*dir(240),linewidth(4.5)); dot("$B,9$",dir(300),1.5*dir(300),linewidth(4.5)); dot("$C,10$",dir(0),1.5*dir(0),linewidth(4.5)); dot("$D$",dir(60),1.5*dir(60),linewidth(4.5)); dot("$E$",dir(120),1.5*dir(120),linewidth(4.5)); dot("$F$",dir(180),1.5*dir(180),linewidth(4.5)); [/asy] ~ihatemath123 ~MRENTHUSIASM

## Solution 1 (Height From the Center)
The pillar at $B$ has height $9$ and the pillar at $A$ has height $12.$ Since the solar panel is flat, the inclination from pillar $B$ to pillar $A$ is $3.$ Call the center of the hexagon $G.$ Since $\overrightarrow{CG}\parallel\overrightarrow{BA},$ it follows that the solar panel has height $13$ at $G.$ Since the solar panel is flat, the heights of the solar panel at $B,G,$ and $E$ are collinear. Therefore, the pillar at $E$ has height $9+4+4=\boxed{\textbf{(D) } 17}.$
~Arcticturn

## Solution 2 (Height From Each Vertex)
Let the height of the pillar at $D$ be $x.$ Notice that the difference between the heights of pillar $C$ and pillar $D$ is equal to the difference between the heights of pillar $A$ and pillar $F.$ So, the height at $F$ is $x+2.$ Now, doing the same thing for pillar $E$ we get the height is $x+3.$ Therefore, we can see the difference between the heights at pillar $C$ and pillar $D$ is half the difference between the heights at $B$ and $E,$ so \begin{align*} x+3-9&=2 \cdot (x-10) \\ x-6&=2 \cdot (x-10) \\ x&=14. \end{align*} The answer is $x+3=\boxed{\textbf{(D) } 17}.$
~kante314

## Solution 3 (Extend the Sides)
We can extend $BA$ and $BC$ to $G$ and $H$ , respectively, such that $AG = CH$ and $E$ lies on $\overline{GH}$ : [asy] unitsize(1cm); pair A = (-sqrt(3),1); pair B = (0,2); pair C = (sqrt(3),1); pair D = (sqrt(3),-1); pair E = (0,-2); pair F = (-sqrt(3),-1); draw(A--B--C--D--E--F--cycle); label("$A, 12$", A, NW); label("$B, 9$", B, N); label("$C, 10$", C, NE); label("$D$", D, SE); label("$E$", E, S); label("$F$", F, SW); pair G = (-4*sqrt(3),-2); pair H = (4*sqrt(3),-2); label("$G, 21$", G, S); label("$H, 13$", H, S); draw(A--G, dashed); draw(C--H, dashed); dot(A^^B^^C^^D^^E^^F^^G^^H,linewidth(4.5)); [/asy] Because of hexagon proportions, $\frac{BA}{AG} = \frac{1}{3}$ and $\frac{BC}{CH} = \frac{1}{3}$ . Let $g$ be the height of $G$ . Because $A$ , $B$ and $G$ lie on the same line, $\frac{12-9}{g-12} = \frac{1}{3}$ , so $g-12 = 9$ and $g = 21$ . Similarly, the height of $H$ is $13$ . $E$ is the midpoint of $GH$ , so we can take the average of these heights to get our answer, $\boxed{\textbf{(D) } 17}$ .
~ihatemath123

## Solution 4 (Averages of Heights)
Denote by $h_X$ the height of any point $X$ .
Denote by $M$ the midpoint of $A$ and $C$ . Hence, \[h_M = \frac{h_A + h_C}{2} = 11.\] Denote by $O$ the center of $ABCDEF$ . Because $ABCDEF$ is a regular hexagon, $O$ is the midpoint of $B$ and $E$ . Hence, \[h_O = \frac{h_E + h_B}{2} = \frac{h_E + 9}{2}.\] Because $ABCDEF$ is a regular hexagon, $M$ is the midpoint of $B$ and $O$ . Hence, \[h_M = \frac{h_B + h_O}{2} = \frac{9 + h_O}{2}.\] Solving these equations, we get $h_E = \boxed{\textbf{(D) } 17}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 5 (Vectors)
In this solution, we define rise as the change of height (in meters) from the solar panel to the ground. It follows that the rise from $B$ to $A$ is $12-9=3,$ and the rise from $B$ to $C$ is $10-9=1.$ Note that $\vec{BE}=2\vec{BA}+2\vec{BC},$ so the rise from $B$ to $E$ is $2\cdot3+2\cdot1=8.$
Together, the height of the pillar at $E$ is $9+8=\boxed{\textbf{(D) } 17}$ meters.
~MRENTHUSIASM

## Solution 6 (Vectors)
WLOG, let the side length of the hexagon be $6$ .
Establish a 3D coordinate system, in which $A=(0,0,0)$ . Let the coordinates of $B$ and $C$ be $(6,0,0)$ , $\left(9,-3\sqrt{3},0\right)$ , respectively. Then, the solar panel passes through $P=(0,0,12), Q=(6,0,9), R=\left(9,-3\sqrt{3},10\right)$ .
The vector $\vec{PQ}=\langle 6,0,-3\rangle$ and $\vec{PR}=\left\langle 9,-3\sqrt{3}, -2\right\rangle$ . Computing $\vec{PQ} \times \vec{PR}$ by the matrix \[\begin{bmatrix} i & j & k \\ 6 & 0 & -3 \\ 9 & -3\sqrt{3} & -2 \end{bmatrix}\] gives the result $-9\sqrt{3}i -15j -18\sqrt{3} k$ . Therefore, a normal vector of the plane of the solar panel is $\left\langle -9\sqrt{3},-15,-18\sqrt{3}\right\rangle$ , and the equation of the plane is $-9\sqrt{3}x-15y-18\sqrt{3}z=k$ . Substituting $(x,y,z)=(0,0,12)$ , we find that $k=-216\sqrt{3}$ .
Since $E=\left(0,-6\sqrt{3}\right)$ , we substitute $(x,y)=\left(0,-6\sqrt{3}\right)$ into $-9\sqrt{3}x-15y-18\sqrt{3}z=-216\sqrt{3}$ , which gives $z=\boxed{\textbf{(D) } 17}$ .

## Solution 7 (3D Slopes)
Let the pillars be $AA', BB', \ldots, FF'$ . Since solar panel $A'B'C'D'E'F'$ is a hexagon, the line $B'E'$ hits the midpoint $M$ of $A'C'$ . So, the 3D slope (change in $x$ : change in $y$ : change in $z$ ) of $BE$ is same as $BD$ . If $a$ is side of the hexagonal solar panel, \[B'M' = \frac{1}{2}a, B'E' = a+2\cdot \frac{1}{2}a = 2a\] . So, $B'M:B'E'$ = $1:4$ . Since the height of $M$ to ground $ABCDEF$ is $(10+12)/2 = 11$ , the rise (in z) from $B'$ to $M$ is 2 meaning the rise from $B'$ to $E'$ is $8$ . Thus, $EE' = 8+BB' = \boxed{\textbf{(D) } 17}$ .
~sml1809

## Solution 8 (Midpoints, SIMPLE)
Set the midpoint of $\overline{AC}$ as $M$ : [asy] unitsize(1cm); pair A = (-sqrt(3),1); pair B = (0,2); pair C = (sqrt(3),1); pair D = (sqrt(3),-1); pair E = (0,-2); pair F = (-sqrt(3),-1); pair M =(0,1.35); draw(A--B--C--D--E--F--cycle); label("$A, 12$", A, NW); label("$B, 9$", B, N); label("$C, 10$", C, NE); label("$D$", D, SE); label("$E$", E, S); label("$F$", F, SW); dot((0,1)); label("$M$", M); draw((-sqrt(3),1)--(sqrt(3),1),black); [/asy] We know that the height of $M$ is $11$ as it is the midpoint of $\overline{AC}$ , so the height is the average of $A$ and $C$ , which is $\frac{10 + 12}{2}= 11$ . Since $ABCDEF$ is a regular hexagon, $BE = 4\cdot BM$ . Because the increase in height is proportional to the length of the line segments, and the increase in height from $B$ to $M$ is $2$ , the increase in height from $B$ to $E$ is $2\cdot4=8.$ Adding to the height of $B$ , we get $8+9=\boxed{\textbf{(D) } 17}$ .
~iluvme

## Solution 9 (Educated Guess)
Because the three points given are integers, it is likely that the answer is also an integer. This leaves us with $9$ or $17$ . Because both $A$ and $C$ are greater than $9$ and closer to $E$ than $B$ , we can assume that the height increases as the point gets closer to $E$ . Thus, we know the answer is greater than $9$ . The only choice that satisfies both these criteria is $\boxed{\textbf{(D) } 17}$ .
~iluvme

## Video Solution (Under 2 min!)
https://youtu.be/lwEl3GxnysI
~Education, the Study of Everything

## Video Solution by TheBeautyofMath
Inefficient, but it gets the job done https://youtu.be/SarZNOgo4DA
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .