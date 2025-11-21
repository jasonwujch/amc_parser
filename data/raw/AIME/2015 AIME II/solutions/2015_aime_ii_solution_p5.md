# 2015 AIME II Problem 5

## Problem

Two unit squares are selected at random without replacement from an $n \times n$ grid of unit squares. Find the least positive integer $n$ such that the probability that the two selected unit squares are horizontally or vertically adjacent is less than $\frac{1}{2015}$ .

## Solution 1
Call the given grid "Grid A". Consider Grid B, where the vertices of Grid B fall in the centers of the squares of Grid A; thus, Grid B has dimensions $(n-1) \times (n-1)$ . There is a one-to-one correspondence between the edges of Grid B and the number of adjacent pairs of unit squares in Grid A. The number of edges in Grid B is $2n(n-1)$ , and the number of ways to pick two squares out of Grid A is $\dbinom{n^2}{2}$ . So, the probability that the two chosen squares are adjacent is $\frac{2n(n-1)}{\binom{n^2}{2}} = \frac{2n(n-1)}{\frac{n^2(n^2-1)}{2}} = \frac{4}{n(n+1)}$ . We wish to find the smallest positive integer $n$ such that $\frac{4}{n(n+1)} < \frac{1}{2015}$ , and by inspection the first such $n$ is $\boxed{090}$ .

## Solution 2
Consider a $3 \times 3$ grid, where there are $4$ corner squares, $4$ edge squares, and $1$ center square. A $4 \times 4$ grid has $4$ corner squares, $8$ edge squares, and $4$ center squares. By examining simple cases, we can conclude that for a grid that is $n \times n$ , there are always $4$ corners squares, $4(n-2)$ edge squares, and $n^2-4n+4$ center squares.
Each corner square is adjacent to $2$ other squares, edge squares to $3$ other squares, and center squares to $4$ other squares. In the problem, the second square can be any square that is not the first, which means there are $n^2-1$ to choose from. With this information, we can conclude that the probability that second unit square is adjacent to the first is $\frac{2}{n^2-1}(\frac{4}{n^2}) +\frac{3}{n^2-1}(\frac{4(n-2)}{n^2}) +\frac{4}{n^2-1}(\frac{n^2-4n+4}{n^2})$ .
Simplifying, we get $\frac{4}{n(n+1)}$ which we can set to be less than $\frac{1}{2015}$ . By inspection, we find that the first such $n$ is $\boxed{090}$ .

## Solution 3
There are 3 cases in this problem. Number one, the center squares. Two, the edges, and three, the corners. The probability of getting one center square and an adjacent square is $\frac{(n-2)(n-2)}{n^2}$ multiplied by $\frac{4}{n^2 -1}$ . Add that to the probability of an edge and an adjacent square( $\frac{4n-8}{n^2}$ multiplied by $\frac{3}{n^2-1}$ ) and the probability of a corner and an adjacent square( $\frac{4}{n^2}$ multiplied by $\frac{2}{n^2-1}$ ) to get $\frac{4n^2-4n}{n^4-n^2}$ . Simplify to get $\frac{4}{n^2+n}$ . With some experimentation, we realize that the smallest value of n is $\boxed{090}$ .

## Solution 4 (cheese)
Notice how a chosen unit square on the grid has 4 vertically & horizontally adjacent squares around it (not counting corners or sides.) That's $\frac{4}{n^2}$ . Using this, we rewrite $\frac{1}{2015}$ as $\frac{4}{8060}$ . Notice that the denominator $8060$ is really close to $90^2$ , and the problem is asking for the least positive integer less than $\frac{1}{2015}$ . Therefore, the closest possible estimation is $\boxed{090}$ . We can check this by adding in our corners and sides. Easy multiplication and simplification finds us with $\boxed{090}$ as the correct answer.
~ orenbad

## Solution 5
Lets start with some simpler cases. For example, lets use a 2x2. We have $2$ horizontally and $2$ vertically, for a total of $4$ . Then, our possible outcomes is just $\binom{4}{2}$ , so our probability is just $\dfrac{2}{3}$ . Now, lets do a 3x3. We have that there are $6$ horizontally and $6$ vertically, for a total of $12$ . Our possible outcomes is just $\binom{9}{2} = 36$ . Now, our probability is just $\dfrac{1}{3}$ . Now, lets try to generalize. For each colum, there is $n-1$ ways, then we multiply that by $n$ for our $n$ columns. Then we multiply all that by $2$ for the rows to get $2n(n-1)$ . For our denominator, we have $n^2$ squares, and we need to choose $2$ of them, so our probability is: \[\dfrac{2n(n-1)}{\binom{n^2}{2}}\] . Lets simplify this. We have: \[\dfrac{2n(n-1)}{\dfrac{n^2(n^2-1)}{2}} \Longrightarrow \dfrac{4}{n(n+1)}\] . So, we have this to be less than $\dfrac{1}{2015}$ . So we have: \[\dfrac{4}{n(n+1)} < \dfrac{1}{2015} \Longrightarrow n(n+1) > 8060\] , so the smallest $n$ that satisfies this condition is $n = \boxed{090}$
-jb2015007

## Video Solution
https://www.youtube.com/watch?v=9re2qLzOKWk&t=304s
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .