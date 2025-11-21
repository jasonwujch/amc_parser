# 2012 AIME II Problem 12

## Problem

For a positive integer $p$ , define the positive integer $n$ to be $p$ -safe if $n$ differs in absolute value by more than $2$ from all multiples of $p$ . For example, the set of $10$ -safe numbers is $\{ 3, 4, 5, 6, 7, 13, 14, 15, 16, 17, 23, \ldots\}$ . Find the number of positive integers less than or equal to $10,000$ which are simultaneously $7$ -safe, $11$ -safe, and $13$ -safe.

## Solution
We see that a number $n$ is $p$ -safe if and only if the residue of $n \mod p$ is greater than $2$ and less than $p-2$ ; thus, there are $p-5$ residues $\mod p$ that a $p$ -safe number can have. Therefore, a number $n$ satisfying the conditions of the problem can have $2$ different residues $\mod 7$ , $6$ different residues $\mod 11$ , and $8$ different residues $\mod 13$ . The Chinese Remainder Theorem states that for a number $x$ that is $a$ (mod b) $c$ (mod d) $e$ (mod f) has one solution if $\gcd(b,d,f)=1$ . For example, in our case, the number $n$ can be: 3 (mod 7) 3 (mod 11) 7 (mod 13) so since $\gcd(7,11,13)$ =1, there is 1 solution for n for this case of residues of $n$ .
This means that by the Chinese Remainder Theorem, $n$ can have $2\cdot 6 \cdot 8 = 96$ different residues mod $7 \cdot 11 \cdot 13 = 1001$ . Thus, there are $960$ values of $n$ satisfying the conditions in the range $0 < n \le 10010$ . However, we must now remove any values greater than $10000$ that satisfy the conditions. By checking residues, we easily see that the only such values are $10006$ and $10007$ , so there remain $\fbox{958}$ values satisfying the conditions of the problem.
- We can also say $\frac{2}{7}$ of all numbers are 7-safe, $\frac{6}{11}$ of all numbers are 11-safe, and $\frac{8}{13}$ of all numbers are 13-safe. We can multiply these to get that $\frac{96}{1001}$ of all numbers are simultaneously 7-safe, 11-safe, and 13-safe.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .