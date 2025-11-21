# 2005 AIME I Problem 4

## Problem

The director of a marching band wishes to place the members into a formation that includes all of them and has no unfilled positions. If they are arranged in a square formation, there are 5 members left over. The director realizes that if he arranges the group in a formation with 7 more rows than columns, there are no members left over. Find the maximum number of members this band can have.

## Solution

## Solution 1
If $n > 14$ then $n^2 + 6n + 14 < n^2 + 7n < n^2 + 8n + 21$ and so $(n + 3)^2 + 5 < n(n + 7) < (n + 4)^2 + 5$ . If $n$ is an integer there are no numbers which are 5 more than a perfect square strictly between $(n + 3)^2 + 5$ and $(n + 4)^2 + 5$ . Thus, if the number of columns is $n$ , the number of students is $n(n + 7)$ which must be 5 more than a perfect square, so $n \leq 14$ . In fact, when $n = 14$ we have $n(n + 7) = 14\cdot 21 = 294 = 17^2 + 5$ , so this number works and no larger number can. Thus, the answer is $\boxed{294}$ .

## Solution 2
Define the number of rows/columns of the square formation as $s$ , and the number of rows of the rectangular formation $r$ (so there are $r - 7$ columns). Thus, $s^2 + 5 = r(r-7) \Longrightarrow r^2 - 7r - s^2 - 5 = 0$ . The quadratic formula yields $r = \frac{7 \pm \sqrt{49 - 4(1)(-s^2 - 5)}}{2} = \frac{7 \pm \sqrt{4s^2 + 69}}{2}$ . $\sqrt{4s^2 + 69}$ must be an integer , say $x$ . Then $4s^2 + 69 = x^2$ and $(x + 2s)(x - 2s) = 69$ . The factors of $69$ are $(1,69), (3,23)$ ; $x$ is maximized for the first case. Thus, $x = \frac{69 + 1}{2} = 35$ , and $r = \frac{7 \pm 35}{2} = 21, -14$ . The latter obviously can be discarded, so there are $21$ rows and $21 - 7 = 14$ columns, making the answer $294$ .

## Solution 3
The number of members is $m^2+5=n(n+7)$ for some $n$ and $m$ . Multiply both sides by $4$ and complete the square to get $4m^2+69=(2n+7)^2$ . Thus, we have $69=((2n+7)+2m)((2n+7)-2m)$ . Since we want to maximize $n$ , set the first factor equal to $69$ and the second equal to $1$ . Now we have the systems of equations \[2n+2m+7 = 69\] \[2n-2m+7 = 1\] Adding these two equations gives us $4n+14=70$ which means $4n=56$ so $n=14$ . Thus, the answer is $14\cdot21=294$ . $\square$
~lpieleanu

## Solution 4
Partially completing the square
Geometrically: Split up the formation of $n + 7$ rows and $n$ columns into a square of $n$ rows and $n$ columns and a separate rectangle of the dimensions $7$ rows by $n$ columns. We want to take the rows from the rectangle and add them to the square to get another square and $5$ left over. If we attach exactly $2$ rows on the top and exactly $2$ rows on the side of the $n$ x $n$ square, then we have an $(n + 2)$ x $(n + 2)$ square that's missing a $2$ x $2$ corner. For the remaining $3n$ to fill this square plus the $5$ extra members, $n$ must be $3$ . If we instead plaster exactly $3$ rows from the $7$ x $n$ formation to two adjacent sides of the $n$ x $n$ square, we have an $(n + 3)$ x $(n + 3)$ formation that's missing a $3$ x $3$ corner. For the remaining row of length $n$ to fill this plus five, $n = 14$ . Plugging these in, we find $n = 14$ has a much higher count of members: $(n + 7)n; n = 14 --> 21(14) = 294$
Algebraically: We have $n^2 + 7n = m$ , where $m$ is the number of members in the band and $n$ is a positive integer. We partially complete the square for $n$ to get $n^2 + 7n = (n + 1)^2 + 5n - 1 = (n + 2)^2 + 3n - 4 = (n + 3)^2 + n - 9$ Our goal is to get $n^2 + 7n = y^2 + 5$ because we want $m$ to be $5$ more than a perfect square. From the above, $5n - 1 = 5$ means $n$ isn't an integer, $3n - 4 = 5$ means that $n = 3$ , and $n - 9 = 5$ means that $n = 14$ . Out of these, $n = 14$ is associated with the highest number of members in the band, so $m = (14^2) + 7(14) = 294$

## Solution 5
Let there be $m$ members and $n$ members for the square and $c$ for the number of columns of the other formation. We have $n^2 +5 = c(c+7) \implies n^2+5 = \left(c+\frac{7}{2}\right)^2 -\frac{49}{4} \implies n^2 - \left(c+\frac{7}{2}\right)^2 = -\frac{69}{4} \implies \left(n-c-\frac{7}{2}\right)\left(n + c +\frac{7}{2}\right) \implies (2n-2c-7)(2n+2n+7) = -69.$
To maximize this we let $2n+2c+7 = 69$ and $2n-2c-7 = -1.$ Solving we find $n = 17$ so the desired number of members is $17^2 + 5 = \boxed{294}.$

## Solution 6 (NO ALGEBRA)
Think of the process of moving people from the last column to new rows. Since there are less columns than rows, for each column removed, there are people discarded to the "extra" pile to be placed at the end. To maximize the number of "extra" people to fill in the last few rows. We remove 3 columns and add 4 rows. For the first new row, one more person will be discarded. For the second, 1 extra person are added since there is one more row now, and there are 2 less columns. Thus, there are 3 extra people discarded. Similarly, 5 extra people are discarded for the third column. Now there are $5+1+3+5=14$ people in the extra pile to put as the last row, so there are $14(14+7)=\boxed{294}$ people.
~ CELLSecret

## Solution 7 (Bash-not advisable)
Note: Only do this if you have a LOT of time (and you've memorized all your perfect squares up to 1000).
We can see that the number of members in the band must be of the form $n(n + 7)$ for some positive integer $n$ . When $n = 28$ , this product is $980$ , and since AIME answers are nonnegative integers less than $1000$ , we don't have to check any higher $n$ . Also, we know that this product must be 5 more than a perfect square, so we can make a table as shown and bash: \[\begin{tabular}{|c|c|c|} n & n(n+7) & 5 more than a perfect square?\\ \hline 1 & 8 & no\\ \hline 2 & 18 & no\\ \hline 3 & 30 & yes\\ \hline 4 & 44 & no\\ \hline 5 & 60 & no\\ \hline 6 & 78 & no\\ \hline 7 & 98 & no\\ \hline 8 & 120 & no\\ \hline 9 & 144 & no\\ \hline 10 & 170 & no\\ \hline 11 & 198 & no\\ \hline 12 & 228 & no\\ \hline 13 & 260 & no\\ \hline 14 & 294 & yes\\ \hline 15 & 330 & no\\ \hline 16 & 368 & no\\ \hline 17 & 408 & no\\ \hline 18 & 450 & no\\ \hline 19 & 494 & no\\ \hline 20 & 540 & no\\ \hline 21 & 588 & no\\ \hline 22 & 638 & no\\ \hline 23 & 690 & no\\ \hline 24 & 744 & no\\ \hline 25 & 800 & no\\ \hline 26 & 858 & no\\ \hline 27 & 918 & no\\ \hline 28 & 980 & no\\ \hline \end{tabular}\] Thus, we can see that our largest valid $n(n+7)$ is $\boxed{294}$ .
~lpieleanu (Minor reformatting and editing)
These problems are copyrighted © by the Mathematical Association of America.