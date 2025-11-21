# 2011 AMC 10B Problem 19

## Problem

What is the product of all the roots of the equation \[\sqrt{5 | x | + 8} = \sqrt{x^2 - 16}.\]

$\textbf{(A)}\ -64 \qquad\textbf{(B)}\ -24 \qquad\textbf{(C)}\ -9 \qquad\textbf{(D)}\ 24 \qquad\textbf{(E)}\ 576$

## Solution 1
First, square both sides, and isolate the absolute value. \begin{align*} 5|x|+8&=x^2-16\\ 5|x|&=x^2-24\\ |x|&=\frac{x^2-24}{5}. \\ \end{align*} Solve for the absolute value and factor.
Case 1: $x=\frac{x^2-24}{5}$
Multiplying both sides by $5$ gives us \[5x=x^2-24.\] Rearranging and factoring, we have \begin{align*} x^2-5x-24 &=0, \\ (x-8)(x+3) &= 0.\\ \end{align*}
Case 2: $x=\frac{-x^2+24}{5}$
As above, we multiply both sides by $5$ to find \[5x=-x^2+24.\] Rearranging and factoring gives us \begin{align*} x^2+5x-24 &=0, \\ (x+8)(x-3) &= 0. \\ \end{align*}
Combining these cases, we have $x= -8, -3, 3, 8$ . Because our first step of squaring is not reversible, however, we need to check for extraneous solutions. Plug each solution for $x$ back into the original equation to ensure it works. Whether the number is positive or negative does not matter since the absolute value or square will cancel it out anyways. Trying $|x|=|3|$ , we have \begin{align*} \sqrt{5|3|+8}&=\sqrt{3^2-16}, \\ \sqrt{15+8}&=\sqrt{9-16}, \\ \sqrt{23} &\not= \sqrt{-7}.\\ \end{align*} Therefore, $x = 3$ and $x= -3$ are extraneous.
Checking $|x|=|8|$ , we have \begin{align*} \sqrt{5|8|+8}&=\sqrt{8^2-16}, \\ \sqrt{40+8}&=\sqrt{64-16}, \\ \sqrt{48}&=\sqrt{48}.\\ \end{align*}
The roots of our original equation are $-8$ and $8$ and product is $-8 \times 8 = \boxed{\textbf{(A)} -64}$ .

## Solution 2
Square both sides, to get $5|x| + 8 = x^2-16$ . Rearrange to get $x^2 - 5|x| - 24 = 0$ . Seeing that $x^2 = |x|^2$ , substitute to get $|x|^2 - 5|x| - 24 = 0$ . We see that this is a quadratic in $|x|$ . Factoring, we get $(|x|-8)(|x|+3) = 0$ , so $|x| = \{8,-3\}$ . Since the radicand of the equation can't be negative, the sole solution is $|x| = 8$ . Therefore, $x$ can be $8$ or $-8$ . The product is then $-8 \times 8 = \boxed{\textbf{(A)} -64}$ .

## Solution 3
First we note that $x \in (-\infty,-4] \cup [4,\infty]$ . This will help us later with finding extraneous solutions. Next, we have two cases: \[\text{IF } x\leq 4:\] \[\text{ } \sqrt{-5x+8} = \sqrt{x^2-16} \implies x^2+5x-24=0 \rightarrow x = -8,3\] . We note that $3$ is not in the range of possible $x$ 's and thus is not a solution.
\[\text{IF } x\geq 4:\] \[\text{ } \sqrt{5x+8} = \sqrt{x^2-16} \implies x^2-5x-24=0 \rightarrow x = -3,8\] . We again not that $-3$ is an extraneous solution.
Thus, we have the two solutions $-8$ and $8$ . Therefore product is $-8 \cdot 8 = \boxed{\textbf{(A)} -64}$ .
-ConfidentKoala4

## Solution 4
To make this problem easier to comprehend, we can define variable $a = |x|$ , with the condition that $a$ is always nonnegative. Also, since any number squared is always nonnegative, we can define $|x|^2 = x^2$ . Then we can square both sides and substitute: \[\sqrt{5 | x | + 8} = \sqrt{x^2 - 16} => 5a + 8 = a^2 - 16.\] Bringing the equation over to one side, we get: \[a^2 - 5a - 24 = 0.\] Solving for a by factoring, we get: \[a^2 - 5a - 24 = 0 = (a - 8)(a + 3) = 0,\] so $a = 8$ or $a = -3$ . But $a$ must be nonnegative, so the only value that works is $8$ . If $a = 8$ , then $|x| = 8$ and $x^2 = 8^2 = 64$ , so $x$ can equal $8 or -8$ . Multiplying the two, we get $8 * -8 = \boxed{\textbf{(A)} -64}$ .
~BeepTheSheep954

## Video Solution
https://youtu.be/ubGzkmVyAwE
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .