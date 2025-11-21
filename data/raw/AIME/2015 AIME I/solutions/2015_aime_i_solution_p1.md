# 2015 AIME I Problem 1

## Problem

The expressions $A$ = $1 \times 2 + 3 \times 4 + 5 \times 6 + \cdots + 37 \times 38 + 39$ and $B$ = $1 + 2 \times 3 + 4 \times 5 + \cdots + 36 \times 37 + 38 \times 39$ are obtained by writing multiplication and addition operators in an alternating pattern between successive integers. Find the positive difference between integers $A$ and $B$ .

## Video Solution For Problems 1-3
https://www.youtube.com/watch?v=5HAk-6qlOH0

## Solution 1
We have \[|A-B|=|1+3(4-2)+5(6-4)+ \cdots + 37(38-36)-39(1-38)|\] \[\implies |2(1+3+5+7+ \cdots +37)-1-39(37)|\] \[\implies |361(2)-1-39(37)|=|722-1-1443|=|-722|\implies \boxed{722}\]

## Solution 2
We see that
$A=(1\times 2)+(3\times 4)+(5\times 6)+\cdots +(35\times 36)+(37\times 38)+39$
and
$B=1+(2\times 3)+(4\times 5)+(6\times 7)+\cdots +(36\times 37)+(38\times 39)$ .
Therefore,
$B-A=-38+(2\times 2)+(2\times 4)+(2\times 6)+\cdots +(2\times 36)+(2\times 38)$
$=-38+4\times (1+2+3+\cdots+19)$
$=-38+4\times\frac{20\cdot 19}{2}=-38+760=\boxed{722}.$

## Solution 3 (slower solution)
For those that aren't shrewd enough to recognize the above, we may use Newton's Little Formula to semi-bash the equations.
We write down the pairs of numbers after multiplication and solve each layer:
\[2, 12, 30, 56, 90...(39)\]
\[10, 18, 26, 34...\]
\[8, 8, 8...\]
and
\[(1) 6, 20, 42, 72...\] \[14, 22, 30...\]
\[8, 8, 8...\]
Then we use Newton's Little Formula for the sum of $n$ terms in a sequence.
Notice that there are $19$ terms in each sequence, plus the tails of $39$ and $1$ on the first and second equations, respectively.
So,
\[2\binom{19}{1}+10\binom{19}{2}+8\binom{19}{3}+1\]
\[6\binom{19}{1}+14\binom{19}{2}+8\binom{19}{3}+39\]
Subtracting $A$ from $B$ gives:
\[4\binom{19}{1}+4\binom{19}{2}-38\]
Which unsurprisingly gives us $\boxed{722}.$
-jackshi2006
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .