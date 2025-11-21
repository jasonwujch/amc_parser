# 2013 AMC 10A Problem 17

## Problem

Daphne is visited periodically by her three best friends: Alice, Beatrix, and Claire. Alice visits every third day, Beatrix visits every fourth day, and Claire visits every fifth day. All three friends visited Daphne yesterday. How many days of the next $365$ -day period will exactly two friends visit her?

$\textbf{(A)}\ 48\qquad\textbf{(B)}\ 54\qquad\textbf{(C)}\ 60\qquad\textbf{(D)}\ 66\qquad\textbf{(E)}\ 72$

## Solution 1
The $365$ -day time period can be split up into $6$ , $60$ -day time periods, because after $60$ days, all three of them visit again (Least common multiple of $3$ , $4$ , and $5$ ). You can find how many times each pair of visitors can meet by finding the LCM of their visiting days and dividing that number by 60. Remember to subtract $1$ , because you do not wish to count the $60$ th day, when all three visit.
A and B visit $\frac{60}{3 \cdot 4}-1 = 4$ times.
A and C visit $\frac{60}{3 \cdot 5}-1 = 3$ times.
B and C visit $\frac{60}{4 \cdot 5}-1 = 2$ times.
This is a total of $9$ visits per $60$ day period. Therefore, the total number of $2$ -person visits is $9 \cdot 6 = \boxed{\textbf{(B) }54}$ .
- Note: We do not have to worry about the numbers over 360: ( $361,362,363,364,365$ ) having 2 factors. This is because we can rewrite
$(361,362,363,364,365) \Rightarrow (361,362, 3\cdot 121, 4 \cdot 91, 5 \cdot 73)$ . We note that $121$ is not further divisible by 4 or 5, $91$ is not further divisible by 3 or 5, 73 is not further divisible by 3 or 4. Therefore, none of the numbers from $361-365$ have 2 factors of $3,4,$ or $5$ , so we can conclude that the answer is indeed $\boxed{54}$

## Solution 2
From the information above, we get that $A=3x$ $B=4x$ $C=5x$
Now, we want the days in which exactly two of these people meet up
The three pairs are $(A,B)$ , $(B,C)$ , $(A,C)$ .
Notice that we are trying to find the LCM of each pair.
Hence, $LCM(A,B)=12x$ , $LCM(B,C)=20x$ , $LCM(A,C)=15x$
Notice that we want to eliminate when all these friends meet up. By doing this, we will find the LCM of the three letters.
Hence, $LCM(A,B,C)=60x$
Now, we add all of the days up(including overcount).
We get $30+18+24=72$ . Now, because $60(6)=360$ , we have to subtract $6$ days from every pair. Hence, our answer is $72-18=\boxed{54}\implies\boxed{B}$ .
### Understanding the Problem, and why it is 54
Lets say Alice, Beatrix, Claire, and Daphne meet up on \( d=0 \).
Firstly, how many days does it take to get to our \( d=0 \)?
Well, that's simple!
If Alice meets Daphne every 3 days, Beatrix does so in 4, and Claire does so in 5, then they will all appear on each 60th day.
Similarly, we can break down the cases for two of Daphne's friends appearing!
If Alice meets Daphne every 3 days and Beatrix does so in 4, then both of them will appear on each 12th day.
If Alice meets Daphne every 3 days and Claire does so in 5, then both of them will appear on each 15th day.
If Beatrix meets Daphne every 4 days and Claire does so in 5, then both of them will appear on each 20th day.
Aha! That's it! We just need to find a common sequence between each of the days and just subtract the cases where they all appear!
We can make this a sequence! Let us have a sequence that shall end the moment they all hit 60!
Letting our sequences be \( S(A \text{ and } B) \), \( S (B \text{ and } C) \), and \( S(A \text{ and } C) \), we get
\[S(A \text{ and } C) = \{0, 12, 24, 36, 48, 60\}\]
\[S(B \text{ and } C) = \{0, 20, 40, 60\}\]
\[S(A \text{ and } C) = \{0, 15, 30, 45, 60\}\]
The 0's are unnecessary, so we get rid of them. We now count how many UNIQUE days are in each set and sum it up.
\( S(A \text{ and } C) = 4 \)
\( S(B \text{ and } C) = 2 \)
\( S(A \text{ and } C) = 3 \)
This gives us 9 unique cases. This process happens 6 times. So we get \( 6*9=\) $\boxed{54 \Rightarrow (B)}$ total days in the 360 day period.
I hope this made things more clear :-)!
~Pinotation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .