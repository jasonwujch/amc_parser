# 2023 AIME I Problem 7

## Problem

Call a positive integer $n$ extra-distinct if the remainders when $n$ is divided by $2, 3, 4, 5,$ and $6$ are distinct. Find the number of extra-distinct positive integers less than $1000$ .

## Solution 1
$n$ can either be $0$ or $1$ (mod $2$ ).
Case 1: $n \equiv 0 \pmod{2}$
Then, $n \equiv 2 \pmod{4}$ , which implies $n \equiv 1 \pmod{3}$ and $n \equiv 4 \pmod{6}$ , and therefore $n \equiv 3 \pmod{5}$ . Using CRT , we obtain $n \equiv 58 \pmod{60}$ , which gives $16$ values for $n$ .
Case 2: $n \equiv 1 \pmod{2}$
$n$ is then $3 \pmod{4}$ . If $n \equiv 0 \pmod{3}$ , $n \equiv 3 \pmod{6}$ , a contradiction. Thus, $n \equiv 2 \pmod{3}$ , which implies $n \equiv 5 \pmod{6}$ . $n$ can either be $0 \pmod{5}$ , which implies that $n \equiv 35 \pmod{60}$ by CRT, giving $17$ cases; or $4 \pmod{5}$ , which implies that $n \equiv 59 \pmod{60}$ by CRT, giving $16$ cases.
The total number of extra-distinct numbers is thus $16 + 16 + 17 = \boxed{049}$ .
~mathboy100

## Solution 2 (Simpler)
Because the LCM of all of the numbers we are dividing by is $60$ , we know that all of the remainders are $0$ again at $60$ , meaning that we have a cycle that repeats itself every $60$ numbers.
After listing all of the remainders up to $60$ , we find that $35$ , $58$ , and $59$ are extra-distinct. So, we have $3$ numbers every $60$ which are extra-distinct. $60\cdot16 = 960$ and $3\cdot16 = 48$ , so we have $48$ extra-distinct numbers in the first $960$ numbers. Because of our pattern, we know that the numbers from $961$ thru $1000$ will have the same remainders as $1$ thru $40$ , so we have $1$ other extra-distinct number ( $35$ ).
$48 + 1 = \boxed{049}$ .
~Algebraik

## Solution 3
$\textbf{Case 0: } {\rm Rem} \ \left( n, 6 \right) = 0$ .
We have ${\rm Rem} \ \left( n, 2 \right) = 0$ . This violates the condition that $n$ is extra-distinct. Therefore, this case has no solution.
$\textbf{Case 1: } {\rm Rem} \ \left( n, 6 \right) = 1$ .
We have ${\rm Rem} \ \left( n, 2 \right) = 1$ . This violates the condition that $n$ is extra-distinct. Therefore, this case has no solution.
$\textbf{Case 2: } {\rm Rem} \ \left( n, 6 \right) = 2$ .
We have ${\rm Rem} \ \left( n, 3 \right) = 2$ . This violates the condition that $n$ is extra-distinct. Therefore, this case has no solution.
$\textbf{Case 3: } {\rm Rem} \ \left( n, 6 \right) = 3$ .
The condition ${\rm Rem} \ \left( n, 6 \right) = 3$ implies ${\rm Rem} \ \left( n, 2 \right) = 1$ , ${\rm Rem} \ \left( n, 3 \right) = 0$ .
Because $n$ is extra-distinct, ${\rm Rem} \ \left( n, l \right)$ for $l \in \left\{ 2, 3, 4 \right\}$ is a permutation of $\left\{ 0, 1 ,2 \right\}$ . Thus, ${\rm Rem} \ \left( n, 4 \right) = 2$ .
However, ${\rm Rem} \ \left( n, 4 \right) = 2$ conflicts ${\rm Rem} \ \left( n, 2 \right) = 1$ . Therefore, this case has no solutions.
$\textbf{Case 4: } {\rm Rem} \ \left( n, 6 \right) = 4$ .
The condition ${\rm Rem} \ \left( n, 6 \right) = 4$ implies ${\rm Rem} \ \left( n, 2 \right) = 0$ and ${\rm Rem} \ \left( n, 3 \right) = 1$ .
Because $n$ is extra-distinct, ${\rm Rem} \ \left( n, l \right)$ for $l \in \left\{ 2, 3, 4 , 5 \right\}$ is a permutation of $\left\{ 0, 1 ,2 , 3 \right\}$ .
Because ${\rm Rem} \ \left( n, 2 \right) = 0$ , we must have ${\rm Rem} \ \left( n, 4 \right) = 2$ . Hence, ${\rm Rem} \ \left( n, 5 \right) = 3$ .
Hence, $n \equiv -2 \pmod{{\rm lcm} \left( 4, 5 , 6 \right)}$ . Hence, $n \equiv - 2 \pmod{60}$ .
We have $1000 = 60 \cdot 16 + 40$ . Therefore, the number of extra-distinct $n$ in this case is 16.
$\textbf{Case 5: } {\rm Rem} \ \left( n, 6 \right) = 5$ .
The condition ${\rm Rem} \ \left( n, 6 \right) = 5$ implies ${\rm Rem} \ \left( n, 2 \right) = 1$ and ${\rm Rem} \ \left( n, 3 \right) = 2$ .
Because $n$ is extra-distinct, ${\rm Rem} \ \left( n, 4 \right)$ and ${\rm Rem} \ \left( n, 5 \right)$ are two distinct numbers in $\left\{ 0, 3, 4 \right\}$ . Because ${\rm Rem} \ \left( n, 4 \right) \leq 3$ and $n$ is odd, we have ${\rm Rem} \ \left( n, 4 \right) = 3$ . Hence, ${\rm Rem} \ \left( n, 5 \right) = 0$ or 4.
$\textbf{Case 5.1: } {\rm Rem} \ \left( n, 6 \right) = 5$ , ${\rm Rem} \ \left( n, 4 \right) = 3$ , ${\rm Rem} \ \left( n, 5 \right) = 0$ .
We have $n \equiv 35 \pmod{60}$ .
We have $1000 = 60 \cdot 16 + 40$ . Therefore, the number of extra-distinct $n$ in this subcase is 17.
$\textbf{Case 5.2: } {\rm Rem} \ \left( n, 6 \right) = 5$ , ${\rm Rem} \ \left( n, 4 \right) = 3$ , ${\rm Rem} \ \left( n, 5 \right) = 4$ .
$n \equiv - 1 \pmod{60}$ .
We have $1000 = 60 \cdot 16 + 40$ . Therefore, the number of extra-distinct $n$ in this subcase is 16.
Putting all of the cases together, the total number of extra-distinct $n$ is $16 + 17 + 16 = \boxed{049}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com) \[\] ~minor formatting changes by PojoDotCom

## Solution 4 (Small addition to solution 2)
We need to find that $35$ , $58$ , and $59$ are all extra-distinct numbers smaller than $61.$
Let $k \in \left\{2, 3, 4, 5, 6 \right\}.$ Denote the remainder in the division of $a$ by $b$ as ${\rm Rem} \ \left( a, b \right).$
${\rm Rem} \ \left( -1, k \right) = k - 1 \implies {\rm Rem} \ \left( 59, k \right) = k - 1 = \left\{1, 2, 3, 4, 5 \right\}\implies 59$ is extra-distinct. ${\rm Rem} \ \left( -2, k \right) = k - 2 \implies {\rm Rem} \ \left( 58, k \right) = k - 2 = \left\{0, 1, 2, 3, 4 \right\} \implies 58$ is extra-distinct. \[{\rm Rem} \ \left( x + 12y, k \right) = {\rm Rem} \ \left(x, k \right) + \left\{0, 0, 0, {\rm Rem} \ \left(12y, k \right), 0 \right\}.\] We need to check all of the remainders up to $12 - 3 = 9$ and remainders \[{\rm Rem} \ \left( 59 - 12, k \right) = {\rm Rem} \ \left( 59 - 36, k \right) = \left\{1, 2, 3, 3, 5 \right\}, {\rm Rem} \ \left( 59 - 48, k \right) = \left\{1, 2, 3, 1, 5 \right\},\] ${\rm Rem} \ \left( 59 - 24, k \right) ={\rm Rem} \ \left(35, k \right) = \left\{1, 2, 3, 0, 5 \right\} \implies 35$ is extra-distinct. $58 - 12 = 46 \implies {\rm Rem} \ \left( 46, 5 \right) = 1 = {\rm Rem} \ \left( 46, 3 \right),$ $58 - 24 = 34 \implies {\rm Rem} \ \left( 34, 5 \right) = 4 = {\rm Rem} \ \left( 34, 6 \right),$ $58 - 36 = 22 \implies {\rm Rem} \ \left( 22, 5 \right) = 2 = {\rm Rem} \ \left( 22, 4 \right),$ $58 - 48 = 10 \implies {\rm Rem} \ \left( 10, 5 \right) = 0 = {\rm Rem} \ \left( 10, 2 \right).$
vladimir.shelomovskii@gmail.com, vvsss

## Video Solution
https://youtu.be/8oOik9d1fWM
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .