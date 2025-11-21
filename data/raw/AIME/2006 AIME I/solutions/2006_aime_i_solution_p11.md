# 2006 AIME I Problem 11

## Problem

A collection of 8 cubes consists of one cube with edge - length $k$ for each integer $k, 1 \le k \le 8.$ A tower is to be built using all 8 cubes according to the rules:

- Any cube may be the bottom cube in the tower.

- The cube immediately on top of a cube with edge-length $k$ must have edge-length at most $k+2.$

Let $T$ be the number of different towers than can be constructed. What is the remainder when $T$ is divided by 1000?

## Solution
We proceed recursively . Suppose we can build $T_m$ towers using blocks of size $1, 2, \ldots, m$ . How many towers can we build using blocks of size $1, 2, \ldots, m, m + 1$ ? If we remove the block of size $m + 1$ from such a tower (keeping all other blocks in order), we get a valid tower using blocks $1, 2, \ldots, m$ . Given a tower using blocks $1, 2, \ldots, m$ (with $m \geq 2$ ), we can insert the block of size $m + 1$ in exactly 3 places: at the beginning, immediately following the block of size $m - 1$ or immediately following the block of size $m$ . Thus, there are 3 times as many towers using blocks of size $1, 2, \ldots, m, m + 1$ as there are towers using only $1, 2, \ldots, m$ . There are 2 towers which use blocks $1, 2$ , so there are $2\cdot 3^6 = 1458$ towers using blocks $1, 2, \ldots, 8$ , so the answer is $\boxed{458}$ .
(Note that we cannot say, "there is one tower using the block $1$ , so there are $3^7$ towers using the blocks $1, 2, \ldots, 8$ ." The reason this fails is that our recursion only worked when $m \geq 2$ : when $m = 1$ , there are only 2 places to insert a block of size $m + 1 = 2$ , at the beginning or at the end, rather than the 3 places we have at later stages. Also, note that this method generalizes directly to seeking the number of towers where we change the second rule to read, "The cube immediately on top of a cube with edge-length $k$ must have edge-length at most $k + n$ ," where $n$ can be any fixed integer.)

## Video Solution by OmegaLearn
https://youtu.be/WpSpnx8PPnc?t=732
~ pi_is_3.14
- 2015 AIME II Problem 10
These problems are copyrighted © by the Mathematical Association of America.