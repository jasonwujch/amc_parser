# 2001 AIME II Problem 9

## Problem

Each unit square of a 3-by-3 unit-square grid is to be colored either blue or red. For each square, either color is equally likely to be used. The probability of obtaining a grid that does not have a 2-by-2 red square is $\frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
We can use complementary counting , counting all of the colorings that have at least one red $2\times 2$ square.
- For at least one red $2 \times 2$ square:
- For at least two $2 \times 2$ squares:
- For at least three $2 \times 2$ squares:
- For at least four $2 \times 2$ squares, we clearly only have one way.
By the Principle of Inclusion-Exclusion , there are (alternatively subtracting and adding) $128-40+8-1=95$ ways to have at least one red $2 \times 2$ square.
There are $2^9=512$ ways to paint the $3 \times 3$ square with no restrictions, so there are $512-95=417$ ways to paint the square with the restriction. Therefore, the probability of obtaining a grid that does not have a $2 \times 2$ red square is $\frac{417}{512}$ , and $417+512=\boxed{929}$ .

## Solution 2
We consider how many ways we can colour the $2 \times 2$ grid:
$(1)$ : All the grids are red-- $1$ case
$(2)$ : One unit square is blue--The blue lies on the center of the bigger square, makes no $2 \times 2$ grid $9-1=8$ cases
$(3)$ : Two unit squares are blue--one of the squares lies in the center of the bigger square, makes no $2 \times 2$ grid, $8$ cases. Or, two squares lie on second column, first row, second column third row; second row first column, second row third column, 2 extra cases. $\binom 9 2-8-2=26$ cases
$(4)$ Three unit squares are blue. We find that if a $2 \times 2$ square is formed, there are 5 extra unit squares can be painted. But cases that three squares in the same column or same row is overcomunted. So in this case, there are $4\cdot (\binom 5 3)-4=36$
$(5)$ Four unit squares are blue, no overcounted case will be considered. there are $4\cdot \binom 5 4=20$
$(6)$ Five unit squares are blue, $4$ cases in all
Sum up those cases, there are $1+8+26+36+20+4=95$ cases that a $2 \times 2$ grid can be formed.
In all, there are $2^9=512$ possible ways to paint the big square, so the answer is $1-\frac{95}{512}=\frac{417}{512}$ leads to $\boxed{929}$
~bluesoul

## Solution 3 (Case Work)
\[\begin{array}{|c|c|c|} \hline C_{11} & C_{12} & C_{13}\\ \hline C_{21} & C_{22} & C_{23}\\ \hline C_{31} & C_{32} & C_{33}\\ \hline \end{array}\]
Case 1: The 3-by-3 unit-square grid has exactly $1$ 2-by-2 red square
Assume the 2-by-2 red square is at $C_{11}, C_{12}, C_{21}, C_{22}$ . To make sure there are no more 2-by-2 red squares, $C_{31} \text{and} C_{32}$ can't both be red and $C_{13} \text{and} C_{23}$ can't both be red. Meaning that there are $2^2-1=3$ coloring methods for $C_{31} \text{and} C_{32}$ and $C_{13} \text{and} C_{23}$ . $C_{33}$ can be colored with either colors. However, the coloring method where $C_{23}, C_{32}, C_{33}$ are all red needs to be removed. For exactly one 2-by-2 red square at $C_{11}, C_{12}, C_{21}, C_{22}$ , there are $3 \cdot 3 \cdot 2 -1=17$ coloring methods. As there are $4$ locations for the 2-by-2 red square on the 3-by-3 unit-square grid, there are $17 \cdot 4 = 68$ coloring methods.
Case 2: The 3-by-3 unit-square grid has exactly $2$ 2-by-2 red squares
Case 2.1: $2$ 2-by-2 red squares take up $6$ unit grids
Assume the $2$ 2-by-2 red squares are at $C_{11}, C_{12}, C_{21}, C_{22}, C_{31}, C_{32}$ . To make sure there are no more 2-by-2 red squares, $C_{13} \text{and} C_{23}$ can't both be red. Meaning that there are $2^2-1=3$ coloring methods for $C_{13} \text{and} C_{23}$ . $C_{33}$ can be colored with either colors. However, the coloring method where $C_{13}, C_{23}, C_{33}$ are all red needs to be removed. For exactly $2$ 2-by-2 red squares at $C_{11}, C_{12}, C_{21}, C_{22}, C_{31}, C_{32}$ , there are $3 \cdot 2 -1=5$ coloring methods. As there are $4$ locations for the $2$ 2-by-2 red squares on the 3-by-3 unit-square grid, there are $5 \cdot 4 = 20$ coloring methods.
Case 2.2: $2$ 2-by-2 red squares take up $7$ unit grids
Assume the $2$ 2-by-2 red squares are at $C_{11}, C_{12}, C_{21}, C_{22}, C_{23}, C_{32}, C_{33}$ . To make sure there are no more 2-by-2 red squares, $C_{13}$ and $C_{31}$ can't be red. Meaning that there is $1$ coloring method for $C_{13}$ and $C_{31}$ . For exactly $2$ 2-by-2 red squares at $C_{11}, C_{12}, C_{21}, C_{22}, C_{23}, C_{32}, C_{33}$ , there is $1$ coloring method. As there are $2$ locations for the $2$ 2-by-2 red squares on the 3-by-3 unit-square grid, there are $1 \cdot 2 = 2$ coloring methods.
Hence, if the 3-by-3 unit-square grid has exactly $2$ 2-by-2 red squares, there are $20+2 = 22$ coloring methods.
Case 3: The 3-by-3 unit-square grid has exactly $3$ 2-by-2 red squares
Assume the $3$ 2-by-2 red squares are at $C_{11}, C_{12}, C_{13}, C_{21}, C_{22}, C_{23}, C_{32}, C_{33}$ . To make sure there are no more 2-by-2 red squares, $C_{33}$ can't be red. Meaning that there is $1$ coloring method for $C_{33}$ . For exactly $3$ 2-by-2 red squares at $C_{11}, C_{12}, C_{13}, C_{21}, C_{22}, C_{23}, C_{32}, C_{33}$ , there is $1$ coloring method. As there are $4$ locations for the $3$ 2-by-2 red squares on the 3-by-3 unit-square grid, there are $1 \cdot 4 = 4$ coloring methods.
Case 4: The 3-by-3 unit-square grid has exactly $4$ 2-by-2 red squares
If the 3-by-3 unit-square grid has exactly $4$ 2-by-2 red squares, all $9$ unit grids are red and there is $1$ coloring method.
In total, there are $68+22+4+1=95$ coloring methods with 2-by-2 red squares. \[\frac{m}{n}=1-\frac{95}{2^9}=\frac{417}{512}\]
\[m+n=417+512=\boxed{\textbf{929}}\]
~ isabelchen
These problems are copyrighted © by the Mathematical Association of America.