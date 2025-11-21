# 2001 AIME I Problem 1

## Problem

Find the sum of all positive two-digit integers that are divisible by each of their digits.

## Solution 1
Let our number be $10a + b$ , $a,b \neq 0$ . Then we have two conditions: $10a + b \equiv 10a \equiv 0 \pmod{b}$ and $10a + b \equiv b \pmod{a}$ , or $a$ divides into $b$ and $b$ divides into $10a$ . Thus $b = a, 2a,$ or $5a$ (note that if $b = 10a$ , then $b$ would not be a digit).
- For $b = a$ , we have $n = 11a$ for nine possibilities, giving us a sum of $11 \cdot \frac {9(10)}{2} = 495$ .
- For $b = 2a$ , we have $n = 12a$ for four possibilities (the higher ones give $b > 9$ ), giving us a sum of $12 \cdot \frac {4(5)}{2} = 120$ .
- For $b = 5a$ , we have $n = 15a$ for one possibility (again, higher ones give $b > 9$ ), giving us a sum of $15$ .
If we ignore the case $b = 0$ as we have been doing so far, then the sum is $495 + 120 + 15 = \boxed{630}$ .

## Solution 2
By testing every 2-digit number, we can list out all of the possibilities: \[11+12+15+22+24+33+36+44+48+55+66+77+88+99=\boxed{630}.\]

## Solution 3
To further expand on solution 2, it would be tedious to test all $90$ two-digit numbers. We can reduce the amount to look at by focusing on the tens digit. First, we cannot have any number that is a multiple of $10$ . We also note that any number with the same digits is a number that satisfies this problem. This gives \[11, 22, 33, ... 99.\] We start from each of these numbers and constantly add the digit of the tens number of the respective number until we get a different tens digit. For example, we look at numbers $11, 12, 13, ... 19$ and numbers $22, 24, 26, 28$ . This heavily reduces the numbers we need to check, as we can deduce that any number with a tens digit of $5$ or greater that does not have two of the same digits is not a valid number for this problem. This will give us the numbers from solution 2.

## Solution 4
In this solution, we will do casework on the ones digit. Before we start, let's make some variables. Let $a$ be the ones digit, and $b$ be the tens digit. Let $n$ equal our number. Our number can be expressed as $10b+a$ . We can easily see that $b|a$ , since $b|n$ , and $b|10b$ . Therefore, $b|(n-10b)$ . Now, let's start with the casework.
Case 1: $a=1$ Since $b|a$ , $b=1$ . From this, we get that $n=11$ satisfies the condition.
Case 2: $a=2$ We either have $b=1$ , or $b=2$ . From this, we get that $n=12$ and $n=22$ satisfy the condition.
Case 3: $a=3$ We have $b=3$ . From this, we get that $n=33$ satisfies the condition. Note that $b=1$ was not included because $3$ does not divide $13$ .
Case 4: $a=4$ We either have $b=2$ or $b=4$ . From this, we get that $n=24$ and $n=44$ satisfy the condition. $b=1$ was not included for similar reasons as last time.
Case 5: $a=5$ We either have $b=1$ or $b=5$ . From this, we get that $n=15$ and $n=55$ satisfy the condition.
Continuing with this process up to $a=9$ , we get that $n$ could be $11, 12, 22, 33, 24, 44, 15, 55, 36, 66, 77, 48, 88, 99$ . Summing, we get that the answer is $\boxed{630}$ . A clever way to sum would be to group the multiples of $11$ together to get $11+22+\dots+99=(45)(11)=495$ , and then add the remaining $12+24+15+36+48=135$ .
-bronzetruck2016
These problems are copyrighted © by the Mathematical Association of America.