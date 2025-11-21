# 2019 AMC 8 Problem 6

## Problem

There are $81$ grid points (uniformly spaced) in the square shown in the diagram below, including the points on the edges. Point $P$ is in the center of the square. Given that point $Q$ is randomly chosen among the other $80$ points, what is the probability that the line $PQ$ is a line of symmetry for the square?

[asy] draw((0,0)--(0,8)); draw((0,8)--(8,8)); draw((8,8)--(8,0)); draw((8,0)--(0,0)); dot((0,0)); dot((0,1)); dot((0,2)); dot((0,3)); dot((0,4)); dot((0,5)); dot((0,6)); dot((0,7)); dot((0,8)); dot((1,0)); dot((1,1)); dot((1,2)); dot((1,3)); dot((1,4)); dot((1,5)); dot((1,6)); dot((1,7)); dot((1,8)); dot((2,0)); dot((2,1)); dot((2,2)); dot((2,3)); dot((2,4)); dot((2,5)); dot((2,6)); dot((2,7)); dot((2,8)); dot((3,0)); dot((3,1)); dot((3,2)); dot((3,3)); dot((3,4)); dot((3,5)); dot((3,6)); dot((3,7)); dot((3,8)); dot((4,0)); dot((4,1)); dot((4,2)); dot((4,3)); dot((4,4)); dot((4,5)); dot((4,6)); dot((4,7)); dot((4,8)); dot((5,0)); dot((5,1)); dot((5,2)); dot((5,3)); dot((5,4)); dot((5,5)); dot((5,6)); dot((5,7)); dot((5,8)); dot((6,0)); dot((6,1)); dot((6,2)); dot((6,3)); dot((6,4)); dot((6,5)); dot((6,6)); dot((6,7)); dot((6,8)); dot((7,0)); dot((7,1)); dot((7,2)); dot((7,3)); dot((7,4)); dot((7,5)); dot((7,6)); dot((7,7)); dot((7,8)); dot((8,0)); dot((8,1)); dot((8,2)); dot((8,3)); dot((8,4)); dot((8,5)); dot((8,6)); dot((8,7)); dot((8,8)); label("P",(4,4),NE); [/asy]

$\textbf{(A) }\frac{1}{5}\qquad\textbf{(B) }\frac{1}{4} \qquad\textbf{(C) }\frac{2}{5} \qquad\textbf{(D) }\frac{9}{20} \qquad\textbf{(E) }\frac{1}{2}$

## Solution 1
[asy] draw((0,0)--(0,8)); draw((0,8)--(8,8)); draw((8,8)--(8,0)); draw((8,0)--(0,0)); dot((0,0)); dot((0,1)); dot((0,2)); dot((0,3)); dot((0,4)); dot((0,5)); dot((0,6)); dot((0,7)); dot((0,8)); dot((1,0)); dot((1,1)); dot((1,2)); dot((1,3)); dot((1,4)); dot((1,5)); dot((1,6)); dot((1,7)); dot((1,8)); dot((2,0)); dot((2,1)); dot((2,2)); dot((2,3)); dot((2,4)); dot((2,5)); dot((2,6)); dot((2,7)); dot((2,8)); dot((3,0)); dot((3,1)); dot((3,2)); dot((3,3)); dot((3,4)); dot((3,5)); dot((3,6)); dot((3,7)); dot((3,8)); dot((4,0)); dot((4,1)); dot((4,2)); dot((4,3)); dot((4,4)); dot((4,5)); dot((4,6)); dot((4,7)); dot((4,8)); dot((5,0)); dot((5,1)); dot((5,2)); dot((5,3)); dot((5,4)); dot((5,5)); dot((5,6)); dot((5,7)); dot((5,8)); dot((6,0)); dot((6,1)); dot((6,2)); dot((6,3)); dot((6,4)); dot((6,5)); dot((6,6)); dot((6,7)); dot((6,8)); dot((7,0)); dot((7,1)); dot((7,2)); dot((7,3)); dot((7,4)); dot((7,5)); dot((7,6)); dot((7,7)); dot((7,8)); dot((8,0)); dot((8,1)); dot((8,2)); dot((8,3)); dot((8,4)); dot((8,5)); dot((8,6)); dot((8,7)); dot((8,8)); label("P",(4,4),NE); draw((0,4)--(3,4)); draw((0,8)--(3,5)); draw((8,8)--(5,5)); draw((4,8)--(4,5)); draw((4,0)--(4,3)); draw((0,0)--(3,3)); draw((8,0)--(5,3)); draw((5,4)--(8,4)); [/asy] Lines of symmetry go through point $P$ , and there are $8$ directions the lines could go, and there are $4$ dots at each direction. $\frac{4\times8}{80}=\boxed{\textbf{(C)} \frac{2}{5}}$ .

## Solution 2
Divide the grid into 4 4x5 quadrants. Each row of 5 points has 1 point on a horizontal/vertical line of symmetry + 1 point on a diagonal line of symmetry: $\boxed{\textbf{(C)} \frac{2}{5}}$ .

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/IgpayYB48C4?si=AdzSEy4Ocrte4gEU&t=1650
~Math-X

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/PizqK-oBLqk
~Education, the Study of Everything

## Video Solution
The Learning Royal : https://youtu.be/8njQzoztDGc

## Video Solution 2
Solution detailing how to solve the problem: https://www.youtube.com/watch?v=4L95z9DwlhI&list=PLbhMrFqoXXwmwbk2CWeYOYPRbGtmdPUhL&index=7

## Video Solution 3
https://youtu.be/TAKmC11vitM
~savannahsolver

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1