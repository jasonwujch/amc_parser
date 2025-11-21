# 2001 AIME II Problem 1

## Problem

Let $N$ be the largest positive integer with the following property: reading from left to right, each pair of consecutive digits of $N$ forms a perfect square. What are the leftmost three digits of $N$ ?

## Solution
The two-digit perfect squares are $16, 25, 36, 49, 64, 81$ . We try making a sequence starting with each one:
- $16 - 64 - 49$ . This terminates since none of them end in a $9$ , giving us $1649$ .
- $25$ .
- $36 - 64 - 49$ , $3649$ .
- $49$ .
- $64 - 49$ , $649$ .
- $81 - 16 - 64 - 49$ , $81649$ .
The largest is $81649$ , so our answer is $\boxed{816}$ .
These problems are copyrighted © by the Mathematical Association of America.