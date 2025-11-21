# 2020 AMC 10B Problem 8

## Problem

Points $P$ and $Q$ lie in a plane with $PQ=8$ . How many locations for point $R$ in this plane are there such that the triangle with vertices $P$ , $Q$ , and $R$ is a right triangle with area $12$ square units?

$\textbf{(A)}\ 2 \qquad\textbf{(B)}\ 4 \qquad\textbf{(C)}\ 6 \qquad\textbf{(D)}\ 8 \qquad\textbf{(E)}\ 12$

## Solution 1 (Geometry)
Let the brackets denote areas. We are given that \[[PQR]=\frac12\cdot PQ\cdot h_R=12.\] Since $PQ=8,$ it follows that $h_R=3.$
We construct a circle with diameter $\overline{PQ}.$ All such locations for $R$ are shown below:
[asy] /* Made by MRENTHUSIASM */ size(250); pair O, P, Q, R1, R2, R3, R4, R5, R6, R7, R8, I1, I2; O = (0,0); P = (-4,0); Q = (4,0); R1 = (-4,3); R4 = (4,3); R5 = (-4,-3); R8 = (4,-3); path C; C = Circle(O,4); R3 = intersectionpoints(C,R1--R4)[0]; R2 = intersectionpoints(C,R1--R4)[1]; R6 = intersectionpoints(C,R5--R8)[0]; R7 = intersectionpoints(C,R5--R8)[1]; I1 = intersectionpoint(R2--R6,P--Q); I2 = intersectionpoint(R3--R7,P--Q); markscalefactor=0.0375; draw(rightanglemark(R1,P,Q)^^rightanglemark(R2,I1,Q)^^rightanglemark(R3,I2,P)^^rightanglemark(R4,Q,P),red); draw(Circle(O,4),dashed); draw(R1--R5^^R4--R8^^R2--R6^^R3--R7^^P--Q); dot(O,linewidth(4)); dot("$P$",P,1.5W,linewidth(4)); dot("$Q$",Q,1.5E,linewidth(4)); dot("$R_1$",R1,1.5NW,blue+linewidth(4)); dot("$R_4$",R4,1.5NE,blue+linewidth(4)); dot("$R_5$",R5,1.5SW,blue+linewidth(4)); dot("$R_8$",R8,1.5SE,blue+linewidth(4)); dot("$R_2$",R2,1.5NW,blue+linewidth(4)); dot("$R_3$",R3,1.5NE,blue+linewidth(4)); dot("$R_6$",R6,1.5SW,blue+linewidth(4)); dot("$R_7$",R7,1.5SE,blue+linewidth(4)); dot(I1,linewidth(4)); dot(I2,linewidth(4)); Label L1 = Label("$8$", align=(0,0), position=MidPoint, filltype=Fill(3,0,white)); Label L2 = Label("$3$", align=(0,0), position=MidPoint, filltype=Fill(0,3,white)); draw(P-(0,5)--Q-(0,5), L=L1, arrow=Arrows(),bar=Bars(15)); draw(R4+(2,0)--Q+(2,0), L=L2, arrow=Arrows(),bar=Bars(15)); draw(Q+(2,0)--R8+(2,0), L=L2, arrow=Arrows(),bar=Bars(15)); [/asy]
We apply casework to the right angle of $\triangle PQR:$
1. If $\angle P=90^\circ,$ then $R\in\{R_1,R_5\}$ by the tangent.
1. If $\angle Q=90^\circ,$ then $R\in\{R_4,R_8\}$ by the tangent.
1. If $\angle R=90^\circ,$ then $R\in\{R_2,R_3,R_6,R_7\}$ by the Inscribed Angle Theorem.
Together, there are $\boxed{\textbf{(D)}\ 8}$ such locations for $R.$
Remarks
1. The reflections of $R_1,R_2,R_3,R_4$ about $\overleftrightarrow{PQ}$ are $R_5,R_6,R_7,R_8,$ respectively.
1. The reflections of $R_1,R_2,R_5,R_6$ about the perpendicular bisector of $\overline{PQ}$ are $R_4,R_3,R_8,R_7,$ respectively.
~MRENTHUSIASM

## Solution 2 (Algebra)
Let the brackets denote areas. We are given that \[[PQR]=\frac12\cdot PQ\cdot h_R=12.\] Since $PQ=8,$ it follows that $h_R=3.$
Without loss of generality, let $P=(-4,0)$ and $Q=(4,0).$ We conclude that the $y$ -coordinate of $R$ must be $\pm3.$
We apply casework to the right angle of $\triangle PQR:$
1. $\angle P=90^\circ.$ The -coordinate of must be so we have In this case, there are such locations for
1. $\angle Q=90^\circ.$ The -coordinate of must be so we have In this case, there are such locations for
1. $\angle R=90^\circ.$ For the Pythagorean Theorem gives Solving this equation, we have or For we have by a similar process. In this case, there are such locations for
The $x$ -coordinate of $R$ must be $-4,$ so we have $R=(-4,\pm3).$
In this case, there are such locations for
The $x$ -coordinate of $R$ must be $4,$ so we have $R=(4,\pm3).$
In this case, there are such locations for
For $R=(x,3),$ the Pythagorean Theorem $PR^2+QR^2=PQ^2$ gives \[\left[(x+4)^2+3^2\right]+\left[(x-4)^2+3^2\right]=8^2.\] Solving this equation, we have $x=\pm\sqrt7,$ or $R=\left(\pm\sqrt7,3\right).$
For $R=(x,-3),$ we have $R=\left(\pm\sqrt7,-3\right)$ by a similar process.
In this case, there are such locations for
Together, there are $2+2+4=\boxed{\textbf{(D)}\ 8}$ such locations for $R.$
~MRENTHUSIASM ~mewto

## Video Solution (HOW TO CRITICALLY THINK!!!)
https://youtu.be/C_9Wa_owu9s
~Education, the Study of Everything

## Video Solution
https://youtu.be/OHR_6U686Qg
https://youtu.be/cUzK5DqKaRY
~savannahsolver

## Video Solution by Sohil Rathi
https://youtu.be/GrCtzL0S-Uo?t=19
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .