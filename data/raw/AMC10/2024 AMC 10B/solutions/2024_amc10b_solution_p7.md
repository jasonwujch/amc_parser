# 2024 AMC 10B Problem 7

## Problem

What is the remainder when $7^{2024}+7^{2025}+7^{2026}$ is divided by $19$ ?

$\textbf{(A) } 0 \qquad\textbf{(B) } 1 \qquad\textbf{(C) } 7 \qquad\textbf{(D) } 11 \qquad\textbf{(E) } 18$

## Solution 1
We can factor the expression as
\[7^{2024} (1 + 7 + 7^2) = 7^{2024} (57).\]
Note that $57=19\cdot3$ , this expression is actually divisible by 19. The answer is $\boxed{\textbf{(A) } 0}$ .

## Solution 2
If you failed to realize that the expression can be factored, you might also apply modular arithmetic to solve the problem.
Since $7^3\equiv1\pmod{19}$ , the powers of $7$ repeat every three terms:
\[7^1\equiv7\pmod{19}\] \[7^2\equiv11\pmod{19}\] \[7^3\equiv1\pmod{19}\]
The fact that $2024\equiv2\pmod3$ , $2025\equiv0\pmod3$ , and $2026\equiv1\pmod3$ implies that $7^{2024}+7^{2025}+7^{2026}\equiv11+1+7\equiv19 \equiv0\pmod{19}$ .
~ Bloggish

## Solution 3
We start the same as solution 2, and find that:
\[7^1\equiv7\pmod{19}\] \[7^2\equiv11\pmod{19}\] \[7^3\equiv1\pmod{19}\]
We know that for $2024$ , $2025$ , and $2026$ , because there are three terms, we can just add them up. $1 + 7 + 11 = 19$ , which is $0$ mod $19$ .

## Solution 4 (Given more advanced knowledge)
By Fermat's Little Theorem (FLT), we know that \[7^{18}\equiv1\pmod{19}\] Then its order must divide $18$ . Trying simple values we try and succeed: \[7^3\equiv1\pmod{19}\]
So the expression is equivalent to $1+7+49\pmod{19}$ , which gives $\boxed{\textbf{(A) } 0}$ when divided by 19.
~xHypotenuse

## Solution 5 (Basic Mod Almost same as sol one)
$7^{2024} * (1+7+49) == 0 (mod 19)$ $57 == 0 mod 19$
so it is just $\boxed{\textbf{(A) } 0}$ .
~Cheerfulfrog

## 🎥✨ Video Solution by Scholars Foundation ➡️ (Easy-to-Understand 💡✔️)
https://youtu.be/T_QESWAKUUk?si=5euBbKNMaYBROuTV&t=100

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/QLziG_2e7CY?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=24EZaeAThuE

## Video Solution by TheBeautyofMath
https://youtu.be/ZaHv4UkXcbs?t=208
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .