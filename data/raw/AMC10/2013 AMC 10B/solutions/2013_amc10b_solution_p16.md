# 2013 AMC 10B Problem 16

## Problem

In triangle $ABC$ , medians $AD$ and $CE$ intersect at $P$ , $PE=1.5$ , $PD=2$ , and $DE=2.5$ . What is the area of $AEDC$ ?

[asy] unitsize(0.2cm); pair A,B,C,D,E,P; A=(0,0); B=(80,0); C=(20,40); D=(50,20); E=(40,0); P=(33.3,13.3); draw(A--B); draw(B--C); draw(A--C); draw(C--E); draw(A--D); draw(D--E); dot(A); dot(B); dot(C); dot(D); dot(E); dot(P); label("A",A,SW); label("B",B,SE); label("C",C,N); label("D",D,NE); label("E",E,SSE); label("P",P,SSW); [/asy]

$\textbf{(A) }13 \qquad \textbf{(B) }13.5 \qquad \textbf{(C) }14 \qquad \textbf{(D) }14.5 \qquad \textbf{(E) }15$

## Solution 1 ( mass points)
Let us use mass points: Assign $B$ mass $1$ . Thus, because $E$ is the midpoint of $AB$ , $A$ also has a mass of $1$ . Similarly, $C$ has a mass of $1$ . $D$ and $E$ each have a mass of $2$ because they are between $B$ and $C$ and $A$ and $B$ respectively. Note that the mass of $D$ is twice the mass of $A$ , so $AP$ must be twice as long as $PD$ . PD has length $2$ , so $AP$ has length $4$ and $AD$ has length $6$ . Similarly, $CP$ is twice $PE$ and $PE=1.5$ , so $CP=3$ and $CE=4.5$ . Now note that triangle $PED$ is a $3-4-5$ right triangle with the right angle $DPE$ . Since the diagonals of quadrilaterals $AEDC$ , $AD$ and $CE$ , are perpendicular, the area of $AEDC$ is $\frac{6 \times 4.5}{2}=\boxed{\textbf{(B)} 13.5}$

## Solution 2
Note that triangle $DPE$ is a right triangle, and that the four angles (angles $APC, CPD, DPE,$ and $EPA$ ) that have point $P$ are all right angles. Using the fact that the centroid ( $P$ ) divides each median in a $2:1$ ratio, $AP=4$ and $CP=3$ . Quadrilateral $AEDC$ is now just four right triangles. The area is $\frac{4\cdot 1.5+4\cdot 3+3\cdot 2+2\cdot 1.5}{2}=\boxed{\textbf{(B)} 13.5}$

## Solution 3
From the solution above, we can find that the lengths of the diagonals are $6$ and $4.5$ . Now, since the diagonals of AEDC are perpendicular, we use the area formula to find that the total area is $\frac{6\times4.5}{2} = \frac{27}{2} = 13.5 = \boxed{\textbf{(B)} 13.5}$

## Solution 4
From the solutions above, we know that the sides CP and AP are 3 and 4 respectively because of the properties of medians that divide cevians into 1:2 ratios. We can then proceed to use the heron's formula on the middle triangle EPD and get the area of EPD as 3/2, (its simple computation really, nothing large). Then we can find the areas of the remaining triangles based on side and ratio length of the bases.

## Solution 5
We know that $[AEDC]=\frac{3}{4}[ABC]$ , and $[ABC]=3[PAC]$ using median properties. So Now we try to find $[PAC]$ . Since $\triangle PAC\sim \triangle PDE$ , then the side lengths of $\triangle PAC$ are twice as long as $\triangle PDE$ since $D$ and $E$ are midpoints. Therefore, $\frac{[PAC]}{[PDE]}=2^2=4$ . It suffices to compute $[PDE]$ . Notice that $(1.5, 2, 2.5)$ is a Pythagorean Triple, so $[PDE]=\frac{1.5\times 2}{2}=1.5$ . This implies $[PAC]=1.5\cdot 4=6$ , and then $[ABC]=3\cdot 6=18$ . Finally, $[AEDC]=\frac{3}{4}\times 18=\boxed{13.5}$ .
~CoolJupiter

## Solution 6
As from Solution 4, we find the area of $\triangle DPE$ to be $\frac{3}{2}$ . Because $DE = \frac{5}{2}$ , the altitude perpendicular to $DE = \frac{6}{5}$ . Also, because $DE || AC$ , $\triangle ABC$ is similar to $\triangle{DBE}$ with side length ratio $2:1$ , so $AC=5$ and the altitude perpendicular to $AC = \frac{12}{5}$ . The altitude of trapezoid $ACDE$ is then $\frac{18}{5}$ and the bases are $\frac{5}{2}$ and $5$ . So, we use the formula for the area of a trapezoid to find the area of $ACDE = \boxed{13.5}$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .