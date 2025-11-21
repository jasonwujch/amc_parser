# 2007 AMC 8 Problem 16

## Problem

Amanda Reckonwith draws five circles with radii $1, 2, 3, 4$ and $5$ . Then for each circle she plots the point $(C,A)$ , where $C$ is its circumference and $A$ is its area. Which of the following could be her graph?

$\textbf{(A)}$ [asy] size(75); pair A= (1.5,2) , B= (3,4) , C= (4.5,7) , D= (6,11) , E= (7.5,16) ; draw((0,-1)--(0,16)); draw((-1,0)--(16,0)); dot(A^^B^^C^^D^^E); label("$A$", (0,8), W); label("$C$", (8,0), S);[/asy]

$\textbf{(B)}$ [asy] size(75); pair A= (1.5,9) , B= (3,6) , C= (4.5,6) , D= (6,9) , E= (7.5,15) ; draw((0,-1)--(0,16)); draw((-1,0)--(16,0)); dot(A^^B^^C^^D^^E); label("$A$", (0,8), W); label("$C$", (8,0), S);[/asy]

$\textbf{(C)}$ [asy] size(75); pair A= (1.5,2) , B= (3,6) , C= (4.5,8) , D= (6,6) , E= (7.5,2) ; draw((0,-1)--(0,16)); draw((-1,0)--(16,0)); dot(A^^B^^C^^D^^E); label("$A$", (0,8), W); label("$C$", (8,0), S);[/asy]

$\textbf{(D)}$ [asy] size(75); pair A= (1.5,2) , B= (3,5) , C= (4.5,8) , D= (6,11) , E= (7.5,14) ; draw((0,-1)--(0,16)); draw((-1,0)--(16,0)); dot(A^^B^^C^^D^^E); label("$A$", (0,8), W); label("$C$", (8,0), S);[/asy]

$\textbf{(E)}$ [asy] size(75); pair A= (1.5,15) , B= (3,10) , C= (4.5,6) , D= (6,3) , E= (7.5,1) ; draw((0,-1)--(0,16)); draw((-1,0)--(16,0)); dot(A^^B^^C^^D^^E); label("$A$", (0,8), W); label("$C$", (8,0), S);[/asy]

## Solution
The circumference of a circle is obtained by simply multiplying the radius by $2\pi$ . So, the C-coordinate (in this case, it is the x-coordinate) will increase at a steady rate. The area, however, is obtained by squaring the radius and multiplying it by $\pi$ . Since squares do not increase in an evenly spaced arithmetic sequence, the increase in the A-coordinates (aka the y- coordinates) will be much more significant. The answer is $\boxed{\textbf{(A)}},$ [asy] size(75); pair A= (1.5,2) , B= (3,4) , C= (4.5,7) , D= (6,11) , E= (7.5,16) ; draw((0,-1)--(0,16)); draw((-1,0)--(16,0)); dot(A^^B^^C^^D^^E); label("$A$", (0,8), W); label("$C$", (8,0), S);[/asy] . -RBANDA

## Video Solution by WhyMath
https://youtu.be/AW6BhCQ_ig8
~savannahsolver
### See Also