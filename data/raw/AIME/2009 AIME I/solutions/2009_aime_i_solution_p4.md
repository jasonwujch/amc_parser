# 2009 AIME I Problem 4

## Problem

In parallelogram $ABCD$ , point $M$ is on $\overline{AB}$ so that $\frac {AM}{AB} = \frac {17}{1000}$ and point $N$ is on $\overline{AD}$ so that $\frac {AN}{AD} = \frac {17}{2009}$ . Let $P$ be the point of intersection of $\overline{AC}$ and $\overline{MN}$ . Find $\frac {AC}{AP}$ .

## Solution 1
One of the ways to solve this problem is to make this parallelogram a straight line. So the whole length of the line is $APC$ ( $AMC$ or $ANC$ ), and $ABC$ is $1000x+2009x=3009x.$
$AP$ ( $AM$ or $AN$ ) is $17x.$
So the answer is $3009x/17x = \boxed{177}$

## Solution 2
Draw a diagram with all the given points and lines involved. Construct parallel lines $\overline{DF_2F_1}$ and $\overline{BB_1B_2}$ to $\overline{MN}$ , where for the lines the endpoints are on $\overline{AM}$ and $\overline{AN}$ , respectively, and each point refers to an intersection. Also, draw the median of quadrilateral $BB_2DF_1$ $\overline{E_1E_2E_3}$ where the points are in order from top to bottom. Clearly, by similar triangles, $BB_2 = \frac {1000}{17}MN$ and $DF_1 = \frac {2009}{17}MN$ . It is not difficult to see that $E_2$ is the center of quadrilateral $ABCD$ and thus the midpoint of $\overline{AC}$ as well as the midpoint of $\overline{B_1}{F_2}$ (all of this is easily proven with symmetry). From more triangle similarity, $E_1E_3 = \frac12\cdot\frac {3009}{17}MN\implies AE_2 = \frac12\cdot\frac {3009}{17}AP\implies AC = 2\cdot\frac12\cdot\frac {3009}{17}AP$ $= \boxed{177}AP$ .

## Solution 3
Using vectors, note that $\overrightarrow{AM}=\frac{17}{1000}\overrightarrow{AB}$ and $\overrightarrow{AN}=\frac{17}{2009}\overrightarrow{AD}$ . Note that $\overrightarrow{AP}=\frac{x\overrightarrow{AM}+y\overrightarrow{AN}}{x+y}$ for some positive x and y, but at the same time is a scalar multiple of $\overrightarrow{AB}+\overrightarrow{AD}$ . So, writing the equation $\overrightarrow{AP}=\frac{x\overrightarrow{AM}+y\overrightarrow{AN}}{x+y}$ in terms of $\overrightarrow{AB}$ and $\overrightarrow{AD}$ , we have $\overrightarrow{AP}=\frac{\frac{17x}{1000}\overrightarrow{AB}+\frac{17y}{2009}\overrightarrow{AD}}{x+y}$ . But the coefficients of the two vectors must be equal because, as already stated, $\overrightarrow{AP}$ is a scalar multiple of $\overrightarrow{AB}+\overrightarrow{AD}$ . We then see that $\frac{x}{x+y}=\frac{1000}{3009}$ and $\frac{y}{x+y}=\frac{2009}{3009}$ . Finally, we have $\overrightarrow{AP}=\frac{17}{3009}(\overrightarrow{AB}+\overrightarrow{AD})$ and, simplifying, $\overrightarrow{AB}+\overrightarrow{AD}=177\overrightarrow{AP}$ and the desired quantity is $177$ .

## Solution 4
We approach the problem using mass points on triangle $ABD$ as displayed below. [asy] pair A=(0,0),B=(50,0),D=(10,40),C=B+D,M=(8,0),NN=(2,8); draw(A--B--C--D--cycle); draw(B--D^^A--C^^M--NN); pair O=extension(A,C,B,D); pair P=extension(A,C,M,NN); dot(A);dot(B);dot(C);dot(D);dot(O);dot(M);dot(NN);dot(P); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,NE); label("$D$",D,NW); label("$M$",M,S); label("$N$",NN,NW); label("$P$",P,NNE); label("$O$",O,N); [/asy]
But as $MN$ does not protrude from a vertex, we will have to "split the mass" at point $A$ . First, we know that $DO$ is congruent to $BO$ because diagonals of parallelograms bisect each other. Therefore, we can assign equal masses to points $B$ and $D$ . In this case, we assign $B$ and $D$ a mass of 17 each. Now we split the mass at $A$ , so we balance segments $AB$ and $AD$ separately, and then the mass of $A$ is the sum of those masses. A mass of 983 is required to balance segment $AB$ , while a mass of 1992 is required to balance segment $AD$ . Therefore, $A$ has a mass of $1992+983=2975$ . Also, $O$ has a mass of 34. Therefore, $\frac{AO}{AP}=\frac{2975+34}{34}=\frac{3009}{34}$ , so $\frac{AC}{AP}=\frac{2 (3009)}{34}=177$ .

## Solution 5
Assume, for the ease of computation, that $AM=AN=17$ , $AB=1000$ , and $AD=2009$ . Now, let line $MN$ intersect line $CD$ at point $X$ and let $Y$ be a point such that $XY\parallel AD$ and $AY\parallel DX$ . As a result, $ADXY$ is a parallelogram. By construction, $\triangle MAN\sim \triangle MYX$ so \[\frac{MY}{MA}=\frac{YX}{AN}=\frac{AD}{AN}=\frac{2009}{17}\implies MY=2009\] and $AY=DX=2009-17$ . Also, because $AM\parallel XC$ , we have $\triangle PAM\sim \triangle PCX$ so \[\frac{PC}{PA}=\frac{CX}{AM}=\frac{DX+CD}{AM}=\frac{2009-17+1000}{17}=176.\] Hence, $\frac{AC}{AP}=\frac{PC}{PA}+1=\boxed{177}.$

## Solution 6(Coordinate Geometry)
Assign $A = (0,0)$ . Since there are no constraints in the problem against this, assume $ABCD$ to be a rectangle with dimensions $1000 \times 2009.$ Now, we can assign \[A=(0,0)\] \[B=(1000, 0)\] \[C=(1000,-2009)\] \[D=(0,-2009).\]
Then, since $\frac{AM}{AB} = \frac{17}{1000}$ and $AB = 1000$ , we can place $M$ at $(17, 0).$ Similarly, place $AN$ at $(0, 17).$ Then, the equation of line $MN$ is $y=x-17,$ and the equation of $AC$ is $y=\frac{-2009}{1000}x.$ Solve to find point $P$ at $\left( \frac{1000}{177}, \frac{-2009}{177} \right)$ .
We can calculate vectors to represent the distances: \[\overrightarrow{AC}= <1000, -2009>\] \[\overrightarrow{AP}= \frac{1}{177}<1000, -2009>.\] In this way, we can see that \[AC:AP = 177:1,\] and our answer is $\boxed{177}.$
~ HappyHuman
### Note
It is possible to use coordinate geometry without setting $ABCD$ as a rectangle, either by projecting the plane onto another (tilted) plane or removing the restriction that the axes have to be perpendicular .

## Solution 7 (Coordinates and Similar triangles)
Let $ABCD$ be a square with side length $1$ where $D = (0,0)$ , $A = (0,1)$ , $B = (1,1)$ , and $C = (1,0)$ .
Draw $M$ on $AB$ such that $AM$ has length $\frac{17}{1000}$ and $AN$ has length $\frac{17}{2009}$ . Draw $AC$ with $P$ as the intersection point of $AC$ and $MN$ .
$N$ has coordinates $(0, 1-\frac{17}{2009}) = (0, \frac{1992}{2009})$
Extend lines $MN$ and $CD$ such that their intersection point is point $E$ , which lies on $y=0$ .
Line $ME$ has slope $\frac{AN}{AM} = \frac{1000}{2009}$ .
With the y-intercept $N$ it has the equation $y = \frac{1000}{2009}x + \frac{1992}{2009}$ .
Solving for the $x$ coordinate on point $E$ $(y = 0)$ , $x = -\frac{1992}{1000}$ . $ED$ has length $\frac{1992}{1000}$ and $EC$ has length $\frac{1992}{1000} + 1 = \frac{2992}{1000}$ .
Triangles $APM$ and $CPE$ are similar (AA). $\frac{AP}{PC} = \frac{AM}{EC} = \frac{2992}{17}$ . $PC = \frac{2992}{17}AP$
$\frac{AC}{AP} = \frac{PC+AP}{AP} = \frac{3009}{17} = 177$ .
~unhappyfarmer

## Video Solution
Unique solution: https://youtu.be/2Xzjh6ae0MU
~IceMatrix

## Video Solution
https://youtu.be/kALrIDMR0dg
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.