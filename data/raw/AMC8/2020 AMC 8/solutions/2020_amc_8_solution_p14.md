# 2020 AMC 8 Problem 14

## Problem

There are $20$ cities in the County of Newton. Their populations are shown in the bar chart below. The average population of all the cities is indicated by the horizontal dashed line. Which of the following is closest to the total population of all $20$ cities?

[asy] // made by SirCalcsALot size(300); pen shortdashed=linetype(new real[] {6,6}); for (int i = 2000; i < 9000; i = i + 2000) { draw((0,i)--(11550,i), linewidth(0.5)+1.5*grey); label(string(i), (0,i), W); } for (int i = 500; i < 9300; i=i+500) { draw((0,i)--(150,i),linewidth(1.25)); if (i % 2000 == 0) { draw((0,i)--(250,i),linewidth(1.25)); } } int[] data = {8750, 3800, 5000, 2900, 6400, 7500, 4100, 1400, 2600, 1470, 2600, 7100, 4070, 7500, 7000, 8100, 1900, 1600, 5850, 5750}; int data_length = 20; int r = 550; for (int i = 0; i < data_length; ++i) { fill(((i+1)*r,0)--((i+1)*r, data[i])--((i+1)*r,0)--((i+1)*r, data[i])--((i+1)*r,0)--((i+1)*r, data[i])--((i+2)*r-100, data[i])--((i+2)*r-100,0)--cycle, 1.5*grey); draw(((i+1)*r,0)--((i+1)*r, data[i])--((i+1)*r,0)--((i+1)*r, data[i])--((i+1)*r,0)--((i+1)*r, data[i])--((i+2)*r-100, data[i])--((i+2)*r-100,0)); } draw((0,4750)--(11450,4750),shortdashed); label("Cities", (11450*0.5,0), S); label(rotate(90)*"Population", (0,9000*0.5), 10*W); // axis draw((0,0)--(0,9300), linewidth(1.25)); draw((0,0)--(11550,0), linewidth(1.25)); [/asy]

$\textbf{(A) }65{,}000 \qquad \textbf{(B) }75{,}000 \qquad \textbf{(C) }85{,}000 \qquad \textbf{(D) }95{,}000 \qquad \textbf{(E) }105{,}000$

## Solution
We can see that the dotted line is exactly halfway between $4{,}500$ and $5{,}000$ , so it is at $4{,}750$ . As this is the average population of all $20$ cities, the total population is simply $4{,}750 \cdot 20 = \boxed{\textbf{(D) }95{,}000}$ .

## Solution 2
The dotted line is slightly below $5000$ . Since $5000\cdot20=100000$ , the answer is slightly below this, so $\boxed{\textbf{(D) }95{,}000}$ would be the best choice to guess.

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=bHNrBwwUCMI
~NiuniuMaths

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=gX3KbBHBdLQ4DJBT&t=2139
~Math-X

## Video Solution (🚀ok Very Fast🚀)
https://youtu.be/2FYz_ze566I
~Education, the Study of Everything

## Video Solution by North America Math Contest Go Go Go
https://www.youtube.com/watch?v=IqoLKBx20dQ
~North America Math Contest Go Go Go

## Video Solution by WhyMath
https://youtu.be/5y4uDwZEF0M
~savannahsolver

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=608
~Interstigation