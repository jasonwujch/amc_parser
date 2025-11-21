# 2025 AIME I Problem 1

## Problem

Find the sum of all integer bases $b>9$ for which $17_b$ is a divisor of $97_b.$

## Video solution by grogg007
https://www.youtube.com/watch?v=PNBxBvvjbcU

## Solution 1 (thorough)
We are tasked with finding the number of integer bases $b>9$ such that $\cfrac{9b+7}{b+7}\in\mathbb{Z}$ . Notice that \[\cfrac{9b+7}{b+7}=\cfrac{9b+63-56}{b+7}=\cfrac{9(b+7)-56}{b+7}=9-\cfrac{56}{b+7}\] so we need only $\cfrac{56}{b+7}\in\mathbb{Z}$ . Then $b+7$ is a factor of $56$ .
The factors of $56$ are $1,2,4,7,8,14,28,56$ . Of these, only $8,14,28,56$ produce a positive $b$ , namely $b=1,7,21,49$ respectively. However, we are given that $b>9$ , so only $b=21,49$ are solutions. Thus the answer is $21+49=\boxed{070}$ . ~eevee9406 ~NOOK(Minor LaTeX Edits)

## Solution 2 (quick)
We have, $b + 7 \mid 9b + 7$ meaning $b + 7 \mid -56$ so taking divisors of $56$ under bounds to find $b = 49, 21$ meaning our answer is $49+21=\boxed{070}.$
~ mathkiddus

## Solution 3
This means that $a(b+7)=9b+7$ where $a$ is a natural number. Rearranging we get $(a-9)(b+7)=-56$ . Since $b>9$ , $b=49,21$ . Thus the answer is $49+21=\boxed{070}$
~ zhenghua

## Solution 4
Let $\dfrac{9b+7}{b+7} = n$ . Now, we have: $\dfrac{9(b+7)-56}{b+7} = n \Longrightarrow 9-\dfrac{56}{b+7}$ . Now, we can just find the factors of $56$ , subtract $7$ , and sum them. Listing them out, we have the only ones that are positive are $8-1 = 7, 14-7 = 7, 28-7 = 21, 56-7 = 49$ . But, we have this condition: $b > 9$ , so the only ones that work are $21,49 \Longrightarrow 21 + 49 = \boxed{070}$
-jb2015007

## Solution 5 (Solution 4 but different approach)
We want \( 17_b \) to divide \( 97_b \). Converting to base 10 gives \( 17_b = b + 7 \) and \( 97_b = 9b + 7 \). The condition is \( b + 7 \mid 9b + 7 \). Subtracting \( 9(b + 7) \) from \( 9b + 7 \) gives \( (9b + 7) - 9(b + 7) = -56 \). So \( b + 7 \) must divide 56. Continue as in Solution 4 to get $\boxed{070}$
~Pinotation

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=J-0BapU4Yuk

## Video Solution by Steakmath (simplest)
https://youtu.be/Qi8EjzfoLUU

## Video Solution(Fast!, Easy, Beginner-Friendly)
https://www.youtube.com/watch?v=S8aakoJToM0
~MC

## Video Solution by Mathletes Corner
https://www.youtube.com/watch?v=fEYpnDxSlk0
~GP102

## Quick & Easy Video Solution
https://www.youtube.com/watch?v=A-h121roYg8
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .