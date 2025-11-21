# 2020 AMC 10B Problem 22

## Problem

What is the remainder when $2^{202} +202$ is divided by $2^{101}+2^{51}+1$ ?

$\textbf{(A) } 100 \qquad\textbf{(B) } 101 \qquad\textbf{(C) } 200 \qquad\textbf{(D) } 201 \qquad\textbf{(E) } 202$

## Solution 1 (MAA Original Solution)
Completing the square, then difference of squares:
\begin{align*} 2^{202} + 202 &= (2^{101})^2 + 2\cdot 2^{101} + 1 - 2\cdot 2^{101} + 201\\ &= (2^{101} + 1)^2 - 2^{102} + 201\\ &= (2^{101} - 2^{51} + 1)(2^{101} + 2^{51} + 1) + 201. \end{align*}
Thus, we see that the remainder is $\boxed{\textbf{(D) } 201}$
(Source: https://artofproblemsolving.com/community/c5h2001950p14000817 )

## Solution 2
Let $x=2^{50}$ . We are now looking for the remainder of $\frac{4x^4+202}{2x^2+2x+1}$ .
We could proceed with polynomial division, but the numerator looks awfully similar to the Sophie Germain Identity , which states that \[a^4+4b^4=(a^2+2b^2+2ab)(a^2+2b^2-2ab)\]
Let's use the identity, with $a=1$ and $b=x$ , so we have
\[1+4x^4=(1+2x^2+2x)(1+2x^2-2x)\]
Rearranging, we can see that this is exactly what we need:
\[\frac{4x^4+1}{2x^2+2x+1}=2x^2-2x+1\]
So \[\frac{4x^4+202}{2x^2+2x+1} = \frac{4x^4+1}{2x^2+2x+1} +\frac{201}{2x^2+2x+1}\]
Since the first half divides cleanly as shown earlier, the remainder must be $\boxed{\textbf{(D) }201}$
~quacker88

## Solution 3 (Same As Solution 2)
We let \[x = 2^{50}\] and \[2^{202} + 202 = 4x^{4} + 202\] . Next we write \[2^{101} + 2^{51} + 1 = 2x^{2} + 2x + 1\] . We know that \[4x^{4} + 1 = (2x^{2} + 2x + 1)(2x^{2} - 2x + 1)\] by the Sophie Germain identity so to find \[4x^{4} + 202,\] we find that \[4x^{4} + 202 = 4x^{4} + 201 + 1\] which shows that the remainder is $\boxed{\textbf{(D) } 201}$

## Solution 4
We let $x=2^{50.5}$ . That means $2^{202}+202=x^{4}+202$ and $2^{101}+2^{51}+1=x^{2}+2^{0.5}x+1$ . Then, we simply do polynomial division, and find that the remainder is $\boxed{\textbf{(D) } 201}$ .
The long division is essentially the same if you work with $x=2$ , or do repeated multiplication and subtraction using the original expression.

## Solution 5 (Modular Arithmetic)
Let $n=2^{101}+2^{51}+1$ . Then, mod $n$ :
$2^{202}+202 \equiv (-2^{51}-1)^2 + 202$
$\equiv 2^{102}+2^{52}+203$
$= 2(n-1)+203 \equiv 201 \pmod{n}$ .
Thus, the remainder is $\boxed{\textbf{(D) } 201}$ .
~ Leo.Euler
~ (edited by asops)

## Solution 6 (by Shiva Kumar Kannan - Least insightful & very straightforward + Manipulation)
We can repeatedly manipulate the numerator to make parts of it divisible by the denominator:
\[\frac{2^{202}+202}{2^{101}+2^{51}+1}\] \[= \frac{2^{202} + 2^{152} + 2^{101}}{2^{101}+2^{51}+1} - \frac{2^{152} + 2^{101} - 202}{2^{101}+2^{51}+1}\] \[= 2^{101} - \frac{2^{152} + 2^{101} - 202}{2^{101}+2^{51}+1}\] \[=2^{101} - \frac{2^{152}+2^{101}+2^{101}+2^{51} - 2^{101} - 2^{51} - 202}{2^{101}+2^{51}+1}\] \[=2^{101} - 2^{51} + \frac{2^{101}+2^{51}+202}{2^{101}+2^{51}+1}\] \[= 2^{101} - 2^{51} + \frac{2^{101}+2^{51}+1+201}{2^{101}+2^{51}+1}\] \[= 2^{101} - 2^{51} + 1 + \frac{201}{2^{101} + 2^{51} + 1}.\]
Clearly, $201 < 2^{201} + 2^{51} + 1$ , hence, we cannot manipulate the numerator further to make the denominator divide into one of its parts. This concludes, that the remainder is $\boxed{\textbf{(D) } 201}$ .

## Video Solutions

## Video Solution 1 by Mathematical Dexterity (2 min)
https://www.youtube.com/watch?v=lLWURnmpPQA

## Video Solution 2 by The Beauty Of Math
https://youtu.be/gPqd-yKQdFg

## Video Solution 3
https://www.youtube.com/watch?v=Qs6UnryIAI8&list=PLLCzevlMcsWNcTZEaxHe8VaccrhubDOlQ&index=9&t=0s ~ MathEx

## Video Solution 4 Using Sophie Germain's Identity
https://youtu.be/ba6w1OhXqOQ?t=5155
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .