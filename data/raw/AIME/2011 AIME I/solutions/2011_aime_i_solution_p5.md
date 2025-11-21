# 2011 AIME I Problem 5

## Problem

The vertices of a regular nonagon (9-sided polygon) are to be labeled with the digits 1 through 9 in such a way that the sum of the numbers on every three consecutive vertices is a multiple of 3. Two acceptable arrangements are considered to be indistinguishable if one can be obtained from the other by rotating the nonagon in the plane. Find the number of distinguishable acceptable arrangements.

### Diagram

Red $0$ 's mean numbers divisible by 3, green $1$ 's and $2$ 's mean remainder of $1$ or $2$ when divided by $3$ .

~WhatdoHumanitariansEat

## Solution 1
First, we determine which possible combinations of digits $1$ through $9$ will yield sums that are multiples of $3$ . It is simplest to do this by looking at each of the digits $\bmod{3}$ .
We see that the numbers $1, 4,$ and $7$ are congruent to $1 \pmod{3}$ , that the numbers $2, 5,$ and $8$ are congruent to $2 \pmod{3}$ , and that the numbers $3, 6,$ and $9$ are congruent to $0 \pmod{3}$ . In order for a sum of three of these numbers to be a multiple of three, the mod $3$ sum must be congruent to $0$ . Quick inspection reveals that the only possible combinations are $0+0+0, 1+1+1, 2+2+2,$ and $0+1+2$ . However, every set of three consecutive vertices must sum to a multiple of three, so using any of $0+0+0, 1+1+1$ , or $2+2+2$ would cause an adjacent sum to include exactly $2$ digits with the same $\bmod{3}$ value, and this is an unacceptable arrangement. Thus the only possible groupings are composed of three digits congruent to three different $\bmod{3}$ values.
We see also that there are two possible arrangements for these trios on the nonagon: a digit congruent to $1 \pmod{3}$ can be located counterclockwise of a digit congruent to $0$ and clockwise of a digit congruent to $2 \pmod{3}$ , or the reverse can be true.
We set the first digit as $3$ avoid overcounting rotations, so we have one option as a choice for the first digit. The other two $0 \pmod{3}$ numbers can be arranged in $2!=2$ ways. The three $1 \pmod{3}$ and three $2 \pmod{3}$ can both be arranged in $3!=6$ ways. Therefore, the desired result is $2(2 \times 6 \times 6)=\boxed{144}$ .

## Solution 2
Notice that there are three triplets of congruent integers $\mod 3$ : $(1,4,7),$ $(2,5,8),$ and $(3,6,9).$ There are $3!$ ways to order each of the triplets individually and $3!$ ways to order the triplets as a group (see solution 1). Rotations are indistinguishable, so there are $(3!)^4/9=\boxed{144}$ total arrangements.

## Video solution
https://www.youtube.com/watch?v=vkniYGN45F4
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .