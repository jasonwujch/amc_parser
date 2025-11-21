# 2003 AIME I Problem 9

## Problem

An integer between $1000$ and $9999$ , inclusive, is called balanced if the sum of its two leftmost digits equals the sum of its two rightmost digits. How many balanced integers are there?

## Solution 1
If the common sum of the first two and last two digits is $n$ , such that $1 \leq n \leq 9$ , there are $n$ choices for the first two digits and $n + 1$ choices for the second two digits (since zero may not be the first digit). This gives $\sum_{n = 1}^9 n(n + 1) = 330$ balanced numbers. If the common sum of the first two and last two digits is $n$ , such that $10 \leq n \leq 18$ , there are $19 - n$ choices for both pairs. This gives $\sum_{n = 10}^{18} (19 - n)^2 = \sum_{n = 1}^9 n^2 = 285$ balanced numbers. Thus, there are in total $330 + 285 = \boxed{615}$ balanced numbers.
Both summations may be calculated using the formula for the sum of consecutive squares , namely $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$ .

## Solution 2 (Painful Casework)
Call the number $\overline{abcd}$ . Then $a+b=c+d$ . Set $a+b=x$ .
Clearly, $0\le x \le18$ .
If $x=0$ : $0000$ is not acceptable.
If $x=1$ : The only case is $1001$ or $1010$ . 2 choices.
If $x=2$ : then since $a\neq0$ , $a=1=b$ or $a=2, b=0$ . There are 3 choices for $(c,d)$ : $(2,0), (0, 2), (1, 1)$ . $2*3=6$ here.
If $x=3$ : Clearly, $a\neq b$ because if so, the sum will be even, not odd. Counting $(a,b)=(3,0)$ , we have $4$ choices. Subtracting that, we have $3$ choices. Since it doesn't matter whether $c=0$ or $d=0$ , we have 4 choices for $(c,d)$ . So $3*4=12$ here.
If $x=4$ : Continue as above. $4$ choices for $(a,b)$ . $5$ choices for $(c,d)$ . $4*5=20$ here.
If $x=5$ : You get the point. $5*6=30$ .
If $x=6$ : $6*7=42$ .
If $x=7$ : $7*8=56$ .
If $x=8$ : $8*9=72$ .
If $x=9$ : $9*10=90$ .
Now we need to be careful because if $x=10$ , $(c,d)=(0,10)$ is not valid. However, we don't have to worry about $a\neq0$ .
If $x=10$ : $(a,b)=(1,9), (2, 8), ..., (9, 1)$ . Same thing for $(c,d)$ . $9*9=81$ .
If $x=11$ : We start at $(a,b)= (2,9)$ . So $8*8$ .
Continue this pattern until $x=18: 1*1=1$ . Add everything up: we have $\boxed{615}$ .
~hastapasta

## Solution 3
We ignore the requirement that the first digit is non-zero, and do casework on the sum of the sum of the pairs of digits.
If two digits $a$ and $b$ sum to $0$ , we have $1$ possibility: $(a,b) = (0,0)$
If $a+b = 1$ , we have $2$ possibilities: $(a,b) = (0,1)$ and $(a,b) = (1,0)$
$a+b = 2$ : $(0,2)$ , $(2,0)$ , and $(1,1)$ are the only $3$ possibilities.
We notice a pattern: for all $k \leq 9$ , there are $k+1$ ordered pairs of digits $(a,b)$ such that $a+b = k$ . Then, testing for $10 \leq k \leq 18$ , we notice that there are $(18 - k) + 1$ ordered pairs with a sum of $k$ .
So the number of ways to pick $4$ digits satisfying the constraint is \[(1)(1) + (2)(2) \dots (10)(10) + (9)(9) + \dots + (1)(1) = \frac{(10)(11)(21)}{6} + \frac{(9)(10)(19)}{6} = 670\]
We have to subtract out the cases where the first digit is $0$ , which is $1+2+\dots+10 = 55$
So our answer is $670-55 = \boxed{615}$
This solution takes some inspiration from dice. In a way, we are counting the number of ways to roll a given number with a pair of $10$ -sided dice.
~jd9
These problems are copyrighted © by the Mathematical Association of America.