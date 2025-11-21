# 2014 AIME I Problem 13

## Problem

On square $ABCD$ , points $E,F,G$ , and $H$ lie on sides $\overline{AB},\overline{BC},\overline{CD},$ and $\overline{DA},$ respectively, so that $\overline{EG} \perp \overline{FH}$ and $EG=FH = 34$ . Segments $\overline{EG}$ and $\overline{FH}$ intersect at a point $P$ , and the areas of the quadrilaterals $AEPH, BFPE, CGPF,$ and $DHPG$ are in the ratio $269:275:405:411.$ Find the area of square $ABCD$ .

[asy] pair A = (0,sqrt(850)); pair B = (0,0); pair C = (sqrt(850),0); pair D = (sqrt(850),sqrt(850)); draw(A--B--C--D--cycle); dotfactor = 3; dot("$A$",A,dir(135)); dot("$B$",B,dir(215)); dot("$C$",C,dir(305)); dot("$D$",D,dir(45)); pair H = ((2sqrt(850)-sqrt(306))/6,sqrt(850)); pair F = ((2sqrt(850)+sqrt(306)+7)/6,0); dot("$H$",H,dir(90)); dot("$F$",F,dir(270)); draw(H--F); pair E = (0,(sqrt(850)-6)/2); pair G = (sqrt(850),(sqrt(850)+sqrt(100))/2); dot("$E$",E,dir(180)); dot("$G$",G,dir(0)); draw(E--G); pair P = extension(H,F,E,G); dot("$P$",P,dir(60)); label("$w$", intersectionpoint( A--P, E--H )); label("$x$", intersectionpoint( B--P, E--F )); label("$y$", intersectionpoint( C--P, G--F )); label("$z$", intersectionpoint( D--P, G--H ));[/asy]

## Solution (Official Solution, MAA)
Let $s$ be the side length of $ABCD$ , let $Q$ , and $R$ be the midpoints of $\overline{EG}$ and $\overline{FH}$ , respectively, let $S$ be the foot of the perpendicular from $Q$ to $\overline{CD}$ , let $T$ be the foot of the perpendicular from $R$ to $\overline{AD}$ . [asy] size(150); defaultpen(fontsize(10pt)); pair A,B,C,D,E,F,Fp,G,Gp,H,O,I,J,R,S,T; A=dir(45*3); B=dir(-45*3); C=dir(-45); D=dir(45); O = origin; real theta=15; E=extension(A,B,O,dir(180+theta)); G=extension(C,D,O,dir(theta)); I=extension(A,D,O,dir(90+theta)); J=extension(B,C,O,dir(-90+theta)); H=(A+I)/2; F=H+(J-I); R=midpoint(H--F); S=midpoint(C--D); T=(R.x, A.y); draw(A--B--C--D--cycle^^E--G^^F--H, black+0.8); draw(S--R--T, gray+0.4); dotfactor = 3; dot("$A$",A,dir(135)); dot("$B$",B,dir(215)); dot("$C$",C,dir(305)); dot("$D$",D,dir(45)); dot("$H$",H,dir(90)); dot("$F$",F,dir(270)); dot("$E$",E,dir(180)); dot("$G$",G,dir(0)); dot("$Q$",O,dir(-90)); dot("$R$",R,dir(-180)); dot("$S$",S,dir(0)); dot("$T$",T,dir(90)); pair P = extension(F,H,E,G); dot("$P$",P,dir(180+60)); [/asy] The fraction of the area of the square $ABCD$ which is occupied by trapezoid $BCGE$ is \[\frac{275+405}{269+275+405+411}=\frac 12,\] so $Q$ is the center of $ABCD$ . Thus $R$ , $Q$ , $S$ are collinear, and $RT=QS=\tfrac 12 s$ . Similarly, the fraction of the area occupied by trapezoid $CDHF$ is $\tfrac 35$ , so $RS=\tfrac 35s$ and $RQ=\tfrac{1}{10}s$ .
Because $\triangle QSG \cong \triangle RTH$ , the area of $DHPG$ is the sum \[[DHPG]=[DTRS]+[RPQ].\] Rectangle $DTRS$ has area $RS\cdot RT = \tfrac 35s\cdot \tfrac 12 s = \tfrac{3}{10}s^2$ . If $\angle QRP = \theta$ , then $\triangle RPQ$ has area \[[RPQ]= \tfrac 12 \cdot \tfrac 1{10}s\sin\theta \cdot \tfrac 1{10}s\cos\theta = \tfrac 1{400}s^2\sin 2\theta.\] Therefore the area of $[DHPG]$ is $s^2(\tfrac 3{10}+\tfrac 1{400}\sin 2\theta)$ . Because the area of trapezoid $CDHF$ is $\tfrac 35 s^2$ , the area of $CGPF$ is $s^2(\tfrac 3{10}-\tfrac 1{400}\sin 2\theta)$ .
Because these areas are in the ratio $411:405=(408+3):(408-3)$ , it follows that \[\frac{\frac 1{400}\sin 2\theta}{\frac 3{10}}=\frac 3{408},\] from which we get $\sin 2\theta = \tfrac {15}{17}$ . Note that $\theta =\angle RHT > \angle QAT = 45^\circ$ , so $\cos 2\theta = -\sqrt{1-\sin^2 2\theta}= -\tfrac 8{17}$ and $\sin^2\theta = \tfrac{1}{2}(1-\cos 2\theta) = \tfrac{25}{34}$ . Then \[[ABCD]=s^2 = EG^2\sin^2\theta = 34^2 \cdot \tfrac {25}{34} = 850.\]

## Solution 1
Let $s$ be the side length of $ABCD$ , let $[ABCD]=1360a$ . Let $Q$ and $R$ be the midpoints of $\overline{EG}$ and $\overline{FH}$ , respectively; because $269+411=275+405$ , $Q$ is also the center of the square. Draw $\overline{IJ} \parallel \overline{HF}$ through $Q$ , with $I$ on $\overline{AD}$ , $J$ on $\overline{BC}$ . [asy] size(150); defaultpen(fontsize(9pt)); pair A,B,C,D,E,F,G,H,I,J,L,P,Q,R,S; Q=MP("Q",origin,down); A=MP("A",(-1,1),dir(135)); B=MP("B",(-1,-1),dir(225)); C=MP("C",(1,-1),dir(-45)); D=MP("D",(1,1),dir(45)); real theta = 20; real shift=0.4; E=MP("E",extension(A,B,Q,dir(theta)),left); J=MP("J",extension(B,C,Q,dir(90+theta)),down); F=MP("F",J+(shift*left),down); G=MP("G",extension(C,D,Q,dir(theta)),right); I=MP("I",extension(A,D,Q,dir(90+theta)),up); H=MP("H",I+(shift*left),up); P=MP("P",extension(E,G,F,H),2*dir(-110)); R=MP("R",extension(F,H,Q,left),left); draw(A--B--C--D--cycle^^E--G^^F--H, black+1); draw(R--Q^^I--J, gray); [/asy] Segments $\overline{EG}$ and $\overline{IJ}$ divide the square into four congruent quadrilaterals, each of area $\tfrac 14 [ABCD]=340a$ . Then \[[HFJI]=[ABJI]-[ABFH]=136a.\] The fraction of the total area occupied by parallelogram $HFJI$ is $\tfrac 1{10}$ , so $RQ=\tfrac{s}{10}$ .
Because $[HFJI]= HF\cdot PQ$ , with $HF=34$ , we get $PQ=4a$ . Now \[[PQR]=[HPQI]-[HRQI]= ([AEQI]-[AEPH])-\tfrac 12[IJFH] = 3a,\] and because $[PQR]=\tfrac 12 \cdot PQ\cdot PR$ , with $PQ=4a$ , we get $PR=\tfrac 32$ . By Pythagoras' Theorem on $\triangle PQR$ , we get \[16a^2+\frac 94 =\tfrac{68}{5}a,\quad \text{i.e.}\quad 320a^2-272a+45=0,\] with roots $a=\tfrac 9{40}$ or $a=\tfrac58$ . The former leads to a square with diagonal less than $34$ , which can't be, since $EG=FH=34$ ; therefore $a=\tfrac 58$ and $[ABCD]=850$ .

## Solution 2 (Fakesolve)
$269+275+405+411=1360$ , a multiple of $17$ . In addition, $EG=FH=34$ , which is $17\cdot 2$ . Therefore, we suspect the square of the "hypotenuse" of a right triangle, corresponding to $EG$ and $FH$ must be a multiple of $17$ . All of these triples are primitive:
\[17=1^2+4^2\] \[34=3^2+5^2\] \[51=\emptyset\] \[68=\emptyset\text{ others}\] \[85=2^2+9^2=6^2+7^2\] \[102=\emptyset\] \[119=\emptyset \dots\]
The sides of the square can only equal the longer leg, or else the lines would have to extend outside of the square. Substituting $EG=FH=34$ : \[\sqrt{17}\rightarrow 34\implies 8\sqrt{17}\implies A=\textcolor{red}{1088}\] \[\sqrt{34}\rightarrow 34\implies 5\sqrt{34}\implies A=850\] \[\sqrt{85}\rightarrow 34\implies \{18\sqrt{85}/5,14\sqrt{85}/5\}\implies A=\textcolor{red}{1101.6,666.4}\]
Thus, $\boxed{850}$ is the only valid answer.

## Solution 3
Continue in the same way as solution 1 to get that $POK$ has area $3a$ , and $OK = \frac{d}{10}$ . You can then find $PK$ has length $\frac 32$ .
Then, if we drop a perpendicular from $H$ to $BC$ at $L$ , We get $\triangle HLF \sim \triangle OPK$ .
Thus, $LF = \frac{15\cdot 34}{d}$ , and we know $HL = d$ , and $HF = 34$ . Thus, we can set up an equation in terms of $d$ using the Pythagorean theorem.
\[\frac{15^2 \cdot 34^2}{d^2} + d^2 = 34^2\]
\[d^4 - 34^2 d^2 + 15^2 \cdot 34^2 = 0\]
\[(d^2 - 34 \cdot 25)(d^2 - 34 \cdot 9) = 0\]
$d^2 = 34 \cdot 9$ is extraneous, so $d^2 = 34 \cdot 25$ . Since the area is $d^2$ , we have it is equal to $34 \cdot 25 = \boxed{850}$
-Alexlikemath

## Video Solution
https://youtu.be/Kcug2ALOjkA?si=VoImhnX5rAKhprgk
~MathProblemSolvingSkills.com

## Video Solution by Punxsutawney Phil
https://youtube.com/watch?v=wrxET2c0ZgU
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .