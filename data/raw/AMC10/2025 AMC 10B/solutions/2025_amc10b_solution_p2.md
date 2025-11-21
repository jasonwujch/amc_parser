# 2025 AMC 10B Problem 2

## Problem

Jerry wrote down the ones digit of each of the first $2025$ positive squares: $1, 4, 9, 6, 5, 6, \dots$ . What is the sum of all the numbers Jerry wrote down?

$\textbf{(A)}~9025 \qquad \textbf{(B)}~9070 \qquad \textbf{(C)}~9090 \qquad \textbf{(D)}~9115 \qquad \textbf{(E)}~9160$

## Solution 1
By a modulo $10$ argument, the ones digits repeat with period $10$ in the following order: \[1,4,9,6,5,6,9,4,1,0\] The sum of the numbers can be verified to be $45$ .
There are $202$ periods that occur from $1$ to $2025$ , and there are five extra numbers, those being $1,4,9,6,5$ , corresponding to $2021,2022,2023,2024,2025$ . The sum of these numbers is $25$ .
Hence, the total is \[202\cdot 45+25=9090+25=\boxed{\textbf{(D)}~9115}\]
~ eevee9406
~ Phinetium

## Solution 2 (Slightly more rigorous than Solution 1, but same idea)
Let $x\equiv n\quad\textrm{(mod 10)}$ . We have $x^2\equiv n^2\quad\textrm{(mod 10)}$ . So, the numbers must repeat in patterns of $10$ . Listing them out gives: \[1,4,9,6,5,6,9,4,1,0.\] These numbers sum to $45$ , so the sum of the first $2020$ numbers is $45\cdot202=9090$ . Since we need $5$ more numbers, we add $1+4+9+6+5=25$ to our answer to get $\boxed{\textbf{(D)}~9115}$ .
~Franklin2013

## Solution 3 (Similar to the other solutions but without the use of mods)
The ones digit of a square number is determined by the ones digit of the base. We can find the pattern by looking at the ones digits of the first ten positive squares:
\begin{aligned} 1^2 &= 1 \\ 2^2 &= 4 \\ 3^2 &= 9 \\ 4^2 &= 16 \quad (\text{ones digit } 6) \\ 5^2 &= 25 \quad (\text{ones digit } 5) \\ 6^2 &= 36 \quad (\text{ones digit } 6) \\ 7^2 &= 49 \quad (\text{ones digit } 9) \\ 8^2 &= 64 \quad (\text{ones digit } 4) \\ 9^2 &= 81 \quad (\text{ones digit } 1) \\ 10^2 &= 100 \quad (\text{ones digit } 0) \end{aligned}
The sequence of ones digits is:
$1$ , $4$ , $9$ , $6$ , $5$ , $6$ , $9$ , $4$ , $1$ , $0$
This pattern of ten digits repeats for every subsequent group of ten squares (e.g., \(11^2\) has the same ones digit as \(1^2\), \(12^2\) as \(2^2\), etc.).
$1$ + $4$ + $9$ + $6$ + $5$ + $6$ + $9$ + $4$ + $1$ + $0$ = $45$
We now divide by $10$ as the pattern repeats every $10$ terms: $2025$ / $10$ results in $202$ full cycles with a remainder of $5$ . The sum of the $202$ full cycles is:
$202$ * $45$ = $9090$
However, we must add back $5$ digits, as we had a remainder of $5$ when we divided $2025$ by $10$ . Therefore, the sum of the remaining $5$ digits is:
$1$ + $4$ + $9$ + $6$ + $5$ = $25$
Thus, the total sum is:
$9090$ + $25$ = $9115$
(NOTE: This is my first solution and it might need some LaTeX editing)
~BryBro7

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=jxSb3BIzKJg
~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution by Daily Dose of Math
https://youtu.be/s-Wimgu9wto
~Thesmartgreekmathdude
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .