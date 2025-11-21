# 2010 AIME II Problem 11

## Problem

Define a T-grid to be a $3\times3$ matrix which satisfies the following two properties:

1. Exactly five of the entries are $1$ 's, and the remaining four entries are $0$ 's.

1. Among the eight rows, columns, and long diagonals (the long diagonals are $\{a_{13},a_{22},a_{31}\}$ and $\{a_{11},a_{22},a_{33}\}$ , no more than one of the eight has all three entries equal.

Find the number of distinct T-grids .

## Solution

## Solution 1
The T-grid can be considered as a tic-tac-toe board: five $1$ 's (or X's) and four $0$ 's (or O's).
There are only $\dbinom{9}{5} = 126$ ways to fill the board with five $1$ 's and four $0$ 's. Now we just need to subtract the number of bad grids. Bad grids are ones with more than one person winning, or where someone has won twice.
Let three-in-a-row/column/diagonal be a "win" and let player $0$ be the one that fills in $0$ and player $1$ fills in $1$ .
Case : Each player wins once.
If player X takes a diagonal, player Y cannot win. If either takes a row, all the columns are blocked, and visa versa. Therefore, they either both take a row or they both take a column.
1. Both take a row: There are ways for player to pick a row, ways for player to pick a row and, ways for player to take a single box in the remaining row. Therefore, there are cases.
1. Both take a column: Using similar reasoning, there are $18$ cases.
- There are $3$ ways for player $1$ to pick a row,
- $2$ ways for player $0$ to pick a row and,
- $3$ ways for player $0$ to take a single box in the remaining row.
Therefore, there are $3 \cdot 2 \cdot 3=18$ cases.
Case $1$ : $36$ cases
Case : Player $1$ wins twice. (Player $0$ cannot win twice because he only has 4 moves.)
1. Player $1$ picks a row and a column. There are ways to pick the row and ways to pick the column. So there are cases.
1. Player $1$ picks a row/column and a diagonal. There are ways to pick the row/column and to pick the diagonal, so there are cases
1. 2 diagonals It is clear that there is only case. (Make a X).
- There are $3$ ways to pick the row
- and $3$ ways to pick the column.
- There are $6$ ways to pick the row/column
- and $2$ to pick the diagonal,
so there are $12$ cases
- It is clear that there is only $1$ case. (Make a X).
Case $2$ total: $22$
Thus, the answer is $126-22-36=\boxed{68}$

## Solution 2
We can use generating functions to compute the case that no row or column is completely filled with $1$ 's. Given a row, let $a$ , $b$ , $c$ be the events that the first, second, third respective squares are $1$ 's. Then the generating function representing the possible events that exclude a row of $1,1,1$ or $0,0,0$ from occuring is \[ab+bc+ca+a+b+c.\] Therefore, the generating function representing the possible grids where no row is filled with $0$ 's and $1$ 's is \[P(a,b,c)=((ab+bc+ca)+(a+b+c))^3.\] We expand this by the Binomial Theorem to find \[P(a,b,c)=(ab+bc+ca)^3+3(ab+bc+ca)^2(a+b+c)+3(ab+bc+ca)(a+b+c)^2+(a+b+c)^3.\] Recall that our grid has five $1$ 's, hence we only want terms where the sum of the exponents is $5$ . This is given by \[3(ab+bc+ca)^2(a+b+c).\] When we expand this, we find \[3(2abc(a+b+c)+a^2b^2+b^2c^2+c^2a^2)(a+b+c).\] We also want to make sure that each of $a$ , $b$ , $c$ appears at least once (so there is no column filled with $0$ 's) and the power of each of $a$ , $b$ , $c$ is not greater than or equal to $3$ (so there is no column filled with $1$ 's). The sum of the coefficients of the above polynomial is clearly $81$ (using $a,b,c=1$ ), and the sum of the coefficients of the terms $a^3bc$ , $ab^3c$ , and $abc^3$ is $6+6+6+3+3+3+3+3+3=36$ , hence the sum of the coefficients of the desired terms is $81-36=45$ . This counts the number of grids where no column or row is filled with $0$ 's or $1$ 's. However, we could potentially have both diagonals filled with $1$ 's, but this is the only exception to our $45$ possibilities, hence the number of $T$ -grids with no row or column filled with the same digit is $44$ .
On the other hand, if a row (column) is filled with $0$ 's, then by the Pigeonhole Principle, another row (column) must be filled with $1$ 's. Hence this is impossible, so all other possible $T$ -grids have a row (column) filled with $1$ 's. If the top row is filled with $1$ 's, then we have two $1$ 's left to place. Clearly they cannot go in the same row, because then the other row is filled with $0$ 's. They also cannot appear in the same column. This leaves $3\cdot 2$ arrangements--3 choices for the location of the $1$ in the second row, and 2 choices for the location of the $1$ in the last row. However, two of these arrangements will fill a diagonal with $1$ 's. Hence there are only $4$ $T$ -grids where the top row is filled with $1$ 's. The same argument applies if any other row or column is filled with $1$ 's. Hence there are $4\cdot 6=24$ such $T$ -grids.
Thus the answer is $44+24=\boxed{68}$ .

## Solution 3
We proceed by complimentary counting.
There are $\binom{9}{5} = 126$ ways to fill the board with five $1$ 's and four $0$ 's. We subtract the cases where at least two of the eight rows, columns, and long diagonals have all three entries equal. For the sake of simplicity, let a line denote a row/column/diagonal.
Firstly, observe that there can be at most one line of $0$ 's and at most two lines of $1$ 's. Also, if there is one line of $0$ 's, there can at most be one line of $1$ 's. Therefore, there are only two "bad" cases we must consider:
Case : There is one line of $0$ 's and one line of $1$ 's.
In this case, note that both lines must be horizontal or vertical. If both are horizontal, there are $3 \cdot 2 = 6$ ways to select the columns, and $\binom{3}{1} = 3$ ways to place the remaining $0$ in the remaining $3$ grids, yielding a total of $6 \cdot 3 = 18$ bad cases. Similarly, there are $18$ bad cases where both lines are vertical, so $18 + 18 = 36$ cases.
Case : There are two lines of $1$ 's.
In this case, note that all five $1$ 's are used, and the two lines can be horizontal/vertical, horizontal/diagonal, vertical/diagonal, or diagonal/diagonal, yielding $3 \cdot 3 = 9$ , $3 \cdot 2 = 6$ , $3 \cdot 2 = 6$ , and $1$ case, respectively. $9 + 6 + 6 + 1 = 22$ cases.
Hence, the answer is $126 - 36 - 22 = \boxed{068}$ .
--OZ30
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .