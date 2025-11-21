# 2006 AIME II Problem 7

## Problem

Find the number of ordered pairs of positive integers $(a,b)$ such that $a+b=1000$ and neither $a$ nor $b$ has a zero digit.

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4 (Similar to Solution 2) 2.5 Solution 5

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4 (Similar to Solution 2)

- 2.5 Solution 5

## Solution

## Solution 1
There are $\left\lfloor\frac{999}{10}\right\rfloor = 99$ numbers up to 1000 that have 0 as their units digit. All of the other excluded possibilities are when $a$ or $b$ have a 0 in the tens digit, and since the equation is symmetric, we will just count when $a$ has a 0 in the tens digit and multiply by 2 (notice that the only time both $a$ and $b$ can have a 0 in the tens digit is when they are divisible by 100, which falls into the above category, so we do not have to worry about overcounting ).
Excluding the numbers divisible by 100, which were counted already, there are $9$ numbers in every hundred numbers that have a tens digit of 0 (this is true from 100 to 900), totaling $9 \cdot 9 = 81$ such numbers; considering $b$ also and we have $81 \cdot 2 = 162$ . Therefore, there are $999 - (99 + 162) = \boxed{738}$ such ordered pairs.

## Solution 2
Let $a = \overline{cde}$ and $b = \overline{fgh}$ be 3 digit numbers:
$e$ and $h$ must add up to $10$ , $d$ and $g$ must add up to $9$ , and $c$ and $f$ must add up to $9$ . Since none of the digits can be 0, there are $9 \times 8 \times 8=576$ possibilites if both numbers are three digits.
There are two other scenarios. $a$ and $b$ can be a three digit number and a two digit number, or a three digit number and a one digit number. For the first scenario, there are $9 \times 8 \times 2=144$ possibilities (the two accounting for whether $a$ or $b$ has three digits) and for the second case there are $9 \times 2=18$ possibilities. Thus, thus total possibilities for $(a,b)$ is $576+144+18=738$ .

## Solution 3
We first must notice that we can find all the possible values of $a$ between $1$ and $500$ and then double that result.
When $1 < a < 100$ there are $9\times9 = 81$ possible solution for $a$ so that neither $a$ nor $b$ has a zero in it, counting $1$ through $9$ , $11$ through $19$ , ..., $81$ through $89$ . When $100 < a < 200$ there are $9\times8 =72$ possible solution for a so that neither a nor b has a zero in it, counting $111$ through $119$ , $121$ through $129$ , ..., $181$ through $189$ . This can clearly be extended to $100k < a < 100(k+1)$ where $k$ is an integer and $0 <k < 9$ . Thus for $100 < a < 500$ there are $72\times4$ = $288$ possible values of $a$ .
Thus when $1 < a < 500$ there are $288 + 81 =369$ possible values of $a$ and $b$ .
Doubling this yields $369\times2= 738$ .

## Solution 4 (Similar to Solution 2)
We proceed by casework on the number of digits of $a.$
Case 1: Both $a$ and $b$ have three digits
We now use constructive counting. For the hundreds digit of $a,$ we see that there are $8$ options - the numbers $1$ through $8.$ (If $a = 9,$ that means that $b$ will be a two digit number, and if $a = 0,$ $a$ will have two digits). Similarly, the tens digit can be $1-8$ as well because a tens digit of $0$ is obviously prohibited and a tens digit of $9$ will lead to a tens digit of $0$ in the other number. The units digit can be anything from $1-9.$ Hence, there are $8 \cdot 8 \cdot 9 = 576$ possible values in this case.
Case 2: $a$ (or $b$ ) has two digits
If $a$ has two digits, the only restrictions are that the units digit must not be $0$ and the tens digit must not be $9$ (because then that would lead to $b$ beginning with $90...$ ). There thus are $8 \cdot 9 = 72$ possibilities for $a,$ and we have to multiply by $2$ because there are the same number of possibilities for $b.$ Thus, there are $72 \cdot 2 = 144$ possible values in this case.
Case 3: $a$ (or $b$ ) has one digit
This is easy -- $a$ can be anything from $1$ to $9,$ for a total of $9$ possible values. We multiply this by $2$ to account for the single digit $b$ values, so we have $9 \cdot 2 = 18$ possible values for this case.
Adding them all up, we get $576 + 144 + 18 = \boxed{738},$ and we're done.
Solution by Ilikeapos

## Solution 5
For every $a \in [1, 999]$ , $(a, 1000 - a)$ is a potential candidate for a solution, barring the cases where $a$ or $1000 -a$ has zero digits.
First, let's consider all viable $a$ that do not have a zero digit. As there are 9 non-zero digits, we have:
- $9^1$ 1-digit numbers without a zero digit
- $9^2$ 2-digit numbers without a zero digit
- $9^3$ 3-digit numbers without a zero digit
However, we have still overlooked the cases where $1000 - a$ contains zero digits:
- Case 1 : If the one's digit of $1000 - a$ is zero, then $a$ will trivially end in a zero, which we've already excluded.
- Case 2 : If the ten's digit of $1000 - a$ is zero, with digital representation $\overline{X0Y}$ , then $a$ has the digital representation $\overline{[9-X]9[10-Y]}$ . $X$ and $Y$ can each take on any value in $[1, 9]$ to produce a value in our set of potential $a$ . There are thus $9^2$ cases that we overlooked, where $a$ had no zero digits, but $1000 - a$ did.
Adding up the cases with $a \in [1, 999]$ with no zero digits and removing the cases with $1000 - a$ with zero digits gives us \[(9^1 + 9^2 + 9^3) - 9^2 = \boxed{738}\]
~SaifHakim
These problems are copyrighted © by the Mathematical Association of America.