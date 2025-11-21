# 2003 AMC 10A Problem 23

## Problem

A large equilateral triangle is constructed by using toothpicks to create rows of small equilateral triangles. For example, in the figure, we have $3$ rows of small congruent equilateral triangles, with $5$ small triangles in the base row. How many toothpicks would be needed to construct a large equilateral triangle if the base row of the triangle consists of $2003$ small equilateral triangles?

[asy] unitsize(15mm); defaultpen(linewidth(.8pt)+fontsize(8pt)); pair Ap=(0,0), Bp=(1,0), Cp=(2,0), Dp=(3,0), Gp=dir(60); pair Fp=shift(Gp)*Bp, Ep=shift(Gp)*Cp; pair Hp=shift(Gp)*Gp, Ip=shift(Gp)*Fp; pair Jp=shift(Gp)*Hp; pair[] points={Ap,Bp,Cp,Dp,Ep,Fp,Gp,Hp,Ip,Jp}; draw(Ap--Dp--Jp--cycle); draw(Gp--Bp--Ip--Hp--Cp--Ep--cycle); for(pair p : points) { fill(circle(p, 0.07),white); } pair[] Cn=new pair[5]; Cn[0]=centroid(Ap,Bp,Gp); Cn[1]=centroid(Gp,Bp,Fp); Cn[2]=centroid(Bp,Fp,Cp); Cn[3]=centroid(Cp,Fp,Ep); Cn[4]=centroid(Cp,Ep,Dp); label("$1$",Cn[0]); label("$2$",Cn[1]); label("$3$",Cn[2]); label("$4$",Cn[3]); label("$5$",Cn[4]); for (pair p : Cn) { draw(circle(p,0.1)); }[/asy]

$\mathrm{(A) \ } 1,004,004 \qquad \mathrm{(B) \ } 1,005,006 \qquad \mathrm{(C) \ } 1,507,509 \qquad \mathrm{(D) \ } 3,015,018 \qquad \mathrm{(E) \ } 6,021,018$

## Solution 1
There are $1+3+5+...+2003=1002^{2}=1004004$ small equilateral triangles.
Each small equilateral triangle needs $3$ toothpicks to make it.
But, each toothpick that isn't one of the $1002\cdot3=3006$ toothpicks on the outside of the large equilateral triangle is a side for $2$ small equilateral triangles.
So, the number of toothpicks on the inside of the large equilateral triangle is $\frac{10040004\cdot3-3006}{2}=1504503$ .
Therefore the total number of toothpicks is $1504503+3006=\boxed{\mathrm{(C)}\ 1,507,509}$ . ~dolphin7

## Solution 2
We just need to count upward facing triangles because if we exclude the downward-facing triangles, we won't be overcounting any toothpicks. The first row of triangles has $1$ upward-facing triangle, the second row has $2$ upward-facing triangles, the third row has $3$ upward-facing triangles, and so on having $n$ upward-facing triangles in the $n^\text{th}$ row. The last row with $2003$ small triangles has $1002$ upward-facing triangles. By Gauss's formula , the number of the upward-facing triangles in the entire triangle are now $\frac{1002\times1003}{2}$ , meaning that the number of toothpicks are $\frac{1002\times1003}{2}\times3$ , or $\boxed{\mathrm{(C)}\ 1,507,509}$ .
~mathpro12345
### Note
You don't have to calculate the value of $\frac{1002\times1003}{2}\times3$ , and you can use units digits to find the answer easily. The units digit of $1002\times1003$ is $6$ , and has a unit digit of $3$ after being divided by $2$ . Then this is multiplied by $3$ , now the final number ending with a $9$ . This leaves only one answer choice possible, which is $\boxed{\mathrm{(C)}\ 1,507,509}$ .

## Solution 3
Test out some smaller cases first.
When there is just $1$ equilateral triangle in the base, you need $3$ toothpicks. When there are $3$ equilateral triangles in the base, you need $9$ toothpicks in all. When there are $5$ equilateral triangles in the base, you need $18$ toothpicks in all. When there are $7$ equilateral triangles in the base, you need $30$ toothpicks in all.
Taking the finite differences, we get $6, 9, 12.$ It forms a linear sequence. This means the original numbers $(3, 9, 18, 30)$ form a quadratic.
Let the quadratic be $y = ax^2 + bx + c$ where $y = 2 \cdot \text{(number of equilateral triangles in base)} - 1.$
Then, we have the following points: $(1, 3), (2, 9), (3, 18), (4, 30).$
We can plug these values into $y = ax^2 + bx + c$ , giving:
\[a + b + c = 3, 4a + b + c = 9, 9a + 3b + c = 18.\]
Solving gives $a = b = 1.5, c = 0.$ So \[y = 1.5x^2 + 1.5x.\]
For our problem, we need $2003$ equilateral triangles in the base. For the quadratic, the corresponding $x$ -value would be $\frac{2003 + 1}{2} = 1002$ . So our answer is simply: \[1.5 \cdot 1002^2 + 1.5 \cdot 1002 = \boxed{\mathrm{(C)}\ 1,507,509}.\]

## Solution 4
We can count the slanted toothpicks and the horizontal toothpicks separately. Since the bottom row has $2003$ triangles, there will be toothpicks between the triangles and on the edges, which makes $2004$ toothpicks on the bottom row. The row above it will have $2$ fewer triangles, so it will have $2$ fewer toothpicks. This continues all the way to the top. Therefore, the number of slanted toothpicks is \[2004 + 2002 + 2000 + \cdots + 4 + 2 = 1002^2 + 1002.\]
The horizontal toothpicks are easier. For each row, we will only count the toothpicks on the bottom of the row to avoid overcounting. Since the bottom row has $2003$ toothpicks, there will be $1002$ toothpicks below the row and $1001$ toothpicks above the row (which is the bottom of the next row). This continues all the way to the top, so the number of horizontal toothpicks is \[1002 + 1001 + 1000 + \cdots + 2 + 1 = \frac{(1002)(1003)}{2}.\]
Adding these together, we get our answer of \[1002^2 + 1002 + \frac{(1002)(1003)}{2} = \boxed{\mathrm{(C)}\ 1,507,509}.\]
~jk11507

## Video Solution (Meta-Solving Technique)
https://youtu.be/GmUWIXXf_uk?t=494
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .