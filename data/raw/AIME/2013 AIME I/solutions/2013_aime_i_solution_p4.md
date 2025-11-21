# 2013 AIME I Problem 4

## Problem

In the array of 13 squares shown below, 8 squares are colored red, and the remaining 5 squares are colored blue. If one of all possible such colorings is chosen at random, the probability that the chosen colored array appears the same when rotated 90 degrees around the central square is $\frac{1}{n}$ , where n is a positive integer. Find n .

[asy] draw((0,0)--(1,0)--(1,1)--(0,1)--(0,0)); draw((2,0)--(2,2)--(3,2)--(3,0)--(3,1)--(2,1)--(4,1)--(4,0)--(2,0)); draw((1,2)--(1,4)--(0,4)--(0,2)--(0,3)--(1,3)--(-1,3)--(-1,2)--(1,2)); draw((-1,1)--(-3,1)--(-3,0)--(-1,0)--(-2,0)--(-2,1)--(-2,-1)--(-1,-1)--(-1,1)); draw((0,-1)--(0,-3)--(1,-3)--(1,-1)--(1,-2)--(0,-2)--(2,-2)--(2,-1)--(0,-1)); size(100);[/asy]

## Solution
When the array appears the same after a 90-degree rotation, the top formation must look the same as the right formation, which looks the same as the bottom one, which looks the same as the right one. There are four of the same configuration. There are not enough red squares for these to be all red, nor are there enough blue squares for there to be more than one blue square in each three-square formation. Thus there are 2 reds and 1 blue in each, and a blue in the center. There are 3 ways to choose which of the squares in the formation will be blue, leaving the other two red.
There are $\binom{13}{5}$ ways to have 5 blue squares in an array of 13.
$\frac{3}{\binom{13}{5}}$ = $\frac{1}{429}$ , so = $\boxed{429}$

## Solution 2
By the Pigeonhole Principle, if the middle square isn't blue, than any 90 degree rotation won't map onto itself because one extra blue square will be mapped onto a red square. Therefore, we have to have 1 blue square in the middle and 1 blue square in each of the 4 seperate containers(think if there is two in each a 90 degree rotation wouldn't move it to the other side). There are 3 places in each of the seperate tilings for it and everything else will be red. Therefore, there are only 3 good combinations. Now the total amount is 13choose5, so we lead to the answer: $\frac{3}{\binom{13}{5}}$ = $\frac{1}{429}$ , so = $\boxed{429}$
~MathCosine

## Solution 3
We use the same idea as the other solutions, knowing the middle square must be blue, which has probability $\frac{5}{13}$ , the next blue square can go anywhere; then the last three must go in the three spots they rotate in, giving us $\frac{3!}{11*10*9}$ . Multiplying yields $\boxed{429}$ .
~boppitybobii

## Video Solution
https://www.youtube.com/watch?v=9way8JrtD04&t=555s ~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .