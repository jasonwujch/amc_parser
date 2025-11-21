# 2021 AIME II Problem 1

## Problem

Find the arithmetic mean of all the three-digit palindromes. (Recall that a palindrome is a number that reads the same forward and backward, such as $777$ or $383$ .)

## Solution 1
Recall that the arithmetic mean of all the $n$ digit palindromes is just the average of the largest and smallest $n$ digit palindromes, and in this case the $2$ palindromes are $101$ and $999$ and $\frac{101+999}{2}=\boxed{550},$ which is the final answer.
~ math31415926535

## Solution 2
For any palindrome $\underline{ABA},$ note that $\underline{ABA}$ is $100A + 10B + A = 101A + 10B.$ The average for $A$ is $5$ since $A$ can be any of $1, 2, 3, 4, 5, 6, 7, 8,$ or $9.$ The average for $B$ is $4.5$ since $B$ is either $0, 1, 2, 3, 4, 5, 6, 7, 8,$ or $9.$ Therefore, the answer is $505 + 45 = \boxed{550}.$
- ARCTICTURN

## Solution 3 (Symmetry and Generalization)
For every three-digit palindrome $\underline{ABA}$ with $A\in\{1,2,3,4,5,6,7,8,9\}$ and $B\in\{0,1,2,3,4,5,6,7,8,9\},$ note that $\underline{(10-A)(9-B)(10-A)}$ must be another palindrome by symmetry. Therefore, we can pair each three-digit palindrome uniquely with another three-digit palindrome so that they sum to \begin{align*} \underline{ABA}+\underline{(10-A)(9-B)(10-A)}&=\left[100A+10B+A\right]+\left[100(10-A)+10(9-B)+(10-A)\right] \\ &=\left[100A+10B+A\right]+\left[1000-100A+90-10B+10-A\right] \\ &=1000+90+10 \\ &=1100. \end{align*} For instances: \begin{align*} 171+929&=1100, \\ 262+838&=1100, \\ 303+797&=1100, \\ 414+686&=1100, \\ 545+555&=1100, \end{align*} and so on.
From this symmetry, the arithmetic mean of all the three-digit palindromes is $\frac{1100}{2}=\boxed{550}.$
Remark
By the Multiplication Principle, there are $9\cdot10=90$ three-digit palindromes in total. Their sum is $1100\cdot45=49500,$ as we can match them into $45$ pairs such that each pair sums to $1100.$
~MRENTHUSIASM

## Solution 4 (Similar to Solution 2: Very, Very Easy and Quick)
We notice that a three-digit palindrome looks like this: $\underline{aba}.$
And we know $a$ can be any digit from $1$ through $9,$ and $b$ can be any digit from $0$ through $9,$ so there are $9\times{10}=90$ three-digit palindromes.
We want to find the sum of these $90$ palindromes and divide it by $90$ to find the arithmetic mean.
How can we do that? Instead of adding the numbers up, we can break each palindrome into two parts: $101a+10b.$
Thus, all of these $90$ palindromes can be broken into this form.
Thus, the sum of these $90$ palindromes will be $101\times{(1+2+...+9)}\times{10}+10\times{(0+1+2+...+9)}\times{9},$ because each $a$ will be in $10$ different palindromes (since for each $a,$ there are $10$ choices for $b$ ). The same logic explains why we multiply by $9$ when computing the total sum of $b.$
We get a sum of $45\times{1100},$ but don't compute this! Divide this by $90$ and you will get $\boxed{550}.$
~ $\alpha b \alpha$

## Solution 5 (Extremely Fast Solution)
The possible values of the first and last digits each are $1, 2, ..., 8, 9$ with a sum of $45$ so the average value is $5.$ The middle digit can be any digit from $0$ to $9$ with a sum of $45,$ so the average value is $4.5.$ The average of all three-digit palindromes is $5\cdot 10^2+4.5\cdot 10+5=\boxed{550}.$
~MathIsFun286
~MathFun1000 (Rephrasing with more clarity)

## Solution 6 (Two cases)
Case 1
Consider palindromes of the form $5x5 = 505 + 10x.$ There are $10$ of them. The arithmetic mean of the first term is $505,$ and the second $\frac {10 \cdot(0 + 1 + ... + 9)}{10} = 45.$ The arithmetic mean of the sum is $505 + 45 = 550.$
Case 2
Consider palindromes of the form $yxy,$ where $y= {1,2,3,4,6,7,8,9}.$ Let $u = 10 – y, v = 9 – x.$ Then $uvu$ is a symmetric palindrome that can be constructed for each $yxy.$ The arithmetic mean of each such pair is $550.$ For example, $\frac{737 + 363}{2} = 550.$
Thus, all palindromes are divided into groups of numbers with the arithmetic mean in each group equal to $550.$
The arithmetic mean of all numbers is also $550.$
vladimir.shelomovskii@gmail.com, vvsss
### Remark
Visit the Discussion Page for questions and further generalizations.
~MRENTHUSIASM

## Video Solution
https://www.youtube.com/watch?v=jDP2PErthkg

## Video Solution by Interstigation
https://youtu.be/3_ik5N33CnQ
speedy 2 min video
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .