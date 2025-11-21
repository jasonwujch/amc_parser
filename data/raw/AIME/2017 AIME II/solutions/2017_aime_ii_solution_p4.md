# 2017 AIME II Problem 4

## Problem

Find the number of positive integers less than or equal to $2017$ whose base-three representation contains no digit equal to $0$ .

## Solution

## Solution 1
The base- $3$ representation of $2017_{10}$ is $2202201_3$ . Because any $7$ -digit base- $3$ number that starts with $22$ and has no digit equal to $0$ must be greater than $2017_{10}$ , all $7$ -digit numbers that have no digit equal to $0$ must start with $21$ or $1$ in base $3$ . Of the base- $3$ numbers that have no digit equal to $0$ , there are $2^5$ $7$ -digit numbers that start with $21$ , $2^6$ $7$ -digit numbers that start with $1$ , $2^6$ $6$ -digit numbers, $2^5$ $5$ -digit numbers, $2^4$ $4$ -digit numbers, $2^3$ $3$ -digit numbers, $2^2$ $2$ -digit numbers, and $2^1$ $1$ -digit numbers. Summing these up, we find that the answer is $2^5+2^6+2^6+2^5+2^4+2^3+2^2+2^1=\boxed{222}$ .

## Solution 2
Note that $2017=2202201_{3}$ , and $2187=3^7=10000000_{3}$ . There can be a $1,2,...,7$ digit number less than $2187$ , and each digit can either be $1$ or $2$ . So $2^1$ one digit numbers and so on up to $2^7$ $7$ digit.
Now we have to subtract out numbers from $2018$ to $2187$
Then either the number must begin $221...$ or $222...$ with four more digits at the end
Using $1$ s and $2$ s there are $2^4$ options for each so:
$2+4+8+16+32+64+128-2*16=256-2-32=\boxed{222}$

## Solution 3 (Casework)
Since the greatest power of $3$ that can be used is $3^6$ , we can do these cases.
Coefficient of $3^6=0$ : Then if the number has only $3^0$ , it has 2 choices (1 or 2). Likewise if the number has both a $3^1$ and $3^0$ term, there are 4 choices, and so on until $3^5$ , so the sum is $2+4+...+64=127-1=126$ .
Coefficient of $3^6=1$ : Any combination of $1$ or $2$ for the remaining coefficients works, so $2^6=64$ . Why is this less than $126$ ? Because the first time around, leading zeroes didn't count. But this time, all coefficients $3^n$ of $n<6$ need 1 and 2.
Coefficient of $3^6=2$ : Look at $3^5$ coefficient. If 1, all of them work because $3^7=2187-3^5=243<<2017$ . That's 32 cases. Now of this coefficient is 2, then at the coefficient of $3^4=81$ is at least 1. However, $3^6*2+3^5*2+3^4>>2017$ , so our answer is $126+64+32=\boxed{222}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .