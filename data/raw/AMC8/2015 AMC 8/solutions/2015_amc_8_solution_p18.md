# 2015 AMC 8 Problem 18

## Problem

An arithmetic sequence is a sequence in which each term after the first is obtained by adding a constant to the previous term. For example, $2,5,8,11,14$ is an arithmetic sequence with five terms, in which the first term is $2$ and the constant added is $3$ . Each row and each column in this $5\times5$ array is an arithmetic sequence with five terms. The square in the center is labelled $X$ as shown. What is the value of $X$ ?

$\textbf{(A) }21\qquad\textbf{(B) }31\qquad\textbf{(C) }36\qquad\textbf{(D) }40\qquad \textbf{(E) }42$

[asy] size(3.85cm); label("$X$",(2.5,2.1),N); for (int i=0; i<=5; ++i) draw((i,0)--(i,5), linewidth(.5)); for (int j=0; j<=5; ++j) draw((0,j)--(5,j), linewidth(.5)); void draw_num(pair ll_corner, int num) { label(string(num), ll_corner + (0.5, 0.5), p = fontsize(19pt)); } draw_num((0,0), 17); draw_num((4, 0), 81); draw_num((0, 4), 1); draw_num((4,4), 25); void foo(int x, int y, string n) { label(n, (x+0.5,y+0.5), p = fontsize(19pt)); } foo(2, 4, " "); foo(3, 4, " "); foo(0, 3, " "); foo(2, 3, " "); foo(1, 2, " "); foo(3, 2, " "); foo(1, 1, " "); foo(2, 1, " "); foo(3, 1, " "); foo(4, 1, " "); foo(2, 0, " "); foo(3, 0, " "); foo(0, 1, " "); foo(0, 2, " "); foo(1, 0, " "); foo(1, 3, " "); foo(1, 4, " "); foo(3, 3, " "); foo(4, 2, " "); foo(4, 3, " "); [/asy]

## Solutions

## Solution 1
We begin filling in the table. The top row has a first term $1$ and a fifth term $25$ , so we have the common difference is $\frac{25-1}4=6$ . This means we can fill in the first row of the table: [asy] size(3.85cm); label("$X$",(2.5,2.1),N); for (int i=0; i<=5; ++i) draw((i,0)--(i,5), linewidth(.5)); for (int j=0; j<=5; ++j) draw((0,j)--(5,j), linewidth(.5)); void draw_num(pair ll_corner, int num) { label(string(num), ll_corner + (0.5, 0.5), p = fontsize(19pt)); } draw_num((0,0), 17); draw_num((4, 0), 81); draw_num((1,4), 7); draw_num((2,4), 13); draw_num((3,4), 19); draw_num((0, 4), 1); draw_num((4,4), 25); void foo(int x, int y, string n) { label(n, (x+0.5,y+0.5), p = fontsize(19pt)); } foo(2, 4, " "); foo(3, 4, " "); foo(0, 3, " "); foo(2, 3, " "); foo(1, 2, " "); foo(3, 2, " "); foo(1, 1, " "); foo(2, 1, " "); foo(3, 1, " "); foo(4, 1, " "); foo(2, 0, " "); foo(3, 0, " "); foo(0, 1, " "); foo(0, 2, " "); foo(1, 0, " "); foo(1, 3, " "); foo(1, 4, " "); foo(3, 3, " "); foo(4, 2, " "); foo(4, 3, " "); [/asy]
The fifth row has a first term of $17$ and a fifth term of $81$ , so the common difference is $\frac{81-17}4=16$ . We can fill in the fifth row of the table as shown: [asy] size(3.85cm); label("$X$",(2.5,2.1),N); for (int i=0; i<=5; ++i) draw((i,0)--(i,5), linewidth(.5)); for (int j=0; j<=5; ++j) draw((0,j)--(5,j), linewidth(.5)); void draw_num(pair ll_corner, int num) { label(string(num), ll_corner + (0.5, 0.5), p = fontsize(19pt)); } draw_num((0,0), 17); draw_num((4, 0), 81); draw_num((1,4), 7); draw_num((2,4), 13); draw_num((3,4), 19); draw_num((4, 4), 25); draw_num((0, 4), 1); draw_num((1, 0), 33); draw_num((2, 0), 49); draw_num((3, 0), 65); void foo(int x, int y, string n) { label(n, (x+0.5,y+0.5), p = fontsize(19pt)); } foo(2, 4, " "); foo(3, 4, " "); foo(0, 3, " "); foo(2, 3, " "); foo(1, 2, " "); foo(3, 2, " "); foo(1, 1, " "); foo(2, 1, " "); foo(3, 1, " "); foo(4, 1, " "); foo(2, 0, " "); foo(3, 0, " "); foo(0, 1, " "); foo(0, 2, " "); foo(1, 0, " "); foo(1, 3, " "); foo(1, 4, " "); foo(3, 3, " "); foo(4, 2, " "); foo(4, 3, " "); [/asy]
We must find the third term of the arithmetic sequence with a first term of $13$ and a fifth term of $49$ . The common difference of this sequence is $\frac{49-13}4=9$ , so the third term is $13+2\cdot 9=\boxed{\textbf{(B) }31}$ .

## Solution 2
The middle term of the first row is $\frac{25+1}{2}=13$ , since the middle number is just the average in an arithmetic sequence. Similarly, the middle of the bottom row is $\frac{17+81}{2}=49$ . Applying this again for the middle column, the answer is $\frac{49+13}{2}=\boxed{\textbf{(B)}~31}$ .

## Solution 3
The value of $X$ is simply the average of the average values of both diagonals that contain $X$ . This is $\frac{\frac{1+81}{2}+\frac{17+25}{2}}{2} =\frac{\frac{82}{2}+\frac{42}{2}}{2} = \frac{41+21}{2} = \boxed{\textbf{(B)}~31}$

## Video Solution (HOW TO THINK CRITICALLY!!!)
https://youtu.be/1BUbtuK_MXI
~Education, the Study of Everything

## Video Solution
https://youtu.be/tKsYSBdeVuw?t=1258

## Video Solution
https://youtu.be/QFC4VmFa9Kc
~savannahsolver
### See Also