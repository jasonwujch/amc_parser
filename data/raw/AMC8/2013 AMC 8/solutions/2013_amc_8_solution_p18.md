# 2013 AMC 8 Problem 18

## Problem

Isabella uses one-foot cubical blocks to build a rectangular fort that is $12$ feet long, $10$ feet wide, and $5$ feet high. The floor and the four walls are all one foot thick. How many blocks does the fort contain?

[asy]import three; currentprojection=orthographic(-8,15,15); triple A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P; A = (0,0,0); B = (0,10,0); C = (12,10,0); D = (12,0,0); E = (0,0,5); F = (0,10,5); G = (12,10,5); H = (12,0,5); I = (1,1,1); J = (1,9,1); K = (11,9,1); L = (11,1,1); M = (1,1,5); N = (1,9,5); O = (11,9,5); P = (11,1,5); //outside box far draw(surface(A--B--C--D--cycle),white,nolight); draw(A--B--C--D--cycle); draw(surface(E--A--D--H--cycle),white,nolight); draw(E--A--D--H--cycle); draw(surface(D--C--G--H--cycle),white,nolight); draw(D--C--G--H--cycle); //inside box far draw(surface(I--J--K--L--cycle),white,nolight); draw(I--J--K--L--cycle); draw(surface(I--L--P--M--cycle),white,nolight); draw(I--L--P--M--cycle); draw(surface(L--K--O--P--cycle),white,nolight); draw(L--K--O--P--cycle); //inside box near draw(surface(I--J--N--M--cycle),white,nolight); draw(I--J--N--M--cycle); draw(surface(J--K--O--N--cycle),white,nolight); draw(J--K--O--N--cycle); //outside box near draw(surface(A--B--F--E--cycle),white,nolight); draw(A--B--F--E--cycle); draw(surface(B--C--G--F--cycle),white,nolight); draw(B--C--G--F--cycle); //top draw(surface(E--H--P--M--cycle),white,nolight); draw(surface(E--M--N--F--cycle),white,nolight); draw(surface(F--N--O--G--cycle),white,nolight); draw(surface(O--G--H--P--cycle),white,nolight); draw(M--N--O--P--cycle); draw(E--F--G--H--cycle); label("10",(A--B),SE); label("12",(C--B),SW); label("5",(F--B),W);[/asy]

$\textbf{(A)}\ 204 \qquad \textbf{(B)}\ 280 \qquad \textbf{(C)}\ 320 \qquad \textbf{(D)}\ 340 \qquad \textbf{(E)}\ 600$

## Solution 1
There are $10 \cdot 12 = 120$ cubes on the base of the box. Then, for each of the 4 layers above the bottom (as since each cube is 1 foot by 1 foot by 1 foot and the box is 5 feet tall, there are 4 feet left), there are $9 + 11 + 9 + 11 = 40$ cubes. Hence, the answer is $120 + 4 \cdot 40 = \boxed{\textbf{(B)}\ 280}$ .

## Solution 2 (Complementary Counting)
We can just calculate the volume of the prism that was cut out of the original $12\times 10\times 5$ box. Each interior side of the fort will be $2$ feet shorter than each side of the outside. Since the floor is $1$ foot, the height will be $4$ feet. So the volume of the interior box is $10\times 8\times 4=320\text{ ft}^3$ .
The volume of the original box is $12\times 10\times 5=600\text{ ft}^3$ . Therefore, the number of blocks contained in the fort is $600-320=\boxed{\textbf{(B)}\ 280}$

## Video Solution by OmegaLearn
https://youtu.be/FDgcLW4frg8?t=5261
~ pi_is_3.14

## Video Solution 2
https://youtu.be/WlMUXUloTFM Soo, DRMS, NM

## Video Solution 3
https://youtu.be/zFNf8WxBdoY ~savannahsolver
### See Also