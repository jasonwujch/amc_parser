# 2003 AMC 10A Problem 25

## Problem

Let $n$ be a $5$ -digit number, and let $q$ and $r$ be the quotient and the remainder, respectively, when $n$ is divided by $100$ . For how many values of $n$ is $q+r$ divisible by $11$ ?

$\mathrm{(A) \ } 8180\qquad \mathrm{(B) \ } 8181\qquad \mathrm{(C) \ } 8182\qquad \mathrm{(D) \ } 9000\qquad \mathrm{(E) \ } 9090$

## Solutions

## Solution 1
$11|(q+r)$ implies that $11|(99q+q+r)$ and therefore $11|(100q+r)$ , so $11|n$ . Then, $n$ can range from $10010$ to $99990$ for a total of $\boxed{8181\Rightarrow \mathrm{(B)}}$ numbers.

## Solution 2
When a $5$ -digit number is divided by $100$ , the first $3$ digits become the quotient, $q$ , and the last $2$ digits become the remainder, $r$ .
Therefore, $q$ can be any integer from $100$ to $999$ inclusive, and $r$ can be any integer from $0$ to $99$ inclusive.
For each of the $9\cdot10\cdot10=900$ possible values of $q$ , there are at least $\left\lfloor \frac{100}{11} \right\rfloor = 9$ possible values of $r$ such that $q+r \equiv 0\pmod{11}$ .
Since there is $1$ "extra" possible value of $r$ that is congruent to $0\pmod{11}$ , each of the $\left\lfloor \frac{900}{11} \right\rfloor = 81$ values of $q$ that are congruent to $0\pmod{11}$ have $1$ more possible value of $r$ such that $q+r \equiv 0\pmod{11}$ . Another way to think about it is the number of possible values of q when r, the remainder, is $0$ . In this case, q itself has to be a multiple of $11$ . $\left\lfloor \frac{999}{11} = 90 \right\rfloor$ . Then we'll need to subtract $9$ from $90$ since we only want multiples of $11$ greater than $100$ $(90-9=81)$
Therefore, the number of possible values of $n$ such that $q+r \equiv 0\pmod{11}$ is $900\cdot9+81\cdot1=8181 \rightarrow B$ .

## Solution 3
Let $n$ equal $\overline{abcde}$ , where $a$ through $e$ are digits. Therefore,
$q=\overline{abc}=100a+10b+c$
$r=\overline{de}=10d+e$
We now take $q+r\bmod{11}$ :
$q+r=100a+10b+c+10d+e\equiv a-b+c-d+e\equiv 0\bmod{11}$
The divisor trick for 11 is as follows:
"Let $n=\overline{a_1a_2a_3\cdots a_x}$ be an $x$ digit integer. If $a_1-a_2+a_3-\cdots +(-1)^{x-1} a_x$ is divisible by $11$ , then $n$ is also divisible by $11$ ."
Therefore, the five-digit number $n$ is divisible by 11. The 5-digit multiples of 11 range from $910\cdot 11$ to $9090\cdot 11$ . There are $8181\Rightarrow \mathrm{(B)}$ divisors of 11 between those inclusive.

## Solution 4
Since $q$ is a quotient and $r$ is a remainder when $n$ is divided by $100$ . So we have $n=100q+r$ . Since we are counting choices where $q+r$ is divisible by $11$ , we have $n=99q+q+r=99q+11k$ for some $k$ . This means that $n$ is the sum of two multiples of $11$ and would thus itself be a multiple of $11$ . Then we can count all the five-digit multiples of $11$ as in Solution 2. (This solution is essentially the same as Solution 3, but it does not necessarily involve mods and so could potentially be faster.)

## Solution 5
Defining $q$ and $r$ in terms of floor functions and $n$ would yield: $q=\left \lfloor \frac{n}{100} \right \rfloor$ and $r=n-100 \left \lfloor \frac{n}{100} \right \rfloor$ . Since $q+r \equiv 0\pmod{11}$ , $\left \lfloor \frac{n}{100} \right \rfloor + n-100 \left \lfloor \frac{n}{100} \right \rfloor \equiv 0\pmod{11}$ . Simplifying gets us $n-99 \left \lfloor \frac{n}{100} \right \rfloor\equiv 0\pmod{11} \rightarrow n \equiv 0\pmod{11}$ ( $99 \left \lfloor \frac{n}{100} \right \rfloor\equiv 0\pmod{11}$ is always true since floor function always yields an integer, and 99 is divisible by 11 w/o any remainder). After we come to this conclusion, it becomes easy to solve the rest of the problem ( $\left \lfloor \frac{n}{99999} \right \rfloor - \left \lfloor \frac{n}{10000} \right \rfloor$ ). ~hw21

## Video Solution 1
https://youtu.be/OpGHj-B0_hg?t=672
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .