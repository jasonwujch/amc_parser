# 1999 AMC 8 Problem 4

## Problem

The diagram shows the miles traveled by bikers Alberto and Bjorn. After four hours, about how many more miles has Alberto biked than Bjorn?

[asy] for (int a = 0; a < 6; ++a) { for (int b = 0; b < 6; ++b) { dot((4*a,3*b)); } } draw((0,0)--(20,0)--(20,15)--(0,15)--cycle); draw((0,0)--(16,12)); draw((0,0)--(16,9)); label(rotate(30)*"Bjorn",(12,6.75),SE); label(rotate(37)*"Alberto",(11,8.25),NW); label("$0$",(0,0),S); label("$1$",(4,0),S); label("$2$",(8,0),S); label("$3$",(12,0),S); label("$4$",(16,0),S); label("$5$",(20,0),S); label("$0$",(0,0),W); label("$15$",(0,3),W); label("$30$",(0,6),W); label("$45$",(0,9),W); label("$60$",(0,12),W); label("$75$",(0,15),W); label("H",(6,-2),S); label("O",(8,-2),S); label("U",(10,-2),S); label("R",(12,-2),S); label("S",(14,-2),S); label("M",(-4,11),N); label("I",(-4,9),N); label("L",(-4,7),N); label("E",(-4,5),N); label("S",(-4,3),N); [/asy]

$\text{(A)}\ 15 \qquad \text{(B)}\ 20 \qquad \text{(C)}\ 25 \qquad \text{(D)}\ 30 \qquad \text{(E)}\ 35$

## Solution
After 4 hours, we see that Bjorn biked 45 miles, and Alberto biked 60. Thus the answer is $60-45=15$ $\boxed{\text{(A)}}$ .

## Solution 2
We see that each dot is $15$ units away from the nearest one above it. So the answer is $\boxed{\text{A}}$ .
### Video(By YippieMath)
https://www.youtube.com/watch?v=OOgTEjyBk0s
### See Also