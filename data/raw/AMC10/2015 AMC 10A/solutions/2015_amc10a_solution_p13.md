# 2015 AMC 10A Problem 13

## Problem

Claudia has 12 coins, each of which is a 5-cent coin or a 10-cent coin. There are exactly 17 different values that can be obtained as combinations of one or more of her coins. How many 10-cent coins does Claudia have?

$\textbf{(A) }3\qquad\textbf{(B) }4\qquad\textbf{(C) }5\qquad\textbf{(D) }6\qquad\textbf{(E) }7$

## Solution 1
Let Claudia have $x$ 5-cent coins and $\left( 12 - x \right)$ 10-cent coins. It is easily observed that any multiple of $5$ between $5$ and $5x + 10(12 - x) = 120 - 5x$ inclusive can be obtained by a combination of coins. Thus, $24 - x = 17$ combinations can be made, so $x = 7$ . But the answer is not $7,$ because we are asked for the number of 10-cent coins, which is $12 - 7 = \boxed{\textbf{(C) } 5}$ ~kurt

## Solution 2
Since the coins are 5-cent and 10-cent, all possible values that can be made will be multiples of $5.$ To have exactly 17 different multiples of $5,$ we will need to make up to $85$ cents. There are two solutions from here:
1. Hare and Chicken approach
We assume that the 12 coins are all 10-cent coins. The sum will now be (12)(10) which is 120. 120 is 35 more than 85, and every 10-cent coin we switch for a 5-cent one will reduce the sum by 10-5=5 cents. Since 35/5=7, we will need to switch 7 10-cent coins for 5-cent ones, meaning we will have 7 5-cent coins and 12-7=5 10-cent coins. Therefore, the correct answer is answer choice $\boxed{\textbf{(C) } 5}$
2. Algebra approach
We assume we have (x) 5-cent coins and (12-x)10-cent coins. Then we have the algebra formula 5x+10(12-x)=85 Simplyfying that, we get 120-5x=85, 5x=35, x=7. And since x is the number of 5-cent coins, the number of 10-cent coins is 12-x or 12-7=5. Therefore, the correct answer is answer choice $\boxed{\textbf{(C) } 5}$
-Alina

## Solution 3 (Quick Insight)
Notice that for every $d$ dimes, any multiple of $5$ less than or equal to $10d + 5(12-d)$ is a valid arrangement. Since there are $17$ in our case, we have $10d + 5(12-d)=17 \cdot 5 \Rightarrow d=5$ . Therefore, the answer is $\boxed{\textbf{(C) } 5}$ .
~MrThinker

## Solution 4
Dividing by 5cents to reduce clutter:
$D$ double coins and $S$ single coins can reach any value between $1$ and $2D + S$ . Set $2D + S = 17$ and $D + S = 12$ .
Subtract to get $D = \boxed{\textbf{(C) } 5}$ .
~oinava

## Video Solution
https://youtu.be/F2iyhLzmCB8
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .