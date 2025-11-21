# 2004 AMC 8 Problem 23

## Problem

Tess runs counterclockwise around rectangular block $JKLM$ . She lives at corner $J$ . Which graph could represent her straight-line distance from home?

[asy] unitsize(5mm); pair J=(-3,2); pair K=(-3,-2); pair L=(3,-2); pair M=(3,2); draw(J--K--L--M--cycle); label("$J$",J,NW); label("$K$",K,SW); label("$L$",L,SE); label("$M$",M,NE); [/asy]

$\textbf{(A)}$ [asy] size(80);defaultpen(linewidth(0.8)); //A draw((16,0)--origin--(0,16)); draw(origin--(15,15)); label("time", (8,0), S); label(rotate(90)*"distance", (0,8), W); [/asy]

$\textbf{(B)}$ [asy] size(80);defaultpen(linewidth(0.8)); //B draw((16,0)--origin--(0,16)); draw((0,6)--(1,6)--(1,12)--(2,12)--(2,11)--(3,11)--(3,1)--(12,1)--(12,0)); label("time", (8,0), S); label(rotate(90)*"distance", (0,8), W); [/asy]

$\textbf{(C)}$ [asy] size(80);defaultpen(linewidth(0.8)); //C draw((16,0)--origin--(0,16)); draw(origin--(2.7,8)--(3,9)^^(11,9)--(14,0)); draw(Arc((4,9), 1, 0, 180)); draw(Arc((10,9), 1, 0, 180)); draw(Arc((7,9), 2, 180,360)); label("time", (8,0), S); label(rotate(90)*"distance", (0,8), W); [/asy]

$\textbf{(D)}$ [asy] size(80);defaultpen(linewidth(0.8)); //D draw((16,0)--origin--(0,16)); draw(origin--(2,6)--(7,14)--(10,12)--(14,0)); label("time", (8,0), S); label(rotate(90)*"distance", (0,8), W); [/asy]

$\textbf{(E)}$ [asy] size(80);defaultpen(linewidth(0.8)); //E draw((16,0)--origin--(0,16)); draw(origin--(3,6)--(7,6)--(10,12)--(14,12)); label("time", (8,0), S); label(rotate(90)*"distance", (0,8), W); [/asy]

## Solution 1
For her distance to be represented as a constant horizontal line, Tess would have to be running in a circular shape with her home as the center. Since she is running around a rectangle, this is not possible, ruling out $B$ and $E$ with straight lines. Because $JL$ is the diagonal of the rectangle, and $L$ is at the middle distance around the perimeter, her maximum distance should be in the middle of her journey. The maximum in $A$ is at the end, and $C$ has two maximums, ruling both out. Thus the answer is $\boxed{\textbf{(D)}}$ .

## Solution 2
Even though Solution 1 may find an answer, it is never proven that $D$ actually describes the distance to Tess' home.
It may be easier to compare the distance traveled by Tess rather than the time spent, if we suppose that Tess moves at constant speed then the graphs distance-time and distance-position are equivalent.
Let $x$ be the linear distance walked by Tess, and $d$ her distance from home $J$ . We will divide this problem into four parts (sections $JK$ , $KL$ , $LM$ and $MJ$ ).
[asy] unitsize(5mm); pair J=(-3,2); pair K=(-3,-2); pair L=(3,-2); pair M=(3,2); draw(J--K--L--M--cycle); label("$J$",J,NW); label("$K$",K,SW); label("$L$",L,SE); label("$M$",M,NE); [/asy]
Section $JK$ : At any point of the segment $JK$ , the distance of Tess from home is described by the function $d_{JK}(x)=x_J$ where $x_J$ is the linear distance traveled by Tess from point $J$ .
Section $KL$ : From $K$ to $L$ , the distance from home is described by a right triangle, where $d$ is the hypotenuse. In this situation the distance follows the function $d_{KL}(x)=\sqrt{JK^2+x_K^2}$ , which is a curve (this was obtained by applying the Pythagorean Theorem).
Section $LM$ : Following an analogue reasoning to Section $KL$ , the distance function in this case results $d_{LM}(x)=\sqrt{MJ^2+(LM-x_L)^2}$ which is also a curve.
Section $MJ$ : Analogue to Section $JK$ , we obtain a linear function $d_{MJ}(x)=MJ-x_M$
None of the shown answers in the multiple choice describe the real distance between Tess and home along the path.
The real graph should have a shape of the following kind:
[asy] size(80);defaultpen(linewidth(0.8)); //D draw((16,0)--origin--(0,16)); draw(origin--(3.2,10.3)^^(10,12.2)--(14,0)); draw(Arc((26.7,1.9), 25, 145, 160)); draw(Arc((12,18), 6, 198, 250)); label("time", (8,0), S); label(rotate(90)*"distance", (0,8), W); [/asy]
Which is slightly different from the expected solution $D$ .
~ FaC7oR
### See Also