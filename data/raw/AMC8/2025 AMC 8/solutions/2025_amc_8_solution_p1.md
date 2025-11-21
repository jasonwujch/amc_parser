# 2025 AMC 8 Problem 1

## Problem

The eight-pointed star, shown in the figure below, is a popular quilting pattern. What percent of the entire $4\times4$ grid is covered by the star?

[asy] path x = (0,1)--(1,2)--(2,2)--(1,1)--cycle; path y = reflect((0,0),(4,4)) * x; path z = (1,0)--(2,1)--(3,0)--(3,1)--(2,2)--(1,1); fill(x, gray(0.6)); fill(rotate(90, (2,2)) * x, gray(0.6)); fill(rotate(180, (2,2)) * x, gray(0.6)); fill(rotate(270, (2,2)) * x, gray(0.6)); fill(y, gray(0.8)); fill(rotate(90, (2,2)) * y, gray(0.8)); fill(rotate(180, (2,2)) * y, gray(0.8)); fill(rotate(270, (2,2)) * y, gray(0.8)); draw(z); draw(rotate(90, (2,2)) * z); draw(rotate(180, (2,2)) * z); draw(rotate(270, (2,2)) * z); add(grid(4,4)); [/asy]

$\textbf{(A)}\ 40 \qquad \textbf{(B)}\ 50 \qquad \textbf{(C)}\ 60 \qquad \textbf{(D)}\ 75 \qquad \textbf{(E)}\ 80$

## Solution 1
Each of the unshaded triangles has base length $2$ and height $1$ , so they all have area $\frac{2 \cdot 1}{2} = 1$ . Each of the unshaded unit squares has area $1$ . The area of the shaded region is equal to the area of the entire grid minus the area of the unshaded region, or $4^2 - 4 \cdot 1 - 4 \cdot 1 = 8$ . The star is then $\frac{8}{16} = \frac{1}{2} = \frac{50}{100}$ , or $\boxed{\textbf{(B)}~50}$ percent of the entire grid. ~cxsmi

## Solution 2
There are $16$ total squares in the diagram and each square has $2$ triangles whose areas are half the area of a unit square. Thus, the total number of triangles in the diagram is $4^2 \cdot 2 = 32$ triangles. There are $16$ shaded triangles in the diagram, so the area of the star is $\dfrac{16}{32} = \frac{1}{2} = \frac{50}{100}$ , or $\boxed{\textbf{(B)}~50}$ percent. ~Pi_in_da_box

## Solution 3
There are $4$ squares that are entirely shaded and $4$ squares that have no shading. The rest of the squares are half-half. Therefore the shaded region is $\boxed{\textbf{(B)}~50}$ percent of the grid.

## Solution 4
Note that we can move one triangle from each of the four cells in the middle to each of the four corners. This will leave every cell in the grid with one triangle each, and each triangle has an area of half the area of each cell. Thus, our answer must equal to $\frac{1}{2}$ , and so our answer is $\boxed{\textbf{(B)}~50}.$ ~derekwang2048

## Solution 5
The shaded area is a $2 \times 2$ square in the middle of the figure combined with $8$ small triangles. Since each small triangle is $\frac{1}{2}$ of a unit square, the star's area is equal to the area of $4 + 8 \cdot \frac{1}{2} = 8$ unit squares, which $\boxed{\textbf{(B)}~50}$ percent of the grid.
-vockey

## Solution 6
Using Pick's Theorem , we see there are 16 boundary points and 1 interior point. $1 + \frac{16}{2} - 1 = 8$ . There are $4 \cdot 4 = 16$ squares, and 8 is $\boxed{\textbf{(B)}~50}$ percent of 16.
-leafy

## Video Solution 1
~ ChillGuyDoesMath

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI

## Video Solution 3
~hsnacademy

## Video Solution 4 by Daily Dose of Math
~Thesmartgreekmathdude

## Video Solution 5 by Thinking Feet
https://youtu.be/PKMpTS6b988

## Video Solution 6 by CoolMathProblems
https://youtu.be/SNviHnUR3x4

## Video Solution 7 by Pi Academy
https://youtu.be/Iv_a3Rz725w?si=E0SI_h1XT8msWgkK

## Video Solution 8
https://youtu.be/Yc4KSp0aOco

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC
### See Also