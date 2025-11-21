# 2012 AIME I Problem 4

## Problem

Butch and Sundance need to get out of Dodge. To travel as quickly as possible, each alternates walking and riding their only horse, Sparky, as follows. Butch begins by walking while Sundance rides. When Sundance reaches the first of the hitching posts that are conveniently located at one-mile intervals along their route, he ties Sparky to the post and begins walking. When Butch reaches Sparky, he rides until he passes Sundance, then leaves Sparky at the next hitching post and resumes walking, and they continue in this manner. Sparky, Butch, and Sundance walk at $6,$ $4,$ and $2.5$ miles per hour, respectively. The first time Butch and Sundance meet at a milepost, they are $n$ miles from Dodge, and they have been traveling for $t$ minutes. Find $n + t$ .

## Solution
When they meet at the milepost, Sparky has been ridden for $n$ miles total. Assume Butch rides Sparky for $a$ miles, and Sundance rides for $n-a$ miles. Thus, we can set up an equation, given that Sparky takes $\frac{1}{6}$ hours per mile, Butch takes $\frac{1}{4}$ hours per mile, and Sundance takes $\frac{2}{5}$ hours per mile:
\[\frac{a}{6} + \frac{n-a}{4} = \frac{n-a}{6} + \frac{2a}{5} \rightarrow a = \frac{5}{19}n.\]
The smallest possible integral value of $n$ is $19$ , so we plug in $n = 19$ and $a = 5$ and get $t = \frac{13}{3}$ hours, or $260$ minutes. So our answer is $19 + 260 = \boxed{279}$ .
Note that this solution is not rigorous because it is not guaranteed that they will switch properly to form this combination.

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/332
~ dolphin7
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .