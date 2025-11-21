# 2020 AMC 8 Problem 4

## Problem

Three hexagons of increasing size are shown below. Suppose the dot pattern continues so that each successive hexagon contains one more band of dots. How many dots are in the next hexagon?

[asy] // diagram by SirCalcsALot, edited by MRENTHUSIASM size(250); path p = scale(0.8)*unitcircle; pair[] A; pen grey1 = rgb(100/256, 100/256, 100/256); pen grey2 = rgb(183/256, 183/256, 183/256); for (int i=0; i<7; ++i) { A[i] = rotate(60*i)*(1,0);} path hex = A[0]--A[1]--A[2]--A[3]--A[4]--A[5]--cycle; fill(p,grey1); draw(scale(1.25)*hex,black+linewidth(1.25)); pair S = 6A[0]+2A[1]; fill(shift(S)*p,grey1); for (int i=0; i<6; ++i) { fill(shift(S+2*A[i])*p,grey2);} draw(shift(S)*scale(3.25)*hex,black+linewidth(1.25)); pair T = 16A[0]+4A[1]; fill(shift(T)*p,grey1); for (int i=0; i<6; ++i) { fill(shift(T+2*A[i])*p,grey2); fill(shift(T+4*A[i])*p,grey1); fill(shift(T+2*A[i]+2*A[i+1])*p,grey1); } draw(shift(T)*scale(5.25)*hex,black+linewidth(1.25)); [/asy]

$\textbf{(A) }35 \qquad \textbf{(B) }37 \qquad \textbf{(C) }39 \qquad \textbf{(D) }43 \qquad \textbf{(E) }49$

## Solution 1 (Pattern of the Rows)
Looking at the rows of each hexagon, we see that the first hexagon has $1$ dot, the second has $2+3+2$ dots, and the third has $3+4+5+4+3$ dots. Given the way the hexagons are constructed, it is clear that this pattern continues. Hence, the fourth hexagon has $4+5+6+7+6+5+4=\boxed{\textbf{(B) }37}$ dots.

## Solution 2 (Pattern of the Bands)
The dots in the next hexagon have four bands. From innermost to outermost:
Together, the answer is $1+6+12+18=\boxed{\textbf{(B) }37}.$
~MRENTHUSIASM

## Solution 3 (Pattern of the Bands)
The first hexagon has $1$ dot, the second hexagon has $1+6$ dots, the third hexagon has $1+6+12$ dots, and so on. The pattern continues since to go from hexagon $n$ to hexagon $(n+1),$ we add a new band of dots around the outside of the existing ones, with each side of the band having side length $(n+1).$ Thus, the number of dots added is $6(n+1)-6 = 6n$ (we subtract $6$ as each of the corner hexagons in the band is counted as part of two sides.). We therefore predict that the fourth hexagon has $1+6+12+18=\boxed{\textbf{(B) }37}$ dots.
Remark
For positive integers $n,$ let $h_n$ denote the number of dots in the $n$ th hexagon. We have $h_1=1$ and $h_{n+1}=h_n+6n.$
It follows that $h_2=7,h_3=19,$ and $h_4=37.$

## Solution 4 (Brute Force)
From the full diagram below, the answer is $\boxed{\textbf{(B) }37}.$ [asy] // diagram by SirCalcsALot, edited by MRENTHUSIASM size(400); path p = scale(0.8)*unitcircle; pair[] A; pen grey1 = rgb(100/256, 100/256, 100/256); pen grey2 = rgb(183/256, 183/256, 183/256); for (int i=0; i<7; ++i) { A[i] = rotate(60*i)*(1,0);} path hex = A[0]--A[1]--A[2]--A[3]--A[4]--A[5]--cycle; fill(p,grey1); draw(scale(1.25)*hex,black+linewidth(1.25)); pair S = 6A[0]+2A[1]; fill(shift(S)*p,grey1); for (int i=0; i<6; ++i) { fill(shift(S+2*A[i])*p,grey2);} draw(shift(S)*scale(3.25)*hex,black+linewidth(1.25)); pair T = 16A[0]+4A[1]; fill(shift(T)*p,grey1); for (int i=0; i<6; ++i) { fill(shift(T+2*A[i])*p,grey2); fill(shift(T+4*A[i])*p,grey1); fill(shift(T+2*A[i]+2*A[i+1])*p,grey1); } draw(shift(T)*scale(5.25)*hex,black+linewidth(1.25)); pair R = 30A[0]+6A[1]; fill(shift(R)*p,grey1); for (int i=0; i<6; ++i) { fill(shift(R+2*A[i])*p,grey2); fill(shift(R+4*A[i])*p,grey1); fill(shift(R+2*A[i]+2*A[i+1])*p,grey1); fill(shift(R+6*A[i+1])*p,grey2); fill(shift(R+2*A[i]+4*A[i+1])*p,grey2); fill(shift(R+4*A[i]+2*A[i+1])*p,grey2); } draw(shift(R)*scale(7.25)*hex,black+linewidth(1.25)); [/asy] ~MRENTHUSIASM

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=8hgK6rESdek&t=9s
~NiuniuMaths

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=bKY7jHWZFGeYKoM6&t=324
~Math-X

## Video Solution (🚀Under 2 min🚀)
https://youtu.be/V5EaJihwEMQ
~Education, the Study of Everything

## Video Solution by WhyMath
https://youtu.be/szWgrOPNw8c
~savannahsolver

## Video Solution by The Learning Royal
https://youtu.be/eSxzI8P9_h8
~The Learning Royal

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=123
~Interstigation

## Video Solution by North America Math Contest Go Go Go
https://www.youtube.com/watch?v=_IjQnXnVKeU
~North America Math Contest Go Go Go

## Video Solution by STEMbreezy
https://youtu.be/L_vDc-i585o?list=PLFcinOE4FNL0TkI-_yKVEYyA_QCS9mBNS&t=141
~STEMbreezy