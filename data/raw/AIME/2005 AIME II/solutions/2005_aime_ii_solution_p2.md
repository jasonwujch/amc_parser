# 2005 AIME II Problem 2

## Problem

A hotel packed breakfast for each of three guests. Each breakfast should have consisted of three types of rolls, one each of nut, cheese, and fruit rolls. The preparer wrapped each of the nine rolls and once wrapped, the rolls were indistinguishable from one another. She then randomly put three rolls in a bag for each of the guests. Given that the probability each guest got one roll of each type is $\frac mn,$ where $m$ and $n$ are relatively prime integers , find $m+n.$

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3

- 3 Solution 4

- 4 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

## Solution

## Solution 1
Use construction . We need only calculate the probability the first and second person all get a roll of each type, since then the rolls for the third person are determined.
- Person 1: $\frac{9 \cdot 6 \cdot 3}{9 \cdot 8 \cdot 7} = \frac{9}{28}$
- Person 2: $\frac{6 \cdot 4 \cdot 2}{6 \cdot 5 \cdot 4} = \frac 25$
- Person 3: One roll of each type is left, so the probability here is $1$ .
Our answer is thus $\frac{9}{28} \cdot \frac{2}{5} = \frac{9}{70}$ , and $m + n = \boxed{79}$ .

## Solution 2
Call the three different types of rolls as A, B, and C. We need to arrange 3As, 3Bs, and 3Cs in a string such that A, B, and C appear in the first three, second three, and the third three like ABCABCABC or BCABACCAB. This can occur in $\left(\frac{3!}{1!1!1!}\right)^3 = 6^3 = 216$ different manners. The total number of possible strings is $\frac{9!}{3!3!3!} = 1680$ . The solution is therefore $\frac{216}{1680} = \frac{9}{70}$ , and $m + n = \boxed{79}$ .

## Solution 3
The denominator of m/n is equal to the total amount of possible roll configurations given to the three people. This is equal to ${9 \choose 3}{6 \choose3}$ as the amount of ways to select three rolls out of 9 to give to the first person is ${9 \choose 3}$ , and three rolls out of 6 is ${6 \choose3}$ . After that, the three remaining rolls have no more configurations.
The numerator is the amount of ways to give one roll of each type to each of the three people, which can be done by defining the three types of rolls as x flavored, y flavored, and z flavored.
xxx, yyy, zzz
So you have to choose one x, one y, and one z to give to the first person. There are 3 xs, 3 ys, and 3 zs to select from, giving $3^3$ combinations. Multiply that by the combinations of xs, ys, and zs for the second person, which is evidently $2^3$ since there are two of each letter left.
$(27*8)/{9 \choose 3}{6 \choose3}$ simplifies down to our fraction m/n, which is $9/70$ . Adding them up gives $9 + 70 = \boxed{79}$ .

## Solution 4
Let the objects be $A_1$ , $A_2$ , $A_3$ with similar labeling for $B$ and $C$ . There are $9!$ ways to order these nine objects in a line.
We then label three "zones" corresponding to the three people's meals as the first, second, and third objects in the line corresponding to the first zone, the fourth, fifth, and sixth to the second zone, and the remainder to the third zone. Each zone must contain one of each $A$ , $B$ , and $C$ . There are $6$ ways to place the three $A$ rolls in three different zones, and the same goes for $B$ and $C$ . In each zone, there are $6$ ways to order the three rolls, so there are in total $6^6$ legal orderings.
Thus the desired probability is $\frac{6^6}{9!}=\frac{9}{70}$ , so the answer is $9+70=\boxed{79}$ .
~eevee9406
These problems are copyrighted © by the Mathematical Association of America.