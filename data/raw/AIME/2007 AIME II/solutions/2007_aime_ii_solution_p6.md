# 2007 AIME II Problem 6

## Problem

An integer is called parity-monotonic if its decimal representation $a_{1}a_{2}a_{3}\cdots a_{k}$ satisfies $a_{i}<a_{i+1}$ if $a_{i}$ is odd , and $a_{i}>a_{i+1}$ if $a_{i}$ is even . How many four-digit parity-monotonic integers are there?

## Solution 1
Let's set up a table of values. Notice that 0 and 9 both cannot appear as any of $a_1,\ a_2,\ a_3$ because of the given conditions. (Also note that 0 cannot appear as 0 cannot be the first digit of an integer.) A clear pattern emerges.
For example, for $3$ in the second column, we note that $3$ is less than $4,6,8$ , but greater than $1$ , so there are four possible places to align $3$ as the second digit.
For any number from 1-8, there are exactly 4 numbers from 1-8 that are odd and less than the number or that are even and greater than the number (the same will happen for 0 and 9 in the last column). Thus, the answer is $4^{k-1} \cdot 10 = 4^3\cdot10 = 640$ . -yeetdayeet

## Solution 2: Recursion
This problem can be solved via recursion since we are "building a string" of numbers with some condition. We want to create a new string by adding a new digit at the front so we avoid complications( $0$ can't be at the front and no digit is greater than $9$ ). There are $4$ options to add no matter what(try some examples if you want) so the recursion is $S_n=4S_{n-1}$ where $S_n$ stands for the number of such numbers with $n$ digits. Since $S_1=10$ the answer is $\boxed{640}$ .
These problems are copyrighted © by the Mathematical Association of America.