# 2006 AMC 10B Problem 11

## Problem

What is the tens digit in the sum $7!+8!+9!+...+2006!$

$\textbf{(A) } 1\qquad \textbf{(B) } 3\qquad \textbf{(C) } 4\qquad \textbf{(D) } 6\qquad \textbf{(E) } 9$

## Solution
Since $10!$ is divisible by $100$ , any factorial greater than $10!$ is also divisible by $100$ . The last two digits of all factorials greater than $10!$ are $00$ , so the last two digits of $10!+11!+...+2006!$ are $00$ . (*)
So all that is needed is the tens digit of the sum $7!+8!+9!$
$7!+8!+9!=5040+40320+362880=408240$
So the tens digit is $\boxed{\textbf{(C) }4}$ .
(*) A slightly faster method would be to take the $\pmod {100}$ residue of $7! + 8! + 9!.$ Since $7! = 5040,$ we can rewrite the sum as \[5040 + 8\cdot 5040 + 72\cdot 5040 \equiv 40 + 8\cdot 40 + 72\cdot 40 = 40 + 320 + 2880 \equiv 40 \pmod{100}.\] Since the last two digits of the sum is $40$ , the tens digit is $\boxed{\textbf{(C) }4}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .