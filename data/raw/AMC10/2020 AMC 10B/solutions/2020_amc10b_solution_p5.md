# 2020 AMC 10B Problem 5

## Problem

How many distinguishable arrangements are there of $1$ brown tile, $1$ purple tile, $2$ green tiles, and $3$ yellow tiles in a row from left to right? (Tiles of the same color are indistinguishable.)

$\textbf{(A)}\ 210 \qquad\textbf{(B)}\ 420 \qquad\textbf{(C)}\ 630 \qquad\textbf{(D)}\ 840 \qquad\textbf{(E)}\ 1050$

## Solution 1
Let's first find how many possibilities there would be if they were all distinguishable, then divide out the ones we overcounted.
There are $7!$ ways to order $7$ objects. However, since there's $3!=6$ ways to switch the yellow tiles around without changing anything (since they're indistinguishable) and $2!=2$ ways to order the green tiles, we have to divide out these possibilities: $\frac{7!}{3! \cdot2}=\boxed{\textbf{(B) }420}$ .
~quacker88

## Solution 2
There are $7$ choose $3$ ways to arrange the yellow tiles which is $35$ . Then from the remaining tiles there are $\binom{4}{2}=6$ ways to arrange the green tiles. And now from the remaining two tiles and two slots we can see there are two ways to arrange the purple and brown tiles, giving us an answer of $35\cdot6\cdot2=420$ .
~noahdavid (Edited by starshooter11)

## Solution 3
We can choose a different frame to solve this problem. Our tile combination can be written as $Y, Y, Y, G, G, B, P.$ We can focus on $Y, Y, Y, G, G$ first, which gives us $\binom{5}{3}=10.$ Now we can insert our brown tile into this which only has $6$ choices(like $Y,B, Y, Y, G, G$ and $Y, Y, Y, G, G, B$ etc.), then insert purple tile which only has $7$ choices(like $B,Y, P, Y, Y, G, G$ and $B, Y, Y, Y, G, G, P$ etc.). Multiply them together we get $10\cdot 6\cdot 7=\boxed{\textbf{(B)}\ 420}$ .
~@azure123456 BZ

## Solution 4 (Concise)
Let $B$ be brown, $P$ be purple, $G$ be green, and $Y$ be yellow. Then, we are just ordering $Y$ , $Y$ , $Y$ , $G$ , $G$ , $B$ , and $P$ . Hence, $\frac{7!}{3! \cdot 2!} = \boxed{\textbf{(B)}\ 420}$ .
~MrThinker

## Solution 5 (Reverse Order)
There are $1 + 1 + 2 + 3 = 7$ ways you can arrange the brown tile, $1 + 2 + 3 = 6$ ways you can arrange the purple tile, $\binom{5}{2} = 10$ ways to arrange the green tiles, and only 1 possible arrangement of the yellow tiles after all of this. Therefore, $7 * 6 * 10 * 1 = \boxed{\textbf{(B)}\ 420}$ .
~ RealJohnMantle

## Video Solution (HOW TO CRITICALLY THINK!!!)
https://youtu.be/SQ8XRpl2gXE
~Education, the Study of Everything

## Video Solution
https://youtu.be/0W3VmFp55cM?t=540

## Video Solution 2
https://youtu.be/Gkm5rU5MlOU

## Video Solution 3
https://youtu.be/4vz8IPfzs2c
~savannahsolver

## Video Solution 4
https://youtu.be/waxVSOt_v1M?t=275
~ AMBRIGGS
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .