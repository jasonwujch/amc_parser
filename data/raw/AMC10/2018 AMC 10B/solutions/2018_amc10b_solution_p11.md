# 2018 AMC 10B Problem 11

## Problem

Which of the following expressions is never a prime number when $p$ is a prime number?

$\textbf{(A) } p^2+16 \qquad \textbf{(B) } p^2+24 \qquad \textbf{(C) } p^2+26 \qquad \textbf{(D) } p^2+46 \qquad \textbf{(E) } p^2+96$

## Solution 1
Each expression is in the form $p^2 + n$ .
All prime numbers are of the form $6k \pm 1$ , AKA they are congruent to $\pm1 \pmod{6}$ . We can utilize this nicely to check for what we are looking for. If the expression is a prime, then
$p^2 + n \equiv \pm1 \pmod{6}$
$\Rightarrow (\pm1)^2 + n \equiv \pm1 \pmod{6}$
$\Rightarrow 1 + n \equiv \pm1 \pmod{6}$
$\Rightarrow n \equiv (\pm1) - 1 \pmod{6}$
$\Rightarrow n \equiv (1$ $or$ $-1) - 1 \pmod{6}$
$\Rightarrow n \equiv 0$ $or$ $-2 \pmod{6}$
Now, just check for $n$ in each option using this condition to check whether its prime or not.
\[(A)\ n = 16; prime\] \[(B)\ n = 24; prime\] \[(C)\ n = 26; not\ prime\] \[(D)\ n = 46; prime\] \[(E)\ n = 96; prime\]
Therefore, the answer is $\boxed{\textbf{(C) } p^2 + 26}$ .
~ $shalomkeshet$

## Solution 2
Because squares of a non-multiple of 3 is always $1 \pmod{3}$ , the only expression always a multiple of $3$ is $\boxed{\textbf{(C) } p^2+26}$ . This is excluding when $p\equiv 0 \pmod{3}$ , which only occurs when $p=3$ , then $p^2+26=35$ which is still composite.

## Solution 3
\( p^2 + 16 \) is prime for \( p = 5 \), so we know that \( A \) doesn't work.
Because \( p^2 + 96 = p^2 + (16) \cdot 6 \), we see that eventually there exists a number \( p \) that makes the sum prime, therefore \( E \) also doesn't work.
Option \( B \) is \( p^2 + 24 \), but because the number itself has no carryover, we can assume \( p = 5 \) again to get the number \( 41 \), which is prime.
Option \( D \) is \( p^2 + 46 \), ending in \( 6 \), so we try \( p = 5 \) again to get \( 71 \). This is also prime.
We can either deduce through elimination that \( p^2 + 26 \) is always composite for any prime \( p \), but we can prove it by showing \( p = 5 \) doesn't work, \( p = 7 \) doesn't work, and \( p = 11 \) doesn't work, and through Engineer's Induction , \( p^2 + 26 \) always remains composite.
Therefore the answer is $\boxed{\textbf{(C) } p^2 + 26}$ .
~Pinotation

## Solution 4 (Answer Choices)
Since the question asks which of the following will never be a prime number when $p$ is a prime number, a way to find the answer is by trying to find a value for $p$ such that the statement above won't be true.
A) $p^2+16$ isn't true when $p=5$ because $25+16=41$ , which is prime
B) $p^2+24$ isn't true when $p=7$ because $49+24=73$ , which is prime
C) $p^2+26$
D) $p^2+46$ isn't true when $p=5$ because $25+46=71$ , which is prime
E) $p^2+96$ isn't true when $p=19$ because $361+96=457$ , which is prime
Therefore, $\framebox{C}$ is the correct answer.
-DAWAE
Minor edit by Lucky1256. P=___ was the wrong number.
More minor edits by beanlol.
More minor edits by mathmonkey12.

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/PyCyMEBQCXM
~Education, the Study of Everything

## Video Solution 1
https://youtu.be/XRCWccGFnds

## Video Solution 2
https://youtu.be/3bRjcrkd5mQ?t=187
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .