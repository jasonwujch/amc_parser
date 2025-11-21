# 2021 AMC 10B Problem 16

## Problem

Call a positive integer an uphill integer if every digit is strictly greater than the previous digit. For example, $1357, 89,$ and $5$ are all uphill integers, but $32, 1240,$ and $466$ are not. How many uphill integers are divisible by $15$ ?

$\textbf{(A)} ~4 \qquad\textbf{(B)} ~5 \qquad\textbf{(C)} ~6 \qquad\textbf{(D)} ~7 \qquad\textbf{(E)} ~8$

## Solution 1
The divisibility rule of $15$ is that the number must be congruent to $0$ mod $3$ and congruent to $0$ mod $5$ . Being divisible by $5$ means that it must end with a $5$ or a $0$ . We can rule out the case when the number ends with a $0$ immediately because the only integer that is uphill and ends with a $0$ is $0$ which is not positive. So now we know that the number ends with a $5$ . Looking at the answer choices, the answer choices are all pretty small, so we can generate all of the numbers that are uphill and are divisible by $3$ . These numbers are $15, 45, 135, 345, 1245, 12345$ , or $\boxed{\textbf{(C)} ~6}$ numbers.
~ilikemath40

## Solution 2
First, note how the number must end in either $5$ or $0$ in order to satisfying being divisible by $15$ . However, the number can't end in $0$ because it's not strictly greater than the previous digits. Thus, our number must end in $5$ . We do casework on the number of digits.
Case 1: $1$ digit. No numbers work, so $0$ numbers.
Case 2: $2$ digits. We have the numbers $15, 45,$ and $75$ , but $75$ isn't an uphill number, so $2$ numbers
Case 3: $3$ digits. We have the numbers $135, 345$ , so $2$ numbers.
Case 4: $4$ digits. We have the numbers $1235, 1245$ and $2345$ , but only $1245$ satisfies this condition, so $1$ number.
Case 5: $5$ digits. We have only $12345$ , so $1$ number.
Adding these up, we have $2+2+1+1=\boxed{\textbf{(C)} ~6}$ .
~JustinLee2017

## Solution 3
Like solution 2, we can proceed by using casework. A number is divisible by $15$ if is divisible by $3$ and $5.$ In this case, the units digit must be $5,$ otherwise no number can be formed.
Case 1: sum of digits = 6
There is only one number, $15.$
Case 2: sum of digits = 9
There are two numbers: $45$ and $135.$
Case 3: sum of digits = 12
There are two numbers: $345$ and $1245.$
Case 4: sum of digits = 15
There is only one number, $12345.$
We can see that we have exhausted all cases, because in order to have a larger sum of digits, then a number greater than $5$ needs to be used, breaking the conditions of the problem. The answer is $\boxed{\textbf{(C)} ~6}.$
~coolmath34

## Solution 4
An integer is divisible by $15$ if it is divisible by $3$ and $5$ . Divisibility by $5$ means ending in $0$ or $5$ , but since no digit is less than $0$ , the only uphill integer ending in $0$ could be $0$ , which is not positive. This means the integer must end in $5$ .
All uphill integers ending in $5$ are formed by picking any subset of the sequence $(1,2,3,4)$ of digits (keeping their order), then appending a $5$ . Divisibility by $3$ means the sum of the digits is a multiple of $3$ , so our choice of digits must add to $0$ modulo $3$ .
$5 \equiv -1 \pmod{3}$ , so the other digits we pick must add to $1$ modulo $3$ . Since $(1,2,3,4) \equiv (1,-1,0,1) \pmod{3}$ , we can pick either nothing, or one residue $1$ (from $1$ or $4$ ) and one residue $-1$ (from $2$ ), and we can then optionally add a residue $0$ (from $3$ ). This gives $(1+2\cdot1)\cdot2 = \boxed{\textbf{(C)}~6}$ possibilities.
~ emerald_block

## Solution 5 (Solution 2 but more in depth)
First, by intuition note how the number must end in either $5$ or $0$ in order to satisfying being divisible by $15$ . However, the number can't end in $0$ because it's not greater than the previous digits and it has to be positive. Thus, our number must end in $5$ . Now we can do casework on the number of digits.
Case 1: $1$ digit. Only $0$ is a a $1$ digit number that is divisible by $15$ but it must be positive, so $0$ numbers.
Case 2: $2$ digits. We have to find numbers that end in $5$ and is divisible by $3$ , so we get $15, 45,$ and $75$ , but $75$ isn't an uphill number, so we only have $2$ numbers.
Case 3: $3$ digits. Finding $3$ digits is the same as removing $2$ digits that add to a multiple off $3$ from $12345$ , so we can remove $24$ and $15$ becoming $135$ and $234$ respectively, so we have $2$ numbers.
Case 4: $4$ digits. This is the same as removing one multiple of $3$ from $12345$ so removing $3$ becomes $1245$ , so we have $1$ number.
Case 5: $5$ digits. We have only $12345$ , so $1$ number.
Adding these up, we have $2+2+1+1=\boxed{\textbf{(C)} ~6}$ .
~ T3CHN0B14D3
Note: This is my first solution so please forgive me for any errors, thank you.
### Note
The number of "uphill" positive integers as specified in the problem is 511.

## Video Solution (🚀Solved in 3 minutes and 2 seconds🚀)
https://youtu.be/c54455_3Xcc
Education, the Study of Everything

## Video Solution by OmegaLearn (Using Divisibility Rules and Casework)
https://youtu.be/n2FnKxFSW94
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/FV9AnyERgJQ
~IceMatrix

## Video Solution by Interstigation
https://youtu.be/9ZlJTVhtu_s
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .