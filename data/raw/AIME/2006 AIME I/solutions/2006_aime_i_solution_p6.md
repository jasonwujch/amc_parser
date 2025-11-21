# 2006 AIME I Problem 6

## Problem

Let $\mathcal{S}$ be the set of real numbers that can be represented as repeating decimals of the form $0.\overline{abc}$ where $a, b, c$ are distinct digits . Find the sum of the elements of $\mathcal{S}.$

## Solution 1
Numbers of the form $0.\overline{abc}$ can be written as $\frac{abc}{999}$ . There are $10\times9\times8=720$ such numbers. Each digit will appear in each place value $\frac{720}{10}=72$ times, and the sum of the digits, 0 through 9, is 45. So the sum of all the numbers is $\frac{45\times72\times111}{999}= \boxed{360}$ .

## Solution 2
Alternatively, for every number, $0.\overline{abc}$ , there will be exactly one other number, such that when they are added together, the sum is $0.\overline{999}$ , or, more precisely, 1. As an example, $.\overline{123}+.\overline{876}=.\overline{999} \Longrightarrow 1$ .
Thus, the solution can be determined by dividing the total number of permutations by 2. The answer is $\frac{10 \cdot 9 \cdot 8}{2} = \frac{720}{2}= \boxed{360}$ .
Another method, albeit a little risky, that can be used is to note that the numbers between 1 and 999 with distinct digits average out to $\frac{999}{2}$ . Then the total sum becomes $\frac{\frac{999}{2}\times720}{999}$ which reduces to $\boxed{360}$

## Solution 3
Another way is to do complementary counting and casework. $0.\overline{abc} = abc/999$ . Excluding numbers with repeating digits our answer would just be $\frac{999 \cdot (1000/2)}{999} = 500$ . We subtract off the sum of the numbers with at least two digits being the same:
Case 1: $aba$ : Sum = $1010(1 + 2 + 3 + \dots + 9) + 450\cdot 10 = 999 \cdot 50$ .
Case 2: $aab$ : Sum = $1100(1 + 2 + 3 + \dots + 9) + 45\cdot 10 = 999 \cdot 50$
Case 3: $baa$ : Sum = $110(1 + 2 + 3 + \dots + 9) + 4500\cdot 10 = 999 \cdot 50$ .
We overcounted the case where $a = b$ twice (the numbers with all 3 digits being the same). The sum of these numbers is $111(1 + 2 + 3 + \dots + 9) = 999 \cdot 5$ .
So, our final answer is $\frac{999 \cdot 500 - 999 \cdot 150 + 999 \cdot 5 \cdot 2}{999} = \boxed{360}$ .
~ grogg007
These problems are copyrighted © by the Mathematical Association of America.