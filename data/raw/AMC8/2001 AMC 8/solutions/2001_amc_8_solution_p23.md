# 2001 AMC 8 Problem 23

## Problem

Points $R$ , $S$ and $T$ are vertices of an equilateral triangle, and points $X$ , $Y$ and $Z$ are midpoints of its sides. How many noncongruent triangles can be drawn using any three of these six points as vertices?

[asy] pair SS,R,T,X,Y,Z; SS = (2,2*sqrt(3)); R = (0,0); T = (4,0); X = (2,0); Y = (1,sqrt(3)); Z = (3,sqrt(3)); dot(SS); dot(R); dot(T); dot(X); dot(Y); dot(Z); label("$S$",SS,N); label("$R$",R,SW); label("$T$",T,SE); label("$X$",X,S); label("$Y$",Y,NW); label("$Z$",Z,NE); [/asy]

$\text{(A)}\ 1 \qquad \text{(B)}\ 2 \qquad \text{(C)}\ 3 \qquad \text{(D)}\ 4 \qquad \text{(E)}\ 20$

## Solution 1 (Complementary Counting)
There are $6$ points in the figure, and $3$ of them are needed to form a triangle, so there are ${6\choose{3}} =20$ possible triplets of the $6$ points. However, some of these created congruent triangles, and some don't even make triangles at all.
Case 1: Triangles congruent to There is obviously only $1$ of these: $\triangle RST$ itself.
Case 2: Triangles congruent to There are $4$ of these: $\triangle SYZ, \triangle RXY, \triangle TXZ,$ and $\triangle XYZ$ .
Case 3: Triangles congruent to There are $6$ of these: $\triangle RSX, \triangle TSX, \triangle STY, \triangle RTY, \triangle RSZ,$ and $\triangle RTZ$ .
Case 4: Triangles congruent to There are again $6$ of these: $\triangle SYX, \triangle SZX, \triangle TYZ, \triangle TYX, \triangle RXZ,$ and $\triangle RYZ$ .
However, if we add these up, we accounted for only $1+4+6+6=17$ of the $20$ possible triplets. We see that the remaining triplets don't even form triangles; they are $SYR, RXT,$ and $TZS$ . Adding these $3$ into the total yields for all of the possible triplets, so we see that there are only $4$ possible non-congruent, non-degenerate triangles, $\boxed{(D)}$

## Solution 2 (Brute Force)
We can do casework in this problem like the solution above, but that would take too much time. Instead, we see that we can split this equilateral dot triangle to two halves by dropping an altitude from the top vertex of the big triangle. Using the smaller triangle we won't have to worry about extra unneeded cases. We can see that there are three distinct triangles in the half, and combining this with the larger equilateral triangle our answer is $3+1 = \boxed{4}$ , which is $\boxed{\text{D}}$
-FIREDRAGONMATH16

## Solution 3 (Elimination)
Notice that 20 is obviously too high (There are only 20 ways to choose 3 of the points to form a triangle or a line in total!) and you can count 4 distinct triangles quickly: $\triangle RYX$ , $\triangle RYT$ , $\triangle RYZ$ , $\triangle RST$ . So the answer is $\boxed{\text{(D) } 4}$

## Solution 4 (Some symmetry)
Note that there is only one triangle $\triangle XYZ$ that does not use any vertex from the largest triangle $\triangle RST$ but $\triangle XYZ$ is congruent to $\triangle SYZ$ . Therefore we can always count non-congruent triangles that has at least one vertex from $\triangle RST$ , and by symmetry, we assume $S$ is always used. And by symmetry, we only count the triangles whose "left" edge from $S$ is no shorter than the "right". Easily we get all four ones: $\triangle SYZ$ , $\triangle SRX$ , $\triangle SRT$ , $\triangle SXZ$ .
--Sean Y

## Solution 5 (FREESTYLE!)
Simply count all possible such triangles, while keeping in mind that the maximum length of any such triangle is 2 units:
(2,1,1) lengths
(2,1,2) lengths
(2,2,2) lengths
(1,1,1) lengths
To avoid stuff being congruent, we know that there are 4 different such triangles. So, our answer is $\boxed{4}$ .
- cheltstudent B)
### See Also