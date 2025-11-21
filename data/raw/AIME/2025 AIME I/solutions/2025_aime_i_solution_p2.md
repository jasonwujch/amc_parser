# 2025 AIME I Problem 2

## Problem

On $\triangle ABC$ points $A$ , $D$ , $E$ , and $B$ lie in that order on side $\overline{AB}$ with $AD = 4$ , $DE = 16$ , and $EB = 8$ . Points $A$ , $F$ , $G$ , and $C$ lie in that order on side $\overline{AC}$ with $AF = 13$ , $FG = 52$ , and $GC = 26$ . Let $M$ be the reflection of $D$ through $F$ , and let $N$ be the reflection of $G$ through $E$ . Quadrilateral $DEGF$ has area $288$ . Find the area of heptagon $AFNBCEM$ .

[asy] unitsize(14); pair A = (0, 9), B = (-6, 0), C = (12, 0), D = (5A + 2B)/7, E = (2A + 5B)/7, F = (5A + 2C)/7, G = (2A + 5C)/7, M = 2F - D, N = 2E - G; filldraw(A--F--N--B--C--E--M--cycle, lightgray); draw(A--B--C--cycle); draw(D--M); draw(N--G); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(G); dot(M); dot(N); label("$A$", A, dir(90)); label("$B$", B, dir(225)); label("$C$", C, dir(315)); label("$D$", D, dir(135)); label("$E$", E, dir(135)); label("$F$", F, dir(45)); label("$G$", G, dir(45)); label("$M$", M, dir(45)); label("$N$", N, dir(135)); [/asy]

## Video solution by grogg007
https://youtu.be/PNBxBvvjbcU?t=80

## Solution 1
Note that the triangles outside $\triangle ABC$ have the same height as the unshaded triangles in $\triangle ABC$ . Since they have the same bases, the area of the heptagon is the same as the area of triangle $ABC$ . Therefore, we need to calculate the area of $\triangle ABC$ . Denote the length of $DF$ as $x$ and the altitude of $A$ to $DF$ as $h$ . Since $\triangle ADF \sim \triangle AEG$ , $EG = 5x$ and the altitude of $DFGE$ is $4h$ . The area $[DFGE] = \frac{5x + x}{2} \cdot 4h = 3x \cdot 4h = 12xh = 288 \implies xh = 24$ . The area of $\triangle ABC$ is equal to $\frac{1}{2} 7x \cdot 7h = \frac{1}{2} 49xh = \frac{1}{2} 49 \cdot 24 = \frac{1}{2} 1176 = \boxed{588}$ .
~alwaysgonnagiveyouup

## Solution 2
Because of reflections, and various triangles having the same bases, we can conclude that $|AFNBCEM| = |ABC|$ . Through the given lengths of $4-16-8$ on the left and $13-52-26$ on the right, we conclude that the lines through $\triangle ABC$ are parallel, and the sides are in a $1:4:2$ ratio. Because these lines are parallel, we can see that $ADF,~AEG,~ABC$ , are similar, and from our earlier ratio, we can give the triangles side ratios of $1:5:7$ , or area ratios of $1:25:49$ . Quadrilateral $DEGF$ corresponds to the $|AEG|-|ADF|$ , which corresponds to the ratio $25-1=24$ . Dividing $288$ by $24$ , we get $12$ , and finally multiplying $12 \cdot 49$ gives us our answer of $\boxed{588}$
~shreyan.chethan, cleaned up by cweu001

## Solution 3
By area lemma, we can see that the areas of the shaded areas are equivalent to the areas of the unshaded areas. Thus, we see that the desired area is equivalent to the area of the triangle $\triangle ABC$ . Since $AF : FG : GC = 1 : 4 : 2$ , we have $[ADF]:[AEG]:[ABC] = 1:25:49$ , meaning $[ADF]:[DEGF]:[BEGC] = 1:24:24$ . Thus, since $\frac{[DEGF]}{ABC} = \frac{24}{49}$ , we can calculate $[ABC] = 588$ .
~cweu001, cleaned up by shreyan.chethan

## Solution 4 (Vectors)
Let \( \triangle ABC \) be given with points \( D, E \) on segment \( AB \) such that \( A, D, E, B \) lie in that order, and \( AD = 4 \), \( DE = 16 \), and \( EB = 8 \). Similarly, points \( F, G \) lie on segment \( AC \) such that \( A, F, G, C \) lie in that order with \( AF = 13 \), \( FG = 52 \), and \( GC = 26 \).
Note that the segment \( AB \) is partitioned into three parts with lengths \( 4:16:8 \), which simplifies to the ratio \( 1:4:2 \). Similarly, segment \( AC \) is partitioned into parts \( 13:52:26 \), also reducing to the ratio \( 1:4:2 \). This implies that the points \( D, E \) divide \( AB \) and points \( F, G \) divide \( AC \) in the same proportions.
Because the divisions correspond proportionally on \( AB \) and \( AC \), the line segments \( DE \) and \( FG \) are parallel to \( BC \). In particular, triangles \( ADF \), \( AEG \), and \( ABC \) are similar by the Angle-Angle similarity criterion.
Let us introduce vector notation for convenience. Represent points \( A, B, C \) by vectors \( \vec{A}, \vec{B}, \vec{C} \) respectively. Then the points on \( AB \) satisfy:
\( \vec{D} = \vec{A} + \frac{1}{7} (\vec{B} - \vec{A}) \), \( \vec{E} = \vec{A} + \frac{5}{7} (\vec{B} - \vec{A}) \), \( D = A + \frac{1}{7} (B - A) \), \( E = A + \frac{5}{7} (B - A) \),
and the points on \( AC \) satisfy:
\( \vec{F} = \vec{A} + \frac{1}{7} (\vec{C} - \vec{A}) \), \( \vec{G} = \vec{A} + \frac{5}{7} (\vec{C} - \vec{A}) \). \( F = A + \frac{1}{7} (C - A) \), \( G = A + \frac{5}{7} (C - A) \).
The point \( M \) is the reflection of \( D \) about \( F \), so
\( \vec{M} = 2\vec{F} - \vec{D} \), \( M = 2F - D \),
and \( N \) is the reflection of \( G \) about \( E \), so
\( \vec{N} = 2\vec{E} - \vec{G} \). \( N = 2E - G \).
The polygon \( AFNBCEM \) has vertices at \( \vec{A}, \vec{F}, \vec{N}, \vec{B}, \vec{C}, \vec{E}, \vec{M} \).
Because \( M \) and \( N \) are reflections of points \( D \) and \( G \) about points \( F \) and \( E \) respectively, the triangles \( \triangle DFM \) and \( \triangle EGN \) are congruent to \( \triangle ADF \) and \( \triangle AEG \) respectively. Thus, the area of polygon \( AFNBCEM \) can be decomposed as
\[[heptagon] = [ \triangle ABC ] + [ \triangle DFM ] + [ \triangle EGN ] = [ \triangle ABC ] + [ \triangle ADF ] + [ \triangle AEG ].\]
Since \( \triangle ADF \), \( \triangle AEG \), and \( \triangle ABC \) are similar with similarity ratios in lengths of \( 1:5:7 \), their areas are in the ratio
\[[ADF] : [AEG] : [ABC] = 1^2 : 5^2 : 7^2 = 1:25:49.\]
Given the quadrilateral \( DEGF \) is the region between \( \triangle AEG \) and \( \triangle ADF \), its area is
\[[DEGF] = [AEG] - [ADF] = 25k - k = 24k,\]
where \( k = [ADF] \).
From the problem, \( [DEGF] = 288 \), so
\[24k = 288 \implies k = 12.\]
Hence,
\[[ABC] = 49k = 49 \times 12 = 588.\]
Since the heptagon's area is \( [ABC] + [ADF] + [AEG] = [ABC] + k + 25k = [ABC] + 26k \), but recalling that \( \triangle DFM \) and \( \triangle EGN \) are precisely the reflected copies of \( \triangle ADF \) and \( \triangle AEG \) that replace these smaller triangles inside \( ABC \), the total area of the heptagon \( AFNBCEM \) is exactly the area of \( \triangle ABC \): \(\boxed{588}\).
~Pinotation

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=J-0BapU4Yuk

## Video Solution(Fast! Easy!)
https://youtu.be/LQyncubz30U
~MC

## Video Solution by Mathletes Corner
https://www.youtube.com/watch?v=fVBk2vOusio&t=3s
~GP102

## Video Solution by yjtest
https://www.youtube.com/watch?v=avaHHEOQEZs
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .