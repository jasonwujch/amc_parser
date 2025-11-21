# 2021 Fall AMC 10B Problem 13

## Problem

A square with side length $3$ is inscribed in an isosceles triangle with one side of the square along the base of the triangle. A square with side length $2$ has two vertices on the other square and the other two on sides of the triangle, as shown. What is the area of the triangle?

[asy] //diagram by kante314 draw((0,0)--(8,0)--(4,8)--cycle, linewidth(1.5)); draw((2,0)--(2,4)--(6,4)--(6,0)--cycle, linewidth(1.5)); draw((3,4)--(3,6)--(5,6)--(5,4)--cycle, linewidth(1.5)); [/asy]

$(\textbf{A})\: 19\frac14\qquad(\textbf{B}) \: 20\frac14\qquad(\textbf{C}) \: 21 \frac34\qquad(\textbf{D}) \: 22\frac12\qquad(\textbf{E}) \: 23\frac34$

## Solution 1
Let's split the triangle down the middle and label it:
[asy] import olympiad; pair A,B,C,D,E,F,G,H,I,J,K; A = origin; B = (0.5,0); C=(2.5,0); D=(3,0); E = (0.5,2); F=(0.83333333333,2); G=(2.166666666667,2); H=(2.5,2); I=(0.83333333333,3.333333333333); J=(2.166666666667,3.3333333333); K=(1.5,6); draw(A--D--K--cycle); draw(B--E); draw(C--H); draw(F--I); draw(G--J); draw(I--J); draw(E--H); draw(K--(1.5,0)); label("$A$",(1.5,0),S); label("$B$",(1.5,2),SW); label("$C$",(1.5,3.3333333),SW); label("$D$",D,SE); label("$E$",H,SE); label("$F$",J,SE); label("$G$",K,N); [/asy]
We see that $\bigtriangleup ADG \sim \bigtriangleup BEG \sim \bigtriangleup CFG$ by AA similarity. $BE = \frac{3}{2}$ because $AG$ cuts the side length of the square in half; similarly, $CF = 1$ . Let $CG = h$ : then by side ratios,
\[\frac{h+2}{h} = \frac{\frac{3}{2}}{1} \implies 2(h+2) = 3h \implies h = 4\] .
Now the height of the triangle is $AG = 4+2+3 = 9$ . By side ratios, \[\frac{9}{4} = \frac{AD}{1} \implies AD = \frac{9}{4}\] .
The area of the triangle is $AG\cdot AD = 9 \cdot \frac{9}{4} = \frac{81}{4} = \boxed{\textbf{(B) }20 \frac{1}{4}}$
~KingRavi

## Solution 2
By similarity, the height is $3+\frac31\cdot2=9$ and the base is $\frac92\cdot1=4.5$ . Thus the area is $\frac{9\cdot4.5}2=20.25=\boxed{\textbf{(B) }20 \frac{1}{4}}$ .
~Hefei417, or 陆畅 Sunny from China

## Solution 3 (With two different endings)
This solution is based on this figure: Image:2021_AMC_10B_(Nov)_Problem_13,_sol.png
Denote by $O$ the midpoint of $AB$ .
Because $FG = 3$ , $JK = 2$ , $FJ = KG$ , we have $FJ = \frac{1}{2}$ .
We observe $\triangle ADF \sim \triangle FJH$ . Hence, $\frac{AD}{FJ} = \frac{FD}{HJ}$ . Hence, $AD = \frac{3}{4}$ . By symmetry, $BE = AD = \frac{3}{4}$ .
Therefore, $AB = AD + DE + BE = \frac{9}{2}$ .
Because $O$ is the midpoint of $AB$ , $AO = \frac{9}{4}$ .
We observe $\triangle AOC \sim \triangle ADF$ . Hence, $\frac{OC}{DF} = \frac{AO}{AD}$ . Hence, $OC = 9$ .
Therefore, ${\rm Area} \ \triangle ABC = \frac{1}{2} AB \cdot OC = \frac{81}{4} = 20 \frac{1}{4}$ .
Therefore, the answer is $\boxed{\textbf{(B) }20 \frac{1}{4}}$ .
~Steven Chen (www.professorchenedu.com)
Alternatively, we can find the height in a slightly different way.
Following from our finding that the base of the large triangle $AB = \frac{9}{2}$ , we can label the length of the altitude of $\triangle{CHI}$ as $x$ . Notice that $\triangle{CHI} \sim \triangle{CAB}$ . Hence, $\frac{HI}{AB} = \frac{x}{CO}$ . Substituting and simplifying, $\frac{HI}{AB} = \frac{x}{CO} \Rightarrow \frac{2}{\frac{9}{2}} = \frac{x}{x+5} \Rightarrow \frac{x}{x+5} = \frac{4}{9} \Rightarrow x = 4 \Rightarrow CO = 4 + 5 = 9$ . Therefore, the area of the triangle is $\frac{\frac{9}{2} \cdot 9}{2} = \frac{81}{4} = \boxed{\textbf{(B) }20 \frac{1}{4}}$ .
~mahaler

## Solution 4 (Coordinates)
For convenience, we will use the image provided in the third solution.
We can set $O$ as the origin.
We know that $FG = 3$ and $JK = 2$ .
We subtract $JK$ from $FG$ and divide by $2$ to get $KG = FJ = \frac{1}{2}$ .
Since $HIKJ$ is a square, we know that $IK = 2$ .
Using rise over run, we find that the slope of $CB$ is $\frac{-2}{0.5} = -4$ .
The coordinates of $I$ are $(1, 5)$ . We plug this in to get the equation of the line that $CB$ runs along: \[y = -4x + 9\]
We know that the $x-value$ of $C$ is $0$ . Using this, we find that the $y-value$ is $9$ . So the coordinates of $C$ are $(0, 9)$ .
This gives us the height of $\triangle ACB$ : $CO = 9$ .
Now we need to find the coordinates of $B$ .
We know that the $y-value$ is $0$ . Plugging this in, we find $0 = -4x +9$ , or $\frac{9}{4} = x$ .
The coordinates of $B$ are $(\frac{9}{4}, 0)$ .
Since $\triangle ACB$ is symmetrical along $CO$ , we can multiply $CO$ by $OB$ to get \[9 \cdot \frac{9}{4} = \frac{81}{4}\]
Simplifying, we get $\boxed{\textbf{(B) }20 \frac{1}{4}}$ for the area.
~Achelois

## Solution 5 (interesting)
Call the right triangle to the right of the square with side length $2$ triangle $a_1$ . Similarly, call the triangle to the right of the square with side length $3$ $a_2$ . Label the ENTIRE triangle triangle ABC. We notice AA similarity between $a_1$ and $a_2$ . Additionally, the base of $a_1$ must have a length of $0.5$ , because the middle square takes up a length of $2$ and the other length of $1$ must be evenly split between the two congruent triangles next to the square, being all situated on a length of $3$ . We then see that the ratio of $2:1$ must hold for the base of triangle ABC. $3:x = 2:1$ , and we find that $x = 1.5$ . The length of the base is then $1.5 + 3 = 9/2$ .
We can then find the height of the triangle by thinking about a geometrical sequence. It must be possible that you could continue inscribing squares in the triangles that are made, as every triangle created is similar to the one before it. Using this, we have the geometrical sequence of $3 + 2 + 4/3 +...$ (for each side length is the height that is being added) Using the geometrical sequence formula, we find $\frac{3}{1 - \frac{2}{3}}= \frac{3}{\frac{1}{3}} = 3\cdot3= 9$ . The height is $9$ whilst the base length is $\frac{9}{2}$ , and multiplying both values and dividing by $2$ yields $\frac{9(9)}{2(2)} = 81/4 = \boxed{\textbf{(B) }20 \frac{1}{4}}$
~ martianrunner (i do NOT know how to latex)~RandomMathGuy500 (latex)

## Video Solution by Interstigation
https://www.youtube.com/watch?v=mq4e-s9ENas

## Video Solution
https://youtu.be/gxZE3cscswo
~Education, the Study of Everything

## Video Solution by WhyMath
https://youtu.be/Uh5Umekq4A8
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/R7TwXgAGYuw?t=639
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .