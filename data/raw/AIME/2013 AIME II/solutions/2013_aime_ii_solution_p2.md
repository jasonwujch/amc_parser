# 2013 AIME II Problem 2

## Problem

Positive integers $a$ and $b$ satisfy the condition \[\log_2(\log_{2^a}(\log_{2^b}(2^{1000}))) = 0.\] Find the sum of all possible values of $a+b$ .

## Solution 1
To simplify, we write this logarithmic expression as an exponential one. Just looking at the first log, it has a base of 2 and an argument of the expression in parenthesis. Therefore, we can make 2 the base, 0 the exponent, and the argument the result. That means $\log_{2^a}(\log_{2^b}(2^{1000}))=1$ (because $2^0=1$ ). Doing this again, we get $\log_{2^b}(2^{1000})=2^a$ . Doing the process one more time, we finally eliminate all of the logs, getting ${(2^{b})}^{(2^a)}=2^{1000}$ . Using the property that ${(a^x)^{y}}=a^{xy}$ , we simplify to $2^{b\cdot2^{a}}=2^{1000}$ . Eliminating equal bases leaves $b\cdot2^a=1000$ . The largest $a$ such that $2^a$ divides $1000$ is $3$ , so we only need to check $1$ , $2$ , and $3$ . When $a=1$ , $b=500$ ; when $a=2$ , $b=250$ ; when $a=3$ , $b=125$ . Summing all the $a$ 's and $b$ 's gives the answer of $\boxed{881}$ .
Note that $a$ cannot be $0,$ since that would cause the $\log_{2^a}$ to have a $1$ in the base, which is not possible (also the problem specifies that $a$ and $b$ are positive).

## Solution 2
We proceed as in Solution 1, raising $2$ to both sides to achieve $\log_{2^a}(\log_{2^b}(2^{1000})) = 1.$ We raise $2^a$ to both sides to get $\log_{2^b}(2^{1000})=2^a$ , then simplify to get $\dfrac{1000}b=2^a$ .
At this point, we want both $a$ and $b$ to be integers. Thus, $2^a$ can only be a power of $2$ . To help us see the next step, we factorize $1000$ : $\dfrac{2^35^3}b=2^a.$ It should be clear that $a$ must be from $1$ to $3$ ; when $a=1$ , $b=500$ ; when $a=2$ , $b=250$ ; and finally, when $a=3$ , $b=125.$ We sum all the pairs to get $\boxed{881}.$
~Technodoggo

## Video Solution
https://youtu.be/zf9ld5KL_g4
~Lucas
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .