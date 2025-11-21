# 2006 AIME II Problem 3

## Problem

Let $P$ be the product of the first $100$ positive odd integers . Find the largest integer $k$ such that $P$ is divisible by $3^k .$

## Solution
Note that the product of the first $100$ positive odd integers can be written as $1\cdot 3\cdot 5\cdot 7\cdots 195\cdot 197\cdot 199=\frac{1\cdot 2\cdots200}{2\cdot4\cdots200} = \frac{200!}{2^{100}\cdot 100!}$
Hence, we seek the number of threes in $200!$ decreased by the number of threes in $100!.$
There are
$\left\lfloor \frac{200}{3}\right\rfloor+\left\lfloor\frac{200}{9}\right\rfloor+\left\lfloor \frac{200}{27}\right\rfloor+\left\lfloor\frac{200}{81}\right\rfloor =66+22+7+2=97$
threes in $200!$ and
$\left\lfloor \frac{100}{3}\right\rfloor+\left\lfloor\frac{100}{9}\right\rfloor+\left\lfloor \frac{100}{27}\right\rfloor+\left\lfloor\frac{100}{81}\right\rfloor=33+11+3+1=48$
threes in $100!$
Therefore, we have a total of $97-48=\boxed{049}$ threes.
For more information, see also prime factorizations of a factorial .

## Solution 2
We count the multiples of $3^k$ below 200 and subtract the count of multiples of $2\cdot 3^k$ :
\[\left\lfloor \frac{200}{3}\right\rfloor - \left\lfloor \frac{200}{6}\right\rfloor +\left\lfloor\frac{200}{9}\right\rfloor - \left\lfloor \frac{200}{18}\right\rfloor +\left\lfloor \frac{200}{27}\right\rfloor - \left\lfloor \frac{200}{54}\right\rfloor+\left\lfloor\frac{200}{81}\right\rfloor - \left\lfloor \frac{200}{162}\right\rfloor\] \[= 66 - 33 + 22 - 11 + 7 - 3 + 2 - 1 = 49.\]

## Solution 3
We can use a modified version of Legendre's Formula. First, we count the number of multiples of 3 in the sequence 1, 3, 5, 7, 9, ..., 195, 197, 199.
This is the same as the number of multiples of 3 in the sequence 3, 9, 15, 21, ..., 192, 195. There are clearly 33 terms in this sequence.
Next, we count the number of multiples of 9 in the sequence 1, 3, 5, 7, 9, ..., 195, 197, 199. This is the same as the number of multiples of 9 in the sequence 9, 18, 27, 36, ...., 189, 198 - but there's a catch. Note that every other member of this sequence isn't odd and thus is not part of the product of the first 100 odd integers, so our new sequence is actually 9, 27, 45...189. Divide every term by 9 to get a new sequence; 1, 3, 5...21, which clearly has 11 terms.
Next, we similarly count the number of multiples of 27 in the sequence 1, 3, 5, 7, 9, ..., 195, 197, 199. This is just 27, 81, 135, 189, so 4 multiples here.
Finally, we count the number of multiples of 81 in the sequence 1, 3, 5, 7, 9, ..., 195, 197, 199. There is only one such multiple, 81.
Any power of 3 above 81 doesn't fit into our sequence.
Finally, we have 33+11+4+1=49.
Our final answer is 49.
(Note that I oversimplified this a lot, in real life we wouldn't have to list out the sequences as tediously as I did).

## Solution 4
We are obviously searching for multiples of three set S of odd numbers 1-199. Starting with 3, every number $\equiv 2 \pmod{3}$ in set S will be divisible by 3. In other words, every number $\equiv 3 \pmod{6}$ . This is because the LCM must be divisible by 3, and 2, because the set is comprised of only odd numbers. Using some simple math, there are 33 numbers that fit this description. All you have to do is find the largest odd number that is divisible by 3 and below 200, then add 3 and divide by 6. Next, we find the number of odd digits below 200 that are divisible by 9. The same strategy works, and gives us 11. 27 gives 3, and 81 gives 1. $33 + 11 + 4 + 1 = \boxed{49}$ .
-jackshi2006
- Number Theory
These problems are copyrighted © by the Mathematical Association of America.