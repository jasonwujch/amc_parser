# 2017 AMC 10A Problem 16

## Problem

There are $10$ horses, named Horse $1$ , Horse $2$ , . . . , Horse $10$ . They get their names from how many minutes it takes them to run one lap around a circular race track: Horse $k$ runs one lap in exactly $k$ minutes. At time $0$ all the horses are together at the starting point on the track. The horses start running in the same direction, and they keep running around the circular track at their constant speeds. The least time $S > 0$ , in minutes, at which all $10$ horses will again simultaneously be at the starting point is $S=2520$ . Let $T > 0$ be the least time, in minutes, such that at least $5$ of the horses are again at the starting point. What is the sum of the digits of $T?$

$\textbf{(A) }2 \qquad \textbf{(B) }3 \qquad \textbf{(C) }4 \qquad \textbf{(D) }5 \qquad \textbf{(E) }6$

## Solution 1 (Classical Way)
If we have horses, $a_1, a_2, \ldots, a_n$ , then any number that is a multiple of all those numbers is a time when all horses will meet at the starting point. The least of these numbers is the LCM. To minimize the LCM, we need the smallest primes, and we need to repeat them a lot. By inspection, we find that $\text{LCM}(1,2,3,2\cdot2,2\cdot3) = 12$ . Finally, $1+2 = \boxed{\textbf{(B) }3}$ .

## Solution 2
We are trying to find the smallest number that has $5$ one-digit divisors. Therefore we try to find the LCM for smaller digits, such as $1$ , $2$ , $3$ , or $4$ . We quickly consider $12$ since it is the smallest number that is the LCM of $1$ , $2$ , $3$ and $4$ . Since $12$ has $5$ single-digit divisors, namely $1$ , $2$ , $3$ , $4$ , and $6$ , our answer is $1+2 = \boxed{\textbf{(B)}\ 3}$

## Solution 3 (Speedy Guess and Check)
First, for 5 horses to simultaneously pass the starting line after $T$ seconds, $T$ must be divisible by the amount of seconds it takes each of the 5 horses to pass the starting line, meaning all of the horses must be divisors of $T$ , and therefore meaning $T$ must have at least $5$ $1$ -digit divisors. Since we want to minimize $T$ , we will start by guessing the lowest natural number, $1$ . $1$ has only $1$ factor, so it does not work, we now repeat the process for the numbers between $2$ and $12$ (This should not take more than a minute) to get that $12$ is the first number to have $5$ or more single-digit divisors ( $1, 2, 3, 4, 6$ ). The sum of the digits of $12$ is $1+2 = \boxed{\textbf{(B)}\ 3}$ , which is our answer.
Note that this solution is rather fast with this problem because the numbers given in the question are low, this may not always be the case, however, when given higher numbers.

## Solution 4 (Inspection)
By inspection, $(1, 2, 3, 4, 6)$ yields the lowest answer of $12$ and the sum of the digits is $1+2 \Longrightarrow \boxed{\textbf{(B)}\ 3}$
~JH. L

## Video Solution
https://youtu.be/umr2Aj9ViOA

## Video Solution 2
https://youtu.be/igOErrux95I
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .