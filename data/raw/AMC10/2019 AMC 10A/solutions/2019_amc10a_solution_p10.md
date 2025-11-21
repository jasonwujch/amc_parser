# 2019 AMC 10A Problem 10

## Problem

A rectangular floor that is $10$ feet wide and $17$ feet long is tiled with $170$ one-foot square tiles. A bug walks from one corner to the opposite corner in a straight line. Including the first and the last tile, how many tiles does the bug visit?

$\textbf{(A) } 17 \qquad\textbf{(B) } 25 \qquad\textbf{(C) } 26 \qquad\textbf{(D) } 27 \qquad\textbf{(E) } 28$

## Solution 1
The number of tiles the bug visits is equal to $1$ plus the number of times it crosses a horizontal or vertical line. As it must cross $16$ horizontal lines and $9$ vertical lines, it must be that the bug visits a total of $16+9+1 = \boxed{\textbf{(C) }26}$ squares.
Note : The general formula for this is $a+b-\gcd(a,b)$ , because it is the number of vertical/horizontal lines crossed minus the number of corners crossed (to avoid double counting). In this particular problem, it was $16 + 9 - 1$ (since $\text{gcd}(16,9) = 1$ ), which is $24$ , but then you add $2$ because the first tile and the last tile are counted, which in the general formula are not counted.
One can see why it is gcd(a,b) due to slope ~Williamgolly
Comment : The above note defines a, b incorrectly. One counter example is a 17x9 grid, which should result in 25 tiles. However, $\text{gcd}(16, 8) = 8$ . Here $a+b-\gcd(a,b)$ is correct when a = 17 and b = 9. ~aliciawu

## Solution 2 (Less than 1 minute)
A 1x1 tile has a diagonal length of \( \sqrt{2} \). The rectangle has a diagonal length of \( 50\sqrt{2} \). So we get \( 50\sqrt{2}/\sqrt{2} = 50\).
However, we are overcounting by double because each diagonal is shared by 2 segments that overlap an area, so we divide \( 50/2 = 25 \).
However, now we are not including the last square, which is alone and has no overlap, so we add back 1 to get \( 25+1 =\) $\boxed{\textbf{(C) }26}$ .
~Pinotation

## Solution 3 (drawing)
We can also draw a diagram or scale model of the entire rectangular floor (optionally with grid paper and/or a ruler so it will be to scale), then simply count the number of tiles the path crosses. To make this slightly easier, we can divide the full grid into $4$ sections, and just draw one of these $5$ feet by $8.5$ feet sections.
[asy] unitsize(20); for(int i =0; i<= 7; ++i) { for(int j =0; j<= 4; ++j) { draw((i,j)--(i+1,j)--(i+1,j+1)--(i,j+1)--cycle); } for(int k =0; k<= 4; ++k) { draw((8,k)--(8.5,k)--(8.5,k+1)--(8,k+1)--cycle); } } draw((0,5)--(8.5,0)--cycle); [/asy]
Though it may appear that the line we drew comes very close to several points, we know that since $10$ and $17$ are relatively prime (numbers where the only positive integer that divides both of them is 1, a.k.a. numbers with a gcd of 1), the line will not actually pass through any of these points, so the total number of squares crossed will be the same regardless of which side we count. If we count the number of squares the line passes through using the diagram, we get $13$ squares. We can then multiply this by 2 to find out the total number of squares the bug passes through on the rectangular floor giving us a total of $2 \cdot 13 = \boxed{\textbf{(C) }26}$ .

## Solution 4 (Under 1 Minute)
We can see that the big $10$ by $17$ rectangle can be split into $2$ smaller $5$ by $17$ rectangles. This means that the number of small rectangles is divisible by $2$ . This also means that the number of small rectangles in the $5$ by $17$ rectangles is an odd number since it can't be divided into any smaller triangles. Thus the only number that meets the requirements is $\boxed{\textbf{(C) } 26}$ .
~Continuous_Pi

## Video Solution
https://www.youtube.com/watch?v=qN1g7Vt5SCg
https://youtu.be/Z-sUMqZH0j4
~savannahsolver

## Video Solution by Omega Learn
https://youtu.be/zfChnbMGLVQ?t=843
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .