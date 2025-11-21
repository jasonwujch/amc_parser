# 2015 AIME II Problem 3

## Problem

Let $m$ be the least positive integer divisible by $17$ whose digits sum to $17$ . Find $m$ .

## Solution 1
The three-digit integers divisible by $17$ , and their digit sum: \[\begin{array}{c|c} m & s(m)\\ \hline 102 & 3 \\ 119 & 11\\ 136 & 10\\ 153 & 9\\ 170 & 8\\ 187 & 16\\ 204 & 6\\ 221 & 5\\ 238 & 13\\ 255 & 12\\ 272 & 11\\ 289 & 19\\ 306 & 9\\ 323 & 8\\ 340 & 7\\ 357 & 15\\ 374 & 14\\ 391 & 13\\ 408 & 12\\ 425 & 11\\ 442 & 10\\ 459 & 18\\ 476 & 17 \end{array}\]
Thus the answer is $\boxed{476}$ .

## Solution 2 (Shortcut)
We can do the same thing as solution 1, except note the following fact: $102$ is a multiple of $17$ and its digits sum to $3$ .
Therefore, we can add it onto an existing multiple of $17$ that we know of to have $s(m) = 14$ , shown in the right-hand column, provided that its units digit is less than $8$ and its hundreds digit is less than $9$ . Unfortunately, $68$ does not fit the criteria, but $374$ does, meaning that, instead of continually adding multiples of $17$ , we can stop here and simply add $102$ to reach our final answer of $\boxed{476}$ .
~Tiblis
(Comment from another person: Actually, this doesn't work because you can't be sure there are no numbers between 374 and 476 that work. This solution just lucks out.)

## Solution 3
The digit sum of a base $10$ integer $m$ is just $m\pmod{9}$ . In this problem, we know $17\mid m$ , or $m=17k$ for a positive integer $k$ .
Also, we know that $m\equiv 17\equiv -1\pmod{9}$ , or $17k\equiv -k\equiv -1\pmod{9}$ .
Obviously $k=1$ is a solution. This means in general, $k=9x+1$ is a solution for non-negative integer $x$ .
Checking the first few possible solutions, we find that $m=\boxed{476}$ is the first solution that has $s(m)=17$ , and we're done.

## Solution 4
Since the sum of the digits in the base-10 representation of $m$ is $17$ , we must have $m\equiv 17 \pmod{9}$ or $m\equiv -1\pmod{9}$ . We also know that since $m$ is divisible by 17, $m\equiv 0 \pmod{17}$ .
To solve this system of linear congruences, we can use the Chinese Remainder Theorem. If we set $m\equiv (-1)(17)(8)\pmod {153}$ , we find that $m\equiv 0\pmod{17}$ and $m\equiv -1\pmod{9}$ , because $17\cdot 8\equiv 136 \equiv 1\pmod{9}$ . The trick to getting here was to find the number $x$ such that $17x\equiv 1\pmod{9}$ , so that when we take things $\pmod{9}$ , the $17$ goes away. We can do this using the Extended Euclidean Algorithm or by guess and check to find that $x\equiv 8\pmod{9}$ .
Finally, since $m\equiv 17\pmod{153}$ , we repeatedly add multiples of $153$ until we get a number in which its digits sum to 17, which first happens when $m=\boxed{476}$ .

## Solution 5
We proceed by casework on the number of digits. Clearly the answer must have at least two digits, seeing as the maximum digit sum for a one-digit number is 9. The answer must also have less than 4 digits, because this is the AIME.
Case 1: The answer is a 2-digit number. Represent the number as $10a + b$ , where $0 < a \leq 9$ and $0 \leq b \leq 9$ . The conditions of the problem translated into algebra are: \[17|10a+b\] \[a+b=17\] By the Euclidean Algorithm, this is equivalent to: \[17|9a\] 9 is not a factor of 17, so $17|a$ . So $a$ must be a multiple of 17, but this is impossible because of the conditions we placed on $a$ and $b$ . (Alternatively, note that the only possible options are 89 and 98, and neither works.)
Case 2: The answer is a 3-digit number. Represent the number as $100a+10b+c$ , where $0 < a \leq 9$ and $0 \leq b,c \leq 9$ . Translating the conditions again: \[17|100a+10b+c\] \[a+b+c=17\] \[17|99a+9b\] \[17|9(11a+b)\] \[17|11a+b\] Testing multiples of 17 yields $(4, 7, 6)$ as the minimal solution for $(a, b, c)$ and thus the answer is $\boxed{476}$ .
- gting
Note: We have $11a+b \equiv \mod(17)$ . Doing some experimentation for the smallest value of $a$ , since we want to minimize $abc_{10}$ , we get $11a+b=51 \implies a=4, b=7, c=6$ . Trying $17$ and $34$ don't work, because $0 \leq c \leq 9$ . Also, one can use long division to verify that $17$ is a divisor of $476$ , specifically $17 \cdot 28=476$ . So the answer is $476$ . ~First

## Video Solution
https://www.youtube.com/watch?v=9re2qLzOKWk&t=133s
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .