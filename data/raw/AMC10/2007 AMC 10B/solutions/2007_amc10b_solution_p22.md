# 2007 AMC 10B Problem 22

## Problem

A player chooses one of the numbers $1$ through $4$ . After the choice has been made, two regular four-sided (tetrahedral) dice are rolled, with the sides of the dice numbered $1$ through $4.$ If the number chosen appears on the bottom of exactly one die after it has been rolled, then the player wins $1$ dollar. If the number chosen appears on the bottom of both of the dice, then the player wins $2$ dollars. If the number chosen does not appear on the bottom of either of the dice, the player loses $1$ dollar. What is the expected return to the player, in dollars, for one roll of the dice?

$\textbf{(A) } -\frac{1}{8} \qquad\textbf{(B) } -\frac{1}{16} \qquad\textbf{(C) } 0 \qquad\textbf{(D) } \frac{1}{16} \qquad\textbf{(E) } \frac{1}{8}$

## Solution
There are $2 \cdot 3 \cdot 1 = 6$ ways for your number to show up once, $1 \cdot 1 = 1$ way for your number to show up twice, and $3 \cdot 3 = 9$ ways for your number to not show up at all. Think of this as a set of sixteen numbers with six $1$ 's, one $2$ , and nine $-1$ 's. The average of this set is the expected return to the player. \[\frac{6(1)+1(2)-9(1)}{16} = \frac{6+2-9}{16} = \boxed{\mathrm{(B) \ } -\frac{1}{16}}\]

## Solution 2
We approach this through casework. We have a $\frac{1}{4} \cdot \frac{3}{4} \cdot 2$ chance of earning $1$ dollar. We have a $\frac{1}{4} \cdot \frac{1}{4}$ chance of earning $2$ dollars, and a $\frac{3}{4} \cdot \frac{3}{4}$ chance of losing $1$ dollar. Thus, our final answer is $\frac{3}{8} \cdot 1 + \frac{1}{16} \cdot 2 + \frac{9}{16} \cdot -1 = \boxed{\mathrm{(B) \ } -\frac{1}{16}}$ -SuperJJ
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .