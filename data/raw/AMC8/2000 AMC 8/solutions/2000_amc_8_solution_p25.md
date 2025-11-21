# 2000 AMC 8 Problem 25

## Problem

The area of rectangle $ABCD$ is $72$ units squared. If point $A$ and the midpoints of $\overline{BC}$ and $\overline{CD}$ are joined to form a triangle, the area of that triangle is

[asy] pair A,B,C,D; A = (0,8); B = (9,8); C = (9,0); D = (0,0); draw(A--B--C--D--A--(9,4)--(4.5,0)--cycle); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW);[/asy]

$\text{(A)}\ 21\qquad\text{(B)}\ 27\qquad\text{(C)}\ 30\qquad\text{(D)}\ 36\qquad\text{(E)}\ 40$

## Solution 1
To quickly solve this multiple choice problem, make the (not necessarily valid, but very convenient) assumption that $ABCD$ can have any dimension. Give the rectangle dimensions of $AB = CD = 12$ and $BC = AD= 6$ , which is the easiest way to avoid fractions. Labelling the right midpoint as $M$ , and the bottom midpoint as $N$ , we know that $DN = NC = 6$ , and $BM = MC = 3$ .
$[\triangle ADN] = \frac{1}{2}\cdot 6\cdot 6 = 18$
$[\triangle MNC] = \frac{1}{2}\cdot 3\cdot 6 = 9$
$[\triangle ABM] = \frac{1}{2}\cdot 12\cdot 3 = 18$
$[\triangle AMN] = [\square ABCD] - [\triangle ADN] - [\triangle MNC] - [\triangle ABM]$
$[\triangle AMN] = 72 - 18 - 9 - 18$
$[\triangle AMN] = 27$ , and the answer is $\boxed{B}$

## Solution 2
The above answer is fast, but satisfying, and assumes that the area of $\triangle AMN$ is independent of the dimensions of the rectangle. All in all, it's a very good answer though. However this is an alternative if you don't get the above answer. Label $AB = CD = l$ and $BC = DA = h$
Labelling $m$ and $n$ as the right and lower midpoints respectively, and redoing all the work above, we get:
$[\triangle ADN] = \frac{1}{2}\cdot h\cdot \frac{l}{2} = \frac{lh}{4}$
$[\triangle MNC] = \frac{1}{2}\cdot \frac{l}{2}\cdot \frac{h}{2} = \frac{lh}{8}$
$[\triangle ABM] = \frac{1}{2}\cdot l\cdot \frac{h}{2} = \frac{lh}{4}$
$[\triangle AMN] = [\square ABCD] - [\triangle ADN] - [\triangle MNC] - [\triangle ABM]$
$[\triangle AMN] = lh - \frac{lh}{4} - \frac{lh}{8} - \frac{lh}{4}$
$[\triangle AMN] = \frac{3}{8}lh = \frac{3}{8}\cdot 72 = 27$ , and the answer is $\boxed{B}$

## Solution 3
Let's assume WLOG that the sides of the rectangle are $9$ and $8.$ The area of the 3 triangles would then be $8\cdot\frac{9}{2}\cdot\frac{1}{2} = 18,$ $4\cdot\frac{9}{2}\cdot\frac{1}{2} = 9,$ $4\cdot 9\cdot\frac{1}{2} = 18.$ Adding these up, we get $45$ , and subtracting that from $72$ , we get $27$ , so the answer is $\boxed{B}$
~ilee0820

## Video Solution
https://youtu.be/yoIO9q_GTig . Soo, DRMS, NM
https://www.youtube.com/watch?v=XxQwfirFn4M ~David