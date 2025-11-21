# 2004 AMC 10B Problem 20

## Problem

In $\triangle ABC$ points $D$ and $E$ lie on $BC$ and $AC$ , respectively. If $AD$ and $BE$ intersect at $T$ so that $\frac{AT}{DT}=3$ and $\frac{BT}{ET}=4$ , what is $\frac{CD}{BD}$ ?

[asy] unitsize(1.5 cm); pair A, B, C, D, E, F, T; A = (0,0); B = (3,3); C = (4.5,0); D = (2*C + B)/3; E = (5*C + 2*A)/7; T = extension(A,D,B,E); F = extension(D, D + A - C, B, E); draw(A--B--C--cycle); draw(A--D); draw(B--E); label("$A$", A, SW); label("$B$", B, N); label("$C$", C, SE); label("$D$", D, NE); label("$E$", E, S); label("$T$", T, SE); [/asy]

$\mathrm{(A) \ } \frac{1}{8} \qquad \mathrm{(B) \ } \frac{2}{9} \qquad \mathrm{(C) \ } \frac{3}{10} \qquad \mathrm{(D) \ } \frac{4}{11} \qquad \mathrm{(E) \ } \frac{5}{12}$

## Solution 1 (Triangle Areas)
We use the square bracket notation $[\cdot]$ to denote area.
WLOG, we can assume $[\triangle BTD] = 1$ . Then $[\triangle BTA] = 3$ , and $[\triangle ATE] = 3/4$ . We have $CD/BD = [\triangle ACD]/[\triangle ABD]$ , so we need to find the area of quadrilateral $TDCE$ .
Draw the line segment $TC$ to form the two triangles $\triangle TDC$ and $\triangle TEC$ . Let $x = [\triangle TDC]$ , and $y = [\triangle TEC]$ . By considering triangles $\triangle BTC$ and $\triangle ETC$ , we obtain $(1+x)/4=y$ , and by considering triangles $\triangle ATC$ and $\triangle DTC$ , we obtain $\dfrac{\frac{3}{4} +y}{3}=x$ . Solving, we get $x=4/11$ , $y=15/44$ , so the area of quadrilateral $TDCE$ is $x+y=31/44$ .
Therefore $\frac{CD}{BD}=\frac{\frac{3}{4}+\frac{31}{44}}{3+1}=\boxed{\textbf{(D)} \frac{4}{11}}$

## Solution 2 (Triangle Areas, Alternate Approach)
We observe that $\frac{BC}{CD} = \frac{[BAE]}{[DAE]}$ . The proof is that if $B_H$ and $D_H$ are the feet of the altitudes from $B$ and $D$ , respectively, to $AC$ , then both sides of that equation are equal to $\frac{BB_H}{DD_H}$ .
From there, we can easily finish: \[\frac{BC}{CD} = \frac{[BAE]}{[DAE]} = \frac{[BAT]\cdot\frac{5}{4}}{[EAT]\cdot \frac{4}{3}} = 4\cdot\frac{5}{4}\cdot\frac{3}{4} = \frac{15}{4}\] and thus $\frac{CD}{BD} = \boxed{\textbf{(D)}\frac 4{11}}$ .

## Solution 3 (Mass points)
The presence of only ratios in the problem essentially cries out for mass points.
As per the problem, we assign a mass of $1$ to point $A$ , and a mass of $3$ to $D$ . Then, to balance $A$ and $D$ on $T$ , $T$ has a mass of $4$ .
Now, were we to assign a mass of $1$ to $B$ and a mass of $4$ to $E$ , we'd have $5T$ . Scaling this down by $4/5$ (to get $4T$ , which puts $B$ and $E$ in terms of the masses of $A$ and $D$ ), we assign a mass of $\frac{4}{5}$ to $B$ and a mass of $\frac{16}{5}$ to $E$ .
Now, to balance $A$ and $C$ on $E$ , we must give $C$ a mass of $\frac{16}{5}-1=\frac{11}{5}$ .
Finally, the ratio of $CD$ to $BD$ is given by the ratio of the mass of $B$ to the mass of $C$ , which is $\frac{4}{5}\cdot\frac{5}{11}=\boxed{\textbf{(D)}\ \frac{4}{11}}$ .

## Solution 4 (Coordinates)
Affine transformations preserve ratios of distances, and for any pair of triangles, there is an affine transformation that maps the first one onto the second one. This is why the answer is the same for any $\triangle ABC$ , and we just need to compute it for any single triangle.
We can choose the points $A=(-3,0)$ , $B=(0,4)$ , and $D=(1,0)$ . This way we will have $T=(0,0)$ , and $E=(0,-1)$ . The situation is shown in the picture below:
[asy] unitsize(1cm); defaultpen(0.8); pair A=(-3,0), B=(0,4), C=(15/11,-16/11), D=(1,0), E=(0,-1); draw(A--B--C--cycle); draw(A--D); draw(B--E); pair T=intersectionpoint(A--D,B--E); label("$A$",A,SW); label("$B$",B,N); label("$C$",C,SE); label("$D$",D,NE); label("$E$",E,S); label("$T$",T,NW); label("$3$",A--T,N); label("$4$",B--T,W); label("$1$",D--T,N); label("$1$",E--T,W); [/asy]
The point $C$ is the intersection of the lines $BD$ and $AE$ . The points on the first line have the form $(t,4-4t)$ , the points on the second line have the form $(t,-1-t/3)$ . Solving for $t$ we get $t=15/11$ , hence $C=(15/11,-16/11)$ .
The ratio $CD/BD$ can now be computed simply by observing the $x$ coordinates of $B$ , $C$ , and $D$ :
\[\frac{CD}{BD} = \frac{15/11 - 1}{1 - 0} = \boxed{\textbf{(D)}\frac 4{11}}\]

## Solution 5 (Menelaus)
By Menelaus on triangle $BDT$ , we have that \begin{align*}1&=\dfrac{DA}{TA}\cdot\dfrac{TE}{BE}\cdot\dfrac{BC}{DC} \\ &= \dfrac43 \cdot \dfrac 15 \cdot \dfrac {BC}{DC},\end{align*} giving $\dfrac{BC}{DC} = \dfrac{15}{4}$ . Therefore, $\dfrac{CD}{BD} = \boxed{\textbf{(D)}\dfrac{4}{11}}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .