# 2004 AIME I Problem 1

## Problem

The digits of a positive integer $n$ are four consecutive integers in decreasing order when read from left to right. What is the sum of the possible remainders when $n$ is divided by $37$ ?

## Solution 1
A brute-force solution to this question is fairly quick, but we'll try something slightly more clever: our numbers have the form ${\underline{(n+3)}}\,{\underline{(n+2)}}\,{\underline{( n+1)}}\,{\underline {(n)}}$ $= 1000(n + 3) + 100(n + 2) + 10(n + 1) + n = 3210 + 1111n$ , for $n \in \lbrace0, 1, 2, 3, 4, 5, 6\rbrace$ .
Now, note that $3\cdot 37 = 111$ so $30 \cdot 37 = 1110$ , and $90 \cdot 37 = 3330$ so $87 \cdot 37 = 3219$ . So the remainders are all congruent to $n - 9 \pmod{37}$ . However, these numbers are negative for our choices of $n$ , so in fact the remainders must equal $n + 28$ .
Adding these numbers up, we get $(0 + 1 + 2 + 3 + 4 + 5 + 6) + 7\cdot28 = \boxed{217}$

## Solution 2
There are only $7$ possible values of $n$ : $3210, 4321, 5432, \cdots, 9876$ .
$3210$ gives a remainder of $28$ when divided by $37$ . To calculate the remainders of the other integers, notice that each number is $1111$ more than the previous number. Since $1111$ gives a remainder of $1$ when divided by $37$ , the remainders of the other integers will be $29, 30, 31, \cdots, 34$ .
Therefore, our answer is $28 + 29 + 30 + 31 + 32 + 33 + 34 = \frac{28 + 34}{2} \cdot 7 = \boxed{217}$ . ~Viliciri
These problems are copyrighted © by the Mathematical Association of America.