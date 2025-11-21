# 2025 AMC 12B Problem 4

## Problem

The value of the two-digit number $\underline{a}~\underline{b}$ in base seven equals the value of the two-digit number $\underline{b}~\underline{a}$ in base nine. What is $a+b?$

$\textbf{(A)}~7\qquad\textbf{(B)}~9\qquad\textbf{(C)}~10\qquad\textbf{(D)}~11\qquad\textbf{(E)}~14$

## Solution 1
By definition of bases, $\underline{a}~\underline{b}$ base seven is equal to $7a+b$ , and $\underline{b}~\underline{a}$ base nine is equal to $9b+a$ . Therefore, we must have $7a+b=9b+a$ , or $6a=8b$ , or $3a=4b$ . But in base seven, we must have $a,b<7$ . Testing cases yields $a=4,b=3$ as the only solution. Their sum is $\boxed{\textbf{(A)}~7}$ .
~Note that $lcm(6,8) = 24$ , which should reveal the answer a lot faster than testing.
~ eevee9406
~ CW
### Remark
The first equation comes from the following idea. In base $10$ , a two-digit number can be represented as $10$ times the tens digit plus the units digit, or $10^1 \cdot a + 10^0 \cdot b$ . If we insert the base numbers into this expression for $\underline{a}~\underline{b}$ and $\underline{b}~\underline{a}$ , we get $7^1 \cdot a + b = 9^1 \cdot b + a$ . The rest of the solution is above.
Note that this method applies to any number of digits as well as decimals. ~OlympiadMaster

## Solution 2 (Answer Choices)
Since $a$ and $b$ are both digits base $7$ , they must be from $0$ to $6$ . Furthermore, $\underline{a}$ must be strictly greater than $b$ because two-digit representations in base $7$ exceed the values of those in base $9$ . Starting from testing $\text{(A)}$ , we see that the combination $(a, b) = (4, 3)$ satisfies the condition. The answer is $\boxed{\textbf{(A)}~7}$ .
~megaboy6679

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=4uIAAy7jvE8 ~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution by Daily Dose of Math
https://youtu.be/s-Wimgu9wto
~Thesmartgreekmathdude
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .