# 2004 AIME I Problem 7

## Problem

Let $C$ be the coefficient of $x^2$ in the expansion of the product $(1 - x)(1 + 2x)(1 - 3x)\cdots(1 + 14x)(1 - 15x).$ Find $|C|.$

1 Problem

- 1 Problem

- 2 Solutions 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 (Bash) 2.4 Solution 4 (Easy) 2.5 Solution 4.5(easier explanation)

- 3 Solution 4

- 4 Solution 5

- 5 Solution 6

- 6 Solution 7

- 7 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3 (Bash)

- 2.4 Solution 4 (Easy)

- 2.5 Solution 4.5(easier explanation)

## Solutions

## Solution 1
Let our polynomial be $P(x)$ .
It is clear that the coefficient of $x$ in $P(x)$ is $-1 + 2 - 3 + \ldots + 14 - 15 = -8$ , so $P(x) = 1 -8x + Cx^2 + Q(x)$ , where $Q(x)$ is some polynomial divisible by $x^3$ .
Then $P(-x) = 1 + 8x + Cx^2 + Q(-x)$ and so $P(x)\cdot P(-x) = 1 + (2C - 64)x^2 + R(x)$ , where $R(x)$ is some polynomial divisible by $x^3$ .
However, we also know $P(x)\cdot P(-x) = (1 - x)(1 + x)(1 +2x)(1 - 2x) \cdots (1 - 15x)(1 + 15x)$ $= (1 - x^2)(1 - 4x^2)\cdots(1 - 225x^2)$ $= 1 - (1 + 4 + \ldots + 225)x^2 + R(x)$ .
Equating coefficients, we have $2C - 64 = -(1 + 4 + \ldots + 225) = -1240$ , so $-2C = 1176$ and $|C| = \boxed{588}$ .

## Solution 2
Let $S$ be the set of integers $\{-1,2,-3,\ldots,14,-15\}$ . The coefficient of $x^2$ in the expansion is equal to the sum of the product of each pair of distinct terms, or $C = \sum_{1 \le i \neq j}^{15} S_iS_j$ . Also, we know that \begin{align*}\left(\sum_{i=1}^{n} S_i\right)^2 &= \left(\sum_{i=1}^{n} S_i^2\right) + 2\left(\sum_{1 \le i \neq j}^{15} S_iS_j\right)\\ (-8)^2 &= \frac{15(15+1)(2\cdot 15+1)}{6} + 2C\end{align*} where the left-hand sum can be computed from:
and the right-hand sum comes from the formula for the sum of the first $n$ perfect squares. Therefore, $|C| = \left|\frac{64-1240}{2}\right| = \boxed{588}$ .

## Solution 3 (Bash)
Consider the set $[-1, 2,-3,4,-5,6,-7,8,-9,10,-11,12,-13,14,-15]$ . Denote by $S$ all size 2 subsets of this set. Replace each element of $S$ by the product of the elements. Now, the quantity we seek is the sum of each element. Since consecutive elements add to $1$ or $-1$ , we can simplify this to $588$

## Solution 4 (Easy)
We know that this polynomial has roots $1, -\frac{1}{2}, \frac{1}{3},\ldots$ and the coefficient of $x^2$ will be the sum of the product taken by $13$ . However, since this is closer to the constant side, we can create a new polynomial with the reciprocal roots which will make $C$ the coefficient of $x^{13}$ and thus the sum of the reciprocal roots taken by 2. We can calculate this with $1\cdot(8-1)-2\cdot(8-(-2))+\ldots+15(8-15)$ . This will give us $2C = -1176$ giving us a final answer of $|C| = \fbox{588}$ .
~ Vedoral

## Solution 4.5(easier explanation)
In this polynomial, we can see that the coefficient of $x^2$ by Vieta’s Formulae is the sum of the products of every 13 of the roots. Let us denote the roots $r_1, r_2 \dots ,r_15$
Then, by Veita’s, we have that \[r_1\cdot r_2 \dots \cdot r_13 + \dots + r_3 \cdot r_4 + \cdots r_15\] . Also, since we know that the product of the roots is $1$ again by vieta’s formulae, we can make an arbitrary term of this expression, for example the $r_1 \cdot r_2 \dots r_13$ equal to \[\frac{r_1 \cdot r_2 \dots \cdot r_15}{r_14 \cdot r_15} = \frac{1}{r_14 , r_15}\] Now we are just finding the expression, because this is just an expansion of \[\frac{(\frac{1}{r_1} + \dots \frac{1}{r_15}) \cdot (\frac{1}{r_1} + \dots \frac{1}{r_15}) - ((\frac{1}{r_1})^2 \dots)}{2}\] which easily evaluates to $8 \cdot \frac{147}{2} = \fbox{588}$

## Solution 4
Let set $N$ be $\{-1, -3, \ldots -15\}$ and set $P$ be $\{2, 4, \ldots 14\}$ . The sum of the negative $x^2$ coefficients is the sum of the products of the elements in all two element sets such that one element is from $N$ and the other is from $P$ . Each summand is a term in the expansion of \[(-1 - 3 - \ldots - 15)(2 + 4 + \ldots + 14)\] which equals $-56 * 64 = -(60^2 - 4^2) = -3584$ . The sum of the positive $x^2$ coefficients is the sum of the products of all two element sets such that the two elements are either both in $N$ or both in $P$ . By counting, the sum is $2992$ , so the sum of all $x^2$ coefficients is $-588$ . Thus, the answer is $\boxed{588}$ .

## Solution 5
We can find out the coefficient of $x^2$ by multiplying every pair of two coefficients for $x$ . This means that we multiply $-1$ by $2,-3,4,-5,6,-7,8,-9,10,-11,12,-13,14,-15$ and $2$ by $3,4,-5,6,-7,8,-9,10,-11,12,-13,14,-15$ . and etc. This sum can be easily simplified and is equal to $(-1)(-7)+(-3)(-6)+(-5)(-5)+(-7)(-4)+(-9)(-3)+(-11)(-2)+(-13)(-1)+2(-9)+4(-10)+6(-11)+8(-12)+10(-13)+12(-14)+14(-15)$ or $588$ .
-David Camacho

## Solution 6
This is just another way of summing the subsets of 2 from $[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15]$ . Start from the right and multiply -15 to everything on its left. Use the distributive property and add all the 14 integers together to get 7. This gives us $-15 * 7$ . Doing this for 14 gives us $14 * -7$ , and for -13 we get $-13 * 6$ . This pattern repeats where every two integers will multiple 7, 6,... to 0. Combining and simplifying the pattern give us this: $-(29 * 7 + 25 * 6 + 21 * 5 + 17 * 4 + 13 * 3 + 9 * 2 + 5*1)$ . The expression gives us -588, or $C = \boxed{588}$ . This is a good solution because it guarantees we never add a product twice, and the pattern is simple to add by hand.
-jackshi2006

## Solution 7
We expand and obtain $\left(x-1\right)\left(2x-1\right)\left(3x-1\right)\cdots\left(15x-1\right) = 1307674368000x^{15} - 948550176000x^{14} - 689324826240x^{13} + 2733483288464x^{12} + 82808260416x^{11} - 23038684088x^{10} - 3811851848x^9 + 828730833x^8 + 81228128x^7 - 14661124x^6 - 853104x^5 + 132902x^4 + 4256x^3 - \boxed{588}x^2 - 8x + 1.$
Do not do this in an actual competition.
~Sliced_Bread
These problems are copyrighted © by the Mathematical Association of America.