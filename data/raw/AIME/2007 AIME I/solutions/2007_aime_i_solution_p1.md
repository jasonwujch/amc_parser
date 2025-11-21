# 2007 AIME I Problem 1

## Problem

How many positive perfect squares less than $10^6$ are multiples of $24$ ?

## Solution
The prime factorization of $24$ is $2^3\cdot3$ . Thus, each square must have at least $3$ factors of $2$ and $1$ factor of $3$ and its square root must have $2$ factors of $2$ and $1$ factor of $3$ . This means that each square is in the form $(12c)^2$ , where $12 c$ is a positive integer less than $\sqrt{10^6}$ . There are $\left\lfloor \frac{1000}{12}\right\rfloor = \boxed{083}$ solutions.

## Solution 2
The perfect squares divisible by $24$ are all multiples of $12$ : $12^2$ , $24^2$ , $36^2$ , $48^2$ , etc... Since they all have to be less than $10^6$ , or $1000^2$ , the closest multiple of $12$ to $1000$ is $996$ ( $12*83$ ), so we know that this is the last term in the sequence. Therefore, we know that there are $\boxed{083}$ perfect squares divisible by $24$ that are less than $10^6$ .
These problems are copyrighted © by the Mathematical Association of America.