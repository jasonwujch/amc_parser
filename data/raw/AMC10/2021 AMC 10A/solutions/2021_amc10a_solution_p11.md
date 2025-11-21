# 2021 AMC 10A Problem 11

## Problem

For which of the following integers $b$ is the base- $b$ number $2021_b - 221_b$ not divisible by $3$ ?

$\textbf{(A)} ~3 \qquad\textbf{(B)} ~4\qquad\textbf{(C)} ~6\qquad\textbf{(D)} ~7\qquad\textbf{(E)} ~8$

## Solution 1 (Factor)
We have \begin{align*} 2021_b - 221_b &= (2021_b - 21_b) - (221_b - 21_b) \\ &= 2000_b - 200_b \\ &= 2b^3 - 2b^2 \\ &= 2b^2(b-1), \end{align*} which is divisible by $3$ unless $b\equiv2\pmod{3}.$ The only choice congruent to $2$ modulo $3$ is $\boxed{\textbf{(E)} ~8}.$
~MRENTHUSIASM

## Solution 2 (Vertical Subtraction)
Vertically subtracting $2021_b - 221_b,$ we see that the ones place becomes $0,$ and so does the $b^1$ place. Then, we perform a carry (make sure the carry is in base $b$ ). Let $b-2 = A.$ Then, we have our final number as \[1A00_b.\] Now, when expanding, we see that this number is simply $b^3 - (b - 2)^2.$
Now, notice that the final number will only be congruent to \[b^3-(b-2)^2\equiv0\pmod{3}.\] If either $b\equiv0\pmod{3},$ or if $b\equiv1\pmod{3}$ (because note that $(b - 2)^2$ would become $\equiv1\pmod{3},$ and $b^3$ would become $\equiv1\pmod{3}$ as well, and therefore the final expression would become $1-1\equiv0\pmod{3}.$ Therefore, $b$ must be $\equiv2\pmod{3}.$ Among the answers, only $8$ is $\equiv2\pmod{3},$ and therefore our answer is $\boxed{\textbf{(E)} ~8}.$
~icecreamrolls8

## Solution 3 (Answer Choices)
By the definition of bases, we have \[2021_b - 221_b = \left(2b^3+2b+1\right) - \left(2b^2+2b+1\right).\] For values $b_1$ and $b_2$ such that $b_1\equiv b_2\pmod{3},$ we get \[\left(2b_1^3+2b_1+1\right) - \left(2b_1^2+2b_1+1\right) \equiv \left(2b_2^3+2b_2+1\right) - \left(2b_2^2+2b_2+1\right) \pmod{3}.\] Note that answer choices $\textbf{(A)},\textbf{(B)},\textbf{(C)},\textbf{(D)},\textbf{(E)}$ are congruent to $0,1,0,1,2$ modulo $3,$ respectively. So, $\textbf{(A)}$ and $\textbf{(C)}$ are either both correct or both incorrect. Since there is only one correct answer, $\textbf{(A)}$ and $\textbf{(C)}$ are both incorrect. Similarly, $\textbf{(B)}$ and $\textbf{(D)}$ are both incorrect. This leaves us with $\boxed{\textbf{(E)} ~8},$ the answer choice with a unique residue modulo $3.$
~ emerald_block ~MRENTHUSIASM

## Solution 4 (like Solution 1)
As with the beginning of Solution 1, we get that 3 does not divide $2b^2(b-1)$ . We can just test each answer choice (doing short circuit evaluation for $3$ and $6$ ), and finding that only $\boxed{\textbf{(E)} ~8}$ works. Honestly, Solution 1 is easier, but during an actual test when your brain is fried, I'd just check each option.
~vaishnav

## Video Solution by Omega Learn
https://youtu.be/CPYCUnL_Yc0
~ pi_is_3.14

## Video Solution (Simple and Quick)
https://youtu.be/1TZ1uI9z8fU
~ Education, the Study of Everything

## Video Solution
https://www.youtube.com/watch?v=XBfRVYx64dA&list=PLexHyfQ8DMuKqltG3cHT7Di4jhVl6L4YJ&index=10
~North America Math Contest Go Go Go

## Video Solution
https://youtu.be/zYIuBXDhJJA
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/t-EEP2V4nAE
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .