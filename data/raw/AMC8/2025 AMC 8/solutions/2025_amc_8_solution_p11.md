# 2025 AMC 8 Problem 11

## Problem

A $\textit{tetromino}$ consists of four squares connected along their edges. There are five possible tetromino shapes, $I$ , $O$ , $L$ , $T$ , and $S$ , shown below, which can be rotated or flipped over. Three tetrominoes are used to completely cover a $3\times4$ rectangle. At least one of the tiles is an $S$ tile. What are the other two tiles?

[asy] unitsize(12); add(grid(1,4)); label("I", (0.5,-1)); add(shift((5,0)) * grid(2,2)); label("O", (6,-1)); add(shift((11,0)) * grid(1,3)); add(shift((11,0)) * grid(2,1)); label("L", (12,-1)); add(shift((18,0)) * grid(1,1)); add(shift((17,1)) * grid(3,1)); label("T", (18.5,-1)); add(shift((25,1)) * grid(2,1)); add(shift((24,0)) * grid(2,1)); label("S", (25.5,-1)); add(shift((12,-6)) * grid(4,3)); [/asy]

$\textbf{(A)}I$ and $L\qquad \textbf{(B)} I$ and $T\qquad \textbf{(C)} L$ and $L\qquad \textbf{(D)}L$ and $S\qquad \textbf{(E)}O$ and $T$

## Solution 1
The $3\times4$ rectangle allows for $7$ possible places to put the S piece, with each possible placement having an inverted version. One of the cases looks like this: [asy] path x = (0,0)--(0,2)--(1,2)--(1,3)--(2,3)--(2,1)--(1,1)--(1,0)--cycle; fill(x, rgb(0,30,0)); add(grid(4,3)); [/asy] As you can see, there is a hole in the top left corner of the board, which would be impossible to fill using the tetrominos. There are three cases in which a hole isn't created; the S lies flat in the bottom left corner, it lies flat in the top right corner, or it stands upright in the center. All three tilings are shown below. [asy] path z1 = (2,0)--(3,0)--(3,2)--(2,2)--(2,3)--(1,3)--(1,1)--(2,1)--cycle; path z2 = (0,0)--(2,0)--(2,1)--(1,1)--(1,3)--(0,3)--cycle; path z3 = (2,3)--(4,3)--(4,0)--(3,0)--(3,2)--(2,2)--cycle; fill(z1, rgb(0,30,0)); fill(z2, rgb(127,80,0)); fill(z3, rgb(127,100,0)); add(grid(4,3)); [/asy]
[asy] path y1 = (0,0)--(2,0)--(2,1)--(3,1)--(3,2)--(1,2)--(1,1)--(0,1)--cycle; path y2 = (0,1)--(1,1)--(1,2)--(3,2)--(3,3)--(0,3)--cycle; path y3 = (2,0)--(4,0)--(4,3)--(3,3)--(3,1)--(2,1)--cycle; fill(y1, rgb(0,30,0)); fill(y2, rgb(127,80,0)); fill(y3, rgb(127,100,0)); add(grid(4,3)); [/asy]
[asy] path w1 = (1,1)--(3,1)--(3,2)--(4,2)--(4,3)--(2,3)--(2,2)--(1,2)--cycle; path w2 = (0,0)--(0,3)--(2,3)--(2,2)--(1,2)--(1,0)--cycle; path w3 = (1,0)--(4,0)--(4,2)--(3,2)--(3,1)--(1,1)--cycle; fill(w1, rgb(0,30,0)); fill(w2, rgb(127,80,0)); fill(w3, rgb(127,100,0)); add(grid(4,3)); [/asy] For each of the inverted cases, the L pieces can be inverted along with the S piece. Because the only cases that fill the rectangle after the S is placed are the ones that use two L pieces, the answer must be $\boxed{\textbf{(C)}~L \ and \ L}$ . ~bubby617

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=mhn50YKL4_Yo1PH6&t=965 ~hsnacademy

## Video Solution 1 by Thinking Feet
https://youtu.be/PKMpTS6b988

## Video Solution(Quick, fast, easy!)
https://youtu.be/fdG7EDW_7xk
~MC
### See Also