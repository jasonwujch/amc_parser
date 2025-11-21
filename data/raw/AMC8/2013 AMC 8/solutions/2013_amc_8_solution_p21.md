# 2013 AMC 8 Problem 21

## Problem

Samantha lives 2 blocks west and 1 block south of the southwest corner of City Park. Her school is 2 blocks east and 2 blocks north of the northeast corner of City Park. On school days she bikes on streets to the southwest corner of City Park, then takes a diagonal path through the park to the northeast corner, and then bikes on streets to school. If her route is as short as possible, how many different routes can she take?

$\textbf{(A)}\ 3 \qquad \textbf{(B)}\ 6 \qquad \textbf{(C)}\ 9 \qquad \textbf{(D)}\ 12 \qquad \textbf{(E)}\ 18$

## Video Solution
https://youtu.be/9nveueuZiqs ~savannahsolver

## Solution
[asy] unitsize(8mm); for(int i=0; i<=8; ++i) { draw((0,i)--(8,i)); draw((i,0)--(i,8)); } fill((2,1)--(6,1)--(6,6)--(2,6)--cycle); for(int j=0; j<= 38; ++j) { draw((0,0)--(2,0)--(2,1)--(0,1)--(0,0), black+linewidth(3)); draw((6,6)--(6,8)--(8,8)--(8,6)--(6,6), black+linewidth(3)); }[/asy]
Using combinations , we get that the number of ways to get from Samantha's house to City Park is $\binom31 = \dfrac{3!}{1!2!} = 3$ , and the number of ways to get from City Park to school is $\binom42= \dfrac{4!}{2!2!} = \dfrac{4\cdot 3}{2} = 6$ . Since there's one way to go through City Park (just walking straight through), the number of different ways to go from Samantha's house to City Park to school $3\cdot 6 = \boxed{\textbf{(E)}\ 18}$ .
~Note by Theraccoon: The person who posted this did not include their name.
### See Also