# 2004 AIME II Problem 10

## Problem

Let $S$ be the set of integers between $1$ and $2^{40}$ whose binary expansions have exactly two $1$ 's. If a number is chosen at random from $S,$ the probability that it is divisible by $9$ is $p/q,$ where $p$ and $q$ are relatively prime positive integers. Find $p+q.$

## Solution 1 (Rigorous)
Any number from 1 to $2^{40}$ can be represented in binary with 40 digits (because $2^{40}$ has 41) with leading zeroes if necessary. Therefore the number of sets where there are exactly two 1’s in this binary representation is just $\binom {40}{2}$ because we’re choosing 2 1s to go in 40 digit slots. This is equal to 780; we have found $q$ , our denominator.
With these particular numbers, when converting back to decimal note that the 38 zeroes all cancel out. Let the first 1 when reading the number in binary from left to right be in position $y$ , I.e. when converting to decimal, it will have value $2^{y}$ . Similarly, let the second 1 have position $x$ (note $x<y$ ); then the decimal value of that 1 will be $2^{x}$ . For example, with the binary string 0001001000 $y$ is 6 and $x$ is 3 (note that it is zero indexed).
It should also be noted that our constraints on $x$ and $y$ are $0 \leq x < y < 40$ and $x, y \in \mathbb{Z}$ .
The numbers that satisfy the constraints are therefore equal to $2^{x}+2^{y} = 2^{x} \cdot (1+2^{y-x})$ . The conditions say that this is divisible by 9. $2^{x}$ is clearly never divisible by 9, so we can just focus on $1+2^{y-x}$ . \[1+2^{y-x} \equiv 0 \pmod 9 \implies 2^{y-x} \equiv -1 \pmod 9 \implies 2^{y-x} \equiv 8 \pmod 9\]
$y-x = 3$ clearly satisfies the congruence, but are there any more? Well, we see that any time we raise -1 (in the second congruence above) to an odd power we get -1 again, so if we raise $2^{3}$ , which we know already works, to an odd power, we will also satisfy the congruence. Thus, $2^{3}, 2^{9}, 2^{15},$ etc. work; or, \[y-x \equiv 3 \pmod 6\]
To count the numbers that satisfy the condition, we need to find the amount of numbers that satisfy $2^{x} \cdot (1+2^{y-x}) \leq 2^{40}$ , and $y-x \equiv 3 \pmod 6 = 6n +3$ for some whole number $n$ .
Since we know $1+2^{y-x} = 1+2^{6n+3}$ is positive, we can divide both sides of the inequality by it; \[2^{x} \cdot (1+2^{y-x}) \leq 2^{40} \implies 2^{x} \leq \frac{2^{40}}{1+2^{y-x}} \implies 2^{x} \leq \frac{2^{40}}{1+2^{6n+3}}\] \[\implies 2^{x} < \frac{2^{40}}{2^{6n+3}} \implies 2^{x} < 2^{40-(6n+3)}\implies 2^{x} < 2^{37-6n} \implies x < 37 - 6n\]
Finally, the number of possible values of $x$ is $37-6n$ because $x$ can also be 0 and must be an integer.Therefore, as we increase $n$ from zero upwards, we get the total number of possibilities for $x$ is $37+31+25+\ldots+1 = 7 + 36 + 30 + 24 + \ldots + 6 + 0 = 7 + 6 \cdot (6 + 5 + 4\ldots + 1)$
$= 7 + 6 \cdot 3 \cdot 7 = 7 + 18 \cdot 7 = 19 \cdot 7 = 133$ .
Since 133 and 780 are relatively prime, the answer is $\frac{133}{780}$ and our final answer is $133+780 = \boxed{913}$
~KingRavi

## Solution 2
A positive integer $n$ has exactly two 1s in its binary representation exactly when $n = 2^j + 2^k$ for $j \neq k$ nonnegative integers. Thus, the set $S$ is equal to the set $\{n \in \mathbb{Z} \mid n = 2^j + 2^k \,\mathrm{ and }\, 0 \leq j < k \leq 39\}$ . (The second condition ensures simultaneously that $j \neq k$ and that each such number less than $2^{40}$ is counted exactly once.) This means there are ${40 \choose 2} = 780$ total such numbers.
Now, consider the powers of $2$ mod $9$ : $2^{6n} \equiv 1, 2^{6n + 1} \equiv 2, 2^{6n + 2} \equiv 4, 2^{6n + 3} \equiv 8 \equiv -1,$ $2^{6n + 4} \equiv 7 \equiv -2,$ $2^{6n + 5} \equiv 5 \equiv -4 \pmod 9$ .
It's clear what the pairs $j, k$ can look like. If one is of the form $6n$ (7 choices), the other must be of the form $6n + 3$ (7 choices). If one is of the form $6n + 1$ (7 choices) the other must be of the form $6n + 4$ (6 choices). And if one is of the form $6n + 2$ (7 choices), the other must be of the form $6n + 5$ (6 choices). This means that there are $7\cdot 7 + 7\cdot 6 + 7\cdot 6 = 49 + 42 +42 = 133$ total "good" numbers.
The probability is $\frac{133}{780}$ , and the answer is $133 + 780 = \boxed{913}$ .
-minor edit by Mathkiddie

## Solution 3 (similar to 2)
As mentioned above, there are 780 possible combinations. Since we are essentially adding two powers of two together, thinking about the properties of this sum organizes our solution. All powers of two are even except for $2^0$ , so we begin with labeling an entire group "where one of the 1s is in the rightmost spot". In an equation, $2^n+1$ is congruent to 0 mod 9. Instantly we think of $2^3=8$ , and trial and error soon gives us $2^9=512$ . Notice a pattern? Trying 2^15 = 32768 also works. You could go on, but basically all powers of two 3 mod 6 are 1 mod 9. (This is proven with the fact that $2^6$ is 1 mod 9) There are seven 3 mod 6 powers of 2 from 1-39, so for our first category there are seven "good" combinations.
Next, we look at powers of two exclusive from 1-39. Expressed in an equation, $2^n+2^m$ is congruent to 0 mod 9. Since nine is a relatively small number, we can treat powers of two as remainders of nine, to find "good" combinations quickly. Making a list of powers of two from 1-6 shows that the remainders when divided by nine are 2, 4, 8, 7, 5, and 1. This repeats itself every 6 powers. With simple counting we see there are seven powers of two that give remainders of 2, 4, and 8 each. Also there are six powers of two two that give remainders of 7, 5, and 1 each. Notice that each trio of powers correspond with another in the opposite trio. WLOG, if you choose two, (which there are seven to select) there are six different sevens to pair. This gives $7*6$ . Repeat for the other two pairs.
In the end there are $7+42+42+42$ "good" combinations, for an answer of $133 + 780 = \boxed{913}$ .
-jackshi2006

## Solution 4
Notice that in any binary expression, when we take it modulo $9$ and look at it in groups of 3 starting from the right, we get bases with modulo's $4,2,1$ in the first group and $-4,-2,-1$ in the second group. For our number to be divisible by $9$ , we have to get one of the positive multipliers and its opposite to cancel out. There are a total of $7$ complete positive groups and $6$ complete negative groups and then $2^{39}$ is left which is $-1$ . If we select a $1$ , we have $7$ ways to negate it and $7$ ways to select it giving $49$ . If we select a $2$ , we have $6$ ways to negate it and $7$ ways to select it giving $42$ . The same follows for selecting a $4$ . In total, we need to choose $2$ out of the total $40$ digits to "activate" and turn into a $1$ . In total we get \[\frac{49+42+42}{{40\choose{2}}} = \frac{133}{780}\] Adding, we get $133 + 780 = \boxed{913}$ .
-Vedoral
These problems are copyrighted © by the Mathematical Association of America.