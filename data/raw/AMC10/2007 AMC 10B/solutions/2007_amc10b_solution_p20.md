# 2007 AMC 10B Problem 20

## Problem

A set of $25$ square blocks is arranged into a $5 \times 5$ square. How many different combinations of $3$ blocks can be selected from that set so that no two are in the same row or column?

$\textbf{(A) } 100 \qquad\textbf{(B) } 125 \qquad\textbf{(C) } 600 \qquad\textbf{(D) } 2300 \qquad\textbf{(E) } 3600$

## Solution 1
There are $25$ ways to choose the first square. The four remaining squares in its row and column and the square you chose exclude nine squares from being chosen next time.
There are $16$ remaining blocks to be chosen for the second square. The three remaining spaces in its row and column and the square you chose must be excluded from being chosen next time.
Finally, the last square has $9$ remaining choices.
The number of ways to choose $3$ squares is $25 \cdot 16 \cdot 9,$ but the order in which you chose the squares does not matter as the blocks are indistinguishable, so we divide by $3!$ .
\[\frac{25 \cdot 16 \cdot 9}{3 \cdot 2 \cdot 1} = 25 \cdot 8 \cdot 3 = 100 \cdot 6 = \boxed{\mathrm{(C) \ } 600}\]

## Solution 2
Once we choose our three squares, we will have occupied three separate columns $(A, B, C)$ and three separate rows. There are ${5 \choose 3} \times {5 \choose 3}$ ways to choose these rows and columns.
There are $3$ ways to assign the square in column $A$ to a row, $2$ ways to assign the square in column $B$ to one of the remaining two rows, and poor square in column $C$ doesn't get to choose. $:($
In total, we have \[{5 \choose 3} \times {5 \choose 3} \times 3!\] which totals out to $\boxed{\mathrm{(C) \ } 600}$ .
~HappyHuman

## Solution 3 (Answer choices)
We know that there are $\binom{25}{3}=2300$ ways to choose three blocks. However, the restriction clearly limits the number of ways we can choose our blocks. Hence, only $\text{(A)}$ , $\text{(B)}$ , or $\text{(C)}$ could be the correct answer. Clearly, there are more than $125$ ways, thus yielding $\boxed{\text{(C)} 600}$ ways.

## Video Solution 1 by OmegaLearn
https://youtu.be/0W3VmFp55cM?t=4921
~ pi_is_3.14

## Video Solution 2 by OmegaLearn
https://youtu.be/5UojVH4Cqqs?t=3460
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .