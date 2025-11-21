# 2006 AMC 10A Problem 16

## Problem

A circle of radius $1$ is tangent to a circle of radius $2$ . The sides of $\triangle ABC$ are tangent to the circles as shown, and the sides $\overline{AB}$ and $\overline{AC}$ are congruent. What is the area of $\triangle ABC$ ?

[asy] size(200); pathpen = linewidth(0.7); pointpen = black; real t=2^0.5; D((0,0)--(4*t,0)--(2*t,8)--cycle); D(CR((2*t,2),2)); D(CR((2*t,5),1)); D('B', (0,0),SW); D('C',(4*t,0), SE); D('A', (2*t, 8), N); D((2*t,2)--(2*t,4)); D((2*t,5)--(2*t,6)); MP('2', (2*t,3), W); MP('1',(2*t, 5.5), W);[/asy]

$\textbf{(A) } \frac{35}{2}\qquad\textbf{(B) } 15\sqrt{2}\qquad\textbf{(C) } \frac{64}{3}\qquad\textbf{(D) } 16\sqrt{2}\qquad\textbf{(E) } 24\qquad$

## Solution 1
Let the centers of the smaller and larger circles be $O_1$ and $O_2$ , respectively. Let their tangent points to $\triangle ABC$ be $D$ and $E$ , respectively. We can then draw the following diagram:
[asy] size(200); pathpen = linewidth(0.7); pointpen = black; pointfontpen = fontsize(10); real t=2^0.5; D((0,0)--(4*t,0)--(2*t,8)--cycle); D(CR(D((2*t,2)),2)); D(CR(D((2*t,5)),1)); D('B', (0,0),SW); D('C',(4*t,0), SE); D('A', (2*t, 8), N); pair A = foot((2*t,2),(2*t,8),(4*t,0)), B = foot((2*t,5),(2*t,8),(4*t,0)); D((2*t,0)--(2*t,8)); D((2*t,2)--D(A)); D((2*t,5)--D(B)); D(rightanglemark((2*t,2),A,(4*t,0))); D(rightanglemark((2*t,5),B,(4*t,0))); MP('2', (2*t,3), W); MP('1',(2*t, 5.5), W); MP("F",(2*t,0)); MP("O_1",(2*t,5),W); MP("O_2",(2*t,2),W); MP("D",B,NE); MP("E",A,NE); [/asy]
We see that $\triangle ADO_1 \sim \triangle AEO_2 \sim \triangle AFC$ . Using the first pair of similar triangles , we write the proportion:
$\frac{AO_1}{AO_2} = \frac{DO_1}{EO_2} \Longrightarrow \frac{AO_1}{AO_1 + 3} = \frac{1}{2} \Longrightarrow AO_1 = 3$
By the Pythagorean Theorem , we have $AD = \sqrt{3^2-1^2} = \sqrt{8}$ .
Now using $\triangle ADO_1 \sim \triangle AFC$ ,
$\frac{AD}{AF} = \frac{DO_1}{FC} \Longrightarrow \frac{2\sqrt{2}}{8} = \frac{1}{FC} \Longrightarrow FC = 2\sqrt{2}$
Hence, the area of the triangle is \[\frac{1}{2}\cdot AF \cdot BC = \frac{1}{2}\cdot AF \cdot (2\cdot CF) = AF \cdot CF = 8\left(2\sqrt{2}\right) = \boxed{\textbf{(D) } 16\sqrt{2}}\]

## Solution 2
[asy] size(200); pathpen = linewidth(0.7); pointpen = black; pointfontpen = fontsize(10); real t=2^0.5; D((0,0)--(4*t,0)--(2*t,8)--cycle); D(CR(D((2*t,2)),2)); D(CR(D((2*t,5)),1)); D('B', (0,0),SW); D('C',(4*t,0), SE); D('A', (2*t, 8), N); pair A = foot((2*t,2),(2*t,8),(4*t,0)), B = foot((2*t,5),(2*t,8),(4*t,0)); D((2*t,0)--(2*t,8)); D((2*t,2)--D(A)); D((2*t,5)--D(B)); D(rightanglemark((2*t,2),A,(4*t,0))); D(rightanglemark((2*t,5),B,(4*t,0))); MP('2', (2*t,3), W); MP('1',(2*t, 5.5), W); MP("F",(2*t,0)); MP("O_1",(2*t,5),W); MP("O_2",(2*t,2),W); MP("D",B,NE); MP("E",A,NE); [/asy]
Since $\triangle{A O_1 D} \sim \triangle{A O_2 E},$ we have that $\frac{A O_1}{A O_2} = \frac{O_1 D}{O_2 E} = \frac{1}{2}$ .
Since we know that $O_1 O_2 = 1 + 2 = 3,$ the total length of $A O_2 = 2 \cdot 3 = 6.$
We also know that $O_2 F = 2$ , so $A F = A O_2 + O_2 F = 6 + 2 = 8.$
Also, since $\triangle{ABF} \sim \triangle{A E O_2},$ we have that $\frac{AC}{A O_2} = \frac{FC}{O_2 E}.$
Since we know that $A O_2 = 6$ and $O_2 E = 2,$ we have that $\frac{AC}{6} = \frac{FC}{2}.$
This equation simplified gets us $AC = 3 \cdot FC.$
Let $FC = a$
By the Pythagorean Theorem on $\triangle{AFC},$ we have that $AF^2 + FC^2 = AC^2.$
We know that $AF = 8$ , $FC = a$ and $AC = 3a$ so we have $8^2 + a^2 = (3a)^2.$
Simplifying, we have that $64 = 8a^2 \Rightarrow a^2 = 8 \Rightarrow a = \sqrt{8} = 2 \sqrt{2}.$
Recall that $FC=a$ .
Therefore, $BC = 2 \cdot FC = 2 \cdot 2 \sqrt{2} = 4 \sqrt{2}.$
Since the height is $AF = 8,$ we have the area equal to $\frac{4 \sqrt{2} \cdot 8}{2}=16\sqrt{2}.$
Thus our answer is $\boxed{\textbf{(D) }16 \sqrt{2}}$ .
~mathboy282
Alternatively, using the fact that Area = radius $\cdot$ semiperimeter, and knowing that $AC = \sqrt{FC^2 + 64}$ , we can set up the equation \[2FC + 2 \sqrt{FC^2 + 64} = 8FC.\] Grouping and getting rid of the square root gives us $FC^2 + 64 = 9FC^2$ , meaning that $FC = 2 \sqrt{2}$ . Thus, the area of the triangle is $\boxed{16 \sqrt{2}, D}$ ~ booking(Please feel free to edit this, since this is my first time writing a solution!)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .