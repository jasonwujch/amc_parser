# 2019 AIME II Problem 4

## Problem

A standard six-sided fair die is rolled four times. The probability that the product of all four numbers rolled is a perfect square is $\tfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
Notice that, other than the number 5, the remaining numbers 1, 2, 3, 4, 6 are only divisible by 2 and/or 3. We can do some cases on the number of 5's rolled (note that there are $6^4 = 1296$ outcomes).
Case 1 (easy): Four 5's are rolled. This has probability $\frac{1}{6^4}$ of occurring.
Case 2: Two 5's are rolled.
Case 3: No 5's are rolled.
To find the number of outcomes for the latter two cases, we will use recursion. Consider a 5-sided die with faces numbered 1, 2, 3, 4, 6. For $n \ge 1$ , let $a_n$ equal the number of outcomes after rolling the die $n$ times, with the property that the product is a square. Thus, $a_1 = 2$ as 1 and 4 are the only possibilities.
To find $a_{n+1}$ given $a_n$ (where $n \ge 1$ ), we observe that if the first $n$ rolls multiply to a perfect square, then the last roll must be 1 or 4. This gives $2a_n$ outcomes. Otherwise, the first $n$ rolls do not multiply to a perfect square ( $5^n - a_n$ outcomes). In this case, we claim that the last roll is uniquely determined (either 2, 3, or 6). If the product of the first $n$ rolls is $2^x 3^y$ where $x$ and $y$ are not both even, then we observe that if $x$ and $y$ are both odd, then the last roll must be 6; if only $x$ is odd, the last roll must be 2, and if only $y$ is odd, the last roll must be 3. Thus, we have $5^n - a_n$ outcomes in this case, and $a_{n+1} = 2a_n + (5^n - a_n) = 5^n + a_n$ .
Computing $a_2$ , $a_3$ , $a_4$ gives $a_2 = 7$ , $a_3 = 32$ , and $a_4 = 157$ . Thus for Case 3, there are 157 outcomes. For case 2, we multiply $a_2$ by $\binom{4}{2} = 6$ to distribute the two 5's among four rolls. Thus the probability is
\[\frac{1 + 6 \cdot 7 + 157}{6^4} = \frac{200}{6^4} = \frac{25}{162} \implies m+n = \boxed{187}\]
-scrabbler94

## Solution 2
We can solve this without finding the amount of cases. Notice when we roll a 1 or a 4, it does not affect whether or not the product is a square number. We have a 1/3 chance of rolling either a 1 or 4. We have a 2/3 chance of rolling a 2,3,5 or 6. Let's call rolling 1 or 4 rolling a dud (a perfect square).
Probability of rolling 4 duds: $\left(\frac{1}{3}\right)^4$
Probability of rolling 3 duds: $4 * \left(\frac{1}{3}\right)^3 * \frac{2}{3}$
Probability of rolling 2 duds: $6 * \left(\frac{1}{3}\right)^2 * \left(\frac{2}{3}\right)^2$
Probability of rolling 1 dud: $4 * \frac{1}{3} * \left(\frac{2}{3}\right)^3$
Probability of rolling 0 duds: $\left(\frac{2}{3}\right)^4$
Now we will find the probability of a square product given we have rolled each amount of duds
Probability of getting a square product given 4 duds: 1
Probability of getting a square product given 3 duds: 0 (you will have 1 non-dud and that's never going to be square)
Probability of getting a square product given 2 duds: $\frac{1}{4}$ (as long as our two non-duds are the same, our product will be square)
Probability of getting a square product given 1 dud: $\frac{3!}{4^3}$ = $\frac{3}{32}$ (the only way to have a square product is rolling a 2,3 and 6. There are 3! ways of doing that and a total of $4^3$ ways to roll 3 non-duds).
Probability of getting a square product given 0 duds: $\frac{40}{4^4}$ = $\frac{5}{32}$ (We can have any two non-duds twice. For example, 2,2,5,5. There are $\binom{4}{2} = 6$ ways of choosing which two non-duds to use and $\binom{4}{2} = 6$ ways of choosing how to arrange those 4 numbers. That gives us 6*6=36 combinations. We can also have 2,2,2,2 or 3,3,3,3 or 5,5,5,5 or 6,6,6,6. This gives us a total of 40 combinations).
We multiply each probability of rolling k duds with the probability of getting a square product given k duds and then sum all the values. \[\left(\frac{1}{3}\right)^4 * 1 + 4 * \left(\frac{1}{3}\right)^3 * \frac{2}{3} * 0 + 6 * \left(\frac{1}{3}\right)^2 * \left(\frac{2}{3}\right)^2 * \frac{1}{4} + 4 * \frac{1}{3} * \left(\frac{2}{3}\right)^3 * \frac{3}{32} + \left(\frac{2}{3}\right)^4 * \frac{5}{32} = \frac{25}{162}.\]
$25+162$ = $\boxed{187}$
-dnaidu (silverlizard)

## Solution 3
Note that rolling a 1/4 will not affect whether or not the product is a perfect square. This means that in order for the product to be a perfect square, all non 1/4 numbers rolled must come in pairs, with the only exception being the triplet 2,3, 6. Now we can do casework:
If there are four 1/4's, then there are $2^4=16$ combinations. If there are three 1/4's, then there are 0 combinations, because the fourth number isn't a square. If there are two 1/4's, there are $2^2=4$ ways to choose the two 1/4's, 4 ways to choose the remaining pair of numbers, and $\frac{4!}{2!2!}=6$ ways to arrange, so there are $4\cdot 4\cdot 6=96$ combinations for this case. If there is one 1/4, then there are 2 ways to choose whether it is a 1 or 4, and the remaining three numbers must be 2, 3, and 6, so there are $4!$ ways to order, meaning there are $2\cdot 4!=48$ combinations for this case. Our final case is if there are no 1/4's, in which case we must have two pairs. If the two pairs are of different numbers, then there $\binom{4}{2}$ to choose the numbers and $\frac{4!}{2!2!}=6$ ways to arrange them, so $6\cdot 6=36$ . If all four numbers are the same there are $4$ combinations, so there are $4+36=40$ combinations for this case.
Hence there are $16+0+96+48+40=200$ combinations where the product of the dice is a perfect square, and there are $6^4=1296$ total combinations, so the desired probability is $\frac{200}{1296}=\frac{25}{162}$ , yielding an answer of $25+162=\boxed{187}$ .
-Stormersyle

## Solution 4 (Casework)
Another way to solve this problem is to do casework on all the perfect squares from $1^2$ to $36^2$ , and how many ways they can be ordered $1^2$ - $1,1,1,1$ - $1$ way. $2^2$ - $4,1,1,1$ or $2,2,1,1$ - $\binom{4}{2}+4=10$ ways. $3^2$ - $3,3,1,1$ - $\binom{4}{2}=6$ ways. $4^2$ - $4,4,1,1$ , $2,2,2,2$ , or $2,2,4,1$ - $\binom{4}{2}+1+12=19$ ways. $5^2$ - $5,5,1,1$ - $\binom{4}{2}=6$ ways. $6^2$ - $6,6,1,1$ , $1,2,3,6$ , $2,3,2,3$ , $3,3,4,1$ - $2*\binom{4}{2}+4!+12=48$ ways. $7^2$ - Since there is a prime greater than 6 in its prime factorization there are $0$ ways. $8^2$ - $4,4,4,1$ or $2,4,2,4$ - $\binom{4}{2}+4=10$ ways. $9^2$ - $3,3,3,3$ - $1$ way. $10^2$ - $2,2,5,5$ or $1,4,5,5$ - $6+12=18$ ways. $11^2$ - $0$ ways for the same reason as $7^2$ . $12^2$ - $6,6,2,2$ , $4,4,3,3$ , $2,3,4,6$ , or $1,4,6,6$ - $2*\binom{4}{2}+4!+12=48$ ways. $13^2$ - $0$ ways. $14^2$ - $0$ ways. $15^2$ - $3,3,5,5$ - $\binom{4}{2}=6$ ways. $16^2$ - $4,4,4,4$ - $1$ way. $17^2$ - $0$ ways. $18^2$ - $3,3,6,6$ - $\binom{4}{2}=6$ ways. $19^2$ - $0$ ways. $20^2$ - $4,4,5,5$ - $\binom{4}{2}=6$ ways. $21^2$ - $0$ ways. $22^2$ - $0$ ways. $23^2$ - $0$ ways. $24^2$ - $4,4,6,6$ - $\binom{4}{2}=6$ ways. $25^2$ - $5,5,5,5$ - $1$ way. $26^2$ - $0$ ways. $27^2$ - $0$ ways. $28^2$ - $0$ ways. $29^2$ - $0$ ways. $30^2$ - $5,5,6,6$ - $\binom{4}{2}$ ways. $31^2$ - $0$ ways. $32^2$ - $0$ ways. $33^2$ - $0$ ways. $34^2$ - $0$ ways. $35^2$ - $0$ ways. $36^2$ - $6,6,6,6$ - $1$ way.
There are $6^4=1296$ ways that the dice can land. Summing up the ways, it is easy to see that there are $200$ ways. This results in a probability of $\frac{200}{1296}=\frac{25}{162}\implies\boxed{187}$ -superninja2000

## Solution 5 (Recursion)
We can do recursion on the number of rolls to find the number of ways we can get $4$ rolls to multiply to a square.
After $n$ rolls, let us say that the product is $p = 2^a3^b5^c$ .
Define the following:
$A_{n} =$ the number of ways to have a product after $n$ rolls where $a$ is odd, and $b$ , $c$ are even
$B_{n} =$ the number of ways to have a product after $n$ rolls where $b$ is odd, and $a$ , $c$ are even
$C_{n} =$ the number of ways to have a product after $n$ rolls where $c$ is odd, and $a$ , $b$ are even
$D_{n} =$ the number of ways to have a product after $n$ rolls where $c$ is even, and $a$ , $b$ are odd
$E_{n} =$ the number of ways to have a product after $n$ rolls where $b$ is even, and $a$ , $c$ are odd
$F_{n} =$ the number of ways to have a product after $n$ rolls where $a$ is even, and $b$ , $c$ are odd
$G_{n} =$ the number of ways to have a product after $n$ rolls where $a, b,$ and $c$ are all odd
$S_{n} =$ the number of ways to have a product after $n$ rolls where $a, b,$ and $c$ are all even (square!)
We have the following equations after considering the possible values of the nth roll:
\[A_{n} = S_{n-1}+B_{n-1}+D_{n-1}+E_{n-1}+2A_{n-1}\]
\[B_{n} = A_{n-1}+D_{n-1}+F_{n-1}+S_{n-1}+2B_{n-1}\]
\[C_{n} = S_{n-1}+E_{n-1}+F_{n-1}+G_{n-1}+2C_{n-1}\]
\[D_{n} = S_{n-1}+A_{n-1}+B_{n-1}+G_{n-1}+2D_{n-1}\]
\[E_{n} = A_{n-1}+C_{n-1}+F_{n-1}+G_{n-1}+2E_{n-1}\]
\[F_{n} = B_{n-1}+E_{n-1}+C_{n-1}+G_{n-1}+2F_{n-1}\]
\[G_{n} = C_{n-1}+D_{n-1}+F_{n-1}+E_{n-1}+2G_{n-1}\]
\[S_{n} = A_{n-1}+C_{n-1}+B_{n-1}+D_{n-1}+2S_{n-1}\]
We have the following values after considering the possible values of the 1st roll:
\[A_1 = B_1 = C_1 = D_1 = 1; E_1 = F_1 = G_1 = 0; S_1 = 2\]
After applying recursion twice, we get:
\[A_2 = B_2 = D_2 = 6, C_2 = 4, E_2 = F_2 = G_2 = 2, S_2 = 8\]
\[A_3 = B_3 = D_3 = 34, C_3 = 22, E_3 = F_3 = G_3 = 18, S_3 = 38\]
Finally, we have $S_4 = 200$ , $\frac{m}{n} = \frac{200}{1296} = \frac{25}{162}$ meaning our answer is $\boxed{187}$ .

## Solution 6
Consider all the distinct "fundamental" groups of integers from $1$ to $6$ whose product is a perfect square. A "fundamental" group is one that cannot be broken into two smaller groups that each have a perfect square product. For example, $\{2,2\}$ is a fundamental group, while $\{3,3,4\}$ is not, because it can be broken up into $\{3,3\}$ and $\{4\}$ .
$1$ and $4$ are already perfect squares, so they each form a "fundamental" group and cannot belong in any other group. Pairs of the other $4$ numbers ( $\{2,2\}$ , $\{3,3\}$ , etc. ) form "fundamental" groups as well. The last "fundamental" group is $\{2,3,6\}$ . It can be easily seen that no more groups exist.
Thus, we have the "fundamental" groups $\{1\}$ , $\{4\}$ , $\{2,2\}$ , $\{3,3\}$ , $\{5,5\}$ , $\{6,6\}$ , and $\{2,3,6\}$ .
We now consider the ways to use these groups to form a sequence of $4$ numbers whose product is a perfect square. To form a set, we can simply select zero to two groups of size $2$ or $3$ and fill in any remaining spots with $1$ s and $4$ s. We can do this in one of $5$ ways: Using only $1$ s and $4$ s, using one group of size $2$ , using one group of size $3$ , using two different groups of size $2$ , and using the same group of size $2$ twice.
If we only use $1$ s and $4$ s, each of the $4$ slots can be filled with one of the $2$ numbers, so there are $2^4=16$ possibilities.
If we use one group of size $2$ , there are $4$ options for the group to use, $\binom{4}{2}$ ways to place the two numbers (since they are identical), and $2^2$ ways to fill in the remaining slots with $1$ s and $4$ s, so there are $4\cdot\binom{4}{2}\cdot2^2=96$ possibilities.
If we use one group of size $3$ , there is only $1$ option for the group to use, $4\cdot3\cdot2$ ways to place the three numbers (since they are distinct), and $2$ ways to fill in the remaining slot, so there are $4\cdot3\cdot2\cdot2=48$ possibilities.
If we use two different groups of size $2$ , there are $\binom{4}{2}$ options for the groups to use and $\binom{4}{2}$ ways to place the four numbers (since there are $2$ groups of identical numbers, and one group's placement uniquely determines the other's), so there are $\binom{4}{2}\cdot\binom{4}{2}=36$ possibilities.
If we use the same group of size $2$ twice, there are $4$ options for the group to use and $1$ way to place the four numbers (since they are all identical), so there are $4=4$ possibilities.
This gives us a total of $16+96+48+36+4=200$ possibilities, and since there are $6^4=1296$ total sequences that can be rolled, the probability is equal to $\frac{200}{1296}=\frac{25}{162}$ , so the answer is $25+162=\boxed{187}$ . ~ emerald_block

## Solution 7(Generating functions)
Let's look at the prime factorization of some of these rolls:
Now, using multi-variable generating functions, we get:
Let's square that!
Since we only want the parity of each of the exponents, we can collapse it again.
Last simplification: factor out a factor of two and save it for later.
Let's take a better approach this time.
I know we could use vectors and dot products to make it look neater but come on . It already looks neat enough. Also, we didn't need the other parts, but it just looks nicer . Now let's stick back the two that turned into a four.
We seek the constant term which is 200. 200/1296=100/648=50/324=25/162, 25+162=187
~ Afly ( talk )

## Solution 8
There are a total of $6^4=1296$ possible die rolls.
We use casework:
Case 1 : All 4 numbers are the same. There are obviously $6$ ways.
Case 2 : Sets of 2 different numbers.
A set of two different numbers is basically $(x,x,y,y)$ . There are a total of $\frac{4!}{2!\cdot 2!}=6$ ways to arrange the numbers.
By listing these cases, we quickly see a pattern:
$(1,1,2,2)$
$(1,1,3,3)$
$...$
$(1,1,6,6)$
$(2,2,3,3)$
$...$
$(2,2,6,6)$
$...$
$(5,5,6,6)$
There are a total of $5+4+3+2+1=15$ cases. Multiplying this by $6$ yields $15\cdot 6=90$ ways.
Case 3 : Sets of numbers in the form of $(x,x,1,4)$
A special case must be made for the number $4$ because $4$ itself is a perfect square.
$(1,1,1,4)$ $4$
$(2,2,1,4)$ $12$
$(3,3,1,4)$ $12$
$(4,4,1,4)$ $4$
$(5,5,1,4)$ $12$
$(6,6,1,4)$ $12$
Summing these up yields a total of $4+12+12+4+12+12=56$ ways.
Case 4 : Sets with all 4 numbers different
Note that the sets
$(1,2,3,6)$
$(2,3,4,6)$
Multiply to perfect square. The total of these cases are $24+24=48$ .
Adding all these cases together yields $6+90+56+48=200$ ways that the product of the values of the die can be a perfect square.
Therefore the probability is
$\frac{200}{1296}=\frac{25}{162}$
$m+n = 25+162 = \boxed{187}$
-elchen3_f

## Solution 9 (Clean Generating Functions and Roots of Unity Filter)
Recall that a number is a perfect square iff every prime in its prime factorization has even multiplicity. We can use multi-variable generating functions to track the contribution of each prime (namely 2, 3, 5) in one roll. Let $f(a,b,c)$ be the generating function such that the coefficient of each term $a^xb^yc^z$ is the number of ways to get a product of $2^x3^y5^z$ when rolling 4 dice. For each roll, we can either roll a 1 (basically contribute nothing), roll a 2 (contribute a factor of 2), roll a 3 (contribute a factor of 3), roll a 4 (contribute two factors of 2), roll a 5 (contribute a factor of 5), or roll a 6 (contribute a factor of 2 and a factor of 3), so the generating function for one roll is $1+a+b+a^2+c+ab$ . Hence, $f(a,b,c)= (1+a+b+a^2+c+ab)^4$ . We seek the sum of coefficients of the $a^{2p}b^{2q}c^{2r}$ terms $(p, q, r, \in \mathbb{Z}*)$ . $\newline$
To filter out the desired coefficients, apply Roots of Unity filter 3 times. Filter out the coefficients with even $a$ multiplicity using \[\frac{f(1, b, c)+f(-1, b, c)}{2}=\frac{(3+2b+c)^4+(c+1)^4}{2}=g(b,c).\] Similarly, now filter out the coefficients with even $b$ multiplicity with \[\frac{g(1, c)+g(-1, c)}{2}=\frac{(c+5)^4+3(c+1)^4}{4}=h(c).\] Apply this one more time to get \[\frac{h(1)+h(-1)}{2}=\frac{6^4+3(2)^4+4^4}{8}.\] The requested probability is $\frac{6^4+3(2)^4+4^4}{8\cdot 6^4}=\frac{25}{162} \implies \boxed{187}.$
~bomberdoodles
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .