# 2003 AIME I Problem 13

## Problem

Let $N$ be the number of positive integers that are less than or equal to $2003$ and whose base- $2$ representation has more $1$ 's than $0$ 's. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
In base- $2$ representation, all positive numbers have a leftmost digit of $1$ . Thus there are ${n \choose k}$ numbers that have $n+1$ digits in base $2$ notation, with $k+1$ of the digits being $1$ 's.
In order for there to be more $1$ 's than $0$ 's, we must have $k+1 > \frac{n+1}{2} \implies k > \frac{n-1}{2} \implies k \ge \frac{n}{2}$ . Therefore, the number of such numbers corresponds to the sum of all numbers on or to the right of the vertical line of symmetry in Pascal's Triangle , from rows $0$ to $10$ (as $2003 < 2^{11}-1$ ). Since the sum of the elements of the $r$ th row is $2^r$ , it follows that the sum of all elements in rows $0$ through $10$ is $2^0 + 2^1 + \cdots + 2^{10} = 2^{11}-1 = 2047$ . The center elements are in the form ${2i \choose i}$ , so the sum of these elements is $\sum_{i=0}^{5} {2i \choose i} = 1 + 2 +6 + 20 + 70 + 252 = 351$ .
The sum of the elements on or to the right of the line of symmetry is thus $\frac{2047 + 351}{2} = 1199$ . However, we also counted the $44$ numbers from $2004$ to $2^{11}-1 = 2047$ . Indeed, all of these numbers have at least $6$ $1$ 's in their base- $2$ representation, as all of them are greater than $1984 = 11111000000_2$ , which has $5$ $1$ 's. Therefore, our answer is $1199 - 44 = 1155$ , and the remainder is $\boxed{155}$ .

## Solution 2
We seek the number of allowed numbers which have $k$ 1's, not including the leading 1, for $k=0, 1, 2, \ldots , 10$ .
For $k=0,\ldots , 4$ , this number is
$\binom{k}{k}+\binom{k+1}{k}+\cdots+\binom{2k}{k}$ .
By the Hockey Stick Identity, this is equal to $\binom{2k+1}{k+1}$ . So we get
$\binom{1}{1}+\binom{3}{2}+\binom{5}{3}+\binom{7}{4}+\binom{9}{5}=175$ .
For $k=5,\ldots , 10$ , we end on $\binom{10}{k}$ - we don't want to consider numbers with more than 11 digits. So for each $k$ we get
$\binom{k}{k}+\binom{k+1}{k}+\ldots+\binom{10}{k}=\binom{11}{k+1}$
again by the Hockey Stick Identity. So we get
$\binom{11}{6}+\binom{11}{7}+\binom{11}{8}+\binom{11}{9}+\binom{11}{10}+\binom{11}{11}=\frac{2^{11}}{2}=2^{10}=1024$ .
The total is $1024+175=1199$ . Subtracting out the $44$ numbers between $2003$ and $2048$ gives $1155$ . Thus the answer is $155$ .

## Solution 3
We will count the number of it $< 2^{11}=2048$ instead of $2003$ (In other words, the length of the base-2 representation is at most $11$ . If there are even digits, $2n$ , then the leftmost digit is $1$ , the rest, $2n-1$ , has odd number of digits. In order for the base-2 representation to have more $1$ 's, we will need more $1$ in the remaining $2n-1$ than $0$ 's. Using symmetry, this is equal to $\frac{2^9+2^7+..+2^1}{2}$ Using similar argument where there are odd amount of digits. The remaining even amount of digit must contains the number of $1$ 's at least as the number of $0$ 's. So it's equal to $\frac{\binom{10}{5}+2^{10}+\binom{8}{4}+2^8+\binom{6}{3}+2^6+...+\binom{0}{0}+2^0}{2}$ Summing both cases, we have $\frac{2^0+2^1+..+2^{10}+\binom{0}{0}+..+\binom{10}{5}}{2} = 199$ . There are $44$ numbers between $2004$ and $2047$ inclusive that satisfy it. So the answer is $199-44=\boxed{155}$
~minor edits by minediamonds
These problems are copyrighted © by the Mathematical Association of America.