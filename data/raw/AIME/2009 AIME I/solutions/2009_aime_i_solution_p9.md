# 2009 AIME I Problem 9

## Problem

A game show offers a contestant three prizes A, B and C, each of which is worth a whole number of dollars from $\$ 1$ to $\$ 9999$ inclusive. The contestant wins the prizes by correctly guessing the price of each prize in the order A, B, C. As a hint, the digits of the three prices are given. On a particular day, the digits given were $1, 1, 1, 1, 3, 3, 3$ . Find the total number of possible guesses for all three prizes consistent with the hint.

## Solution 1
[Clarification: You are supposed to find the number of all possible tuples of prices, $(A, B, C)$ , that could have been on that day.]
Since we have three numbers, consider the number of ways we can put these three numbers together in a string of 7 digits. For example, if $A=113, B=13, C=31$ , then the string is
\[1131331.\]
Since the strings have seven digits and three threes, there are $\binom{7}{3}=35$ arrangements of all such strings.
In order to obtain all combination of A,B,C, we partition all the possible strings into 3 groups.
Let's look at the example. We have to partition it into 3 groups with each group having at least 1 digit. In other words, we need to find the solution to
\[x+y+z=7, x,y,z>0.\]
This gives us
\[\binom{6}{2}=15\]
ways by stars and bars. But we have counted the one with 5 digit numbers; that is, $(5,1,1),(1,1,5),(1,5,1)$ .
Thus, each arrangement has \[\binom{6}{2}-3=12\] ways per arrangement, and there are $12\times35=\boxed{420}$ ways.

## Solution 1a (Casework)
Follow Solution 1 until the partitioning of all the possible strings into 3 groups. Another way to partition the strings is by casework.
Case 1: one of [A, B, or C] has one digit, another has two digits, and the last has four digits. There are $3!=6$ ways this can happen.
Case 2: one of [A, B, or C] has two digit, another has two digits, and the last has three digits. There are $3!/2=3$ ways this can happen.
Case 3: one of [A, B, or C] has one digit, another has three digits, and the last has three digits. There are $3!/2=3$ ways this can happen.
The total numbers of ways per arrangement is $6+3+3=12$ ways. Following Solution 1, there are $12\times35=\boxed{420}$ total ways.
-unhappyfarmer

## Video Solution
https://youtu.be/VhyLeQufKr8 (unavailable)
These problems are copyrighted © by the Mathematical Association of America.