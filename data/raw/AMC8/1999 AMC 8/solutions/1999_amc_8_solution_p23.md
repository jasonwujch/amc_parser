# 1999 AMC 8 Problem 23

## Problem

Square $ABCD$ has sides of length 3. Segments $CM$ and $CN$ divide the square's area into three equal parts. How long is segment $CM$ ?

[asy] pair A,B,C,D,M,N; A = (0,0); B = (0,3); C = (3,3); D = (3,0); M = (0,1); N = (1,0); draw(A--B--C--D--cycle); draw(M--C--N); label("$A$",A,SW); label("$M$",M,W); label("$B$",B,NW); label("$C$",C,NE); label("$D$",D,SE); label("$N$",N,S); [/asy]

$\text{(A)}\ \sqrt{10} \qquad \text{(B)}\ \sqrt{12} \qquad \text{(C)}\ \sqrt{13} \qquad \text{(D)}\ \sqrt{14} \qquad \text{(E)}\ \sqrt{15}$

## Solution
Since the square has side length $3$ , the area of the entire square is $9$ .
The segments divide the square into 3 equal parts, so the area of each part is $9 \div 3 = 3$ .
Since $\triangle CBM$ has area $3$ and base $CB = 3$ , using the area formula for a triangle:
$A_{tri} = \frac{1}{2}bh$
$3 = \frac{1}{2}3h$
$h = 2$
Thus, height $BM = 2$ .
Since $\triangle CBM$ is a right triangle, $CM = \sqrt{BM^2 + BC^2} = \sqrt{2^2 + 3^2} = \boxed{\text{(C)}\ \sqrt{13}}$ .

## Solution 2
Connect $AC$ , $S_\triangle AMC=S_\triangle ANC$ . To satisfied the three area is equal, we have $2S_\triangle AMC=S_\triangle BMC$ , $2S_\triangle ANC=S_\triangle DNC$ . Thus, $AM=AN=\frac{1}{2}BM=\frac{1}{2}ND=1$ . $BM=2,BC=3,MC=\boxed{\text{(C)}\ \sqrt{13}}$ .

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=AH5_Gol2GCM
### See Also