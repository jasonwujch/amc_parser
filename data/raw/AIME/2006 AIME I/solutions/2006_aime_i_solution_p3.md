# 2006 AIME I Problem 3

## Problem

Find the least positive integer such that when its leftmost digit is deleted, the resulting integer is $\frac{1}{29}$ of the original integer.

## Solutions

## Solution 1
Suppose the original number is $N = \overline{a_na_{n-1}\ldots a_1a_0},$ where the $a_i$ are digits and the first digit, $a_n,$ is nonzero. Then the number we create is $N_0 = \overline{a_{n-1}\ldots a_1a_0},$ so \[N = 29N_0.\] But $N$ is $N_0$ with the digit $a_n$ added to the left, so $N = N_0 + a_n \cdot 10^n.$ Thus, \[N_0 + a_n\cdot 10^n = 29N_0\] \[a_n \cdot 10^n = 28N_0.\] The right-hand side of this equation is divisible by seven, so the left-hand side must also be divisible by seven. The number $10^n$ is never divisible by $7,$ so $a_n$ must be divisible by $7.$ But $a_n$ is a nonzero digit, so the only possibility is $a_n = 7.$ This gives \[7 \cdot 10^n = 28N_0\] or \[10^n = 4N_0.\] Now, we want to minimize both $n$ and $N_0,$ so we take $N_0 = 25$ and $n = 2.$ Then \[N = 7 \cdot 10^2 + 25 = \boxed{725},\] and indeed, $725 = 29 \cdot 25.$ $\square$

## Solution 2
Let $N$ be the required number, and $N'$ be $N$ with the first digit deleted. Now, we know that $N<1000$ (because this is an AIME problem). Thus, $N$ has $1,$ $2$ or $3$ digits. Checking the other cases, we see that it must have $3$ digits. Let $N=\overline{abc}$ , so $N=100a+10b+c$ . Thus, $N'=\overline{bc}=10b+c$ . By the constraints of the problem, we see that $N=29N'$ , so \[100a+10b+c=29(10b+c).\] Now, we subtract and divide to get \[100a=28(10b+c)\] \[25a=70b+7c.\] Clearly, $c$ must be a multiple of $5$ because both $25a$ and $70b$ are multiples of $5$ . Thus, $c=5$ . Now, we plug that into the equation: \[25a=70b+7(5)\] \[25a=70b+35\] \[5a=14b+7.\] By the same line of reasoning as earlier, $a=7$ . We again plug that into the equation to get \[35=14b+7\] \[b=2.\] Now, since $a=7$ , $b=2$ , and $c=5$ , our number $N=100a+10b+c=\boxed{725}$ .
Here's another way to finish using this solution. From the above, you have \[100a = 28(10b + c).\] Divide by $4$ , and you get \[25a = 7(10b + c).\] This means that $25a$ has to be divisible by $7$ , and hence $a = 7.$ Now, solve for $25 = 10b + c$ , which gives you $a = 7, b = 2, c = 5$ , giving you the number $\boxed{725}$

## Solution 3 (Quick)
Note that if we let the last digit be $c$ we must have $9c \equiv c \pmod{10}.$ Thus we either have $c=0$ which we can quickly check to be impossible (since the number after digit removal could be 10,20,30) or $c=5.$ Testing 5, 15, and 25 as the numbers after removal we find that our answer is clearly $29 \cdot 25 = 725.$
~Dhillonr25
(Note that the quick checking of six numbers was possible thanks to AIME problems having answers less than 1000).

## Solution 4
First we try $2$ digit numbers like $\overline{ab}$ . Removing the leftmost digit gives us $b$ . Now, using the information we are given we can write the equation: \[\dfrac{b}{10a+b} = \dfrac{1}{29} \Longrightarrow 10a+b=29b \Longrightarrow 5a = 14b\] . Since $5$ and $14$ are relatively prime, the smallest case that works is $a = 14$ , and $b = 5$ , but $a$ is an digit so the number must be at least $3$ digits. We let the number be $\overline{abc}$ . So, using the info we know, we can conclude that \[\dfrac{10b+c}{100a+10b+c} = \dfrac{1}{29} \Longrightarrow 25a-70b-7c = 0\] . Rerraranging gives us \[25a = 7(10b+c)\] . So, sicne $25$ and $7$ are relatively prime, the lowest possible case is that $a = 7$ , and $10b+c = 25$ .So, we have $b = 2, c = 5$ . So the desired number is $\boxed{725}$
-jb2015007
- Number Theory
These problems are copyrighted © by the Mathematical Association of America.