# 2019 AIME I Problem 4

## Problem

A soccer team has $22$ available players. A fixed set of $11$ players starts the game, while the other $11$ are available as substitutes. During the game, the coach may make as many as $3$ substitutions, where any one of the $11$ players in the game is replaced by one of the substitutes. No player removed from the game may reenter the game, although a substitute entering the game may be replaced later. No two substitutions can happen at the same time. The players involved and the order of the substitutions matter. Let $n$ be the number of ways the coach can make substitutions during the game (including the possibility of making no substitutions). Find the remainder when $n$ is divided by $1000$ .

## Solution 1 (Recursion)
There are $0-3$ substitutions. The number of ways to sub any number of times must be multiplied by the previous number. This is defined recursively. The case for $0$ subs is $1$ , and the ways to reorganize after $n$ subs is the product of the number of new subs ( $12-n$ ) and the players that can be ejected ( $11$ ). The formula for $n$ subs is then $a_n=11(12-n)a_{n-1}$ with $a_0=1$ .
Summing from $0$ to $3$ gives $1+11^2+11^{3}\cdot 10+11^{4}\cdot 10\cdot 9$ . Notice that $10+9\cdot11\cdot10=10+990=1000$ . Then, rearrange it into $1+11^2+11^3\cdot (10+11\cdot10\cdot9)= 1+11^2+11^3\cdot (1000)$ . When taking modulo $1000$ , the last term goes away. What is left is $1+11^2=\boxed{122}$ .
~BJHHar

## Solution 2 (Casework)
We can perform casework. Call the substitution area the "bench".
$\textbf{Case 1}$ : No substitutions. There is $1$ way of doing this: leaving everybody on the field.
$\textbf{Case 2}$ : One substitution. Choose one player on the field to sub out, and one player on the bench. This corresponds to $11\cdot 11 = 121$ .
$\textbf{Case 3}$ : Two substitutions. Choose one player on the field to sub out, and one player on the bench. Once again, this is $11\cdot 11$ . Now choose one more player on the field to sub out and one player on the bench that was not the original player subbed out. This gives us a total of $11\cdot 11\cdot 11\cdot 10 = 13310\equiv 310 \bmod{1000}$ .
$\textbf{Case 4}$ : Three substitutions. Using similar logic as $\textbf{Case 3}$ , we get $(11\cdot 11)\cdot (11\cdot 10)\cdot (11\cdot 9)$ . The resulting number ends in $690$ .
Therefore, the answer is $1 + 121 + 310 + 690 \equiv \boxed{122} \pmod{1000}$ .
~minor mistake fixed by Prism Melody

## Solution 3 (Official MAA)
There is $1$ way of making no substitutions to the starting lineup. If the coach makes exactly one substitution, this can be done in $11^2$ ways. Two substitutions can happen in $11^2\cdot11\cdot 10$ ways. Similarly, three substitutions can happen $11^2\cdot11\cdot10\cdot11\cdot9$ ways. The total number of possibilities is $1+11^2+11^2\cdot11\cdot10+11^2\cdot11\cdot10\cdot11\cdot9=122+11^3(10+990)\equiv 122\pmod{1000}.$

## Video Solution #1(A bit of casework, a bit of counting)
https://youtu.be/JQdad7APQG8?t=981

## Video Solution
https://youtu.be/I-8xZGhoDUY
~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .