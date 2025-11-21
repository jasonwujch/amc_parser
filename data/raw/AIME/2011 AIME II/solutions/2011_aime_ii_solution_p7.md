# 2011 AIME II Problem 7

## Problem

Ed has five identical green marbles, and a large supply of identical red marbles. He arranges the green marbles and some of the red ones in a row and finds that the number of marbles whose right hand neighbor is the same color as themselves is equal to the number of marbles whose right hand neighbor is the other color. An example of such an arrangement is GGRRRGGRG. Let $m$ be the maximum number of red marbles for which such an arrangement is possible, and let $N$ be the number of ways he can arrange the $m+5$ marbles to satisfy the requirement. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
We are limited by the number of marbles whose right hand neighbor is not the same color as the marble. By surrounding every green marble with red marbles - RGRGRGRGRGR. That's 10 "not the same colors" and 0 "same colors." Now, for every red marble we add, we will add one "same color" pair and keep all 10 "not the same color" pairs. It follows that we can add 10 more red marbles for a total of $m = 16$ . We can place those ten marbles in any of 6 "boxes": To the left of the first green marble, to the right of the first but left of the second, etc. up until to the right of the last. This is a stars-and-bars problem, the solution of which can be found as $\binom{n+k}{k}$ where n is the number of stars and k is the number of bars. There are 10 stars (The unassigned Rs, since each "box" must contain at least one, are not counted here) and 5 "bars," the green marbles. So the answer is $\binom{15}{5} = 3003$ , take the remainder when divided by 1000 to get the answer: $\boxed{003}$ .
Rewording:
There are three states for every marble: the one to the right is different, the one to the right is the same, and there is no marble to its right. Since there are unlimited red marbles, the second value can be created infinitely and is therefore worthless. However, the first value can only be created with a combination green marbles, thus finite, and worthy of our interest. As such, to maximize the amount of red marbles, we need to maximize the appearances of the first value. The "minimal" of this strategy is to simply separate every green marble with a red - RGRGRGRGRGR. There are ten appearances of the first value, so we must add a number of red marbles to add appearances of the second value. With quick testing we can conclude the need of nine new red marbles that can be placed in six defined places that are divided by the green marbles. This is followed by stars and bars which gives us $\binom{15}{5} = 3003$ , $\boxed{003}$ .
-jackshi2006

## Solution 2
Begin with the above solution's reasoning to find that the ideal sequence is RGRGRGRGRGR + 10 Rs. To count the number of arrangements where the Gs are separate, group a G and an R together (GR) which will be rearranged/counted as one. However this also introduces the case of having GRGR.... which results in too few number of marbles whose right-hand neighbor is different, so we fix an R in the beginning of our sequence which also removes it from our counting calculation. Finally we are looking at the arrangement of 5 (GR)s + 10 Rs, all indistinguishable, which is $\frac{15!}{5!10!}=3003\Longrightarrow\boxed{003}$ .
~clarkculus

## Solution 3
Let a collection of consecutive letters be a "blob." Let there be n blobs.
The marbles such that the marble to their right has a different color are the ones that are the last marble of a "blob." The only exception to this is the very last marble in this list. There are \( n-1 \) of these.
The marbles such that the marble to their right has the same color are any marbles which are not at the end of a blob. The only exception to this is the last marble, which does not go in any category.
The problem states that the number of marbles like this is equal to the number of marbles with a different color. Therefore, there are \( (n-1) + (n-1) + 1 \) marbles in total (the last \( +1 \) is for the last marble at the end). We know there are \( m+5 \) marbles, so \( m+5 = 2n-1 \).
Solving for \( n \), we get \( n = \frac{m}{2} + 3 \).
Notice that \( n \leq 11 \) because the "best-case scenario" is that each \( G \) forms its own blob, and there is a red blob in between any two \( G \)'s and a red blob on both ends. Here is how it should look:
<red blob> G <red blob> G <red blob> G <red blob> G <red blob> G <red blob>.
In this case, there are \( 11 \) blobs.
Thus, \( \frac{m}{2} + 3 \leq 11 \implies m \leq 16 \).
This is now a stars and bars problem. For \( m = 16 \), we need to create the optimal solution: \( 11 \) blobs. Since every <red blob> must have at least one red marble, we can just give each blob one red at the start, leaving us with \( 16-6 = 10 \) red marbles left to separate into \( 6 \) groups. By stars and bars, this is \( \binom{15}{5} = 3003 \).
Thus, the answer is \( \boxed{003} \).

## Solution 4 (VERY SIMILAR TO 3)
Let a collection of consecutive letters be a "blob." Let the blobs have sizes s_1, s_2, ... s_n given the existence of n blobs.
The marbles such that the marble to their right has a different color are the ones that are the last marble of a "blob." The only exception to this is the very last marble in this list. There are \( n-1 \) of these.
The marbles such that the marble to their right has the same color is every marble in a blob but the last, which is \[\sum_{i=1}^{n} (s_i - 1) = \left(\sum_{i=1}^{n} s_i\right) - n = m + 5 - n.\]
Equating our two expression $n-1 = m+5-n \rightarrow 2n=m+6.$
Solving for \( n \), we get \( n = \frac{m}{2} + 3 \).
Notice that \( n \leq 11 \) because the "best-case scenario" is that each \( G \) forms its own blob, and there is a red blob in between any two \( G \)'s and a red blob on both ends. Here is how it should look:
<red blob> G <red blob> G <red blob> G <red blob> G <red blob> G <red blob>.
In this case, there are \( 11 \) blobs.
Thus, \( \frac{m}{2} + 3 \leq 11 \implies m \leq 16 \).
This is now a stars and bars problem. For \( m = 16 \), we need to create the optimal solution: \( 11 \) blobs. Since every <red blob> must have at least one red marble, we can just give each blob one red at the start, leaving us with \( 16-6 = 10 \) red marbles left to separate into \( 6 \) groups. By stars and bars, this is \( \binom{15}{5} = 3003 \).
Thus, the answer is \( \boxed{003} \).
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .