# 2003 AIME II Problem 6

## Problem

In triangle $ABC,$ $AB = 13,$ $BC = 14,$ $AC = 15,$ and point $G$ is the intersection of the medians. Points $A',$ $B',$ and $C',$ are the images of $A,$ $B,$ and $C,$ respectively, after a $180^\circ$ rotation about $G.$ What is the area of the union of the two regions enclosed by the triangles $ABC$ and $A'B'C'?$

## Solution
Since a $13-14-15$ triangle is a $5-12-13$ triangle and a $9-12-15$ triangle "glued" together on the $12$ side, $[ABC]=\frac{1}{2}\cdot12\cdot14=84$ .
There are six points of intersection between $\Delta ABC$ and $\Delta A'B'C'$ . Connect each of these points to $G$ .
[asy] size(8cm); pair A,B,C,G,D,E,F,A_1,A_2,B_1,B_2,C_1,C_2; B=(0,0); A=(5,12); C=(14,0); E=(12.6667,8); D=(7.6667,-4); F=(-1.3333,8); G=(6.3333,4); B_1=(4.6667,0); B_2=(1.6667,4); A_1=(3.3333,8); A_2=(8,8); C_1=(11,4); C_2=(9.3333,0); dot(A); dot(B); dot(C); dot(G); dot(D); dot(E); dot(F); dot(A_1); dot(B_1); dot(C_1); dot(A_2); dot(B_2); dot(C_2); draw(B--A--C--cycle); draw(E--D--F--cycle); draw(B_1--A_2); draw(A_1--C_2); draw(C_1--B_2); label("$B$",B,WSW); label("$A$",A,N); label("$C$",C,ESE); label("$G$",G,S); label("$B'$",E,ENE); label("$A'$",D,S); label("$C'$",F,WNW); [/asy]
There are $12$ smaller congruent triangles which make up the desired area. Also, $\Delta ABC$ is made up of $9$ of such triangles. Therefore, $\left[\Delta ABC \bigcup \Delta A'B'C'\right] = \frac{12}{9}[\Delta ABC]= \frac{4}{3}\cdot84=\boxed{112}$ .

## Solution 2(Doesn’t require good diagram)
First, find the area of $\Delta ABC$ either like the first solution or by using Heron’s Formula. Then, draw the medians from $G$ to each of $A, B, C, A’, B’,$ and $C’$ . Since the medians of a triangle divide the triangle into 6 triangles with equal area, we can find that each of the 6 outer triangles have equal area. (Proof: Since I’m too lazy to draw out a diagram, I’ll just have you borrow the one above. Draw medians $GA$ and $GB’$ , and let’s call the points that $GA$ intersects $C’B’$ “ $H$ ” and the point $GB’$ intersects $AC$ “ $I$ ”. From the previous property and the fact that both $\Delta ABC$ and $\Delta A’B’C’$ are congruent, $\Delta GHB’$ has the same area as $\Delta GIA$ . Because of that, both “half” triangles created also have the same area. The same logic can be applied to all other triangles). Also, since the centroid of a triangle divides each median with the ratio $2:1$ , along with the previous fact, each outer triangle has $1/9$ the area of $\Delta ABC$ and $\Delta A’B’C’$ . Thus, the area of the region required is $\frac{4}{3}$ times the area of $\Delta ABC$ which is $\boxed {112}$ .
Solution by Someonenumber011

## Solution 3 (Rigorous)
$[ABC]$ can be calculated as 84 using Heron's formula or other methods. Since a $180^{\circ}$ rotation is equivalent to reflection through a point, we have a homothety with scale factor $-1$ from $ABC$ to $A'B'C'$ through the centroid $G$ . Let $M$ be the midpoint of $BC$ which maps to $M'$ and note that $A'G=AG=2GM,$ implying that $GM=MA'.$ Similarly, we have $AM'=M'G=GM=MA'.$ Also let $D$ and $E$ be the intersections of $BC$ with $A'B'$ and $A'C',$ respectively. The homothety implies that we must have $DE || B'C',$ so there is in fact another homothety centered at $A'$ taking $A'DE$ to $A'B'C'$ . Since $A'M'=3A'M,$ the scale factor of this homothety is 3 and thus $[A'DE]=\frac{1}{9}[A'B'C']=\frac{1}{9}[ABC].$ We can apply similar reasoning to the other small triangles in $A'B'C'$ not contained within $ABC$ , so our final answer is $[ABC]+3\cdot\frac{1}{9}[ABC]=\boxed{112.}$

## Video Solution by Sal Khan
https://www.youtube.com/watch?v=l9j26EOvTYc&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=17 - AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.