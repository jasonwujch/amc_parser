# 2008 AIME II Problem 1

## Problem

Let $N = 100^2 + 99^2 - 98^2 - 97^2 + 96^2 + \cdots + 4^2 + 3^2 - 2^2 - 1^2$ , where the additions and subtractions alternate in pairs. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
Rewriting this sequence with more terms, we have
Factoring this expression yields
Next, we get
Then,
Dividing $10100$ by $1000$ yields a remainder of $\boxed{100}$ .

## Solution 2
Since we want the remainder when $N$ is divided by $1000$ , we may ignore the $100^2$ term. Then, applying the difference of squares factorization to consecutive terms,

## Solution 3
By observation, we realize that the sequence \[(a+3)^2 + (a+2)^2 - (a+1)^2 - a^2\] alternates every 4 terms. Simplifying, we get \[(a+3)^2 + (a+2)^2 - (a+1)^2 - a^2 = 8a + 12\] , turning $N$ into a arithmetic sequence with 25 terms, them being $1, 5, 9, \dots ,97$ , as the series $8a + 12$ alternates every 4 terms.
Applying the sum of arithmetic sequence formula, we get
So the answer would be \[\frac{10100}{1000} = \boxed{100}\] .
- erdaifuu

## Solution 4
We can remove the $100^2$ since $100^2 \equiv 0 \pmod{1000}$ and use difference of squares to factor out the rest. This gives \[(1)(99+98) + (-1)(96+97) + ... +(1)(3+2) +(-1)(1+0)\] Writing this another way, we get \[(99(2) - 1) - (97(2)- 1) + (95(2) - 1) - ... +(3(2)-1) - (1(2) -1)\] We know that the last one is negative because all the numbers before multiplying that are in the form $4a - 1$ (eg. $99 = 25(4) - 1$ ) are positive.
Let $x = 99$ . This makes the expression \[(2x-1) - (2(x-2) - 1) + (2(x-4) - 1) - ... + (2(x-96) - 1) - (2(x-98) - 1)\] This simplifies to \[(2x-1) - (2x-5) + (2x-9) - ... +(2x - 193) - (2x-197)\] Since the first one is positive and the last one is negative, that means there are an even number of terms and using the associative property and the distributive property, all of the $2x$ terms cancel out. A consequence of this is that all of the positive integers turn negative and all the negative ones turn positive(eg. $-(2x-5) = -2x + 5$ ).
We are left with the sequence \[-1+5-9+...-193+197\] We can notice the property that the number of terms in the sequence to a positive number n is equal to $(n+3)/4$ , as well as the fact that every pair sums up to 4. Therefore the total number of terms is $(197+3) / 4 = 50$ . Therefore, there are 25 pairs each summing up to 4, leaving us with $25(4) = \boxed{100}$ .
~idk12345678

## Solution 5
We simply take the outer pairs and from there, we use the inside terms. That is, $N = 100^2 + 99^2 - 98^2 - 97^2 + 96^2 + \cdots + 4^2 + 3^2 - 2^2 - 1^2$ becomes $N = (100^2 - 1^2) + (99^2 - 2^2) - (98^2 - 3^2) - (97^2 - 4^2) + (96^2 - 5^2) ...$ and thus is reduced to $N = 101(99 + 97 - 95 - 93 + 81 + 89 - ... - 7 - 5 + 3 + 1)$ since the entire sequence has 50 terms. Therefore, the last two terms must be positive as the above inner sequence repeats as follows : Positive - positive - negative - negative. It follows that $N = 101[8(12) + 4] = 101[100] = 10100$ . So the requested answer is $\boxed{100}$ . ~elpianista227
### See also
These problems are copyrighted © by the Mathematical Association of America.