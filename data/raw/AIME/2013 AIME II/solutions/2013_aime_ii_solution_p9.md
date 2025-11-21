# 2013 AIME II Problem 9

## Problem

A $7\times 1$ board is completely covered by $m\times 1$ tiles without overlap; each tile may cover any number of consecutive squares, and each tile lies completely on the board. Each tile is either red, blue, or green. Let $N$ be the number of tilings of the $7\times 1$ board in which all three colors are used at least once. For example, a $1\times 1$ red tile followed by a $2\times 1$ green tile, a $1\times 1$ green tile, a $2\times 1$ blue tile, and a $1\times 1$ green tile is a valid tiling. Note that if the $2\times 1$ blue tile is replaced by two $1\times 1$ blue tiles, this results in a different tiling. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
Firstly, we consider how many different ways possible to divide the $7\times 1$ board. We ignore the cases of 1 or 2 pieces since we need at least one tile of each color.
- Three pieces: $5+1+1$ , $4+2+1$ , $4+1+2$ , etc, $\dbinom{6}{2}=15$ ways in total (just apply stars and bars here)
- Four pieces: $\dbinom{6}{3}=20$
- Five pieces: $\dbinom{6}{4}=15$
- Six pieces: $\dbinom{6}{5}=6$
- Seven pieces: $\dbinom{6}{6}=1$
Secondly, we use Principle of Inclusion-Exclusion to consider how many ways to color them:
- Three pieces: $3^3-3\times 2^3+3=6$
- Four pieces: $3^4-3\times 2^4+3=36$
- Five pieces: $3^5-3\times 2^5+3=150$
- Six pieces: $3^6-3\times 2^6+3=540$
- Seven pieces: $3^7-3\times 2^7+3=1806$
Finally, we combine them together: $15\times 6+20\times 36+15\times 150+6\times 540+1\times 1806= 8106$ .
So the answer is $\boxed{106}$ .
### Explanation
In the $7*1$ tiling, when counting the ways to split this into $k$ pieces what you do is set the leftmost of the first tile and the rightmost of the last tile as borders.
Then if we select say $1$ vertical line from the remaining $6$ vertical lines, we would have split into $2$ pieces. Similarly if we select $k$ vertical lines from them $6$ , we would have $k+1$ pieces.
Furthermore, to count the number of countings of $k$ pieces you apply the Principle of Inclusion and Exclusion.
Done so by noticing that we have $3^k$ ways to color without any restricitons. Then, let's count the number of ways that we use atleast only $2$ colors and subtract off.
If we use atleast only $2$ colors, we have $3$ ways to pick these colors, and then $3*2^k$ ways to color the squares in. However, this overcounts the case where we used only one color, two times each.
Thus number of ways we use atleast only $2$ colors is $3*2^k-3$ .
Subtracting from total arrangements, we obtain $3^k-3*2^k+3$ .
~Bigbrain_2009

## Solution 1.1 (Faster/Streamlined 1)
This solution is basically solution 1 with more things done at once. The game plan:
$\sum_{i=0}^{7} ($ the amount of ways to divide the board into $i$ pieces $) \cdot ($ the amount of ways to color the respective divisions)
The amount of ways to divide the board is determined using stars and bars. The colorings are found using PIE giving $3^i-3\cdot2^i+3$ . Plus, we don't have to worry about the cases where $i=1$ or $i=2$ since they both give no solutions. So our equation becomes:
$\sum_{i=3}^{7} \left(\dbinom{6}{i}\right)\cdot\left(3^i-3\cdot2^i+3\right)$
Writing it all out and keeping the numbers small with mod 1000, we will eventually arrive at the answer of $\boxed{106}$ .
~Rowechen Zhong

## Solution 2 (Recursive)
3 colors is a lot. How many ways can we tile an $n \times 1$ board with one color? It's going to be $2^{n-1}$ because if you draw out the $n$ spaces, you can decide whether each of the borders between the tiles are either there or not there. There are $n-1$ borders so there are $2^{n-1}$ tilings. Define a one-tiling of an mx1 as $f_1(m)$
Now let's look at two colors. Let's see if we can get a two-tiling of an $(n+1) \times 1$ based off a $n \times 1$ . There are 2 cases we should consider:
1) The $n \times 1$ was a one-coloring and the block we are going to add consists of the second color. The number of ways we can do this is $2f_1(n)$
2) The $n \times 1$ was a two-color tiling so now we've got 3 cases to form the $(n+1) \times 1$ : We can either add a block of the first color, the second color, or we can adjoin a block to the last block in the $n \times 1$ .
This gives us $f_2(n+1)=2f_1(n)+3f_2(n)$
Time to tackle the 3-color tiling. Again, we split into 2 cases:
1) The $n \times 1$ was a two-color tiling, and the block we are adding is of the 3rd color. This gives $f_2(n)$ ways but we have to multiply by $3C2 = 3$ because we have to pick 2 different colors for the two-color tiling.
2) The $n \times 1$ was a 3-color tiling, and we have to consider what we can do with the block that we are adding. It can be any of the 3 colors, or we can adjoin it to whatever was the last block in the $n \times 1$ . This gives $4f_3(n)$
So in total we have $f_3(n+1)=3f_2(n)+4f_3(n)$ .
Finally, we just sorta bash through the computation to get $f_3(7)=8\boxed{106}$

## Solution 3
Let $n$ be the length of the board and $x$ be the number of colors. We will find the number of ways to tile the $n \times 1$ board with no color restrictions (some colors may be unused) and then use PIE.
By stars and bars, the number of ways to divide the board into $k$ pieces is ${n-1 \choose k-1}$ . There are $x^k$ ways to color each of these divisions. Therefore, the total number of ways to divide and color the board is \begin{align*} \chi(n, x) &:= \sum_{k=1}^n {n-1 \choose k-1} x^k \\ &= x\sum_{k=0}^{n-1} {n-1 \choose k} x^k \\ &= x(x+1)^{n-1}. \end{align*}
In the given problem, we have $n=7$ . By PIE, we have \begin{align*} &\quad {3 \choose 3} \chi(7, 3) - {3 \choose 2} \, \chi(7, 2) + {3 \choose 1} \, \chi(7, 1) \\ &= 3 \cdot 4^6 - 3(2 \cdot 3^6) + 3(1 \cdot 2^6) \\ &= 8106 \rightarrow \boxed{106}. \end{align*}
The above formula for $\chi(n, x)$ can also be derived directly as follows:
- The first square can be colored in one of $x$ ways.
- Proceeding left to right, at each of the remaining $n-1$ squares, we have $x+1$ options: ways to begin a new tile, selecting an arbitrary color. Note that this includes the case where we begin a new tile of the same color. way to expand the current tile by attaching a square of the current color.
- $x$ ways to begin a new tile, selecting an arbitrary color. Note that this includes the case where we begin a new tile of the same color.
- $1$ way to expand the current tile by attaching a square of the current color.
This results in $x(x+1)^{n-1}$ overall ways to divide and color the board (without the color use restriction).
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .