# 2012 AMC 10A Problem 14

## Problem

Chubby makes nonstandard checkerboards that have $31$ squares on each side. The checkerboards have a black square in every corner and alternate red and black squares along every row and column. How many black squares are there on such a checkerboard?

$\textbf{(A)}\ 480 \qquad\textbf{(B)}\ 481 \qquad\textbf{(C)}\ 482 \qquad\textbf{(D)}\ 483 \qquad\textbf{(E)}\ 484$

## Solution 1
There are 15 rows with 15 black tiles, and 16 rows with 16 black tiles, so the answer is $15^2+16^2 =225+256= \boxed{\textbf{(B)}\ 481}$
Note: When solving $16^2$ + $15^2$ , you only need to calculate the units digit.

## Solution 2
We build the $31 \times 31$ checkerboard starting with a board of $30 \times 30$ that is exactly half black. There are $15 \cdot 30$ black tiles in this region.
Add to this $30 \times 30$ checkerboard a $1 \times 30$ strip on the bottom that has $15$ black tiles.
Add to this $31 \times 30$ checkerboard a $31 \times 1$ strip on the right that has $15 + 1$ black tiles.
In total, there are $15 \cdot 30 + 15 + 15 + 1 = 481$ tiles, giving an answer of $\boxed{\textbf{(B)}\ 481}$

## Solution 3
For every $2 \times 31$ strip, there are 31 black tiles and 31 white tiles. There are 15 such strips in total and another $1 \times 31$ strip having 16 black titles.
In total, there are $31\times 15+16=481$ black tiles.
~Bran_Quin

## Solution 4
Drawing smaller scale sketches, we notice that the odd columns of an $n \times n$ (where $n$ is odd) board have $\left \lceil \frac{n}{2} \right \rceil$ black tiles, while the even columns have $\left \lfloor \frac{n}{2} \right \rfloor$ black tiles. In our case, we have a $31 \times 31$ board. We have $16$ odd columns, and $15$ even columns, so the number of black tiles in total is $16^2 + 15^2 = \boxed{\textbf{(B)}\ 481}$ .
~kn07
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .