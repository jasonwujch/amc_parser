# 2002 AMC 10B Problem 20

## Problem

Let $a$ , $b$ , and $c$ be real numbers such that $a-7b+8c=4$ and $8a+4b-c=7$ . Then $a^2-b^2+c^2$ is

$\mathrm{(A)\ }0\qquad\mathrm{(B)\ }1\qquad\mathrm{(C)\ }4\qquad\mathrm{(D)\ }7\qquad\mathrm{(E)\ }8$

## Solutions

## Solution 1
Rearranging, we get $a+8c=7b+4$ and $8a-c=7-4b$
Squaring both, $a^2+16ac+64c^2=49b^2+56b+16$ and $64a^2-16ac+c^2=16b^2-56b+49$ are obtained.
Adding the two equations and dividing by $65$ gives $a^2+c^2=b^2+1$ , so $a^2-b^2+c^2=\boxed{(\text{B})1}$ .

## Solution 2
The easiest way is to assume a value for $a$ and then solve the system of equations. For $a = 1$ , we get the equations $-7b + 8c = 3$ and $4b - c = -1$ Multiplying the second equation by $8$ , we have $32b - 8c = -8$ Adding up the two equations yields $25b = -5$ , so $b = -\frac{1}{5}$ We obtain $c = \frac{1}{5}$ after plugging in the value for $b$ . Therefore, $a^2-b^2+c^2 = 1-\frac{1}{25}+\frac{1}{25}=\boxed{1}$ which corresponds to $\text{(B)}$ . This time-saving trick works only because we know that for any value of $a$ , $a^2-b^2+c^2$ will always be constant (it's a contest), so any value of $a$ will work. This is also called without loss of generality or WLOG.

## Solution 3 (fakesolve)
Notice that the coefficients of $a$ and $c$ are pretty similar (15s for reading and noticing), so let $b=0$ gives $a+8c=4$ , and $8a-c=7$ (10s writing). Since the desired quantity simplifies to $a^2+c^2$ , the $ac$ term of the quadratics after squaring gets canceled by adding up the squares of the two equations because they have the same coefficients but opposite sign (15s mind-binom). This simplifies to $65(a^2+c^2)=16+49$ , or $a^2-b^2+c^2=\frac{65}{65}=\boxed{1}$ (15s writing and addition and fraction simplification and (B) circling and submission)

## Solution 4 (very simple)
Note that the answer choices list different numbers, as opposed to an expression involving variables. This means that the expression $a^2-b^2+c^2$ evaluates to a constant. This means that we can assume $a = 0$ since the expression will stay the same for any value of a. Then since $a = 0$ and $8a = 8 \cdot 0 = 0$ , the equations given in the problem become $-7b + 8c = 4$ and $4b - c = 7$ . Multiplying the second equation, we obtain $32b - 8c = 56$ . Adding this to our first equation, this gives us $25b = 60$ , so $b = 60/25 = 12/5$ . Plugging this into $4b - c = 7$ , we get $4(12/5) - c = 7 \implies 48/5 - c = 35/5 \implies c = 13/5$ . Then, $a^2-b^2+c^2 = 0^2 - (12/5)^2 + (13/5)^2 = -144/25 + 169/25 = 25/25 = \boxed{1 (B)}$ .
- Loquacious_Autodidact

## Video Solution
https://www.youtube.com/watch?v=3Oq21r5OezA ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .