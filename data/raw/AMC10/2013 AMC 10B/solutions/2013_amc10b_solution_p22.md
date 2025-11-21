# 2013 AMC 10B Problem 22

## Problem

The regular octagon $ABCDEFGH$ has its center at $J$ . Each of the vertices and the center are to be associated with one of the digits $1$ through $9$ , with each digit used once, in such a way that the sums of the numbers on the lines $AJE$ , $BJF$ , $CJG$ , and $DJH$ are all equal. In how many ways can this be done?

$\textbf{(A)}\ 384 \qquad\textbf{(B)}\ 576 \qquad\textbf{(C)}\ 1152 \qquad\textbf{(D)}\ 1680 \qquad\textbf{(E)}\ 3456$

[asy] pair A,B,C,D,E,F,G,H,J; A=(20,20(2+sqrt(2))); B=(20(1+sqrt(2)),20(2+sqrt(2))); C=(20(2+sqrt(2)),20(1+sqrt(2))); D=(20(2+sqrt(2)),20); E=(20(1+sqrt(2)),0); F=(20,0); G=(0,20); H=(0,20(1+sqrt(2))); J=(10(2+sqrt(2)),10(2+sqrt(2))); draw(A--B); draw(B--C); draw(C--D); draw(D--E); draw(E--F); draw(F--G); draw(G--H); draw(H--A); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(G); dot(H); dot(J); label("A",A,NNW); label("B",B,NNE); label("C",C,ENE); label("D",D,ESE); label("E",E,SSE); label("F",F,SSW); label("G",G,WSW); label("H",H,WNW); label("J",J,SE); [/asy]

## Solution 1
First of all, note that $J$ must be $1$ , $5$ , or $9$ to preserve symmetry, since the sum of 1 to 9 is 45, and we need the remaining 8 to be divisible by 4 (otherwise we will have uneven sums). So, we have:
[asy] pair A,B,C,D,E,F,G,H,J; A=(20,20(2+sqrt(2))); B=(20(1+sqrt(2)),20(2+sqrt(2))); C=(20(2+sqrt(2)),20(1+sqrt(2))); D=(20(2+sqrt(2)),20); E=(20(1+sqrt(2)),0); F=(20,0); G=(0,20); H=(0,20(1+sqrt(2))); J=(10(2+sqrt(2)),10(2+sqrt(2))); draw(A--B); draw(B--C); draw(C--D); draw(D--E); draw(E--F); draw(F--G); draw(G--H); draw(H--A); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(G); dot(H); dot(J); label("A",A,NNW); label("B",B,NNE); label("C",C,ENE); label("D",D,ESE); label("E",E,SSE); label("F",F,SSW); label("G",G,WSW); label("H",H,WNW); label("J $(1, 5, 9)$",J,SE); [/asy]
We also notice that $A+E = B+F = C+G = D+H$ .
WLOG, assume that $J = 1$ . Thus the pairs of vertices must be $9$ and $2$ , $8$ and $3$ , $7$ and $4$ , and $6$ and $5$ . There are $4! = 24$ ways to assign these to the vertices. Furthermore, there are $2^{4} = 16$ ways to switch them (i.e. do $2$ $9$ instead of $9$ $2$ ).
Thus, there are $16(24) = 384$ ways for each possible J value. There are $3$ possible J values that still preserve symmetry: $384(3) = \boxed{\textbf{(C) }1152}$

## Solution 2
As in solution 1, $J$ must be $1$ , $5$ , or $9$ giving us 3 choices. Additionally $A+E = B+F = C+G = D+H$ . This means once we choose $J$ there are $8$ remaining choices. Going clockwise from $A$ we count, $8$ possibilities for $A$ . Choosing $A$ also determines $E$ which leaves $6$ choices for $B$ , once $B$ is chosen it also determines $F$ leaving $4$ choices for $C$ . Once $C$ is chosen it determines $G$ leaving $2$ choices for $D$ . Choosing $D$ determines $H$ , exhausting the numbers. Additionally, there are three possible values for $J$ . To get the answer we multiply $2\cdot4\cdot6\cdot8\cdot3=\boxed{\textbf{(C) }1152}$ .
### Remark
Solutions 1 and 2 state that $J=1, 5, 9$ without rigorous analysis. Here it is:
Because $gcd(4,3)=1$ , so $4|(15+J)$ , but $15 \equiv 3 \pmod 4$ , so $J \equiv 1 \pmod 4$ , $J=1,5,9$
~ isabelchen

## Video Solution by Pi Academy
https://youtu.be/0djZt1Fvuvw?si=TnPgQi3DnrI5IsE8
~ Pi Academy

## Video Solution 2
https://youtu.be/3MDr_t1ZzQk
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .