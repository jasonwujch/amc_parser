# 2004 AMC 10A Problem 16

## Problem

The $5\times 5$ grid shown contains a collection of squares with sizes from $1\times 1$ to $5\times 5$ . How many of these squares contain the black center square?

[asy] for (int i=0; i<5; ++i) { for (int j=0; j<5; ++j) { draw((-2.5+i, -2.5+j)--(-1.5+i, -2.5+j) -- (-1.5+i, -1.5+j) -- (-2.5+i, -1.5+j)--cycle); } fill((-0.5,-0.5)--(-0.5, 0.5)--(0.5,0.5) -- (0.5,-0.5)--cycle, black); } [/asy]

$\mathrm{(A) \ } 12 \qquad \mathrm{(B) \ } 15 \qquad \mathrm{(C) \ } 17 \qquad \mathrm{(D) \ } 19\qquad \mathrm{(E) \ } 20$

## Solution

## Solution 1
Since there are five types of squares: $1 \times 1, 2 \times 2, 3 \times 3, 4 \times 4,$ and $5 \times 5.$ We must find how many of each square contain the black shaded square in the center.
If we list them, we get that
- There is $1$ of all $1\times 1$ squares, containing the black square
- There are $4$ of all $2\times 2$ squares, containing the black square
- There are $9$ of all $3\times 3$ squares, containing the black square
- There are $4$ of all $4\times 4$ squares, containing the black square
- There is $1$ of all $5\times 5$ squares, containing the black square
Thus, the answer is $1+4+9+4+1=19\Rightarrow\boxed{\mathrm{(D)}\ 19}$ .

## Solution 2
We use complementary counting. There are only $2\times2$ and $1\times1$ squares that do not contain the black square. Counting, there are $12$ - $2\times2$ squares, and $25-1 = 24$ $1\times1$ squares that do not contain the black square. That gives $12+24=36$ squares that don't contain it. There are a total of $25+16+9+4+1 = 55$ squares possible $(25$ - $1\times1$ squares $16$ - $2\times2$ squares $9$ - $3\times3$ squares $4$ - $4\times4$ squares and $1$ - $5\times5$ square), therefore there are $55-36 = 19$ squares that contain the black square, which is $\boxed{\mathrm{(D)}\ 19}$ .

## Video Solution by OmegaLearn
https://youtu.be/HhdpuJt78Hg?t=168
~ pi_is_3.14 ~VictorZhang

## Video Solutions
- https://youtu.be/0W3VmFp55cM?t=4697
- https://youtu.be/aMmF6jz6xA4
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .