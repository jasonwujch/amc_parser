# 2018 AMC 8 Problem 14

## Problem

Let $N$ be the greatest five-digit number whose digits have a product of $120$ . What is the sum of the digits of $N$ ?

$\textbf{(A) }15\qquad\textbf{(B) }16\qquad\textbf{(C) }17\qquad\textbf{(D) }18\qquad\textbf{(E) }20$

## Solution 1
If we start off with the first digit, we know that it can't be $9$ since $9$ is not a factor of $120$ . We go down to the digit $8$ , which does work since it is a factor of $120$ . Now, we have to know what digits will take up the remaining four spots. To find this result, just divide $\frac{120}{8}=15$ . The next place can be $5$ , as it is the largest factor, aside from $15$ . Consequently, our next three values will be $3,1$ and $1$ if we use the same logic. Therefore, our five-digit number is $85311$ , so the sum is $8+5+3+1+1=18\implies \boxed{\textbf{(D) }18}$ .

## Solution 2 (Factorial)
$120$ is $5!$ , so we have $(5)(4)(3)(2)(1) = 120$ . (Alternatively, you could identify the prime factors $(5)(3)(2)(2)(2) = 120$ .) Now look for the largest digit you can create by combining these factors.
$8=4 \cdot 2$
Use this largest digit for the ten-thousands place: $8$ _ , _ _ _
Next you use the $5$ and the $3$ for the next places: $85,3$ _ _ (You can't use $3 \cdot 2=6$ because the $2$ was used to make $8$ .)
Fill the remaining places with 1: $85,311$
$= (5)(8)(3)(1)(1) =120$
$8+5+3+1+1=\boxed{\textbf{(D) }18}$ .

## Video Solution (CREATIVE ANALYSIS!!!)
https://youtu.be/zxEO6amczPU
~Education, the Study of Everything

## Video Solutions
https://youtu.be/IAKhC_A0kok
https://youtu.be/7an5wU9Q5hk?t=13
https://youtu.be/Q5YrDW62VDU
~savannahsolver
### See Also