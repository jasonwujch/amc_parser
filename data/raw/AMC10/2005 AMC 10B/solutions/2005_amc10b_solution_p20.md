# 2005 AMC 10B Problem 20

## Problem

What is the average (mean) of all 5-digit numbers that can be formed by using each of the digits 1, 3, 5, 7, and 8 exactly once?

$\textbf{(A) }48000\qquad\textbf{(B) }49999.5\qquad\textbf{(C) }53332.8\qquad\textbf{(D) }55555\qquad\textbf{(E) }56432.8$

## Solution 1 (Expectation)
The average of all valid numbers is simply the expected value of a randomly chosen valid number. In other words, it is $E[\text{ten thousands digit}]\cdot 10^4+E[\text{thousands digit}]\cdot 10^3+\cdots+E[\text{ones digit}]\cdot 1$ . However, every digit is equally likely to be chosen for every place, so we can simplify this to $\frac{1+3+5+7+8}{5}\cdot(10^4+10^3+10^2+10^1+1)$ $=4.8\cdot11111 = \boxed{(C) 53332.8}$ .

## Solution 2
We first look at how many times each number will appear in each slot. If we fix a number in a slot, then there are $4! = 24$ ways to arrange the other numbers, so each number appears in each spot $24$ times. Therefore, the sum of all such numbers is $24 \times (1+3+5+7+8) \times (11111) = 24 \times 24 \times 11111 = 6399936.$ Since there are $5! = 120$ such numbers, we divide $6399936 \div 120$ to get $\boxed{\textbf{(C) }53332.8}$

## Solution 3
We can first solve for the mean for the digits $1, 3, 5, 7,$ and $9$ since each is $2$ away from each other. The mean of the numbers than can be solved using these digits is $55555$ . The total amount of numbers that can be formed using these digits is $5! =120$ . The sum of these numbers is $55555(120) = 6666600$ . Now we can find out the total value that was gained by replacing the $8$ with a $9$ . We can start how be calculating the gain when the $8$ was in the ones digit. Since there are $4! = 24$ numbers with the $8$ in the ones digit and $1$ was gain from each of them, $24$ is the number gained. Then, we repeat this with the tens, hundreds, thousands, and ten thousands place, leading to a total of $24+240+2400+24000+240000=266664$ as the total amount that was gained. Subtract this amount from the sum of the digits using the $9$ instead of the $8$ to get $6666600-266664=6399936$ . Finally, we divide this by $120$ to get the average. $\frac{6399936}{120}= \boxed{\textbf{(C) }53332.8}$

## Video Solution
https://www.youtube.com/watch?v=Ha3xtyz5bME ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .