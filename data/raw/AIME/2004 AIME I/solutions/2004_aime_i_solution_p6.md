# 2004 AIME I Problem 6

## Problem

An integer is called snakelike if its decimal representation $a_1a_2a_3\cdots a_k$ satisfies $a_i<a_{i+1}$ if $i$ is odd and $a_i>a_{i+1}$ if $i$ is even . How many snakelike integers between 1000 and 9999 have four distinct digits?

## Solution 1
We divide the problem into two cases: one in which zero is one of the digits and one in which it is not. In the former case, suppose we pick digits $x_1,x_2,x_3,x_4$ such that $x_1<x_2<x_3<x_4$ . There are five arrangements of these digits that satisfy the condition of being snakelike: $x_1x_3x_2x_4$ , $x_1x_4x_2x_3$ , $x_2x_3x_1x_4$ , $x_2x_4x_1x_3$ , $x_3x_4x_1x_2$ . Thus there are $5\cdot {9\choose 4}=630$ snakelike numbers which do not contain the digit zero.
In the second case we choose zero and three other digits such that $0<x_2<x_3<x_4$ . There are three arrangements of these digits that satisfy the condition of being snakelike: $x_2x_30x_4$ , $x_2x_40x_3$ , $x_3x_40x_2$ . Because we know that zero is a digit, there are $3\cdot{9\choose 3}=252$ snakelike numbers which contain the digit zero. Thus there are $630+252=\boxed{882}$ snakelike numbers.

## Solution 2
Let's create the snakelike number from digits $a < b < c < d$ , and, if we already picked the digits there are 5 ways to do so, as said in the first solution. And, let's just pick the digits from 0-9. This get's a total count of $5\cdot{10 \choose 4}$ But, this over-counts since it counts numbers like 0213. We can correct for this over-counting. Lock the first digit as 0 and permute 3 other chosen digits $a < b < c$ . There are 2 ways to permute to make the number snakelike, b-a-c, or c-a-b. And, we pick a,b,c from 1 to 9, since 0 has already been chosen as one of the digits. So, the amount we have overcounted by is $2\cdot{9 \choose 3}$ . Thus our answer is $5\cdot{10 \choose 4} - 2\cdot{9 \choose 3} = \boxed{882}$

## Solution 3
We will first decide the order of the 4 digits, greatest to least. To do this, we will pretend that we have selected the digits 1,2,3,4, and we need to arrange them to create a snakelike number. By testing all permutations, there are only 5 ways to make a snakelike number: (1,3,2,4),(1,4,2,3),(2,3,1,4),(2,4,1,3),(3,4,1,2).
Now we select 4 digits to replace the 1,2,3,4.
In first 2 of cases: (1,3,2,4),(1,4,2,3), the leading digit is a 1, which means it is the smallest of our 4 digits. If we select a 0, the leading digit will be a zero, which is bad because all numbers between 1000 and 9999 have nonzero leading digits. So, we need to select our 4 digits only from the pool of 1-9. There are 9 choose 4 ways and there are 2 cases:
$2 \cdot \dbinom{9}{4} = 252$
Thus, there are 252 ways for those 2 cases.
For the next 3 cases, selecting a 0 is okay, so we can select from the pool of 0-9. There are 10 choose 4 ways to select our 4 digits and there are 3 cases:
$3 \cdot \dbinom{10}{4} = 630$
For those 3 cases there are 630 ways.
Thus, our answer is 630+252 = $\boxed{882}$ .
-Alexlikemath
These problems are copyrighted © by the Mathematical Association of America.