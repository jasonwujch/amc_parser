# 2020 AIME II Problem 2

## Problem

Let $P$ be a point chosen uniformly at random in the interior of the unit square with vertices at $(0,0), (1,0), (1,1)$ , and $(0,1)$ . The probability that the slope of the line determined by $P$ and the point $\left(\frac58, \frac38 \right)$ is greater than or equal to $\frac12$ can be written as $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
The areas bounded by the unit square and alternately bounded by the lines through $\left(\frac{5}{8},\frac{3}{8}\right)$ that are vertical or have a slope of $1/2$ show where $P$ can be placed to satisfy the condition. One of the areas is a trapezoid with bases $1/16$ and $3/8$ and height $5/8$ . The other area is a trapezoid with bases $7/16$ and $5/8$ and height $3/8$ . Then, \[\frac{\frac{1}{16}+\frac{3}{8}}{2}\cdot\frac{5}{8}+\frac{\frac{7}{16}+\frac{5}{8}}{2}\cdot\frac{3}{8}=\frac{86}{256}=\frac{43}{128}\implies43+128=\boxed{171}\] ~mn28407

## Solution 2 (Official MAA)
The line through the fixed point $\left(\frac58,\frac38\right)$ with slope $\frac12$ has equation $y=\frac12 x + \frac1{16}$ . The slope between $P$ and the fixed point exceeds $\frac12$ if $P$ falls within the shaded region in the diagram below consisting of two trapezoids with area \[\frac{\frac1{16}+\frac38}2\cdot\frac58 + \frac{\frac58+\frac7{16}}2\cdot\frac38 = \frac{43}{128}.\] Because the entire square has area $1,$ the required probability is $\frac{43}{128}$ . The requested sum is $43+128 = 171$ . [asy] defaultpen(fontsize(8pt)); unitsize(4cm); pair A = (0,0); pair B = (1,0); pair C = (1,1); pair D = (0,1); pair F = (0, 1/16); pair G = (1, 9/16); pair H = (5/8, 0); pair J = (5/8, 1); pair K = IP(H--J, F--G); pair P = (13/16, 12/16); pair Q = extension(P,K,A,B); pair R = extension(K,P,C,D); draw(A--B--C--D--cycle); label("$(0,0)$", A, SW); label("$(1,0)$", B, SE); label("$(1,1)$", C, E); label("$(0,1)$", D, W); filldraw(A--H--K--F--cycle, lightgray); filldraw(K--G--C--J--cycle, lightgray); dot(K); dot("$P$", P, W); draw(Q -- R, dashed); label("$\frac 38$", H--K, E); label("$\frac 58$", K--J, W); label("$\frac 7{16}$", G--C, E); label("$\frac 38$", C--J, N); label("$\frac 1{16}$", A--F, dir(160)); [/asy]

## Video Solution
https://youtu.be/x0QznvXcwHY?t=190
~IceMatrix

## Video Solution 2
https://youtu.be/VBwlVbM0GRw
~avn
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .