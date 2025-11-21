# 2025 AMC 10B Problem 22

## Problem

A seven-digit positive integer is chosen at random. What is the probability that the number is divisible by $11$ , given that the sum of its digits is $61?$

$\textbf{(A) }\frac{3}{14}\qquad\textbf{(B) }\frac{3}{11}\qquad\textbf{(C) }\frac{2}{7}\qquad\textbf{(D) }\frac{4}{11}\qquad\textbf{(E) }\frac{3}{7}$

## Solution 1
Let the number be represented as $\overline{a_1a_2a_3a_4a_5a_6a_7}.$
We first seek to find the number of seven-digit integers with $a_1+a_2+a_3+a_4+a_5+a_6+a_7 = 61.$ We would love to do stars and bars here, but we have the condition that $0 \leq a_n \leq 9.$ Therefore, we define $a_n' = 9-a_n \implies a_n = 9-a_n'.$ This is a bijective operation, so the total number of integers doesn't change when we use these digits instead. Substituting in gives that
\begin{align*} \sum_{k=1}^{7}{(9-a'_k)} &= 61, \\ a_1' + a_2' + a_3' + a_4' + a_5' + a_6' + a_7' &= 2. \end{align*}
Since the $a_n'$ are nonnegative integers and the condition $a_n' \leq 9$ doesn't matter with a sum less than 9, we can do stars and bars to figure out the number of permutations of digits that satisfy the constraint: ${{2+6}\choose {2}} = {8\choose 2} = 28.$
Now, we need to find how many of these integers are divisible by $11.$ We can use the divisibility by $11$ rule, which says that $(a_1+a_3+a_5+a_7) - (a_2+a_4+a_6) = 11k$ for some integer $k.$ Notice that $k \geq 1$ because, otherwise, $a_2+a_4+a_6 > 27$ which is the maximum sum of three digits. In addition, $k \leq 1$ because, otherwise $a_1+a_3+a_5+a_7 > 36$ which is the maximum sum of four digits. Therefore $k = 1.$
Then we have that $(a_1+a_3+a_5+a_7) - (a_2+a_4+a_6) = 11,$ so $a_1+a_3+a_5+a_7 = 36$ and $a_2+a_4+a_6 = 25.$ The first equation can only result in $a_1=a_3=a_5=a_7 = 9.$ The second equation can be rewritten in a similar manner as before to get that \begin{align*} (9-a_2') + (9-a_4') + (9-a_6') &= 25, \\ a_2' + a_4' + a_6' &= 2. \end{align*}
Again, with stars and bars, there exists ${{2+2}\choose {2}} = {4\choose 2} = 6$ ordered triples of $(a_2, a_4, a_6)$ .
Therefore, our answer is \[\frac{6}{28} = \boxed{\text{(A)\ } \frac{3}{14}}.\]
~vaisri

## Solution 2 (similar to 1, simplified)
Note the divisibility rule of 11. The sum of every other digit minus the sum of the rest of the digits must be divisible by 11.
The maximum possible sum of digits in a 7-digit number is 63 ( $9999999$ ). Since the sum of the digits in the mystery number is 61, we have two possible scenarios. Either 5 digits are 9 and 2 digits are 8 (ex: $9899989$ , $9999988$ ), or 6 digits are 9 and 1 digit is 7 ( $9979999$ ). Going case by case, there are 7 numbers involving six digits as 9 and one as 7 and 21 numbers involving five digits as 9 and two digits as eight, giving a total 28 possible numbers.
Utilizing the divisibility rule, it can be seen that in order to satisfy the rule, the 7 or both 8s must be in the even positions (such that the number satisfies $9X9X9X9$ ). There are 3 numbers that satisfy $9X9X9X9$ where one of the $X$ is 7 and the other two are 9, and 3 numbers that satisfy $9X9X9X9$ where 2 of the $X$ are 8 and the other is 9, giving 6 satisfying numbers. Therefore, the answer is \[\frac{6}{28} = \boxed{\text{(A)\ } \frac{3}{14}}.\] .
~tkaim

## Video Solution 1 by OmegaLearn.org
https://youtu.be/B1PPVAkGbfI

## Video Solution 2 (Fast and Easy)
https://www.youtube.com/watch?v=hw_zeHbG1tQ
~ Pi Academy
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .